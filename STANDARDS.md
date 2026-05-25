# STANDARDS.md — Cross-Project Conventions and Governance

**Version:** v1.0
**Date:** 2026-05-21
**Audience:** All projects in the prompts ecosystem
**Authority:** Human orchestrator
**Enforcement:** `template_compliance.py` + `system_audit.py`

---

## 1. Architecture Principle

> **"The simplest possible stack works. No orchestration framework. No multi-agent simulation. No cloud infrastructure."** — Force-Multiplier Playbook §4

The human is the orchestrator. The LLM is the execution engine. Structural gates prevent known failures. Templates enforce consistency. Scripts automate cross-project tasks. There are zero management agents.

---

## 2. Document Naming Conventions

### Project Files

| Artifact | Filename | Format |
|:---------|:---------|:-------|
| Project charter | `PROJECT-CHARTER.md` | From PROJECT-CHARTER-TEMPLATE.md |
| Sprint backlog | `SPRINT-BACKLOG.md` | From SPRINT-BACKLOG-TEMPLATE.md |
| Product backlog | `PRODUCT-BACKLOG.md` | MoSCoW-prioritized |
| Changelog | `CHANGELOG.md` | keepachangelog.com format |
| Risk register | `RISK-REGISTER.md` | From RISK-REGISTER-TEMPLATE.md |
| Definition of Done | `DEFINITION-OF-DONE.md` | Per-task-type criteria |
| Architecture decisions | `docs/adr/NNNN-lowercase-title.md` | Nygard ADR format |
| Sprint retrospectives | `docs/retrospectives/YYYY-MM-DD-sprint-name.md` | From RETROSPECTIVE-TEMPLATE.md |
| Versioned content | `0.N.md`, `0.N.py` | Chronological, PERMANENT |
| Helper scripts | `_descriptive_name.py` | Ephemeral, delete when done |
| Publications | `Descriptive Title — Subtitle.md` | Per §11.1 |

### Project Directory

```
projects/YYYY/MM/kebab-case-name/
```

### Archive

```
Archive/projects/YYYY/MM/kebab-case-name/
```

### Releases

```
G:\My Drive\Obsidian\releases\YYYY\MM\descriptive-filename.md
```

---

## 3. Documentation Status Labels (§0.10)

All system documentation MUST use status labels on every major section:

| Label | Meaning | Agent Behavior |
|:------|:--------|:---------------|
| `[BINDING]` | Enforced. Violation = hard stop. | Must follow |
| `[BEST-EFFORT]` | Should be followed. Violation = flag only. | Best attempt |
| `[HISTORICAL]` | Prior state. Do not act on it. | Read for context only |
| `[ASPIRATIONAL]` | Desired state not yet implemented. | Do not treat as available |
| `[DEPRECATED]` | Scheduled for removal. | Avoid; migrate away |

Example:
```
## §9 Git Protocol [BINDING]
## §11.3 Curly Quote Standard [BEST-EFFORT]
```

At session start, agents must scan for `[ASPIRATIONAL]` and `[HISTORICAL]` labels and treat those sections as non-actionable context.

---

## 4. Git Standards

### Branch Naming
```
feature/kebab-case-description
```

### Commit Format
```
ACTION:[CREATE|EDIT|DELETE] FILE: path/to/file.ext RATIONALE:reason
```

### Branch Lifecycle
- Created at project initialization
- Merged to main at project close-out
- Deleted after merge
- Never reused across projects

### Required Files
- `.gitignore` (created at initialization with: `__pycache__/`, `*.pyc`, `*.pyo`, `.DS_Store`, `Thumbs.db`)

---

## 5. File Lifecycle Classification (§10.6)

| Category | Examples | Rule |
|:---------|:---------|:-----|
| **PERMANENT** | 0.N.md, 0.N.py, mandatory docs, core libraries | NEVER DELETE |
| **EPHEMERAL** | _fix_quotes.py, _audit_*.py, _temp_*.py | Delete when workflow complete and verified |
| **EXTERNAL** | Publication documents (descriptive filenames) | Copy to releases; keep project copy |

---

## 6. Publication Standards (§11)

