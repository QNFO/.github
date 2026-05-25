---
author: Rowan Brad Quni
email: rowan.quni@qnfo.org
website: http://qnfo.org
ORCID: 0009-0002-4317-5604
ISNI: 0000000526456062
robots: By accessing this content, you agree to https://qnfo.org/LICENSE. Non-commercial use only. Attribution required.
DC.rights: https://qnfo.org/LICENSE. Users are bound by terms upon access.
modified: 2025-10-06T17:01:20Z
title: Architecture for 6G
aliases:
  - Architecture for 6G
---
# Compute-on-Frequency Architecture for 6G Telecommunications

## A Strategic Imperative for National Telecoms

**Author:** Rowan Brad Quni-Gudzinas
**Affiliation:** QNFO
**Contact:** rowan.quni@qnfo.org
**ORCID:** 0009-0002-4317-5604
**ISNI:** 0000 0005 2645 6062
**DOI:** 10.5281/zenodo.17280553
**Publication Date:** 2025-10-06
**Version:** 1.0.1

The dominant paradigm of digital computation, founded on the substrate-agnostic Turing machine and von Neumann architecture, is approaching fundamental physical and architectural limits. This paper presents a foundational critique of this paradigm, arguing that its core principle—the dissociation of abstract logic from physical reality—leads to intrinsic inefficiencies like the von Neumann bottleneck and immense thermodynamic costs associated with suppressing the native dynamics of physical systems. This foundational mismatch has precipitated dual crises for modern telecommunications: a crisis of computational intractability in managing the complexity of 6G networks and a crisis of cryptographic collapse, as new harmonic analysis methods pose a potential non-quantum threat to factorization-based security. As a resolution, this paper proposes a hybrid classical-harmonic architectural framework. This new model retains the classical paradigm for robust data transport while offloading intractable optimization and security tasks to specialized, physically-aligned co-processors that compute via resonance. The strategic imperative is a preemptive architectural transformation, securing national infrastructure with post-harmonic cryptography and optimizing network control planes with harmonic co-processors. This reframes telecommunications as a branch of applied physics, shifting the focus from programming abstract logic to engineering and harvesting the computational dynamics of physical systems.

---

### **1.0 The Foundational Mismatch: Abstract Logic Versus Physical Reality**

The prevailing paradigm of digital computation, built upon the abstract foundations of the Turing machine and the physical architecture of von Neumann, is predicated on a fundamental mismatch between the abstract, logical models used to represent information and the physical reality in which these models are implemented. This schism, while enabling the universality of digital systems, has created a framework that is fundamentally at odds with the principles of physical efficiency. The classical approach succeeds not by harnessing the native dynamics of its physical substrate, but by expending enormous and ever-increasing amounts of energy to suppress them, forcing the continuous, complex behavior of the universe into a discrete, simplified logical structure. This core inefficiency is the source of the dual crises now confronting the telecommunications industry: a crisis of computational intractability and a crisis of cryptographic collapse.

#### **1.1 The Classical Paradigm: Computation as an Abstract Logical Process**

The classical framework that underpins all modern telecommunications is a direct technological descendant of the abstract, logical model of computation developed in the mid-20th century. This framework treats information as a sequence of abstract symbols and computation as a set of rules for manipulating them, with the physical world serving as a convenient but often problematic medium for implementation. This separation of logic from physics, while powerful, is the ultimate source of the framework’s emerging limitations.

##### **1.1.1 Architectural Blueprint: The Von Neumann Model**

The von Neumann model, which has served as the architectural blueprint for virtually all digital computers for over seventy years, institutionalizes the separation of logic from physics (von Neumann, 1945). Its design principles create inherent and unavoidable inefficiencies that are now reaching their physical limits.

##### **1.1.1.1 The Separation of Processing and Memory**

The defining characteristic of the von Neumann architecture is the physical separation of the central processing unit (CPU), where logical instructions are executed, from random-access memory (RAM), where data and instructions are stored. This design necessitates the constant shuttling of data across a physical bus, creating a fundamental performance constraint known as the von Neumann bottleneck. The system’s overall throughput becomes limited not by the speed of the processor, but by the bandwidth and latency of the connection to memory (Wulf & McKee, 1995). For the data-intensive workloads of modern network management and artificial intelligence, the energy and time consumed by this data movement can far exceed that of the actual computation (Hennessy & Patterson, 2012). This architectural tax grows more severe as problems become more data-intensive, forcing processors to spend an increasing fraction of their operational cycles in a stalled state, idly waiting for data.

##### **1.1.1.2 The Sequential Execution of Instructions**

The von Neumann model operates on a principle of sequential execution, processing a linear stream of instructions one at a time. While modern processors employ parallelism through multiple cores, each core still fundamentally operates on this sequential principle. This approach is profoundly inefficient for solving problems that are inherently parallel and interconnected, such as global network optimization, where the state of every component affects every other component simultaneously. The architecture forces a naturally parallel problem to be broken down into a series of discrete, sequential steps, adding massive computational overhead and creating a profound mismatch between the structure of the problem and the structure of the machine designed to solve it.

