---
author: Rowan Brad Quni-Gudzinas
ORCID: 0009-0002-4317-5604
ISNI: 0000000526456062
modified: 2025-11-06T09:30:58Z
title: Reassessing the Foundations of Quantum Computation
aliases:
  - Reassessing the Foundations of Quantum Computation
  - 0.4.5
---

## Reassessing the Foundations of Quantum Computation: From Theoretical Artifacts to Physical Realities

**Author:** Rowan Brad Quni-Gudzinas
**Contact:** rowan.quni@outlook.com
**ORCID:** 0009-0002-4317-5604
**ISNI:** 0000 0005 2645 6062
**DOI:** 10.5281/zenodo.17541087
**Publication Date:** 2025-11-06
**Version:** 1.0

**Abstract**: This analysis argues that Shor’s algorithm, while mathematically elegant, functions as a theoretical artifact defined under physically unrealizable conditions—perfect coherence, infinite precision, and unbounded resources—rendering it a mathematical trap that has misdirected the field toward infeasible engineering goals. In contrast, Landauer’s principle—that “information is physical”—provides a necessary foundation for evaluating computation within thermodynamic and material constraints. Empirical evidence reveals a fundamental scaling phase transition: beyond current scales, quantum error correction fails to suppress errors due to correlated failures, operator imprecision, and material defects, causing system reliability to degrade. The resulting divergence in resource requirements makes commercial-scale quantum computing physically infeasible. A constructive path forward requires abandoning idealized models of exponential speedup and developing computational paradigms intrinsically grounded in physical law.

**Keywords**: Quantum computing; Shor’s algorithm; Landauer’s principle; Quantum error correction; Computational scalability; Fault-tolerant quantum computing; Physical limits of computation; Decoherence; Two-level systems; Operator imprecision; Phase transition in quantum systems; Quantum hardware; Information theory; Thermodynamics of computation; Quantum supremacy

---

## A Critical Reevaluation of Shor’s Algorithm as a Theoretical Construct

The narrative that has dominated quantum computing for decades positions Peter Shor’s 1994 algorithm as a revolutionary breakthrough, a watershed moment that transformed the field from speculative physics into a viable technological trajectory (Shor, 1994). This portrayal is not merely celebratory—it functions as a foundational myth, structuring investment priorities, research agendas, and public perception. However, a rigorous methodological analysis reveals that Shor’s algorithm occupies a problematic epistemic category: it is a formally correct mathematical construct within an idealized computational model, but one whose physical realizability remains unsupported by empirical evidence or engineering feasibility. Its primary consequence has not been technological advancement, but the institutionalization of a research paradigm centered on an artifact defined under physically unattainable conditions.

Shor’s algorithm purports to factor large integers in polynomial time using a quantum computer, thereby threatening widely used cryptographic systems like RSA (Shor, 1994; Gidney & Ekerå, 2021). The theoretical framework assumes perfect unitary evolution, infinite precision in state preparation and gate operations, and complete isolation from environmental decoherence—conditions that are known to be violated in all physical implementations (Dyakonov, 2018; Levin, 2003). The algorithm requires manipulating quantum states with amplitudes specified to hundreds or even millions of decimal places, a level of control far beyond any demonstrated or foreseeable experimental capability (Levin, 2003). As Leonid Levin emphasized, no physical law has ever been tested to such precision; treating these continuous parameters as manipulable quantities is an extrapolation without empirical basis (Levin, 2003). Furthermore, the complexity model underpinning the algorithm assumes constant cost per quantum operation regardless of system size, ignoring the physical resources required to maintain coherence across exponentially growing Hilbert spaces—a stance challenged by Oded Goldreich, who argued that operational cost must scale with state non-degeneracy (Goldreich, 2005).

