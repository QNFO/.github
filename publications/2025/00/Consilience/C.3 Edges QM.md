---
ISNI: 0000000526456062
author: Rowan Brad Quni
email: rowan.quni@qnfo.org
website: http://qnfo.org
ORCID: https://orcid.org/0009-0002-4317-5604
robots: By accessing this content, you agree to https://qnfo.org/LICENSE. Non-commercial use only. Attribution required.
DC.rights: https://qnfo.org/LICENSE. Users are bound by terms upon access.
created: 2025-04-10T03:08:58Z
modified: 2025-05-09T03:21:34Z
title: C.3 Edges QM
aliases: [C.3 Edges QM, C Edges]
---

**Appendix C: Detailed Graph Data (Edges)**

**C.3: Edges Originating from Quantum Mechanics (QM - Standard Interpretation) Nodes:**

| Source Node ID              | Target Node ID              | Type   | Rationale                                                                                                                               | Conf. | Dir. |
|:-------------------------- |:-------------------------- |:----- |:-------------------------------------------------------------------------------------------------------------------------------------- |:---- |:--- |
| `QM`                        | `CM`                        | `F-LIM` (Inverse) | Quantum Mechanics contains Classical Mechanics as its macroscopic or large quantum number limit (Correspondence Principle).                 | H     | D    |
| `QM`                        | `SM`                        | `F-BAS`| Quantum Mechanics provides the foundational principles upon which the Standard Model (as a QFT) is built.                                 | H     | D    |
| `QM`                        | `Math::HilbertSpace`        | `S-FORM`| The standard mathematical formulation of QM uses Hilbert spaces to represent states and operators.                                      | H     | D    |
| `QM`                        | `Math::ProbabilityTheory`   | `F-BAS`| QM fundamentally relies on probability theory via the Born rule to connect formalism to experimental outcomes.                            | H     | D    |
| `QM`                        | `Problem::QuantumGravity`   | `F-REQ`| Standard QM does not incorporate gravity dynamically, necessitating a unification with GR (Quantum Gravity).                               | H     | D    |
| `QM`                        | `Problem::QMeasurement`     | `S-COMP`| The measurement problem is an internal conceptual inconsistency or incompleteness within standard QM interpretations.                      | H     | D    |
| `QM::StateVector`           | `QM`                        | `S-COMP`| The state vector (wavefunction) is the core representation of a system’s state in QM.                                                   | H     | D    |
| `QM::StateVector`           | `QM::Superposition`         | `L-ENT`| The vector nature of states in Hilbert space directly entails the principle of superposition (linear combinations are valid states).      | H     | D    |
| `QM::HilbertSpace`          | `QM::StateVector`           | `F-BAS`| Hilbert space is the mathematical structure within which state vectors are defined.                                                     | H     | D    |
| `QM::ObservableOperator`    | `QM`                        | `S-COMP`| Associating observables with operators is a core postulate of QM.                                                                       | H     | D    |
| `QM::ObservableOperator`    | `QM::Quantization`          | `L-ENT`| The postulate that measurement results are eigenvalues of operators directly leads to observed quantization.                              | H     | D    |
| `QM::SchrodingerEq`         | `QM`                        | `S-COMP`| The Schrödinger equation is the core postulate governing time evolution (between measurements).                                         | H     | D    |
| `QM::SchrodingerEq`         | `QM::UnitaryEvolution`      | `L-ENT`| The mathematical form of the Schrödinger equation ensures that time evolution is unitary.                                               | H     | D    |
| `QM::UnitaryEvolution`      | `QM::MeasurementCollapse`   | `L-CTR`| Unitary evolution is deterministic and preserves superposition, contradicting the non-unitary, probabilistic nature of collapse.        | H     | S    |
| `QM::BornRule`              | `QM`                        | `S-COMP`| The Born rule is the core postulate linking the formalism (state vector) to experimental probabilities.                                 | H     | D    |
| `QM::BornRule`              | `QM::IntrinsicIndeterminism`| `F-BAS`| The Born rule provides probabilities, which are interpreted as fundamental indeterminism in standard QM.                                | H     | D    |
| `QM::MeasurementCollapse`   | `QM`                        | `S-COMP`| The projection postulate (collapse) is a core component of the standard description of measurement.                                     | H     | D    |
| `QM::MeasurementCollapse`   | `CM::ObjectiveProperties`   | `L-CTR`| Collapse implies properties are defined/created by measurement, contradicting classical objective reality.                               | H     | S    |
| `QM::MeasurementCollapse`   | `Phil::Realism`             | `F-CHL`| The nature of collapse challenges simple forms of scientific realism about pre-measurement properties.                                  | M/H   | D    |
| `QM::MeasurementCollapse`   | `Problem::QMeasurement`     | `L-ENT`| The collapse postulate is central to the measurement problem, conflicting with unitary evolution.                                       | H     | D    |
| `QM::Superposition`         | `QM`                        | `S-COMP`| Superposition is a fundamental principle arising from the linearity of the Hilbert space structure.                                     | H     | D    |
| `QM::Quantization`          | `CM`                        | `L-CTR`| Observed quantization contradicts the classical assumption that physical quantities can take continuous values.                           | H     | S    |
| `QM::IntrinsicIndeterminism`| `CM::Determinism`           | `L-CTR`| Fundamental indeterminism contradicts classical determinism.                                                                            | H     | S    |
| `QM::IntrinsicIndeterminism`| `Phil::Determinism`         | `L-CTR`| Standard QM interpretation contradicts the philosophical thesis of determinism.                                                         | H     | S    |
| `QM::IntrinsicIndeterminism`| `Phil::CausalClosure`       | `F-CHL`| If quantum events are truly random, it potentially challenges the idea that all physical events have sufficient *physical* causes.       | M     | D    |
| `QM::Complementarity`       | `CM::ObjectiveProperties`   | `F-CHL`| Complementarity challenges the classical assumption that all properties can possess definite values simultaneously.                     | H     | D    |
| `QM::UncertaintyPrinciple`  | `QM`                        | `S-COMP`| The Uncertainty Principle is a core principle derived from the QM formalism (non-commuting operators).                                | H     | D    |
| `QM::UncertaintyPrinciple`  | `CM::ObjectiveProperties`   | `F-CHL`| The Uncertainty Principle places fundamental limits on the simultaneous definability of properties assumed objective in CM.             | H     | D    |
| `QM::Entanglement`          | `QM`                        | `S-COMP`| Entanglement is a key phenomenon predicted and described by the QM formalism for multi-part systems.                                  | H     | D    |
| `QM::Entanglement`          | `CM::Locality`              | `F-CHL`| Entanglement demonstrates non-local correlations that challenge the implicit locality assumptions of classical mechanics.                 | H     | D    |
| `QM::Entanglement`          | `Phil::LocalRealism`        | `L-CTR`| Experimental verification of Bell’s theorem violations using entangled states contradicts local realism.                                | H     | S    |
| `QM::NonLocality`           | `GR::Locality`              | `L-CTR` / `F-CHL` | QM non-locality conflicts with the local nature of interactions described by classical GR field equations.                            | H     | S/D |
| `QM::ClassicalDescriptionReq`| `QM`                       | `S-COMP`| Bohr’s requirement for classical descriptions is a component of the Copenhagen interpretation.                                        | H     | D    |
| `QM::ClassicalDescriptionReq`| `Problem::QMeasurement`    | `C-INF`| This requirement contributes to the measurement problem by creating an ambiguous quantum-classical divide.                              | M     | D    |
| `QM::MeasurementProblem`    | `QM`                       | `F-CHL`| The measurement problem indicates a fundamental conceptual incompleteness or inconsistency within standard QM interpretations.           | H     | D    |