##### **1.1.2 Informational Primitive: The Abstract, Discrete Bit**

The informational primitive of the classical framework is the bit, a purely abstract, dimensionless symbol representing one of two discrete states, $0$ or $1$. The very abstraction of the bit from its underlying physical reality is the source of the paradigm’s thermodynamic inefficiency.

##### **1.1.2.1 The Suppression of Native Physical Dynamics**

A transistor, the physical embodiment of a bit, is a complex analog device with a continuous range of electrical behaviors. The digital paradigm achieves reliability by expending significant energy to force this continuous physical system into just two discrete, stable states (e.g., cutoff or saturation). All the intermediate, analog information about the transistor’s state is treated as noise and actively suppressed. This process requires constant power to maintain the artificial binary states against the natural tendency of the physical system to explore its full, continuous state space. This act of information suppression is not merely an implementation detail; it is a defining feature of the paradigm and a primary source of its energetic cost.

##### **1.1.2.2 The Thermodynamic Cost of Maintaining Artificial States**

To maintain the integrity of these artificial discrete states against inherent physical noise, such as thermal fluctuations, digital systems rely on energy-intensive error correction codes and redundant logic. This entire apparatus represents a thermodynamic tax paid to maintain the illusion of a perfect, noiseless logical state on top of an imperfect, noisy physical substrate. The system is constantly fighting against the second law of thermodynamics, expending energy to create and preserve an unnatural state of low-entropy order. In large-scale data centers, the energy required to power and cool this brute-force approach to reliability constitutes a significant and growing fraction of global electricity consumption.

#### **1.2 The Harmonic Paradigm: Computation as a Physical Dynamic Process**

In direct opposition to the classical framework, a harmonic paradigm redefines computation as a physical dynamic process. It seeks to close the gap between logic and physics by aligning the computational model with the native, energy-minimizing behavior of the physical substrate.

##### **1.2.1 Architectural Blueprint: The Principle of Computational Alignment**

The architectural blueprint of the harmonic paradigm is the principle of computational alignment, which posits that maximum efficiency is achieved when the structure of a problem is made isomorphic to the natural dynamics of the physical computing substrate.

##### **1.2.1.1 The Isomorphism of Problem Structure and Substrate Dynamics**

This principle mandates a shift from imposing a universal set of logical operations onto a passive substrate to engineering a substrate whose natural physical evolution intrinsically solves the problem. For example, a complex optimization problem is solved by mapping its cost function onto the physical energy landscape (the Hamiltonian) of a system, such that the system’s natural tendency to settle into its lowest energy state directly yields the optimal solution. The computation becomes analogous to a soap film naturally finding the minimal surface area that spans a given boundary—a complex optimization problem solved instantly and with minimal energy by the laws of physics.

##### **1.2.1.2 The Unification of Processing and Memory in the Substrate State**

In this model, the distinction between processing and memory dissolves. The state of the physical substrate *is* both the memory and the processor. Information is stored in the configuration of the system’s components, and computation occurs as the entire system evolves in parallel, with every component interacting with every other component simultaneously. This inherently parallel and in-memory processing model completely eliminates the von Neumann bottleneck by making the entire substrate the computer, thereby removing the need to shuttle data between separate processing and memory units.

##### **1.2.2 Informational Primitive: The Physical, Continuous Cycle**

The informational primitive of this framework is the physical, continuous cycle—an oscillation with inherent properties of frequency, amplitude, and phase. The cycle is the native language of physical systems, from the vibration of atoms to the propagation of light.

##### **1.2.2.1 The Harnessing of Native Physical Dynamics**

Instead of suppressing the physical dynamics of the substrate, the harmonic paradigm harnesses them as the computational mechanism itself. Phenomena like resonance, interference, and diffraction are no longer sources of noise to be eliminated, but are the fundamental operations of the computer. The computation becomes a process of guiding and interpreting the natural, complex interactions of waves and oscillators. A calculation is performed not by executing a sequence of logical gates, but by creating a physical system where the constructive and destructive interference of waves leads to a final state that represents the solution.

##### **1.2.2.2 The Energetic Efficiency of Operating in Native States**

By operating in the native, continuous states of a physical system, this framework avoids the immense energetic cost of forcing and maintaining artificial discrete states. The computation is a process of the system settling into a natural, stable equilibrium or resonant mode, which is often a path of minimum energy expenditure. This results in a computational paradigm that is orders of magnitude more energy-efficient than its classical counterpart for aligned problem classes, as it works with the grain of physics rather than against it.

### **2.0 The Consequence: Dual Crises of the Classical Framework**

The foundational mismatch of the classical framework is no longer a purely academic concern. It has given rise to two imminent and interconnected crises that threaten the stability and performance of the global telecommunications infrastructure: a crisis of computational intractability in the management of next-generation networks, and a crisis of cryptographic collapse that undermines the security of all digital communications.

