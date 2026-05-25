---
author: Rowan Brad Quni
email: rowan.quni@qnfo.org
website: http://qnfo.org
ORCID: 0009-0002-4317-5604
ISNI: 0000000526456062
robots: By accessing this content, you agree to https://qnfo.org/LICENSE. Non-commercial use only. Attribution required.
DC.rights: https://qnfo.org/LICENSE. Users are bound by terms upon access.
modified: 2025-10-06T13:07:36Z
title: Substrate-Integrated Computation
aliases:
  - Substrate-Integrated Computation
---

# Substrate-Integrated Computation 
## A Paradigm Shift from Abstract Logic to Geometric Resonance

**Author:** Rowan Brad Quni-Gudzinas
**Affiliation:** QNFO
**Contact:** rowan.quni@qnfo.org
**ORCID:** 0009-0002-4317-5604
**ISNI:** 0000 0005 2645 6062
**DOI:** 10.5281/zenodo.17278401
**Publication Date:** 2025-10-06
**Version:** 1.0

The dominant computational paradigm, rooted in the substrate-agnostic logic of the Turing machine and the von Neumann architecture, faces a foundational crisis of inefficiency and conceptual limitation. This paper critiques this dissociation of abstract logic from physical reality, which results in the von Neumann bottleneck, the high thermodynamic cost of information suppression, and the representational deficiencies of linear models. As a resolution, we propose a paradigm shift to substrate-integrated computation, where the fundamental unit of information is redefined from the static bit to the dynamic physical cycle. This approach is governed by the principle of computational alignment, which posits that efficiency is maximized when a problem’s structure is made isomorphic to the natural, energy-minimizing dynamics of the physical computing substrate. We present the dual-mode monolithic photonic integrated circuit as a pragmatic architectural embodiment of this paradigm. This architecture integrates a specialized harmonic annealing core for rapid optimization and a universal gate-based computation subsystem on a single, room-temperature, CMOS-compatible platform. By engineering and controlling the geometric resonance of a physical medium, this framework moves beyond programming abstract logic to harvesting the intrinsic computational capabilities of physical systems, reframing computer science as a branch of applied physics.

---

## 1.0 Foundational Critique Of The Substrate-Agnostic Computational Paradigm

### 1.1 The Dissociation Of Abstract Logic From Physical Reality

The dominant digital computing paradigm, rooted in the abstract logic of the Turing machine and the von Neumann architecture (von Neumann, 1945), is predicated on a fundamental dissociation of abstract logic from the physical substrate. This separation, while the source of its universality, forces the natural, dynamic, and continuous behavior of physical systems into a simplified, discrete, and static computational model. This profound misalignment between the computational model and the physical world it inhabits is the origin of deep-seated inefficiencies and performance ceilings that are now becoming critical limitations. The paradigm’s success has been achieved not by working with physics, but by expending enormous energy to suppress it.

#### 1.1.1 The Inefficiency Of The Von Neumann Architecture

The von Neumann architecture, the practical embodiment of the Turing machine, institutionalizes the separation of logic and physical reality, leading to inherent and unavoidable inefficiencies in its operation. By physically separating the components that process data from those that store it, the architecture creates a system perpetually at war with the physical constraints of space and time.

##### 1.1.1.1 The Von Neumann Bottleneck And The Separation Of Processing From Memory

The architecture artificially separates the central processing unit (CPU) from memory, necessitating constant data shuttling over a limited-capacity bus. This physical separation between where data is stored and where it is processed creates the **von Neumann bottleneck**, a fundamental constraint on throughput that is determined by the physical limitations of the interconnects—their bandwidth and latency—rather than the raw computational power of the processor itself. For data-intensive workloads, the time and energy spent moving data can dwarf the time and energy spent on the actual computation, rendering the processor’s speed increasingly irrelevant.

##### 1.1.1.2 The Memory Wall And The Latency Cost Of Data Shuttling

The physical separation of processing and memory gives rise to a critical performance limitation known as the **memory wall**, a term defined as the growing disparity between the rapid increase in processor speed and the much slower improvement in memory access times (Wulf & McKee, 1995). Historically, while processor performance improved at a rate of over 50% annually, the latency of Dynamic Random-Access Memory (DRAM) improved by less than 10% per year (Hennessy & Patterson, 2012). This divergence creates a severe performance bottleneck; a processor capable of executing billions of instructions per second is forced to spend a significant and increasing fraction of its operational time in a stalled state, idly waiting for data to be fetched from main memory. Complex and energy-intensive architectural patches, such as multi-level cache hierarchies and speculative prefetching algorithms, have been developed to mitigate this, but they do not solve the underlying problem. These processor stall cycles represent a fundamental opportunity cost, where the computational potential of the hardware is wasted due to the latency inherent in shuttling data across the physical distance separating the processor and memory. Consequently, the memory wall is not merely an inconvenience but a fundamental architectural constraint that severely limits the real-world performance of any system built on the von Neumann model, negating many of the gains achieved through faster processors.

#### 1.1.2 The Thermodynamic Cost Of Information Suppression

Digital computing relies on a strategy of information suppression: the act of expending energy to force a complex analog system into a simplified, discrete state to achieve reliability and control. This entire strategy is profoundly energy-intensive, as it requires constantly fighting against the natural tendencies of the physical medium and the second law of thermodynamics.

##### 1.1.2.1 Forcing Continuous Physical Systems Into Discrete Binary States

A transistor, the fundamental building block of a digital computer, is a complex physical device with a continuous range of electrical behaviors, described by its current-voltage (I-V) characteristic curve. The digital paradigm achieves reliability by expending significant energy to force this complex analog system into just two discrete, stable regions of operation (cutoff or saturation), representing a binary ‘0’ or ‘1’. All the intermediate, analog information about the transistor’s state is treated as noise and actively discarded, a process that requires constant power to maintain the artificial binary states.

##### 1.1.2.2 Energy Expenditure For External Error Correction Mechanisms

To maintain the integrity of these artificial discrete states against inherent physical noise (e.g., thermal fluctuations, quantum tunneling, cosmic rays), digital systems rely on sophisticated error correction codes (ECC). These codes add redundancy to the data—extra bits that do not carry new information but are used to detect and correct errors in the primary data bits. This adds significant overhead, increasing the amount of data that must be stored and transmitted, and requiring additional computational cycles for encoding and decoding. This entire apparatus represents a further thermodynamic cost, an energy tax paid to maintain the illusion of a perfect, noiseless logical state on top of an imperfect, noisy physical substrate.

