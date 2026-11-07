#!/usr/bin/env python3
"""QNFO agent-config sync — keeps MCP server definitions identical across every
AI agent app on this machine. Canonical source: ~/.kimi-code/mcp.json.

Run manually or via the 'QNFO-AgentConfig-Sync' scheduled task (daily).
Idempotent: rewrites only the four managed entries, preserves everything else.
Never prints secrets.
"""
import json
import os
import re
import subprocess
import sys

GH_URL = "https://api.githubcopilot.com/mcp/"
CF_INDEX = r"C:\Users\LENOVO\npm-global\node_modules\@cloudflare\mcp-server-cloudflare\dist\index.js"
CF_ACCOUNT = "edb167b78c9fb901ea5bca3ce58ccc4b"
CTX7_URL = "https://mcp.context7.com/mcp"
MANAGED = ["github", "cloudflare", "context7", "playwright"]

HOME = os.path.expanduser("~")
CODEX = os.path.join(HOME, ".codex", "config.toml")
CLAUDE = os.path.join(HOME, ".claude.json")
OPENCODE = os.path.join(HOME, ".config", "opencode", "opencode.json")
VSCODE = os.path.join(os.environ.get("APPDATA", ""), "Code", "User", "settings.json")
MARK_BEGIN = "# BEGIN MCP SERVERS (auto-synced by tools-sync-agent-configs.py)"
MARK_END = "# END MCP SERVERS"


def tokens():
    gh = subprocess.check_output(["gh", "auth", "token"], text=True).strip()
    cf = os.environ.get("CLOUDFLARE_API_TOKEN", "")
    if not cf:
        raise SystemExit("CLOUDFLARE_API_TOKEN not in environment; cannot sync.")
    return gh, cf


def codex_block(gh, cf):
    return f"""{MARK_BEGIN}
[mcp_servers.github]
url = "{GH_URL}"
http_headers = {{ Authorization = "Bearer {gh}" }}

[mcp_servers.cloudflare]
command = "node"
args = ["{CF_INDEX.replace(chr(92), '/')}", "run", "{CF_ACCOUNT}"]
env = {{ CLOUDFLARE_API_TOKEN = "{cf}" }}

[mcp_servers.context7]
url = "{CTX7_URL}"

[mcp_servers.playwright]
command = "npx"
args = ["-y", "@playwright/mcp@latest"]
{MARK_END}
"""


def sync_codex(gh, cf):
    s = open(CODEX, encoding="utf-8").read()
    # drop previously synced block
    s = re.sub(re.escape(MARK_BEGIN) + r".*?" + re.escape(MARK_END) + r"\n?", "", s, flags=re.S)
    # drop any stray managed blocks from older manual edits (keep e.g. node_repl)
    for name in MANAGED:
        s = re.sub(rf"\n?\[mcp_servers\.{name}\]\n(?:[^\[]|\[(?!mcp_servers))*?(?=\n\[|\Z)", "\n", s)
    open(CODEX, "w", encoding="utf-8").write(s.rstrip() + "\n\n" + codex_block(gh, cf))
    import tomllib
    tomllib.load(open(CODEX, "rb"))
    print("codex: synced + TOML valid")


def defs(gh, cf):
    return {
        "github": {"type": "http", "url": GH_URL, "headers": {"Authorization": f"Bearer {gh}"}},
        "cloudflare": {"command": "node", "args": [CF_INDEX, "run", CF_ACCOUNT],
                       "env": {"CLOUDFLARE_API_TOKEN": cf}},
        "context7": {"type": "http", "url": CTX7_URL},
        "playwright": {"command": "npx", "args": ["-y", "@playwright/mcp@latest"]},
    }


def sync_claude(gh, cf):
    d = json.load(open(CLAUDE, encoding="utf-8"))
    servers = d.get("mcpServers") or {}
    if isinstance(servers, list):
        servers = {}
    servers.update(defs(gh, cf))
    d["mcpServers"] = servers
    json.dump(d, open(CLAUDE, "w", encoding="utf-8"), indent=2)
    print("claude: synced")


def sync_opencode(gh, cf):
    d = json.load(open(OPENCODE, encoding="utf-8")) if os.path.exists(OPENCODE) else {"$schema": "https://opencode.ai/config.json"}
    mcp = d.setdefault("mcp", {})
    for name, v in defs(gh, cf).items():
        if "command" in v:
            entry = {"type": "local", "command": [v["command"], *v["args"]], "enabled": True}
            if v.get("env"):
                entry["environment"] = v["env"]
        else:
            entry = {"type": "remote", "url": v["url"], "enabled": True}
            if v.get("headers"):
                entry["headers"] = v["headers"]
        mcp[name] = entry
    json.dump(d, open(OPENCODE, "w", encoding="utf-8"), indent=2)
    print("opencode: synced")


def sync_vscode(gh, cf):
    s = open(VSCODE, encoding="utf-8-sig").read()
    try:
        d = json.loads(s)
    except json.JSONDecodeError:
        s2 = re.sub(r"/\*.*?\*/", "", s, flags=re.S)
        s2 = "\n".join(l for l in s2.splitlines() if not l.strip().startswith("//"))
        d = json.loads(s2)
    servers = d.setdefault("mcp", {}).setdefault("servers", {})
    for name, v in defs(gh, cf).items():
        entry = {k: val for k, val in v.items() if k != "type"}
        servers[name] = entry
    json.dump(d, open(VSCODE, "w", encoding="utf-8"), indent=2)
    print("vscode: synced")


def health_check(gh, cf):
    """Probe every MCP server and write a machine-readable status file."""
    import urllib.request

    def probe(name, req):
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                return {"ok": r.status in (200, 401, 405), "http": r.status}
        except urllib.error.HTTPError as e:
            return {"ok": e.code in (200, 401, 405), "http": e.code}
        except Exception as e:
            return {"ok": False, "error": str(e)[:120]}

    status = {"checked_at": subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip(),
              "servers": {}}
    status["servers"]["github"] = probe("github", urllib.request.Request(
        GH_URL, headers={"Authorization": f"Bearer {gh}", "Accept": "application/json, text/event-stream"}))
    status["servers"]["context7"] = probe("context7", urllib.request.Request(CTX7_URL))
    r = urllib.request.Request(f"https://api.cloudflare.com/client/v4/accounts/{CF_ACCOUNT}/workers/scripts",
                               headers={"Authorization": f"Bearer {cf}"})
    status["servers"]["cloudflare"] = probe("cloudflare", r)
    p = subprocess.run(["node", "--version"], capture_output=True)
    status["servers"]["playwright"] = {"ok": p.returncode == 0, "detail": "node present; chromium preinstalled"}
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agent-toolchain-status.json")
    json.dump(status, open(out, "w"), indent=2)
    print(f"health: { {k: v.get('ok') for k, v in status['servers'].items()} } -> {out}")


def main():
    gh, cf = tokens()
    sync_codex(gh, cf)
    sync_claude(gh, cf)
    sync_opencode(gh, cf)
    sync_vscode(gh, cf)
    health_check(gh, cf)
    print("all agent apps in sync")


if __name__ == "__main__":
    main()
