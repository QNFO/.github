# QNFO / QWAV — Portfolio Inventory (Public Mirror)

> **Source of truth:** QNFO Knowledge Graph (Cloudflare D1 `nodes`/`edges`), snapshot **2026-08-13**.
> **Purpose:** Public, funder-facing mirror of ALL QNFO/QWAV programs, projects, tasks, and
> ongoing activities. GitHub is the transparency ledger; Cloudflare (KG/D1/R2) remains canonical.
> **Regenerate:** see `QNFO/qnfo-ops/SYNC-PORTFOLIO-GITHUB.md` (sync procedure).
> **Live status board:** https://github.com/orgs/QNFO/projects/7

> **Known drift (flagged, not hidden):** the KG lists two active strategic programs — **ACRP**
> (Adelic Core Research Program, ACRP-01..08) and **KEPLER** (10-phase master roadmap) — that are
> not yet assigned WBS codes in `WBS.TAXONOMY.md`. The canonical **Portfolio API**
> (`qnfo-data-api.q08.workers.dev/v2`) was **unreachable (HTTP 404)** at snapshot time; the KG is
> therefore the authoritative source used here.

---

## Programs (21)

| WBS | Program | Slug | GitHub | DOI | Status |
|:----|:--------|:-----|:-------|:----|:-------|
| `QNFO.SR` | Silent Radix Cryptography | `silent-radix` | — | — | active |
| `QNFO.ADL` | Adelic Physics Program | `adelic-physics` | `QNFO/adelic-shannon-theory` | 10.5281/zenodo.21336099 | active |
| `QNFO.PBO` | Pattern-Based Ontology (Autaxys) | `pbo-autaxys` | — | — | active |
| `QNFO.QD` | The Qubit Delusion | `qubit-delusion` | — | — | active |
| `QNFO.UF` | Ultrametric Foundations | `ultrametric-foundations` | — | 10.5281/zenodo.21046993 | active |
| `QNFO.CON` | Cross-Pillar Consilience | `cross-pillar-consilience` | `QNFO/wbs-6-synthesis` | 10.5281/zenodo.21547793 | active |
| `QNFO.CMP` | Computing Machines | `computing-machines` | `QNFO/computing-machines` | — | active |
| `QNFO.JPC` | JPCub Validation | `jpcub-validation` | `QNFO/jpcub-validation` | — | active |
| `QNFO.ODR` | ODR Thesis Program | `odr-thesis` | `QNFO/odr-thesis` | 10.5281/zenodo.21780909 | active |
| `QNFO.CGS` | Consilient Gap Synthesis | `consilient-gap-synthesis` | `QNFO/consilient-gap-synthesis` | 10.5281/zenodo.21782596 | active |
| `QNFO.SLB` | Laws of Form (Spencer-Brown) | `laws-of-form` | `QNFO/laws-of-form` | — | active |
| `QNFO.GOV` | Portfolio Governance & Public Transparency | `governance-transparency` | `QNFO/.github` | — | active |
| `QNFO.INM` | Infomatics | `infomatics` | `QNFO/infomatics` | — | active |
| `QNFO.CFE` | CFPE / Paradigm Engineering | `cfpe` | `QNFO/cfpe` | — | active |
| `QNFO.UMP` | Ultrametric Physics | `ultrametric-physics` | `QNFO/ultrametric-physics` | — | active |
| `QNFO.RES` | QNFO Research Archive | `qnfo-research` | `QNFO/qnfo-research` | — | active |
| `QWAV.PLT` | QWAV Platform | `qwav-platform` | `QNFO/qwav-platform` | — | active |
| `QWAV.DEM` | QWAV Interactive Demos | `qwav-demos` | `QNFO/qwav-demos` | — | active |
| *(KG)* | ACRP — Adelic Core Research Program | `acrp` | — | — | ACTIVE (ACRP-01..08) |
| *(KG)* | KEPLER Program (master roadmap) | `kepler` | — | — | ACTIVE (10 phases / 48 tasks) |
| *(KG)* | qwav (loose node) | `qwav` | — | — | last_active 2026-07-13 |

---

## Ongoing Activities — Open Items (21)