The practical consequences of this algorithm have been minimal. Despite over three decades of effort, the largest integer factored using Shor’s algorithm remains 21, achieved on highly specialized hardware under controlled laboratory conditions (Martín-López et al., 2012). Current quantum processors have recently surpassed 1,000 physical qubits, yet estimates for running Shor’s algorithm on cryptographically relevant inputs (e.g., 2048-bit RSA) range from 20 million to over a billion physical qubits when accounting for error correction overheads (Gidney & Ekerå, 2021; Gidney, 2017). These figures highlight a chasm between theoretical description and implementable design. Rather than serving as a roadmap for scalable computation, Shor’s algorithm functions more accurately as a *mathematical trap*: it defines a problem so resource-intensive that its pursuit diverts attention and funding toward overcoming increasingly prohibitive engineering challenges, many of which stem directly from the unrealistic assumptions baked into the original formulation. The algorithm does not demonstrate a feasible path forward; instead, it establishes a benchmark predicated on the suspension of physical constraints, thereby privileging formalism over material reality.

This is not to dismiss the internal mathematical consistency of the algorithm, which stands as a valid result within the standard quantum circuit model. However, its status as a catalyst for progress must be critically reassessed. The widespread acceptance of Shor’s algorithm as a proof of quantum advantage has led to a conflation of theoretical possibility with practical plausibility—a conflation that undermines methodological rigor. By anchoring the entire justification for large-scale quantum computing to a single, unimplementable protocol, the field risks becoming a self-referential enterprise, where success is measured by incremental improvements toward an asymptotic limit rather than by the delivery of functional, reliable computation. A constructive analysis demands that we treat Shor’s algorithm not as a triumph, but as a cautionary case study in how idealized models can mislead when decoupled from physical grounding.

## Landauer’s Principle and the Primacy of Physical Law in Information Processing

In stark contrast to the abstract formalism surrounding Shor’s algorithm, Rolf Landauer’s work provides a principled foundation for evaluating computational schemes based on their adherence to physical law. While employed at IBM’s Thomas J. Watson Research Center, Landauer developed a framework that insisted on the inseparability of information and physics—a perspective crystallized in his dictum “information is physical” (Landauer, 1991, 1996). This principle asserts that every bit of information must be instantiated in a physical medium, subject to the laws of thermodynamics, statistical mechanics, and material science. It serves as a necessary corrective to theories that treat computation as a purely logical or mathematical activity, divorced from energetic and entropic costs.

Landauer’s most influential contribution, formulated in 1961, established that logically irreversible operations—such as the erasure of a bit—are necessarily accompanied by a minimum energy dissipation of $kT \ln 2$ joules per bit erased (Landauer, 1961; Bennett, 2003). This result, now known as Landauer’s principle, grounded the thermodynamics of computation in statistical physics and demonstrated that information processing cannot evade the second law of thermodynamics (Bennett, 2003). Far from being a mere technical detail, this insight redefined the boundaries of what is computationally possible. It implied that zero-energy computation could only occur if all operations were reversible, a constraint that shaped subsequent research into reversible logic and low-power computing architectures (Landauer, 1996). Unlike formulations that assume idealized, lossless operations, Landauer’s approach demanded accountability: any proposed computational model must specify how it manages entropy production and heat dissipation.

Crucially, Landauer applied this same rigor to emerging proposals for quantum computing. He did not reject the concept outright, but insisted that claims about performance gains be evaluated against realistic models of noise, control error, and material imperfection (Landauer, 1995; DiVincenzo, 1995). He pointed out that quantum systems are exceptionally sensitive to environmental coupling, and that maintaining coherent superpositions at scale would require unprecedented levels of isolation and stability—conditions unlikely to be achievable in practice (Dyakonov, 2018). He advocated for a disclaimer in quantum computing publications stating explicitly that proposed schemes relied on speculative technology, failed to account for all sources of noise, and probably would not work (Landauer, 1995). This was not skepticism born of conservatism, but a defense of scientific integrity: without such caveats, the field risked substituting mathematical elegance for physical plausibility.

Given this context, Landauer’s credibility in assessing the feasibility of quantum computing exceeds that of theorists working within abstract computational models. His expertise was not confined to formalism; it extended to the engineering realities of device physics, noise management, and thermodynamic limits—all central to building functional machines. Where Shor’s algorithm operates in a domain of unbounded resources and perfect fidelity, Landauer’s framework insists on boundedness, dissipation, and irreversibility. His work predates the quantum computing boom and offers a stable reference point from which to evaluate later claims. When viewed through Landauer’s lens, the promise of exponential speedups via quantum parallelism appears not as a discovery, but as a failure to incorporate fundamental physical constraints into the computational model. The burden of proof, therefore, lies not with critics of scalability, but with proponents of large-scale quantum computation to demonstrate how their designs circumvent or satisfy the physical principles Landauer so clearly articulated.

