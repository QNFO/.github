---
author: Rowan Brad Quni-Gudzinas
ORCID: 0009-0002-4317-5604
ISNI: 0000000526456062
title: Physics-Bounded Computational Substrate
aliases:
  - Physics-Bounded Computational Substrate
modified: 2025-12-17T18:22:23Z
---

# Physics-Bounded Computational Substrate

## A Brief Synthesis of Thermodynamic Limits in Analog and Quantum Information Processing

**Author:** Rowan Brad Quni-Gudzinas
**Contact:** rowan.quni@outlook.com
**ORCID:** [0009-0002-4317-5604](https://orcid.org/0009-0002-4317-5604)
**ISNI:** [0000000526456062](https://isni.org/isni/0000000526456062)
**DOI:** 10.5281/zenodo.17967800
**Date:** 2025-12-17
**Version:** 1.0

> The physical realization of any computational model is fundamentally bounded not by algorithmic complexity alone, but by the thermodynamic and quantum statistical limits of its substrate, a constraint that recasts computationally hard problems as problems of physical resource scaling and forces a distinction between abstract universality and practical realizability.

## The Foundational Constraint: Energy Scales and Information Resolution

The core argument advanced by Quni-Gudzinas (2025) is that computation is a physical process whose fidelity is governed by the energy landscape of the substrate. In analog systems designed to map mathematical problems like integer factorization onto physical dynamics, the correct solution corresponds to a specific state within the system’s energy spectrum. The ability to resolve this state depends on the spectral gap, ($\Delta E$), separating it from nearby incorrect states. As the problem size ($N$) increases, number-theoretic bounds (Ford, 2008) dictate that the density of potential solutions increases, causing ($\Delta E$) to shrink super-logarithmically. Concurrently, any substrate at a temperature ($T > 0$) is subject to thermal noise of magnitude ($k_B T$). The computation fails—the signal is swamped—when ($\Delta E \lesssim k_B T$). This establishes a non-algorithmic, thermodynamic “hardness”: for a given physical substrate with a fixed operating temperature and characteristic energy, there exists a maximum problem complexity beyond which reliable computation is physically impossible.

This principle directly critiques paradigms like room-temperature photonic analog computing. While photonic systems can possess high characteristic frequencies ($\omega_0$), the ($k_B T$) noise floor at 300 Kelvin (~26 meV) is immense. For a problem like factoring a 2048-bit integer, the required spectral gap, derived from the physical encoding of the problem, is many orders of magnitude smaller than this thermal noise (Quni-Gudzinas, 2025). Therefore, despite the speed of light propagation and low decoherence of photons, the analog “signal” of the answer is irretrievably lost to thermal agitation before it can be read. This is not a failure of photonics per se, but a demonstration of the thermodynamic swamping limit applied to a specific physical instantiation.

## The Illusion of “Free” Quantum Speedup and the Error Correction Imperative

The thermodynamic argument extends critically to quantum computation. A naive interpretation of quantum speedup suggests that superposition and entanglement allow a quantum processor to “explore” an exponential space without exponential physical resources. However, maintaining the coherent superposition necessary for algorithms like Shor’s factorization requires isolating the system from environmental noise that induces decoherence. The energy scale of this noise is again governed by ($k_B T$). As Preskill (1998) articulated in the context of fault-tolerant quantum computing, the central challenge is to manage decoherence faster than it occurs.

The synthesis reveals that the thermodynamic swamping limit and decoherence are manifestations of the same physical constraint: the competition between the energy scales of the computational process and the environment. Digital gate-based quantum computing attempts to circumvent this not by avoiding the limit, but by engineering around it through quantum error correction (QEC). QEC creates a hierarchy where many noisy physical qubits, each susceptible to thermal and control errors, are entangled to form a single, better-protected logical qubit (Fowler, Mariantoni, Martinis, & Cleland, 2012). The overhead is staggering, often requiring thousands of physical qubits per logical one. This overhead is the direct, practical cost of fighting the thermodynamic limit; it transforms the challenge from one of pure physics to one of physical resource scaling. The claim that large-scale quantum factorization is possible is contingent on the assumption that this physical overhead—itself subject to engineering limits like qubit yield and connectivity—can be successfully managed.

## Topological Protection as a Physical, Not Abstract, Advantage

The analysis of topological systems within this framework clarifies their potential and limits. A topological qubit, such as the theorized Majorana zero mode, encodes information in a global state that is not local to any single particle (Nayak, Stern, Freedman, & Das Sarma, 2008). Its purported robustness stems from a topological energy gap ($\Delta_{top}$) that suppresses local noise events. The thermodynamic perspective asks a crucial question: How does ($\Delta_{top}$) compare to ($k_B T$) and other relevant energy scales in the material?

A topological gap is a material property. If ($\Delta_{top}$) of a candidate system is 1 meV, then at a temperature where ($k_B T \approx 1$) meV (about 10 K), the protection mechanism becomes ineffective. Thus, the search for high-temperature topological quantum computing is fundamentally a materials science problem to maximize ($\Delta_{top}$). This grounds an otherwise abstract mathematical advantage in concrete solid-state physics. It also explains why proposed realizations often require extreme conditions (e.g., low temperatures, high magnetic fields): these are necessary to make the protective energy gap dominant over environmental noise. Room-temperature operation would require a topological gap on the order of 25 meV or larger, a significant challenge for known materials.

## The Universe as a Computational Limit Case

The most profound synthesis emerges from considering the cosmological scale. Quni-Gudzinas (2025) posits that the Planck-scale vacuum is the only substrate with a characteristic energy (($E_P \sim 10^{19}$) GeV) high enough to trivially overcome the swamping limit for any physically meaningful computation. In this view, the universe’s evolution *is* a computational process operating at this ultimate energy scale. The observed cosmological constant, or dark energy, is reinterpreted not as a mysterious field but as the dissipative cost of this computation, consistent with Landauer’s principle linking information erasure to entropy production (Landauer, 1961).

This aligns with the speculative “It from Qubit” paradigm in quantum gravity, which posits that spacetime and gravity emerge from entangled quantum degrees of freedom (Susskind, 2016). Here, the universe’s most fundamental “substrate” is quantum information. The thermodynamic constraints do not disappear but are elevated to a cosmic scale; the holographic principle suggests the information content of a volume is bounded by its surface area, a geometric manifestation of an information cap (Bousso, 2002). Therefore, the ultimate computer is the universe itself, and its operating specifications—the Planck energy, the cosmological constant—define the absolute limits of information processing within it. Any terrestrial computer is a limited, low-energy fragment of this process, forever battling the noise from which the cosmic system is largely insulated.

## Synthesis: Redefining Hardness and the Path Forward

The consilience of these ideas forces a reevaluation of computational “hardness.” Classically, hardness is an intrinsic property of a problem (e.g., NP-hardness). The physical view reveals a dual: **substrate-dependent hardness**. A problem may be algorithmically hard but physically easy if mapped onto a system with a sufficiently dominant energy scale (like the Planck vacuum). Conversely, an easy problem can be physically hard for a noisy, warm substrate.

The practical path for quantum and analog computing is thus refined:

1.  **Problem-Substrate Co-Design**: The choice of computational problem must be matched to the physical strengths of the substrate. Photonic neural networks for optimization, for instance, may thrive at room temperature because they do not require the exponentially precise spectral resolution of analog factorization.
2.  **Embracing Hybrid Models**: The future likely lies in hybrid systems where quantum or analog co-processors handle specific, physics-friendly subroutines, while classical computers manage control, error correction, and higher-level logic.
3.  **Reinterpreting Claims**: A claim of “quantum supremacy” or “analog efficiency” must be evaluated against the specific problem solved and the scalability of the substrate’s physical parameters (gap, temperature, coherence time, error rates) with problem size. Demonstrating an advantage for a toy problem is necessary but not sufficient; the path through the thermodynamic swamp must be charted.

The ultimate conclusion is that there is no free lunch in physical computation. Every operation, every bit of information processed, pays a thermodynamic tariff. The grand challenge of next-generation computing is not merely to build a better abstract machine, but to engineer a physical system that can pay this tariff for the problems we care about, whether through error correction, topological protection, or radical new materials.

## References

Bousso, R. (2002). The holographic principle. *Reviews of Modern Physics, 74*(3), 825–874. https://doi.org/10.1103/RevModPhys.74.825

Ford, K. (2008). The distribution of integers with a divisor in a given interval. *Annals of Mathematics, 168*(2), 367–433. https://doi.org/10.4007/annals.2008.168.367

Fowler, A. G., Mariantoni, M., Martinis, J. M., & Cleland, A. N. (2012). Surface codes: Towards practical large-scale quantum computation. *Physical Review A, 86*(3), 032324. https://doi.org/10.1103/PhysRevA.86.032324

Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM Journal of Research and Development, 5*(3), 183–191. https://doi.org/10.1147/rd.53.0183

Nayak, C., Stern, A., Freedman, M., & Das Sarma, S. (2008). Non-Abelian anyons and topological quantum computation. *Reviews of Modern Physics, 80*(3), 1083–1159. https://doi.org/10.1103/RevModPhys.80.1083

Preskill, J. (1998). Reliable quantum computers. *Proceedings of the Royal Society of London. Series A: Mathematical, Physical and Engineering Sciences, 454*(1969), 385–410. https://doi.org/10.1098/rspa.1998.0167

Quni-Gudzinas, R. B. (2025). *Topological hydrodynamics and the spectral gap: Defining the thermodynamic limits of analog vacuum computation*. Zenodo. https://doi.org/10.5281/zenodo.17965042

Susskind, L. (2016). Computational complexity and black hole horizons. *Fortschritte der Physik, 64*(1), 24–43. https://doi.org/10.1002/prop.201500093