| ID | Title | Status | Priority |
|:---|:------|:-------|:---------|
| OI-001 | Agent Swarm Architecture | STUB | MEDIUM |
| OI-002 | Automated Peer Review | STUB | MEDIUM |
| OI-003 | Consistency Engine | STUB | HIGH |
| OI-004 | Portfolio API | IN-PROGRESS | — |
| OI-005 | Portfolio Infrastructure | ANALYZING | — |
| OI-006 | Reproducibility as Code | STUB | MEDIUM |
| OI-007 | Ultrametric Playground | STUB | LOW |
| OI-008 | QWAV Compute Cloud | STUB | LOW |
| OI-009 | Analytics Infrastructure | BACKLOG | — |
| OI-010 | Knowing Patterns Refactor | BACKLOG | — |
| OI-011 | Prompts Directory Triage | COMPLETED | HIGH |
| OI-012 | Archive Migration Completion | IN-PROGRESS | — |
| OI-013 | Discovery Momentum Assets | PARTIAL | — |
| OI-014 | PM Mirror Builder | STUB | LOW |
| OI-015 | Applications Framework | STUB | LOW |

*(6 additional `task-*` nodes carry label OpenItem in the KG — analytics-infrastructure-01..03 and
knowing-patterns-refactor-01..03, all `pending` — a KG label-drift artifact, noted for cleanup.)*

---

## KEPLER Program — Master Roadmap (Phases 0–10)

The KEPLER program is the umbrella roadmap spanning Silent Radix, Adelic Physics, Ultrametric
Foundations, and Infomatics. **Phase 1 (Ostrowski → Fault Tolerance Proof) is COMPLETE and
published** under the harmonic-adelic-completions program (DOI 10.5281/zenodo.21511271).

| Phase | Name | Priority | Status (tasks) |
|:------|:-----|:---------|:---------------|
| P0 | Master Plan & Infrastructure | P0-CRITICAL | 2 done / 6 pending / 1 in-progress |
| P1 | Ostrowski → Fault-Tolerance Proof | P0-CRITICAL | **COMPLETE (7/7)** |
| P2 | File IP — QEC Patents | P0-CRITICAL | 0/7 pending |
| P3 | Hensel Code v1.3.0 + Software Patent | P1-HIGH | 0/6 pending |
| P4 | Trapped-Ion Page-Wootters Experiment | P1-HIGH | 0/6 pending |
| P5 | Silent Radix + Braided Memory IP | P2-MEDIUM | 0/6 pending |
| P6 | Seed Dimensionless Physics Program | P4-GREENFIELD | 0/6 pending |
| P7 | FMO / p-adic Bridge | P4-GREENFIELD | 0/6 pending |
| P8 | Cross-Cutting Dissemination | P3-LOW | 0/6 pending |
| P9 | Infrastructure Modernization | P3-LOW | 1 done / 1 in-progress / 8 pending |
| P10 | Synthesis — Ecosystem Convergence | P3-LOW | 0/9 pending |

### Phase 1 (COMPLETE — the proof)
- P1-001 Formalize OFT Conjecture — COMPLETED
- P1-002 Prove Key Lemma 1 (error metrics classification) — COMPLETED
- P1-003 Prove Key Lemmas 2–3 (metric insufficiency) — COMPLETED
- P1-004 Counter-example search — COMPLETED
- P1-005 Full proof synthesis — COMPLETED (DOI 10.5281/zenodo.21511271)
- P1-006 Publish proof to Zenodo — COMPLETED
- P1-007 Update 57 dependent entities in D1 — COMPLETED

### Phase 0 (infrastructure — partially done)
- M-001 Generate Master Implementation Plan — COMPLETED
- M-002 Update D1 Knowledge Graph with plan metadata — IN_PROGRESS
- M-005 Worker consolidation audit (36→33 workers) — COMPLETED
- M-003/M-004/M-006/M-007/M-008 — PENDING (tracking dashboard, Vectorize pipeline, citation-graph audit, worker consolidation plan)

*(Full 77-task register is in the KG `nodes` table, label `Task`, `program=kepler`. The remaining
P2–P10 tasks are enumerated there with per-task estimated hours and phase tags.)*

---

## Projects

### WBS-coded projects (canonical)

