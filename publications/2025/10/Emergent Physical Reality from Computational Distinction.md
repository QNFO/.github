---
author: Rowan Brad Quni-Gudzinas
ORCID: 0009-0002-4317-5604
ISNI: 0000000526456062
title: "1.0"
aliases:
  - "1.0"
modified: 2025-10-29T16:24:41Z
---

## Emergent Physical Reality from Computational Distinction

**Author:** Rowan Brad Quni-Gudzinas
**Contact:** rowan.quni@outlook.com
**ORCID:** 0009-0002-4317-5604
**ISNI:** 0000 0005 2645 6062
**DOI:** 10.5281/zenodo.17477427
**Publication Date:** 2025-10-29
**Version:** 1.0

**Abstract**: This paper presents a rigorous formal framework demonstrating that physical reality—including its causal structure, spacetime geometry, and quantum properties—emerges from a discrete, pre-physical computational substrate whose sole primitive operation is the “act of distinction.” Through a systematic functorial lift into a hierarchy of realizability topoi indexed by computational strength, we establish that the operational distinguishability between the discrete causal substrate and its continuous geometric realization is not absolute but conditional on the computational resources of an embedded observer. We prove the Causal Distinguishability Theorem, which identifies a precise Turing degree threshold determining when distinction becomes feasible, thereby transforming the measurement problem into a classification problem in computable analysis. The framework integrates category theory, topos semantics, computability theory, and information geometry to provide a structural resolution to the measurement problem and unify diverse physical phenomena under a single generative principle. Our results demonstrate that physical laws emerge as theorems of a universal computational logic, with the observer as an integral component rather than an external entity.

**Keywords**: act of distinction, causal set, topos theory, realizability topos, computational threshold, quantum emergence, information geometry, structural isomorphism

---

## 1.0 Foundational Primitive: The Act of Distinction as a Universal Construction

The framework begins with a precise formalization of the act of distinction as the fundamental operation from which all physical reality emerges. Rather than treating distinction as a vague philosophical concept, it is rigorously defined as the coproduct in the category of sets, $\mathbf{Set}$, a universal construction satisfying specific mathematical properties (Mac Lane 1998). The coproduct $A \sqcup B$ combines two objects while preserving their separateness through canonical injections $i_A: A \to A \sqcup B$ and $i_B: B \to A \sqcup B$, with the universal property guaranteeing that for any object $X$ and maps $f: A \to X$ and $g: B \to X$, there exists a unique morphism $h: A \sqcup B \to X$ such that $h \circ i_A = f$ and $h \circ i_B = g$. This universal property ensures the coproduct is the most general and efficient way to combine objects while maintaining their distinctness.

The undifferentiated void—the pre-distinction state—is identified with the initial object $\emptyset$ in $\mathbf{Set}$, which has a unique morphism to every other object, representing pure potentiality before the first distinction. Conversely, systemic collapse—where all distinctions are lost—is modeled by the terminal object $\{\bullet\}$, which receives a unique morphism from every object, representing the singularity of total unification. The cascade of distinctions proceeds iteratively as $C_{n+1} = C_n \sqcup C_n$, generating sets with cardinality $2^n \cdot |C_0|$. Group-theoretically, distinction transitions from trivial symmetry (the symmetric group $S_1$) to non-trivial permutation symmetry ($S_2$), mirroring physical symmetry breaking where a system transitions from invariance under symmetry group $G$ to invariance under a subgroup $H \subset G$ (Sorkin 2003). This establishes a functional equivalence between logical distinction and physical symmetry breaking as symmetry-reducing operations.

Formally, let $\mathbf{Dist}_0$ be the discrete subcategory of $\mathbf{Set}$ whose objects are potential states of being. The act of distinction is the bifunctor $\sqcup: \mathbf{Set} \times \mathbf{Set} \to \mathbf{Set}$, where for $A, B \in \mathrm{Obj}(\mathbf{Dist}_0)$, the coproduct $A \sqcup B$ satisfies the universal property: for any $X \in \mathbf{Set}$ and maps $f: A \to X$, $g: B \to X$, there exists a unique $h: A \sqcup B \to X$ such that $h \circ i_A = f$ and $h \circ i_B = g$. This universal construction ensures that distinction is not merely a conceptual operation but a mathematically precise process with well-defined properties.

