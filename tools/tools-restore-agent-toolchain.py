#!/usr/bin/env python3
"""Restore the Quniverse agent toolchain on a fresh/wiped machine.

Recreates the machine-local config that cannot live in git (~/.kimi-code/mcp.json,
Windows scheduled task, Startup sync hook) from the canonical copies in this repo
plus live tokens from the environment. Idempotent.

Prerequisites on the fresh machine: gh (authenticated), node/npm, python,
CLOUDFLARE_API_TOKEN and GITHUB_TOKEN set as user env vars.

Usage: python tools-restore-agent-toolchain.py
"""
import json
import os
import subprocess
import sys

REPO_TOOLS = os.path.dirname(os.path.abspath(__file__))
DEV = os.path.normpath(os.path.join(REPO_TOOLS, "..", ".."))
HOME = os.path.expanduser("~")
CF_ACCOUNT = "edb167b78c9fb901ea5bca3ce58ccc4b"
CF_INDEX = os.path.join(HOME, "npm-global", "node_modules", "@cloudflare",
                        "mcp-server-cloudflare", "dist", "index.js")


def tokens():
    gh = subprocess.check_output(["gh", "auth", "token"], text=True).strip()
    cf = os.environ.get("CLOUDFLARE_API_TOKEN", "")
    if not cf:
        sys.exit("CLOUDFLARE_API_TOKEN not in environment.")
    return gh, cf


def step(msg):
    print(f"[restore] {msg}")


def install_cloudflare_server():
    if not os.path.exists(CF_INDEX):
        step("installing @cloudflare/mcp-server-cloudflare globally")
        subprocess.run(["npm", "install", "-g", "@cloudflare/mcp-server-cloudflare"], check=True)


def kimi_mcp(gh, cf):
    path = os.path.join(HOME, ".kimi-code", "mcp.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    d = {
        "mcpServers": {
            "github": {"url": "https://api.githubcopilot.com/mcp/",
                       "bearerTokenEnvVar": "GITHUB_TOKEN"},
            "cloudflare": {"command": "node",
                           "args": [CF_INDEX, "run", CF_ACCOUNT],
                           "env": {"CLOUDFLARE_API_TOKEN": cf},
                           "startupTimeoutMs": 60000},
            "context7": {"url": "https://mcp.context7.com/mcp"},
            "playwright": {"command": "npx", "args": ["-y", "@playwright/mcp@latest"],
                           "startupTimeoutMs": 120000},
        }
    }
    json.dump(d, open(path, "w"), indent=2)
    step(f"wrote {path}")


def scheduled_task():
    py = sys.executable
    sync = os.path.join(DEV, "tools-sync-agent-configs.py")
    if not os.path.exists(sync):
        sync = os.path.join(REPO_TOOLS, "tools-sync-agent-configs.py")
    subprocess.run(["schtasks", "/Create", "/TN", "QNFO-AgentConfig-Sync",
                    "/TR", f'"{py}" "{sync}"', "/SC", "DAILY", "/ST", "04:17", "/F"],
                   capture_output=True)
    step("scheduled task QNFO-AgentConfig-Sync (daily 04:17)")


def startup_hook():
    bat = os.path.join(os.environ.get("APPDATA", ""),
                       "Microsoft", "Windows", "Start Menu", "Programs", "Startup",
                       "qnfo-agent-sync.bat")
    py = os.path.join(os.path.dirname(sys.executable), "pythonw.exe")
    sync = os.path.join(DEV, "tools-sync-agent-configs.py")
    if not os.path.exists(sync):
        sync = os.path.join(REPO_TOOLS, "tools-sync-agent-configs.py")
    with open(bat, "w") as f:
        f.write(f'@echo off\n"{py}" "{sync}" >> "{DEV}\\agent-sync.log" 2>&1\n')
    step(f"startup hook -> {bat}")


def main():
    gh, cf = tokens()
    install_cloudflare_server()
    kimi_mcp(gh, cf)
    scheduled_task()
    startup_hook()
    step("done. Now run: python " + os.path.join(REPO_TOOLS, "tools-sync-agent-configs.py"))


if __name__ == "__main__":
    main()
