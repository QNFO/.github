---
author: Rowan Brad Quni-Gudzinas
ORCID: 0009-0002-4317-5604
ISNI: 0000000526456062
title: "1.0"
aliases:
  - "1.0"
modified: 2025-10-31T07:30:07Z
---

# Prime Duality 

## Decoupling Computational Utility and Cryptographic Security

**Author:** Rowan Brad Quni-Gudzinas
**Contact:** rowan.quni@outlook.com
**ORCID:** 0009-0002-4317-5604
**ISNI:** 0000 0005 2645 6062
**DOI:** 10.5281/zenodo.17491362
**Publication Date:** 2025-10-31
**Version:** 1.0

**Abstract**: The use of prime numbers for both canonical data encoding and cryptographic security has created a fundamental, long-term conflict in computer science. The migration to post-quantum standards, driven by the threat of quantum algorithms, reveals an implicit but unformalized design principle: selecting for mathematical problems that are hard but lack the broad “constructive utility” of integer factorization. This work provides a formal framework to classify computational hardness assumptions based on their intrinsic algebraic and geometric properties. We argue that a problem’s potential for constructive utility is a direct function of its underlying algebraic structure, such as supporting unique, canonical decompositions in an abelian group. By analyzing the properties of integer factorization versus those of lattice-based problems, we formalize the “hardness without utility” principle, providing a theoretical explanation for the ongoing cryptographic transition. The proposed taxonomy offers a constructive methodology for the design and evaluation of future cryptographic systems, ensuring security is decoupled from general computational utility.

**Keywords**: Prime Numbers, Cryptography, Post-Quantum Cryptography, Computational Complexity, Lattice-Based Cryptography, Constructive Utility, Hardness Assumptions, Algebraic Structures

---

## 1.0 State of the Art and Gap Identification

The use of prime numbers for both canonical data encoding and cryptographic security has created a fundamental, long-term conflict in computer science. While the migration to post-quantum standards is well-documented, the underlying design principles motivating the choice of new hardness assumptions remain largely heuristic. This work provides a novel theoretical lens, arguing that the Post-Quantum Cryptography (PQC) transition represents an implicit move away from problems with high ‘constructive utility’ (like integer factorization) towards those whose hardness is rooted in geometric ambiguity (like lattice problems). We formalize this principle with a new taxonomy of hardness assumptions, providing a rigorous methodology for future cryptographic design.

### 1.1 Summary of Key Prior Work

The principle of using unique prime factorization for constructive encoding is central to the theory of computation, enabling the representation of complex logical systems as unique integers. The security of first-generation public-key cryptography is predicated on the presumed computational difficulty of reversing this construction, specifically via integer factorization and the discrete logarithm problem. This paradigm was rendered vulnerable by Shor’s algorithm, which demonstrated that these number-theoretic problems are solvable in polynomial time on a quantum computer by exploiting the abelian group structure of modular arithmetic. In response, lattice-based cryptography has emerged as a promising alternative, grounded in the hardness of problems like Learning With Errors (LWE), which benefit from proofs reducing their average-case security to worst-case hardness—a feature absent in number-theoretic cryptography.

### 1.2 Identified Open Problems or Tensions

The ongoing migration to Post-Quantum Cryptography (PQC), as managed by bodies like NIST, is guided by an informal heuristic of selecting for “hardness without utility,” but this principle has not been formalized in the literature. There is no rigorous, accepted theory that explains *why* the algebraic and geometric structure of lattice-based problems is inherently less suited for general-purpose computation than the highly structured, constructive nature of prime factorization. The lack of a formal framework connecting a problem’s intrinsic structure to its potential for constructive utility creates a risk of repeating past design flaws and hinders the systematic discovery of new, robust cryptographic foundations.

### 1.3 Positioned Contribution of This Work

Building on the paradigm shift prompted by Shor (1994) and Ajtai (1996), this work proposes a formal framework to classify computational hardness assumptions based on their intrinsic algebraic and geometric properties. This framework formalizes the “hardness without utility” principle, providing a theoretical explanation for the migration to lattice-based cryptography. The proposed taxonomy offers a constructive methodology for the design and evaluation of future cryptographic systems, ensuring security is decoupled from general computational utility.

## 2.0 The Prime Duality: A Structural Conflict in Computation

The utility of primes in computation and their vulnerability in cryptography stem from the same source: the simple, constructive, and unique algebraic structure of integers under multiplication.

### 2.1 The Constructive Utility of Unique Factorization

The existence and uniqueness of prime factorization provide a canonical mapping from composite structures (like sequences or logical formulas) to single integers, a technique foundational to mathematical logic. This property is computationally ‘constructive’ because it is efficient to compose (multiply) and provides a well-defined path for decomposition (factoring), making it ideal for symbolic AI and data representation.

### 2.2 The Cryptographic Reliance on Hardness

Prime-based cryptography treats multiplication as a candidate one-way function, where composition is easy but decomposition is presumed to be classically hard. The security of these systems is therefore entirely dependent on the absence of an efficient classical algorithm for reversing the constructive process.

### 2.3 The Inevitable Collision Course

Because the same mathematical properties underpin both domains, any significant advance in the efficiency of decomposition for computational purposes necessarily breaks the cryptographic security assumption. This establishes a fundamental, long-term conflict, making prime-based problems an unstable foundation for security in an era of accelerating computational power.

## 3.0 The Post-Quantum Shift: An Implicit Appeal to “Hardness Without Utility”