### 1.2 The Representational Deficiencies Of Linear And Periodic Models

The mathematical tools underlying the digital paradigm, namely the linear number line and periodic signal analysis, introduce their own set of limitations by failing to capture the geometric richness of the physical world. They are, in effect, low-dimensional projections of a higher-dimensional reality.

#### 1.2.1 Projection Artifacts Of The Linear Number Line

The standard representation of numbers on a linear Euclidean axis is a source of projection artifacts—illusions of complexity or randomness that arise when a higher-dimensional, structured reality is forced onto a lower-dimensional, inadequate representation.

##### 1.2.1.1 The Discarding Of Rotational And Phase Information

The linear number line inherently discards rotational information and phase relationships that are critical to modeling complex systems and multiplicative structures. A complex number, for instance, has both a magnitude and a phase (an angle), but a real number line can only represent the magnitude. The apparent randomness of prime number distribution is a classic artifact of this linear projection; when plotted on a spiral, their hidden geometric order becomes evident (Gardner, 1964).

##### 1.2.1.2 The Inability To Natively Represent Non-Orientable Geometries

The linear model is fundamentally incapable of natively representing non-orientable geometries. A key physical example is the quantum mechanical spin of a fermion (e.g., an electron), whose quantum state requires a 720-degree ($4\pi$) rotation to return to its original state. This topological property cannot be naturally described by a linear, orientable framework and must be treated as an ad-hoc rule.

#### 1.2.2 Artificial Constraints Of Periodic Signal Modulation

Periodic signal modulation frameworks, the standard in digital communications, compound these limitations through implicit assumptions that constrain both theoretical capacity and practical security.

##### 1.2.2.1 The Spectral Efficiency Ceiling Imposed By Fourier Analysis

The celebrated Shannon-Hartley channel capacity theorem (Shannon, 1948) rests on a foundation of periodicity embedded in its reliance on Fourier analysis, which decomposes any signal into a sum of periodic sinusoids. This mathematical tool implicitly assumes that signals are periodic, creating an artificial spectral efficiency ceiling that persists across all conventional modulation schemes (QAM, PSK, OFDM). The Nyquist sampling theorem, which dictates the minimum sampling rate for a bandlimited signal, is a direct consequence of this periodic assumption, not an immutable physical law.

##### 1.2.2.2 The Vulnerability Of Security Based On Computational Hardness

Cryptographic security in the digital paradigm traditionally depends on the computational hardness of certain mathematical problems, like integer factorization (the basis of RSA) and the discrete logarithm problem. These problems are difficult precisely because of the properties of cyclic groups and modular arithmetic—mathematical structures with inherent periodicity. Advances in quantum computing, particularly Shor’s algorithm which uses the Quantum Fourier Transform to efficiently find the period of a function (Shor, 1994), threaten to render these security models obsolete. This reveals that conventional security is contingent on the limitations of current computing technology, not on fundamental physical principles.

## 2.0 The Paradigm Of Substrate-Integrated Computation

The resolution to the foundational crisis of the substrate-agnostic paradigm lies in a fundamental shift toward **substrate-integrated computation**, where computation is understood and engineered as a harvested physical process, deeply intertwined with the properties of the physical medium itself.

### 2.1 The Redefinition Of The Computational Primitive

This paradigm shift begins by redefining the fundamental unit of information from a dimensionless abstraction to a dynamic, physical entity.

#### 2.1.1 The Static, Abstract Bit As The Legacy Primitive

The bit is a dimensionless, two-state abstraction representing a choice between ‘0’ and ‘1’. Its very abstraction from the underlying physics is the source of the foundational crisis, necessitating the energy-intensive suppression of the medium’s natural behavior.

#### 2.1.2 The Dynamic, Physical Cycle As The Foundational Primitive

The proposed foundational primitive is the **cycle**, a physical oscillation with continuous degrees of freedom such as rate (frequency), magnitude (amplitude), and relative position (phase). The cycle is the native language of physical systems, from the vibration of atoms to the propagation of light, and its properties can encode information with far greater richness and physical fidelity than a simple binary state.

### 2.2 The Principle Of Computational Alignment

This new ontology gives rise to the **principle of computational alignment**: computational efficiency is maximized when the structure of a problem is made isomorphic to the natural, energy-minimizing dynamics of the physical computing substrate.

#### 2.2.1 Computation As A Harvested Physical Process

This principle mandates a shift in perspective from viewing computation as an imposed logical process to seeing it as a harvested physical process, treating computation as a cultivated natural resource.

##### 2.2.1.1 Shifting From Imposed Logic To The Natural Evolution Of A Medium

Instead of executing long sequences of simple, universal instructions on a passive substrate, this paradigm seeks to identify or engineer physical systems whose natural evolution intrinsically solves the problem of interest. The focus shifts from programming the logic to engineering the physics of the computational medium.

##### 2.2.1.2 Engineering The Substrate Versus Programming The Logic

The goal is to prepare a system in a specific initial state and then observe its natural evolution toward a final state that represents the solution. This changes the role of the engineer from a micromanager of logical steps to a cultivator who prepares an environment that produces a solution, guiding the system’s natural tendencies rather than fighting against them.

#### 2.2.2 Isomorphism Between Problem Structure And Substrate Dynamics

Efficiency is achieved by finding or creating a high degree of isomorphism (structural similarity) between the problem to be solved and the natural dynamics of the substrate.

##### 2.2.2.1 Mapping Optimization Problems To Energy Minimization Dynamics

Complex optimization problems, which involve finding the minimum value in a vast landscape of possibilities, can be solved with extreme efficiency by mapping them onto physical systems (such as a network of coupled oscillators or a quantum annealer) that naturally seek and settle into their lowest energy state. The problem’s cost function is directly translated into the system’s physical energy function (its Hamiltonian).

##### 2.2.2.2 Mapping Harmonic Problems To Resonant Substrates

Problems with an inherent harmonic or periodic structure, such as integer factorization, could be efficiently solved by mapping them onto resonant physical substrates, where the system’s natural resonance frequencies correspond to the problem’s solutions. This transforms a difficult arithmetic problem into a physical measurement task.

### 2.3 The Unifying Role Of Geometric Constraints

The language that connects abstract problems to physical dynamics is geometry. Specific geometric configurations act as boundary conditions that constrain the behavior of physical fields and waves, defining the “rules” of computation for that substrate.

#### 2.3.1 The Torus As A Boundary Condition Defining The Computational Landscape

A toroidal (donut-shaped) geometry is a powerful example of such a constraint. It is a finite, continuous geometry without edges, which imposes natural periodic boundary conditions on any wave or field confined within it. This creates a predictable computational landscape.