#### **2.1 The Crisis of Computational Intractability in 6G Network Management**

The architectural vision for Sixth-Generation (6G) wireless networks, characterized by AI-native operations, terahertz spectra, and microsecond-scale control loops, creates a control plane management problem of unprecedented complexity. The classical von Neumann architecture is fundamentally incapable of solving these management problems within the required latency budgets, leading to a crisis of computational intractability.

##### **2.1.1 Drivers of Exponential Control Plane Complexity**

The control plane of a telecommunications network is the intelligent layer that manages resources, routes traffic, and maintains quality of service. In 6G, this layer will face an unprecedented level of complexity that will render current management strategies obsolete.

##### **2.1.1.1 The Shift to AI-Native Network Architectures**

Future networks are envisioned as AI-native, where nearly every aspect of their operation, from resource allocation to security, is managed by complex machine learning models in real time. While this provides the necessary intelligence to manage the network, it also creates a massive computational burden, as these algorithms must constantly process vast amounts of data and make decisions on microsecond timescales. The classical architecture is ill-suited for the massive, parallel matrix operations that dominate these workloads, leading to high latency and power consumption.

##### **2.1.1.2 The Management of Terahertz Spectra and Dynamic Slicing**

The move to higher-frequency spectra, such as the terahertz (THz) band, introduces new physical challenges like high atmospheric absorption and sensitivity to blockage, requiring even more sophisticated and rapid beamforming and tracking. Simultaneously, the concept of dynamic network slicing—the creation of virtual, isolated networks with guaranteed performance for specific applications (e.g., autonomous vehicles, remote surgery)—adds another layer of complex, real-time resource allocation. The number of variables to be optimized across these domains grows combinatorially, creating a problem space that is too vast for classical computers to explore effectively in real time.

##### **2.1.2 Failure Modes of Classical Optimization at Microsecond Latencies**

The core optimization tasks in network management are computationally hard, and the classical approach of using heuristic algorithms to find approximate solutions is breaking down as latency requirements become more stringent.

##### **2.1.2.1 The NP-Hard Nature of Global Network Control Problems**

Many of the fundamental problems in network management are classified as NP-hard, meaning that finding a provably optimal solution requires a computational effort that grows exponentially with the size of the network (Luo & Zhang, 2008). Key examples include real-time spectrum resource allocation, which involves assigning frequency blocks to users to maximize overall capacity while minimizing interference, and massive MIMO beamforming vector calculation, which requires solving a massive system of equations to steer antenna beams toward users. For classical computers, these problems represent a hard wall of computational complexity.

##### **2.1.2.2 The Inability to Achieve True Optima within Latency Budgets**

While classical processors can run heuristic algorithms to find approximate solutions to these problems, they are fundamentally unable to find the true global optima within the microsecond-scale latency budgets required for 6G control loops. This forces network operators to rely on sub-optimal solutions that are merely sufficient. This compromise directly results in a significant reduction in the achievable spectral efficiency and overall capacity of the network, leaving a substantial portion of the infrastructure’s potential untapped. This represents a direct economic loss and a failure to fully capitalize on massive infrastructure investments.

#### **2.2 The Crisis of Cryptographic Collapse**

Concurrent with the crisis of complexity is a more systemic threat: the impending collapse of the cryptographic foundations that secure the entirety of modern digital communication. This threat comes not only from the well-publicized development of quantum computers but also from a newly postulated class of non-quantum, classical threats.

##### **2.2.1 The Foundational Vulnerability of Public-Key Cryptography**

The security of nearly all modern public-key cryptography, which underpins secure e-commerce, banking, and government communications, rests on the assumed computational difficulty of a small number of mathematical problems.

##### **2.2.1.1 The Dependence on the Assumed Hardness of Integer Factorization**

The widely used RSA algorithm, for example, derives its security from the fact that it is easy to multiply two large prime numbers together but computationally intractable for classical computers to find those prime factors from the resulting composite number (Rivest et al., 1978). The entire security model is a bet on the continued computational hardness of this specific problem, an assumption that has held for decades but is not a mathematical certainty.

##### **2.2.1.2 The Systemic Risk to All Secure Communications Infrastructure**

The development of any machine—quantum or classical—that can solve the integer factorization problem in a practical amount of time would constitute a systemic failure of the global security infrastructure. It would allow a malicious actor to retroactively decrypt nearly all previously recorded encrypted traffic and to impersonate any secure server on the internet, leading to a catastrophic collapse of digital trust. This “harvest now, decrypt later” scenario poses a grave threat to national security and economic stability.

##### **2.2.2 The Emergence of Non-Quantum, Physically-Aligned Threats**

While the threat from quantum computers via Shor’s algorithm is well-known, a new theoretical vector of attack is emerging that reframes factorization as a problem of physics, potentially solvable by a specialized classical machine.