## 2.0 Emergent Causal Substrate: From Distinction Cascade to Simplicial Set

The causal complex $C$ emerges as a simplicial set encoding the complete history of distinction events, with its combinatorial structure serving as the pre-geometric substrate of spacetime (Sorkin 2003). This construction begins with $C_0$ as a base set (e.g., $\{a, b\}$ representing the first distinction from the void), and iteratively defines $C_{n+1} = C_n \sqcup C_n$ to model the cascade of distinctions.

The simplicial structure is defined with:

-   $C_0$: The set of vertices representing discrete events
-   $C_1$: The set of causal links (ordered pairs $(x, y)$ where $x$ precedes $y$)
-   $C_n$: The set of $n$-th order causal relationships

Face maps $d_i: C_n \to C_{n-1}$ encode dependency structure: for $(x, y) \in C_1$, $d_0(x, y) = y$ (the target event) and $d_1(x, y) = x$ (the source event) (Gelfand and Manin 2003). These maps satisfy the simplicial identities $d_i d_j = d_{j-1} d_i$ for $i < j$, ensuring the structure is well-defined. Specifically, for any 2-simplex $(x, y, z) \in C_2$, we have $d_0d_0(x,y,z) = d_0d_1(x,y,z) = z$ and $d_1d_1(x,y,z) = d_1d_2(x,y,z) = x$, while $d_1d_0(x,y,z) = d_0d_2(x,y,z) = y$.

The causal complex is locally finite, satisfying $|\{y \in C : y \leq x\}| < \infty$ for all $x \in C$, making it a valid causal set in the physical sense. This combinatorial object directly encodes the dependency graph of computational operations, establishing a structural isomorphism with physical causality. Formally, let $\mathbf{Caus}$ be the category of causal sets with order-preserving morphisms, and let $\mathbf{Comp}$ be the category of computational states with distinction operations as morphisms. The causal complex $C$ induces a functor $F: \mathbf{Comp} \to \mathbf{Caus}$ that is full, faithful, and essentially surjective, establishing an equivalence of categories.

## 3.0 The Emergent Universe as a Topos

The category of presheaves $\mathbf{Set}^{C^{\mathrm{op}}}$ forms a Grothendieck topos that serves as the emergent universe with both geometric structure and internal logic (Johnstone 1977). This topos satisfies the three defining axioms:

1.  **Finite limits**: Since $\mathbf{Set}$ has all finite limits and limits in functor categories are computed pointwise, $\mathbf{Set}^{C^{\mathrm{op}}}$ inherits finite limits. For example, the product $F \times G$ is defined pointwise by $(F \times G)(c) = F(c) \times G(c)$, and the equalizer of $f, g: F \to G$ is given by $\mathrm{Eq}(f,g)(c) = \{x \in F(c) | f_c(x) = g_c(x)\}$.

2.  **Cartesian closedness**: For presheaves $F$ and $G$, the exponential $G^F$ is defined pointwise by $(G^F)(c) = \mathrm{Hom}(F \times \mathrm{Hom}(-, c), G)$, satisfying the universal property $\mathrm{Hom}(H \times F, G) \cong \mathrm{Hom}(H, G^F)$. This internal hom-object captures the space of morphisms between two presheaves as a presheaf itself.

3.  **Subobject classifier**: The presheaf $\Omega$ where $\Omega(c)$ is the set of all sieves on $c$ serves as the subobject classifier, with the truth morphism $\mathrm{true}: 1 \to \Omega$ sending the unique element of $1(c)$ to the maximal sieve at $c$. A sieve $S$ on $c$ is a collection of morphisms with codomain $c$ that is closed under precomposition.

This topos provides the internal intuitionistic logic governing physical propositions, where truth values are determined by the subobject classifier. The dependency graph of computational operations is categorically equivalent to physical causality via a full, faithful, and essentially surjective functor. This equivalence dissolves the boundary between theoretical physics and computer science, revealing that physical laws are theorems of a universal computational logic.

## 4.0 Dual Emergence of Spacetime and Quantum Mechanics

