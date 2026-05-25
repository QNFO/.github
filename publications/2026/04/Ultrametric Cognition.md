---
author: Rowan Brad Quni-Gudzinas
ORCID: 0009-0002-4317-5604
ISNI: 0000000526456062
title: Ultrametric Cognition
date: 2026-04-29
version: "0.11"
aliases:
  - Ultrametric Cognition
modified: 2026-04-29T11:34:42Z
---

# Ultrametric Cognition

**Author:** Rowan Brad Quni-Gudzinas
**Contact:** [rowan.quni@outlook.com](mailto:rowan.quni@outlook.com)
**ORCID:** [0009-0002-4317-5604](http://orcid.org/0009-0002-4317-5604)
**ISNI:** [0000000526456062](http://isni.org/isni/0000000526456062)
**DOI:** [10.5281/zenodo.19884970](http://doi.org/10.5281/zenodo.19884970)
**Date:** 2026-04-29
**Version:** 1.0

**Abstract**: Phenomenological time flows continuously; neural processing proceeds in discrete cycles. We resolve this formal contradiction by constructing the cognitive state space as a Bruhat–Tits tree $\mathcal{T}_p$ over $\mathbb{Q}_p$, where global consistency is the $1$-cocycle condition $\delta\omega = 0$, temporal sequence emerges from Page–Wootters conditioning on biological oscillator phases, and phenomenological continuity is the Monna map $\Phi: \mathbb{Z}_p \to [0,1]$—a many-to-one continuous surjection. From these axioms we derive four formal signatures—power-law reaction times, isosceles triplet geometries, clock–sequence dissociation, and projection uniformity—each with a complete inference procedure.

## 1. Introduction

Human temporal experience is Archimedean: it flows as an unbroken continuum. Neural processing is non-Archimedean: it proceeds in discrete cycles bounded by oscillatory phase (VanRullen & Koch 2003; Busch et al. 2009). Standard pacemaker-accumulator models (Treisman 1963; Gibbon et al. 1984) assume Archimedean geometry and cannot resolve this contradiction.

We construct a mathematical framework in which the contradiction is eliminated. The cognitive state space is the Bruhat–Tits tree $\mathcal{T}_p$. Consistency is $\delta\omega = 0$. Sequence emerges from Page–Wootters conditioning (Page & Wootters 1983). Phenomenological continuity is the Monna projection (Monna 1970; Anashin 2023). Each component is a standard mathematical object; the contribution is their assembly and the derivation of joint observational consequences.

## 2. Framework

### 2.1 Ultrametric State Space

**Definition 2.1** ($p$-adic absolute value). For $0 \neq x = p^{v_p(x)} \cdot a/b \in \mathbb{Q}$ with $p \nmid a,b$, $|x|_p = p^{-v_p(x)}$. $\mathbb{Q}_p$ is the completion of $\mathbb{Q}$ under $|\cdot|_p$. $\mathbb{Z}_p = \{x \in \mathbb{Q}_p : |x|_p \leq 1\}$.

**Theorem 2.2** (Strong triangle inequality). For $x,y \in \mathbb{Q}_p$,

$$|x+y|_p \leq \max(|x|_p, |y|_p),$$

with equality when $|x|_p \neq |y|_p$.

*Proof.* Let $m = v_p(x)$, $n = v_p(y)$, $m \leq n$. Write $x = p^m u$, $y = p^n v$ with $u,v \in \mathbb{Z}_p^\times$. Then $x+y = p^m(u + p^{n-m}v)$. When $n > m$, the bracket is a unit, so $|x+y|_p = p^{-m} = \max(|x|_p,|y|_p)$. When $m = n$, the sum may gain a factor of $p$, yielding the inequality. ∎

**Corollary 2.3** (Isosceles triangles). In any ultrametric space, for points $a,b,c$ with $d_{ab} \leq d_{bc} \leq d_{ca}$, necessarily $d_{bc} = d_{ca}$.

*Proof.* $d_{ca} \leq \max(d_{cb}, d_{ba}) = d_{bc}$; with $d_{bc} \leq d_{ca}$ by ordering, equality follows. ∎

**Definition 2.4** (Bruhat–Tits tree). $\mathcal{T}_p$ is the infinite regular tree of degree $p+1$ whose vertices correspond to closed balls in $\mathbb{Q}_p$ (Serre 1980). Fix root $v_0$. $\partial\mathcal{T}_p \cong \mathbb{P}^1(\mathbb{Q}_p)$.

**Proposition 2.5** (Tree-p-adic correspondence). Vertices $v,w$ corresponding to balls $B_{p^{-r}}(x)$, $B_{p^{-s}}(y)$ have lowest common ancestor at depth $k$, where $k$ is the largest integer with $|x-y|_p \leq p^{-k}$. Then $d_{\mathcal{T}}(v,w) = r+s-2k$.

*Proof.* Serre (1980, Ch. II); Gouvêa (1997, §5.4). ∎

**Axiom 2.6** (Cognitive state space). The cognitive state space is $V(\mathcal{T}_p)$. A cognitive state is a distribution $\rho: V(\mathcal{T}_p) \to [0,1]$, with logical content at the deepest supported vertex.

**Axiom 2.7** (Sensory boundary). Sensory input and motor output act on $\partial\mathcal{T}_p$.

### 2.2 Cocycle Coherence

**Definition 2.8** ($1$-cocycle). For an open cover $\{U_i\}$ of $\mathcal{T}_p$, a $1$-cochain is $\omega_{ij}: U_i \cap U_j \to \mathbb{R}$ with $\omega_{ij} = -\omega_{ji}$. The coboundary is $(\delta\omega)_{ijk} = \omega_{ij} + \omega_{jk} + \omega_{ki}$. $\omega$ is a $1$-cocycle iff $\delta\omega = 0$.

**Definition 2.9** (Dissonance functional). $\mathcal{D}(\omega) = \|\delta\omega\|^2 = \sum_{i,j,k} (\omega_{ij} + \omega_{jk} + \omega_{ki})^2$.

**Axiom 2.10** (Cocycle coherence). A cognitive state is globally coherent iff its local transition functions satisfy $\delta\omega = 0$. State updating is discrete gradient descent:

$$v_{t+1} = \underset{v \in \mathcal{N}(v_t)}{\arg\min} \; \mathcal{D}(\omega_v).$$

**Proposition 2.11** (Convergence to normal form). $\mathcal{D}(\omega(t)) \to 0$ as $t \to \infty$ along gradient descent trajectories from any initial state in a basin of attraction.

*Proof.* $\mathcal{D} \geq 0$ is a Lyapunov function: $d\mathcal{D}/dt = -\sum_{i,j} (\partial\mathcal{D}/\partial\omega_{ij})^2 \leq 0$, with equality only at $1$-cocycles. LaSalle’s invariance principle guarantees convergence. ∎

### 2.3 $p$-adic Diffusion

**Definition 2.12** (Vladimirov operator). For $\alpha > 0$,

$$(\Delta^\alpha f)(x) = \frac{1}{\Gamma_p(-\alpha)} \int_{\mathbb{Q}_p} \frac{f(y)-f(x)}{|y-x|_p^{1+\alpha}} \, d\mu(y),$$

with $\mu$ the normalised Haar measure (Vladimirov et al. 1994).

**Definition 2.13** ($p$-adic diffusion). $\partial_t u + D \Delta^\alpha u = 0$, $D > 0$.

**Theorem 2.14** (Survival probability). The fundamental solution satisfies $K(x,y,t) = t^{-1/\alpha} \Psi(|x-y|_p t^{-1/\alpha})$. Consequently,

$$P(T > t) \sim t^{-1/\alpha}, \qquad t \to \infty.$$

*Proof.* $\Delta^\alpha$ is homogeneous of degree $\alpha$: $\Delta^\alpha[f(\lambda^{-1}\,\cdot\,)] = \lambda^{-\alpha}(\Delta^\alpha f)(\lambda^{-1}\,\cdot\,)$. The Haar measure satisfies $d\mu(\lambda x) = \lambda\,d\mu(x)$. The equation is invariant under $x \mapsto \lambda x$, $t \mapsto \lambda^\alpha t$, $u \mapsto \lambda^{-1}u$. Setting $\lambda = t^{-1/\alpha}$ yields the scaling form. Integrating over a ball and extracting the leading asymptotic gives $P(T>t) \sim t^{-1/\alpha}$. ∎

**Corollary 2.15** (Power-law RT density). $f_{\text{RT}}(t) \sim t^{-(1+1/\alpha)}$, $t \to \infty$.

*Proof.* $f_{\text{RT}} = -dP(T>t)/dt \sim t^{-(1+1/\alpha)}$. ∎

### 2.4 Page–Wootters Sequence

**Definition 2.16** (Page–Wootters construction). Let $\mathcal{H} = \mathcal{H}_C \otimes \mathcal{H}_K$ with $\hat{H}_{\text{total}}|\Psi\rangle = 0$ (Page & Wootters 1983). For clock eigenstates $|\theta\rangle$ of $\hat{\Theta}$ on $\mathcal{H}_K$, the conditional conceptual state is

$$|\psi(\theta)\rangle = \frac{(\langle\theta| \otimes I_C)|\Psi\rangle}{\sqrt{\langle\Psi|(|\theta\rangle\langle\theta| \otimes I_C)|\Psi\rangle}}.$$

The sequence $\{|\psi(\theta_1)\rangle, |\psi(\theta_2)\rangle, \dots\}$ for ordered phases constitutes the emergent temporal sequence. This is a classical adaptation: $|\Psi\rangle$ encodes relational probabilities.

**Axiom 2.17** (Biological clock). $\mathcal{H}_K$ is instantiated by alpha (8–12 Hz) and theta (4–7 Hz) neural oscillations. $\theta \in S^1$ is the oscillator phase.

**Proposition 2.18** (Clock–sequence independence). Clock frequency $\nu$ and sequence length $n$ are independent parameters. Dissonance ($\delta\omega > 0$) increases $n$ (more gradient descent steps; Proposition 2.11) without altering $\nu$.

*Proof.* The clock subsystem $\mathcal{H}_K$ has intrinsic dynamics governed by its own Hamiltonian, independent of $\mathcal{H}_C$. Dissonance affects only $\mathcal{H}_C$ through $\mathcal{D}(\omega)$. ∎

### 2.5 Monna Projection

**Definition 2.19** (Monna map). For $x = \sum_{n=0}^\infty a_n p^n \in \mathbb{Z}_p$ with $a_n \in \{0,\dots,p-1\}$,

$$\Phi(x) = \sum_{n=0}^\infty a_n p^{-n-1} \in [0,1].$$

**Theorem 2.20** (Properties of $\Phi$).

1. **Lipschitz.** $|\Phi(x)-\Phi(y)| \leq |x-y|_p$.
2. **Surjectivity.** $\Phi(\mathbb{Z}_p) = [0,1]$.
3. **Many-to-one.** $\Phi^{-1}(y)$ is uncountable for almost every $y \in [0,1]$.

*Proof.* (1) $|x-y|_p = p^{-N} \implies |\Phi(x)-\Phi(y)| \leq \sum_{n=N}^\infty (p-1)p^{-n-1} = p^{-N}$. (2) Every $y \in [0,1]$ has a base-$p$ expansion $y = \sum b_n p^{-n}$; $\Phi(\sum b_{n+1}p^n) = y$. (3) Altering digit $a_N$ for any $N$ changes $x$ but produces at most a $p^{-N-1}$ change in $\Phi(x)$; the preimage of any interval contains uncountably many points. ∎

**Axiom 2.21** (Phenomenological projection). Phenomenological time $\tau(t)$ is the image of tree navigation under $\Phi$: for a continuous interpolation $\bar{v}(t)$ of visited vertices, $\tau(t) = \Phi(\bar{v}(t))$.

**Corollary 2.22** (Continuity from discreteness). $\tau(t)$ is continuous despite discrete tree dynamics.

*Proof.* $\Phi$ is continuous (Theorem 2.20.1); composition with a continuous interpolation preserves continuity. ∎

**Lemma 2.23** (Epistemic probability). Distinct tree paths $\gamma \neq \gamma'$ may satisfy $\Phi(\gamma) = \Phi(\gamma')$. The uniform measure on path space pushes forward to a measure on $[0,1]$ whose conditional distributions, given the projected image, are uniform on preimage classes. Apparent stochasticity at the projected level is branching entropy, not intrinsic randomness.

*Proof.* $\Phi$ is many-to-one (Theorem 2.20.3). Unique geodesics on a tree differ only by branch choice. The counting measure on path equivalence classes under $\Phi$ induces the stated conditional uniformity. ∎

## 3. Formal Signatures

### 3.1 Power-Law Reaction Times

**Theorem 3.1.** Under Axioms 2.6 and 2.10 with $p$-adic diffusion (Definition 2.13), the reaction-time density follows $f_{\text{RT}}(t) \sim t^{-(1+1/\alpha)}$ for $t > t_0$.

*Proof.* Corollary 2.15. ∎

**Corollary 3.2.** The RT distribution belongs to the Fréchet maximum domain of attraction (heavy-tailed). Euclidean drift-diffusion models produce exponential or inverse Gaussian RTs (Gumbel domain).

**Inference procedure 3.3.**

1. Fit Pareto and exponential models to empirical RTs via maximum likelihood.
2. Compute $\Delta\text{AIC} = \text{AIC}_{\text{exp}} - \text{AIC}_{\text{PL}}$. $\Delta\text{AIC} > 10$: strong evidence for power law.
3. Hill estimator $\hat{\alpha}_{\text{Hill}} = (m^{-1}\sum_{i=1}^m \ln X_{(n-i+1)}/X_{(n-m)})^{-1}$ for varying $m$; consistency supports the hypothesis (Clauset et al. 2009).

### 3.2 Isosceles Triplet Geometry

**Theorem 3.4.** For any three cognitive states with pairwise RTs, the sorted distances satisfy $D_{\text{mid}} = D_{\max}$ in the non-equilateral case. The base ratio $R = (D_{\text{mid}}-D_{\min})/D_{\min}$ satisfies $R > 0$.

*Proof.* Corollary 2.3. ∎

**Corollary 3.5.** Euclidean spaces produce $R \approx 0$ (equilateral tendency). Ultrametric spaces produce $R \gg 0$.

**Inference procedure 3.6.**

1. Extract all triplets from empirical RT or similarity data; sort pairwise distances; compute $R$.
2. Generate Euclidean null distribution: random vectors in $\mathbb{R}^n$, same dimensionality, compute $R$ for each triplet.
3. Mann–Whitney $U$ test (or permutation test) for rightward shift. $p < 0.05$ supports ultrametric structure.

### 3.3 Clock–Sequence Dissociation

**Theorem 3.7.** Under Axiom 2.17 and Proposition 2.18, injecting dissonance ($\delta\omega > 0$) produces: (i) $\text{PSE}_{\text{distractor}} > \text{PSE}_{\text{baseline}}$; (ii) $\nu_{\text{distractor}} = \nu_{\text{baseline}}$.

*Proof.* Dissonance requires additional gradient descent steps (Proposition 2.11), increasing sequence length $n$, which delays integration (PSE shift). Clock frequency is independent (Proposition 2.18). ∎

**Inference procedure 3.8.**

1. Temporal integration paradigm: cross-modal distractor vs. baseline.
2. Measure PSE and EEG alpha frequency simultaneously.
3. Paired $t$-tests: reject $H_0^{\text{PSE}}$ (shift detected); fail to reject $H_0^{\nu}$ (frequency unchanged).

### 3.4 Monna Uniformity

**Theorem 3.9.** Let $\{v_n\}$ be a mixing random walk on $\mathcal{T}_p$ and $\tau_n = \Phi(v_n)$. As $N \to \infty$, the empirical distribution of $\{\tau_n\}$ converges weakly to $\text{Uniform}[0,1]$.

*Proof.* $\Phi$ pushes the uniform measure on $\mathbb{Z}_p$ forward to Lebesgue measure on $[0,1]$. A mixing walk samples vertices with asymptotically uniform digit distributions; the continuous mapping theorem yields weak convergence. ∎

**Inference procedure 3.10.**

1. Project observed state sequence via $\Phi$.
2. Kolmogorov–Smirnov test against $\text{Uniform}[0,1]$.
3. Anderson–Darling test (greater tail sensitivity) as complement.

### 3.5 Joint Structure

The four signatures are not independent. Signatures 3.1 and 3.2 both derive from the ultrametric inequality (Corollary 2.3); Signature 3.3 follows from the Page–Wootters decomposition (Proposition 2.18); Signature 3.4 follows from the mixing properties of $\mathcal{T}_p$ under $\Phi$. A hierarchical Bayesian model with prior informed by the axiomatic structure (Section 2) and likelihood combining all four signatures yields a joint posterior over the ultrametric hypothesis.

## 4. Conclusion

We have axiomatically defined a cognitive architecture in which the state space is $\mathcal{T}_p$, coherence is $\delta\omega = 0$, sequence emerges from Page–Wootters conditioning, and phenomenological continuity is the Monna projection. The framework yields four formal signatures with complete inference procedures. The determination of whether this structure describes biological cognition is a question for empirical investigation.

---

## References

Anashin, V. (2023). Free choice in quantum theory: A $p$-adic view. *Entropy*, 25(5), 830.

Busch, N. A., Dubois, J., & VanRullen, R. (2009). The phase of ongoing EEG oscillations predicts visual perception. *Journal of Neuroscience*, 29(24), 7869–7876.

Clauset, A., Shalizi, C. R., & Newman, M. E. J. (2009). Power-law distributions in empirical data. *SIAM Review*, 51(4), 661–703.

DeWitt, B. S. (1967). Quantum theory of gravity. I. The canonical theory. *Physical Review*, 160(5), 1113–1148.

Friston, K., FitzGerald, T., Rigoli, F., Schwartenbeck, P., & Pezzulo, G. (2017). Active inference: A process theory. *Neural Computation*, 29(1), 1–49.

Giannakopoulos, B. (2026). The informational structure of time. *Medium*.

Gibbon, J., Church, R. M., & Meck, W. H. (1984). Scalar timing in memory. *Annals of the New York Academy of Sciences*, 423, 52–77.

Gouvêa, F. Q. (1997). *$p$-adic numbers: An introduction* (2nd ed.). Springer.

Karmarkar, U. R., & Buonomano, D. V. (2007). Timing in the absence of clocks: Encoding time in neural network states. *Neuron*, 53(3), 427–438.

Kochubei, A. N. (2001). *Pseudo-differential equations and stochastics over non-Archimedean fields*. Marcel Dekker.

Mézard, M., Parisi, G., & Virasoro, M. A. (1987). *Spin glass theory and beyond*. World Scientific.

Monna, A. F. (1970). *Analyse non-archimédienne*. Springer.

Page, D. N., & Wootters, W. K. (1983). Evolution without evolution: Dynamics described by stationary observables. *Physical Review D*, 27(12), 2885–2892.

Serre, J.-P. (1980). *Trees*. Springer.

Treisman, M. (1963). Temporal discrimination and the indifference interval: Implications for a model of the “internal clock.” *Psychological Monographs*, 77(13), 1–31.

Tse, P. U., Intriligator, J., Rivest, J., & Cavanagh, P. (2004). Attention and the subjective expansion of time. *Perception & Psychophysics*, 66(7), 1171–1189.

VanRullen, R., & Koch, C. (2003). Is perception discrete or continuous? *Trends in Cognitive Sciences*, 7(5), 207–213.

Vladimirov, V. S., Volovich, I. V., & Zelenov, E. I. (1994). *$p$-adic analysis and mathematical physics*. World Scientific.