##### **2.2.2.1 The Reframing of Factorization as a Harmonic Analysis Problem**

The theoretical foundation for this emergent threat lies in a radical reframing of integer factorization, moving it from the domain of number theory and computational complexity to the domain of harmonic analysis and physical resonance. In this view, a composite number can be modeled as a dissonant state, a complex waveform composed of the superposition of multiple underlying frequencies. The prime factors of the number correspond to the fundamental resonant frequencies that create this dissonant state. The problem of factorization is thus transformed from a computational search into a physical signal decomposition problem: finding the pure tones (primes) that constitute the complex sound (composite).

##### **2.2.2.2 The Postulated Threat of Polynomial-Time Classical Attack Vectors**

This reframing opens the door to new, non-quantum attack vectors that could solve factorization in polynomial time. A postulated harmonic zoom algorithm is a theoretical attack vector that uses principles of signal analysis to iteratively identify these fundamental resonant frequencies. More critically, a harmonic resonance computer is a postulated physical attack vector—a specialized classical analog machine designed to physically resonate at frequencies corresponding to the prime factors, thereby solving the problem through a physical dynamic process rather than a logical one. The existence of such a machine would render factorization-based cryptography obsolete without requiring a quantum computer.

### **3.0 The Synthesis: A Hybrid Classical-Harmonic Architectural Framework**

The resolution to these dual crises requires a fundamental transformation of the network architecture. The path forward is not to completely replace the classical framework, but to augment it, creating a hybrid classical-harmonic architectural framework that leverages the strengths of both paradigms. The unifying principle of this new architecture is computational offloading, where computationally intractable problems are offloaded from the classical controller to a specialized co-processor that is physically aligned with the problem’s structure.

#### **3.1 Unifying Principle: Computational Offloading to Physically-Aligned Substrates**

The concept of computational offloading to specialized hardware is a well-established and successful strategy in computer architecture. The proposed hybrid framework applies this proven principle to the new domain of network management and security.

##### **3.1.1 Conceptual Precedent: The CPU-GPU Model for Heterogeneous Computation**

The relationship between the classical controller and the harmonic co-processor is analogous to the relationship between a CPU and a Graphics Processing Unit (GPU) in a modern computer. The CPU, a general-purpose processor, handles the sequential logic of the main program, but it offloads the massively parallel task of graphics rendering to the GPU, a specialized piece of hardware designed specifically for that task. This model of heterogeneous computing has become the standard for high-performance applications, demonstrating the power of augmenting a general-purpose processor with specialized accelerators.

##### **3.1.2 Core Architectural Division of Labor**

The hybrid architecture creates a clear division of labor within the network, separating the transport of data from the computationally intensive management of the network itself.

##### **3.1.2.1 The Classical Data Plane for Robust, High-Volume Data Transport**

The data plane, which is responsible for the actual transport of user data packets, will remain a classical, digital system. The robustness, reliability, and high volume of classical digital communication are well-suited for this task. The goal is not to replace digital systems where they excel, but to augment them where they are weakest.

##### **3.1.2.2 The Hybrid Control Plane for Computationally Intensive Management**

The control plane, which is responsible for managing the network, will be transformed into a hybrid system. Routine functions will be handled by a classical controller, but the most computationally intensive optimization and security tasks will be offloaded to a harmonic co-processor. This is where the architectural innovation is focused.

#### **3.2 Structure of the Hybrid Control Plane**

The proposed hybrid control plane is a layered architecture designed to seamlessly integrate the classical and harmonic computational domains. It consists of a classical controller, a standardized interface, and the harmonic co-processor itself.

##### **3.2.1 Layer 1: The Classical Controller and Orchestrator**

The top layer is the classical controller, a traditional digital processor responsible for the overall management of the network and the orchestration of the hybrid system. Its key roles are the management of routine network functions, such as session and mobility management, and the identification and formulation of intractable optimization problems that need to be offloaded. It acts as the “brain” of the system, making high-level decisions and delegating the most difficult calculations.

##### **3.2.2 Layer 2: The Computational Offloading Interface and Physical Compiler**

The middle layer is the computational offloading interface, a standardized software and hardware layer that acts as the bridge between the classical and harmonic worlds. This layer would include a standardized Application Programming Interface (API) for classical-harmonic communication, allowing the classical controller to send problems to and receive solutions from the co-processor. It also includes a physical compiler, a sophisticated piece of software responsible for the problem-to-substrate mapping, translating the abstract mathematical problem from the classical controller into the specific set of physical control signals required to configure the harmonic co-processor.

##### **3.2.3 Layer 3: The Harmonic Co-Processor (Control Plane Accelerator)**

The third layer is the harmonic co-processor, also referred to as the control plane accelerator. This is a specialized, non-von Neumann physical system designed to solve specific classes of hard problems with extreme speed and energy efficiency. It operates by mapping the problem onto its physical dynamics, allowing the solution to emerge from the natural evolution of the system. This co-processor is the physical embodiment of the harmonic computational paradigm, acting as the “muscle” that executes the hard computations with physical efficiency.