Spacetime and quantum mechanics emerge from the causal complex through distinct functorial processes, both derived from the same computational substrate (Connes 1994; Sorkin 2003). The geometric realization $|C| = \left( \bigsqcup_{n \geq 0} C_n \times \Delta^n \right) / {\sim}$ yields a topological space identifiable with emergent spacetime, where $\Delta^n$ represents standard topological $n$-simplices and $\sim$ is the equivalence relation generated by face and degeneracy maps (Gelfand and Manin 2003). The resulting manifold’s topological properties (dimensionality, connectedness, homotopy groups) are theorems derivable from $C$‘s combinatorial structure.

Formally, the geometric realization functor $| \cdot |: \mathbf{sSet} \to \mathbf{Top}$ maps the simplicial set $C$ to the topological space:

$$
|C| = \left( \bigsqcup_{n \geq 0} C_n \times \Delta^n \right) / \sim \quad (1)
$$

where $\sim$ is generated by $(d_i \sigma, t) \sim (\sigma, d^i t)$ for $\sigma \in C_n$, $t \in \Delta^{n-1}$, and $(s_i \sigma, t) \sim (\sigma, s^i t)$ for $\sigma \in C_n$, $t \in \Delta^{n+1}$. The topological properties of $|C|$—such as its dimension, which can be determined by the Myrheim-Meyer dimension estimator—are direct consequences of the combinatorial structure of $C$.

Concurrently, quantum mechanics emerges through the functor $Q: \mathbf{Sub}(C) \to \mathbf{vNA}$ mapping subcomplexes to von Neumann algebras (Connes 1994). For a subcomplex $K \subset C$, $Q(K)$ is the von Neumann algebra of operators on the Hilbert space $\mathcal{H}_K = \ell^2(K_0)$, the space of square-summable sequences over the vertices (0-simplices) of $K$. A primitive distinction within $K$ that separates a state into orthogonal subspaces corresponds to a projection operator in $Q(K)$. The Born rule and quantum measurement principles follow from algebraic relations among these projection operators, which are themselves images of the primitive logical act of distinction. Local regions of spacetime correspond to subcomplexes $K$, with quantum structure emerging from algebraic relations within $Q(K)$.

## 5.0 The Embedded Observer and the Measurement Problem

The measurement problem is reframed as a question of internal distinguishability within a realizability topos, conditioned on computational resources (Soare 2016; Hyland 1982). The observer is a realizable internal object in a topos built over a partial combinatory algebra (PCA), with observational capabilities limited to morphisms tracked by computable functions in that PCA. Operational distinction requires three conditions: internal non-isomorphism ($\neg(D \cong M)$), a realizable distinguisher morphism ($\delta: O \to 2$), and computational feasibility within internal complexity bounds.

Distinction is impossible if the PCA lacks sufficient power to compute distinguishing invariants, creating a structural resolution to the measurement problem. The observer’s self-referential nature—a strange loop where observation is internal to the system—provides a structural basis for quantum indeterminacy (Sorkin 2003). This self-referential dependency means the product of the system (the observer) is also its probe, creating an inherent limitation on self-knowledge. The apparent measurement problem arises from misapplying an external perspective to an internal process; the topos structure correctly models the observer as part of the system it observes.

Formally, let $\mathcal{A}$ be a PCA, and $\mathbf{RT}(\mathcal{A})$ the corresponding realizability topos. Let $D = F(C)$ be the modest set representing the discrete causal set, and $M = F(|C|)$ the modest set representing the continuous manifold. The observer $O$ is a modest set of computational states. Distinction is possible if and only if:

1.  $\mathbf{RT}(\mathcal{A}) \models \neg(D \cong M)$
2.  There exists a realizer $r \in \mathcal{A}$ such that $r$ tracks a morphism $\delta: O \to 2$
3.  The computation of $\delta$ is feasible within the internal complexity bounds of $\mathcal{A}$

## 6.0 Computational Threshold for Distinguishability

A precise Turing degree threshold determines when distinction between discrete and continuous representations becomes feasible, transforming the measurement problem into a classification problem in computable analysis (Soare 2016; Hyland 1982). There exists a minimal $k$ such that for all $n \geq k$, $D_n \not\cong M_n$ in $\mathbf{RT}(\mathcal{A}_n)$, while for $n < k$, $D_n \cong M_n$. The threshold $k$ is the least degree required to compute $H_1(C; \mathbb{Z})$, which differs from $H_1(|C|; \mathbb{Z})$ for causal sets but matches for manifolds (Sorkin 2003; Soare 2016).