| WBS | Project | GitHub | DOI | Status |
|:----|:--------|:-------|:----|:-------|
| `QNFO.ADL.001` | Adelic Shannon Theory | `QNFO/adelic-shannon-theory` | 10.5281/zenodo.21336099 | active |
| `QNFO.ADL.002` | Adelic Entropic Numbers | `QNFO/adelic-shannon-theory` | — | active |
| `QNFO.ADL.003` | Adelic Rate Distortion | `QNFO/adelic-shannon-theory` | — | active |
| `QNFO.CMP.001` | Computing Machines | `QNFO/computing-machines` | — | active |
| `QNFO.CON.001` | WBS.6 Consilient Synthesis | `QNFO/wbs-6-synthesis` | 10.5281/zenodo.21547793 | complete |
| `QNFO.CON.002` | Consilience Framework | `QNFO/ultrametric-physics` | 10.5281/zenodo.21804073 | active (P5) |
| `QNFO.JPC.001` | JPCub Validation | `QNFO/jpcub-validation` | — | active |
| `QNFO.ODR.001` | ODR Thesis (Compton Count) | `QNFO/odr-thesis` | 10.5281/zenodo.21780909 | active |
| `QNFO.CGS.001` | QNFO/QWAV Portfolio Gap Synthesis | `QNFO/consilient-gap-synthesis` | 10.5281/zenodo.21782596 | active |
| `QNFO.SLB.001` | The Idempotent Core | `QNFO/laws-of-form` | — | active (P4) |
| `QNFO.SLB.002` | The Void Is Not False | `QNFO/laws-of-form` | — | active (P4) |
| `QNFO.UMP.003` | Invariant Patterns Reframing | `QNFO/ultrametric-physics` | 10.5281/zenodo.21785893 | — |
| `QNFO.RES.002` | Universal Ignorance Audit | `QNFO/qnfo-research` | 10.5281/zenodo.21901984 | active |
| `QNFO.RES.003` | Knowing What We Do Not Know | `QNFO/qnfo-research` | 10.5281/zenodo.21901983 | active |
| `QNFO.RES.004` | QWAV GTM/R&D Strategy | `QNFO/qnfo-research` | — | active (P4) |
| `QNFO.RES.005` | Prime Valuation Depth | `QNFO/qnfo-research` | 10.5281/zenodo.21918838 | published |
| `QNFO.RES.006` | Implications for Computing & QEC | `QNFO/qnfo-research` | — | P0 |
| `QNFO.GOV.001` | Public Transparency Dashboard | `QNFO/.github` | — | active (P0) |

### Archive-indexed active paper projects (selected — full list in KG)

These are individual paper repos that remain in the QNFO org (`project:*` nodes, status `active`),
program-tagged: ultrametric-physics (`adelic-langlands-physics`, `tate-adelic-template`,
`biophoton-ultrametric-consilience`), cfpe (`cfpe-methodology`, `cfpe-paradigm-forecast`,
`harmonic-paradigm`, `harmonische-paradigma`), qnfo-research (`alpha-pi-helix`,
`cancellation-rule-research`, `consilience-physics-numtheory`, `hidden-radix-pqc`, `numerata`,
`zbw-deep-dive`, `zbw-fw-null-test`, `zbw-p5-capstone`, `huang-2025-audit`, `shor-phase3`,
`s10-observer-research`, `measurable-vs-imaginable`, `finite-precision-oc-convergence`, …),
and infomatics (`computing-machines`, `joules-per-compute-benchmark`).

### Deactivated / archived (DEC-020 reduction, 2026-07-11)

~80 project nodes are `ARCHIVED`, `DRAFT`, or `DECOMMISSIONED` — legacy infrastructure projects
(agent-swarm, automated-peer-review, qwav-compute-cloud, reproducibility-as-code, qnfo-hub,
portfolio-api, etc.) and pre-consolidation repos. Retained in the KG for provenance; not active.

---

## Notes

- **Publication corpus:** 1,621 `Paper` nodes in the KG; 92 records in the Zenodo `qwav` community,
  867 records matching "QNFO" on Zenodo (live-checked 2026-08-13).
- **Infrastructure:** 120 `CloudflareAsset` nodes (Workers, Pages, R2, D1, KV, Vectorize, queues,
  DNS zones). Canonical infra on Cloudflare; GitHub is the public mirror.
- **Incident log (transparency):** `Infomatics` project carries status `RECOVERY`
  (INFOMATICS-FALSE-CLAIM-2026-07-19 — content in R2/conversation, GitHub history lost to a
  force-push race). This is disclosed, not hidden.