### **4.0 Implementation Vector I: Securing National Infrastructure via Post-Harmonic Cryptography**

The first and most urgent implementation of the hybrid framework is to address the crisis of cryptographic collapse. The strategic mandate is a preemptive migration of the national communications infrastructure to post-harmonic cryptography, securing it against both quantum and the newly postulated harmonic threats.

#### **4.1 Strategic Mandate: Preemptive Migration Beyond Quantum Resistance**

A comprehensive security strategy must now account for multiple, distinct vectors of attack on the foundations of public-key cryptography. Relying on quantum resistance alone is no longer sufficient.

##### **4.1.1 The Insufficiency of Quantum Resistance as a Sole Security Criterion**

A cryptographic standard that is resistant to quantum computers is a necessary but not sufficient condition for long-term security. The new standard must also be secure against the potential for attacks based on harmonic analysis. A “post-quantum” standard that is inadvertently vulnerable to a specialized classical attack would represent a catastrophic failure of foresight. Therefore, the security of candidate algorithms must be evaluated against both threat vectors.

##### **4.1.2 The Selection of Cryptography Based on Non-Harmonic Hardness Problems**

The selection process for new cryptographic standards must therefore prioritize algorithms whose security is based on mathematical problems that do not appear to have a simple or exploitable harmonic structure.

##### **4.1.2.1 The Prioritization of Lattice-Based Cryptography**

In light of this dual threat landscape, the strategic prioritization shifts toward cryptographic schemes whose security is based on problems believed to be hard for both quantum and harmonic computers, with lattice-based cryptography emerging as a leading candidate. The security of these algorithms rests on the hardness of problems like the Shortest Vector Problem (SVP), which involves finding the closest point in a high-dimensional, irregular grid. The geometric, non-periodic nature of the SVP appears to lack the kind of exploitable harmonic structure that a harmonic resonance computer could attack (Alagic et al., 2022).

##### **4.1.2.2 The Prioritization of Hash-Based Signatures**

For digital signatures, the prioritization shifts to hash-based schemes. The security of these methods relies on the properties of cryptographic one-way functions (hashes), which are designed to be chaotic and to destroy any underlying mathematical structure. As such, they are believed to be resistant to attacks from both Shor’s algorithm and any foreseeable harmonic analysis attacks, as they lack the periodic structure that these attacks exploit.

#### **4.2 Phased Implementation Roadmap**

The migration to post-harmonic cryptography must be a phased and systematic process, beginning with the most critical and centralized components of the national infrastructure.

##### **4.2.1 Phase 1: Core Network and Backhaul Infrastructure Overhaul**

The first phase of the implementation roadmap must focus on securing the core network and backhaul infrastructure. This involves upgrading the cryptographic protocols used on the high-capacity fiber links that connect data centers and core routers, as well as the software and firmware of the routers themselves. It also requires upgrading the Hardware Security Modules (HSMs) located in secure Network Operations Centers, which are responsible for managing the network’s most critical cryptographic keys.

##### **4.2.2 Phase 2: Radio Access Network (RAN) and Edge Security Hardening**

The second phase would extend the security overhaul to the radio access network (RAN) and the network edge. This involves securing the connections between the 5G/6G base stations and the core network, a critical link known as the backhaul. It also requires updating the security protocols used for the authentication of user equipment (such as smartphones and IoT devices) as they connect to the network, likely through updates to SIM card technology and device firmware.

### **5.0 Implementation Vector II: Optimizing the Control Plane via Harmonic Co-Processing**

The second implementation vector focuses on using the hybrid architecture to solve the crisis of computational intractability in the 6G control plane. This involves identifying the most critical optimization problems and offloading them to a harmonic co-processor.

#### **5.1 Target Problem Space for Harmonic Offloading**

The first step is to identify the specific, high-value computational problems that are best suited for being offloaded to a harmonic co-processor.

##### **5.1.1 Real-Time Global Resource Allocation**

Real-time global resource allocation is a prime candidate. The problem of assigning spectrum and power to millions of users to maximize overall network capacity while satisfying quality-of-service constraints and minimizing interference can be formulated as an energy minimization problem. The physical compiler maps the user demands and interference constraints onto the physical Hamiltonian of the harmonic co-processor, allowing the optimal allocation to be found through a physical relaxation process, much like a physical system settling into its ground state.

##### **5.1.2 Dynamic Massive MIMO Beamforming Vector Calculation**

Dynamic massive MIMO beamforming is another critical application. The calculation of the optimal beamforming vectors for a massive MIMO base station involves solving a very large system of linear equations in real time. This problem can be mapped onto a physical system where the solution is found through the constructive and destructive interference of waves in a resonant medium. The final amplitude and phase of the waves at specific points in the medium directly correspond to the solution of the system of equations.

#### **5.2 The Harmonic Resonance Computer (HRC) as the Physical Accelerator**