##### 2.3.1.1 Stable Resonant Modes As Constructive Interference Loci

The geometry allows certain wave patterns to persist by interfering constructively with themselves as they propagate. These stable, discrete, and predictable resonant modes act as natural, robust states for encoding information—stable computational loci that are inherently resilient to perturbation.

##### 2.3.1.2 Unstable Nodes As Destructive Interference Loci

Conversely, the geometry also defines specific locations or configurations where waves interfere destructively, leading to minimal amplitude and suppressed coherence. These unstable nodes are not merely flaws; they are predictable features of the landscape that can be leveraged for controlled state transitions or as part of an intrinsic error management scheme.

#### 2.3.2 The Spiral As The Natural Trajectory Of Resonant Evolution

Within the landscape defined by the torus, the natural, energy-minimizing path of a resonant mode is often a spiral or helical trajectory. This path represents the motion that simultaneously satisfies the dual periodicities of the torus: winding around its minor radius (the “tube”) and its major radius (the “ring”).

##### 2.3.2.1 Helical Paths Within A Toroidal Medium

A resonant mode propagating within a toroidal medium, such as a confined electromagnetic wave or the gyration of a skyrmion core, naturally follows a helical path. The specific pitch of this helix is determined by the ratio of the resonant frequencies associated with the two circular dimensions of the torus.

##### 2.3.2.2 Non-Periodic Waveforms Based On Number-Theoretic Geometries

The mathematics of these spiral trajectories connects directly to number theory via the logarithmic spiral. This allows for the generation of complex, aperiodic (non-repeating) waveforms whose structure is based on the geometric distribution of prime numbers. Such waveforms can carry more information than simple periodic signals and form the basis for novel forms of secure communication and physical computation.

## 3.0 Architectural Embodiment: The Dual-Mode Monolithic Photonic Circuit

The principles of substrate-integrated computation find a pragmatic and powerful architectural embodiment in the form of a dual-mode quantum computing processor built on a single, monolithic **photonic integrated circuit (PIC)**. This architecture directly addresses the key challenges of scalability, cost, and operating conditions that have hindered prior art in quantum computing.

### 3.1 The Unifying Physical Substrate: A CMOS-Compatible Photonic Integrated Circuit (PIC)

The physical foundation of the architecture is a silicon photonics chip, fabricated using established, scalable, and cost-effective CMOS-compatible processes. This choice of substrate is the key enabler for manufacturability and practical deployment, leveraging decades of investment in the semiconductor industry.

#### 3.1.1 Operation At Or Near Room Temperature

A primary advantage of the photonic platform is its ability to support quantum coherent operations at or near room temperature. Photons are relatively immune to thermal decoherence compared to matter-based qubits. This eliminates the need for the massive, complex, and power-intensive dilution refrigerators required by superconducting quantum computers, drastically reducing operating costs and improving environmental stability.

#### 3.1.2 Monolithic Integration Of Specialized Co-Processors

The architecture’s core innovation is the monolithic co-fabrication of two distinct but physically related quantum processing cores on a single chip. This approach replaces the pursuit of a single, compromised universal architecture with a practical, high-performance system of specialized co-processors that addresses the generality versus specialization dilemma.

### 3.2 Core I: The Harmonic Annealing Core (HAC) For Specialized Optimization

The first core is a highly specialized analog computer, a type of **Coherent Ising Machine** (McMahon et al., 2016), designed for rapidly solving complex combinatorial optimization problems.

#### 3.2.1 Operational Principle: Physical Annealing Via An Ising Model

This core works by physically simulating an **Ising model** (Ising, 1925), a concept from physics describing a network of interacting spins. Many difficult optimization problems can be mathematically translated into the problem of finding the lowest-energy state of such a model.

##### 3.2.1.1 Mapping Combinatorial Optimization To A QUBO Formulation

The user’s optimization problem is first translated into a standard mathematical format known as a **Quadratic Unconstrained Binary Optimization (QUBO)** problem. This formulation is mathematically equivalent to an Ising model, providing a direct bridge from the abstract problem to the physical hardware (Lucas, 2014).

##### 3.2.1.2 Collective Evolution Of Oscillators To A Global Energy Minimum

The core physically embodies the QUBO problem and, when activated, the entire system of coupled oscillators rapidly and collectively evolves, physically settling into the configuration with the lowest possible total energy. This process is a form of analog computation that happens in nanoseconds, finding the optimal solution through a natural physical process.

#### 3.2.2 Physical Implementation: Coupled Optical Parametric Oscillators (OPOs)

The physical realization of the Ising model is achieved using an array of thousands of coupled optical oscillators integrated onto the photonic chip.

##### 3.2.2.1 OPO Phase States (0 or π) As Quantum Harmonic Bits

Instead of magnetic spins, the chip uses **Optical Parametric Oscillators (OPOs)**, which are tiny optical resonators. When driven by a laser, a non-linear optical effect causes each OPO to naturally settle into one of two stable phases of light (0 or $\pi$). These two phases directly and robustly correspond to the +1 and -1 states of a spin.

##### 3.2.2.2 Programmable Coupling Matrix As The Physical Hamiltonian

The mathematical problem (the QUBO matrix) is physically programmed into the chip by configuring a mesh of optical waveguides, tunable couplers, and phase shifters. The classical controller applies a set of analog voltages to these components, which precisely sets the interaction strengths between any two OPOs. This programmable matrix physically implements the problem’s energy landscape (its Hamiltonian).

### 3.3 Core II: The Universal Gate Computation Subsystem (UGCS) For Universal Algorithms

The second core is a Turing-complete, gate-based quantum computer, capable of executing any quantum algorithm, such as those for quantum chemistry simulation or factoring.

#### 3.3.1 Operational Principle: Measurement-Based Quantum Computing (MBQC)

This core operates on the principle of **Measurement-Based Quantum Computing (MBQC)**, which differs from the more common circuit-based model (Raussendorf & Briegel, 2001). Instead of applying a sequence of gates to an initial state, computation is performed by making a series of measurements on a pre-prepared, highly entangled resource state.

##### 3.3.1.1 The Cluster State As A Universal Entangled Resource

A dedicated on-chip resource continuously generates a large, two-dimensional, highly entangled state of thousands of photons, known as a “cluster state.” This state is a universal computational resource; any quantum algorithm can be implemented on it. It serves as a blank, entangled slate upon which the computation is performed.

##### 3.3.1.2 Computation Via Sequential, Adaptive Single-Qubit Measurements

