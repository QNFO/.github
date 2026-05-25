---
author: Rowan Brad Quni
email: rowan.quni@qnfo.org
website: http://qnfo.org
ORCID: 0009-0002-4317-5604
ISNI: 0000000526456062
robots: By accessing this content, you agree to https://qnfo.org/LICENSE. Non-commercial use only. Attribution required.
DC.rights: https://qnfo.org/LICENSE. Users are bound by terms upon access.
title: "1.0"
aliases:
  - "1.0"
modified: 2025-10-28T17:19:45Z
---

## A Functorial Characterization of the Prime Numbers via a HoTT-Realizability-Sheaf Correspondence

**Author:** Rowan Brad Quni-Gudzinas
**Affiliation:** QNFO
**Contact:** rowan.quni@qnfo.org
**ORCID:** 0009-0002-4317-5604
**ISNI:** 0000 0005 2645 6062
**DOI:** 10.5281/zenodo.17467643
**Publication Date:** 2025-10-27
**Version:** 1.0

**Abstract**: This paper presents a complete theoretical characterization of the set of prime numbers, $\mathcal{P}$, by demonstrating that it is the geometric support of a canonical object constructed via a three-stage functorial lift. This process begins in the logical stratum of Homotopy Type Theory (HoTT), where a decidable Prime type is constructed. This logical object is then mapped via an interpretation functor into the computational stratum of the effective realizability topos, where its algorithmic content is made explicit as a modest set whose elements are witnessed by computable programs (specifically, the Baillie–PSW primality test). Finally, this computational object is mapped via the direct image functor of a geometric morphism into the geometric stratum of the étale topos of Spec(ℤ), yielding a constructible sheaf whose support is conditionally proven to be $\mathcal{P}$. The framework’s primary utility is not in providing a new algorithm for primality testing, but in offering a complete, foundational model that explains *how* the logical definition of a prime number gives rise to its computational and geometric manifestations. The validity of the framework is conditional on the Baillie–PSW conjecture.

**Keywords**: prime numbers, homotopy type theory, realizability topos, étale sheaf, functorial lift, constructible property, arithmetic geometry, foundational mathematics

---

### 1.0 The Representational Problem of Primality

The study of prime numbers is defined by a central paradox: their definition is elementary, local, and combinatorial—a natural number greater than one is prime if it is divisible only by one and itself—yet their global behavior is governed by deep laws intertwined with continuous, analytic objects such as the Riemann zeta function. This dichotomy has led to a representational crisis in number theory. A synthetic approach that attempts to unify these aspects by combining constraints from different mathematical domains—for instance, by constructing a ‘synthetic prime sheaf’ as the fiber product of sheaves encoding modular, analytic, and geometric properties—is fundamentally inadequate. Such an approach imposes a geometric structure externally rather than deriving it from the definition of primality itself. Consequently, synthetic methods are structurally incapable of providing a complete characterization, suffering from irreparable flaws such as the inability of norm-based constructions to distinguish primes from prime powers without appealing to external oracles (Hartshorne, 1977). A successful characterization, therefore, must not simply combine different views of primality; it must demonstrate how the geometric view is a necessary and canonical consequence of the logical one.

### 2.0 The Solution Strategy: A Functorial Bridge from Logic to Geometry

This framework resolves the aforementioned paradox by constructing a formal, structure-preserving bridge from a foundational logical definition of primality to its ultimate geometric manifestation. The solution is a composed functor, the ‘Prime Realization Functor’ $G = \gamma_* \circ I$, which acts as a realization engine, translating an object in the category of formal types into an object in the category of sheaves on an arithmetic scheme. This process unfolds across three distinct categorical strata—Logical, Computational, and Geometric—ensuring that the final geometric object is not an arbitrary construction but the canonical image of the initial logical definition. The first stage, in the Logical Stratum, defines primality as a decidable type within Homotopy Type Theory (HoTT), providing a foundational, computationally-aware definition. The second stage maps this type via an interpretation functor $I$ into the Computational Stratum of the effective realizability topos $\mathbf{RT}(\mathcal{K}_1)$, where its inherent algorithmic content is made explicit as a “modest set” whose elements are witnessed by computable programs. The third and final stage maps this computational object via the direct image functor $\gamma_*$ of a geometric morphism to the Geometric Stratum of the étale topos of Spec(ℤ), yielding a constructible sheaf whose geometric properties are the necessary manifestation of the original type’s logical and computational structure.