The harmonic resonance computer (HRC) is the physical hardware designed to serve as the control plane co-processor. It is a specialized analog computer that operates on the principle of computation by resonance.

##### **5.2.1 Operational Principle: Computation by Physical Resonance**

The operational principle of the HRC involves three steps. First, the physical compiler encodes the problem into the initial state of the physical system, for example, by setting the coupling strengths in a network of oscillators. Second, the system is activated and allowed to naturally evolve to its lowest energy state, which corresponds to the optimal solution. Third, the final physical state of the system (e.g., the phase of the oscillators) is measured and read out as the solution vector. This entire process can occur on nanosecond timescales.

##### **5.2.2 Critical Engineering Challenges**

The development of a practical HRC faces two significant engineering challenges. The first is the problem-to-substrate isomorphism challenge, which is the difficulty of creating a robust and efficient physical compiler that can automatically and reliably map any problem from a given class onto the physical substrate. The second is the interpretive overhead paradox, which is the risk that the latency of the classical-harmonic interface—the time it takes to compile the problem, configure the HRC, and read out the solution—could negate the speed advantage of the physical computation itself. Overcoming these challenges is the central R&D task for this implementation vector.

### **6.0 Implementation Vector III: Exploiting the Physical Medium as a Computational Substrate**

The third and most forward-looking implementation vector involves a complete inversion of the traditional telecommunications paradigm, treating the physical environment not as a source of noise to be overcome, but as an active computational resource to be exploited.

#### **6.1 The Conceptual Inversion of the Signal-Versus-Noise Paradigm**

This approach re-contextualizes the physical effects of the propagation channel, such as multipath fading and scattering, as sources of information and computational structure, rather than as sources of noise.

##### **6.1.1 Re-contextualizing the Environment from Adversary to Resource**

By re-contextualizing multipath fading and scattering, this paradigm shift allows the system to harness environmental perturbations as a source of information about the physical world. The channel’s transfer function, which classical systems try to equalize and remove, is instead treated as the result of a useful computation.

##### **6.1.2 Harnessing Environmental Perturbations as Intrinsic Computation**

The complex way in which the environment alters a signal is not seen as damage, but as a complex computation performed by the environment itself. This new perspective enables the development of novel, physically-aligned protocols that use the channel itself to perform useful functions, such as sensing and ultra-low-power communication.

#### **6.2 The Emergence of Physically-Aligned Communication Protocols**

This new perspective enables the development of novel, physically-aligned protocols that use the channel itself to perform useful functions, such as sensing and ultra-low-power communication.

##### **6.2.1 Sensor-less Sensing via Channel State Tomography (CST)**

Computation via channel state tomography (CST) is a technique that uses ambient RF signals, such as Wi-Fi or cellular signals, as environmental probes. By deploying a network of simple receivers and analyzing the perturbations to these signals as they reflect off objects and people, the system can perform sensor-less sensing, for example, to create a real-time map of a building’s occupancy, monitor the vital signs of individuals within a room, or detect minute structural changes in a bridge for health monitoring.

##### **6.2.2 Ultra-Low-Power Communication via Resonant Channel Optimization**

Resonant channel optimization involves first identifying the natural harmonic properties of the transmission medium itself. The system then designs impedance-matched waveforms that are specifically tailored to excite the natural resonant modes of the channel. This allows for ultra-low-power communication by transmitting signals that the channel is naturally inclined to propagate, minimizing the energy lost to reflection and absorption. This could be particularly valuable for extending the battery life of massive Internet of Things (IoT) deployments.

### **7.0 Conclusion: The Strategic Imperative for Architectural Transformation**

The convergence of the dual crises in complexity and security creates a strategic imperative for a fundamental architectural transformation of our national telecommunications infrastructure. The continued reliance on the classical, digital paradigm is not a sustainable trajectory, and a failure to adapt could lead to a future of stagnating performance and systemic insecurity.

#### **7.1 The Inevitability of the Hybrid Architecture**

The adoption of a hybrid architecture is not a matter of choice, but of necessity. The classical scaling trajectory, which has served us for decades, is reaching its physical and economic limits, while the demands of a fully realized 6G network continue to grow exponentially.

##### **7.1.1 The Exhaustion of the Classical Scaling Trajectory**

The classical scaling trajectory, which has served us for decades, is reaching its physical and economic limits, while the demands of a fully realized 6G network continue to grow exponentially. The dual imperatives of maintaining national security in the face of new cryptographic threats and ensuring the performance of our critical communications infrastructure will force this architectural shift.

##### **7.1.2 The Dual Imperatives of National Security and Network Performance**

The dual imperatives of maintaining national security in the face of new cryptographic threats and ensuring the performance of our critical communications infrastructure will force this architectural shift. The continued reliance on the classical, digital paradigm is not a sustainable trajectory, and a failure to adapt could lead to a future of stagnating performance and systemic insecurity.