The algorithm is implemented on this resource by performing a sequence of single-qubit measurements. Crucially, the basis (the angle or type) of each measurement depends on the classical outcome of the previous measurements. This requires an extremely fast classical feedback loop to guide the computation through the entangled resource.

#### 3.3.2 Physical Implementation: Cluster State Generation And Measurement

The MBQC principle is realized using integrated photonic components for generating and measuring the entangled photon state.

##### 3.3.2.1 Spontaneous Four-Wave Mixing For Entangled Photon Generation

The cluster state is generated using a physical process called **spontaneous four-wave mixing (SFWM)** in a plurality of silicon nitride micro-rings. This is a well-established non-linear optical technique that can be efficiently implemented on a photonic chip to produce entangled photon pairs.

##### 3.3.2.2 Adaptive Measurement Array With High-Speed Feed-Forward

The computation is performed by an array of high-speed single-photon detectors (such as superconducting nanowire detectors or avalanche photodiodes) and fast electro-optic modulators. The classical controller executes the measure-and-guide cycle with a latency of less than 10 nanoseconds, a critical performance metric that determines the depth and complexity of the quantum algorithms that can be run.

### 3.4 The Classical Control And Interface Layer (CCIL)

The entire dual-mode quantum processor is managed by a powerful, high-speed classical digital controller (such as an FPGA or ASIC) that serves as the central controller of the system.

#### 3.4.1 Function As A High-Speed Compiler And Router

The classical controller is responsible for receiving problems from a user, analyzing their structure, and dispatching them to the appropriate quantum core.

##### 3.4.1.1 Problem Analysis And Core Selection

The controller evaluates the mathematical structure of a submitted problem and selects the most efficient operational mode: the harmonic annealing core for optimization, the universal gate computation subsystem for algorithms, or a hybrid approach that uses both.

##### 3.4.1.2 Translation Of Problems Into Low-Level Physical Control Signals

The controller compiles the high-level problem description into the precise set of analog voltage settings (for the HAC) or the sequence of measurement bases and feed-forward logic map (for the UGCS) required to physically control the chip.

#### 3.4.2 Orchestration Of Hybrid Computational Workflows

For complex, multi-stage problems, the classical controller orchestrates a synergistic workflow that leverages both quantum cores, making the platform more powerful than the sum of its parts.

##### 3.4.2.1 Seeding The UGCS With Solutions From The HAC

The controller can first use the HAC to find a rapid, high-quality approximate solution to an optimization sub-problem. This classical result is then used to inform or initialize a more precise, refined calculation on the universal gate subsystem, significantly reducing the search space for the more computationally expensive universal algorithm.

##### 3.4.2.2 Management Of The Classical-Quantum Feedback Loop

The controller manages all real-time feedback loops, including the high-speed adaptive measurements for the UGCS and the continuous self-calibration of all optical components on the chip to compensate for thermal drift and ensure stable, high-fidelity operation over time.

## 4.0 Methodological Framework: Substrate Programming And Hamiltonian Engineering

The architecture’s design suggests a novel methodological framework for quantum computing: **substrate programming** or **Hamiltonian engineering**. This approach moves beyond writing software for a fixed, universal hardware architecture and instead focuses on configuring a physical substrate to make its natural dynamics solve a problem.

### 4.1 Stage I: Problem-To-Hamiltonian Compilation

The first stage involves translating an abstract computational problem into the language of physics.

#### 4.1.1 Mapping Problem Variables To Physical Interaction Strengths

The variables and constraints of the problem are mapped onto the physical interaction strengths of the chosen substrate. For the harmonic annealing core, this means translating the QUBO matrix into the coupling strengths between the optical oscillators, which are set by applying voltages to the programmable coupling matrix.

#### 4.1.2 Defining The Energy Landscape Of The Physical Substrate

This mapping effectively defines the energy landscape (the Hamiltonian) of the physical system. The geometry of this landscape is engineered such that its lowest point (the ground state) corresponds to the solution of the original computational problem.

### 4.2 Stage II: Substrate Initialization And Physical Evolution

The second stage is the execution of the computation through physical evolution.

#### 4.2.1 Preparation Of The System In A Defined Initial State

The physical system is prepared in a specific initial state. For the annealer, this involves setting the programmable coupling matrix before activation. For the universal computer, this involves the continuous generation of the cluster state resource.

#### 4.2.2 Allowing The System To Spontaneously Evolve To Its Ground State

The system is then activated (e.g., by an optical pump) and allowed to evolve naturally according to the laws of physics. This physical annealing or in-transit evolution is the core computational step, where the system spontaneously seeks its ground state or a stable configuration that represents the solution.

### 4.3 Stage III: Coherence And State Management

During evolution, the system’s quantum coherence must be managed to ensure the integrity of the computation. This framework proposes moving beyond simple error suppression to active state management.

#### 4.3.1 Stroboscopic Coherence Stabilization

This technique is used to perform computations that require longer evolution times than the natural coherence time of the system allows.

##### 4.3.1.1 Iterative Evolve-Measure-Correct Cycles

The computation is broken down into a series of short, coherent evolution steps. After each step, the partially evolved state is measured, a correction is calculated by the classical controller based on a comparison to an ideal model, and a corrected state is re-injected for the next interval.

##### 4.3.1.2 Synthesis Of Long Computations From Short, Coherent Intervals

This iterative cycle effectively synthesizes one long, stable computation from many short, decoherence-limited ones, enabling the solution of more complex problems by actively managing the accumulation of errors.

#### 4.3.2 Holographic Calibration For Robust Readout

This technique ensures that the final state of the system can be measured with high fidelity, even in the presence of noise and hardware imperfections.

##### 4.3.2.1 Concurrent Transmission Of A Known Reference Field

A known, stable reference field (or signal) is transmitted or generated concurrently with the computational state. This reference acts as a physical yardstick against which the computational state can be measured.

##### 4.3.2.2 Real-Time Self-Calibration To Compensate For Noise And Drift

The receiver uses the reference field to dynamically self-calibrate its measurement process in real-time. By comparing the received reference to its known ideal form, the system can calculate and correct for any distortions introduced by the channel or the receiver hardware, effectively correcting for distortions in the raw data.

### 4.4 Stage IV: Final State Readout And Interpretation

The final stage involves extracting the result of the physical computation.

#### 4.4.1 Measurement Of The System’s Final Physical State

The final, stable physical state of the system (e.g., the phase configuration of the optical oscillators, the final state of a propagated radio wave, or the sequence of classical outcomes from the MBQC process) is measured using high-fidelity detectors.