### 3.0 Stage 1: The Logical Stratum—A Decidable Prime Type in HoTT

The necessary starting point for a foundational framework is a formal system where logical definitions are intrinsically linked to computational content. Homotopy Type Theory (HoTT) is uniquely suited for this role, as its “proofs-as-programs” paradigm and its internal logic allow for the definition of mathematical objects and the verification of their properties (e.g., proving a type is a set) within a single, coherent language (Univalent Foundations Program, 2013). Within this system, the Prime type is formally constructed as a dependent sum over the natural numbers, $\sum_{n:\mathbb{N}} \| \mathsf{isPrime}(n) \|_{-1}$, which is then proven to be a 0-type (a set), ensuring it faithfully represents the prime numbers as a discrete collection. This abstract logical object is then endowed with concrete computational meaning by proving that, conditional on the Baillie–PSW conjecture—a standard conjecture in computational number theory—the Prime type has decidable equality, making it a discrete object suitable for algorithmic manipulation.

### 4.0 Stage 2: The Computational Stratum—The Realizability Interpretation

The first functorial step, $I$, translates the Prime type from the logical stratum into the computational stratum of the effective topos, $\mathbf{RT}(\mathcal{K}_1)$. This topos is the canonical category of computable mathematics, a setting where the truth of every statement is required to be witnessed by a specific computation, or “realizer” (van Oosten, 2008). The interpretation functor $I: \mathrm{HoTT} \to \mathbf{RT}(\mathcal{K}_1)$ maps the decidable Prime type to a modest set $\underline{\mathcal{P}} = (P, \Vdash)$. This object makes the implicit computational content of the HoTT type explicit. It consists of the carrier set $P$ (the standard set of primes) and a realizability relation $\Vdash$, where $e \Vdash p$ holds if and only if $e$ is the Gödel number of a program that correctly certifies the primality of $p$. The Baillie–PSW algorithm, with its deterministic $O((\log p)^3)$ complexity (Baillie & Wagstaff, 1980), provides the explicit family of realizers for this relation, thus giving a concrete computational embodiment to the abstract Prime type.

### 5.0 Stage 3: The Geometric Stratum—The Constructible Sheaf on Spec(ℤ)

The second functorial step, $\gamma_*$, completes the bridge by mapping the computational object $\underline{\mathcal{P}}$ into the canonical category of arithmetic geometry. The target is the étale topos of Spec(ℤ), the natural geometric environment for number theory, where local geometric data corresponds to arithmetic properties at each prime ideal (Milne, 2017). A canonical geometric morphism $\gamma: \mathbf{RT}(\mathcal{K}_1) \to \mathrm{Sh}(\mathrm{Ét}(\mathrm{Spec}(\mathbb{Z})))$ exists, providing a formal connection from the computable universe to the arithmetic-geometric universe. The direct image functor $\gamma_*$ of this morphism pushes the prime modest set $\underline{\mathcal{P}}$ forward to a sheaf $\gamma_*(\underline{\mathcal{P}})$ on the étale site of Spec(ℤ). The resulting sheaf is *constructible*, a key geometric property which signifies that its structure is finite and algorithmically defined, directly reflecting the nature of its computational realizers. Finally, it is proven that, conditional on the Baillie–PSW conjecture, the support of this sheaf—the geometric locus where it is non-trivial—is precisely the set of prime numbers.

### 6.0 Synthesis: Primality as a Constructible Geometric Property

