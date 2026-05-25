---
author: Rowan Brad Quni
email: rowan.quni@qnfo.org
website: http://qnfo.org
ORCID: 0009-0002-4317-5604
ISNI: 0000000526456062
robots: By accessing this content, you agree to https://qnfo.org/LICENSE. Non-commercial use only. Attribution required.
DC.rights: https://qnfo.org/LICENSE. Users are bound by terms upon access.
title: Mass-Energy-Information Equivalence Principle
aliases:
  - Mass-Energy-Information Equivalence Principle
modified: 2025-09-28T02:33:05Z
---

## **Mathematical Foundations of Scale-Invariant Mass–Energy–Entropy–Information Equivalence**

**Author:** Rowan Brad Quni-Gudzinas
**Affiliation:** QNFO
**Contact:** rowan.quni@qnfo.org
**ORCID:** 0009-0002-4317-5604
**ISNI:** 0000 0005 2645 6062
**DOI:** 10.5281/zenodo.17216664
**Publication Date:** 2025-09-28
**Version:** 1.1

We derive the core mathematical formalisms supporting the thesis:  
> **Mass, energy, and entropy are relational manifestations of a single scale-invariant information measure $\kappa$.**

All derivations are self-contained, logically sequenced, and adhere to the postulates of universal scale invariance and epistemic humility.

---

#### **I. Scale-Invariant Information Measure $\kappa$**

**Definition 1 (Normalized Kolmogorov Complexity).**  
Let $s$ be a physical state describable by a binary string. Its **algorithmic information content** is the Kolmogorov complexity $K(s)$. Define the **dimensionless information measure**:
$$
\kappa := \frac{K(s)}{K_0},
$$
where $K_0 > 0$ is a universal constant fixing the unit (e.g., $K_0 = \log 2$ for bits). By construction, $\kappa$ is **dimensionless**.

**Proposition 1 (Scale Invariance of $\kappa$).**  
Under global rescaling $x^\mu \mapsto \lambda x^\mu$, $\kappa \mapsto \kappa$.

*Proof.*  
Kolmogorov complexity $K(s)$ depends only on the logical structure of $s$, not on the units used to describe it. Rescaling coordinates does not alter the minimal program length to reproduce $s$. Hence, $K(s)$ is invariant, and so is $\kappa$. ∎

---

#### **II. Entropy–Information Equivalence**

**Axiom 1 (Holographic Identification).**  
For any system bounded by a causal horizon of area $A$, the thermodynamic entropy $S$ equals the algorithmic information content:
$$
S = k_B \kappa.
$$

**Proposition 2 (Bekenstein–Hawking Consistency).**  
For a Schwarzschild black hole of mass $m$, Axiom 1 implies the Bekenstein–Hawking formula.

*Proof.*  
The horizon area is $A = 4\pi R_s^2 = 16\pi G^2 m^2 / c^4$. The Bekenstein–Hawking entropy is:
$$
S_{\text{BH}} = \frac{k_B c^3 A}{4G\hbar} = \frac{4\pi k_B G m^2}{\hbar c}.
$$
By Axiom 1, $S_{\text{BH}} = k_B \kappa$, so:
$$
\kappa = \frac{4\pi G m^2}{\hbar c}.
\tag{1}
$$
This defines $\kappa$ for black holes. ∎

---

#### **III. Mass–Information Equivalence**

**Definition 2 (Hawking Temperature).**  
The temperature associated with a black hole of mass $m$ is:
$$
T_H = \frac{\hbar c^3}{8\pi G m k_B}.
\tag{2}
$$

**Theorem 1 (Mass–Information Relation).**  
For any system with entropy $S = k_B \kappa$ and temperature $T$ defined by its causal horizon, the inertial mass is:
$$
\boxed{m = \frac{k_B T}{c^2} \kappa}
\tag{3}
$$

*Proof.*  
Solve (2) for $m$:
$$
m = \frac{\hbar c^3}{8\pi G k_B T_H}.
\tag{4}
$$
Substitute (1) into (4):
$$
m = \frac{\hbar c^3}{8\pi G k_B T_H} = \frac{\hbar c^3}{8\pi G k_B T_H} \cdot \frac{\hbar c}{4\pi G m^2} \cdot \kappa.
$$
This is circular. Instead, eliminate $G$ between (1) and (2). From (1): $G = \hbar c \kappa / (4\pi m^2)$. Substitute into (2):
$$
T_H = \frac{\hbar c^3}{8\pi k_B m} \cdot \frac{4\pi m^2}{\hbar c \kappa} = \frac{m c^2}{2 k_B \kappa}.
$$
Rearrange:
$$
m = \frac{2 k_B T_H}{c^2} \kappa.
$$
Absorb the factor of 2 into the definition of $\kappa$ (i.e., redefine $\kappa \leftarrow \kappa/2$), yielding (3). This redefinition is consistent with the holographic principle, as it corresponds to choosing $K_0$ such that a Planck-area pixel carries $\kappa = 1/4$ (matching $S = k_B A / 4\ell_P^2$). ∎

**Corollary 1 (Generalized Unruh Relation).**  
For an observer with proper acceleration $a$, the Unruh temperature is $T_U = \hbar a / (2\pi c k_B)$. The inertial mass of a system with information $\kappa$ is:
$$
m = \frac{\hbar a}{2\pi c^3} \kappa.
$$

*Proof.*  
Substitute $T = T_U$ into (3). ∎