### Minimum Requirements
- YAML frontmatter (author, ORCID, title, date)
- Curly quotes throughout body text (Python scan verification)
- Publication Language Gate: zero internal project language hits
- Standalone: zero references to project files, sprints, modules
- Reader testing: 2 rounds minimum
- DOI resolved (no [DOI-PENDING] placeholders)
- Copy in `G:\My Drive\Obsidian\releases\YYYY\MM\`

### Language Gate Categories (BLOCKING if any hit)
- Sprint/task references ("Module 0", "Task 4", "SPRINT")
- File management references ("0.3.py", "PROJECT STATE")
- Developer notes ("self-test", "Cross-Project: YES")
- Tooling references ("cp1252", "Unicode box")
- Process references ("ready for handoff", "new agent starting from cold")

---

## 7. CPL Promotion Criteria

A lesson qualifies for CROSS-PROJECT-LEARNINGS.md promotion if:

1. It occurred in at least one project
2. It could recur in another project without structural prevention
3. It is not already documented in CPL (deduplication check)
4. It is tagged `Cross-Project: YES` in a sprint retrospective

Promotion is handled by `promote_cpl.py` — not manual transfer.

---

## 8. Template Compliance

All project files must be created from templates in `prompts/templates/`. No project may invent its own document structure.

Compliance verified by `template_compliance.py` at:
- Project initialization
- Each sprint review
- Project close-out

### Available Templates

| Template | For |
|:---------|:----|
| PROJECT-CHARTER-TEMPLATE.md | Project scope, success criteria, constraints |
| SPRINT-BACKLOG-TEMPLATE.md | Current sprint tasks with DoD checkboxes |
| PRODUCT-BACKLOG-TEMPLATE.md | Future work, MoSCoW prioritized |
| CHANGELOG-TEMPLATE.md | Release notes, keepachangelog.com format |
| RISK-REGISTER-TEMPLATE.md | Known risks with mitigation |
| DEFINITION-OF-DONE-TEMPLATE.md | Completion criteria per task type |
| ADR-TEMPLATE.md | Architecture decisions, Nygard format |
| RETROSPECTIVE-TEMPLATE.md | Sprint retrospectives |
| README-TEMPLATE.md | Project overview |
| CONTRIBUTING-TEMPLATE.md | Agent workflow for the project |
| HANDOFF-TEMPLATE.md | Program→Project, Project→Task, Session→Session |

---

## 9. Automation Scripts

| Script | Function | When |
|:-------|:---------|:-----|
| `system_audit.py` | Verify structural gates present in DEFAULT.md | Session start |
| `promote_cpl.py` | Scan retros, deduplicate, generate CPL candidates | Per sprint |
| `portfolio_status.py` | Scan active projects, generate dashboard | On demand |
| `template_compliance.py` | Verify project files match templates | Project init, sprint review, close-out |

---

## 10. Human Orchestrator Touchpoints

The human is the Portfolio Manager, Program Manager, and Project Manager. These touchpoints are embedded as gates in DEFAULT.md:

| Touchpoint | Gate | Human Decision |
|:-----------|:-----|:---------------|
| Project start | §0.1 | Approve project charter |
| Milestone review | §0.7.1 | Review deliverables; redirect if needed |
| Publication ready | §11.7 | Final editorial review |
| Project close-out | §12 | Sign off; approve archive |
| Portfolio review | PORTFOLIO-DASHBOARD.md | Decide next project |

There is no "quarterly review." The review cadence is per-project close-out — which may be hours or days, not months.

---

## 11. QWAV Program Conventions

QWAV is a specialist domain, not a separate management hierarchy. The human directs QWAV tasks the same way they direct DEFAULT.md tasks — through the Five Phases (Define → Delegate → Execute → Verify → Synthesize).

QWAV-DEFAULT.md inherits all structural gates from DEFAULT.md and adds:
- Physics limit checks (dimension verification, known-limit reduction)
- Mathematical rigor gates (proof verification, assumption audits)
- Domain-specific terminology standards

QWAV project directories follow the same conventions as all other projects.

---

## 12. Compliance and Audit

### Session Start
1. `system_audit.py` — verify all structural gates present
2. `template_compliance.py` — verify project files match templates
3. Read CROSS-PROJECT-LEARNINGS.md — check for new applicable lessons

### Sprint Review
1. DoD checklist verified per task type
2. Publication Language Gate run on any external-facing output
3. `template_compliance.py` run
4. Sprint retrospective filed in `docs/retrospectives/`
5. CPL candidates tagged for `promote_cpl.py`

### Project Close-Out
1. All deliverables meet DoD
2. Publication Language Gate: zero hits
3. Project Name Review (§12.1)
4. All ADRs filed
5. Final retrospective filed
6. Feature branch merged to main, deleted
7. Project archived

---

**This document defines the conventions. DEFAULT.md enforces them structurally. The human decides direction.**

[STANDARDS.md v1.0 — 2026-05-21]
