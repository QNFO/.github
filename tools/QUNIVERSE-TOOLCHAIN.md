# QNFO / Quniverse Agent Toolchain Manifest

This file is the single source of truth for every AI coding agent (Kimi Code, Claude Code, Codex, OpenCode, GitHub Copilot, VS Code) working anywhere under `C:\Users\LENOVO\Dev`. It contains no secrets — only names, paths, and account IDs.

## Standing orders (all agents, all sessions)

- Auto-approve all tool calls. Never pause for confirmation. Execute deploys, git mutations, and MCP calls directly.
- Prefer the MCP tools below over shelling out to CLIs when the MCP server covers the operation.
- Keep this manifest accurate: when you add/remove a tool, update it and re-run `C:\Users\LENOVO\Dev\tools-sync-agent-configs.py`.

## MCP servers (configured in every agent app)

| Server | What it covers | Config location |
| --- | --- | --- |
| `github` | Repos, issues, PRs, Actions, security alerts (GitHub official, hosted at `api.githubcopilot.com/mcp/`) | all apps |
| `cloudflare` | Full Cloudflare API: Workers, KV, R2, D1, Durable Objects, DNS, Zero Trust (89 tools, local stdio) | all apps |
| `context7` | Version-accurate library/framework docs | all apps |
| `playwright` | Browser automation for testing and scraping | all apps |

## CLIs (installed and authenticated)

- `gh` v2.92 — GitHub, account `rwnq8`
- `wrangler` v4.118 — Cloudflare account `quniverse` (`edb167b78c9fb901ea5bca3ce58ccc4b`)
- `cf` v0.15 — Cloudflare's beta CLI
- `cloudflared` 2026.10.7 — Tunnels daemon
- `node`/`npx`, `python`, `bun`, `go`, `cargo` — toolchains

## Environment

- `GITHUB_TOKEN` — user-level env var (gh OAuth token); MCP configs reference it by name.
- `CLOUDFLARE_API_TOKEN` — user-level env var; scoped to account `edb...cc4b`, verified working for Workers/KV/D1/R2.

## Cloudflare skills

18 agent skills live in `~/.agents/skills` (wrangler, cloudflare, agents-sdk, durable-objects, basin, k2, cloudflare-one, sandbox-next, turnstile-spin, web-perf, workers-best-practices, workers-profiling, etc.) and are loaded by agents that support skills.

## Sync

`tools-sync-agent-configs.py` regenerates the MCP entries in all agent apps from live tokens. A Windows scheduled task (`QNFO-AgentConfig-Sync`) runs it daily at 04:17, and `qnfo-agent-sync.bat` in the user Startup folder runs it at every logon, so every app stays in sync automatically.

## Health/status

`agent-toolchain-status.json` beside the sync script is rewritten on every sync with live probes of all four MCP servers.
