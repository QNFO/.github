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
title: C.8 Edges InfoSci
aliases: [C.8 Edges InfoSci, C Edges]
---

**Appendix C: Detailed Graph Data (Edges)**

**C.8: Edges Originating from Information Science Nodes**

| Source Node ID                 | Target Node ID             | Type     | Rationale                                                                                                                                                                             | Conf. | Dir. |
|:----------------------------- |:------------------------- |:------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |:---- |:--- |
| `InfoSci::ShannonTheory`       | `Math::ProbabilityTheory`  | `F-BAS`  | Shannon Information Theory is mathematically formulated using and relies fundamentally on probability theory.                                                                         | H     | D    |
| `InfoSci::ShannonTheory`       | `Concept::Information`     | `S-FORM` | Provides a specific, quantitative, syntactic definition of information as reduction of uncertainty.                                                                                   | H     | D    |
| `InfoSci::ShannonEntropy`      | `InfoSci::ShannonTheory`   | `S-COMP` | Shannon Entropy (H) is a core concept/measure defined within Shannon Information Theory.                                                                                              | H     | D    |
| `InfoSci::ShannonEntropy`      | `StatMech::GibbsEntropy`   | `S-FORM` | Shannon Entropy has the identical mathematical form as Gibbs Entropy.                                                                                                                 | H     | S    |
| `InfoSci::ShannonEntropy`      | `StatMech::GibbsEntropy`   | `E-ANL`  | The identical form suggests a deep analogy related to uncertainty/information/number of states between the two concepts.                                                              | H     | S    |
| `InfoSci::ShannonEntropy`      | `Concept::Entropy`         | `L-INST` | Shannon Entropy is a specific instance of the broader concept of entropy, focused on information/uncertainty.                                                                         | H     | D    |
| `InfoSci::ChannelCapacity`     | `InfoSci::ShannonTheory`   | `S-COMP` | Channel Capacity (C) is a core concept/limit defined within Shannon Information Theory.                                                                                               | H     | D    |
| `InfoSci::SourceCodingTheorem` | `InfoSci::ShannonTheory`   | `S-COMP` | The Source Coding Theorem is a key result derived within Shannon Information Theory concerning data compression limits.                                                               | H     | D    |
| `InfoSci::SourceCodingTheorem` | `InfoSci::ShannonEntropy`  | `F-BAS`  | The limit for lossless compression is determined by the Shannon Entropy of the source.                                                                                                | H     | D    |
| `InfoSci::NoisyChannelTheorem` | `InfoSci::ShannonTheory`   | `S-COMP` | The Noisy-Channel Coding Theorem is a key result derived within Shannon Information Theory concerning reliable communication limits.                                                  | H     | D    |
| `InfoSci::NoisyChannelTheorem` | `InfoSci::ChannelCapacity` | `F-BAS`  | The limit for reliable communication is determined by the Channel Capacity.                                                                                                           | H     | D    |
| `InfoSci::Information`         | `InfoSci::ShannonTheory`   | `S-COMP` | The specific syntactic concept of information (reduction of uncertainty) is central to Shannon Theory.                                                                                | H     | D    |
| `InfoSci::Information`         | `Physics`                  | `E-ANL`  | Connections between Shannon’s syntactic information and physical concepts like entropy or energy are often analogical or require careful interpretation (e.g., Landauer’s principle). | M     | S    |
| `InfoSci::Information`         | `Physics`                  | `F-REQ`  | The precise relationship between abstract Shannon information and physical reality requires further explanation/unification.                                                          | M     | D    |
| `InfoSci::Information`         | `Philosophy`               | `F-CHL`  | Shannon’s purely syntactic definition challenges broader philosophical concepts of information involving meaning or semantics.                                                        | H     | D    |
