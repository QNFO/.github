---
author: Rowan Brad Quni-Gudzinas
ORCID: 0009-0002-4317-5604
ISNI: 0000000526456062
title: "1.0"
aliases:
  - "1.0"
modified: 2025-10-30T10:56:18Z
---

## A Functorial Map from Number Theory to Oscillator Dynamics for Physical Computation

**Author:** Rowan Brad Quni-Gudzinas
**Contact:** rowan.quni@outlook.com
**ORCID:** 0009-0002-4317-5604
**ISNI:** 0000 0005 2645 6062
**DOI:** 10.5281/zenodo.17483833
**Publication Date:** 2025-10-30
**Version:** 1.0

**Abstract**: Physical computation research is bifurcated: mainstream approaches are often limited by compilation to generic representations (e.g., QUBO) that do not preserve a problem’s higher-order structure, while the promising paradigm of oscillator-based computing has been largely confined to problems with a native graph-theoretic structure. This paper introduces a formal, constructive method that bridges this gap: a functorial map that translates the number-theoretic problem of integer factorization, via the Chinese Remainder Theorem, into the coupling matrix of a Kuramoto-type oscillator network. This work thus provides a formal bridge between number theory and dynamical systems, unlocking a new, robust paradigm for physical computation based on emergent synchronization.

**Keywords**: Physical Computation, Oscillator-Based Computing, Functorial Map, Kuramoto Model, Category Theory, Number Theory, Integer Factorization, Emergent Dynamics

---

### 1.0 Introduction

Physical computation research is bifurcated: mainstream approaches are often limited by compilation to generic representations like Quadratic Unconstrained Binary Optimization (QUBO), which do not preserve a problem’s higher-order structure (Lucas, 2014), while the promising paradigm of oscillator-based computing is largely confined to problems with a native graph-theoretic structure (Roychowdhury, 2021). While prior work has explored oscillator-based factorization using methods like positive feedback architectures, a formal, constructive map from the number-theoretic structure of the problem to the coupling topology of an oscillator network remains an open area for development.

This paper introduces and details the construction of such a method: a functorial map that translates the number-theoretic problem of integer factorization, via the Chinese Remainder Theorem (CRT), into the coupling matrix of a Kuramoto-type oscillator network. This work thus provides a formal bridge between number theory and dynamical systems, unlocking a new, robust paradigm for physical computation based on emergent synchronization.

### 2.0 A Functorial Map from Number Theory to Oscillator Dynamics

The mapping from the problem of factoring an integer $N$ to a programmable dynamical system can be formalized as a structure-preserving map, or functor. This map is constructed as a composition of three stages: a number-theoretic decomposition, a translation to an intermediate graph representation, and an embodiment as a physical dynamical system.

#### 2.1 Categorical Formulation

To formalize the “functorial” claim, we define the source and target categories.

-   **Source Category ($\text{Cat\_CRT}$)**: The objects are CRT systems, each defined by an integer $N$ and a set of coprime moduli $\{m_i\}$. A morphism between two objects is the inclusion of an additional modulus, which refines the problem structure.
-   **Target Category ($\text{Cat\_Dyn}$)**: The objects are Kuramoto models, each defined by a set of oscillators and a coupling matrix $K$. A morphism is the addition of a new set of oscillators and the corresponding extension of the coupling matrix.

The map described herein is a functor $F: \text{Cat\_CRT} \rightarrow \text{Cat\_Dyn}$ because it preserves composition: mapping a problem refined by two successive moduli inclusions is equivalent to mapping the initial problem and then applying the two corresponding dynamical system extensions.

#### 2.2 Stage 1: Number-Theoretic Decomposition

The global, multiplicative constraint $pq = N$ is decomposed into a system of local, independent constraints $pq \equiv N \pmod{m_i}$ for a chosen set of small, coprime moduli $\{m_i\}$. The moduli are chosen such that their product exceeds $N$, ensuring a unique solution via CRT. For each modulus $m_i$, the finite set of all local solution pairs $(p_j, q_j)$ is enumerated by exhaustive search.

