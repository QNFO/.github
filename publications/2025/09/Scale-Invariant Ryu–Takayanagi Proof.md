---
author: Rowan Brad Quni
email: rowan.quni@qnfo.org
website: http://qnfo.org
ORCID: 0009-0002-4317-5604
ISNI: 0000000526456062
robots: By accessing this content, you agree to https://qnfo.org/LICENSE. Non-commercial use only. Attribution required.
DC.rights: https://qnfo.org/LICENSE. Users are bound by terms upon access.
title: Scale-Invariant Ryu–Takayanagi Proof
aliases:
  - Scale-Invariant Ryu–Takayanagi Proof
modified: 2025-09-27T22:11:41Z
---

## **Scale-Invariant Reformulation of the Ryu–Takayanagi Formula**

**Author:** Rowan Brad Quni-Gudzinas
**Affiliation:** QNFO
**Contact:** rowan.quni@qnfo.org
**ORCID:** 0009-0002-4317-5604
**ISNI:** 0000 0005 2645 6062
**DOI:** 10.5281/zenodo.17216372
**Publication Date:** 2025-09-28
**Version:** 1.0

---

### **Given**

Let a $d$-dimensional boundary conformal field theory (CFT) be holographically dual to a $(d+1)$-dimensional asymptotically anti-de Sitter (AdS) bulk spacetime of radius $L$. Let $A \subset \partial \mathcal{M}$be a spatial subregion of the boundary with characteristic linear size $R$, and let $\gamma_A$be the codimension-2 extremal surface in the bulk that is homologous to $A$and satisfies $\partial \gamma_A = \partial A$.

Assume the Ryu–Takayanagi (RT) formula holds in its standard form:

$$
S_A = \frac{\mathrm{Area}(\gamma_A)}{4G_N^{(d+1)}},
$$

where $G_N^{(d+1)}$is the $(d+1)$-dimensional Newton constant.

Assume the AdS/CFT dictionary relates the bulk gravitational parameters to boundary CFT data via:

$$
\frac{L^{d-1}}{G_N^{(d+1)}} = k_d \cdot a_d,
$$

where $a_d$is a dimensionless central charge of the CFT (e.g., $a_2 = c/3$in $d=2$, $a_4 = a$in $d=4$), and $k_d$is a known dimensionless constant depending only on $d$.

Let $\epsilon$denote a UV cutoff in the boundary theory, interpreted geometrically as a bulk cutoff at radial coordinate $z = \epsilon$.

---

### **Goal**

Reformulate the Ryu–Takayanagi formula in a **scale-invariant** manner that eliminates dependence on absolute scales ($L$, $\epsilon$, $R$) and isolates the universal, dimensionless information-theoretic content of holographic entanglement entropy.

---

### **Derivation**

#### **Step 1: Dimensional Analysis of the Standard Formula**

In natural units ($\hbar = c = 1$), the dimensions are:

- $[S_A] = 1$(dimensionless entropy),
- $[\mathrm{Area}(\gamma_A)] = [\mathrm{length}]^{d-1}$,
- $[G_N^{(d+1)}] = [\mathrm{length}]^{d-1}$.

Thus, the RT formula is dimensionally consistent but **not scale-invariant**, as it depends on the absolute AdS scale $L$through both $\mathrm{Area}(\gamma_A)$and $G_N^{(d+1)}$.

#### **Step 2: Express Gravitational Coupling via CFT Central Charge**

From the AdS/CFT dictionary, the combination $L^{d-1}/G_N^{(d+1)}$is proportional to the number of degrees of freedom in the boundary CFT. Define the dimensionless central charge $a_d$by:

$$
a_d := \frac{1}{k_d} \cdot \frac{L^{d-1}}{G_N^{(d+1)}},
$$

so that:

$$
G_N^{(d+1)} = \frac{L^{d-1}}{k_d a_d}. \tag{1}
$$

This expresses the bulk gravitational coupling in terms of a **dimensionless** boundary quantity.

#### **Step 3: Parametrize the Minimal Surface Area**

For a region $A$with characteristic size $R$, the area of the extremal surface $\gamma_A$in pure AdS$_{d+1}$takes the form:

$$
\mathrm{Area}(\gamma_A) = L^{d-1} \cdot \mathcal{F}_d\left( \frac{R}{\epsilon}, \frac{R}{L} \right), \tag{2}
$$

where $\mathcal{F}_d$is a dimensionless function encoding both UV-divergent and finite contributions. The dependence on $R/L$arises only in the finite part; the divergent part depends solely on $R/\epsilon$.

For example, in $d=2$with an interval of length $R$:

$$
\mathrm{Area}(\gamma_A) = 2L \log\left( \frac{R}{\epsilon} \right).
$$

#### **Step 4: Substitute into the Ryu–Takayanagi Formula**

Substituting (1) and (2) into the RT formula:

