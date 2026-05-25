---
author: Rowan Brad Quni-Gudzinas
ORCID: 0009-0002-4317-5604
ISNI: 0000000526456062
modified: 2026-04-03T08:18:53Z
title: Ultrametric Quantum Gravity and Computation
aliases:
  - Ultrametric Quantum Gravity and Computation
---

**Technical Report**
# Ultrametric Quantum Gravity and Computation

**Author:** Rowan Brad Quni-Gudzinas  
**Contact:** [rowan.quni@outlook.com](mailto:rowan.quni@outlook.com)  
**ORCID:** 0009-0002-4317-5604  
**ISNI:** 0000000526456062  
**DOI:** 10.5281/zenodo.19397516
**Date:** 2026-04-03
**Version:** 1.0

## **Executive Summary**

This report presents a unified theoretical framework that bridges two seemingly disparate frontiers: **ultrametric quantum computation** and **ultrametric quantum gravity**. Both paradigms replace the conventional Archimedean continuum with a discrete, hierarchical, tree‑like geometry described by p‑adic numbers and their associated Bruhat–Tits trees. The framework demonstrates that:

1. **The same non‑Archimedean geometry** that provides intrinsic fault‑tolerance in quantum computing also resolves the “problem of time” in quantum gravity via the Wheeler–DeWitt equation.
2. **Strange loops**–self‑referential cycles in hierarchical structures–emerge naturally in both contexts, offering a geometric origin for epistemic time and observer‑dependent phenomena.
3. **Physical predictions** include a discrete spectrum of area/volume, modified dispersion relations at high energies, and an emergent smooth spacetime as a coarse‑grained limit of the underlying fractal.

The synthesis yields a coherent picture: reality is a timeless, branching fractal; quantum computation is navigation of this fractal; and quantum gravity is the constraint that selects admissible branches.

---

## **Part I: Foundations Revisited – Non‑Archimedean Quantum Theory**

### **1. The Archimedean Limitation and the p‑adic Alternative**

#### **1.1 The Continuum Hypothesis and Its Discontents**
Conventional quantum mechanics and quantum field theory are built on the field of real (or complex) numbers, an Archimedean structure that assumes distances can be subdivided arbitrarily. This leads to the familiar problems of ultraviolet divergences, decoherence from continuous noise, and the measurement problem. In quantum computing, the same continuum forces an endless battle against small, accumulating errors.

#### **1.2 The p‑adic Number System**
For a fixed prime $p$, the p‑adic numbers $\mathbb{Q}_p$ form a complete field with an **ultrametric** norm: $|x+y|_p \le \max(|x|_p,|y|_p)$. The norm $|x|_p = p^{-n}$ measures divisibility by powers of $p$, making numbers with higher powers of $p$ “smaller.” This inversion of the usual notion of size is the key to hierarchical organization.

#### **1.3 The Bruhat–Tits Tree – Geometry of the Ultrametric**
The unit ball $\mathbb{Z}_p \subset \mathbb{Q}_p$ is a fractal tree: each vertex has exactly $p+1$ neighbours, and the distance between two vertices is the length of the unique geodesic connecting them. The tree is **self‑similar**–every subtree is isomorphic to the whole–and provides a natural visualization of the nested, disjoint balls that characterize ultrametric spaces.

#### **1.4 Ultrametric Quantum Mechanics (Vladimirov–Volovich)**
Quantum mechanics on $\mathbb{Q}_p$ replaces the Laplacian with the **Vladimirov fractional derivative**
$$
(D_p^\alpha\psi)(x)=\frac{1-p^{\alpha-1}}{1-p^{-\alpha}}\int_{\mathbb{Q}_p}\frac{\psi(x)-\psi(y)}{|x-y|_p^{\alpha+1}}\,d\mu_p(y),\quad \alpha>0,
$$
a pseudo‑differential operator whose eigenfunctions are p‑adic plane waves $\chi_p(kx)=e^{2\pi i\{kx\}_p}$. The spectrum is discrete, and the operator respects the tree structure–it is **ultrametric**.

#### **1.5 Intrinsic Fault‑Tolerance in Quantum Computation**
Encoding quantum information on the vertices of the Bruhat–Tits tree exploits the strong triangle inequality: small perturbations cannot accumulate. An error becomes significant only if it is large enough to jump to a different branch. This **geometric error suppression** eliminates the need for continuous, active error correction and offers a path to scalable, thermodynamically efficient quantum processors.

### **2. The Ultrametric Quantum Processor – A Hardware Blueprint**

#### **2.1 Physical Realization of the Bruhat–Tits Tree**
A candidate hardware architecture consists of coupled superconducting loops or topological qubits arranged in a hierarchical network. The coupling strengths decrease exponentially with tree distance, creating the required nested energy landscape. Control pulses address specific branches via frequency combs matched to the p‑adic norm.

#### **2.2 Discrete Gates and Topological Logic**
Quantum gates are not continuous rotations but discrete **isometries of the tree**. Elementary operations include:
- **Branch‑swap**: exchange two subtrees,
- **Vertex‑shift**: move the logical state to an adjacent vertex,
- **Scale transformation**: coarse‑graining or refinement of the description.