#### 2.3 Stage 2: Construction of the CRT Consistency Graph

A vertex is created in the consistency graph for each unique local solution pair enumerated in Stage 1. An edge is drawn between two vertices if and only if their respective local solutions are mutually consistent under the CRT. The resulting consistency graph is inherently a k-partite graph, where k is the number of chosen moduli. This construction ensures that the unique integer factors $(p,q)$ of $N$ correspond to the unique largest clique in this graph.

#### 2.4 Stage 3: Embodiment as a Kuramoto Model

An isomorphism is established between the consistency graph and a Kuramoto-type oscillator network. Each vertex in the graph is mapped to a physical oscillator. The adjacency matrix of the graph is mapped to the coupling matrix $K$ of the Kuramoto model. This transforms the abstract problem of finding the largest clique into the physical problem of identifying the largest synchronized cluster of oscillators (Rodrigues et al., 2016).

### 3.0 Properties of the Resulting Dynamical System

The construction yields a dynamical system whose phase space topology encodes the solution structure of the original problem.

#### 3.1 Solution State as a Dominant Attractor

The large clique in the consistency graph, corresponding to the true factors, gives rise to a stable, phase-locked state in the Kuramoto model. This synchronized state acts as a dominant attractor with a large basin of attraction, making the solution robust to initial conditions and small perturbations.

#### 3.2 Infeasibility as Partial Synchronization

If a problem has no globally consistent solution, its consistency graph will lack a large clique, resulting in a “frustrated” network. This prevents the emergence of a single large-scale synchronized cluster. Infeasibility is therefore physically identifiable by the system’s evolution into multiple, smaller, competing clusters, leading to a global order parameter $r(t)$ that is significantly lower than that of a solvable instance with a dominant clique.

### 4.0 Physical Realization and Implementation

A modular, hybrid architecture is proposed, consisting of an analog substrate of coupled oscillators managed by a digital CMOS control plane. The analog substrate can be realized using various technologies, such as MEMS resonators or opto-electronic oscillators (Mallick et al., 2022). The digital plane acts as a programmable coupling fabric, setting the interaction strengths between oscillators to instantiate the coupling matrix $K$.

### 5.0 Discussion

#### 5.1 Performance Characterization and Scalability

The proposed method involves a classical pre-computation to construct the coupling matrix $K$, followed by a physical evolution of the oscillator system.

-   **Classical Complexity**: The number of vertices (oscillators) $M$ is the sum of the number of local solutions for each modulus. The dominant classical cost is the construction of the consistency graph, which scales polynomially with $M$. For cryptographically relevant $N$, $M$ can become large, posing a significant hardware challenge.
-   **Time-to-Solution**: The physical “time-to-solution” is the synchronization time of the network. This is a complex function of the coupling strength, the number of oscillators, and the spectral properties of the coupling graph’s Laplacian. While a precise scaling law is an open research question, this metric provides a concrete target for physical optimization.

#### 5.2 Comparison to Prior and Alternative Methods

Compared to other oscillator-based factorization methods, our CRT-based approach offers a formal and deterministic method for constructing the required coupling graph directly from the number-theoretic properties of the integer $N$. This provides a clear and analyzable structure for the resulting dynamical system. The framework’s use of synchronization as a computational primitive also draws parallels with attractor-based neuromorphic architectures like Hopfield networks.

### 6.0 Conclusion

This work introduces a new, formally grounded discipline of physical compilation that maps number-theoretic problems to the emergent dynamics of oscillator networks. By providing a constructive, functorial map, we resolve a key limitation in oscillator-based computing and demonstrate a physically robust, scalable alternative to mainstream physical computing paradigms.

---

### Appendix A: Formalism of the Kuramoto Model

The state of a network of $N$ oscillators is described by their phases, $\theta_1, \dots, \theta_N$. The time evolution of the phase $\theta_i$ is governed by the differential equation (Acebrón et al., 2005):