#### **7.2 The Reframing of Telecommunications as Applied Physics**

This architectural transformation represents a profound reframing of the field of telecommunications itself. It marks a shift away from the domain of logical abstraction and back toward the domain of physical implementation.

##### **7.2.1 The Shift from Abstract Programming to Physical Systems Engineering**

The future of network design and management will be less about writing software for abstract machines and more about engineering the physical dynamics of the network itself. The national telecommunications network will evolve into a vast, distributed, heterogeneous computer, where the flow of information is managed by a symbiotic interplay of robust classical systems and powerful, physically-aligned co-processors. The required skill set will shift from pure computer science to a hybrid of physics, materials science, and electrical engineering.

##### **7.2.2 The Network as a Distributed, Heterogeneous Computer**

The national telecommunications network will evolve into a vast, distributed, heterogeneous computer, where the flow of information is managed by a symbiotic interplay of robust classical systems and powerful, physically-aligned co-processors, marking a new era of computation that is deeply and fundamentally integrated with the physical world.

---

### **References**

Alagic, G., Apon, D., Cooper, D., Dang, Q., Dang, T., Kelsey, J., Lichtinger, J., Miller, C., Moody, D., Peralta, R., Perlner, R., Robinson, A., Smith-Tone, D., & Winder, D. (2022). *Status Report on the Third Round of the NIST Post-Quantum Cryptography Standardization Process* (NISTIR 8413). National Institute of Standards and Technology.

Hennessy, J. L., & Patterson, D. A. (2012). *Computer architecture: A quantitative approach* (5th ed.). Morgan Kaufmann.

Luo, Z. Q., & Zhang, S. (2008). Dynamic spectrum management: Complexity and duality. *IEEE Journal of Selected Topics in Signal Processing*, *2*(1), 57–73.

Rivest, R. L., Shamir, A., & Adleman, L. (1978). A method for obtaining digital signatures and public-key cryptosystems. *Communications of the ACM*, *21*(2), 120–126. https://doi.org/10.1145/359340.359342

von Neumann, J. (1945). *First draft of a report on the EDVAC*. Moore School of Electrical Engineering, University of Pennsylvania.

Wulf, W. A., & McKee, S. A. (1995). Hitting the memory wall: Implications of the obvious. *ACM SIGARCH Computer Architecture News*, *23*(1), 20–24. https://doi.org/10.1145/216585.216588

---

### **Appendix: Formal Derivation of the Equivalence between the Ising Model and the Quadratic Unconstrained Binary Optimization (QUBO) Formulation**

**1.0 Axioms and Definitions**

-   **Definition 1.1 (Ising Model):** The Ising model describes a system of interacting spins. For a set of $N$ spins, the state of the system is given by a vector $s = (s_1, s_2, \dots, s_N)$, where each spin variable $s_i$ can take one of two values, $s_i \in \{-1, 1\}$. The energy of the system, described by the Ising Hamiltonian $H$, is given by:

    $$ H(s) = - \sum_{i<j} J_{ij} s_i s_j - \sum_{i=1}^{N} h_i s_i $$

    where $J_{ij}$ is the coupling strength between spin $i$ and spin $j$, and $h_i$ is an external magnetic field acting on spin $i$. Finding the ground state of the Ising model is equivalent to finding the spin configuration $s$ that minimizes $H(s)$.

-   **Definition 1.2 (Quadratic Unconstrained Binary Optimization - QUBO):** A QUBO problem is an optimization problem that involves finding the minimum of a quadratic objective function of binary variables. For a set of $N$ binary variables, the state is given by a vector $x = (x_1, x_2, \dots, x_N)$, where each variable $x_i$ can take one of two values, $x_i \in \{0, 1\}$. The objective function to be minimized is:

    $$ f(x) = \sum_{i \le j} Q_{ij} x_i x_j = x^T Q x $$

    where $Q$ is an $N \times N$ matrix of real-valued coefficients. The diagonal terms $Q_{ii}$ represent linear costs (since $x_i^2 = x_i$ for $x_i \in \{0, 1\}$), and the off-diagonal terms $Q_{ij}$ represent quadratic costs.

**2.0 Proposition**

The problem of finding the ground state of an Ising model is mathematically equivalent to solving a QUBO problem. A direct mapping exists that transforms the Ising Hamiltonian into the QUBO objective function.

**3.0 Proof**

The proof demonstrates this equivalence by establishing a linear transformation between the spin variables $s_i$ and the binary variables $x_i$, and then substituting this transformation into the Ising Hamiltonian to derive the QUBO form.

-   **Statement 3.1:** Define the transformation between spin variables and binary variables.
    -   **Justification:** A linear mapping is required to connect the set $\{-1, 1\}$ to the set $\{0, 1\}$. The standard transformation is:

        $$ s_i = 2x_i - 1 $$

    -   **Verification:**
        -   If $x_i = 1$, then $s_i = 2(1) - 1 = 1$.
        -   If $x_i = 0$, then $s_i = 2(0) - 1 = -1$.
        The transformation correctly maps the domains. The inverse transformation is $x_i = (s_i + 1)/2$.