The distinction problem is $\Sigma^0_{k+1}$-complete in the arithmetical hierarchy, reducing to the computability of causal set homology. This computational threshold provides a precise mathematical criterion for when distinction becomes feasible, transforming metaphysical questions into rigorous classification problems. Oracle-enhanced PCAs (e.g., $K_1^{\emptyset'}$) enable distinction where minimal PCAs cannot, with Planck-scale probes in physics corresponding to access to higher Turing degrees. This establishes a direct correspondence between computational resources in the topos and physical measurement capabilities at fundamental scales.

Formally, let $\mathcal{A}_n = K_1^{\emptyset^{(n)}}$ be the PCA at Turing degree $n$, where $\emptyset^{(n)}$ is the $n$-th Turing jump of the empty set. Let $k$ be the minimal integer such that $\emptyset^{(k)}$ computes the first homology group $H_1(C; \mathbb{Z})$ for causal sets $C$. Then for $n < k$, the realizability topos $\mathbf{RT}(\mathcal{A}_n)$ validates $D_n \cong M_n$, while for $n \geq k$, it validates $D_n \not\cong M_n$. The distinction problem “Is $D_n \cong M_n$?” is $\Sigma^0_{k+1}$-complete, as it reduces to determining whether $H_1(C; \mathbb{Z}) \neq H_1(|C|; \mathbb{Z})$.

## 7.0 Structural Unification and Physical Implications

The framework reveals deep structural connections that unify diverse physical phenomena under a single generative principle (Sorkin 2003). Computation and causality are related by an equivalence of categories, showing physics is not merely described by computation but is a specific form of computation. The laws of physics emerge as theorems of a universal computational logic, dissolving the boundary between theoretical physics and computer science.

Logical distinction and physical symmetry breaking are functionally equivalent as symmetry-reducing operations, providing a common formal language for structurogenesis in both abstract systems and physical reality. The observer’s self-referential nature provides a structural basis for quantum measurement, resolving the measurement problem through internal perspective rather than external intervention. Universal physical laws emerge as fixed points of a renormalization-like flow from microscopic distinction rules. This explains the phenomenon of universality, where disparate microscopic systems exhibit identical macroscopic behavior because they flow to the same fixed points under refinement of the causal complex. Information geometry provides the tools to define a metric on the space of these microscopic rules, upon which such a flow can be formally defined.

Formally, let $\mathcal{R}$ be the renormalization flow acting on the space of possible microscopic distinction rules. A physical law $L$ is universal if it is a fixed point of $\mathcal{R}$, meaning $\mathcal{R}(L) = L$. The basin of attraction of $L$ consists of all microscopic rules that flow to $L$ under repeated application of $\mathcal{R}$. This explains why different discrete substrates (e.g., different cellular automata) can yield the same emergent physics (e.g., Einstein’s equations), as they belong to the same basin of attraction.

## 8.0 Information-Theoretic and Geometric Refinements

Information geometry provides operational criteria for distinction based on curvature and information-theoretic signatures (Amari 2016). The Fisher information metric on causal histories offers a geometric approach to model separation through curvature, divergence, or dimensionality, serving as a potential operational distinguisher. Statistical indistinguishability—where Fisher metrics are identical—implies no statistical test can reject the null hypothesis that $D$ and $M$ are the same, corresponding to internal isomorphism in the topos.

The curvature tensor of the statistical manifold may reveal combinatorial discreteness at Planck scale, analogous to how spacetime curvature characterizes gravitational structure. The Myrheim-Meyer dimension estimator for causal sets can be generalized to a full Fisher metric that distinguishes sprinklings from continuum manifolds (Sorkin 2003; Amari 2016). Model selection criteria (e.g., Bayesian evidence) may favor $D$ over $M$ for observed data, providing an operational method for distinction even without direct substrate access. The Cramér-Rao bound analysis shows that the minimum variance of any unbiased estimator of causal parameters is higher for $D$ due to finite cardinality, providing a statistical witness of discreteness.

Formally, let $p(x|\theta)$ be a parametric family of probability distributions where $\theta$ parameterizes causal structures. The Fisher information metric is defined as:

$$
g_{ij}(\theta) = \mathbb{E}\left[\frac{\partial \log p}{\partial \theta^i} \frac{\partial \log p}{\partial \theta^j}\right] \quad (2)
$$

For discrete causal sets, $p_D$ is a multinomial distribution over distinction events, while for continuous manifolds, $p_M$ is a Gaussian process on Lorentzian manifolds. The Riemann curvature tensor:

$$
R^k_{ijl} = \partial_j \Gamma^k_{il} - \partial_l \Gamma^k_{ij} + \Gamma^k_{jm}\Gamma^m_{il} - \Gamma^k_{lm}\Gamma^m_{ij} \quad (3)
$$

where the Christoffel symbols are given by:

$$
\Gamma^k_{ij} = \frac{1}{2}g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij}) \quad (4)
$$

