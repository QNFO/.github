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
title: C.4 Edges Thermo StatMech
aliases: [C.4 Edges Thermo StatMech, C Edges]
---

**Appendix C: Detailed Graph Data (Edges)**

**C.4.1: Edges Originating from Thermodynamics (Thermo) Nodes:**

| Source Node ID              | Target Node ID              | Type   | Rationale                                                                                                                               | Conf. | Dir. |
|:-------------------------- |:-------------------------- |:----- |:-------------------------------------------------------------------------------------------------------------------------------------- |:---- |:--- |
| `Thermo`                    | `StatMech`                  | `E-XPBY` | The macroscopic laws of thermodynamics are explained by the statistical behavior of microscopic constituents described by statistical mechanics. | M/H   | D    |
| `Thermo`                    | `Concept::Energy`           | `F-BAS`| Thermodynamics is fundamentally concerned with energy, its forms (heat, work), and its conservation (First Law).                          | H     | D    |
| `Thermo`                    | `Concept::Entropy`          | `F-BAS`| Thermodynamics introduces entropy as a key state variable governing spontaneity and equilibrium (Second, Third Laws).                     | H     | D    |
| `Thermo::ZerothLaw`         | `Thermo`                    | `S-COMP`| The Zeroth Law is a foundational principle defining thermal equilibrium within thermodynamics.                                            | H     | D    |
| `Thermo::FirstLaw`          | `Thermo`                    | `S-COMP`| The First Law is a core principle of thermodynamics, stating energy conservation.                                                       | H     | D    |
| `Thermo::FirstLaw`          | `Concept::Energy`           | `L-ENT`| The First Law is a specific application/statement of the general principle of energy conservation to thermodynamic systems.               | H     | D    |
| `Thermo::SecondLaw`         | `Thermo`                    | `S-COMP`| The Second Law is a core principle of thermodynamics, defining entropy increase and the direction of spontaneous processes.             | H     | D    |
| `Thermo::SecondLaw`         | `Thermo::Entropy`           | `L-ENT`| The Second Law is formulated in terms of the behavior of thermodynamic entropy.                                                         | H     | D    |
| `Thermo::SecondLaw`         | `ArrowOfTime` *(Concept needed)* | `E-XPL` | The Second Law provides the basis for the macroscopic thermodynamic arrow of time (irreversibility).                                    | H     | D    |
| `Thermo::SecondLaw`         | `CM::Determinism` / `QM::UnitaryEvolution` | `F-CHL` | The irreversibility implied by the Second Law appears to conflict with the time-reversible nature of underlying micro-dynamics (Loschmidt’s paradox). | H     | D    |
| `Thermo::ThirdLaw`          | `Thermo`                    | `S-COMP`| The Third Law is a core principle concerning the behavior of entropy near absolute zero.                                                | H     | D    |
| `Thermo::ThirdLaw`          | `Thermo::Entropy`           | `L-ENT`| The Third Law makes specific statements about the limiting value of thermodynamic entropy.                                              | H     | D    |
| `Thermo::Entropy`           | `Concept::Entropy`          | `L-INST`| Thermodynamic entropy is a specific instance/measure of the broader concept of entropy, related to heat and macroscopic disorder.       | H     | D    |
| `Thermo::MacroscopicSystem` | `Thermo`                    | `F-BAS`| The laws of thermodynamics are formulated for and apply primarily to macroscopic systems near equilibrium.                              | H     | D    |

**C.4.2: Edges Originating from Statistical Mechanics (StatMech) Nodes:**

| Source Node ID                | Target Node ID              | Type   | Rationale                                                                                                                               | Conf. | Dir. |
|:---------------------------- |:-------------------------- |:----- |:-------------------------------------------------------------------------------------------------------------------------------------- |:---- |:--- |
| `StatMech`                    | `Thermo`                    | `E-RED`| Statistical mechanics provides a microscopic foundation aiming to reduce thermodynamic laws to statistical behavior of constituents.      | M/H   | D    |
| `StatMech`                    | `CM` / `QM`                 | `F-BAS`| Statistical mechanics applies statistical methods to the underlying microscopic dynamics described by either classical or quantum mechanics. | H     | D    |
| `StatMech`                    | `Math::ProbabilityTheory`   | `F-BAS`| Statistical mechanics fundamentally relies on probability theory and statistical ensembles to calculate macroscopic properties.           | H     | D    |
| `StatMech::BoltzmannEntropy`  | `StatMech`                  | `S-COMP`| Boltzmann’s entropy formula is a core definition within statistical mechanics linking entropy to microstate count.                      | H     | D    |
| `StatMech::BoltzmannEntropy`  | `Thermo::Entropy`           | `S-FORM`/`E-XPL`| Provides a microscopic interpretation intended to correspond to thermodynamic entropy for isolated systems in equilibrium.            | H     | D    |
| `StatMech::BoltzmannEntropy`  | `StatMech::Microstate`      | `F-BAS`| Boltzmann entropy is defined based on the number (W or Ω) of accessible microstates.                                                    | H     | D    |
| `StatMech::GibbsEntropy`      | `StatMech`                  | `S-COMP`| Gibbs’ entropy formula is a core definition within statistical mechanics for ensembles described by probability distributions.          | H     | D    |
| `StatMech::GibbsEntropy`      | `Thermo::Entropy`           | `S-FORM`/`E-XPL`| Provides a more general microscopic interpretation intended to correspond to thermodynamic entropy.                                 | H     | D    |
| `StatMech::GibbsEntropy`      | `InfoSci::ShannonEntropy`   | `S-FORM`/`E-ANL`| Gibbs entropy has the identical mathematical form as Shannon entropy, indicating a deep formal analogy.                             | H     | S    |
| `StatMech::Microstate`        | `StatMech`                  | `S-COMP`| The concept of microstates is fundamental to the statistical mechanics approach.                                                        | H     | D    |
| `StatMech::Macrostate`        | `StatMech`                  | `S-COMP`| The concept of macrostates (defined by macroscopic variables) is fundamental to linking micro and macro descriptions.                 | H     | D    |
| `StatMech::Macrostate`        | `StatMech::Microstate`      | `S-ABS`| A macrostate is an abstraction corresponding to a large ensemble of possible microstates.                                               | H     | D    |
| `StatMech::ProbabilisticAssumption` | `StatMech`            | `F-BAS`| Assumptions like equal a priori probabilities or ergodicity are necessary methodological components for standard statistical mechanics calculations. | H     | D    |
| `StatMech`                    | `Thermo::SecondLaw`         | `E-XPL`| Statistical mechanics explains the Second Law as the overwhelming tendency for systems to evolve towards more probable macrostates (higher W or H). | H     | D    |