#### 4.4.2 Translation Of The Physical State Into A Classical Solution

The measured physical state is then translated back into a classical, symbolic solution that represents the answer to the user’s original problem. This is performed by the classical control layer.

## 5.0 Foundational Challenges And Future Trajectories

While the substrate-integrated paradigm offers a compelling path forward, it faces several foundational challenges that define the future trajectories of research and development.

### 5.1 The Generality Versus Specialization Dilemma

There is an inherent trade-off between the extreme efficiency of specialized physical solvers and the flexibility of universal computers.

#### 5.1.1 The Impracticality Of A Unique Physical Medium For Every Problem

Fabricating a unique, perfectly aligned physical medium for every individual computational problem is impractical. This suggests that specialized hardware will be targeted at broad, high-value classes of problems (e.g., optimization).

#### 5.1.2 The Requirement For A Dynamically Reconfigurable Medium

The critical gap is the development of a single physical substrate that can be **dynamically reconfigured** in real-time to perform both specialized annealing and universal computation. This would require real-time control over the medium’s effective geometry and non-linear properties, creating a truly universal resonant processor.

### 5.2 The Quantum Versus Classical Advantage Question

A significant challenge is rigorously proving that these systems offer a true quantum advantage over the best possible classical counterparts.

#### 5.2.1 Differentiating True Quantum Speedup From Sophisticated Analog Computation

The collective evolution of coupled oscillators in the harmonic annealer, for example, can often be described by semi-classical physics. It is a major experimental challenge to demonstrate that quantum effects, such as entanglement between the oscillators during their evolution, are essential to its computational performance and provide a genuine speedup over classical analog devices.

#### 5.2.2 The Experimental Challenge Of Proving Quantum Advantage

Rigorously benchmarking these new architectures against state-of-the-art classical algorithms running on specialized classical hardware (like GPUs and TPUs) is a complex but necessary step to validate any claims of quantum advantage.

### 5.3 The Interpretive Overhead Paradox

All substrate-integrated systems require a powerful classical controller to perform problem compilation, system control, and solution readout.

#### 5.3.1 The Energy And Latency Cost Of The Classical Control Layer

The energy and latency costs of this classical control infrastructure could potentially negate the efficiency gains of the physical computation itself. The performance of the classical-quantum interface is as critical as the performance of the quantum core.

#### 5.3.2 The Net Gain Condition For Physical Computation

The viability of this paradigm depends on the **net gain condition**: the energy and time saved by leveraging the substrate’s dynamics must significantly exceed the overhead of the classical control layer. This defines the class of problems for which this approach is truly advantageous.

## 6.0 Conclusion: The Thesis Of A Hybrid, Substrate-Integrated Architecture

The synthesis of these concepts leads to a powerful and coherent thesis regarding the future of high-performance computing. The path forward lies not in a single, universal architecture, but in a hybrid, substrate-integrated paradigm that leverages the right computational tool for the right job.

### 6.1 The Pragmatism Of A Dual-Protocol System-On-Chip

The most pragmatic and scalable path to practical quantum advantage is a **dual-protocol, hybrid quantum system-on-chip** that provides both specialized and universal computational capabilities on a single, manufacturable platform.

#### 6.1.1 Integrating Specialized And Universal Cores

By integrating a specialized harmonic annealing core for rapid optimization alongside a universal gate computation subsystem for universal algorithms, the architecture addresses the competing demands of high-speed problem solving and high-fidelity algorithmic execution, resolving the specialization-versus-generality dilemma.

#### 6.1.2 Leveraging A Manufacturable, Room-Temperature Photonic Platform

The use of a monolithic photonic platform, compatible with established CMOS fabrication processes and capable of room-temperature operation, provides a practical and economically viable pathway to scaling quantum hardware, directly addressing the primary engineering and cost barriers of competing modalities.

### 6.2 The Shift From Programming Logic To Engineering Physical Dynamics

This architecture represents a fundamental paradigm shift in how we conceive of computation, moving from the realm of abstract logic to that of applied physics.

#### 6.2.1 Computation As The Controlled Evolution Of A Physical System

The computational process is no longer a sequence of instructions but the set of engineered physical constraints, and the execution is the system’s spontaneous physical evolution. This reframes computer science as the science of engineering and controlling the computational properties of matter.

#### 6.2.2 The Future Of Computing As A Branch Of Applied Physics

Ultimately, this paradigm re-contextualizes computer science as a branch of experimental and applied physics. The future of computing will involve discovering new computational phenomena in nature and developing the interfaces required to harness and interpret the universe’s native computational processes.

---
## Appendices

### Appendix A: Formal Derivation of the Equivalence between the Ising Model and the Quadratic Unconstrained Binary Optimization (QUBO) Formulation

#### 1.0 Axioms and Definitions

-   **Definition 1.1 (Ising Model):** The Ising model describes a system of interacting spins. For a set of $N$ spins, the state of the system is given by a vector $s = (s_1, s_2, \dots, s_N)$, where each spin variable $s_i$ can take one of two values, $s_i \in \{-1, 1\}$. The energy of the system, described by the Ising Hamiltonian $H$, is given by:

    $$
    H(s) = - \sum_{i<j} J_{ij} s_i s_j - \sum_{i=1}^{N} h_i s_i
    $$

    where $J_{ij}$ is the coupling strength between spin $i$ and spin $j$, and $h_i$ is an external magnetic field acting on spin $i$. Finding the ground state of the Ising model is equivalent to finding the spin configuration $s$ that minimizes $H(s)$.

-   **Definition 1.2 (Quadratic Unconstrained Binary Optimization - QUBO):** A QUBO problem is an optimization problem that involves finding the minimum of a quadratic objective function of binary variables. For a set of $N$ binary variables, the state is given by a vector $x = (x_1, x_2, \dots, x_N)$, where each variable $x_i$ can take one of two values, $x_i \in \{0, 1\}$. The objective function to be minimized is:

    $$
    f(x) = \sum_{i \le j} Q_{ij} x_i x_j = x^T Q x
    $$

    where $Q$ is an $N \times N$ matrix of real-valued coefficients. The diagonal terms $Q_{ii}$ represent linear costs (since $x_i^2 = x_i$ for $x_i \in \{0, 1\}$), and the off-diagonal terms $Q_{ij}$ represent quadratic costs.

#### 2.0 Proposition

The problem of finding the ground state of an Ising model is mathematically equivalent to solving a QUBO problem. A direct mapping exists that transforms the Ising Hamiltonian into the QUBO objective function.

