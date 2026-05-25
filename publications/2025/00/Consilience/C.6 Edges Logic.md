---
ISNI: 0000000526456062
author: Rowan Brad Quni
email: rowan.quni@qnfo.org
website: http://qnfo.org
ORCID: https://orcid.org/0009-0002-4317-5604
robots: By accessing this content, you agree to https://qnfo.org/LICENSE. Non-commercial use only. Attribution required.
DC.rights: https://qnfo.org/LICENSE. Users are bound by terms upon access.
created: 2025-04-10T03:08:58Z
modified: 2025-05-09T03:21:33Z
title: C.6 Edges Logic
aliases: [C.6 Edges Logic, C Edges]
---

**Appendix C: Detailed Graph Data (Edges)**

**C.6: Edges Originating from Logic Nodes**

| Source Node ID             | Target Node ID           | Type     | Rationale                                                                                                                                                                                            | Conf. | Dir. |
|:------------------------- |:----------------------- |:------- |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |:---- |:--- |
| `FOL`                      | `ZFC`                    | `F-BAS`  | First-Order Logic provides the formal language and deductive system within which the axioms of ZFC are stated and theorems are derived.                                                              | H     | D    |
| `FOL`                      | `Math::FormalSystem`     | `L-INST` | First-Order Logic is a primary example and foundation for many mathematical formal systems.                                                                                                          | H     | D    |
| `FOL`                      | `Logic::Soundness`       | `L-ENT`  | The standard proof systems for FOL are sound (only prove valid formulas).                                                                                                                            | H     | D    |
| `FOL`                      | `Logic::Completeness`    | `L-ENT`  | FOL is semantically complete (all valid formulas are provable) according to Gödel’s Completeness Theorem.                                                                                            | H     | D    |
| `FOL::Syntax`              | `FOL`                    | `S-COMP` | The syntax (symbols, formation rules) is a defining component of FOL.                                                                                                                                | H     | D    |
| `FOL::Semantics`           | `FOL`                    | `S-COMP` | The semantics (rules for interpretation in models, truth definition) are a defining component of FOL.                                                                                                | H     | D    |
| `FOL::ProofTheory`         | `FOL`                    | `S-COMP` | The proof theory (logical axioms, inference rules) is a defining component of FOL.                                                                                                                   | H     | D    |
| `FOL::ProofTheory`         | `Logic::Soundness`       | `L-ENT`  | Soundness is a property *of* the proof theory relative to the semantics.                                                                                                                             | H     | D    |
| `ZFC`                      | `Mathematics`            | `F-BAS`  | ZFC serves as the standard foundational axiomatic system for the vast majority of contemporary mathematics.                                                                                          | H     | D    |
| `ZFC`                      | `Math::Continuum`        | `S-FORM` | The real number continuum is typically constructed rigorously within ZFC using set-theoretic definitions (e.g., Dedekind cuts).                                                                      | H     | D    |
| `ZFC`                      | `Math::HilbertSpace`     | `S-FORM` | The definition and properties of Hilbert spaces rely on concepts (sets, functions, limits) formally grounded in ZFC.                                                                                 | H     | D    |
| `ZFC`                      | `Math::GoedelTheorems`   | `F-CHL`  | Gödel’s Incompleteness Theorems apply to ZFC (assuming its consistency), challenging its potential for syntactic completeness and demonstrating the unprovability of its own consistency from within | H     | D    |
| `ZFC::Axioms`              | `ZFC`                    | `S-COMP` | The specific axioms are the defining components of the ZFC system.                                                                                                                                   | H     | D    |
| `ZFC::AxiomOfChoice`       | `ZFC::Axioms`            | `S-COMP` | The Axiom of Choice is a distinct (and historically controversial) axiom within the ZFC axiom set.                                                                                                   | H     | D    |
| `ZFC::AxiomOfInfinity`     | `ZFC::Axioms`            | `S-COMP` | The Axiom of Infinity is crucial within ZFC for founding analysis and dealing with infinite sets.                                                                                                    | H     | D    |
| `ZFC::AxiomOfRegularity`   | `ZFC::Axioms`            | `S-COMP` | The Axiom of Regularity is a key axiom in ZFC ensuring sets are well-founded.                                                                                                                        | H     | D    |
| `ZFC::SetConcept`          | `ZFC`                    | `F-BAS`  | The ontological commitment to pure sets is fundamental to the ZFC framework.                                                                                                                         | H     | D    |
| `ZFC::CumulativeHierarchy` | `ZFC`                    | `F-BAS`  | The cumulative hierarchy provides the standard intended model or picture for the universe of sets described by ZFC.                                                                                  | H     | D    |
| `ZFC::CumulativeHierarchy` | `ZFC::AxiomOfRegularity` | `L-ENT`  | The Axiom of Regularity formally implies the well-founded hierarchical structure.                                                                                                                    | H     | D    |
