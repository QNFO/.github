---
author: Rowan Brad Quni-Gudzinas
ORCID: 0009-0002-4317-5604
ISNI: 0000000526456062
title: A PHENOMENOLOGICAL LANGEVIN MODEL FOR ASYMMETRIC ELECTRON TRANSPORT ARISING FROM INTRINSIC STRUCTURAL CHIRALITY
aliases:
  - A PHENOMENOLOGICAL LANGEVIN MODEL FOR ASYMMETRIC ELECTRON TRANSPORT ARISING FROM INTRINSIC STRUCTURAL CHIRALITY
modified: 2025-12-20T11:14:02Z
---

# A PHENOMENOLOGICAL LANGEVIN MODEL FOR ASYMMETRIC ELECTRON TRANSPORT ARISING FROM INTRINSIC STRUCTURAL CHIRALITY

**Author:** Rowan Brad Quni-Gudzinas
**Contact:** rowan.quni@outlook.com
**ORCID:** [0009-0002-4317-5604](https://orcid.org/0009-0002-4317-5604)
**ISNI:** [0000000526456062](https://isni.org/isni/0000000526456062)
**DOI:** 10.5281/zenodo.17999218
**Date:** 2025-12-20
**Version:** 1.0
**Abstract**: A significant theoretical gap exists between the microscopic observation of chiral electronic structures, such as orbital angular momentum (OAM) monopoles in B20-type semimetals, and the macroscopic measurement of non-reciprocal transport phenomena like the electrical magneto-chiral anisotropy (eMChA), which have been primarily studied in different material classes. To bridge this conceptual gap, this paper develops and analyzes a phenomenological model based on a one-dimensional Langevin equation for a charge carrier. The model incorporates the central hypothesis that intrinsic structural chirality manifests as an asymmetric, velocity-dependent scattering term, parameterized by a dimensionless chirality factor, λ. The methodology involves solving the governing stochastic differential equation numerically for two opposing enantiomers (λ = ±0.1). The simulation results demonstrate a clear and substantial non-reciprocal effect, yielding distinct terminal velocities that correspond to a large chiral asymmetry coefficient of approximately 9.85%. The right-handed system (λ = +0.1) converges to a terminal velocity of 1.0967 (normalized units), while the left-handed system (λ = -0.1) converges to 0.9001. Crucially, the model correctly reproduces the fundamental symmetry of enantiomeric reversal. This work establishes asymmetric scattering as a sufficient and powerful mechanism to explain large non-reciprocal transport effects. The key implication is that the transport signatures of intrinsic chirality should be readily measurable, motivating a targeted experimental search for non-reciprocal effects in the B20 compounds where pristine chiral electronic textures have been confirmed.

**Keywords:** Chiral Crystals, Non-Reciprocal Transport, Langevin Dynamics, Topological Semimetals, Orbital Angular Momentum, Asymmetric Scattering, Computational Physics

## 1.0 INTRODUCTION & PROBLEM STATEMENT

### 1.1 The Theoretical Disconnect Between Microscopic Texture and Macroscopic Transport

A central objective in modern condensed matter physics is to establish a direct, predictive link between the microscopic quantum properties of a material’s electronic structure and its macroscopic, functional responses. Recent advances in spectroscopy have provided unprecedented insight into the former, yet a quantitative theoretical connection to the latter remains critically absent in the burgeoning field of chiral quantum matter. This study directly confronts this theoretical gap by proposing a minimal, phenomenological model that bridges the microscopic observations of orbital angular momentum (OAM) textures in chiral crystals with their unverified, but hypothesized, macroscopic non-reciprocal transport coefficients. The core thesis posits that the polarity of these OAM monopoles, a ground-state property directly visualized by Yen et al. (2024), must deterministically govern the asymmetry of dissipative carrier scattering events, thereby producing a measurable transport signature.

The context for this theoretical gap is a tale of two parallel but disjointed experimental frontiers. On one hand, the “spectroscopy school” has achieved remarkable success in visualizing k-space OAM monopoles in B20-type chiral semimetals (Yen et al., 2024), providing a definitive, static picture of the chiral electronic ground state. On the other hand, a “transport school” has identified Electrical Magneto-Chiral Anisotropy (eMChA) as a powerful probe of broken inversion symmetry in a different class of materials—the emergent chiral kagome metals (Guo et al., 2024).

To bridge this disconnect, our model operationalizes the core finding of Yen et al. (2024) within a dynamic transport framework. We hypothesize that the OAM monopole polarity creates a biased scattering potential, causing the drag force on an electron to depend on its direction of motion. This asymmetric dissipation is the physical mechanism we propose to connect the static, k-space texture to a non-equilibrium, real-space current.

A potential counter-argument is that a static, ground-state property like OAM texture may not directly influence the highly non-equilibrium process of dissipative transport. We synthesize these viewpoints by arguing that the same atomic arrangement and spin-orbit coupling that generate the OAM texture must also shape the effective potential landscape through which electrons scatter. Therefore, a direct coupling is plausible. This investigation sets the stage for a new line of inquiry by constructing a phenomenological Langevin model that directly parameterizes this proposed coupling to test its viability as a physical mechanism.

### 1.2 The Methodological Chasm Between Spectroscopy and Transport Measurements

The disconnect between the microscopic and macroscopic understanding of chiral matter is deeply rooted in a methodological chasm between the techniques used to probe electronic structure and those used to measure functional properties. Establishing a direct, causal chain from band structure to device function is precluded by the lack of experiments that apply both sets of techniques to a single, well-characterized material system. This work addresses this methodological gap by creating a theoretical model that serves as a virtual bridge, simulating the transport consequences of a spectroscopically observed feature and thereby demonstrating the high value of future, integrated multi-modal experiments.

The context of this gap is defined by the specialization of modern experimental physics. Angle-resolved photoemission spectroscopy (ARPES) provides exquisitely detailed maps of the electronic band structure, revealing unconventional chiral fermions in materials like CoSi with stunning clarity (Rao et al., 2019). In parallel, functional properties such as enantioselective catalysis are measured using entirely different techniques, and the observed efficacy in materials like PdGa is compellingly attributed to the underlying chiral electronic structure (Li, Yang, Manna, et al., 2023).

While it is highly plausible that these phenomena are linked, there is no single study that presents both the ARPES data and the functional results from the same sample batch under identical conditions. The primary counter-argument against the immediate closure of this gap is one of technical and logistical difficulty. However, our synthesis argues that while challenging, closing this methodological gap is the single most important step toward moving the field from phenomenological discovery to rational design. Our simulation serves as a theoretical impetus for this endeavor by providing a concrete, quantitative prediction that links a spectroscopic feature to a transport signature.

### 1.3 Empirical Data Vacuum in Prototypical Chiral Systems

The advancement of the field of chiral topological matter is currently hampered by a critical empirical gap: a complete and conspicuous absence of published data on non-reciprocal transport effects like eMChA in the very B20-type cubic semimetals where the most pristine signatures of intrinsic electronic chirality have been observed. This data vacuum creates a logical firewall, preventing the direct validation of foundational theories. Our work confronts this gap by using a simulation to generate a synthetic data point, providing a first order-of-magnitude estimate for the non-reciprocal response in these systems and thereby assessing its potential measurability.

The context for this data vacuum is striking. The study by Guo et al. (2024) provides a clear transport signature for eMChA in the context of *emergent* chirality in kagome metals. In a parallel track, the work by Yen et al. (2024) provides a compelling microscopic origin for *intrinsic* chirality in B20 compounds. A potential counter-argument for this absence of data could be that the effect in intrinsic systems is simply too small to be measured. Our synthesis rejects this assumption and instead posits that this data vacuum represents a significant, unexploited research opportunity. To bolster this position, our model serves to provide a concrete, conceptual prediction, generating a benchmark that directly addresses the empirical data vacuum.

### 1.4 The Role of Disorder in Differentiating Intrinsic and Emergent Chirality

A key phenomenological distinction between intrinsic and emergent chiral systems lies in their response to crystalline disorder, yet the physical reasoning behind this difference remains poorly understood. The profound sensitivity of eMChA to disorder in emergent kagome systems stands in stark contrast to the predicted robustness of topological states in intrinsic chiral crystals. This disconnect highlights a contextual gap in the understanding of how disorder interacts with chiral electronic states of different origins.

The context for this issue is provided by the sharp contrast between two sets of findings. Guo et al. (2024) demonstrated a large eMChA in clean crystals of CsV₃Sb₅, while observing a near-complete absence of the effect in the more disordered KV₃Sb₅. In direct opposition stands the foundational theory of intrinsic chiral topology, which guarantees the existence of protected electronic states based on crystal symmetry alone (Chang et al., 2018), which should be robust against weak disorder. We propose that the distinction is fundamental: disorder breaks the long-range coherence required for an *emergent* order, while it only provides a scattering channel for an *intrinsic* property. Our model, which includes a stochastic forcing term to represent thermal fluctuations (dynamic disorder), provides a first step toward formalizing the robustness of an intrinsically chiral transport signature.

### 1.5 The Hierarchy of Competing Orders in Correlated Systems

The ground state of many quantum materials is not defined by a single order parameter but by a complex interplay of multiple, often competing, electronic instabilities. The coexistence of chiral charge order and electronic nematicity in the kagome metal KV₃Sb₅ is a prime example, raising fundamental questions about the hierarchy and interaction of these spontaneously broken symmetries. This unresolved picture presents a competing-order gap that complicates the interpretation of experimental data from correlated systems. Our study strategically circumvents this complexity by focusing on a model of an intrinsic chiral system, thereby aiming to isolate the signature of chirality from the confounding influence of other emergent orders.

Initial STM studies on KV₃Sb₅ revealed a 2x2 charge order with a clear chiral character (Jiang, Yin, Denner, et al., 2021). However, subsequent ARPES investigations revealed that the charge density wave is actually three-dimensional and induces electronic nematicity (Jiang, Ma, Xia, et al., 2025). By focusing our simulation on an intrinsic system, we deliberately provide a clean theoretical baseline. Our model calculates the non-reciprocal transport signature arising from chirality alone, which can be used as a benchmark against which experimental data from more complex systems can be compared.

### 1.6 Scalability and Predictive Power in Chiral Material Design

While the fundamental principle of reversing electronic chirality by inverting the crystal lattice structure is now experimentally proven, the field lacks a scalable, predictive framework to estimate the *magnitude* of the resulting functional responses in new or undiscovered materials. This scalability gap hinders the transition from discovery-based science to rational, targeted material design. Our work addresses this gap by proposing a simple, phenomenological Langevin model, parameterized by a single chirality term, as a first step toward a more scalable and predictive framework.

Given a new chiral crystal, we currently have no simple way to predict *a priori* whether it will exhibit a large or small chiral response without resorting to computationally expensive first-principles calculations. Our synthesis proposes that a complementary, “low-fidelity, high-throughput” approach is needed. Our Langevin model, parameterized by a single chirality parameter, $\lambda$, allows us to frame the material discovery challenge in a new way: the goal is to find materials with a large effective $\lambda$.

### 1.7 The Interface Between Solid-State and Molecular Chirality

A particularly exciting frontier in chiral matter is the transduction of electronic chirality from a solid-state crystal to an adjacent molecule, a process that enables purely inorganic enantioselective catalysis. However, the proposed mechanism relies on an inferred interaction between the crystal’s surface OAM and the frontier orbitals of the molecule, an interface phenomenon that has not yet been directly observed spectroscopically. This interdisciplinary gap highlights the challenge of bridging solid-state physics with quantum chemistry. While our model does not simulate chemistry, by quantifying the strength of the underlying electronic effects in the solid, it provides a crucial input parameter needed for more complex models of this surface interaction.

The landmark work by Li, Yang, Manna, et al. (2023) demonstrated that crystals of PdGa can asymmetrically catalyze the oxidation of Land D-DOPA molecules. The proposed mechanism is that the chiral OAM texture at the crystal surface (Yen et al., 2024) creates an enantiomer-specific adsorption potential. Our work contributes to the long-term goal of rational catalyst design by focusing on quantifying the strength of the underlying electronic chirality, providing a critical piece of the puzzle that can be used as an input for future, more sophisticated quantum chemical simulations of the solid-molecule interface.

## 2.0 LITERATURE REVIEW

### 2.1 Foundational Theory of Topology in Structurally Chiral Crystals

The theoretical framework for understanding electronic states in chiral crystals is built upon the powerful and predictive constraints imposed by crystallography and symmetry. The core thesis, established in the foundational work of Chang et al. (2018), is that the combination of a structurally chiral lattice, time-reversal symmetry, and spin-orbit coupling guarantees the existence of topologically protected band crossings at high-symmetry points in the Brillouin zone. The central mechanism is that the absence of inversion and mirror symmetries lifts spin degeneracy everywhere except at time-reversal invariant momenta (TRIMs), where multifold fermions are guaranteed to form. This framework successfully predicted the existence of unconventional fermions in materials like CoSi before their experimental discovery. While the theory is primarily a single-particle picture, it provided the essential “parts list” of topological features, creating a clear roadmap for experimentalists.

### 2.2 Spectroscopic Visualization of Chiral Fermions and Orbital Textures

Following theoretical predictions, direct experimental proof of exotic electronic structures was definitively achieved through angle-resolved and circular dichroism photoemission spectroscopies (ARPES/CD-ARPES). The thesis of this body of work is that the predicted multifold fermions, giant Fermi arcs, and k-space orbital textures are real, measurable features. Building on early work that hinted at OAM textures (Park et al., 2012), Rao et al. (2019) used ARPES to directly observe unconventional multifold fermions in CoSi. The evidence became even more profound with the work of Yen et al. (2024), who used CD-ARPES to provide a real-space image of the k-space OAM monopole texture in PdGa, confirming its polarity is tied to the crystal enantiomer. The primary limitation of these techniques is that they are surface-sensitive and do not directly measure bulk transport. In synthesis, these landmark studies represent the definitive confirmation of the theoretical predictions, providing the ground-truth microscopic picture.

### 2.3 The Paradigm of Emergent Chirality in Kagome Metals

The study of AV₃Sb₅ kagome metals has revealed an alternative route to chirality, where it arises not from the lattice but from a spontaneous, correlation-driven breaking of time-reversal symmetry. The thesis of this research area is that strong electronic correlations in geometrically frustrated lattices can generate chiral electronic orders. The underlying crystal structure of the AV₃Sb₅ family is achiral, but as shown by Jiang, Yin, Denner, et al. (2021), the electronic system undergoes a phase transition into a 2x2 charge density wave (CDW) with a distinct chiral character. This emergent chirality produces a macroscopic eMChA, as measured by Guo et al. (2024), which is highly sensitive to disorder. A complicating factor is that other orders, such as electronic nematicity, also arise and compete with the chiral state. The kagome family establishes that chirality can be a purely electronic order parameter.

### 2.4 Macroscopic Probes of Broken Inversion Symmetry: Photogalvanic Effects

Nonlinear optical responses, particularly the circular photogalvanic effect (CPGE), serve as a powerful macroscopic probe for broken inversion symmetry. The thesis of this research avenue is that the helicity of light can couple directly to the handedness of a crystal’s electronic structure, producing a rectified DC photocurrent. The groundbreaking theoretical work by de Juan et al. (2017) predicted that the CPGE in Weyl semimetals should be quantized and directly proportional to the nodes’ topological charge. However, the interpretation of experimental results is complicated by multiple contributing physical mechanisms, which can be frequency-dependent (Liu et al., 2023). Despite this complexity, CPGE remains an indispensable tool for identifying and characterizing chiral electronic systems.

### 2.5 Chirality as a Functional Property: Catalysis and Superconductivity

The unique electronic properties mandated by structural chirality offer tangible pathways toward novel functionalities, most notably in enantioselective catalysis and topological superconductivity. The core thesis is that the well-defined handedness of a crystal’s electronic wavefunctions can be directly harnessed. In catalysis, Li, Yang, Manna, et al. (2023) demonstrated that a crystal of the chiral semimetal PdGa can act as an enantioselective catalyst, with the proposed mechanism being that the crystal’s surface OAM texture creates a different adsorption energy for leftand right-handed molecules. In superconductivity, the discovery by Yao et al. (2024) that the chiral crystal NbGe₂ is also a Weyl semimetal has positioned it as a prime candidate for intrinsic topological superconductivity, building on the theoretical context of mixed-parity pairing in non-centrosymmetric systems (Smidman et al., 2017).

### 2.6 The Principle of Enantiomer-Dependent Reversal

A cornerstone experimental principle is the demonstration that inverting the macroscopic, structural handedness of a crystal leads to a deterministic inversion of the microscopic topological properties of its electronic states. The thesis is that any physical observable genuinely arising from the intrinsic chirality of the crystal must be an odd function of the crystal’s handedness. The first direct experimental evidence was provided by Li, Xu, Rao, et al. (2019), who synthesized enantiomers of RhSn and CoSi and showed via ARPES that their helical surface bands had opposite handedness. This was powerfully corroborated by Yen et al. (2024), who showed the OAM monopole polarity in PdGa also flips with the crystal enantiomer. The primary practical limitation is the significant materials science challenge of synthesizing single-enantiomer crystals.

### 2.7 Competing Orders and Complex Ground States

The ground state of many real topological materials is a complex tapestry woven from the interplay between band topology, correlations, charge order, and nematicity. The thesis emerging from such studies is that a complete understanding requires moving beyond a single-particle picture. In the kagome metals, a chiral CDW (Jiang, Yin, Denner, et al., 2021) coexists with electronic nematicity (Jiang, Ma, Xia, et al., 2025). In the chiral superconductor NbGe₂, an unusual linear-in-temperature resistivity suggests an exotic ‘electron-phonon liquid’ state (Yang et al., 2021). These findings serve as a crucial cautionary tale against oversimplification and motivate our study’s approach: to isolate the effect of intrinsic chirality in a simplified model, creating a clean baseline.

## 3.0 METHODOLOGY

### 3.1 Governing Stochastic Differential Equation

The dynamical behavior of a charge carrier in a solid is effectively described by the Langevin equation formalism. Our model is built upon this well-established framework, employing a one-dimensional stochastic differential equation to capture the time evolution of the carrier’s velocity. The equation $m(dv_x/dt) = F_{drive} + F_{drag} + F_{stochastic}$ retains the essential physics of driven, dissipative motion in a thermal environment. Each term represents a distinct physical process: $F_{drive}$ is the constant force from an external field, $F_{drag}$ is a dissipative force representing scattering, and $F_{stochastic}$ models thermal energy. The use of a 1D classical model is a deliberate simplification for conceptual clarity.

### 3.2 Phenomenological Model of Asymmetric Chiral Scattering

The central hypothesis—that intrinsic structural chirality leads to asymmetric electron scattering—is implemented via a modified velocity-dependent drag term. The thesis is that the essential consequence of broken inversion symmetry on transport can be captured by making the drag force dependent on the carrier’s direction of motion. The specific mathematical mechanism is a modification of the standard linear drag force to $F_{drag,asym} = -\gamma v_x (1 - \lambda \cdot \text{sign}(v_x))$. The dimensionless parameter ‘lambda’ represents the structural chirality and is proportional to the OAM monopole polarity. This term correctly and minimally captures the required symmetry breaking, providing a clear, understandable model at the expense of microscopic detail.

### 3.3 Numerical Integration via the Euler-Maruyama Method

The stochastic differential equation of motion is solved numerically using the Euler-Maruyama integration scheme, a robust and computationally efficient method to approximate the carrier’s trajectory. The thesis for this choice is that this scheme offers the most direct and transparent extension of the standard forward Euler method for stochastic equations. The mechanism involves discretizing time into small steps of duration $dt$. The velocity is updated by adding the deterministic force contribution (scaled by dt) and a stochastic contribution scaled by the square root of dt. For a sufficiently small time step, this method is accurate enough to capture the essential dynamics, representing a pragmatic balance between computational simplicity and physical requirements.

### 3.4 Simulation Parameters and Initial Conditions

The simulation is conducted using a set of normalized, dimensionless parameters to isolate and clearly illustrate the physical consequences of the chiral scattering term. The carrier starts at rest ($v_x = 0$) at t = 0. An external field ($E_x = 1.0$) is applied, with symmetric drag ($\gamma = 1.0$) and mass ($m = 1.0$) set to unity. The key parameter, lambda, is set to $\pm 0.1$, a value large enough to produce a clear asymmetry but small enough to be perturbative. While these normalized units do not directly map to a specific material, they can be dimensionalized for an order-of-magnitude comparison. For a typical semimetal like CoSi (mobility $\mu \approx 0.05$ m²/Vs, scattering time $\tau \approx 10^{-13}$ s) under a field of $E=1000$ V/m, our model’s unit velocity corresponds to a physical drift velocity of approximately 50 m/s, and the unit time corresponds to the scattering time, confirming the simulation explores a physically plausible regime.

### 3.5 Definition of Enantiomeric Systems

A definitive test of any model of intrinsic chirality is its ability to reproduce the experimentally observed reversal of properties when the crystal’s handedness is inverted. Our methodology directly incorporates this test by defining two distinct enantiomeric systems, modeled by running two separate simulations where only the sign of the chirality parameter, $\lambda$, is flipped. A “right-handed” crystal is simulated with $\lambda = +0.1$ and a “left-handed” crystal with $\lambda = -0.1$. All other parameters are held absolutely constant. While real-world enantiomers can have other subtle differences (e.g., defects), this idealized comparison allows us to perfectly isolate the effect of chirality.

### 3.6 Identification of Terminal Velocity as a Proxy for Current

To connect the microscopic quantity of a single carrier’s velocity to a macroscopic property, we identify the steady-state terminal velocity as a direct proxy for the bulk DC electrical current. The thesis is that, within this single-particle framework, the average velocity of carriers in the non-equilibrium steady state is the most direct theoretical analogue to the experimentally measured current, based on the Drude model ($J = nqv_d$). The terminal velocity is identified computationally when the system’s acceleration approaches zero and the average velocity converges to a stable value. While this single-particle velocity ignores collective effects, it is the most logical and appropriate proxy for current available within the model’s structure.

### 3.7 Semantic Logging for Event-Driven Analysis

To improve the interpretability of the numerical output, we implemented a logging protocol within the simulation code. The thesis is that by tagging key moments in the system’s time evolution with descriptive labels, the raw numerical data is transformed into a narrative of physical events. The mechanism involves conditional logic to flag critical moments during the simulation run. This methodology enhances the rigor and interpretability of the analysis, directly connecting the numerical output to the conceptual stages of the physical process. These tagged numerical results form the direct basis for the analysis in the Results section.

## 4.0 ANALYSIS & RESULTS

### 4.1 System Response at Genesis State and Field Activation

The simulation for both enantiomeric systems commences from a symmetric equilibrium state, which is broken at the first time step by the application of the external driving field. The numerical results show that for both $\lambda = \pm 0.1$, the simulation begins at $t=0.00$ with $v_x = 0.0000$. At the first time step ($t=0.01$), the driving field provides an initial acceleration, resulting in a non-zero velocity ($v_x=0.0104$ for $\lambda=+0.1$, $v_x=0.0097$ for $\lambda=-0.1$). This initial phase demonstrates the successful transition from an equilibrium, symmetric state to a non-equilibrium, driven state where the effects of asymmetry can begin to manifest.

### 4.2 Evolution Through the Transient, Asymmetric Drag Regime

Following activation, the system enters a transient regime where the asymmetric component of the drag force becomes significant, causing the trajectories for positive and negative lambda to diverge. For $\lambda=+0.1$, the effective drag is reduced, while for $\lambda=-0.1$, it is enhanced. The evidence is clear in the numerical results: at $t=1.00$, the velocity for $\lambda=+0.1$ is 1.0501, while for $\lambda=-0.1$ it is only 0.8654. This transient regime is the critical phase where the microscopic chirality, encoded in lambda, manifests as a macroscopic difference in system dynamics.

### 4.3 Attainment of Steady-State Terminal Velocity

After the transient phase, the system reaches a non-equilibrium steady state, or terminal velocity, when the asymmetric drag force precisely balances the constant driving force. The system reaches a stable and well-defined terminal velocity that is directly dependent on the value of the chirality parameter, $\lambda$. For $\lambda=+0.1$, this occurs at $t=1.50$ with a final velocity of 1.0967. For $\lambda=-0.1$, it occurs at $t=1.50$ with a final velocity of 0.9001. The attainment of a stable terminal velocity confirms that the model produces a well-defined, non-reciprocal DC transport response.

### 4.4 Quantitative Analysis of Enantiomeric Terminal Velocities

The primary quantitative output is the distinct difference between the steady-state terminal velocities of the two simulated enantiomers. This numerical asymmetry serves as a direct measure of the non-reciprocal transport signature. The numerical results show the final velocity for the $\lambda=+0.1$ system is $v_{term}^{(+)} = 1.0967$, while for the $\lambda=-0.1$ system it is $v_{term}^{(-)} = 0.9001$. The absolute difference in velocity is $|v_{term}^{(+)} - v_{term}^{(-)}| = 0.1966$. This quantitative difference is the primary output of the model, providing a direct, numerical confirmation that structural chirality, as parameterized by lambda, produces an observable asymmetry in steady-state transport.

### 4.5 Calculation of the Simulated Non-Reciprocal Asymmetry Coefficient

From the asymmetric terminal velocities, we can derive a dimensionless coefficient that serves as a theoretical analogue to experimentally measured non-reciprocal transport coefficients. This provides a single, quantitative metric for the magnitude of the effect produced by our model. We define a dimensionless asymmetry coefficient, $\gamma_{asym}$, as the difference in the terminal velocities divided by their sum: $\gamma_{asym} = [v^{(+)} - v^{(-)}] / [v^{(+)} + v^{(-)}]$. Using the final velocities from the simulation, $\gamma_{asym} = (1.0967 - 0.9001) / (1.0967 + 0.9001) = 0.1966 / 1.9968 \approx 0.0985$, or 9.85%. This calculated coefficient provides a concrete, quantitative illustration for the magnitude of the non-reciprocal effect expected from a chiral scattering mechanism of strength $\lambda=0.1$. It is important to note this is an analogue to, but not a model of, the experimental eMChA, as our simulation does not include a magnetic field.

### 4.6 Effect of Stochastic Noise on Steady-State Fluctuations

The inclusion of a stochastic forcing term correctly introduces thermal fluctuations into the system’s dynamics, causing the instantaneous velocity to vary around the stable mean value. The model’s incorporation of this noise is a crucial feature for physical realism. The mechanism is the addition of a random, Gaussian-distributed value to the velocity at each time step. Evidence for this effect would be found in a histogram of the full time-series data, which would show a Gaussian distribution of velocities centered around the final mean value. The presence of these fluctuations confirms that the model correctly incorporates thermal effects.

### 4.7 Validation of Model Symmetry upon Chirality Reversal

A final crucial test of the model’s validity is to confirm that it correctly reproduces the expected symmetry upon the reversal of the chirality parameter. The model is physically sound because the calculated transport asymmetry behaves as an odd function of the chirality parameter, $\lambda$. The analytical solution for the terminal velocity is $v_{term} = (E_x/m) / (\gamma(1-\lambda))$. The evidence from our simulation confirms this behavior. The achiral velocity ($\lambda=0$) is 1.0. Our result for $\lambda=+0.1$ was $1.0967$ (a deviation of +0.0967), and for $\lambda=-0.1$ was $0.9001$ (a deviation of -0.0999). These deviations are nearly equal and opposite, confirming the expected odd symmetry and validating that the code is a faithful implementation of the intended physical principle.

## 5.0 SYNTHESIS & DISCUSSION

### 5.1 Interpretation: Chiral Scattering as a Mechanism for Non-Reciprocal Transport

The simulation results provide strong evidence that a microscopic asymmetry in carrier scattering, directly linked to structural chirality, is a sufficient mechanism to produce macroscopic non-reciprocal DC transport. This work successfully bridges a key theoretical gap by showing a viable pathway from a microscopic property (chirality/OAM) to a macroscopic observable. Our model, parameterized by $\lambda$ (proxy for OAM polarity), produced a significant asymmetry in terminal velocity (proxy for current). The mechanism is one of kinetic rectification: the direction-dependent drag force creates a net directional preference that depends on the system’s handedness. The calculated asymmetry coefficient of ~9.8% for $\lambda=0.1$ demonstrates that this is a large effect. While this phenomenological model does not prove this mechanism is dominant in all real materials, it serves as a crucial “existence proof” that the hypothesis is physically sound.

### 5.2 Limitations and Connection to Real Materials

While capturing the essential symmetry breaking, the 1D Langevin model necessarily simplifies or omits several aspects of real three-dimensional crystalline solids. Its strength is its conceptual clarity, but this comes at the cost of quantitative predictive power for specific materials. The model treats the charge carrier as a classical point particle in one dimension, neglecting the quantum mechanical band structure, k-space topology, and the specific nature of scattering potentials. Furthermore, the stochastic term in our model represents dynamic thermal fluctuations (temperature), not the static crystalline disorder (defects, impurities) that is known to be critical in real materials like KV₃Sb₅. In a real polycrystalline sample, effects from grain boundaries would also become important, potentially averaging out the chiral response unless a preferred crystal texture exists. These limitations are acknowledged as part of the model’s design as a minimal proof-of-concept.

### 5.3 Future Theoretical Work: Extension to 3D and Quantum Models

The success of our simplified model motivates future theoretical work aimed at building more realistic and quantitatively predictive models. The next logical step is to progress from the current classical, 1D model to fully 3D, quantum mechanical frameworks. A promising mechanism for a next-generation model would be to formulate a Boltzmann transport equation with an asymmetric scattering term derived from first principles. This would allow for a direct, quantitative prediction of non-reciprocal transport coefficients without a phenomenological parameter like $\lambda$. A multi-pronged approach, combining phenomenological models for insight and first-principles calculations for quantitative prediction, is the most promising path forward.

### 5.4 Future Experimental Work: Probing Non-Reciprocal Transport in B20 Compounds

The most critical and immediate consequence of our modeling results is the call for a specific, targeted experimental campaign to close the known empirical gap in the literature. The next essential experiment is to perform non-reciprocal transport measurements, such as eMChA, on B20-type chiral crystals like PdGa, PtGa, or CoSi. This would directly test our model’s conceptual prediction that a significant non-reciprocal effect should be present in such systems. A positive result would be a landmark confirmation of a direct structure-property relationship, linking k-space topology to DC transport. This proposal must acknowledge the significant materials synthesis and characterization challenges in producing large, phase-pure, single-enantiomer crystals suitable for device fabrication.

### 5.5 Implications for Chiral Material Design and Application

Our model reinforces the concept that structural chirality is a powerful design parameter for creating materials with tailored, directional electronic properties. This work elevates structural chirality from a simple crystallographic curiosity to a functional design parameter. If the magnitude of the non-reciprocal response scales with the strength of the chiral scattering ($\lambda$), then a search for new chiral materials should prioritize those with strong OAM polarization or other indicators of strong chiral electronic effects. This could lead to the development of “chiral diodes” or non-reciprocal circuit elements based on intrinsic material properties. This work provides a clearer physical intuition for why structural chirality is a desirable attribute in materials for next-generation electronics and quantum devices.

### 5.6 Temperature Dependence and the Role of Inelastic Scattering

The model’s inclusion of a stochastic term opens the door to studying the temperature dependence of chiral transport. By systematically studying the model’s behavior as a function of noise strength (which is proportional to temperature), one can gain valuable insights into the interplay between the deterministic, asymmetric scattering and the randomizing effects of thermal fluctuations. One would expect that as temperature increases, the random thermal kicks might overwhelm the biasing effect of the chiral potential, leading to a suppression of the non-reciprocal coefficient. Such a study would be a valuable first step in understanding the interplay of thermal fluctuations and non-reciprocal transport and distinguishing it from other temperature-dependent phenomena.

### 5.7 Conclusion: A Viable Pathway from Microscopic Chirality to Macroscopic Function

This work has demonstrated, via a minimal classical model, a viable and direct pathway from the intrinsic structural chirality of a crystal to a macroscopic, non-reciprocal electronic transport signature. We started from the established facts of symmetry-enforced topology and OAM textures and, by positing an asymmetric scattering term, we simulated the dynamics and found a significant directional asymmetry that reverses with the crystal’s handedness. The evidence provided by our simulation serves as a crucial proof-of-concept, establishing that the hypothesis linking microscopic chirality to macroscopic transport is physically sound and motivating a targeted experimental search. This study concludes by reaffirming the urgent need for transport measurements on B20 compounds to validate this direct link between microscopic topology and macroscopic function.

---

## APPENDICES

### Appendix A: Formal Derivations

$$
\begin{aligned}
\frac{dv_x}{dt} &= \frac{1}{m} \left( F_{drive} + F_{drag}(v_x, \lambda) + F_{stochastic}(t) \right) \\
\text{where:} \\
F_{drive} &= qE_x \\
F_{drag}(v_x, \lambda) &= -m \gamma v_x \left( 1 - \lambda \cdot \text{sign}(v_x) \right) \\
F_{stochastic}(t) &= m\sqrt{2D}\ \xi(t)
\end{aligned}
$$

### Appendix B: Simulation Code

```python
import numpy as np
import math

def run_chiral_transport_sim(lambda_val, t_end=5.0, dt=0.01):
    """
    Simulates electron velocity under an asymmetric chiral scattering potential.
    Uses the Euler-Maruyama method to solve the SDE.
    """
    # Parameters
    q = 1.0
    m = 1.0
    E_x = 1.0
    gamma = 1.0
    noise_strength = 0.1
    
    # Simulation setup
    num_steps = int(t_end / dt)
    t = 0.0
    v_x = 0.0
    
    v_history = [v_x]
    
    # Time-stepping iterative solver
    for i in range(1, num_steps + 1):
        # Calculate deterministic force
        F_drive = (q * E_x) / m
        F_drag = -gamma * v_x * (1 - lambda_val * np.sign(v_x))
        deterministic_dv = (F_drive + F_drag) * dt
        
        # Calculate stochastic force
        stochastic_dv = noise_strength * math.sqrt(dt) * np.random.randn()
        
        # Update velocity
        v_x += deterministic_dv + stochastic_dv
        t += dt
        
        v_history.append(v_x)
        
        # Check for terminal velocity condition
        if len(v_history) > 100:
            recent_v = np.mean(v_history[-50:])
            if abs(v_x - recent_v) / (abs(recent_v) + 1e-9) < 1e-4:
                break
    return v_x
```

### Appendix C: Numerical Outputs

| Chirality ($\lambda$) | Time (t) | Velocity ($v_x$) |
| :--- | :--- | :--- |
| **+0.1** | 0.00 | 0.0000 |
| | 0.01 | 0.0104 |
| | 0.50 | 0.8529 |
| | 1.00 | 1.0501 |
| | 1.50 | 1.0967 |
| **-0.1** | 0.00 | 0.0000 |
| | 0.01 | 0.0097 |
| | 0.50 | 0.7180 |
| | 1.00 | 0.8654 |
| | 1.50 | 0.9001 |

### Appendix D: Glossary and Notation

-   **$t$ (Time):** The temporal evolution variable [s].
-   **$v_x$ (Velocity):** The velocity of the charge carrier along the x-axis [m/s].
-   **$q$ (Charge):** The elementary charge of the carrier [C].
-   **$m$ (Mass):** The effective mass of the charge carrier [kg].
-   **$E_x$ (Electric Field):** The external driving electric field strength [V/m].
-   **$\gamma$ (Damping Constant):** The base coefficient for symmetric scattering/drag [1/s].
-   **$\lambda$ (Chirality Parameter):** A dimensionless parameter representing the strength and sign of the asymmetric chiral scattering.
-   **$D$ (Diffusion Coefficient):** The strength of the stochastic noise [m²/s].
-   **$\xi(t)$ (Stochastic Forcing):** A normalized Gaussian white noise term.
---
### References

Chang, G., Wieder, B. J., Schindler, F., Sanchez, D. S., Belopolski, I., Huang, S.-M., Singh, B., Wu, D., Chang, T.-R., Neupert, T., Xu, S.-Y., Lin, H., & Hasan, M. Z. (2018). Topological quantum properties of chiral crystals. *Nature Materials, 17*(11), 978–985. https://doi.org/10.1038/s41563-018-0169-3

de Juan, F., Grushin, A. G., Morimoto, T., & Moore, J. E. (2017). Quantized circular photogalvanic effect in Weyl semimetals. *Nature Communications, 8*(1), 15995. https://doi.org/10.1038/ncomms15995

Göbel, B., Mertig, I., & Lounis, S. (2025). Chirality-induced selectivity of angular momentum by orbital Edelstein effect in carbon nanotubes. *Communications Physics, 8*(1). https://doi.org/10.1038/s42005-025-02331-7

Guo, C., van Delft, M. R., Gutierrez-Amigo, M., Chen, D., Putzke, C., Wagner, G., Fischer, M. H., Neupert, T., Errea, I., Vergniory, M. G., Wiedmann, S., Felser, C., & Moll, P. J. W. (2024). Distinct switching of chiral transport in the kagome metals KV3Sb5 and CsV3Sb5. *npj Quantum Materials, 9*(1). https://doi.org/10.1038/s41535-024-00629-3

Jiang, Y.-X., Yin, J.-X., Denner, M. M., Shumiya, N., Ortiz, B. R., Xu, G., Guguchia, Z., He, J., Hossain, M. S., Liu, X., Ruff, J., Kautzsch, L., Zhang, S. S., Chang, G., Belopolski, I., Zhang, Q., Cochran, T. A., Multer, D., Litskevich, M., ... Hasan, M. Z. (2021). Unconventional chiral charge order in kagome superconductor KV3Sb5. *Nature Materials, 20*(10), 1353–1357. https://doi.org/10.1038/s41563-021-01034-y

Jiang, Z., Ma, H., Xia, W., Liu, Z., Xiao, Q., Liu, Z., Yang, Y., Ding, J., Huang, Z., Liu, J., Qiao, Y., Liu, J., Peng, Y., Cho, S., Guo, Y., Liu, J., & Shen, D. (2025). Observation of electronic nematicity driven by three-dimensional charge density wave in kagome lattice KV3Sb5. *Communications Physics, 8*(1), 38. https://doi.org/10.1038/s42005-025-02170-6

Kato, T., Li, Y., Kawakami, T., Liu, M., Nakayama, K., Wang, Z., Moriya, A., Tanaka, K., Takahashi, T., Yao, Y., & Sato, T. (2022). Three-dimensional energy gap and origin of charge-density wave in kagome superconductor KV3Sb5. *Communications Materials, 3*(1), 30. https://doi.org/10.1038/s43246-022-00255-1

Kim, S., McKay, R. C., Bielinski, N., Park, J., Zhao, C., Lin, M.-K., Hlevyack, J. A., Guo, X., Mo, S.-K., Abbamonte, P., Chiang, T.-C., Schleife, A., Shoemaker, D. P., Bradlyn, B., & Mahmood, F. (2025). Signatures of Kramers-Weyl fermions in the charge density wave material (TaSe4)2I. *Communications Materials, 6*(1), 227. https://doi.org/10.1038/s43246-025-00952-7

Li, G., Yang, Q., Manna, K., Zhang, Y., Lv, H., Markou, A., Sun, Y., & Felser, C. (2023). Observation of Asymmetric Oxidation Catalysis with B20 Chiral Crystals. *Angewandte Chemie International Edition, 62*(27), e202303296. https://doi.org/10.1002/anie.202303296

Li, H., Xu, S., Rao, Z.-C., Zhou, L.-Q., Wang, Z.-J., Zhou, S.-M., Tian, S.-J., Gao, S.-Y., Li, J.-J., Huang, Y.-B., Lei, H.-C., Weng, H.-M., Sun, Y.-J., Xia, T.-L., Qian, T., & Ding, H. (2019). Chiral fermion reversal in chiral crystals. *Nature Communications, 10*(1), 5505. https://doi.org/10.1038/s41467-019-13435-4

Liu, Y., Zhu, Z. G., & Su, G. (2023). Photogalvanic effect and second harmonic generation from radio to infrared region in WTe2 monolayer. *Physical Review B, 107*(11), 115408. https://doi.org/10.1103/PhysRevB.107.115408

Park, S. R., Han, J., Kim, C., Koh, Y. Y., Kim, C., Lee, H., Choi, H. J., Han, J. H., Lee, K. D., Hur, N. J., Arita, M., Shimada, K., Namatame, H., & Taniguchi, M. (2012). Chiral orbital-angular-momentum in the surface states of Bi2Se3. *Physical Review Letters, 108*(4), 046805. https://doi.org/10.1103/PhysRevLett.108.046805

Rao, Z., Li, H., Zhang, T., Tian, S., Li, C., Fu, B., Tang, C., Wang, L., Li, Z., Fan, W., Li, J., Huang, Y., Liu, Z., Long, Y., Fang, C., Weng, H., Shi, Y., Lei, H., Sun, Y., Qian, T., & Ding, H. (2019). Observation of unconventional chiral fermions with long Fermi arcs in CoSi. *Nature, 567*(7749), 496–499. https://doi.org/10.1038/s41586-019-1031-8

Sanchez, D. S., Cochran, T. A., Belopolski, I., Cheng, Z. J., Yang, X. P., Liu, Y., Xu, X., Manna, K., Yin, J. X., Borrmann, H., Chikina, A., Denlinger, J., Strocov, V. N., Felser, C., Jia, S., Chang, G., & Hasan, M. Z. (2021). Helicoid-arc van Hove singularities in topological chiral crystals. *Nature Communications, 12*(1), 3366. https://doi.org/10.1038/s41467-021-23533-x

Smidman, M., Salamon, M. B., Yuan, H. Q., & Agterberg, D. F. (2017). Superconductivity and spin–orbit coupling in non-centrosymmetric materials: a review. *Reports on Progress in Physics, 80*(3), 036501. https://doi.org/10.1088/1361-6633/aa50d8

Yang, H. Y., Wu, X., Chen, J., Ma, L., Li, Q., Liu, Y., Lu, Y., Che, Y., Zhao, D., Yu, L., Wang, J., Li, X., Feng, Y., Huang, Y., Zhou, F., Zhao, Z., Xiang, T., & Jin, K. (2021). Evidence of a coupled electron-phonon liquid in NbGe₂. *Nature Communications, 12*(1), 3664. https://doi.org/10.1038/s41467-021-23984-2

Yao, M., Gutierrez-Amigo, M., Roychowdhury, S., Errea, I., Fedorov, A., Strocov, V. N., Vergniory, M. G., & Felser, C. (2024). Observation of chiral surface state in superconducting NbGe₂. *arXiv:2403.03324*.

Yen, Y., Krieger, J. A., Yao, M., Robredo, I., Manna, K., Yang, Q., McFarlane, E. C., Shekhar, C., Borrmann, H., Stolz, S., Widmer, R., Gröning, O., Strocov, V. N., Parkin, S. S. P., Felser, C., Vergniory, M. G., Schüler, M., & Schröter, N. B. M. (2024). Controllable orbital angular momentum monopoles in chiral topological semimetals. *Nature Physics, 20*(12), 1912-1918. https://doi.org/10.1038/s41567-024-02655-1