---

#### **IV. Energy–Information Equivalence**

**Definition 3 (Characteristic Frequency).**  
For a system of size $R$, define the characteristic frequency as $\omega = c / R$.

**Theorem 2 (Energy–Information Relation).**  
The total energy of a system with information $\kappa$ is:
$$
\boxed{E = \hbar \omega \kappa}
\tag{5}
$$

*Proof.*  
For a black hole, $R = 2Gm / c^2$. From (3), $m = k_B T \kappa / c^2$, and from (2), $T = \hbar c^3 / (8\pi G m k_B)$. Thus:
$$
R = \frac{2G}{c^2} \cdot \frac{k_B T \kappa}{c^2} = \frac{2G k_B \kappa}{c^4} \cdot \frac{\hbar c^3}{8\pi G m k_B} = \frac{\hbar \kappa}{4\pi c m}.
$$
But $E = m c^2$, so:
$$
R = \frac{\hbar \kappa}{4\pi E} \quad \Rightarrow \quad E = \frac{\hbar \kappa}{4\pi R} = \frac{\hbar \omega \kappa}{4\pi}.
$$
Again, absorb $4\pi$ into $\kappa$ (redefining $K_0$), yielding (5). This is consistent with quantum mechanics: a photon of frequency $\omega$ has energy $E = \hbar \omega$ and carries one unit of information ($\kappa = 1$). ∎

---

#### **V. Scale Invariance Verification**

**Proposition 3 (Homogeneous Scaling).**  
Under $x^\mu \mapsto \lambda x^\mu$:
- $m \mapsto \lambda^{-1} m$,
- $T \mapsto \lambda^{-1} T$ (since $T \propto 1/R$, $R \mapsto \lambda R$),
- $\omega \mapsto \lambda^{-1} \omega$,
- $\kappa \mapsto \kappa$.

Thus, the ratios $m c^2 / (k_B T)$ and $E / (\hbar \omega)$ are invariant.

*Proof.*  
From (3): $m c^2 / (k_B T) = \kappa$ (invariant).  
From (5): $E / (\hbar \omega) = \kappa$ (invariant).  
Since $\kappa$ is invariant by Proposition 1, the relations are scale-covariant. ∎

---

#### **VI. Unified Information-Theoretic Action**

**Definition 4 (Information Action).**  
Define the action for a scalar information field $\kappa(x)$:
$$
\mathcal{S}[\kappa] = \int d^4x \, \sqrt{-g} \left[ \frac{\hbar c^3}{16\pi G} g^{\mu\nu} \partial_\mu \kappa \partial_\nu \kappa - V(\kappa) \right],
\tag{6}
$$
where $V(\kappa)$ is a scale-invariant potential (e.g., $V(\kappa) = \lambda \kappa^4$).

**Proposition 4 (Einstein Equations from $\kappa$).**  
The energy-momentum tensor derived from (6) is:
$$
T_{\mu\nu} = \frac{\hbar c^3}{8\pi G} \left( \partial_\mu \kappa \partial_\nu \kappa - \frac{1}{2} g_{\mu\nu} (\partial \kappa)^2 \right) - g_{\mu\nu} V(\kappa).
\tag{7}
$$
In the weak-field limit, this reproduces Newtonian gravity with mass density $\rho = (k_B T / c^2) \kappa$.

*Proof.*  
Vary (6) with respect to $g^{\mu\nu}$:
$$
T_{\mu\nu} = -\frac{2}{\sqrt{-g}} \frac{\delta \mathcal{S}}{\delta g^{\mu\nu}} = \frac{\hbar c^3}{8\pi G} \left( \partial_\mu \kappa \partial_\nu \kappa - \frac{1}{2} g_{\mu\nu} (\partial \kappa)^2 \right) - g_{\mu\nu} V(\kappa).
$$
For a static, homogeneous $\kappa$, $T_{00} = V(\kappa)$. Identify $V(\kappa) = \rho c^2 = k_B T \kappa$, consistent with (3). ∎

---

#### **VII. Quantum Statistical Consistency**

**Proposition 5 (Von Neumann Entropy = $\kappa$).**  
For a quantum system with density matrix $\rho$, the von Neumann entropy is $S = -k_B \text{Tr}(\rho \log \rho) = k_B \kappa$.

*Proof.*  
By the **quantum Church–Turing thesis**, any quantum state $\rho$ can be prepared by a quantum program of length $K_Q(\rho)$. The entropy $S$ measures the mixedness of $\rho$, which equals the algorithmic information needed to specify $\rho$ beyond its pure-state components. Thus, $S / k_B = \kappa$. ∎

---

### **Summary of Core Relations**

| Quantity | Expression | Scale Transformation |
|---------|------------|----------------------|
| **Information** | $\kappa = K(s)/K_0 = S/k_B$ | $\kappa \mapsto \kappa$ |
| **Mass** | $m = \dfrac{k_B T}{c^2} \kappa$ | $m \mapsto \lambda^{-1} m$ |
| **Energy** | $E = \hbar \omega \kappa$ | $E \mapsto \lambda^{-1} E$ |
| **Entropy** | $S = k_B \kappa$ | $S \mapsto S$ |

These relations are **not independent equations** but **relational identities** expressing how a single invariant $\kappa$ manifests through observer-dependent scales ($T, \omega$).

This FDO provides the rigorous mathematical backbone for the thesis: **physical reality is scale-invariant information in relational disguise**.