## The Scaling Phase Transition: Resource Divergence in Real-World Systems

A constructive analysis of quantum computing must confront the phenomenon of scaling phase transitions—critical thresholds beyond which increases in system size lead not to improved performance, but to catastrophic degradation in reliability. This behavior is observed empirically in current quantum hardware and contradicts the optimistic projections of fault-tolerant quantum computing theory, which assumes that error correction can suppress logical errors indefinitely as long as physical error rates remain below a threshold value. In practice, multiple interdependent factors conspire to produce a nonlinear divergence in resource requirements, rendering commercial-scale deployment physically infeasible despite laboratory-scale demonstrations.

Quantum Error Correction (QEC), particularly through surface codes, is intended to enable fault tolerance by encoding logical qubits across thousands of physical qubits (Fowler et al., 2012). However, the overhead is immense: estimates consistently place the requirement at 1,000 to 10,000 physical qubits per logical qubit, depending on error rates and code distance (Terhal, 2015). For meaningful applications—for instance, breaking 2048-bit RSA encryption—this translates to tens of millions of physical qubits (Gidney & Ekerå, 2021; Gidney, 2017). Current state-of-the-art processors have recently surpassed 1,000 physical qubits, yet none have demonstrated functional logical qubits at scale (IBM Quantum, 2023). More troubling, recent experiments show that existing systems operate in a *crossover regime*, where larger codes do not reliably outperform smaller ones. Data from a 72-qubit device implementing a distance-5 surface code revealed only a 4% reduction in logical error rate compared to smaller codes, with simulations indicating that component performance must improve by over 20% to definitively cross below the fault-tolerance threshold (Google Quantum AI, 2023). At current error levels, increasing code size yields diminishing returns; slight degradations in gate fidelity would reverse the trend entirely, causing larger codes to perform worse—a hallmark of a phase transition.

This instability is exacerbated by correlated errors, which standard QEC protocols are ill-equipped to handle. High-energy events, such as cosmic ray impacts, induce bursts of errors across dozens of qubits simultaneously, overwhelming local decoding algorithms (Vepsäläinen et al., 2020; Google Quantum AI, 2023). Such events occur roughly once per hour in current devices, imposing a hard floor on logical error rates around $10^{-7}$, independent of further coding improvements (Google Quantum AI, 2023). Similarly, operator imprecision—systematic errors in gate calibration—accumulates coherently across circuits, behaving mathematically like decoherence and evading detection by stabilizer measurements (Alicki et al., 2010). Because these errors affect all qubits in a code block uniformly, they cannot be distinguished from legitimate quantum evolution, making them invisible to conventional error correction. Simulations show that even small rotation errors accumulate over the deep circuits required for algorithms like Shor’s, reducing success probabilities to levels indistinguishable from classical search methods (Alicki et al., 2010).

Material defects further constrain scalability. Two-level systems (TLS) at interfaces and surfaces are the dominant source of energy relaxation ($T_1$ decay) in superconducting qubits (Wang et al., 2015; Khalil et al., 2012). These defects arise from fabrication residues and native oxides, and their distribution is non-uniform, leading to significant variability in qubit performance (Hover et al., 2012). Efforts to mitigate TLS density through improved lithography (e.g., short-liftoff processes) yield measurable improvements, but eliminating them entirely is likely impossible with current materials (Hover et al., 2012). Additionally, flux noise in superconducting loops correlates with material disorder, suggesting a fundamental link between microscopic imperfections and decoherence mechanisms (de Graaf et al., 2018). Even if individual qubit lifetimes are extended, low-frequency noise causes pure dephasing, limiting overall coherence times regardless of $T_1$ improvements (Place et al., 2021). These effects do not scale linearly; they introduce heterogeneity and unpredictability that grow with system size, undermining the uniformity required for effective error correction.

