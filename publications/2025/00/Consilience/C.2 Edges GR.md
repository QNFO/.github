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
title: C.2 Edges GR
aliases: [C.2 Edges GR, C.2 GR Edges, C Edges]
---

**Appendix C: Detailed Graph Data (Edges)**

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
