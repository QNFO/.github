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
title: C.7 Edges Philosophy
aliases: [C.7 Edges Philosophy, C Edges]
---

**Appendix C: Detailed Graph Data (Edges)**

**C.7: Edges Originating from Philosophy Nodes**

| Source Node ID            | Target Node ID               | Type     | Rationale                                                                                                                                               | Conf. | Dir. |
|:------------------------ |:--------------------------- |:------- |:------------------------------------------------------------------------------------------------------------------------------------------------------ |:---- |:--- |
| `Phil::Physicalism`       | `Physics`                    | `O-DEP`  | Physicalism, particularly theory-based versions, defines the “physical” based on the content provided by physical theories.                             | H     | D    |
| `Phil::Physicalism`       | `CM`                         | `L-CON`  | The ontology of classical mechanics (matter, forces, absolute spacetime) is generally considered compatible with physicalism/materialism.               | M/H   | S    |
| `Phil::Physicalism`       | `QM::MeasurementProblem`     | `F-CHL`  | The measurement problem, especially interpretations involving consciousness or observer effects, challenges standard physicalist assumptions.           | M/H   | D    |
| `Phil::Physicalism`       | `GR::DynamicSpacetime`       | `F-REQ`  | Physicalism needs to provide a clear ontological account of dynamic spacetime–is it a fundamental physical entity or emergent?                        | M     | D    |
| `Phil::Physicalism`       | `Phil::OntologicalMonism`    | `L-ENT`  | Physicalism entails ontological monism, asserting only physical substance/properties are fundamental.                                                   | H     | D    |
| `Phil::Physicalism`       | `Phil::CausalClosure`        | `F-BAS`  | Physicalism often assumes or argues for the causal closure of the physical domain as a core tenet.                                                      | M/H   | D    |
| `Phil::OntologicalMonism` | `Phil::Physicalism`          | `S-COMP` | Ontological monism is a core component defining the physicalist thesis.                                                                                 | H     | D    |
| `Phil::CausalClosure`     | `Phil::Physicalism`          | `F-BAS`  | Causal closure provides support for physicalism by excluding non-physical causes for physical events.                                                   | M/H   | D    |
| `Phil::CausalClosure`     | `QM::IntrinsicIndeterminism` | `F-CHL`  | If quantum events lack sufficient *physical* causes (are truly random), it challenges strict causal closure.                                            | M     | D    |
| `Phil::Supervenience`     | `Phil::Physicalism`          | `S-FORM` | Supervenience is often used to formalize the dependence relationship between mental/higher-level properties and physical properties within physicalism. | H     | D    |
| `Phil::Fundamentality`    | `Physics`                    | `E-XPL`  | Physics seeks fundamental laws and entities, directly engaging with the philosophical concept of fundamentality.                                        | H     | D    |
| `Phil::Fundamentality`    | `Phil::Grounding`            | `F-BAS`  | The concept of grounding is a primary tool used in contemporary metaphysics to analyze fundamentality relationships.                                    | H     | D    |
| `Phil::Grounding`         | `Phil::Fundamentality`       | `S-FORM` | Grounding provides a formal way to express claims about what is metaphysically fundamental relative to what is derived.                                 | H     | D    |
| `Phil::Grounding`         | `Phil::Physicalism`          | `S-FORM` | Physicalists often use grounding to state that mental/biological properties are grounded in physical properties.                                        | H     | D    |
| `Phil::Causation`         | `Physics`                    | `E-XPL`  | Physical laws (e.g., force laws, field equations) are typically interpreted as describing causal relationships or enabling causal explanations.         | H     | D    |
| `Phil::Causation`         | `CM::Law2_Force`             | `L-INST` | F=ma provides a specific instance of a causal law (force causes acceleration).                                                                          | H     | D    |
| `Phil::Causation`         | `GR::EFE`                    | `L-INST` | EFE describe how stress-energy causes spacetime curvature, which in turn dictates motion (a form of causation).                                         | H     | D    |
| `Phil::Causation`         | `Thermo::SecondLaw`          | `C-INF`  | While not strictly causal, the Second Law provides constraints on possible causal processes (directionality).                                           | M     | D    |
| `Phil::Determinism`       | `CM::Determinism`            | `F-BAS`  | The philosophical concept of determinism finds a strong exemplar in the deterministic nature of classical mechanics.                                    | H     | D    |
| `Phil::Determinism`       | `QM::IntrinsicIndeterminism` | `L-CTR`  | The philosophical thesis of determinism is contradicted by the standard interpretation of quantum mechanics.                                            | H     | S    |
| `Phil::Realism`           | `CM::ObjectiveProperties`    | `L-CON`  | Scientific realism aligns well with the classical view of objective, measurement-independent properties.                                                | H     | S    |
| `Phil::Realism`           | `QM::MeasurementCollapse`    | `F-CHL`  | Measurement collapse and contextuality in QM pose significant challenges to naive forms of scientific realism about properties.                         | H     | D    |
| `Phil::LocalRealism`      | `Concept::Locality`          | `F-BAS`  | Local realism combines the classical assumptions of locality and realism regarding pre-existing properties.                                             | H     | D    |
| `Phil::LocalRealism`      | `Phil::Realism`              | `F-BAS`  | Local realism combines the classical assumptions of locality and realism regarding pre-existing properties.                                             | H     | D    |
| `Phil::LocalRealism`      | `QM::Entanglement`           | `L-CTR`  | Quantum entanglement, via Bell’s theorem violations, demonstrably contradicts local realism.                                                            | H     | S    |
|                           |                              |          |                                                                                                                                                         |       |      |