A modified scaling model captures this collapse: $S_{\mathrm{effective}} = 2^L \times F^D \times C$, where $L$ is logical qubit count, $F$ is gate fidelity, $D$ is circuit depth, and $C$ is connectivity. The term $F^D$ illustrates how fidelity decays exponentially with depth; at 99.9% single-qubit fidelity, a 1,000-gate circuit retains only ~37% of its initial fidelity. Multi-qubit gates, essential for entanglement, exhibit lower fidelities (~99%), accelerating error accumulation (Arute et al., 2019). This model explains why noisy intermediate-scale quantum (NISQ) devices fail to achieve exponential scaling: effective computational power grows polynomially, if at all. The transition from laboratory feasibility to commercial viability is not gradual—it is punctuated by a phase change where accumulated imperfections overwhelm control mechanisms. There is no evidence that this transition can be avoided through engineering alone; it appears to be a consequence of the physical embedding of information in matter.

## Synthesis: Toward a Physically Grounded Framework for Computation

The preceding analysis reveals a fundamental tension between two paradigms: one rooted in abstract mathematical formalism, exemplified by Shor’s algorithm, and another grounded in physical law, embodied by Landauer’s principle. The former posits that computation can transcend material constraints through clever algorithmic design; the latter insists that all computation is bound by thermodynamics, noise, and irreversibility. Historical development has privileged the first, but empirical evidence increasingly supports the second. To advance the field constructively, a shift in epistemological priority is required—one that treats physical realizability as the primary criterion for evaluating computational models.

Shor’s algorithm, while mathematically sound, functions as a theoretical artifact defined in a regime of unbounded resources and perfect control. Its influence has been to anchor the justification for quantum computing to a task that may never be physically executable, thereby diverting focus from more tractable problems. In contrast, Landauer’s work provides a methodological framework for assessing any computational scheme based on its consistency with known physical laws. His insistence on accountability for entropy generation, noise susceptibility, and control precision offers a robust filter for distinguishing plausible technologies from speculative constructs.

The observation of a scaling phase transition in real quantum hardware—the point at which increased size leads to increased error rather than suppression—confirms the predictive power of a physics-first approach. Resource requirements diverge not due to temporary engineering limitations, but because of intrinsic couplings between information, matter, and energy. Correlated errors, material defects, and operator imprecision are not bugs to be fixed, but features of a system operating under physical constraints.

Therefore, the path forward lies not in pursuing ever-larger implementations of currently infeasible algorithms, but in developing computational models that explicitly incorporate physical bounds from the outset. This includes exploring alternative paradigms such as analog Hamiltonian simulation, neuromorphic computing, or reversible logic architectures that align more closely with thermodynamic principles. It also requires adopting Landauer’s call for intellectual honesty: disclaimers acknowledging the speculative nature of proposed systems should accompany all claims of exponential advantage. Only by centering physical reality can the field move beyond mathematical curiosities toward genuinely transformative technologies.

### References

Alicki, R., Horodecki, M., Horodecki, P., & Horodecki, R. (2010). On thermal stability of topological qubit in Kitaev’s 4D model. *Open Systems & Information Dynamics*, 17(1), 1-16. DOI: 10.1142/s1230161210000016

Arute, F., Arya, K., Babbush, R., et al. (2019). Quantum supremacy using a programmable superconducting processor. *Nature*, 574(7779), 505–510. DOI: 10.1038/s41586-019-1666-5

Bennett, C. H. (2003). Notes on Landauer’s principle, reversible computation, and Maxwell’s demon. *Studies in History and Philosophy of Science Part B: Studies in History and Philosophy of Modern Physics*, 34(3), 501–510. DOI: 10.1016/S1355-2198(03)00039-X

de Graaf, S. E., Danilov, A. V., Adamyan, A. A., & Kubatkin, S. E. (2018). Low-frequency magnetic flux noise in niobium superconducting rings. *Physical Review B*, 97(1), 014502. DOI: 10.1103/PhysRevB.97.014502

DiVincenzo, D. P. (1995). Quantum computation. *Science*, 270(5234), 255–261. DOI: 10.1126/science.270.5234.255

Dyakonov, M. I. (2018). The Case Against Quantum Computing. *IEEE Spectrum*, 55(11), 40-45. DOI: 10.1109/MSPEC.2018.8529941