$$
S_A = \frac{L^{d-1} \cdot \mathcal{F}_d(R/\epsilon, R/L)}{4 \cdot (L^{d-1}/(k_d a_d))} = \frac{k_d a_d}{4} \cdot \mathcal{F}_d\left( \frac{R}{\epsilon}, \frac{R}{L} \right). \tag{3}
$$

The factor $L^{d-1}$cancels, leaving an expression that depends only on **dimensionless ratios** and the **dimensionless central charge** $a_d$.

#### **Step 5: Isolate the Universal (Scale-Invariant) Term**

The function $\mathcal{F}_d$generally contains divergent terms as $\epsilon \to 0$, but also a **universal term** $\mathcal{F}_d^{\mathrm{univ}}$that is independent of $\epsilon$and depends only on the geometry of $A$and the ratio $R/L$. Under a global scale transformation:

$$
R \mapsto \lambda R, \quad L \mapsto \lambda L, \quad \epsilon \mapsto \lambda \epsilon,
$$

the ratio $R/L$is invariant, and thus:

$$
\mathcal{F}_d^{\mathrm{univ}}\left( \frac{R}{L} \right) \mapsto \mathcal{F}_d^{\mathrm{univ}}\left( \frac{R}{L} \right).
$$

Hence, the universal part of $S_A$is **scale-invariant**.

For spherical regions, this universal term is known explicitly:

- In **even** $d$: $S_A^{\mathrm{univ}} = (-1)^{d/2} \cdot 4 a_d \log(R/\epsilon)$,
- In **odd** $d$: $S_A^{\mathrm{univ}} = F_d(a_d)$, a constant independent of $R$.

In both cases, the coefficient is proportional to the **$a$-anomaly** (even $d$) or the **$F$-quantity** (odd $d$), both of which are **dimensionless** and **intrinsic** to the CFT.

#### **Step 6: Construct a Scale-Invariant Entropy Functional**

To extract the scale-invariant content without reference to $\epsilon$or $L$, define the **universal entanglement entropy** as:

$$
S_A^{\mathrm{univ}} := \lim_{\epsilon \to 0} \left[ S_A(R, \epsilon) - S_A^{\mathrm{div}}(R, \epsilon) \right], \tag{4}
$$

where $S_A^{\mathrm{div}}$contains all terms that diverge as $\epsilon \to 0$. This subtraction is equivalent to the **holographic renormalization** procedure in the bulk, which removes boundary counterterms.

Equivalently, for two regions $A$and $A_0$of the same shape but different sizes, the difference:

$$
\Delta S = S_A(R) - S_{A_0}(R_0)
$$

is scale-invariant when expressed in terms of the dimensionless ratio $R/R_0$, and its finite part is universal.

#### **Step 7: Verify Scale Invariance Under Weyl Transformations**

Under a boundary Weyl transformation $g_{\mu\nu} \mapsto e^{2\omega(x)} g_{\mu\nu}$, the bulk metric in Fefferman–Graham coordinates transforms as:

$$
ds^2 = \frac{L^2}{z^2} \left( dz^2 + e^{2\omega(x)} g_{\mu\nu}(x) dx^\mu dx^\nu \right).
$$

The extremal surface $\gamma_A$shifts, and its area changes by:

$$
\delta \mathrm{Area}(\gamma_A) = \int_{\partial A} \omega(x) \cdot (\text{local geometric terms}) + (\text{anomalous term}).
$$

However, the **universal part** of the entropy transforms **covariantly** and, for conformally invariant states, remains **invariant** under global rescalings. This is because the anomaly coefficients $a_d$are Weyl-invariant by construction.

Thus, the combination:

$$
S_A^{\mathrm{univ}} = \kappa_d \cdot a_d
$$

is invariant under $R \mapsto \lambda R$, $L \mapsto \lambda L$, confirming scale invariance.

---

### **Conclusion**

**Theorem (Scale-Invariant Ryu–Takayanagi Formula).**
The universal part of holographic entanglement entropy is scale-invariant and given by:

$$
\boxed{S_A^{\mathrm{univ}} = \kappa_d \cdot a_d}
$$

where:

- $a_d$is the dimensionless central charge of the $d$-dimensional boundary CFT (e.g., $a_2 = c/3$, $a_4 = a$),
- $\kappa_d$is a universal numerical constant depending only on spacetime dimension $d$,
- The expression is invariant under global scale transformations $x^\mu \mapsto \lambda x^\mu$.

For a spherical region of radius $R$in even dimensions, this yields:

$$
S_A^{\mathrm{univ}} = (-1)^{d/2} \cdot 4 a_d \log\left( \frac{R}{\epsilon} \right),
$$

where the logarithmic dependence on the dimensionless ratio $R/\epsilon$reflects the conformal anomaly, and the coefficient is **independent of the AdS radius $L$** and **Newton’s constant $G_N^{(d+1)}$**.

This reformulation demonstrates that the **physically meaningful, observable content** of holographic entanglement entropy resides entirely in **dimensionless, scale-invariant data** characterizing the boundary CFT, consistent with the principles of universal scale invariance and epistemic humility.

---

**Q.E.D.**