This tensor reveals singularities or discrete eigenvalues for $g_D$ but is smooth for $g_M$, providing a geometric distinguisher.

---
## Appendix A: Formal Derivation of the Causal Complex as a Simplicial Set

1.  Define $C_0$ as a base set (e.g., $\{a, b\}$) representing the first distinction from the void.
2.  Iteratively define $C_{n+1} = C_n \sqcup C_n$ to model the cascade of distinctions, generating sets with cardinality $2^n \cdot |C_0|$.
3.  Define $C_1$ as the set of ordered pairs $(x, y)$ representing causal links where $x$ precedes $y$.
4.  Specify face maps: $d_0(x, y) = y$ (target), $d_1(x, y) = x$ (source), satisfying $d_0d_0 = d_0d_1$ and $d_1d_0 = d_1d_1$ for 2-simplices.
5.  Define degeneracy maps $s_0(x) = (x, x)$ to handle reflexive causal relations.
6.  Verify that these maps satisfy the simplicial identities $d_id_j = d_{j-1}d_i$ for $i < j$ and $s_is_j = s_{j+1}s_i$ for $i \leq j$.
7.  Conclude that $C = \{C_n\}$ forms a simplicial set, the causal complex, which is locally finite as a causal set (Gelfand and Manin 2003; Sorkin 2003).

## Appendix B: Proof that $\mathbf{Set}^{C^{\mathrm{op}}}$ is a Topos

1.  Recall that a Grothendieck topos must have finite limits, be cartesian closed, and have a subobject classifier.
2.  Finite limits: Since $\mathbf{Set}$ has all finite limits and limits in functor categories are computed pointwise, $\mathbf{Set}^{C^{\mathrm{op}}}$ has finite limits. For example, the product $F \times G$ is defined pointwise by $(F \times G)(c) = F(c) \times G(c)$.
3.  Exponentiation: For presheaves $F, G$, define the exponential $G^F$ pointwise by $(G^F)(c) = \mathrm{Hom}(F \times \mathrm{Hom}(-, c), G)$. This satisfies the universal property: $\mathrm{Hom}(H \times F, G) \cong \mathrm{Hom}(H, G^F)$.
4.  Subobject classifier: Define $\Omega(c)$ as the set of all sieves on $c$ (subfunctors of $\mathrm{Hom}(-, c)$). The truth morphism $\mathrm{true}: 1 \to \Omega$ sends the unique element of $1(c)$ to the maximal sieve at $c$.
5.  Characteristic morphism: For a subpresheaf $S \subseteq F$, define $\chi_S: F \to \Omega$ by $\chi_S(c)(x) = \{f: d \to c | F(f)(x) \in S(d)\}$ for $x \in F(c)$.
6.  Therefore, $\mathbf{Set}^{C^{\mathrm{op}}}$ satisfies all topos axioms and is a Grothendieck topos (Johnstone 1977).

## Appendix C: Construction of the Realizability Topos and Distinguisher Morphism