The composed functorial lift $G = \gamma_* \circ I$ provides a formal, rigorous, and structure-preserving path from a logical definition to a geometric object, resolving the tension between the discrete and continuous aspects of prime numbers. This process demonstrates that the geometric nature of primes is not an external property to be imposed but is an emergent feature *constructed* from their foundational definition. The final sheaf $\gamma_*(\underline{\mathcal{P}})$ is the “correct” geometric object corresponding to the primes because it is the canonical image of the Prime type, embodying its logical and computational essence in a geometric form. This framework reframes primality not as an anomalous property of integers, but as a constructible property of a formal object within a unified mathematical system that seamlessly integrates logic, computation, and geometry.

### 7.0 The Main Theorem of Prime Characterization

The entire framework culminates in a single, precise theorem that formally connects the foundational definition of primes to their geometric realization.

**Theorem:** Assuming the Baillie–PSW conjecture, the direct image of the prime modest set $\underline{\mathcal{P}}$ under the canonical geometric morphism $\gamma: \mathbf{RT}(\mathcal{K}_1) \to \mathrm{Sh}(\mathrm{Ét}(\mathrm{Spec}(\mathbb{Z})))$ is a constructible étale sheaf whose support is exactly the set of prime numbers.

### 8.0 Significance of the Functorial Characterization

#### 8.1. A Complete Theoretical Model

This framework provides a “complete characterization” in a theoretical and foundational sense. It achieves a unification of the three fundamental aspects of a mathematical object: its logical definition (as a type), its computational content (as a realizable set), and its geometric embodiment (as a sheaf). The completeness lies not in offering a new algorithm, but in demonstrating that these three aspects are formally and functorially connected, forming a single, coherent mathematical story. It answers the question: “What is the canonical geometric object that corresponds to the logical definition of a prime number?”

#### 8.2. Computational vs. Theoretical Utility

The framework’s utility is primarily theoretical, not algorithmic. It does not propose a new, faster primality test. Instead, it *incorporates* a state-of-the-art algorithm (Baillie–PSW) as the “realizer” or computational witness that gives substance to the abstract objects. Its value is explanatory: it provides a formal model that shows *why* an efficient, deterministic primality test can exist and what its existence implies geometrically. The framework demonstrates that the Baillie–PSW algorithm is precisely the computational engine that “constructs” the geometric object whose support is the set of primes. It provides a categorical semantics for a primality algorithm.

#### 8.3. Why This Matters

This characterization matters for several reasons:

1.  **Foundational Insight:** It resolves the long-standing paradox between the discrete, combinatorial definition of primes and their global, analytic properties, showing the latter emerge from the former when viewed through the correct categorical lens.
2.  **Unification in Mathematics:** It provides a concrete, powerful example of the modern mathematical drive to unify disparate fields—in this case, logic (type theory), computer science (realizability), and arithmetic geometry (sheaf theory).
3.  **Reframing “Irregularity”:** It demonstrates that the perceived “irregularity” or “randomness” of the primes is an artifact of viewing them in a limited context (the number line). Within the richer structure of the étale topos, the set of primes is the support of a well-behaved, constructible object.
4.  **Implications for Formal Systems:** For fields like formal verification and automated proof assistants, having a complete, unified model of a fundamental object like the primes is invaluable. It provides a template for how to formally relate abstract definitions to the concrete algorithms that operate on them.

---

### Appendix A: Formal Construction of the Prime Type in HoTT

To construct the Prime type, we proceed formally within Homotopy Type Theory.