The transition to post-quantum standards is not merely a reaction to a new threat (quantum computers) but an implicit rejection of the dual-use nature of number-theoretic problems.

### 3.1 The Quantum Threat and the Failure of the Classical Paradigm

Shor’s algorithm exploits the abelian group structure of modular arithmetic to efficiently find periods, which reduces both integer factorization and the discrete logarithm problem to polynomial time on a quantum computer. This result provides a concrete example of a computational advance that invalidates the security assumptions of an entire class of cryptosystems.

### 3.2 The Rise of Lattice-Based Cryptography

The leading PQC candidates are based on the presumed hardness of problems in high-dimensional lattices, such as finding a uniquely short vector or solving a system of linear equations with noise. Unlike prime factorization, which involves unique algebraic decomposition, lattice problems involve finding approximate solutions to geometric optimization problems in a vector space.

## 4.0 A Formal Framework for Classifying Hardness Assumptions

A problem’s potential for constructive utility is a direct function of its underlying algebraic structure. Robust cryptographic foundations should be sought in mathematical domains that are structurally poor for general-purpose construction.

### 4.1 Defining “Constructive Utility” via Algebraic Properties

A mathematical problem possesses high ‘constructive utility’ if its underlying structure supports operations with canonical and unique results, such as unique factorization in a free abelian group. Problems based on finding non-unique, approximate solutions in non-abelian or purely geometric settings possess low constructive utility.

### 4.2 A Taxonomy of Hardness Structures

Hardness assumptions can be classified into distinct families: (1) Unique Algebraic Decomposition (e.g., factoring), (2) Non-Abelian Algebraic Search (e.g., conjugacy problem in braid groups), and (3) Geometric Approximation (e.g., Shortest Vector Problem (SVP)/Learning With Errors (LWE)). This taxonomy separates problems with high constructive utility (Family 1) from those with low utility (Families 2 and 3), providing a formal basis for the ‘hardness without utility’ principle.

### 4.3 Case Study: Contrasting Integer Factorization and Lattice Problems
The framework developed in this section correctly classifies integer factorization as having high constructive utility and lattice problems as having low constructive utility, thereby formally explaining the PQC migration. Integer factorization belongs to the 'Unique Algebraic Decomposition' family. Its structure is abelian, and its solution (the set of prime factors) is unique and canonical. These properties make it highly suitable for constructive tasks like Gödel numbering but cryptographically fragile. In contrast, lattice problems like SVP and LWE belong to the 'Geometric Approximation' family. The solutions are vectors in a high-dimensional space, are generally not unique (multiple short vectors can exist), and are often sought in an approximate sense. This geometric, approximate, and non-unique nature makes them poorly suited for creating the canonical representations required for high constructive utility.

## 5.0 Toward a Constructive Theory of Secure Cryptographic Design
The security of future cryptographic systems should be based on a formal, structural analysis of their underlying mathematical problems. The principle of 'hardness without utility,' formalized by the proposed framework, provides a robust methodology for selecting hardness assumptions that are resistant to both targeted attacks and general computational progress.

## References
Ajtai, M. (1996). Generating hard instances of lattice problems. In *Proceedings of the Twenty-Eighth Annual ACM Symposium on Theory of Computing*, 99-108. doi:10.1145/237814.237838.

Alagic, G., et al. (2022). *Status Report on the Third Round of the NIST Post-Quantum Cryptography Standardization Process*. NIST Internal Report 8413. doi:10.6028/NIST.IR.8413.

Bernstein, D. J., & Lange, T. (2017). Post-quantum cryptography. *Nature*, 549, 188-194. doi:10.1038/nature23461.

Diffie, W., & Hellman, M. E. (1976). New Directions in Cryptography. *IEEE Transactions on Information Theory*, 22(6), 644-654. doi:10.1109/TIT.1976.1055638.

Gödel, K. (1931). Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I (On Formally Undecidable Propositions of Principia Mathematica and Related Systems I). *Monatshefte für Mathematik und Physik*, 38, 173-198. doi:10.1007/BF01700692.

Kan, A., & Billard, A. (2019). *A Survey of Symbolic AI*. arXiv preprint arXiv:1902.00428.

Micciancio, D., & Goldwasser, S. (2002). *Complexity of Lattice Problems: A Cryptographic Perspective*. Springer. doi:10.1007/978-1-4615-0897-7.

Regev, O. (2005). On Lattices, Learning with Errors, Random Linear Codes, and Cryptography. In *Proceedings of the Thirty-Seventh Annual ACM Symposium on Theory of Computing*, 84-93. doi:10.1145/1060590.1060603.

Regev, O. (2009). On Lattices, Learning with Errors, Random Linear Codes, and Cryptography. *Journal of the ACM*, 56(6), 1-40. doi:10.1145/1568318.1568324.

Rivest, R. L., Shamir, A., & Adleman, L. M. (1978). A Method for Obtaining Digital Signatures and Public-Key Cryptosystems. *Communications of the ACM*, 21(2), 120-126. doi:10.1145/359340.359342.

Shor, P. W. (1994). Algorithms for Quantum Computation: Discrete Logarithms and Factoring. In *Proceedings of the 35th Annual Symposium on Foundations of Computer Science*, 124-134. doi:10.1109/SFCS.1994.365700.

Turing, A. M. (1936). On Computable Numbers, with an Application to the Entscheidungsproblem. *Proceedings of the London Mathematical Society*, s2-42(1), 230-265. doi:10.1112/plms/s2-42.1.230.