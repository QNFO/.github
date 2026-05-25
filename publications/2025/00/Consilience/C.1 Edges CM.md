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
title: C.1 Edges CM
aliases: [C.1 Edges CM, C.1 CM Edges, C Edges]
---

**Appendix C: Detailed Graph Data (Edges)**

**C.1: Edges Originating from Classical Mechanics (CM) Nodes:**

| Source Node ID              | Target Node ID              | Type   | Rationale                                                                                                                               | Conf. | Dir. |
|:-------------------------- |:-------------------------- |:----- |:-------------------------------------------------------------------------------------------------------------------------------------- |:---- |:--- |
| `CM`                        | `GR`                        | `F-LIM`| Classical Mechanics (specifically Newtonian gravity) is the weak-field, low-velocity limit of General Relativity.                         | H     | D    |
| `CM`                        | `QM`                        | `F-LIM`| Classical Mechanics emerges as a limit of Quantum Mechanics (e.g., via correspondence principle, decoherence at large scales).          | H     | D    |
| `CM::NewtonsLaws`           | `CM`                        | `S-COMP`| Newton’s Laws are core defining components of the paradigm of Classical Mechanics.                                                      | H     | D    |
| `CM::Law2_Force`            | `CM::Determinism`           | `L-ENT`| Given initial positions/momenta and F=ma, future states are mathematically determined.                                                  | H     | D    |
| `CM::GravityLaw_Newton`     | `CM::InstantActionDistance` | `L-ENT`| The $1/r^2$form with no time delay implies instantaneous propagation of gravitational influence.                                         | H     | D    |
| `CM::GravityLaw_Newton`     | `GR::EFE`                   | `F-LIM`| Newton’s gravity law is the weak-field, static limit approximation of Einstein’s Field Equations.                                       | H     | D    |
| `CM::AbsoluteSpace`         | `GR::DynamicSpacetime`      | `L-CTR`| The concept of a fixed, absolute background space contradicts GR’s dynamic spacetime that interacts with matter/energy.                 | H     | S    |
| `CM::AbsoluteTime`          | `GR::DynamicSpacetime`      | `L-CTR`| The concept of a universal, absolute time contradicts GR’s notion of time being relative and part of a dynamic spacetime manifold.        | H     | S    |
| `CM::AbsoluteSpacetime`     | `GR::DynamicSpacetime`      | `F-REQ`| Empirical evidence against absolute space (e.g., null result of Michelson-Morley related experiments) necessitated GR’s dynamic view. | H     | D    |
| `CM::Determinism`           | `QM::IntrinsicIndeterminism`| `L-CTR`| Classical determinism (predictable outcomes) contradicts the fundamentally probabilistic nature of measurement in standard QM.          | H     | S    |
| `CM::Determinism`           | `Phil::Determinism`         | `L-INST`| Classical mechanics provides a prime physical instantiation and historical support for the philosophical thesis of determinism.          | H     | D    |
| `CM::ObjectiveProperties`   | `QM::MeasurementCollapse`   | `L-CTR`| The idea that properties have definite values independent of measurement contradicts the QM postulate where measurement defines the state. | H     | S    |
| `CM::ObjectiveProperties`   | `QM::Complementarity`       | `F-CHL`| The classical assumption of simultaneous definite values for all properties is challenged by QM’s principle of complementarity.           | H     | D    |
| `CM::ObjectiveProperties`   | `Phil::Realism`             | `L-CON`/`L-INST`| The classical view of objective properties aligns with and instantiates philosophical realism about measured quantities.              | H     | D    |
| `CM::InstantActionDistance` | `GR::Locality`              | `L-CTR`| Instantaneous gravitational action contradicts the local propagation of influences at speed c inherent in GR.                           | H     | S    |
| `CM::Locality`              | `QM::NonLocality`           | `L-CTR`| The implicit assumption of locality in classical mechanics (excluding Newtonian gravity) is contradicted by QM entanglement.            | H     | S    |
| `CM`                        | `Phil::Physicalism`         | `L-CON`| The ontology of classical mechanics (matter, forces in spacetime) is generally considered compatible with physicalism/materialism.       | M/H   | S    |
| `CM::GravityLaw_Newton`     | `Obs::FlatRotationCurves`   | `L-CTR`| Applying Newton’s gravity law to visible mass fails to predict observed flat galactic rotation curves.                                  | H     | S    |
| `CM::GravityLaw_Newton`     | `Math::Calculus`            | `S-FORM`| Newtonian gravity is formulated using standard differential and integral calculus.                                                      | H     | D    |

**C.2: Edges Originating from General Relativity (GR) Nodes:**