These operations are exact and immune to over‑rotation errors.

#### **2.3 Measurement and the Monna Map**
Reading out the quantum state requires projecting the p‑adic information onto the real numbers. The **Monna map** $M:\mathbb{Q}_p\to\mathbb{R}$ provides a continuous, measure‑preserving projection that translates the discrete branching structure into the familiar continuum. The map is inherently many‑to‑one, explaining the probabilistic outcomes of quantum measurement.

---

## **Part II: Ultrametric Quantum Gravity – The Wheeler–DeWitt Equation**

### **3. From Minisuperspace to p‑adic Superspace**

#### **3.1 The Wheeler–DeWitt Equation – Timelessness as a Feature**
In canonical quantum gravity, the Hamiltonian constraint $\mathcal{H}\Psi=0$ selects physical states from the space of 3‑geometries. The equation contains no time parameter–time is not a fundamental ingredient but an emergent, epistemic concept. This aligns perfectly with the timeless, branching structure of the Bruhat–Tits tree.

#### **3.2 p‑adic Minisuperspace**
Consider the simplest cosmological model: a Friedmann–Lemaître–Robertson–Walker universe with scale factor $a$ and a scalar field $\phi$. The usual Wheeler–DeWitt equation reads
$$
\left[-\frac{\partial^2}{\partial a^2}+\frac{1}{a^2}\frac{\partial^2}{\partial \phi^2}+V(a,\phi)\right]\Psi(a,\phi)=0 .
$$
Replace the real coordinates $(a,\phi)$ with p‑adic coordinates $(a_p,\phi_p)\in\mathbb{Q}_p\times\mathbb{Q}_p$, and the ordinary derivatives with Vladimirov operators $D_p^{\alpha_a}$ and $D_p^{\alpha_\phi}$. The result is the **ultrametric Wheeler–DeWitt equation**:
$$
\boxed{\left[-D_p^{\alpha_a}+\frac{1}{a_p^{2}}D_p^{\alpha_\phi}+V(a_p,\phi_p)\right]\Psi(a_p,\phi_p)=0 } .
$$

#### **3.3 Ultrametric Potential and Boundary Conditions**
The potential $V(a_p,\phi_p)$ is an **ultrametric function**–locally constant on p‑adic balls. Boundary conditions are imposed on the **boundary of the tree** $\partial T_p$, which is isomorphic to the projective line $\mathbb{P}^1(\mathbb{Q}_p)$. This boundary represents the “asymptotic” regime where the universe becomes classical.

### **4. Solutions – Fractal Branches and Hierarchical Cosmologies**

#### **4.1 Separation of Variables**
Write $\Psi(a_p,\phi_p)=A(a_p)\Phi(\phi_p)$. Then
$$
-D_p^{\alpha_a}A=\lambda A,\qquad \frac{1}{a_p^{2}}D_p^{\alpha_\phi}\Phi+V(a_p,\phi_p)\Phi=-\lambda\Phi .
$$

#### **4.2 Scale‑Factor Eigenfunctions**
The first equation is solved by p‑adic plane waves $A_k(a_p)=\chi_p(k a_p)$ with eigenvalue $-|k|_p^{\alpha_a}$. Each $k$ labels a **branch** of the tree. The full wavefunction is a superposition over branches:
$$
\Psi(a_p,\phi_p)=\sum_{k\in\mathbb{Q}_p}c_k\,\chi_p(k a_p)\,\Phi_k(\phi_p),
$$
where $\Phi_k$ satisfies a p‑adic Sturm–Liouville equation with the potential.

#### **4.3 The Branching Universe**
Because the Vladimirov operator is ultrametric, transition amplitudes are non‑zero only between points in the same or adjacent p‑adic balls. Consequently, the configuration space decomposes into a **discrete, branching fractal**. Each branch corresponds to a distinct cosmological history, and the superposition represents a “multiverse” that is static and timeless.

#### **4.4 Emergence of Classical Time**
An observer confined to one branch experiences a sequence of branching events as they move along the tree. This sequence creates the **illusion of time**–epistemic time. The familiar flow of time is thus a strange loop: the observer’s own path through the pre‑existing fractal generates a self‑referential ordering.

### **5. Strange Loops and the Modular Group**

#### **5.1 Self‑Similarity And Closed Orbits**
The Bruhat–Tits tree is invariant under the action of $\mathrm{GL}(2,\mathbb{Q}_p)$. Discrete subgroups (p‑adic modular groups) act by permuting branches while preserving the tree structure. An observer following a sequence of such permutations can return to an equivalent state after a finite number of steps–a **strange loop** in Hofstadter’s sense.

#### **5.2 Entanglement Across Scales**
If the wavefunction $\Psi$ is entangled across different scales of the tree, an observer’s local description becomes correlated with distant branches. This non‑local correlation can produce closed causal loops in the epistemic time experienced by the observer, reinforcing the strange‑loop phenomenon.

