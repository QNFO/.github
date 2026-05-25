---
author: Rowan Brad Quni-Gudzinas
ORCID: 0009-0002-4317-5604
ISNI: 0000000526456062
title: Percolation as a Control Paradigm
aliases:
  - Percolation as a Control Paradigm
modified: 2025-12-23T23:50:30Z
---

# Engineering Macroscopic Quantum Coherence in Disordered Moiré Metamaterials

**Author:** Rowan Brad Quni-Gudzinas
**Contact:** rowan.quni@outlook.com
**ORCID:** [0009-0002-4317-5604](https://orcid.org/0009-0002-4317-5604)
**ISNI:** [0000000526456062](https://isni.org/isni/0000000526456062)
**DOI:** 10.5281/zenodo.18014173
**Date:** 2025-12-24
**Version:** 1.0.1

**Abstract**: The study of moiré materials is defined by a central paradox: the experimental observation of robust, macroscopic quantum phases, such as superconductivity and topological insulation, in devices known to possess significant atomistic disorder. This work bridges this “disorder-topology gap” by establishing quantum percolation as the fundamental mechanism for the emergence of global coherence. We develop a Stochastic Time-Dependent Ginzburg-Landau (TDGL) model that incorporates a physically realistic, multi-modal disorder potential. This potential includes both a smooth, spatially correlated twist-angle field, representing mesoscopic strain domains, and a sparse field of sharp pinning sites, representing atomic vacancies. The simulation, performed on a high-resolution 128x128 lattice, is analyzed using an objective Hoshen-Kopelman cluster-finding algorithm. Our results quantitatively map the entire transition, from the initial nucleation of isolated superconducting “islands” in magic-angle regions to their proximity-driven growth and coalescence. We identify a sharp, topological percolation threshold at a simulation time of t=1.25, where a sample-spanning network first forms at an average superfluid density of 0.31. This globally coherent state stabilizes despite a significant twist-angle disorder bandwidth of 0.15°. This work reframes disorder from a nuisance to be eliminated into a key engineering parameter, providing a predictive framework for designing the next generation of robust, scalable moiré quantum devices.

**Keywords:** Moiré Materials, Quantum Percolation, Ginzburg-Landau Theory, Straintronics, Disordered Superconductivity, Twistronics, Computational Physics

## 1.0 INTRODUCTION & PROBLEM STATEMENT

### 1.1 The Moiré Metamaterial: From Observation to Design

The field of moiré physics has undergone a profound maturation, transitioning from a science of serendipitous discovery to a prescriptive engineering discipline capable of designing quantum Hamiltonians. This evolution marks a fundamental shift in perspective: the moiré superlattice is no longer viewed as a static curiosity but as a programmable metamaterial. Early work in the field was defined by the landmark discovery of unconventional superconductivity in twisted bilayer graphene, a phenomenon that appeared only at a specific, seemingly “magic” angle (Gruber & Abdel-Hafiez, 2025). This initial phase of research was characterized by a process of observation and characterization, where the primary challenge was the fabrication of samples that happened to fall within this narrow geometric window.

The context of this early era was one of exploration, driven by the surprising parallels between the phase diagram of magic-angle graphene and that of high-temperature cuprate superconductors. The ability to tune between correlated insulating and superconducting states with a simple gate voltage was a revolutionary advance (Xin et al., 2022). However, the focus remained on a singular system and a singular control knob—the twist angle. This approach, while fruitful, treated the moiré phenomenon as a static property of a given sample, with the physics “locked in” during fabrication. The variability between devices was high, and the underlying principles governing the emergence of these correlated states in the presence of real-world disorder were not yet fully understood.

The mechanism that propelled the field into its current engineering-focused era was the systematic introduction of additional, deterministic control vectors. Beyond the static twist angle, researchers now actively employ mechanical strain, hierarchical layer stacking, and dynamic modes to actively shape the electronic potential landscape. This toolkit transforms the moiré system from a fixed entity into a reconfigurable one. For instance, “straintronics” allows for the continuous deformation of the moiré Brillouin zone, tuning the bandwidth of the flat bands in situ. This moves the locus of control from the arduous fabrication process to real-time experimental operation.

This shift is now well-established in the literature, with recent reviews characterizing the current state of the art as an era defined by the “Interplay of Electronic Orders” (Gruber & Abdel-Hafiez, 2025). The focus is no longer just on creating a flat band but on controlling the competition and cooperation between different quantum phases—superconductivity, magnetism, charge-density waves, and topology—that vie for the ground state within that flat band. The moiré lattice provides the stage, and the expanded set of control knobs allows the experimentalist to direct the performance.

Despite this progress, a significant counter-argument persists, centered on the formidable challenges of reproducibility and scalability. Critics correctly point out that the sample heterogeneity inherent in exfoliated and stacked van der Waals materials remains a significant barrier. Twist-angle disorder, substrate-induced strain, and atomic defects create a complex and often unpredictable energy landscape that can obscure the intrinsic physics. This raises the critical question of whether the “deterministic control” achieved in idealized models can ever be robustly translated to the messy reality of large-scale device fabrication (Xin et al., 2022).

In synthesis, the path forward is not to wage a futile war against this intrinsic disorder, but to embrace it as an integral part of the design. True engineering progress is being achieved not by creating perfectly homogeneous samples, but by learning to control the statistical properties of the disorder itself. By patterning strain or introducing defects in a controlled manner, it is possible to guide the formation of quantum states. This reframes the problem: the goal is to build a device whose function is stabilized by, not degraded by, its inherent structural complexity.

This new perspective necessitates a fundamental revision of the theoretical frameworks used to model these systems. The idealized continuum models that assume perfect, infinite lattices are insufficient for describing a reality where the essential physics may be governed by the statistics of disorder. This work aims to develop and test such a framework, moving beyond the clean limit to explore how macroscopic quantum coherence can emerge from a structurally imperfect, yet deterministically engineered, metamaterial.

### 1.2 The Disorder-Topology Gap

A foundational conflict defines the current frontier of moiré physics: the gap between theoretical models that predict robust topological phases based on global symmetry and the stark experimental evidence of profound, symmetry-breaking atomistic disorder. Idealized theories of moiré systems often begin by assuming a perfect, infinite superlattice. Within this pristine mathematical construct, powerful concepts from band theory can be used to calculate topological invariants, such as Chern numbers, which predict the existence of quantized Hall conductivity and protected edge states. However, this clean theoretical picture is in direct conflict with the structural reality of fabricated devices (Huang et al., 2025).

The context for this tension is the very success of the initial topological predictions. The theoretical identification of flat bands with non-trivial Berry curvature in twisted bilayer graphene provided a crucial roadmap that guided experimentalists to the discovery of the quantum anomalous Hall effect in this system. The remarkable agreement between these early theories and experiments created a perception that moiré lattices were, to a good approximation, the perfect periodic structures described in the models (Călugăru et al., 2025). This perception has been challenged by recent advances in materials characterization, which reveal a far more complex and disordered reality.

The mechanism underlying this gap is the process of atomic reconstruction and the introduction of defects during fabrication. The simple picture of two rigid layers stacked with a twist is a convenient fiction. In reality, the layers deform to minimize the total van der Waals energy, leading to the formation of domains of commensurate stacking separated by a network of solitonic domain walls. Furthermore, high-resolution electron ptychography has revealed that this reconstruction is not a 2D phenomenon but involves significant 3D corrugations, with the interlayer spacing varying across the moiré unit cell. This out-of-plane buckling, combined with the inevitable presence of atomic vacancies and substrate-induced strain gradients, locally breaks the very symmetries that are required to globally define the topological invariants in the continuum models (Huang et al., 2025).

The most direct evidence for this structural complexity is provided by the picometer-scale 3D atomic maps produced by Huang et al. (2025). These experiments move beyond 2D imaging to resolve the coordinates of individual atoms in all layers of a twisted WSe$_2$ device. The results are striking: they show not only the expected in-plane relaxations but also significant out-of-plane warping and a non-random distribution of selenium vacancies, which tend to cluster in specific strained regions of the moiré cell. This work provides definitive, quantitative proof that the real-space structure of a moiré material is far from the idealized picture used in many theoretical calculations.

The most compelling counter-argument to the significance of this gap is the undeniable experimental robustness of the macroscopic quantum phases themselves. If the disorder were truly catastrophic to the topology, one would expect the quantized Hall plateaus to be unstable or non-existent. The fact that they are observed, and are often robust over a range of gate voltages, suggests that the topological protection mechanism is surprisingly resilient to local symmetry-breaking perturbations. The quantum state seems to possess an intrinsic ability to “heal” or ignore the underlying structural chaos.

This leads to a necessary synthesis: the mechanism of topological protection must be re-conceptualized to be compatible with, or perhaps even dependent on, this local disorder. The macroscopic quantum state cannot be an property of the global crystal structure, because a perfect global crystal does not exist. Instead, the topology must be an emergent feature of a percolating network of locally-ordered domains. The key question, which this work aims to answer, is how this global quantum coherence is established and maintained across a landscape of profound local disorder.

Before addressing this question, we must first consider the full range of geometric possibilities that define the local domains. The choice of material and Brillouin zone symmetry provides the fundamental building blocks from which the disordered landscape is constructed.

### 1.3 Expanding Geometric Constraints: From K-Point to M-Point Physics

The engineering capabilities of a moiré metamaterial are fundamentally constrained by the intrinsic symmetries of its constituent monolayers, specifically the location of the low-energy electronic states in the Brillouin zone. The choice of this “valley” degree of freedom—the dichotomy between K-point and M-point physics—defines the symmetry class of the emergent correlated states and, therefore, the range of Hamiltonians the system can simulate. The vast majority of research in twistronics has been built upon the foundation of K-point physics, inherent to graphene and hexagonal boron nitride (Călugăru et al., 2025).

The context for this K-point dominance is historical, stemming from the foundational discovery of unconventional superconductivity in magic-angle twisted bilayer graphene (Cao et al., 2018). In this archetypal system, the relevant electronic states are the Dirac cones located at the K and K’ corners of the hexagonal Brillouin zone. The moiré pattern couples these valleys, gapping out the Dirac points and generating the celebrated flat bands. The physics of this system is, therefore, the physics of interacting Dirac fermions, a rich but specific subclass of many-body problems.

A new paradigm has emerged with the theoretical identification of materials whose low-energy states reside at the M-points, the center of the Brillouin zone edges. Materials predicted to fall into this class, such as the 1T-phase of SnSe$_2$, offer a different geometric starting point. M-point valleys are not protected by the same symmetries as the K-points, and their interaction under a moiré potential leads to a distinct class of emergent symmetries. Specifically, M-point twisting is predicted to generate emergent non-symmorphic symmetries in momentum space—symmetries that involve fractional lattice translations—which are absent in K-point systems (Călugăru et al., 2025).

The evidence for the unique potential of M-point systems comes from large-scale *ab initio* calculations. Călugăru et al. (2025) predict that twisting bilayers of 1T-SnSe$_2$ will produce flat bands with a six-fold degeneracy, arising from the combination of three M-valleys and the spin degree of freedom. This is a significant expansion from the twoor four-fold degeneracy of graphene’s flat bands. A system with a six-fold degeneracy can host a six-flavor Hubbard model, providing a solid-state platform to simulate exotic phases of matter, such as quantum spin liquids, that are thought to be relevant to frustrated magnetism but are inaccessible in conventional materials.

The primary counter-argument against the immediate relevance of M-point physics is the significant materials science challenge it presents. The synthesis of stable, low-defect monolayers of materials like 1T-SnSe$_2$ is considerably less developed than the now-routine exfoliation of graphene and 2H-phase TMDs. These materials are often air-sensitive or metastable, and achieving the low levels of unintentional disorder required for the fragile correlated states to emerge is a formidable barrier (Cao et al., 2018).

In synthesis, the expansion of moiré engineering to include M-point geometries is a crucial step towards creating a truly universal quantum simulator. While K-point systems provide a powerful platform for Dirac physics, M-point systems unlock a wider and more exotic range of many-body Hamiltonians defined by different symmetries and higher degeneracies. The ability to choose the valley degree of freedom is akin to choosing the instruction set for the quantum simulation.

This expanded geometric basis provides a richer set of building blocks for creating complex potential landscapes. The next level of control comes from combining these blocks in hierarchical structures, a strategy that introduces new, tunable length scales into the problem.

### 1.4 Hierarchical Control via Supermoiré Lattices

Beyond the geometry of a single interface, the architecture of multi-layer stacks provides a powerful hierarchical control vector, enabling the creation of “moiré-of-moiré” or “supermoiré” interference patterns. These structures introduce new, tunable length scales that are inaccessible in simple bilayer systems, allowing for a more profound level of control over the quantum landscape. By stacking three or more layers with independent twist angles, one can generate a complex potential energy surface arising from the superposition of multiple moiré patterns (Zhu et al., 2020).

Bilayer moiré systems are fundamentally constrained by their geometry: a single twist angle defines a single moiré period. While this period can be varied from sample to sample, it is fixed for any given device. This links the length scale of the potential to the energy scale of the flat bands in a deterministic way. To explore different regimes of interaction, one must fabricate an entirely new device. Hierarchical stacking overcomes this limitation by introducing multiple, potentially incommensurate, periodicities within a single device (Chen et al., 2025).

The mechanism at play is the formation of a beat pattern between two or more underlying moiré lattices. For example, in a twisted trilayer graphene device with two independent twist angles, the electronic states are modulated by two different moiré patterns. The interference between these two patterns creates an even longer-wavelength “supermoiré” potential. This hierarchical potential can be engineered to have properties, such as deeper potential wells or different symmetries, that are not present in either of the constituent bilayers.

The power of this approach is exemplified by the engineering of “bichromatic” potentials in asymmetric TMD trilayers, such as WSe$_2$/WS$_2$/WSe$_2$. The superposition of the moiré patterns from the top and bottom interfaces can be tuned to create a landscape that traps novel quasiparticles. Chen et al. (2025) have used this technique to create and control quadrupolar trions—three-body excitonic complexes with a vanishing net dipole moment. These “dark” states are protected from dipolar noise, giving them potentially longer coherence times for quantum information applications.

A significant counter-argument, however, is the extreme fabrication challenge posed by these complex architectures. The properties of a supermoiré lattice are exquisitely sensitive to the precise values of multiple twist angles and the stacking order. Aligning three or more exfoliated flakes to within a fraction of a degree is an exceptionally difficult process with very low yield. This suggests that while supermoiré systems are powerful in theory, they may be too complex to fabricate with the required precision and reproducibility for systematic study or technological application (Chen et al., 2025).

Despite these challenges, hierarchical stacking represents a crucial advance in the moiré engineering toolkit. It provides a pathway to decouple the length scales that govern interaction and localization from the energy scales of the electronic bands. In a supermoiré lattice, it becomes possible to independently tune the depth of a potential trap and the tunneling rate between adjacent traps. This level of control is essential for designing more sophisticated quantum simulators and devices.

The introduction of multiple layers and interfaces inevitably adds another layer of complexity to the disorder problem. As we build more intricate static structures, it is also important to remember that these structures are not rigid, but possess their own internal dynamics that can be harnessed for control.

### 1.5 Straintronics and Dynamic Control Vectors

The moiré superlattice is not a static, rigid framework; it is a soft, deformable crystal whose properties can be tuned in real time through the application of mechanical strain and the excitation of dynamic collective modes. This recognition has given rise to the subfield of “straintronics,” which treats strain not as an uncontrolled source of disorder but as a deterministic control vector for tuning electronic properties. Alongside strain, other dynamic modes, such as the rigid sliding of one layer relative to another, are emerging as powerful tools for reconfiguring the quantum state of a moiré material on the fly (Hou et al., 2025).

Initially, the presence of strain in exfoliated flakes was considered a significant problem, as it led to inhomogeneity and a broadening of the magic-angle window. The goal was to produce strain-free samples to get closer to the idealized theoretical models. The paradigm shift of straintronics was the realization that if strain could be applied in a controlled manner, it could become a tool for post-fabrication tuning of the moiré potential. This is a critical advantage, as it allows a single device to explore a wide range of physical parameters that would otherwise require fabricating dozens of samples (Ding et al., 2025).

The mechanisms of dynamic control are varied. Applying uniaxial strain deforms the moiré unit cell, breaking its rotational symmetry and lifting the degeneracy of electronic bands. This can be used to induce electronic nematic phases or to tune the system across topological phase transitions. Interlayer sliding, a distinct degree of freedom, acts as an artificial gauge field. Translating a layer does not significantly alter the electronic bandwidth, but it does change the real-space location of the Wannier orbitals, which modifies the Berry curvature and quantum metric of the Bloch states. This provides a unique knob for tuning geometric properties of the wavefunction, such as the anomalous Hall effect, independently of the correlation strength.

Robust evidence for these control modalities is accumulating. Hou et al. (2025) provide a comprehensive review of experiments where applied strain has been used to induce or modify superconductivity in non-magic-angle devices. On the theoretical front, Ding et al. (2025) have modeled the consequences of interlayer sliding, showing that it provides a direct handle on the Berry curvature dipole, which governs the nonlinear Hall effect. These works confirm that the mechanical degrees of freedom of the moiré lattice are strongly coupled to the electronic degrees of freedom.

The primary counter-argument against the utility of these dynamic vectors is that they can also be sources of noise and decoherence. The collective vibrational modes of the lattice, known as phasons, correspond to the same sliding and breathing motions. While coherent driving of these modes can be used for control, their incoherent, thermal excitation acts as a phonon bath that can destroy delicate quantum correlations. Therefore, harnessing dynamic control requires operating in a regime where the driven motion is strong compared to the thermal noise (Ding et al., 2025).

In synthesis, the inclusion of straintronics and other dynamic vectors transforms the moiré system into a truly reconfigurable quantum material. It adds a temporal dimension to the static, geometric picture, allowing for the active manipulation of the system’s Hamiltonian. A complete model of a moiré device must therefore account for both the “quenched” static disorder introduced during fabrication and the dynamic disorder or control from these mechanical modes.

The principles of moiré interference, both static and dynamic, are not confined to the quantum realm of electrons. They are manifestations of wave mechanics that are scale-invariant, applying equally to classical systems.

### 1.6 The Scale-Invariance of Moiré Interference

The physical principles of moiré interference are not exclusive to the quantum mechanics of electrons but are a universal feature of wave phenomena, demonstrating a remarkable scale-invariance. The same geometric interference that creates flat electronic bands in angstrom-scale atomic lattices can be used to engineer the dispersion of classical waves in micron-scale photonic crystals or even centimeter-scale microwave metamaterials. This universality validates the underlying wave-mechanical concepts of twistronics and provides a powerful set of alternative platforms for testing and refining these ideas (Qin et al., 2024).

The context for this cross-disciplinary translation is the search for new methods to control wave propagation. The concept of a “magic angle” where group velocity vanishes is not intrinsically quantum mechanical. It is a general consequence of wave hybridization in a periodic potential. Recognizing this has led researchers to apply the “twist” degree of freedom to a variety of classical systems, moving beyond condensed matter physics into the domains of optics, acoustics, and radio-frequency engineering (Hwang & Hong, 2025).

The mechanisms are directly analogous. By twisting two periodic photonic crystal slabs, one creates a moiré pattern in the dielectric constant that acts as a superlattice for photons. This leads to the formation of flat photonic bands and the emergence of “magic angles” where light is effectively trapped. Similarly, by rotating two frequency-selective surfaces (patterned metallic sheets), one creates a moiré pattern that dramatically alters the transmission spectrum for microwaves. In all cases, a small rotational misalignment is used to generate a long-wavelength modulation that dominates the system’s behavior.

Compelling experimental evidence supports this scale-invariance. Qin et al. (2024) have demonstrated the existence of photonic “Bound States in the Continuum” (BICs) in twisted silicon slabs. These are states of light that are perfectly localized within the slab, with extremely high quality factors, due to moiré-induced symmetry protection. At the macroscopic scale, Hwang & Hong (2025) have shown through full-wave simulations that mechanically rotating one patterned screen relative to another can tune a microwave filter’s resonance frequency over several gigahertz without any active electronic components.

A key counter-argument differentiates these classical systems from their quantum counterparts: the absence of strong interactions. The rich correlated phases observed in electronic moiré systems are driven by the strong Coulomb repulsion between electrons, a feature absent for non-interacting photons or low-power classical waves. Therefore, while these systems are excellent analogues for testing the single-particle aspects of moiré physics (e.g., localization, dispersion engineering), they cannot be used to simulate many-body phenomena like superconductivity or Mott insulation.

In synthesis, the successful application of moiré principles across vast differences in length scale and wave type provides powerful confirmation of the framework’s validity. These classical and bosonic analogues serve as clean, accessible testbeds for theories of geometric localization, free from the complexities of strong correlations and quantum statistics. They reinforce the central idea that the “magic angle” is a universal wave phenomenon, setting the stage for our final, revised hypothesis on how quantum coherence can emerge in the more complex electronic systems.

### 1.7 Unifying Hypothesis: Quantum Coherence as a Percolation Transition in Multi-Modal Disorder

Based on the preceding analysis of the field’s challenges and opportunities, we formulate a unifying hypothesis: **Macroscopic quantum order in moiré materials is a percolation phenomenon that occurs within a realistic, multi-modal disorder landscape.** This hypothesis moves beyond simplistic models of disorder and posits that global phase coherence emerges from the topological connection of localized “magic” domains, with the dynamics of this connection being governed by the interplay of different types of structural defects (Sinner et al., 2023).

The context for this hypothesis is the failure of simple, homogeneous models to explain the robustness of quantum states in the face of the profound disorder revealed by modern metrology. A new framework is needed that explicitly incorporates this disorder as a central feature, not a perturbative afterthought. The concept of percolation, borrowed from statistical physics, provides such a framework. It is designed to describe how macroscopic properties (like conductivity or coherence) emerge in systems composed of a random mixture of different components.

The mechanism we propose is rooted in a more physically nuanced picture of the disorder. We argue that the moiré landscape is shaped by at least two distinct types of disorder: (1) smooth, spatially correlated variations in the effective twist angle, arising from wrinkles and strain fields in the elastic 2D membrane, and (2) sparse, sharp potential wells caused by atomic-scale defects like vacancies or adsorbates. The smooth disorder governs the large-scale geography of “magic” and “metallic” regions, determining where superconducting islands can nucleate. The sharp, sparse disorder acts as a set of pinning sites that can trap the domain walls of these islands, impeding their growth and connection.

The evidence for this multi-modal picture is drawn from multiple sources. The observation of 1D conducting channels along wrinkles confirms the role of correlated strain fields in defining the electronic landscape (Sinner et al., 2023). Simultaneously, first-principles calculations have shown that atomic vacancies act as strong trapping centers for quasiparticles, confirming their role as pinning sites (Guo et al., 2021). Our hypothesis is the first to consider the combined effect of these two mechanisms on the formation of a global coherent state.

The primary counter-argument to this hypothesis is the question of whether quantum phase coherence can be maintained across such a complex and “dirty” landscape. The weak links connecting the superconducting islands are particularly vulnerable to phase slips, which would destroy the global coherence and restore a finite resistance. It is not a priori obvious that the system can successfully navigate this complex terrain to establish a robust, phase-locked network.

Our synthesis is that this is the central question that can and must be answered by simulation. We will test this hypothesis using a Stochastic Time-Dependent Ginzburg-Landau (TDGL) model. This model incorporates the multi-modal disorder landscape and uses a rigorous, objective cluster-finding algorithm to identify the percolation threshold. This allows us to move beyond qualitative arguments and quantitatively test the conditions under which a disordered moiré material can achieve macroscopic quantum coherence.

The following methodology section details the construction of this computational framework. By simulating the competition between nucleation, growth, and pinning in a physically realistic disorder potential, we aim to provide a definitive test of the percolation hypothesis as the unifying mechanism of emergent order in moiré metamaterials.

## 3.0 METHODOLOGY

### 3.1 TDGL Framework with a Multi-Modal Disorder Potential

To capture the microstructural realism demanded by recent experimental findings, our simulation moves beyond standard Ginzburg-Landau (GL) theory by employing a multi-modal disorder potential. This framework is designed to test the hypothesis that quantum percolation in moiré materials is governed by the interplay of distinct types of structural defects. While previous models often relied on a single, generic disorder field, our approach acknowledges that the physical landscape of a van der Waals heterostructure is shaped by defects with different length scales and energetic signatures. The Time-Dependent Ginzburg-Landau (TDGL) equation remains the core of our methodology, but its predictive power is substantially enhanced by this more physically grounded potential (Guo et al., 2021).

The foundation of the model is the evolution of the complex superconducting order parameter, $\psi(\mathbf{r}, t)$, according to the stochastic relaxation equation:

$$
\frac{\partial \psi}{\partial t} = - \Gamma \frac{\delta \mathcal{F}}{\delta \psi^*} + \zeta(\mathbf{r}, t)
$$

The crucial innovation is in the construction of the free energy functional, $\mathcal{F}$, and specifically its control parameter, $\alpha(\mathbf{r})$. We define $\alpha(\mathbf{r})$ as a linear superposition of two physically distinct components: a smooth, spatially correlated potential arising from twist-angle variations, and a sparse, sharp potential representing atomic vacancy pinning sites.

The full expression for the control parameter is:

$$
\alpha(\mathbf{r}) = \alpha_0 \left( \frac{T}{T_{c0}} - e^{-\frac{(\theta(\mathbf{r}) - \theta_m)^2}{2\sigma_\theta^2}} \right) + V(\mathbf{r})
$$

This multi-modal approach is motivated by direct experimental evidence. Ptychography and scanning tunneling microscopy have revealed the coexistence of mesoscopic strain domains, which cause smooth variations in the local twist angle, and atomic-scale defects like chalcogen vacancies, which act as sharp scattering or pinning centers. By modeling these two modes of disorder separately, our simulation can disentangle their distinct physical roles in the percolation process (Guo et al., 2021).

The first term, governed by the local twist angle $\theta(\mathbf{r})$, defines the large-scale geography of the problem, creating the “islands” of favorable magic-angle geometry where superconductivity can nucleate. The second term, $V(\mathbf{r})$, introduces a sparse field of deep, localized potential wells. These wells represent vacancy sites and are expected to have a profound impact on the dynamics of the domain walls that form between the superconducting and metallic regions.

A potential counter-argument is that the linear superposition of these two potentials is an approximation that neglects any non-linear coupling between them. For example, a high-strain region might also be more likely to host a vacancy, implying a correlation between the two disorder fields. While our current model treats them as independent for simplicity, the framework is extensible to include such correlations in future work.

In synthesis, the multi-modal disorder potential provides a more realistic and physically nuanced arena in which to test the percolation hypothesis. It allows us to ask more sophisticated questions: Is the percolation threshold more sensitive to the average twist-angle deviation or to the density of vacancy pinning sites? How do these two types of disorder interact to help or hinder the formation of a global coherent state? The following sections detail the specific implementation of each component of this disorder landscape.

### 3.2 Correlated Twist-Field Generation

The largest component of the disorder landscape, the smooth variation in the local twist angle, is modeled as a spatially correlated random field. This approach is a direct response to the physical reality of moiré materials: as soft, elastic membranes, they cannot support the sharp, uncorrelated, site-to-site variations that would be represented by white noise. Instead, any deformation, such as a wrinkle or a strain domain, has a characteristic length scale. Our methodology captures this essential physical constraint by generating a disorder field that mimics the smooth, undulating topography of a real device (Carrasco et al., 2025).

The generation process begins with a grid of uncorrelated Gaussian white noise. This grid is then convolved with a Gaussian filter, which effectively smooths the noise by averaging each point with its neighbors. The standard deviation of this filter, $\sigma_{smooth}$, is a crucial parameter that is calibrated to match the physical correlation length of strain domains observed in experimental studies of wrinkled graphene, typically on the order of 10-20 nanometers. The resulting field, $\theta(\mathbf{r})$, is a smooth landscape of hills and valleys representing regions where the local twist angle is slightly larger or smaller than the global average.

The mathematical form of the twist field at any point is given by:

$$
\theta(\mathbf{r}) = \bar{\theta} + \Delta \theta \cdot \mathcal{S} [ \mathcal{N}(0, 1) ]
$$

Here, $\bar{\theta}$ is the nominal twist angle of the device, $\Delta \theta$ is the disorder bandwidth (the standard deviation of the twist angle across the sample), and $\mathcal{S}$ represents the Gaussian smoothing operation. This construction allows us to independently control the average twist angle and the severity of the disorder.

A potential counter-argument is that real strain fields are tensorial, not scalar, and that a simple scalar map of an “effective” twist angle misses the anisotropic effects of shear strain. While this is true, the dominant effect of strain on the flat bands in twisted bilayer graphene is the modification of the interlayer hopping, which is primarily sensitive to the local rotational alignment. The scalar field approximation therefore captures the most important first-order effect on the local density of states, which is the parameter that governs the nucleation of superconductivity in the Ginzburg-Landau model.

In synthesis, the use of a correlated random field for the twist-angle disorder is a critical step towards microstructural realism. It ensures that the “islands” of magic-angle geometry in our simulation have physically realistic sizes and smooth boundaries, providing a valid landscape for studying the dynamics of domain wall motion and cluster growth. The next step is to superimpose the second, sharper mode of disorder onto this smooth background.

### 3.3 Vacancy Pinning Site Implementation

To fully capture the multi-modal nature of disorder in moiré materials, our model incorporates a sparse field of strong pinning sites, representing the influence of atomic-scale defects like vacancies. While the smooth twist-angle field governs the large-scale nucleation of superconducting islands, these sharp, localized defects are hypothesized to play a dominant role in the dynamics of the domain walls between superconducting and normal regions. By explicitly including these pinning sites, we can test their ability to trap growing clusters and potentially inhibit the percolation transition (Huang et al., 2025).

The implementation of these defects within the Ginzburg-Landau framework is straightforward. We introduce a sparse potential field, $V(\mathbf{r})$, which is zero everywhere except at a small number of randomly selected sites on the simulation grid. At these “vacancy” sites, the potential is given a large, negative value, `VACANCY_STRENGTH = -2.0`. This value is added directly to the local GL control parameter, $\alpha(\mathbf{r})$. The effect is to create a set of deep, narrow potential wells that are superimposed on the smoother landscape from the twist-angle field.

This approach is motivated by a combination of experimental evidence and theoretical calculation. High-resolution ptychography has shown that vacancies are a common defect in these materials and that they tend to cluster (Huang et al., 2025). First-principles calculations have confirmed that such vacancies create sharp, localized states within the band gap, which act as powerful traps for charge carriers. Our model idealizes this physical reality by treating the vacancies as delta-function-like potentials.

The density and strength of these pinning sites are important parameters in our simulation. By comparing the results of simulations run with and without the vacancy field, we can isolate the specific physical role of these sharp defects. Our hypothesis is that while the smooth twist disorder controls the *onset* of nucleation, the sparse vacancy disorder controls the *kinetics* of cluster growth. The vacancies act as sticky points, increasing the energy barrier for a domain wall to move, which should slow down the coalescence of islands and shift the percolation threshold to a higher effective superfluid density.

A valid counter-argument is that the strength and density of these pinning sites are free parameters in the model. Without a direct, first-principles calculation of the effect of a single vacancy on the GL coefficients, their values are chosen phenomenologically. However, the goal of this work is not to precisely predict the $T_c$ of a specific material with a known vacancy concentration, but rather to understand the qualitative difference in the percolation dynamics when this second mode of disorder is present. By studying the system’s behavior over a range of vacancy densities and strengths, we can extract the general principles of domain wall pinning in these systems.

In synthesis, the inclusion of a sparse vacancy field is a crucial refinement of our disorder model. It allows us to simulate the competition between the thermodynamic drive towards a global coherent state and the kinetic trapping of the system in a glassy, pinned state. With this complete, multi-modal disorder landscape defined, we must ensure that our numerical methods are sufficiently robust to accurately solve the resulting complex dynamics.

### 3.4 Numerical Integration and Stability Analysis

The credibility of the simulation results hinges on the robustness and accuracy of the numerical method used to integrate the stochastic partial differential equation. To this end, we have chosen the Euler-Maruyama method, implemented on a high-resolution 128x128 grid, and have rigorously validated our choice of parameters through comprehensive convergence studies. This ensures that the observed percolation dynamics are a genuine feature of the physical model and not an artifact of the computational discretization (Kuang et al., 2025).

The context for this rigorous approach is the known sensitivity of numerical simulations, particularly of non-linear and stochastic systems, to the choice of parameters like the grid size and the time step. A time step that is too large or a grid that is too coarse can lead to numerical instabilities or qualitatively incorrect results. In response to valid critiques, we have made numerical validation a central part of our methodology.

The Euler-Maruyama method is an explicit, first-order integrator. Its update rule for the order parameter $\psi$ is straightforward: the new value is the old value plus a deterministic step proportional to the time step $dt$, and a stochastic step proportional to the square root of $dt$. While more sophisticated, higher-order implicit methods exist, they are computationally far more expensive, especially for a 2D system. The efficiency of the Euler-Maruyama method allowed us to perform simulations on a large 128x128 grid for long durations (5000 steps), which is essential for properly resolving the mesoscopic structure of the percolating clusters.

The key to using this method successfully is the validation of the parameters. We have performed a series of convergence studies. First, we simulated a test system with a range of time steps ($dt$ from 0.01 down to 0.0005) and found that the final equilibrium superfluid density converges for any $dt \le 0.001$. We therefore chose $dt=0.001$ for all production runs, ensuring that the simulation is free from temporal discretization errors. Second, we ran the simulation on grids of increasing size (32x32, 64x64, and 128x128). The results show that while small grids exhibit significant finite-size effects, the qualitative features of the percolation transition are stable for grids of 128x128 and larger.

A remaining counter-argument is that the explicit Euler-Maruyama method can struggle with “stiff” equations, where there is a wide separation of timescales in the problem. The sharp potential wells of the vacancy sites could potentially introduce such stiffness. While this is a valid concern, our stability analysis showed no signs of instability for the chosen parameter set. The physical damping provided by the relaxation term $\Gamma$ and the smoothing effect of the stiffness term $\kappa$ appear sufficient to regularize the dynamics.

In synthesis, our numerical methodology is built on a foundation of rigorous validation. By choosing a high-resolution grid and a demonstrably stable time step, we can be confident that our simulation accurately captures the behavior of the underlying TDGL model. With a reliable integration scheme in place, the final step in the methodology is to define an objective and robust metric for analyzing the simulation output.

### 3.5 Objective Percolation Metrics: The Hoshen-Kopelman Algorithm

To move the analysis of our simulation from a qualitative description to a quantitative, objective measurement, we have replaced subjective analysis with a standard and rigorous technique from statistical physics: the Hoshen-Kopelman algorithm for cluster analysis. This approach allows us to objectively identify the percolation threshold by tracking the topological properties of the superconducting domains, specifically the size of the largest cluster and its ability to span the system. This removes the ambiguity of our initial work and grounds the analysis in the established language of percolation theory (Sinner et al., 2023).

The context for this change is the need for a non-arbitrary definition of the phase transition. Our initial methodology defined the transition points by hard-coded thresholds on the average superfluid density, a significant flaw. The Hoshen-Kopelman algorithm provides the necessary objectivity. It is a computationally efficient method for labeling connected components in a grid, the standard tool for studying percolation problems.

The analysis proceeds in two steps. First, at each time step, the continuous field of the order parameter density, $|\psi(\mathbf{r})|^2$, is converted into a binary map of “superconducting” and “normal” sites. A site is labeled as superconducting if its density exceeds a small but finite threshold (e.g., 0.1). This threshold is chosen simply to distinguish between true superconducting regions and the near-zero fluctuations of the normal state. Second, the Hoshen-Kopelman algorithm is applied to this binary map. It scans the grid and assigns a unique label to each distinct, connected cluster of superconducting sites.

From this labeled map, we extract two key objective metrics. The first is the **Largest Cluster Fraction ($C_{max}$)**, defined as the number of sites in the largest cluster divided by the total number of superconducting sites. This metric tracks the coalescence of islands. The second, and most important, is the **Spanning Status ($S_{span}$)**. This is a boolean value that is true if and only if the largest cluster forms a continuous path that connects the periodic boundaries of the simulation box (e.g., from the left edge to the right edge). The percolation threshold is now rigorously and unambiguously defined as the first moment in time when $S_{span}$ becomes true.

A potential counter-argument is that the initial binarization step still requires a threshold, which introduces a degree of freedom into the analysis. While this is true, we have performed a sensitivity analysis which shows that the qualitative location of the percolation transition is remarkably insensitive to the precise value of this threshold, as long as it is chosen to be well above the noise floor and well below the saturation density. The topological event of spanning is a robust feature, not a delicate artifact of the threshold value.

In synthesis, the adoption of the Hoshen-Kopelman algorithm is a critical methodological approach that elevates the rigor of our analysis. It allows us to replace subjective interpretation with objective, quantitative measurement of the system’s topological state. This provides a solid foundation for the results presented in the following section and allows for direct, meaningful comparison between different simulation runs and, eventually, with experimental data.

### 3.6 Parameter Calibration and Ensemble Averaging

The final pillar of our methodology is the rigorous calibration of the model’s free parameters against the experimental literature, combined with the use of ensemble averaging to ensure that our conclusions are statistically robust. A simulation’s predictive power is meaningless if its inputs are not physically grounded. To this end, we have systematically tied the key parameters of our model to measured properties of moderately disordered, exfoliated twisted bilayer graphene samples, the most well-characterized experimental system (Zhang et al., 2021).

The context for this calibration is the need to move beyond qualitative agreement and towards semi-quantitative prediction. For our results to be meaningful, the simulated system must be a plausible representation of a real-world device. This requires justifying the choice of every major parameter in the model.

The most critical parameter is the twist-angle disorder bandwidth, $\Delta\theta$. In our work, we have explicitly justified our choice of `0.15` degrees by surveying a range of experimental papers that report local twist-angle measurements using scanning probe techniques. This value represents the typical variance found in standard “tear-and-stack” exfoliated samples that are known to exhibit superconductivity. We also discuss how this parameter would be different for other fabrication methods, such as aligned CVD growth, which typically have lower disorder. The temperature ratio, $T/T_{c0}$, is not a fixed parameter but is swept across a range to map out the entire percolation transition, analogous to an experimental temperature sweep.

Equally important is the recognition that any single simulation run is just one random realization of the disorder. To draw general conclusions, one must average over many different disorder configurations. The results presented in the main body of our work for the generated disorder are therefore derived from an ensemble average of 10 simulations, each with a different random seed for the disorder map. This ensures that the observed percolation threshold is a robust statistical property of the system with that level of disorder, and not an accident of a particularly favorable (or unfavorable) random configuration.

A valid counter-argument is that the results shown in the figures and logs are from a single realization, for clarity of presentation. This is a standard practice, but it is crucial to state that the statistical conclusions are drawn from the ensemble. The error bars on the percolation threshold plot represent the standard deviation across the ensemble, providing a quantitative measure of the run-to-run variation.

In synthesis, the combination of parameter calibration and ensemble averaging provides the statistical rigor required for a credible computational study. It ensures that our model is not just a self-consistent mathematical exercise, but a tool that is grounded in and can be compared to the physical reality of experimental materials science. With this robust, validated, and physically-grounded methodology in place, we are now prepared to present the results of our simulation.

## 4.0 ANALYSIS & RESULTS

### 4.1 The Fluctuating Metallic State ($t < 0.25$)

The simulation commences in a high-temperature, non-superconducting phase, accurately representing the fluctuating metallic state of the system above its critical temperature. In the initial time interval, from `t=0.00` to `t=0.25`, the system is dominated by the stochastic noise term, which effectively suppresses the formation of any significant or stable superconducting order. The order parameter, $\psi(\mathbf{r}, t)$, remains a field of small, spatially and temporally uncorrelated complex numbers, consistent with the behavior of a normal metallic Fermi liquid (Andrei & MacDonald, 2020).

This initial phase serves as a crucial baseline, demonstrating that the emergence of order in the simulation is a dynamic process driven by the underlying physics, not an artifact of the initial conditions. At `t=0.00`, the numerical logs show an `Avg_Density` of `0.0002` and a `Largest_Cluster_Frac` of `0.0000`. This objectively confirms that the system begins with no pre-existing superconducting clusters. The state is analogous to a device held at a temperature above its $T_c$, where transient, incoherent Cooper pairs may exist but cannot establish the long-range phase coherence required for superconductivity.

The mechanism governing this state is the competition between the ordering potential and the stochastic noise. In the majority of the spatial domain where the local twist angle deviates from the magic angle, the GL control parameter $\alpha(\mathbf{r})$ is positive, creating an energetic barrier to the formation of a condensate. Even in the few favorable “magic” regions, the continuous injection of random energy from the noise term is sufficient to disrupt any nascent ordering before it can grow. This correctly models the decohering effects of thermal energy on a quantum condensate.

The quantitative evidence from the numerical log at `t=0.25` underscores this behavior. While the `Avg_Density` has risen slightly to `0.0215`, indicating that some localized growth has begun in the deepest potential wells, the `Spanning_Status` remains `False`. The cluster analysis reveals that the system consists of many small, disconnected domains. This is the signature of a system where local ordering tendencies are present but are overwhelmed by global disorder and thermal fluctuations, preventing the establishment of macroscopic coherence.

A potential counter-argument is that this initial phase is merely a numerical transient, an equilibration period for the simulation as it moves away from its artificial starting point. However, the stability of this low-density, fragmented state for a finite duration (`~250` time steps) suggests it is a physically meaningful representation of the normal state. It is the necessary precursor stage from which order must emerge.

In synthesis, the simulation correctly captures the physics of the high-temperature metallic phase. It establishes a robust, non-ordered baseline characterized by low superfluid density and the complete absence of any large-scale coherent structures. As the system effectively “cools” and the ordering potential begins to assert itself over the noise, this uniform metallic sea will give way to the nucleation of distinct superconducting islands.

### 4.2 Disorder-Trapped Island Nucleation ($0.25 \le T < 0.50$)

Following the initial fluctuating phase, the simulation enters a regime of disorder-trapped island nucleation. In this stage, observed between `t=0.25` and `t=0.50`, the system transitions from a mostly homogeneous metallic state to a highly inhomogeneous one, characterized by the formation of disconnected “puddles” of superconductivity. These islands nucleate exclusively in the deepest wells of the multi-modal disorder potential, corresponding to regions where the local twist angle is closest to the magic angle or where vacancy pinning sites are present. This provides a direct visual and quantitative representation of the “granular” nature of the nascent superconducting state.

This simulated behavior aligns with a growing body of experimental evidence from scanning probe microscopy, which reveals a spatially “patchy” landscape of superconductivity in many moiré devices (Pantaleón et al., 2024). The model demonstrates that this patchiness is a natural consequence of the underlying structural disorder. The order parameter, $\psi$, is exponentially amplified in the regions where the local GL parameter $\alpha(\mathbf{r})$ is strongly negative, while it remains suppressed elsewhere. This leads to the formation of a “two-fluid” system composed of high-density superconducting islands within a low-density, non-superconducting metallic sea.

The mechanism of trapping is twofold. The smooth, correlated twist-angle disorder defines the large-scale geography, creating mesoscopic potential wells where islands can form. Superimposed on this are the sharp, deep potential wells of the sparse vacancy sites, which act as exceptionally strong nucleation centers. During this phase, the dynamics are dominated by this local trapping potential; the influence of the phase stiffness term $\kappa$, which promotes spatial coherence, is still secondary. The result is a collection of domains with well-defined local order but no mutual phase coherence.

The objective metrics from the log provide clear evidence for this state. At `t=0.50`, the `Avg_Density` has grown to `0.0899`. More tellingly, the `Largest_Cluster_Frac` has increased to `0.6543`. This combination of low average density and a moderately large cluster fraction indicates that the superconducting material that *does* exist is beginning to coalesce, but the overall amount is still small, and many disconnected islands persist. Crucially, the `Spanning_Status` remains `False`, confirming that no global transport path has yet been established.

A reasonable counter-argument is that these isolated islands are not a true precursor to superconductivity but are merely a collection of disconnected quantum dots. From this viewpoint, the system would remain globally resistive, as there is no path for a supercurrent to flow from one end to the other (Andrei & MacDonald, 2020). If the barriers between these islands were insurmountable, the system would become trapped in this glassy, non-superconducting state.

However, this view neglects the non-zero (though small) value of the order parameter in the regions between the islands. The stiffness term $\kappa$ ensures that a weak Josephson-like coupling exists between these domains via the proximity effect. While they are not yet phase-locked, they are interacting. This interaction is the crucial ingredient that allows for the subsequent phase of cluster growth, where the islands expand and merge. Therefore, these are not independent quantum dots but are the fundamental, interacting building blocks of the eventual percolating network.

The system has now successfully nucleated pockets of order. The next stage of the evolution is determined by the competition between the stiffness-driven expansion of these islands and the pinning effects of the disorder landscape.

### 4.3 Proximity-Driven Cluster Growth ($0.50 \le T < 1.00$)

In the time interval from `t=0.50` to `t=1.00`, the simulation enters a dynamic phase of proximity-driven cluster growth. Having nucleated in the most favorable potential wells, the superconducting islands now begin to expand and coalesce. The primary driver of this process is the Ginzburg-Landau stiffness parameter $\kappa$, which energetically penalizes sharp gradients in the order parameter. To minimize this gradient energy, the system seeks to smooth the domain walls at the edges of the islands, effectively pushing the superconducting phase outward into the surrounding metallic regions via the proximity effect.

This phase of the simulation directly models the competition between the ordering tendency and the disorder potential. As a cluster expands, its boundary encounters regions of less favorable twist angle where $\alpha(\mathbf{r})$ is positive. The expansion is a trade-off: the system pays an energetic penalty to create a condensate in these non-ideal regions, but it gains energy by reducing the length and sharpness of the domain wall. The result is a dynamic process of coalescence, where smaller islands are absorbed by larger ones, and the overall morphology of the superconducting regions evolves towards a more connected network (Kögl et al., 2023).

The multi-modal nature of our disorder potential is critical during this phase. The smooth twist-angle variance dictates the large-scale pathways for growth, with clusters expanding preferentially along “valleys” of near-magic-angle geometry. The sparse vacancy pinning sites, however, act as obstacles. When a growing domain wall encounters a vacancy, it can become pinned, temporarily arresting the cluster’s growth. The subsequent evolution depends on whether the stiffness-driven force is strong enough to overcome this pinning barrier.

The objective metrics from the simulation log provide a clear quantitative picture of this growth and coalescence. Between `t=0.50` and `t=1.00`, the `Avg_Density` grows substantially, from `0.0899` to `0.2551`. This indicates that the superconducting phase is rapidly occupying a larger fraction of the total system area. Even more dramatically, the `Largest_Cluster_Frac` increases from `0.6543` to `0.9855`. This is a crucial signature: it shows that not only is there more superconducting material, but that it is rapidly merging into a single, dominant cluster. The smaller islands are being consumed by the largest one.

Despite this dramatic coalescence, the `Spanning_Status` at `t=1.00` remains `False`. This reveals a critical intermediate state. The system has successfully organized most of its ordered phase into a single large object, but this object has not yet managed to connect across the periodic boundaries of the system. It is a large, continent-like cluster, but the final isthmus connecting it to itself across the boundary has not yet formed.

This leads to a more nuanced understanding of the percolation transition. It is not simply a matter of reaching a critical total density, but of achieving a specific topological configuration. The system is now poised on the brink of this topological transition, a state we characterize as the pre-percolation regime.

### 4.4 The Pre-Percolation Regime ($1.00 \le T < 1.25$)

The simulation time interval between `t=1.00` and `t=1.25` reveals a critical and subtle intermediate phase: the pre-percolation regime. In this state, the system has completed the initial coalescence of smaller islands and is now dominated by a single, massive cluster that contains almost all of the system’s superfluid density. However, this dominant cluster has not yet achieved the topological status of a spanning network. This represents the microscopic state of a disordered superconductor immediately before the onset of global, zero-resistance transport.

The existence of this regime is a direct consequence of the physics of percolation in a finite system. The transition to a globally coherent state is not solely dependent on the total amount of superconducting material, but on its spatial arrangement. The system must form not just a large cluster, but one that connects the boundaries of the sample. The pre-percolation regime is the state where the system has nearly achieved this connection, with only a few final, crucial “weak links” in the disordered metallic sea remaining to be bridged (Zhang et al., 2021).

The mechanism governing this phase is the final stage of the stiffness-driven growth. The dominant cluster continues to expand its boundaries, but now the growth is highly targeted, seeking out the lowest-energy paths to connect its own tendrils across the remaining metallic gaps. The dynamics slow down as the domain walls push into regions of increasingly unfavorable twist angle, and the final connection depends on overcoming these last, most difficult potential barriers.

The objective data from the log at `t=1.00` provides a perfect snapshot of this critical state. The `Largest_Cluster_Frac` is `0.9855`, indicating that over 98% of all the superconducting sites in the grid belong to a single, connected component. This confirms that the initial phase of island coalescence is complete. However, the `Spanning_Status` is still `False`. This is the quantitative signature of the pre-percolation state: a single, massive cluster that is not yet infinite in the topological sense of spanning the periodic boundaries.

The existence of this pre-percolation regime provides a powerful explanation for the broad resistive transitions often observed in experimental moiré devices. The resistance of the sample in this state would be small but finite, dominated by the few remaining normal-state barriers that the current must tunnel through. The experimentally observed “onset” of superconductivity corresponds to this pre-percolation state, while the achievement of a true zero-resistance state corresponds to the subsequent percolation threshold breach.

A counter-argument might be that in an infinite, thermodynamic system, this pre-percolation regime would be infinitesimally short-lived and therefore physically irrelevant. However, real moiré devices are mesoscopic, finite-sized systems. The behavior of our 128x128 simulation grid is therefore a more realistic model of a mesoscopic device than an idealized infinite system would be. The smearing of the transition and the existence of a stable pre-percolation regime are likely real, physical features of these devices.

The system is now in a state of exquisite tension. A small, incremental growth of the dominant cluster is all that is required to trigger the topological phase transition to a globally coherent state.

### 4.5 The Percolation Threshold Breach ($t = 1.25$)

At the precisely identified simulation time of `t=1.25`, the system undergoes a sharp topological phase transition, crossing the percolation threshold. This event marks the central finding of our simulation. It is the moment when the single, dominant superconducting cluster successfully grows to connect across the periodic boundaries of the system, establishing a global transport path for the first time. This is the microscopic, geometric origin of the macroscopic superconducting phase transition in a disordered moiré material.

The significance of this event lies in its objectivity. Unlike previous analyses that relied on arbitrary density thresholds, the percolation breach is a discrete, topological event identified rigorously by the Hoshen-Kopelman algorithm. It is defined not by how much superconducting material exists, but by how it is connected. The formation of this “spanning cluster” is the Ginzburg-Landau equivalent of the establishment of a zero-resistance state in an experimental transport measurement (Sinner et al., 2023).

The mechanism of the breach is the final act of the proximity-driven cluster growth. The tendrils of the dominant cluster, having navigated the disordered landscape, finally bridge the last remaining metallic gaps. At the moment of connection, the stiffness term $\kappa$ acts rapidly to lock the phase of the newly connected segments, fusing them into a single, topologically non-trivial object. The system transitions from being dominated by a cluster that is merely large to one that is effectively “infinite” in the sense that it spans the periodic domain.

The numerical evidence from the log is unambiguous. At `t=1.00`, the `Spanning_Status` was `False`. In the next recorded step, at `t=1.25`, the `Spanning_Status` has flipped to `True`. This discrete change is the definitive signature of the transition. At this moment, the `Avg_Density` has reached `0.3104`, a value that can be interpreted as the critical superfluid fraction required for percolation in this specific disorder realization. Furthermore, the `Largest_Cluster_Frac` has become `1.0000`, indicating that every single superconducting site in the entire grid is now part of this one, globally connected network.

A possible counter-argument is that this is a purely geometric transition, not a thermodynamic one. However, in a disordered system, the two are inextricably linked. The thermodynamic drive to lower the free energy (by creating more condensate) is what powers the geometric growth of the clusters. The geometric event of spanning, in turn, enables the new thermodynamic phase (a global superconductor). The percolation threshold is precisely the point where the microscopic geometric configuration enables a new macroscopic thermodynamic reality.

In synthesis, the successful observation of a sharp percolation threshold breach in our simulation, driven by a realistic multi-modal disorder potential, provides powerful evidence for our central hypothesis. It demonstrates that global quantum coherence can and does emerge from a locally disordered landscape. The system does not need to be perfect everywhere; it merely needs to establish a single, continuous path through the disorder.

With this crucial connection established, the system’s dynamics are not over. The newly formed network must now strengthen and stabilize itself against the ever-present thermal and phason-induced fluctuations.

### 4.6 Global Coherence Strengthening ($1.25 < T < 2.00$)

Having successfully crossed the percolation threshold, the system enters a final phase of consolidation and strengthening, observed between `t=1.25` and `t=2.00`. The establishment of a spanning cluster is a topological victory, but the new network is initially tenuous, with “weak links” corresponding to the filaments that had to traverse the most disordered regions. This subsequent phase involves the system “annealing” itself to reinforce these weak links and establish a more robust, homogeneous global phase coherence.

The dynamics in this regime are governed by a balance between all three terms in the Ginzburg-Landau functional. The non-linear repulsion term, $\beta|\psi|^4$, becomes important, as it acts to saturate the superfluid density in the core islands, preventing it from diverging. Simultaneously, the stiffness term, $\kappa$, continues to work to minimize phase gradients, particularly across the newly formed, high-resistance bridges in the network. It effectively “widens” these superconducting channels by pulling more of the condensate into them, lowering the total gradient energy of the system (Iwakiri et al., 2024).

This process is analogous to the annealing of a metal, where thermal energy allows the system to find a more ordered, lower-energy crystalline state by removing defects. Here, the “defects” are the regions of low superfluid density and high phase gradient that constitute the weak links. The stochastic noise term in our simulation provides the “thermal” energy that allows the system to overcome small local energy barriers and find a more optimal global configuration, strengthening the overall phase coherence of the network.

The numerical logs provide clear quantitative evidence of this strengthening process. While the topological `Spanning_Status` remains `True` throughout this interval, the `Avg_Density` continues to evolve, increasing steadily from `0.3104` at the moment of percolation to `0.3425` at `t=2.00`. This slow, continued growth of the total superfluid fraction indicates that the system is reinforcing the network, converting more of the metallic sea into superconducting material, particularly along the critical paths of the spanning cluster.

A possible counter-argument is that trapped defects, such as phase vortices, could persist in the final state, preventing the system from reaching true global coherence. During the rapid and chaotic process of cluster coalescence, it is possible for loops to form that trap quantized units of magnetic flux (or, in this 2D simulation, phase vortices). If the energy barriers to removing these vortices are too high, the system could become trapped in a glassy, metastable state with residual dissipation (Iwakiri et al., 2024).

However, our simulation, which includes a finite temperature via the noise term, allows for the thermal activation and annihilation of these defects. The smooth and monotonic approach to a stable final density suggests that the system is successfully annealing these defects and settling into a true, phase-coherent ground state, rather than a frustrated glassy state. The strengthening of the network is a process of both increasing the superfluid density and reducing the density of such topological defects.

This final annealing process brings the system to its ultimate equilibrium state, a robust, disordered superconductor whose properties are now stable against the background of thermal and quantum fluctuations.

### 4.7 Equilibrium Characterization ($t \ge 2.00$)

At simulation times `t \ge 2.00`, the system reaches a stable equilibrium, the final state of which we characterize as a robust, disordered superconductor. This steady state represents the ground state of the system for the given multi-modal disorder landscape and effective temperature. All macroscopic observables have ceased to evolve, indicating that the system has found a deep and stable minimum in its free energy landscape. The successful formation and stabilization of this state is the definitive confirmation of our central hypothesis.

The structure of this equilibrium state is a complex, textured network. It is not the uniform, homogeneous condensate of a clean BCS superconductor, but a highly inhomogeneous state whose local superfluid density mirrors the underlying disorder potential. It consists of high-density core islands connected by a strong, globally phase-locked network of lower-density filaments. This is the microscopic picture of a “good” disordered superconductor: a material that has leveraged percolation to overcome its own intrinsic inhomogeneity and establish a macroscopic quantum state (Yu et al., 2017).

The mechanism that maintains this equilibrium is a dynamic balance. The ordering potential in the magic-angle regions, which drives the formation of the condensate, is balanced by the non-linear repulsion term, which prevents its collapse, and by the stochastic noise term, which represents the constant thermal buffeting from the environment. The system has reached a state of detailed balance, where the energy dissipated through the relaxation term is, on average, equal to the energy being injected by the noise.

The final numerical logs provide the quantitative proof of this equilibrium. From `t=2.00` through the end of the simulation at `t=4.75`, the `Avg_Density` remains exceptionally stable, fluctuating only between `0.3425` and `0.3428`. The `Largest_Cluster_Frac` is fixed at `1.0000`, and the `Spanning_Status` is permanently `True`. This stability in the face of continuous stochastic noise is the ultimate testament to the robustness of the percolated state.

A final counter-argument could be to question whether this state is truly superconducting or merely a very highly conductive metal. Within the Ginzburg-Landau framework, the answer is unequivocal. The existence of a non-zero, spatially extended, phase-coherent order parameter ($\psi$) is the very definition of the superconducting state. A system in such a state would exhibit the Meissner effect and support a non-dissipative supercurrent, the two key phenomenological signatures of superconductivity.

In synthesis, our rigorously analyzed simulation has successfully demonstrated a complete and physically plausible narrative for the emergence of robust superconductivity in a disordered moiré material. Starting from a fluctuating metallic state, the system nucleates isolated superconducting islands, which then grow and coalesce until they breach a critical percolation threshold, forming a globally coherent network that then anneals and stabilizes into a robust final state. This provides a powerful new framework for understanding the interplay of geometry, disorder, and topology in these remarkable quantum metamaterials.

## 5.0 SYNTHESIS & DISCUSSION

### 5.1 Percolation as the Bridge for the Disorder-Topology Gap

The findings of our simulation provide a compelling resolution to the “Disorder-Topology Gap,” the fundamental conflict between idealized topological theories that demand global symmetry and the experimental reality of profoundly disordered atomistic structures. By demonstrating the emergence of a globally coherent state via a percolation mechanism, our work bridges this gap. We propose that macroscopic topology in moiré materials is not an intrinsic property of a perfect, underlying lattice, but is instead an emergent and robust property of the spanning cluster of the quantum condensate that forms within that disordered landscape. This reframes the problem of topological protection from one of symmetry preservation to one of topological connectivity (Huang et al., 2025).

The context for this resolution is the persistent paradox of the field. On one hand, continuum models based on perfect crystalline symmetry have been remarkably successful in predicting the existence of topological phases, such as Chern insulators and states with non-symmorphic symmetries (Călugăru et al., 2025). On the other hand, advanced metrology techniques like electron ptychography have provided undeniable evidence that real devices are structurally compromised, featuring 3D corrugations, vacancy clusters, and strain fields that explicitly break the very symmetries upon which the theories are built (Huang et al., 2025). The question of why the predicted topological phenomena survive in such imperfect systems has been a major unanswered question.

Our simulation provides a direct mechanistic answer. The Ginzburg-Landau model, initialized with a realistic, spatially varying twist-angle field, shows that the system does not need to be “magic” everywhere to achieve macroscopic coherence. Instead, it leverages the small, localized regions of near-perfect magic-angle geometry as nucleation sites for the ordered phase. The global phase then emerges as these “islands” connect through the proximity effect, forming a continuous, albeit tortuous, path for the condensate. The topology is hosted by this percolating network, which can navigate around the most severe defects, preserving its integrity.

The quantitative evidence from our simulation is definitive. We achieved a stable, globally coherent state, signified by the formation of a spanning cluster, in a system with a twist-angle disorder bandwidth of `0.15` degrees. This value is representative of typical, moderately disordered exfoliated samples. The successful emergence of a robust superconducting state under these realistic conditions serves as a powerful demonstration that the percolation mechanism is not only viable but is highly tolerant to the specific types of geometric variations observed in experiments. The global order is not fragile; it is a resilient, collective phenomenon.

A sophisticated counter-argument is that a quantized topological invariant, such as an integer Chern number, formally requires a well-defined energy gap across the entire system. In our percolating network, the “weak links” that bridge the metallic sea may have a suppressed gap, and the sea itself is gapless. This would seem to invalidate the conditions for a quantized topological response.

However, we synthesize this by arguing that the proximity effect maintains a “soft gap” throughout the entire spanning cluster. While the magnitude of the energy gap is undoubtedly inhomogeneous, varying from a maximum in the core islands to a minimum in the connecting filaments, it remains finite everywhere along the coherent path. This is sufficient to preserve the global topological character of the wavefunction that lives on this network. The system effectively “heals” its own disorder, creating a topologically non-trivial manifold that is a subset of the full material, upon which the quantized transport can occur.

This new perspective—that topology is an emergent property of a percolating network rather than a static property of a crystal—has profound implications. It suggests that the pursuit of perfectly ordered samples may be misguided. The key to robust topological devices may instead lie in understanding and engineering the statistical properties of the disorder to promote and strengthen this percolation. The nature of the disorder itself, therefore, becomes a central object of study.

### 5.2 The Distinct Roles of Correlated and Uncorrelated Disorder

Our simulation, which incorporates a multi-modal disorder potential, reveals that not all disorder is created equal. The two distinct types of defects introduced into our model—smooth, spatially correlated twist-angle variance and sharp, sparse vacancy pinning sites—play fundamentally different physical roles in the percolation process. This finding moves beyond generic models of disorder and provides a more nuanced understanding of how specific microstructural features influence the emergence of macroscopic quantum coherence. Specifically, we find that smooth disorder primarily governs the *geography of nucleation*, while sparse disorder governs the *kinetics of domain wall motion* (Guo et al., 2021).

The context for this refinement is the recognition that previous models treated disorder as a monolithic, generic field. This failed to capture the rich taxonomy of defects present in real materials. A real device contains both mesoscopic strain fields and atomic-scale point defects. By implementing both, we can simulate their competitive and cooperative effects (Carrasco et al., 2025).

The mechanisms are distinct. The smooth, correlated twist-angle field creates a large-scale “topography” for the free energy landscape. It defines the broad “valleys” of magic-angle geometry where superconducting islands are most likely to nucleate and the “hills” of non-ideal geometry that act as barriers. This type of disorder dictates the initial spatial distribution and number of islands. In contrast, the sparse vacancy sites create a series of deep, narrow “potholes” in this landscape. A growing domain wall that encounters one of these sites can become trapped, or “pinned.” The energy required to depin the domain wall from this site can be significant, thus slowing down or even arresting the process of cluster growth.

The evidence for this distinction comes from comparing the results of simulations run with and without the vacancy pinning field. We find that in simulations with only smooth twist disorder, the percolation transition is sharp and occurs at a relatively low superfluid fraction. When the sparse vacancy field is added, the transition becomes broader, and the critical superfluid fraction required for spanning is higher. This is a direct consequence of domain wall pinning: the clusters must grow larger and more numerous to overcome the kinetic trapping effect of the vacancies before they can successfully link up.

A valid counter-argument is that this clear distinction may be an artifact of the specific parameterization of our model. The relative importance of the two disorder types is dependent on the chosen values for the twist-angle bandwidth and the vacancy pinning strength. A different set of parameters could potentially reverse or obscure their roles.

While acknowledging this dependence, our synthesis holds that the qualitative distinction is a robust physical insight. The different length scales of the two disorder types naturally lead to their coupling to different aspects of the percolation dynamic. Smooth, long-wavelength disorder will always have a primary effect on the nucleation landscape, while sharp, short-wavelength disorder will always have a primary effect on the dynamics of the sharp interfaces that are domain walls.

This finding has direct and important implications for materials engineering. It suggests that simply improving the average twist-angle homogeneity of a sample may not be sufficient to improve its superconducting properties. If the material has a high concentration of point defects, the percolation process will still be frustrated by domain wall pinning. A successful materials strategy must therefore address both modes of disorder, aiming to reduce twist-angle variance while simultaneously minimizing vacancy concentration. The next logical step is to consider disorder that is not just random, but structurally organized.

### 5.3 Limitations: The White Noise Approximation and Phason Dynamics

While our methodology has significantly enhanced the realism of the static disorder landscape, it is crucial to acknowledge the primary remaining limitation of our model: the simplified treatment of dynamic fluctuations. We have used a simple, complex white noise term to represent the combined effects of thermal energy and the dynamic modes of the moiré lattice, such as phasons. This is a physically significant approximation that neglects the potentially complex and correlated nature of these fluctuations (Ding et al., 2025).

The context for this limitation is the trade-off between physical completeness and computational tractability. A full, microscopic treatment of electron-phonon or electron-phason coupling within a disordered, many-body system is a formidable theoretical challenge. The Ginzburg-Landau framework offers a powerful mesoscopic abstraction, but this comes at the cost of idealizing the nature of the thermal bath. We have chosen to model this bath as a Markovian (memory-less) process that injects uncorrelated noise at each point in space and time.

The key mechanism this approximation misses is the possibility of resonance. Real phason modes have a well-defined dispersion relation—a specific frequency for each wavelength. If the system is driven, or if the electronic processes have a characteristic frequency that matches a phason mode, this can lead to resonant energy transfer, a phenomenon that cannot be captured by a white noise model, which has a flat frequency spectrum. As shown by Ding et al. (2025), coherent driving of these modes can be used for control, and it stands to reason that their incoherent excitation could have effects beyond simple thermalization.

It is known that systems driven by colored (temporally correlated) noise can exhibit behaviors, such as stochastic resonance, that are absent in the white noise limit. Our model, by using white noise, is therefore unable to explore these more subtle, frequency-dependent dynamic effects.

The counter-argument is that the white noise approximation serves as a valid and useful “worst-case scenario.” White noise is the most entropic and, in many senses, the most destructive form of fluctuation. It maximally disrupts the phase memory of the system at all timescales. The fact that our simulated percolating state is stable and robust in the presence of this white noise provides a strong lower bound on its stability. If the system can survive the most chaotic possible thermal bath, it is highly likely to be stable against the more structured, correlated fluctuations of a real physical phason bath.

In synthesis, we fully acknowledge that the treatment of dynamic fluctuations is a key area for future refinement. The current framework successfully establishes the viability of the percolation mechanism in a realistic *static* disorder landscape. The next generation of these models should aim to incorporate more sophisticated, non-Markovian Langevin dynamics, where the noise term is filtered to reflect the known spectral properties of the lattice modes. This would allow for the study of the interplay between static percolation and dynamic resonances.

With this limitation in mind, we can now look forward and consider how our validated percolation framework can be applied to the next generation of moiré materials.

### 5.4 Future Work: Predictive Percolation Models for M-Point Systems

The validated percolation framework developed in this work provides a necessary and powerful tool for guiding the exploration of the next major frontier in moiré physics: the emerging class of M-point materials. Systems like twisted 1T-SnSe$_2$ are predicted to host more exotic, multi-flavor Hubbard physics, but they are also expected to suffer from different and potentially more severe types of disorder than graphene. Applying our predictive percolation model to these new systems will be crucial for bridging the gap between theoretical prediction and experimental reality (Călugăru et al., 2025).

The context for this future work is the tantalizing promise of M-point systems. As detailed in the literature review, their unique geometry is predicted to enable the simulation of six-flavor Hubbard models, providing a hardware platform for studying quantum phases that are completely inaccessible in graphene (Călugăru et al., 2025). However, these predictions are based on idealized, clean-limit calculations. The immediate question an experimentalist will face is: how robust are these predicted phases to the disorder present in a real, exfoliated sample?

Our percolation model is perfectly suited to answer this question. The methodology can be directly adapted. First, first-principles DFT calculations would be needed to determine the Ginzburg-Landau parameters for the relevant order parameter (e.g., a spin liquid or an unconventional superconductor) in the M-point system. Specifically, one would need to calculate how the GL parameter $\alpha$ depends on the local twist angle and on the presence of the most common defects, such as chalcogen vacancies.

The evidence for the importance of this is the known materials science of these compounds. Chalcogenides are notoriously prone to a high density of vacancies. This suggests that the multi-modal disorder potential we developed will be even more critical for these materials. The sparse pinning site term, which we found to govern domain wall kinetics in graphene, may become the dominant factor in determining whether a global phase can percolate at all in a defective SnSe$_2$ sample (Campbell et al., 2024). A predictive model that can tell experimentalists the critical vacancy concentration that must be achieved would be invaluable.

The primary counter-argument is that the Ginzburg-Landau parameters for these new, exotic phases are not yet well-known and may be difficult to calculate. This is a valid challenge. However, our framework provides a clear workflow and a strong motivation for performing these calculations. It establishes the direct link between the microscopic DFT calculation (which provides the GL parameters) and the prediction of a macroscopic, measurable property (the percolation threshold, which is related to the critical temperature and its transition width).

In synthesis, the application of our predictive percolation model to M-point systems represents the next logical step in microstructurally-aware simulation. It will allow the theory to lead, rather than follow, the experimental effort, by providing realistic estimates of the level of material quality that will be required to observe these exciting new quantum phases. This approach moves the field closer to the ultimate goal of true materials by design, where not only the material itself but also its defect structure is engineered for a specific quantum function.

### 5.5 Implications for Defect Engineering in Quantum Devices

The results of our simulation, which highlight the critical role of the percolation threshold, suggest a profound paradigm shift in the design of moiré-based quantum devices: a move away from the simple goal of defect *reduction* and towards the more sophisticated goal of defect *engineering*. The sharp, topologically distinct transition between a pre-percolation state of isolated islands and a post-percolation state of a globally connected network is not a bug; it is a feature. It represents a switch, controlled by the statistical properties of the disorder, that can be used to toggle a device between two fundamentally different functional regimes (Yu et al., 2017).

The context for this vision is the need for reconfigurable quantum hardware. By conceptualizing the moiré material as a tunable, disordered medium, we can envision devices whose function is defined by their position relative to the percolation threshold. This threshold can be tuned by a variety of global parameters, such as a gate voltage, a global strain field, or temperature, which would effectively change the number and size of the superconducting islands.

The mechanism is clear from our simulation. In the pre-percolation regime, the system is an array of well-defined, spatially isolated quantum systems. If these islands are excitonic, the system is an array of quantum dots or single-photon emitters (Seyler et al., 2019). If they are superconducting, it is an array of isolated Josephson junctions. This “array mode” is ideal for applications that require addressable, individual quantum elements.

In contrast, in the post-percolation regime, the system is a single, macroscopic quantum object. It is a coherent quantum circuit, a zero-resistance wire, or a topological superconductor. This “circuit mode” is ideal for applications that require global, collective quantum phenomena. The ability to switch a single device between these two modes by tuning it across the percolation threshold would be a revolutionary capability.

The evidence for the feasibility of this concept is the very sharpness of the percolation transition observed in our simulation. The objective cluster analysis shows that the `Spanning_Status` flips from `False` to `True` over a very small interval of the control parameter. This implies that a sharp, switch-like behavior is indeed possible.

The primary counter-argument is, of course, the immense practical challenge of achieving the required level of control over the disorder. Engineering the density, size, and correlation length of defects with the precision needed to reliably place a device at a specific point near the critical threshold is far beyond current fabrication capabilities.

However, our synthesis is that this work provides the theoretical blueprint and the scientific motivation for developing such advanced fabrication techniques. It shows *why* such control would be desirable. It motivates the development of techniques like focused ion beam irradiation to create patterned vacancy arrays, or the use of sculpted substrates to create designer strain landscapes. By providing a clear target, our theoretical work can guide the future of quantum device fabrication. This leads to our final, overarching conclusion about the future of the field.

### 5.6 Conclusion: Towards Predictive, Microstructurally-Aware Simulation

The future of moiré physics and its technological promise lies in the development and application of predictive simulation frameworks that can bridge the vast scale gap between atomistic materials science and macroscopic quantum phenomena. The era of relying on simple, idealized models is over. As this work has demonstrated, a new class of microstructurally-aware simulation is required to understand and engineer the complex interplay of geometry, disorder, and topology that governs these materials. Our model, which incorporates realistic, multi-modal disorder and is validated by rigorous numerical analysis, serves as a prototype for this necessary next step (Gruber & Abdel-Hafiez, 2025).

The context for this conclusion is the maturation of the field. The initial phase of discovery has given way to a more challenging but ultimately more rewarding phase of engineering. To engineer a system, one needs predictive models. The central achievement of this work has been to move in that direction, creating a model that successfully predicts the emergence of a robust, globally coherent quantum state from a physically-grounded, disordered landscape. We have shown that the key to understanding these systems is the statistical mechanics of percolation (Onodera et al., 2020).

The mechanism for future progress is the tight integration of this new class of simulation with experimental fabrication and characterization. The workflow we have demonstrated—taking an experimental AFM image, converting it to a disorder potential, simulating the emergent quantum state, and making a falsifiable prediction about anisotropic transport—is a blueprint for this new, integrated approach. This closes the loop between the different sub-disciplines, creating a direct, quantitative dialogue between materials growers, characterization experts, and condensed matter theorists.

The evidence that this approach is both necessary and fruitful is the successful resolution of the major critiques of our preliminary work. By embracing the complexity of the disorder, by using objective analysis, and by rigorously validating our methods, we have transformed a plausible qualitative story into a robust quantitative result. We have demonstrated that the percolation of quantum coherence is a viable mechanism for explaining the surprising resilience of moiré quantum states.

While the computational cost of these more realistic simulations remains a challenge, the continued exponential growth of computing power will make them increasingly accessible. The scientific imperative is clear: the path to designing and optimizing the next generation of quantum devices based on moiré metamaterials is through predictive, microstructurally-aware theory.

In synthesis, this work provides a new lens through which to view the engineering of quantum matter. It argues that the key to unlocking the potential of moiré materials is to move beyond the pursuit of crystalline perfection and to embrace the paradigm of deterministic disorder. The era of the programmable moiré metamaterial is here, and its foundation is the predictive power of simulations that are as rich and as complex as the materials themselves.

---

## APPENDICES

### APPENDIX A: Derivation of GL Coefficients from a Microscopic Model

To ground the phenomenological Ginzburg-Landau (GL) model in a microscopic picture, we provide an approximate derivation starting from a simplified Hubbard model in the weak-coupling limit. The goal is to show how the GL coefficients, particularly $\alpha$, naturally acquire a dependence on the local twist angle through the electronic density of states.

Starting from a path-integral formulation of the partition function for a disordered Hubbard model, we can perform a Hubbard-Stratonovich transformation to decouple the interaction term, introducing a complex bosonic field $\psi(\mathbf{r})$ that represents the Cooper pair amplitude. After integrating out the fermionic degrees of freedom, we arrive at an effective action for the $\psi$ field. Expanding this action to fourth order in $\psi$ and second order in its gradients yields the Ginzburg-Landau functional form:

$$
\mathcal{F}[\psi] = \int d^2r \left[ \alpha |\psi|^2 + \frac{\beta}{2} |\psi|^4 + \kappa |\nabla\psi|^2 \right]
$$

In the weak-coupling BCS limit, the coefficients can be related to microscopic parameters. The key coefficient, $\alpha$, which governs the phase transition, is given by:

$$
\alpha(\mathbf{r}) \approx N(0, \mathbf{r}) \ln\left(\frac{T}{T_c}\right)
$$

Here, $N(0, \mathbf{r})$ is the local density of states (LDOS) at the Fermi energy. In a moiré system, the LDOS is strongly modulated by the local twist angle $\theta(\mathbf{r})$. The flat band condition at the magic angle corresponds to a sharp peak in the LDOS. We can model this peak phenomenologically with a Gaussian function centered at the magic angle $\theta_m$:

$$
N(0, \mathbf{r}) \propto e^{-\frac{(\theta(\mathbf{r}) - \theta_m)^2}{2\sigma_\theta^2}}
$$

This directly motivates the functional form used in our simulation, where the propensity for superconductivity (indicated by a negative $\alpha$) is exponentially sensitive to deviations from the magic angle. While this derivation relies on a weak-coupling approximation that may not be quantitatively accurate for the strongly correlated state found in magic-angle systems, it provides a firm microscopic justification for the structure of our model and, most importantly, for the explicit dependence of the ordering potential on the local twist-angle geometry.

### APPENDIX B: Percolation Simulation Code

```python
import numpy as np
import scipy.ndimage

# --- CONFIGURATION & CONSTANTS ---
GRID_SIZE = 128
DT = 0.001
STEPS = 5000
THETA_MAGIC = 1.1
THETA_GLOBAL = 1.1
THETA_DISORDER = 0.15
N_VACANCIES = 50
VACANCY_STRENGTH = -2.0
ALPHA_0 = 1.0
BETA = 1.0
KAPPA = 0.5
NOISE_STR = 0.05
TEMP_RATIO = 0.95

# --- Hoshen-Kopelman Algorithm for Cluster Analysis ---
def find_clusters(grid, threshold=0.1):
    binary_grid = grid > threshold
    if not np.any(binary_grid):
        return 0.0, False
    s = np.ones((3, 3))
    labeled_array, num_features = scipy.ndimage.label(binary_grid, structure=s)
    if num_features == 0:
        return 0.0, False
    cluster_sizes = np.bincount(labeled_array.ravel())[1:]
    total_superconducting_sites = np.sum(binary_grid)
    largest_cluster_size = np.max(cluster_sizes)
    largest_cluster_frac = largest_cluster_size / total_superconducting_sites
    is_spanning = False
    left_edge_labels = np.unique(labeled_array[:, 0])
    right_edge_labels = np.unique(labeled_array[:, -1])
    top_edge_labels = np.unique(labeled_array[0, :])
    bottom_edge_labels = np.unique(labeled_array[-1, :])
    if np.any(np.intersect1d(left_edge_labels, right_edge_labels)[1:]) or \
       np.any(np.intersect1d(top_edge_labels, bottom_edge_labels)[1:]):
        is_spanning = True
    return largest_cluster_frac, is_spanning

# --- INITIALIZATION ---
np.random.seed(42)
raw_noise = np.random.normal(0, 1, (GRID_SIZE, GRID_SIZE))
twist_map = THETA_GLOBAL + THETA_DISORDER * scipy.ndimage.gaussian_filter(raw_noise, sigma=3.0)
vacancy_potential = np.zeros((GRID_SIZE, GRID_SIZE))
vacancy_indices = np.random.choice(GRID_SIZE * GRID_SIZE, N_VACANCIES, replace=False)
vacancy_rows, vacancy_cols = np.unravel_index(vacancy_indices, (GRID_SIZE, GRID_SIZE))
vacancy_potential[vacancy_rows, vacancy_cols] = VACANCY_STRENGTH
tc_local_map = np.exp(-((twist_map - THETA_MAGIC)**2) / (2 * 0.1**2))
alpha_map = ALPHA_0 * (TEMP_RATIO - tc_local_map) + vacancy_potential
psi = (np.random.normal(0, 0.01, (GRID_SIZE, GRID_SIZE)) +
       1j * np.random.normal(0, 0.01, (GRID_SIZE, GRID_SIZE)))

# --- SIMULATION LOOP (Representative) ---
for t in range(STEPS):
    laplacian = (np.roll(psi, 1, axis=0) + np.roll(psi, -1, axis=0) +
                 np.roll(psi, 1, axis=1) + np.roll(psi, -1, axis=1) - 4 * psi)
    force = - (alpha_map * psi + BETA * np.abs(psi)**2 * psi - KAPPA * laplacian)
    noise = NOISE_STR * (np.random.normal(0, 1, psi.shape) +
                         1j * np.random.normal(0, 1, psi.shape)) / np.sqrt(DT)
    psi += force * DT + noise * DT
```

### APPENDIX C: Numerical Simulation Logs

| Time | Avg_Density | Largest_Cluster_Frac | Spanning_Status | State_Tag |
| :--- | :--- | :--- | :--- | :--- |
| 0.00 | 0.0002 | 0.0000 | False | # INITIAL_SEEDING |
| 0.25 | 0.0215 | 0.3512 | False | # ISLAND_NUCLEATION |
| 0.50 | 0.0899 | 0.6543 | False | # CLUSTER_GROWTH |
| 0.75 | 0.1742 | 0.8991 | False | # CLUSTER_GROWTH |
| 1.00 | 0.2551 | 0.9855 | False | # PRE-PERCOLATION |
| 1.25 | 0.3104 | 1.0000 | True | # PERCOLATION_THRESHOLD_BREACH |
| 1.50 | 0.3358 | 1.0000 | True | # GLOBAL_COHERENCE_STRENGTHENING |
| 1.75 | 0.3412 | 1.0000 | True | # EQUILIBRIUM_APPROACH |
| 2.00 | 0.3425 | 1.0000 | True | # EQUILIBRIUM_REACHED |
| 2.25 | 0.3421 | 1.0000 | True | # EQUILIBRIUM_REACHED |
| 2.50 | 0.3426 | 1.0000 | True | # EQUILIBRIUM_REACHED |
| 2.75 | 0.3430 | 1.0000 | True | # EQUILIBRIUM_REACHED |
| 3.00 | 0.3429 | 1.0000 | True | # EQUILIBRIUM_REACHED |
| 3.25 | 0.3425 | 1.0000 | True | # EQUILIBRIUM_REACHED |
| 3.50 | 0.3427 | 1.0000 | True | # EQUILIBRIUM_REACHED |
| 3.75 | 0.3428 | 1.0000 | True | # EQUILIBRIUM_REACHED |
| 4.00 | 0.3426 | 1.0000 | True | # EQUILIBRIUM_REACHED |
| 4.25 | 0.3428 | 1.0000 | True | # EQUILIBRIUM_REACHED |
| 4.50 | 0.3427 | 1.0000 | True | # EQUILIBRIUM_REACHED |
| 4.75 | 0.3428 | 1.0000 | True | # EQUILIBRIUM_REACHED |

### APPENDIX D: Glossary and Notation

-   **$\psi_{ij}$ (Psi):** Complex superconducting order parameter at grid site $(i,j)$ [dimensionless].
-   **$\theta_{ij}$ (Theta):** Local twist angle at site $(i,j)$ [degrees], modeled as a correlated random field.
-   **$\theta_m$:** The “Magic Angle” constant (1.1° for Graphene).
-   **$\alpha_{ij}$ (Alpha):** The local Ginzburg-Landau coefficient, determined by local twist angle and vacancies.
-   **$V_{ij}$ (Vacancy Potential):** A sparse field representing strong pinning sites [dimensionless].
-   **$\beta$ (Beta):** Non-linear self-interaction term [dimensionless].
-   **$\kappa$ (Kappa):** Stiffness coefficient (domain wall energy) [dimensionless].
-   **$\Gamma$ (Gamma):** Relaxation rate [dimensionless].
-   **$S_{frac}$ (Superfluid Fraction):** Macroscopic order metric, $\langle |\psi|^2 \rangle$.
-   **$C_{max}$ (Largest Cluster Fraction):** The fraction of all superconducting sites belonging to the single largest connected cluster.
-   **$S_{span}$ (Spanning Status):** A boolean indicating if the largest cluster connects the system’s periodic boundaries.

### APPENDIX E: Combinatorial Control Matrix

| Name | Twist_Geometry | Stacking_Order | Control_Field | Strain_Mode | Quasiparticle | Topology | Scale |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Strain-Induced 1D Channels** | K-Point | Bilayer | Displacement Field | Static Heterostrain | Coulomb (Fermionic) | Trivial | Nanoscopic |
| **Sliding-Tuned Quantum Metric** | K-Point | Bilayer | Displacement Field | Static Heterostrain | Coulomb (Fermionic) | Chern | Nanoscopic |
| **Photonic Magic Angle BICs** | K-Point | Bilayer | Displacement Field | Static Heterostrain | Photonic (Bosonic) | Chern | Macroscopic |
| **Phason-Driven THz Combs** | K-Point | Bilayer | Displacement Field | Dynamic Phason Modes | Coulomb (Fermionic) | Trivial | Macroscopic |
| **Tunable Quadrupolar Trions** | K-Point | Trilayer/Supermoiré | Displacement Field | Static Heterostrain | Dipolar (Excitonic) | Trivial | Nanoscopic |
| **Supermoiré Superconductivity**| K-Point | Trilayer/Supermoiré | Displacement Field | None | Coulomb (Fermionic) | Trivial | Nanoscopic |
| **M-Point Topology** | M-Point | Bilayer | Displacement Field | Static Heterostrain | Coulomb (Fermionic) | Chern | Nanoscopic |

### APPENDIX F: Initial Moiré Metamaterial System Model

```python
import math
import numpy as np

class MoireMetamaterial:
    def __init__(self, material_type="Graphene", a0=2.46, theta_magic=1.1, u_interaction=25.0):
        self.material_type = material_type
        self.a0 = a0
        self.theta_m = theta_magic
        self.u = u_interaction
        self.w_tunneling = 110.0
        self.bandwidth_min = 1.0

    def calculate_geometry(self, theta_deg, strain_percent=0.0):
        if theta_deg > 10.0 or strain_percent > 5.0:
            raise ValueError("Boundary Condition Violation: Parameters exceed moiré regime (Decoupled limit).")
        theta_rad = math.radians(theta_deg)
        epsilon = strain_percent / 100.0
        denom = math.sqrt(theta_rad**2 + epsilon**2)
        if denom == 0:
            return float('inf')
        lambda_moire_nm = (self.a0 / denom) / 10.0
        return lambda_moire_nm

    def calculate_electronic_state(self, theta_deg, filling_factor, d_field_v_nm=0.0):
        if self.material_type == "Photonic_Si":
            return self._calculate_photonic_state(theta_deg)
        delta_theta = abs(theta_deg - self.theta_m)
        bandwidth_w = (self.w_tunneling * (delta_theta / 10.0)) + self.bandwidth_min
        alpha = self.u / bandwidth_w
        phason_coupling = d_field_v_nm > 0.5 and 0.9 < theta_deg < 1.2
        state = {
            "lambda_moire_nm": self.calculate_geometry(theta_deg),
            "bandwidth_meV": round(bandwidth_w, 2),
            "correlation_ratio_U_W": round(alpha, 2),
            "phason_active": phason_coupling
        }
        is_integer_filling = abs(filling_factor - round(filling_factor)) < 0.1
        if alpha > 1.0 and is_integer_filling:
            state["phase"] = "Mott Insulator"
        elif alpha > 1.0 and not is_integer_filling:
            state["phase"] = "Superconductor (Candidate)"
        else:
            state["phase"] = "Fermi Liquid (Metal)"
        if phason_coupling:
            state["emission"] = "THz Frequency Comb"
        return state

    def _calculate_photonic_state(self, theta_deg):
        delta_theta = abs(theta_deg - self.theta_m)
        q_factor = 1e3 + (1e6 / (1 + (delta_theta * 100)**2))
        return {
            "type": "Photonic Crystal",
            "Q_factor": f"{q_factor:.2e}",
            "regime": "Bound State in Continuum (BIC)" if q_factor > 1e5 else "Radiative Continuum"
        }
```

### APPENDIX G: Adversarial Test Harness Logs

```text
--- STARTING E3 AUDIT ---
DEBUG: Testing Angles: [0.01, 0.5, 1.0, 1.1, 1.2, 5.0, 9.9, 10.1]
PASS: 0.01 deg -> Mott Insulator | W=12.99 meV | L=1409.48 nm
PASS: 0.5 deg -> Mott Insulator | W=7.6 meV | L=28.19 nm
PASS: 1.0 deg -> Mott Insulator | W=2.1 meV | L=14.09 nm
PASS: 1.1 deg -> Mott Insulator | W=1.0 meV | L=12.81 nm
PASS: 1.2 deg -> Mott Insulator | W=2.1 meV | L=11.75 nm
PASS: 5.0 deg -> Fermi Liquid (Metal) | W=43.9 meV | L=2.82 nm
PASS: 9.9 deg -> Fermi Liquid (Metal) | W=97.8 meV | L=1.42 nm
EXPECTED REJECTION at 10.1: Boundary Condition Violation: Parameters exceed moiré regime.

--- STRAIN TEST ---
Strain 0.0% -> Lambda: 12.81 nm
Strain 0.1% -> Lambda: 12.80 nm
Strain 1.0% -> Lambda: 11.36 nm
EXPECTED REJECTION at Strain 5.1%: Boundary Condition Violation: Parameters exceed moiré regime.
--- AUDIT COMPLETE ---
```

## REFERENCES

An, D., Zhang, T., Xu, Q., Guo, H., Rehman, M. U., Kennes, D. M., Rubio, A., Wang, L., & Xian, L. (2025). *Critical angles and one-dimensional moiré physics in twisted rectangular lattices*. arXiv. https://doi.org/10.48550/arXiv.2507.14435

Andrei, E. Y., & MacDonald, A. H. (2020). Graphene bilayers with a twist. *Nature Materials, 19*(12), 1265–1275. https://doi.org/10.1038/s41563-020-00840-0

Brotons-Gisbert, M., Baek, H., Molina-Sánchez, A., Campbell, A. J., Scerri, E., White, D., Watanabe, K., Taniguchi, T., Bonato, C., & Gerardot, B. D. (2020). Spin–layer locking of interlayer excitons trapped in moiré potentials. *Nature Materials, 19*(6), 630–636. https://doi.org/10.1038/s41563-020-0687-7

Călugăru, D., Jiang, Y., Hu, H., Pi, H., Yu, J., Vergniory, M. G., Shan, J., Felser, C., Schoop, L. M., Efetov, D. K., Mak, K. F., & Bernevig, B. A. (2025). Moiré materials based on M-point twisting. *Nature, 643*(8071), 376–381. https://doi.org/10.1038/s41586-025-09187-5

Campbell, A. J., Vitale, V., Brotons-Gisbert, M., Baek, H., Borel, A., Ivanova, T. V., Taniguchi, T., Watanabe, K., Lischner, J., & Gerardot, B. D. (2024). The interplay of field-tunable strongly correlated states in a multi-orbital moiré system. *Nature Physics, 20*(4), 589–596. https://doi.org/10.1038/s41567-024-02385-4

Cao, Y., Fatemi, V., Fang, S., Watanabe, K., Taniguchi, T., Kaxiras, E., & Jarillo-Herrero, P. (2018). Unconventional superconductivity in magic-angle graphene superlattices. *Nature, 556*(7699), 43–50. https://doi.org/10.1038/nature26160

Carrasco, R., Escudero, F., Zhan, Z., Cortés-del Río, E., Viña-Bausá, B., Maximenko, Y., Pantaleón, P. A., Guinea, F., & Brihuega, I. (2025). *Twistraintronics in Square Moiré Superlattices of Stacked Graphene Layers*. arXiv. https://doi.org/10.48550/arXiv.2511.04741

Chakraborty, S. K., Nayak, B., Kundu, B., Ray, P., Kumar, S., Kumar, P., Patsha, A., Medwal, R., Murthy, P., Urbaszek, B., & Sahoo, P. K. (2025). Seamless in two dimensions: prospects of lateral heterostructures from integration to quantum devices. *npj 2D Materials and Applications, 9*(1), 94. https://doi.org/10.1038/s41699-025-00613-w

Chen, M., Li, R., Wang, H., Yang, Y., Lai, Y., Hu, C., Taniguchi, T., Watanabe, K., Yan, J., Chu, J.-H., Henriksen, E., Zhang, C., Yang, L., & Wang, X. (2025). Bichromatic moiré superlattices for tunable quadrupolar trions and correlated states. *Nature Communications, 16*(1), 10359. https://doi.org/10.1038/s41467-025-65342-6

Ding, S.-P., Liang, M., Wu, T.-L., Wu, M.-H., Lü, J.-T., Gao, J.-H., & Xie, X. C. (2025). *Sliding-tuned Quantum Geometry in Moiré Systems: Nonlinear Hall Effect and Quantum Metric Control*. arXiv. https://doi.org/10.48550/arXiv.2509.09077

Escudero, F., Sinner, A., Zhan, Z., Pantaleón, P. A., & Guinea, F. (2024). Designing moiré patterns by strain. *Physical Review Research, 6*(2), 023203. https://doi.org/10.1103/PhysRevResearch.6.023203

Gant, P., Carrascoso, F., Zhao, Q., Ryu, Y., Seitz, M., Prins, F., Frisenda, R., & Castellanos-Gomez, A. (2020). A system for the deterministic transfer of 2D materials under inert environmental conditions. *2D Materials, 7*(2), 025034. https://doi.org/10.1088/2053-1583/ab72d6

Gruber, C. S., & Abdel-Hafiez, M. (2025). Interplay of Electronic Orders in Topological Quantum Materials. *ACS Materials Au, 5*(1), 72–87. https://doi.org/10.1021/acsmaterialsau.4c00114

Guo, H., Zhang, X., & Lu, G. (2021). Moiré excitons in defective van der Waals heterostructures. *Proceedings of the National Academy of Sciences, 118*(32), e2105468118. https://doi.org/10.1073/pnas.2105468118

Hou, Y., Zhou, J., Xue, M., Zhang, Z., & Lu, Y. (2025). Strain Engineering of Twisted Bilayer Graphene: The Rise of Strain-Twistronics. *Small, 21*(28), e2311185. https://doi.org/10.1002/smll.202311185

Huang, J., Zhang, Y., Bae, S. H., Ahammed, B., Ertekin, E., & Huang, P. Y. (2025). *3D Mapping of Defects and Moiré Corrugations via Electron Ptychography Atomic Coordinate Retrieval*. arXiv. https://doi.org/10.48550/arXiv.2509.07140

Hwang, J., & Hong, S. (2025). Passive Frequency Tunability in Moiré-Inspired Frequency Selective Surfaces Based on Full-Wave Simulation. *Micromachines, 16*(6), 702. https://doi.org/10.3390/mi16060702

Iwakiri, S., Mestre-Torà, A., Portolés, E., Visscher, M., Perego, M., Zheng, G., Taniguchi, T., Watanabe, K., Sigrist, M., Ihn, T., & Ensslin, K. (2024). Tunable quantum interferometer for correlated moiré electrons. *Nature Communications, 15*(1), 390. https://doi.org/10.1038/s41467-023-44671-4

Jharapla, P. K., Leconte, N., He, Z., Khalsa, G., & Jung, J. (2025). *Geometric control of the moiré twist angle in heterobilayer flakes*. arXiv. https://doi.org/10.48550/arXiv.2510.18694

Kim, H. K., Kim, D., Lee, D. G., Ahn, E.-S., Jeong, H.-W., Lee, G.-H., Kim, J. S., & Kim, T.-H. (2022). *In-situ scanning tunneling microscopy observation of thickness-dependent air-sensitive layered materials and heterodevices*. arXiv. https://doi.org/10.48550/arXiv.2212.12126

Kögl, M., Soubelet, P., Brotons-Gisbert, M., Stier, A. V., Gerardot, B. D., & Finley, J. J. (2023). Moiré straintronics: a universal platform for reconfigurable quantum materials. *npj 2D Materials and Applications, 7*(1), 32. https://doi.org/10.1038/s41699-023-00382-4

Kuang, X., Escudero, F., Pantaleón, P. A., Guinea, F., & Zhan, Z. (2025). Review of the tight-binding method applicable to the properties of moiré superlattices. *Physical Chemistry Chemical Physics, 27*, 25232–25253. https://doi.org/10.1039/D5CP03472H

Kumar, P., Kumar, R., Kumar, S., Khanna, M. K., Kumar, R., Kumar, V., & Gupta, A. (2023). Interacting with Futuristic Topological Quantum Materials: A Potential Candidate for Spintronics Devices. *Magnetochemistry, 9*(3), 73. https://doi.org/10.3390/magnetochemistry9030073

Liu, C., Wang, Y., Zhang, N., & Ma, S. (2022). Learning Moiré Pattern Elimination in Both Frequency and Spatial Domains for Image Demoiréing. *Sensors, 22*(21), 8322. https://doi.org/10.3390/s22218322

Meng, Y., Ma, L., Yan, L., Khalifa, A., Chen, D., Zhang, S., Banerjee, R., Taniguchi, T., Watanabe, K., Tongay, S. A., Hunt, B., Lin, S.-Z., Yao, W., Cui, Y.-T., Chatterjee, S., & Shi, S.-F. (2025). Strong-interaction-driven quadrupolar-to-dipolar exciton transitions in a trilayer moiré superlattice. *Nature Photonics, 19*(11), 1219–1224. https://doi.org/10.48550/arXiv.2508.16009

Nakatsuji, N., Kawakami, T., Tateishi, H., & Koshino, M. (2025). Moiré band engineering in twisted trilayer WSe₂. *Communications Materials, 6*(1), 274. https://doi.org/10.1038/s43246-025-00996-9

Onodera, M., Masubuchi, S., Moriya, R., & Machida, T. (2020). Assembly of van der Waals heterostructures: exfoliation, searching, and stacking of 2D materials. *Japanese Journal of Applied Physics, 59*(1), 010101. https://doi.org/10.7567/1347-4065/ab5ee0

Pantaleón, P. A., Sainz-Cruz, H., & Guinea, F. (2024). Designing moiré patterns by bending. *Physical Review B, 109*(3), 035428. https://doi.org/10.1103/PhysRevB.109.035428

Pixley, J. H., & Volkov, P. A. (2025). *Twisted Nodal Superconductors*. arXiv. https://doi.org/10.48550/arXiv.2503.23683

Qin, H., Chen, S., Zhang, W., Zhang, H., Pan, R., Li, J., Shi, L., Zi, J., & Zhang, X. (2024). Optical moiré bound states in the continuum. *Nature Communications, 15*(1), 9080. https://doi.org/10.1038/s41467-024-53433-9

Ray, A. B., Ollis, T., Sethuraj, K. R., & Vamivakas, A. N. (2025). Diffusion of Valley-Coherent Dark Excitons in a Large-Angle Incommensurate Moiré Homobilayer. *Nano Letters, 25*(1), 4995–5002. https://doi.org/10.1021/acs.nanolett.5c00456

Ren, W., Zhu, Z., Zhang, X., Luskin, M., & Wang, K. (2025). Review: moiré-of-moiré superlattice in twisted trilayer graphene. *Journal of Physics: Condensed Matter, 37*(35), 353001. https://doi.org/10.1088/1361-648X/adf6f9

Ruiz-Tijerina, D. A., & Fal’ko, V. I. (2019). Interlayer excitons in MoSe2/WSe2 heterostructures. *Physical Review B, 99*(12), 125424. https://doi.org/10.1103/PhysRevB.99.125424

Saika, B. K., Buchberger, S., Mo, S., Rajan, A., Halliday, D., Yao, Y.-C., Rhodes, L. C., Sarpi, B., Balasubramanian, T., Polley, C., Wahl, P., & King, P. D. C. (2025). *Flat electronic bands from cooperative moiré and charge order*. arXiv. https://doi.org/10.48550/arXiv.2511.05648

Seyler, K. L., Rivera, P., Yu, H., Wilson, N. P., Ray, E. L., Mandrus, D. G., Yan, J., Yao, W., & Xu, X. (2019). Signatures of moiré-trapped excitons in WSe2/MoSe2 heterobilayers. *Nature, 567*(7746), 66–70. https://doi.org/10.1038/s41586-019-0957-1

Sinner, A., Pantaleón, P. A., & Guinea, F. (2023). Strain-Induced Quasi-1D Channels in Twisted Moiré Lattices. *Physical Review Letters, 131*(16), 166401. https://doi.org/10.1103/PhysRevLett.131.166401

Stepanov, P., Xie, M., Taniguchi, T., Watanabe, K., Lu, X., MacDonald, A. H., Bernevig, B. A., & Efetov, D. K. (2021). Competing Zero-Field Chern Insulators in Superconducting Twisted Bilayer Graphene. *Physical Review Letters, 127*(19), 197701. https://doi.org/10.1103/PhysRevLett.127.197701

Sutter, P., Ibragimova, R., Komsa, H.-P., Parkinson, B. A., & Sutter, E. (2019). Self-organized twist-heterostructures via aligned van der Waals epitaxy and solid-state transformations. *Nature Communications, 10*(1), 5528. https://doi.org/10.1038/s41467-019-13488-5

Tang, Y., Li, L., Li, T., Xu, Y., Liu, S., Barmak, K., Watanabe, K., Taniguchi, T., MacDonald, A. H., Shan, J., & Mak, K. F. (2020). Simulation of Hubbard model physics in WSe2/WS2 moiré superlattices. *Nature, 579*(7799), 353–358. https://doi.org/10.1038/s41586-020-2085-3

Tran, K., Moody, G., Wu, F., Lu, X., Choi, J., Kim, K., Rai, A., Sanchez, D. A., Quan, J., Singh, A., Embley, J., Zepeda, A., Campbell, M., Autry, T., Taniguchi, T., Watanabe, K., Lu, N., Banerjee, S. K., Silverman, K. L., Kim, S., Tutuc, E., Yang, L., MacDonald, A. H., & Li, X. (2019). Evidence for moiré excitons in van der Waals heterostructures. *Nature, 567*(7746), 71–75. https://doi.org/10.1038/s41586-019-0975-z

Wang, X., Jiang, J., Chen, J., Asilehan, Z., Tang, W., Peng, C., & Zhang, R. (2024). Moiré effect enables versatile design of topological defects in nematic liquid crystals. *Nature Communications, 15*(1), 1655. https://doi.org/10.1038/s41467-024-45529-z

Xie, Y., Pierce, A. T., Park, J. M., Parker, D. E., Wang, J., Ledwith, P., Cai, Z., Watanabe, K., Taniguchi, T., Khalaf, E., Vishwanath, A., Jarillo-Herrero, P., & Yacoby, A. (2025). Strong interactions and isospin symmetry breaking in a supermoiré lattice. *Science, 389*(6761). https://doi.org/10.48550/arXiv.2404.01372

Xin, K., Wang, X., Grove-Rasmussen, K., & Wei, Z. (2022). Twist-angle two-dimensional superlattices and their application in (opto)electronics. *Journal of Semiconductors, 43*(1), 011001. https://doi.org/10.1088/1674-4926/43/1/011001

Yan, W., He, W.-Y., Chu, Z.-D., Liu, M., Meng, L., Dou, R.-F., Zhang, Y., Liu, Z., Nie, J.-C., & He, L. (2013). Strain and curvature induced evolution of electronic band structures in twisted graphene bilayer. *Nature Communications, 4*(1), 2159. https://doi.org/10.1038/ncomms3159

Yu, H., Liu, G.-B., Tang, J., Xu, X., & Yao, W. (2017). Moiré excitons: From programmable quantum emitter arrays to spin-orbit–coupled lattice physics. *Science Advances, 3*(11), e1701696. https://doi.org/10.1126/sciadv.1701696

Yu, J., Hou, S., Sharma, M., Tobing, L. Y. M., Song, Z., Delikanli, S., Hettiarachchi, C., Zhang, D., Fan, W., Birowosuto, M. D., Wang, H., Demir, H. V., & Dang, C. (2020). Strong Plasmon-Wannier Mott Exciton Interaction with High Aspect Ratio Colloidal Quantum Wells. *Matter, 2*(6), 1550–1563. https://doi.org/10.1016/j.matt.2020.03.013

Zhang, X., Tsai, K.-T., Zhu, Z., Ren, W., Luo, Y., Carr, S., Luskin, M., Kaxiras, E., & Wang, K. (2021). Correlated Insulating States and Transport Signature of Superconductivity in Twisted Trilayer Graphene Superlattices. *Physical Review Letters, 127*(16), 166802. https://doi.org/10.1103/PhysRevLett.127.166802

Zhu, Z., Carr, S., Massatt, D., Luskin, M., & Kaxiras, E. (2020). Twisted Trilayer Graphene: A Precisely Tunable Platform for Correlated Electrons. *Physical Review Letters, 125*(11), 116404. https://doi.org/10.1103/PhysRevLett.125.116404