Fowler, A. G., Mariantoni, M., Martinis, J. M., & Cleland, A. N. (2012). Surface codes: Towards practical large-scale quantum computation. *Physical Review A*, 86(3), 032324. DOI: 10.1103/PhysRevA.86.032324

Gidney, C. (2017). Factoring with n+ 2 clean qubits and n-1 dirty qubits. *arXiv preprint arXiv:1706.07884*.

Gidney, C., & Ekerå, M. (2021). How to factor 2048 bit RSA integers in 8 hours using 20 million noisy qubits. *Quantum*, 5, 433. DOI: 10.22331/q-2021-04-15-433

Goldreich, O. (2005). On promise problems (a survey in memory of Shimon Even [1935-2004]). *Electronic Colloquium on Computational Complexity (ECCC)*, 12(024).

Google Quantum AI. (2023). Suppressing quantum errors by scaling a surface code logical qubit. *Nature*, 614(7949), 676–681. DOI: 10.1038/s41586-022-05434-1

Hover, D., Chen, J., Pritchett, E. J., Marx, E., & McDermott, R. (2012). Impact of interface layers on qubit relaxation. *Applied Physics Letters*, 100(20), 202603. DOI: 10.1063/1.4719101

IBM Quantum. (2023, December 4). *IBM Debuts Next-Generation Quantum Processor & IBM Quantum System Two*. IBM Research Blog.

Khalil, M. S., Stoutimore, M. J. A., Wellstood, F. C., & Osborn, K. D. (2012). An analysis method for asymmetric resonator transmission applied to superconducting devices. *Journal of Applied Physics*, 111(5), 054510. DOI: 10.1063/1.3692073

Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM Journal of Research and Development*, 5(3), 183–191. DOI: 10.1147/rd.53.0183

Landauer, R. (1991). Information is physical. *Physics Today*, 44(5), 23–29. DOI: 10.1063/1.881299

Landauer, R. (1995). Is quantum mechanics useful?. *Philosophical Transactions of the Royal Society of London. Series A: Physical and Engineering Sciences*, 353(1703), 367-376. DOI: 10.1098/rsta.1995.0106

Landauer, R. (1996). The physical nature of information. *Physics Letters A*, 217(4-5), 188–193. DOI: 10.1016/0375-9601(96)00453-7

Levin, L. A. (2003). The tale of one-way functions. *Problems of Information Transmission*, 39(1), 92-103.

Martín-López, E., Laing, A., Lawson, T., Alvarez, R., Zhou, X. Q., & O’Brien, J. L. (2012). Experimental realisation of Shor’s quantum factoring algorithm using qubit recycling. *Nature Photonics*, 6(11), 773-776.

Place, A. P. M., Rodgers, L. V. H., Mundada, P., Smitham, B. M., Fitzpatrick, M., Leng, Z., ... & Houck, A. A. (2021). New material platform for superconducting transmon qubits with coherence times exceeding 0.3 milliseconds. *Nature Communications*, 12(1), 1-7. DOI: 10.1038/s41467-021-22030-5

Shor, P. W. (1994). Algorithms for quantum computation: discrete logarithms and factoring. In *Proceedings 35th annual symposium on foundations of computer science* (pp. 124-134). IEEE. DOI: 10.1109/SFCS.1994.365700

Terhal, B. M. (2015). Quantum error correction for quantum memories. *Reviews of Modern Physics*, 87(2), 307. DOI: 10.1103/RevModPhys.87.307

Vepsäläinen, A. P., Karamlou, A. H., Orrell, J. L., Dogra, A. S., Loer, B., Vasconcelos, F., ... & Oliver, W. D. (2020). Impact of ionizing radiation on superconducting qubit coherence. *Nature*, 584(7822), 551-556. DOI: 10.1038/s41586-020-2619-8

Wang, C., Axline, C. J., Gao, Y. Y., Brecht, T., Frunzio, L., Devoret, M. H., & Schoelkopf, R. J. (2015). Surface participation and dielectric loss in superconducting qubits. *Applied Physics Letters*, 107(16), 162601. DOI: 10.1063/1.4934486