-   **Statement 3.2:** Substitute the variable transformation from Statement 3.1 into the Ising Hamiltonian (Definition 1.1).
    -   **Justification:** Direct substitution to express the Hamiltonian $H$ in terms of the binary variables $x_i$.
    -   **Result:**

        $$ H(x) = - \sum_{i<j} J_{ij} (2x_i - 1)(2x_j - 1) - \sum_{i=1}^{N} h_i (2x_i - 1) $$

-   **Statement 3.3:** Expand the algebraic terms in the expression for $H(x)$.
    -   **Justification:** Application of the distributive property of multiplication.
    -   **Calculation:**
        -   The interaction term: $(2x_i - 1)(2x_j - 1) = 4x_i x_j - 2x_i - 2x_j + 1$.
        -   The field term: $(2x_i - 1) = 2x_i - 1$.
    -   **Result:**

        $$ H(x) = - \sum_{i<j} J_{ij} (4x_i x_j - 2x_i - 2x_j + 1) - \sum_{i=1}^{N} h_i (2x_i - 1) $$

-   **Statement 3.4:** Distribute the summations and regroup terms by the power of the variables ($x_i x_j$, $x_i$, and constant terms).
    -   **Justification:** Rearranging the expression to match the structure of the QUBO objective function.
    -   **Result:**
        $$\begin{align*} H(x) = &\left( - \sum_{i<j} 4J_{ij} x_i x_j \right) \\ &+ \left( \sum_{i<j} 2J_{ij} x_i + \sum_{i<j} 2J_{ij} x_j - \sum_{i=1}^{N} 2h_i x_i \right) \\ &+ \left( - \sum_{i<j} J_{ij} + \sum_{i=1}^{N} h_i \right) \end{align*}$$

-   **Statement 3.5:** Consolidate the linear terms into a single summation over the index $i$.
    -   **Justification:** The term $\sum_{i<j} 2J_{ij} x_i$ sums over $j>i$ for a fixed $i$. The term $\sum_{i<j} 2J_{ij} x_j$ can be rewritten by swapping indices as $\sum_{j<i} 2J_{ji} x_i$. Assuming symmetric couplings ($J_{ij} = J_{ji}$), the total coefficient for a given $x_i$ from the interaction terms is $\sum_{j \neq i} 2J_{ij}$.
    -   **Calculation:** The complete linear part is:

        $$ \sum_{i=1}^{N} \left( \sum_{j \neq i} 2J_{ij} - 2h_i \right) x_i $$

    -   **Result:** The full Hamiltonian is:
        $$\begin{align*} H(x) = &\sum_{i<j} (-4J_{ij}) x_i x_j \\ &+ \sum_{i=1}^{N} \left( \sum_{j \neq i} 2J_{ij} - 2h_i \right) x_i \\ &+ \left( \sum_{i=1}^{N} h_i - \sum_{i<j} J_{ij} \right) \end{align*}$$

-   **Statement 3.6:** Identify the QUBO matrix $Q$ and the constant offset.
    -   **Justification:** The expression for $H(x)$ from Statement 3.5 is now in the form of a QUBO objective function plus a constant. Minimizing $H(x)$ is equivalent to minimizing $H(x) - \text{Constant}$.
    -   **Identification:**
        -   The quadratic coefficients (off-diagonal) are: $Q_{ij} = -4J_{ij}$ for $i \neq j$.
        -   The linear coefficients (diagonal, since $x_i^2 = x_i$) are: $Q_{ii} = \sum_{j \neq i} 2J_{ij} - 2h_i$.
        -   The constant offset is: $C = \sum_{i=1}^{N} h_i - \sum_{i<j} J_{ij}$.
    -   **Result:** The Ising Hamiltonian can be written as:

        $$ H(x) = \sum_{i<j} Q_{ij} x_i x_j + \sum_{i=1}^{N} Q_{ii} x_i + C $$

        This is the general form of a QUBO problem.

**4.0 Conclusion**

The derivation demonstrates that the Ising model Hamiltonian $H(s)$ is mathematically equivalent to the Quadratic Unconstrained Binary Optimization (QUBO) objective function $f(x)$. The linear transformation $s_i = 2x_i - 1$ provides a direct mapping between the spin variables $s_i \in \{-1, 1\}$ of the Ising model and the binary variables $x_i \in \{0, 1\}$ of a QUBO problem. The energy function of the Ising model maps to a quadratic polynomial of binary variables, plus a constant offset. As this constant does not affect the location of the minimum, finding the ground state (minimum energy configuration) of the Ising model is formally equivalent to finding the optimal solution to the corresponding QUBO problem. This equivalence is fundamental to the operation of physical systems, such as harmonic annealers, that solve combinatorial optimization problems by finding the ground state of an analogous physical system.