#### **5.3 The Quantum Gravity – Quantum Computation Correspondence**
The same group $\mathrm{GL}(2,\mathbb{Q}_p)$ that generates strange loops in quantum gravity also serves as the **gate set** for universal quantum computation on the Bruhat–Tits tree. This is not a coincidence: both systems are built on the same ultrametric geometry, and both exploit its discrete, hierarchical structure.

---

## **Part III: Synthesis – Bridging the Two Frontiers**

### **6. The Common Geometric Language**

#### **6.1 The Bruhat–Tits Tree as Universal Substrate**
The tree $T_p$ is the fundamental object underlying both theories:
- In quantum computation, its vertices encode quantum states, and its edges define fault‑tolerant gates.
- In quantum gravity, its vertices represent cosmological configurations, and its edges define allowed transitions.

#### **6.2 Ultrametricity as a Unifying Principle**
The strong triangle inequality $|x+y|_p\le\max(|x|_p,|y|_p)$ guarantees:
- **Noise suppression** in quantum computers (small errors cannot add up),
- **Hierarchical clustering** in configuration space (branches are dynamically isolated),
- **Discrete spectrum** of physical observables (area, volume, energy).

#### **6.3 Timelessness and Epistemic Navigation**
Both frameworks eliminate fundamental time. In quantum computation, “computation” is a path through a static tree of possible states. In quantum gravity, “cosmology” is a path through a static tree of possible geometries. The observer’s experience of time is always epistemic–a reading of their own position on the tree.

### **7. Physical Predictions and Experimental Signatures**

#### **7.1 Discrete Geometry of Space**
The p‑adic norm takes values $p^{-n}$; therefore areas and volumes are quantized in units of $p^{-n}$. This predicts a **minimum length** $\ell_{\min}\propto p^{-1/2}$ (in appropriate units) and a holographic scaling of degrees of freedom with area.

#### **7.2 Modified Dispersion Relations**
The Vladimirov operator yields energy–momentum relations of the form $E\propto |k|_p^{\alpha}$. For $\alpha\neq2$, this deviates from the usual relativistic dispersion $E^2=k^2+m^2$. Such deviations could be detectable in ultra‑high‑energy cosmic rays or in table‑top experiments with strongly correlated quantum materials that realize an effective p‑adic geometry.

#### **7.3 Emergent Smooth Spacetime**
The continuum real line emerges as a **coarse‑grained limit** of the p‑adic tree. One can take a sequence of primes $p\to\infty$ or use the Monna map to project the fractal onto the real numbers. In this limit, the Wheeler–DeWitt equation reduces to the standard, smooth version–but the underlying fractal structure leaves residual **quantum fluctuations** that could explain the observed pattern of cosmological perturbations.

#### **7.4 Testability in Quantum Simulators**
Ultrametric quantum computers, once built, can directly simulate the p‑adic Wheeler–DeWitt equation. By preparing states on the Bruhat–Tits tree and measuring their evolution under the Vladimirov operator, one can test the predictions of ultrametric quantum gravity in a controlled laboratory setting.

### **8. Philosophical Implications – A New Ontology**

#### **8.1 The Fractal Quantum Reality**
The synthesis advocates an ontology in which reality is fundamentally discrete, hierarchical, and timeless. The continuous, flowing world of everyday experience is a **coarse‑grained projection** of this deeper fractal structure. Quantum mechanics and gravity are not separate theories but different perspectives on the same underlying geometry.

#### **8.2 The End of the Measurement Problem**
Wavefunction “collapse” is not a physical process but an **epistemic update**–the observer’s location on the tree becomes more precise. Because the tree is static, there is no need for dynamical collapse mechanisms or many worlds. Probability arises from the many‑to‑one nature of the Monna projection.

#### **8.3 Time as a Strange Loop**
Time is not a fundamental dimension but a **self‑referential cycle** generated by the observer’s navigation of the fractal. This explains why time appears to flow, why it seems irreversible, and why it is intimately tied to consciousness (as emphasized by Hofstadter). The strange loop is the missing link between timeless physics and temporal experience.

---

## **Conclusion – The Ultra‑Metric Paradigm**

The unified framework presented here connects ultrametric quantum computation with ultrametric quantum gravity. The key insights are:

1. **Geometry is destiny**–the non‑Archimedean, fractal geometry of the Bruhat–Tits tree provides both intrinsic fault‑tolerance for quantum computers and a natural resolution of the problem of time in quantum gravity.
2. **Strange loops are universal**–they appear in the dynamics of both systems, offering a geometric explanation for self‑reference, consciousness, and the emergence of time.
3. **The framework is testable**–through modified dispersion relations, discrete geometry, and, ultimately, quantum simulators built on ultrametric hardware.

The paradigm shift from Archimedean to ultrametric mathematics is not merely a technical convenience; it is a profound change in our understanding of reality. It suggests that the universe is not a smooth continuum but a vast, timeless, branching fractal–and that our experience of time, computation, and physical law are all manifestations of our navigation through this fractal.