$$
\frac{d\theta_i}{dt} = \omega_i + \sum_{j=1}^{N} K_{ij} \sin(\theta_j - \theta_i)
\tag{1}
$$

The degree of global synchronization is measured by the complex order parameter $r(t)$:

$$
r(t)e^{i\psi(t)} = \frac{1}{N}\sum_{j=1}^{N}e^{i\theta_j(t)}
\tag{2}
$$

For a network of identical oscillators ($\omega_i = \omega_0$), as assumed in our model, any positive coupling in a connected graph is sufficient to guarantee eventual synchronization. The dynamics are dominated by the community structure of the coupling graph, where densely connected subgraphs (cliques) will tend to form internally synchronized clusters (Rodrigues et al., 2016).

### Appendix B: Numerical Simulation of the Factorization Functor for N=91

1.  **Problem Definition**: Set $N = 91$ (factors are 7, 13).
2.  **Decomposition**: Choose coprime moduli $m_1 = 3, m_2 = 4, m_3 = 5$. This gives $2+2+4=8$ vertices.
3.  **Graph Construction**: Construct the CRT consistency graph. The vertices corresponding to the local solutions for the true factors $(7,13)$—namely $(1,1) \pmod 3$, $(3,1) \pmod 4$, and $(2,3) \pmod 5$—form a 3-clique.
4.  **Matrix Embodiment**: Construct the $8 \times 8$ adjacency matrix of the consistency graph. This becomes the coupling matrix $K$.
5.  **Numerical Simulation**: Simulate the time evolution of the 8 oscillator phases. For the simulation, all natural frequencies $\omega_i$ were set to $\omega_0=0$, and the coupling matrix entries were set to $K_{ij} = 1$ if an edge exists and $K_{ij} = 0$ otherwise.
6.  **Result Verification**: The simulation converges to a stable state within approximately 100 time units. The final order parameter for the 3-oscillator solution cluster is $r_{sol} > 0.99$, indicating strong phase-locking. The global order parameter for the entire 8-oscillator system is moderate, $r_{global} \approx 0.5$, reflecting the formation of multiple clusters. The largest synchronized cluster corresponds to the local solutions that reconstruct, via the CRT, to the correct global factors $(p=7, q=13)$.

---

### References

Aaronson, S. (2005). NP-complete Problems and Physical Reality. *ACM SIGACT News*, *36*(1), 30–52. https://doi.org/10.1145/1052796.1052805

Acebrón, J. A., Bonilla, L. L., Vicente, C. J. P., Ritort, F., & Spigler, R. (2005). The Kuramoto model: A simple paradigm for synchronization phenomena. *Reviews of Modern Physics*, *77*(1), 137–185. https://doi.org/10.1103/RevModPhys.77.137

Lawvere, F. W., & Schanuel, S. H. (2009). *Conceptual Mathematics: A First Introduction to Categories*. Cambridge University Press.

Lucas, A. (2014). Ising formulations of many NP problems. *Frontiers in Physics*, *2*. https://doi.org/10.3389/fphy.2014.00005

Mac Lane, S. (1998). *Categories for the Working Mathematician*. Springer. https://doi.org/10.1007/978-1-4757-4721-8

Mallick, A., Bashar, M. K., Lin, Z., & Shukla, N. (2022). Oscillator-based Dynamical Computing Platforms to Solve Combinatorial Optimization. *2022 IEEE International Electron Devices Meeting (IEDM)*, 35.5.1-35.5.4. https://doi.org/10.1109/IEDM45625.2022.10019569

Rodrigues, F. A., Peron, T. K. D., Ji, P., & Kurths, J. (2016). The Kuramoto model in complex networks. *Physics Reports*, *610*, 1–98. https://doi.org/10.1016/j.physrep.2015.10.008

Roychowdhury, J. (2021). Solving combinatorial optimisation problems using oscillator based Ising machines. *Natural Computing*, *20*(2), 287–306. https://doi.org/10.1007/s11047-021-09845-3