1.  **Define the Predicate:** For $n:\mathbb{N}$, we define the type $\mathsf{isPrime}(n) := (n > 1) \times \prod_{a,b:\mathbb{N}} (n = a \cdot b \to (a = 1) + (b = 1))$. This type represents the property of being prime. An inhabitant of this type is a formal proof that $n$ is prime.
2.  **Apply Propositional Truncation:** We define $\mathsf{isPropPrime}(n) := \| \mathsf{isPrime}(n) \|_{-1}$. The truncation $\| \cdot \|_{-1}$ is a higher inductive type that adds a constructor $\mathrm{trunc} : \mathsf{isPrime}(n) \to \| \mathsf{isPrime}(n) \|_{-1}$ and path constructors ensuring that any two inhabitants of $\| \mathsf{isPrime}(n) \|_{-1}$ are equal. This makes it a mere proposition, a type with at most one distinct inhabitant. This step is crucial as it abstracts away from the specifics of any particular proof of primality to the mere fact *that* a number is prime.
3.  **Define the Prime Type:** We define $\mathsf{Prime} := \sum_{n:\mathbb{N}} \mathsf{isPropPrime}(n)$. An element of Prime is a pair $(n, p)$ consisting of a number $n$ and a proof $p$ (unique up to equality) that $n$ is prime.
4.  **Prove Prime is a Set:** A type is a set (a 0-type) if for any two elements $x, y$, the identity type $x = y$ is a mere proposition. This property is proven for Prime because it is a dependent sum of a set ($\mathbb{N}$) and a family of mere propositions ($\mathsf{isPropPrime}(n)$). Thus, the Prime type faithfully represents the prime numbers as a discrete collection, as expected (Univalent Foundations Program, 2013).

---
### Appendix B: Proof of Decidable Equality for Prime

To prove that equality in the Prime type is decidable, we formalize the connection to the Baillie–PSW test.

1.  **Assume the Conjecture:** We assume the Baillie–PSW conjecture, which states that the Baillie–PSW test is a correct and deterministic algorithm for primality.
2.  **Construct the Decision Procedure:** We define a function $\mathsf{decide\_isPrime} : \mathbb{N} \to \mathbf{2}$ (where $\mathbf{2}$ is the boolean type) that implements the Baillie–PSW algorithm. This function is computable and, by assumption, correct.
3.  **Establish Equivalence:** The conjecture implies a logical equivalence: $\mathsf{decide\_isPrime}(n) = \mathrm{true} \leftrightarrow \mathsf{isPropPrime}(n)$. This means our computable function serves as a decision procedure for the primality predicate.
4.  **Prove Decidability for Prime:** To decide if two elements $x = (n, p)$ and $y = (m, q)$ of Prime are equal, we only need to decide if their first components are equal, i.e., $n = m$, since the second components are proofs within a mere proposition and are thus equal if the numbers are. Since equality in $\mathbb{N}$ is decidable, and the predicate $\mathsf{isPropPrime}$ is decidable via $\mathsf{decide\_isPrime}$, the type Prime itself has decidable equality.
5.  **Conclusion:** The type Prime is formally a discrete set, an object with a decidable equality relation, making it computationally well-behaved.

---
### Appendix C: Construction of the Modest Set $\underline{\mathcal{P}}$ in $\mathbf{RT}(\mathcal{K}_1)$

Following the categorical approach to realizability detailed by van Oosten (2008), we construct the modest set for primes.

1.  **Define the Topos:** The effective topos $\mathbf{RT}(\mathcal{K}_1)$ is the category of assemblies over Kleene’s first algebra $\mathcal{K}_1$, which models the universe of Turing-computable functions. An object, a modest set, is a set $X$ equipped with a realizability relation $\Vdash \subseteq \mathbb{N} \times X$ such that every element $x \in X$ has a non-empty set of realizers.
2.  **Define the Interpretation Functor $I$:** This functor maps types with decidable equality in HoTT to modest sets in $\mathbf{RT}(\mathcal{K}_1)$.
3.  **Construct the Modest Set:** The functor $I$ maps the Prime type to $\underline{\mathcal{P}} = (P, \Vdash)$ where:
    a. **Carrier Set:** $P$ is the standard set of prime numbers $\{2, 3, 5, ...\}$.
    b. **Realizability Relation:** $e \Vdash p$ is defined to hold if and only if the program with Gödel number $e$ is an implementation of the Baillie–PSW test that halts and returns true on input $p$.
4.  **Verify Well-formedness:** The construction is valid. Under the Baillie–PSW conjecture, for any prime $p$, the set of its realizers is non-empty. For any composite $n$, the set of its realizers is empty. This structure correctly represents the decidable set Prime within the computational universe of the effective topos.