#### 3.0 Proof

The proof demonstrates this equivalence by establishing a linear transformation between the spin variables $s_i$ and the binary variables $x_i$, and then substituting this transformation into the Ising Hamiltonian to derive the QUBO form.

-   **Statement 3.1:** Define the transformation between spin variables and binary variables.
    -   **Justification:** A linear mapping is required to connect the set $\{-1, 1\}$ to the set $\{0, 1\}$. The standard transformation is:

        $$
        s_i = 2x_i - 1
        $$

    -   **Verification:**
        -   If $x_i = 1$, then $s_i = 2(1) - 1 = 1$.
        -   If $x_i = 0$, then $s_i = 2(0) - 1 = -1$.
        The transformation correctly maps the domains. The inverse transformation is $x_i = (s_i + 1)/2$.

-   **Statement 3.2:** Substitute the variable transformation from Statement 3.1 into the Ising Hamiltonian (Definition 1.1).
    -   **Justification:** Direct substitution to express the Hamiltonian $H$ in terms of the binary variables $x_i$.
    -   **Result:**

        $$
        H(x) = - \sum_{i<j} J_{ij} (2x_i - 1)(2x_j - 1) - \sum_{i=1}^{N} h_i (2x_i - 1)
        $$

-   **Statement 3.3:** Expand the algebraic terms in the expression for $H(x)$.
    -   **Justification:** Application of the distributive property of multiplication.
    -   **Calculation:**
        -   The interaction term: $(2x_i - 1)(2x_j - 1) = 4x_i x_j - 2x_i - 2x_j + 1$.
        -   The field term: $(2x_i - 1) = 2x_i - 1$.
    -   **Result:**

        $$
        H(x) = - \sum_{i<j} J_{ij} (4x_i x_j - 2x_i - 2x_j + 1) - \sum_{i=1}^{N} h_i (2x_i - 1)
        $$

-   **Statement 3.4:** Distribute the summations and regroup terms by the power of the variables ($x_i x_j$, $x_i$, and constant terms).
    -   **Justification:** Rearranging the expression to match the structure of the QUBO objective function.
    -   **Result:**

        $$
        H(x) = \left( - \sum_{i<j} 4J_{ij} x_i x_j \right)
        $$

        $$
        + \left( \sum_{i<j} 2J_{ij} x_i + \sum_{i<j} 2J_{ij} x_j - \sum_{i=1}^{N} 2h_i x_i \right)
        $$

        $$
        + \left( - \sum_{i<j} J_{ij} + \sum_{i=1}^{N} h_i \right)
        $$

-   **Statement 3.5:** Consolidate the linear terms into a single summation over the index $i$.
    -   **Justification:** The term $\sum_{i<j} 2J_{ij} x_i$ sums over $j>i$ for a fixed $i$. The term $\sum_{i<j} 2J_{ij} x_j$ can be rewritten by swapping indices as $\sum_{j<i} 2J_{ji} x_i$. Assuming symmetric couplings ($J_{ij} = J_{ji}$), the total coefficient for a given $x_i$ from the interaction terms is $\sum_{j \neq i} 2J_{ij}$.
    -   **Calculation:** The complete linear part is:

        $$
        \sum_{i=1}^{N} \left( \sum_{j \neq i} 2J_{ij} - 2h_i \right) x_i
        $$

    -   **Result:** The full Hamiltonian is:

        $$
        H(x) = \sum_{i<j} (-4J_{ij}) x_i x_j
        $$

        $$
        + \sum_{i=1}^{N} \left( \sum_{j \neq i} 2J_{ij} - 2h_i \right) x_i
        $$

        $$
        + \left( \sum_{i=1}^{N} h_i - \sum_{i<j} J_{ij} \right)
        $$

-   **Statement 3.6:** Identify the QUBO matrix $Q$ and the constant offset.
    -   **Justification:** The expression for $H(x)$ from Statement 3.5 is now in the form of a QUBO objective function plus a constant. Minimizing $H(x)$ is equivalent to minimizing $H(x) - \text{Constant}$.
    -   **Identification:**
        -   The quadratic coefficients (off-diagonal) are: $Q_{ij} = -4J_{ij}$ for $i \neq j$.
        -   The linear coefficients (diagonal, since $x_i^2 = x_i$) are: $Q_{ii} = \sum_{j \neq i} 2J_{ij} - 2h_i$.
        -   The constant offset is: $C = \sum_{i=1}^{N} h_i - \sum_{i<j} J_{ij}$.
    -   **Result:** The Ising Hamiltonian can be written as:

        $$
        H(x) = \sum_{i<j} Q_{ij} x_i x_j + \sum_{i=1}^{N} Q_{ii} x_i + C
        $$

        This is the general form of a QUBO problem.

#### 4.0 Conclusion

The derivation demonstrates that the Ising model Hamiltonian $H(s)$ is mathematically equivalent to the Quadratic Unconstrained Binary Optimization (QUBO) objective function $f(x)$. The linear transformation $s_i = 2x_i - 1$ provides a direct mapping between the spin variables $s_i \in \{-1, 1\}$ of the Ising model and the binary variables $x_i \in \{0, 1\}$ of a QUBO problem. The energy function of the Ising model maps to a quadratic polynomial of binary variables, plus a constant offset. As this constant does not affect the location of the minimum, finding the ground state (minimum energy configuration) of the Ising model is formally equivalent to finding the optimal solution to the corresponding QUBO problem. This equivalence is fundamental to the operation of physical systems, such as harmonic annealers, that solve combinatorial optimization problems by finding the ground state of an analogous physical system.

---
### Appendix B: Formal Derivation of the Logarithmic Spiral’s Constant Angle Property

#### 1.0 Axioms and Definitions

-   **Axiom 1.1 (Euclidean Plane):** The 2D Euclidean plane $\mathbb{R}^2$ is equipped with Cartesian coordinates $(x, y)$ and the standard inner product.
-   **Definition 1.1 (Polar Coordinates):** A point in $\mathbb{R}^2$ can be represented by polar coordinates $(r, \theta)$, where $r \geq 0$ is the distance from the origin and $\theta \in [0, 2\pi)$ is the angle from the positive x-axis. The relationship to Cartesian coordinates is $x = r\cos\theta$, $y = r\sin\theta$.
-   **Definition 1.2 (Logarithmic Spiral):** A logarithmic spiral is a curve in polar coordinates defined by the equation:

    $$
    r(\theta) = ae^{b\theta}
    $$

    where $a > 0$ and $b \neq 0$ are real constants.