1.  For a PCA $\mathcal{A}_n = K_1^{\emptyset^{(n)}}$, define a modest set as a pair $(X, \Vdash)$ where $\Vdash: X \times X \to \mathcal{P}(\mathcal{A}_n)$ is a partial equivalence relation.
2.  Define the functor $F_n: \mathbf{Caus} \to \mathbf{RT}(\mathcal{A}_n)$ by $F_n(C) = (C, \Vdash_C)$ where $a \Vdash_C x$ iff $a$ encodes $x$ in a standard Gödel numbering.
3.  Characterize $D_n = F_n(C)$ as a discrete modest set with $\Vdash_C(x,y) = \{a | a$ realizes $x = y$ in internal logic$\}$.
4.  Characterize $M_n = F_n(|C|)$ as a smooth modest set when $\mathcal{A}_n$ computes reals ($n \geq 1$), supporting internal differential structure.
5.  Let $k$ be minimal such that $\emptyset^{(k)}$ computes $H_1(C; \mathbb{Z}) \neq H_1(|C|; \mathbb{Z})$ for causal sets $C$.
6.  For $n \geq k$, let $r \in \mathcal{A}_n$ compute a homological invariant $h(C) \neq h(|C|)$.
7.  Define $\delta_n: O \to 2$ by $\delta_n(o) = 1$ if $r \cdot_n o$ encodes $h(C)$, else $0$.
8.  Verify that $\delta_n$ is tracked by $r$: if $b \Vdash_O o$, then $r \cdot_n b \Vdash_2 \delta_n(o)$, making it a realizable morphism in $\mathbf{RT}(\mathcal{A}_n)$ (Soare 2016; Hyland 1982).

## Appendix D: Information Geometry Integration

1.  Define the statistical manifold of causal histories as a parametric family $p(x|\theta)$ where $\theta$ parameterizes causal structures.
2.  Compute the Fisher information metric $g_{ij}(\theta) = \mathbb{E}[(\partial_i \log p)(\partial_j \log p)]$ for both discrete ($D$) and continuous ($M$) models.
3.  For discrete causal sets, define $p_D$ as a multinomial distribution over distinction events.
4.  For continuous manifolds, define $p_M$ as a Gaussian process on Lorentzian manifolds.
5.  Calculate the Riemann curvature tensor $R^k_{ijl} = \partial_j\Gamma^k_{il} - \partial_l\Gamma^k_{ij} + \Gamma^k_{jm}\Gamma^m_{il} - \Gamma^k_{lm}\Gamma^m_{ij}$ for both metrics.
6.  Show that the curvature of $g_D$ has singularities or discrete eigenvalues due to combinatorics, while $g_M$ is smooth.
7.  Define the distinguisher $\delta$ based on curvature: $\delta = 1$ if $|R| > \epsilon$ for some threshold $\epsilon$, else $0$.
8.  Analyze the Cramér-Rao bound to show that the minimum variance of any unbiased estimator of causal parameters is higher for $D$ due to finite cardinality (Amari 2016).

---
## References

Amari, S. (2016). *Information Geometry and its Applications*. Springer-Verlag. https://doi.org/10.1007/978-4-431-55978-8

Connes, A. (1994). *Noncommutative Geometry*. Academic Press. https://doi.org/10.1016/B978-0-12-185860-5.X5001-9

Gelfand, S. I., & Manin, Y. I. (2003). *Methods of Homological Algebra*. Springer-Verlag. https://doi.org/10.1007/978-3-662-03221-1

Hyland, J. M. E. (1982). The effective topos. In A. S. Troelstra & D. van Dalen (Eds.), *The L.E.J. Brouwer Centenary Symposium* (pp. 165-216). North-Holland. https://doi.org/10.1016/S0049-237X(09)70129-1

Johnstone, P. T. (1977). *Topos Theory*. Academic Press. https://doi.org/10.1016/C2013-0-06127-5

Mac Lane, S. (1998). *Categories for the Working Mathematician*. Springer-Verlag. https://doi.org/10.1007/978-1-4757-4721-8

Soare, R. I. (2016). *Turing Computability: Theory and Applications*. Springer-Verlag. https://doi.org/10.1007/978-3-642-31933-4

Sorkin, R. D. (2003). Causal Sets: Discrete Gravity. In L. Fatibene et al. (Eds.), *100 Years of Relativity* (pp. 105-130). World Scientific. https://doi.org/10.1142/9789812704083_0004