| Source Node ID             | Target Node ID               | Type              | Rationale                                                                                                                               | Conf. | Dir. |
|:------------------------- |:--------------------------- |:---------------- |:-------------------------------------------------------------------------------------------------------------------------------------- |:---- |:--- |
| `GR`                       | `CM`                         | `F-LIM` (Inverse) | General Relativity contains Classical Mechanics (Newtonian Gravity) as its weak-field, low-velocity limit.                              | H     | D    |
| `GR`                       | `LCDM`                       | `F-BAS`           | General Relativity provides the fundamental framework for gravity and spacetime dynamics used in the ΛCDM model.                        | H     | D    |
| `GR`                       | `Math::DifferentialGeometry` | `S-FORM`          | General Relativity is mathematically formulated using the language and tools of differential geometry (manifolds, tensors).             | H     | D    |
| `GR`                       | `Problem::QuantumGravity`    | `F-REQ`           | General Relativity’s incompatibility with quantum mechanics necessitates a more fundamental theory of quantum gravity.                  | H     | D    |
| `GR::EquivalencePrinciple` | `GR`                         | `S-COMP`          | The Equivalence Principle is a core conceptual component and motivation for General Relativity’s geometric interpretation.              | H     | D    |
| `GR::EquivalencePrinciple` | `CM::GravityLaw_Newton`      | `F-CHL`           | The Equivalence Principle motivates viewing gravity as geometry, challenging the Newtonian concept of gravity as a force.               | H     | D    |
| `GR::GeneralCovariance`    | `GR`                         | `S-COMP`          | The Principle of General Covariance is a key principle guiding the mathematical formulation of General Relativity.                      | H     | D    |
| `GR::SpacetimeManifold`    | `GR`                         | `S-COMP`          | The modeling of spacetime as a pseudo-Riemannian manifold is the central mathematical structure defining GR.                            | H     | D    |
| `GR::SpacetimeManifold`    | `GR::MetricTensor`           | `S-COMP`          | The metric tensor defines the geometry of the spacetime manifold in GR.                                                                 | H     | D    |
| `GR::MetricTensor`         | `GR::EFE`                    | `S-COMP`          | The metric tensor (and its derivatives forming the Einstein tensor) is a key component of the Einstein Field Equations.                 | H     | D    |
| `GR::GeodesicMotion`       | `GR`                         | `S-COMP`          | The principle that free particles follow geodesics is a core postulate describing motion within GR.                                     | H     | D    |
| `GR::GeodesicMotion`       | `CM::Law2_Force`             | `F-CHL`           | Geodesic motion (path determined by geometry) offers an alternative explanation for gravitational trajectories compared to F=ma.        | H     | D    |
| `GR::EFE`                  | `GR`                         | `S-COMP`          | The Einstein Field Equations are the central dynamical law of General Relativity.                                                       | H     | D    |
| `GR::EFE`                  | `GR::StressEnergyTensor`     | `C-NEC`           | The Stress-Energy Tensor acts as the source term in the EFE, determining the spacetime curvature.                                       | H     | D    |
| `GR::EFE`                  | `GR::CosmologicalConstant`   | `S-COMP`          | The cosmological constant Λ is an optional term within the structure of the EFE.                                                        | H     | D    |
| `GR::EFE`                  | `GR::Determinism`            | `L-ENT`           | The EFE are deterministic partial differential equations for the metric tensor, given source terms and initial/boundary conditions.     | H     | D    |
| `GR::EFE`                  | `CM::GravityLaw_Newton`      | `F-LIM` (Inverse) | Einstein’s Field Equations reduce to Newton’s law of gravitation in the appropriate weak-field, low-velocity limit.                     | H     | D    |
| `GR::StressEnergyTensor`   | `Concept::Energy`            | `F-BAS`           | The Stress-Energy Tensor generalizes the concept of energy density and includes momentum density and stress.                            | H     | D    |
| `GR::DynamicSpacetime`     | `CM::AbsoluteSpacetime`      | `L-CTR`           | GR’s dynamic spacetime, which interacts with matter, contradicts CM’s fixed, absolute spacetime background.                             | H     | S    |
| `GR::DynamicSpacetime`     | `Phil::Physicalism`          | `F-REQ`           | The dynamic nature of spacetime in GR requires physicalism to clarify whether spacetime itself is a fundamental physical entity.        | M     | D    |
| `GR::ContinuumAssumption`  | `Problem::PlanckScale`       | `F-REQ`           | GR’s assumption of a smooth spacetime continuum is expected to break down at the Planck scale, requiring a quantum gravity description. | H     | D    |
| `GR::Determinism`          | `QM::IntrinsicIndeterminism` | `L-CTR`           | The deterministic evolution described by GR conflicts with the probabilistic nature of measurement outcomes in standard QM.             | H     | S    |
| `GR::Locality`             | `QM::NonLocality`            | `F-CHL`           | GR’s description of local interactions propagating at speed c is challenged by the non-local correlations of quantum entanglement.      | H     | D    |
| `GR::Singularity`          | `GR`                         | `F-CHL`           | The prediction of singularities indicates a breakdown or limit of applicability of the GR framework itself.                             | H     | D    |
| `GR::Singularity`          | `Problem::GRSingularity`     | `L-INST`          | GR’s predictions are the primary instances defining the singularity problem in physics.                                                 | H     | D    |
| `GR::Singularity`          | `Problem::QuantumGravity`    | `F-REQ`           | Singularities signal the need for a quantum theory of gravity to describe physics under extreme conditions.                             | H     | D    |

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