-   **Definition 1.3 (Position Vector):** For a point on the spiral at angle $\theta$, the position vector is $\vec{r}(\theta) = (x(\theta), y(\theta)) = (ae^{b\theta}\cos\theta, ae^{b\theta}\sin\theta)$.
-   **Definition 1.4 (Tangent Vector):** The tangent vector to the curve at angle $\theta$ is the derivative of the position vector with respect to $\theta$:

    $$
    \vec{T}(\theta) = \frac{d\vec{r}}{d\theta} = \left( \frac{dx}{d\theta}, \frac{dy}{d\theta} \right)
    $$

#### 2.0 Theorem: Constant Angle Property

The angle $\alpha$ between the position vector $\vec{r}(\theta)$ and the tangent vector $\vec{T}(\theta)$ is constant for all $\theta$ along the logarithmic spiral $r(\theta) = ae^{b\theta}$, and is given by $\alpha = \arctan(1/b)$.

#### 3.0 Proof

-   **Statement 3.1:** Calculate the components of the tangent vector $\vec{T}(\theta)$.
    -   **Justification:** Apply the product rule to differentiate $x(\theta) = ae^{b\theta}\cos\theta$ and $y(\theta) = ae^{b\theta}\sin\theta$.
    -   **Calculation:**

        $$
        \frac{dx}{d\theta} = a(be^{b\theta}\cos\theta - e^{b\theta}\sin\theta) = ae^{b\theta}(b\cos\theta - \sin\theta)
        $$

        $$
        \frac{dy}{d\theta} = a(be^{b\theta}\sin\theta + e^{b\theta}\cos\theta) = ae^{b\theta}(b\sin\theta + \cos\theta)
        $$

    -   **Result:** $\vec{T}(\theta) = ae^{b\theta} \left( (b\cos\theta - \sin\theta), (b\sin\theta + \cos\theta) \right)$

-   **Statement 3.2:** Calculate the dot product $\vec{r}(\theta) \cdot \vec{T}(\theta)$.
    -   **Justification:** Use the definition of the dot product in Cartesian coordinates.
    -   **Calculation:**

        $$
        \vec{r}(\theta) \cdot \vec{T}(\theta) = (ae^{b\theta}\cos\theta) \cdot (ae^{b\theta}(b\cos\theta - \sin\theta))
        $$

        $$
        + (ae^{b\theta}\sin\theta) \cdot (ae^{b\theta}(b\sin\theta + \cos\theta))
        $$

        $$
        = a^2e^{2b\theta} \left[ \cos\theta(b\cos\theta - \sin\theta) + \sin\theta(b\sin\theta + \cos\theta) \right]
        $$

        $$
        = a^2e^{2b\theta} \left[ b\cos^2\theta - \cos\theta\sin\theta + b\sin^2\theta + \sin\theta\cos\theta \right]
        $$

        $$
        = a^2e^{2b\theta} \left[ b(\cos^2\theta + \sin^2\theta) \right] = a^2e^{2b\theta} b
        $$

-   **Statement 3.3:** Calculate the magnitude of the position vector $|\vec{r}(\theta)|$.
    -   **Justification:** Use the definition of vector magnitude.
    -   **Calculation:**

        $$
        |\vec{r}(\theta)| = \sqrt{(ae^{b\theta}\cos\theta)^2 + (ae^{b\theta}\sin\theta)^2}
        $$

        $$
        = \sqrt{a^2e^{2b\theta}(\cos^2\theta + \sin^2\theta)} = ae^{b\theta}
        $$

-   **Statement 3.4:** Calculate the magnitude of the tangent vector $|\vec{T}(\theta)|$.
    -   **Justification:** Use the definition of vector magnitude.
    -   **Calculation:**

        $$
        |\vec{T}(\theta)| = ae^{b\theta} \sqrt{(b\cos\theta - \sin\theta)^2 + (b\sin\theta + \cos\theta)^2}
        $$

        $$
        = ae^{b\theta} \sqrt{
            \begin{aligned}
                &b^2\cos^2\theta - 2b\cos\theta\sin\theta + \sin^2\theta \\
                &+ b^2\sin^2\theta + 2b\sin\theta\cos\theta + \cos^2\theta
            \end{aligned}
        }
        $$

        $$
        = ae^{b\theta} \sqrt{b^2(\cos^2\theta + \sin^2\theta) + (\sin^2\theta + \cos^2\theta)}
        $$

        $$
        = ae^{b\theta} \sqrt{b^2 + 1}
        $$

-   **Statement 3.5:** Calculate the cosine of the angle $\alpha$ between $\vec{r}(\theta)$ and $\vec{T}(\theta)$.
    -   **Justification:** Use the formula for the angle between two vectors: $\cos\alpha = \frac{\vec{r} \cdot \vec{T}}{|\vec{r}||\vec{T}|}$.
    -   **Calculation:**

        $$
        \cos\alpha = \frac{\vec{r}(\theta) \cdot \vec{T}(\theta)}{|\vec{r}(\theta)||\vec{T}(\theta)|}
        $$

        $$
        = \frac{a^2e^{2b\theta} b}{(ae^{b\theta})(ae^{b\theta}\sqrt{b^2 + 1})} = \frac{b}{\sqrt{b^2 + 1}}
        $$

-   **Statement 3.6:** Calculate the tangent of the angle $\alpha$.
    -   **Justification:** Use the identity $\tan^2\alpha + 1 = \sec^2\alpha = 1/\cos^2\alpha$.
    -   **Calculation:**

        $$
        \tan^2\alpha = \frac{1}{\cos^2\alpha} - 1 = \frac{b^2 + 1}{b^2} - 1 = \frac{1}{b^2}
        $$

        Therefore, $\tan\alpha = \frac{1}{b}$.

-   **Statement 3.7:** Conclude the proof.
    -   **Justification:** The calculation in Statement 3.6 shows that $\tan\alpha$ is constant, depending only on the parameter $b$ of the spiral and not on the angle $\theta$.
    -   **Result:** The angle $\alpha$ between the position vector and the tangent vector is constant and is given by $\alpha = \arctan(1/b)$. This completes the proof of the theorem.

---
### Appendix C: Formal Derivation of the Golden Angle’s Optimality for Aperiodic Packing

The study of aperiodic packing, particularly in biological systems like the arrangement of seeds in a sunflower head (Vogel, 1979), reveals deep connections to number theory. The optimal arrangement to avoid periodic alignment and fill space most uniformly is achieved using an angle related to the golden ratio.

#### 1.0 Axioms and Definitions