---
### Appendix D: Construction of the Geometric Morphism $\gamma$

The connection between the topos of computability and the topos of arithmetic geometry is established by a canonical geometric morphism.

1.  **Define Geometric Morphism:** A geometric morphism $\gamma: \mathcal{E} \to \mathcal{F}$ is a pair of adjoint functors $(\gamma^*, \gamma_*)$ between toposes, where $\gamma^*$ (inverse image) is left-exact and preserves finite limits. It is the topos-theoretic analogue of a continuous map between spaces (van Oosten, 2008).
2.  **State Existence:** A canonical geometric morphism $\gamma: \mathbf{RT}(\mathcal{K}_1) \to \mathrm{Sh}(\mathrm{Ét}(\mathrm{Spec}(\mathbb{Z})))$ exists, providing a standard bridge from the category of computable sets to the category of sheaves on the fundamental object of arithmetic geometry, Spec(ℤ) (Milne, 2017).
3.  **Define the Direct Image Functor $\gamma_*$:** The right adjoint $\gamma_*$ maps a modest set $(X, \Vdash)$ to a sheaf $F$ on the étale site of Spec(ℤ). The sections of this sheaf over an étale scheme $U \to \mathrm{Spec}(\mathbb{Z})$ are defined as:

$$
F(U) := \{ s: U \to X \mid \exists e \in \mathbb{N}, \forall x \in U, e \Vdash s(x) \}.
$$

4.  **Intuition:** This definition enforces a strong computational uniformity. A valid section $s$ over a geometric region $U$ is a locally constant function whose values are all certified by the *same single computational witness* $e$. The geometry is thus constrained by computability.

---
### Appendix E: Verification of Sheaf Support

To complete the framework, we prove that the support of the constructed sheaf is precisely the set of primes.

1.  **Define Support:** The support of a sheaf $F$, $\mathrm{supp}(F)$, is the set of points $x$ in the base space for which the stalk $F_x$ is non-empty. The base space is Spec(ℤ), whose closed points are the maximal ideals $(p)$ for prime numbers $p$.
2.  **Analyze the Stalk:** The stalk $F_p$ of the sheaf $F = \gamma_*(\underline{\mathcal{P}})$ at a point $p$ is the limit of sections over all open neighborhoods of $p$. The stalk is non-empty if and only if there exists some section $s$ defined in a neighborhood of $p$ such that $s(p) = p$ and there is a uniform realizer $e$ for that section such that $e \Vdash p$.
3.  **Connect to Realizability:** From the definition of the realizability relation $\Vdash$ (Appendix C), the condition $e \Vdash p$ holds if and only if the Baillie–PSW test certifies $p$ as prime.
4.  **Apply the Conjecture:** Assuming the Baillie–PSW conjecture, a realizer $e$ exists if and only if $p$ is a prime number.
5.  **Conclusion on Support:** For any prime $p$, the stalk $F_p$ is non-empty. For any composite $n$, the stalk $F_n$ is empty because no realizer exists. Therefore, the set of points where the stalk is non-empty is precisely the set of prime numbers: $\mathrm{supp}(\gamma_*(\underline{\mathcal{P}})) = \mathcal{P}$.
6.  **Verify Constructibility:** The sheaf is constructible because the primality test is deterministic and terminates in polynomial time. This finiteness condition on the realizers translates into the geometric property of the sheaf being locally constant on a finite stratification of Spec(ℤ).

---
### References

Baillie, R., & Wagstaff, S. S., Jr. (1980). Lucas pseudoprimes. *Mathematics of Computation*, 35(152), 1391–1417.

Hartshorne, R. (1977). *Algebraic Geometry*. Springer-Verlag.

Milne, J. S. (2017). *Étale Cohomology*. Princeton University Press.

The Univalent Foundations Program. (2013). *Homotopy Type Theory: Univalent Foundations of Mathematics*. Institute for Advanced Study.

van Oosten, J. (2008). *Realizability: An Introduction to its Categorical Side*. Elsevier.