-   **Axiom 1.1 (Circle Geometry):** A circle has a total angle of $2\pi$ radians.
-   **Definition 1.1 (Angular Separation):** In a sequential growth process on a circle, the angular separation $\theta$ is the fixed angle by which the next element is placed relative to the previous one.
-   **Definition 1.2 (Periodic Alignment):** A growth process with angular separation $\theta$ exhibits periodic alignment if placing $n$ elements results in the $n$-th element being close to a starting position after $m$ full rotations. This occurs when the ratio $\frac{\theta}{2\pi}$ is well-approximated by a rational number $\frac{m}{n}$ for small integers $n, m$.
-   **Definition 1.3 (The Golden Ratio, $\phi$):** The golden ratio is the unique positive real number satisfying the equation $\phi = 1 + \frac{1}{\phi}$. Its value is $\phi = \frac{1 + \sqrt{5}}{2} \approx 1.618$.
-   **Definition 1.4 (The Golden Angle, $\theta_g$):** The angle that divides the circumference of a circle into two arcs whose lengths are in the golden ratio. It is given by $\theta_g = \frac{2\pi}{\phi^2}$.
-   **Definition 1.5 (Continued Fraction):** The representation of a real number $x$ as $x = a_0 + \frac{1}{a_1 + \frac{1}{a_2 + \dots}}$, denoted $[a_0; a_1, a_2, \dots]$. The quality of rational approximations is related to the size of the coefficients $a_i$; smaller coefficients lead to slower convergence and poorer approximability.

#### 2.0 Theorem: The Golden Ratio as the Most Irrational Number

The golden ratio $\phi$ has the simplest possible continued fraction representation, $[1; 1, 1, 1, \dots]$, which converges more slowly than that of any other irrational number, making it the “most irrational” number in the sense of Diophantine approximation.

#### 3.0 Proof of Theorem

-   **Statement 3.1:** Start with the defining equation of the golden ratio: $\phi = 1 + \frac{1}{\phi}$.
-   **Statement 3.2:** Substitute the expression for $\phi$ from Statement 3.1 into the denominator on the right-hand side recursively: $\phi = 1 + \cfrac{1}{1 + \cfrac{1}{\phi}}$.
-   **Statement 3.3:** Continue the recursive substitution infinitely to obtain the infinite continued fraction:

    $$
    \phi = 1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{\ddots}}}}
    $$

-   **Statement 3.4:** Express this result in continued fraction notation: $\phi = [1; 1, 1, 1, \dots]$.
-   **Statement 3.5:** The coefficients $a_i$ in the continued fraction for $\phi$ are all 1, which are the smallest possible positive integers.
-   **Statement 3.6:** The rate of convergence of a continued fraction is determined by the size of its coefficients. Smaller coefficients lead to slower convergence and poorer rational approximations.
-   **Statement 3.7:** Since the coefficients for $\phi$ are the smallest possible, its continued fraction converges more slowly than that of any other irrational number. This makes $\phi$ the most difficult number to approximate well with rational numbers, and thus the “most irrational” number.

#### 4.0 Theorem: Optimality of the Golden Angle

The golden angle $\theta_g$ provides the optimal angular separation for preventing periodic alignment in a sequential growth process.

#### 5.0 Proof of Theorem

-   **Statement 5.1:** The problem of avoiding periodic alignment is equivalent to choosing an angle $\theta$ such that the fraction $f = \frac{\theta}{2\pi}$ is maximally resistant to being approximated by simple rational numbers $\frac{m}{n}$.
-   **Statement 5.2:** From Theorem 2, the golden ratio $\phi$ is the most irrational number. Numbers related to $\phi$ by simple rational operations also share this property of being poorly approximable. The relevant fraction for the golden angle is $f_g = \frac{\theta_g}{2\pi} = \frac{1}{\phi^2}$.
-   **Statement 5.3:** Choosing $\theta = \theta_g$ means $f = f_g = \frac{1}{\phi^2}$, which is the value that maximally avoids rational approximation. Therefore, choosing the angular separation to be the golden angle $\theta_g$ maximally avoids periodic alignment, ensuring that successive elements are placed in a manner that most uniformly fills the circle over time.

---
## References

Gardner, M. (1964, March). Mathematical games: The remarkable lore of the prime numbers. *Scientific American*, *210*(3), 120–128.

Hennessy, J. L., & Patterson, D. A. (2012). *Computer architecture: A quantitative approach* (5th ed.). Morgan Kaufmann.

Ising, E. (1925). Beitrag zur Theorie des Ferromagnetismus. *Zeitschrift für Physik*, *31*(1), 253–258. https://doi.org/10.1007/BF02980577

Lucas, A. (2014). Ising formulations of many NP problems. *Frontiers in Physics*, *2*, 5. https://doi.org/10.3389/fphy.2014.00005

McMahon, P. L., Marandi, A., Haribara, Y., Hamerly, R., Langrock, C., Tamate, S., Inagaki, T., Takesue, H., Utsunomiya, S., Aihara, K., Byer, R. L., Fejer, M. M., Mabuchi, H., & Yamamoto, Y. (2016). A fully programmable 100-spin coherent Ising machine with all-to-all connections. *Science*, *354*(6312), 614–617. https://doi.org/10.1126/science.aah5178

Raussendorf, R., & Briegel, H. J. (2001). A one-way quantum computer. *Physical Review Letters*, *86*(22), 5188–5191. https://doi.org/10.1103/PhysRevLett.86.5188

Shannon, C. E. (1948). A mathematical theory of communication. *The Bell System Technical Journal*, *27*(3), 379–423. https://doi.org/10.1002/j.1538-7305.1948.tb01338.x

Shor, P. W. (1994). Algorithms for quantum computation: Discrete logarithms and factoring. In S. Goldwasser (Ed.), *Proceedings of the 35th Annual Symposium on Foundations of Computer Science* (pp. 124–134). IEEE Computer Society Press. https://doi.org/10.1109/SFCS.1994.365700

Vogel, H. (1979). A better way to construct the sunflower head. *Mathematical Biosciences*, *44*(3–4), 179–189. https://doi.org/10.1016/0025-5564(79)90080-4

von Neumann, J. (1945). *First draft of a report on the EDVAC*. Moore School of Electrical Engineering, University of Pennsylvania.

Wulf, W. A., & McKee, S. A. (1995). Hitting the memory wall: Implications of the obvious. *ACM SIGARCH Computer Architecture News*, *23*(1), 20–24. https://doi.org/10.1145/216585.216588216585.216588
