---
author: Rowan Brad Quni-Gudzinas
ORCID: 0009-0002-4317-5604
ISNI: 0000000526456062
title: "**Module 2: Bruhat-Tits Trees with Scaling Ratios**"
modified: 2026-04-06T08:11:48Z
aliases:
  - "**Module 2: Bruhat-Tits Trees with Scaling Ratios**"
---
# ULTRAMETRIC PHYSICS
## **Module 2: Bruhat-Tits Trees with Scaling Ratios**

**Author:** Rowan Brad Quni-Gudzinas  
**Contact:** [rowan.quni@outlook.com](mailto:rowan.quni@outlook.com)  
**ORCID:** [0009-0002-4317-5604](http://orcid.org/0009-0002-4317-5604)  
**ISNI:** [0000000526456062](http://isni.org/isni/0000000526456062)
**DOI:** [10.5281/zenodo.19426816](http://doi.org/10.5281/zenodo.19426816)
**Date:** 2026-04-06
**Version:** 2.0

## **1. Introduction: Trees as Discrete Hierarchical Spaces**

### **1.1 The Bruhat-Tits Tree Construction**

Let $N \in \mathbb{N}$ and $q \in \mathbb{R}^+$ with $q > 1$. The **Bruhat-Tits tree** $T_{N,q}$ is a regular tree where:

- **Vertex set:** Equivalence classes of lattices in a 2-dimensional vector space over a field with residue field of size $N$
- **Edge relation:** Two vertices are connected if corresponding lattices are related by scaling
- **Edge weight:** Each edge has weight $\log q$

**Definition 1.1** (Abstract construction). For parameters $(N,q)$, define $T_{N,q}$ as the infinite $(N+1)$-regular tree with:
- **Degree:** $N+1$ at each vertex
- **Metric:** $d_q(v,w) = d_{\text{graph}}(v,w) \cdot \log q$ where $d_{\text{graph}}$ is graph distance

### **1.2 Physical Interpretation**

**Postulate 1.2** (Physical substrate). In the ratio-based framework, $T_{N,q}$ represents the fundamental discrete hierarchical structure underlying physical reality, with:

- **Scaling ratio $q$:** Fundamental scale separation between levels
- **Branching parameter $N$:** Information capacity or degeneracy at each scale
- **Tree depth:** Logarithmic scale coordinate

## **2. Mathematical Construction**

### **2.1 Formal Definition**

**Definition 2.1** (Bruhat-Tits tree). Let $\mathcal{L}$ be the set of equivalence classes of lattices $\Lambda \subset K^2$ where $K$ is a field with discrete valuation $|\cdot|_q$ and residue field $\kappa$ of size $N$. Define $T_{N,q}$ as:

- **Vertices:** $V(T_{N,q}) = \mathcal{L}$
- **Edges:** Connect $[\Lambda]$ to $[\Lambda']$ if $\pi\Lambda \subset \Lambda' \subset \Lambda$ for uniformizer $\pi$ with $|\pi|_q = q^{-1}$
- **Distance:** $d_q([\Lambda], [\Lambda']) = v_{\mathfrak{p}}(\det(\Lambda^{-1}\Lambda')) \cdot \log q$

**Theorem 2.2** (Regularity). $T_{N,q}$ is an $(N+1)$-regular tree (each vertex has degree $N+1$).

*Proof.* Standard result from Bruhat-Tits theory: the link of each vertex is the building of $\text{PGL}_2(\kappa)$, which is a complete graph on $N+1$ vertices. ∎

### **2.2 Alternative Combinatorial Definition**

**Definition 2.3** (Combinatorial model). For abstract parameters $(N,q)$, define $T_{N,q}$ recursively:

1. **Root vertex** $v_0$
2. Each vertex at depth $d$ has $N+1$ children at depth $d+1$
3. Edge between parent and child has weight $\log q$

**Proposition 2.4.** This combinatorial model is isometric to the algebraic construction when $N$ is a prime power.

## **3. Metric Properties**

### **3.1 Tree Metric**

**Definition 3.1** ($q$-metric). For vertices $v,w \in V(T_{N,q})$:
$$d_q(v,w) = \inf_{\gamma} \sum_{e \in \gamma} \log q$$
where infimum is over paths $\gamma$ connecting $v$ and $w$.

**Theorem 3.2** (Ultrametric property). $d_q$ satisfies the strong triangle inequality:
$$d_q(v,w) \leq \max(d_q(v,u), d_q(u,w))$$
for all $u,v,w \in V(T_{N,q})$.

*Proof.* Follows from tree structure: any three vertices have a unique branching point. ∎

### **3.2 Volume Growth**

**Definition 3.3** (Ball volume). Let $B(v,r) = \{w \in V(T_{N,q}) : d_q(v,w) \leq r\}$.

**Theorem 3.4** (Exponential growth). For $r = d \cdot \log q$ with $d \in \mathbb{N}$:
$$|B(v,r)| = 1 + (N+1)\frac{N^d - 1}{N - 1} \quad \text{for } N > 1$$
$$|B(v,r)| = 2^{d+1} - 1 \quad \text{for } N = 1$$

*Proof.* Count vertices in ball of graph radius $d$ in $(N+1)$-regular tree. ∎

### **3.3 Boundary at Infinity**

**Definition 3.5** (Boundary). The boundary $\partial T_{N,q}$ is the set of equivalence classes of geodesic rays, where two rays are equivalent if they eventually coincide.

**Theorem 3.6** (Boundary structure). $\partial T_{N,q}$ is a Cantor set when $N \geq 2$, with Hausdorff dimension:
$$\dim_H(\partial T_{N,q}) = \frac{\log N}{\log q}$$

*Proof.* Standard result for regular trees: boundary is $N$-adic Cantor set with metric $d(\xi,\eta) = q^{-d(\xi \wedge \eta)}$ where $\xi \wedge \eta$ is confluence point. ∎

## **4. Automorphism Group**

### **4.1 Structure of $\text{Aut}(T_{N,q})$**

**Definition 4.1** (Tree automorphisms). $\text{Aut}(T_{N,q})$ is the group of graph automorphisms preserving the tree structure.

**Theorem 4.2** (Classification). Automorphisms of $T_{N,q}$ are classified as:

1. **Elliptic:** Fix a vertex or finite subtree
2. **Hyperbolic:** Translate along a geodesic axis
3. **Inversion:** Exchange two subtrees

*Proof.* Standard tree automorphism theory (Tits). ∎

### **4.2 Scaling Transformations**

**Definition 4.3** (Scaling automorphism). For $k \in \mathbb{Z}$, define $\sigma_k \in \text{Aut}(T_{N,q})$ by:
$$\sigma_k(v_d) = v_{d+k}$$
along a fixed geodesic ray, where $v_d$ is vertex at depth $d$.

**Theorem 4.4** (Metric action). For hyperbolic automorphism $\sigma$ with translation length $L$:
$$d_q(\sigma(v), \sigma(w)) = d_q(v,w)$$
and if $\sigma$ translates by $k$ edges along its axis:
$$d_q(\sigma(v), v) = k \cdot \log q$$

## **5. Relation to Scaling Ratio $q$**

### **5.1 Scale Invariance**

**Proposition 5.1** (Discrete scale invariance). $T_{N,q}$ is invariant under scaling by $q$ in the sense that:
$$T_{N,q} \cong q^{-1} T_{N,q}$$
where the isomorphism multiplies all distances by $q^{-1}$.

**Theorem 5.2** (Hierarchical structure). The tree $T_{N,q}$ has a natural hierarchical decomposition:
$$T_{N,q} = \bigcup_{i=1}^{N+1} q^{-1} T_{N,q}^{(i)}$$
where $T_{N,q}^{(i)}$ are isomorphic copies.

### **5.2 Continuum Limit**

**Theorem 5.3** (Continuum limit). As $q \to 1^+$ with $N \to \infty$ such that $\frac{\log N}{\log q} \to D$, the Gromov-Hausdorff limit of $T_{N,q}$ (suitably rescaled) is $\mathbb{R}^D$ with Euclidean metric.

*Proof sketch.* Consider sequence $q_n = 1 + \epsilon_n$, $N_n = \lfloor q_n^D \rfloor$. The tree approximates $\mathbb{R}^D$ at large scales. ∎

## **6. Physical Applications Framework**

### **6.1 Quantum States on Trees**

**Definition 6.1** (Tree Hilbert space). $\mathcal{H}_{N,q} = \ell^2(V(T_{N,q}))$ with inner product:
$$\langle \psi, \phi \rangle = \sum_{v \in V(T_{N,q})} \overline{\psi(v)} \phi(v)$$

**Definition 6.2** (Scale-covariant states). A state $\psi \in \mathcal{H}_{N,q}$ is scale-covariant if:
$$\psi(\sigma_k(v)) = q^{-k\Delta} \psi(v)$$
for some scaling dimension $\Delta \in \mathbb{C}$.

### **6.2 Discrete Derivatives**

**Definition 6.3** (Tree gradient). For $f: V(T_{N,q}) \to \mathbb{C}$:
$$(\nabla f)(v) = \sum_{w \sim v} \frac{f(w) - f(v)}{d_q(v,w)}$$

**Theorem 6.4** (Laplacian spectrum). The tree Laplacian $\Delta_{N,q} = \nabla^* \nabla$ has spectrum:
$$\sigma(\Delta_{N,q}) = \left[1 - \frac{2\sqrt{N}}{N+1}, 1 + \frac{2\sqrt{N}}{N+1}\right]$$

## **7. Python Implementation**

```python
"""
Module 2: Bruhat-Tits Trees with Scaling Ratios
"""

import networkx as nx
import numpy as np
from typing import Dict, List, Tuple

class BruhatTitsTree:
    """
    Implementation of Bruhat-Tits tree with scaling ratio q.
    """
    
    def __init__(self, N: int, q: float, max_depth: int):
        """
        Initialize tree with parameters.
        
        Parameters:
        -----------
        N : int
            Residue field size (branching factor = N+1)
        q : float
            Scaling ratio (q > 1)
        max_depth : int
            Maximum tree depth to generate
        """
        if q <= 1:
            raise ValueError("Scaling ratio q must be > 1")
        if N < 1:
            raise ValueError("N must be ≥ 1")
        
        self.N = N
        self.q = q
        self.max_depth = max_depth
        self.tree = self._build_tree()
    
    def _build_tree(self) -> nx.Graph:
        """Build finite approximation of Bruhat-Tits tree."""
        G = nx.Graph()
        
        vertex_id = 0
        vertices_by_depth = {0: [0]}
        G.add_node(0, depth=0)
        
        for depth in range(self.max_depth):
            if depth not in vertices_by_depth:
                continue
            
            for parent in vertices_by_depth[depth]:
                for child_num in range(self.N + 1):
                    vertex_id += 1
                    G.add_node(vertex_id, depth=depth + 1)
                    G.add_edge(parent, vertex_id, weight=np.log(self.q))
                    
                    if depth + 1 not in vertices_by_depth:
                        vertices_by_depth[depth + 1] = []
                    vertices_by_depth[depth + 1].append(vertex_id)
        
        return G
    
    def tree_distance(self, v: int, w: int) -> float:
        """Compute q-metric distance between vertices."""
        path_length = nx.shortest_path_length(self.tree, v, w)
        return path_length * np.log(self.q)
    
    def ball_volume(self, center: int, radius: float) -> int:
        """Count vertices within given q-metric radius."""
        count = 0
        for node in self.tree.nodes():
            dist = self.tree_distance(center, node)
            if dist <= radius:
                count += 1
        return count
    
    def boundary_dimension(self) -> float:
        """Compute theoretical boundary dimension."""
        if self.N < 2:
            return 0.0
        return np.log(self.N) / np.log(self.q)
    
    def laplacian_matrix(self):
        """Compute graph Laplacian matrix."""
        return nx.laplacian_matrix(self.tree).toarray()
    
    def analyze_properties(self) -> Dict:
        """Analyze tree properties."""
        return {
            'N': self.N,
            'q': self.q,
            'max_depth': self.max_depth,
            'num_vertices': self.tree.number_of_nodes(),
            'num_edges': self.tree.number_of_edges(),
            'boundary_dimension': self.boundary_dimension(),
            'log_q': np.log(self.q)
        }

def demonstrate_tree(user_N: int, user_q: float, user_depth: int):
    """
    Demonstrate tree construction with user parameters.
    """
    print("BRUHAT-TITS TREE CONSTRUCTION")
    print("=" * 60)
    
    try:
        tree = BruhatTitsTree(N=user_N, q=user_q, max_depth=user_depth)
        
        props = tree.analyze_properties()
        for key, value in props.items():
            print(f"{key}: {value}")
        
        # Example distance calculation
        if tree.tree.number_of_nodes() >= 3:
            nodes = list(tree.tree.nodes())[:3]
            for i in range(len(nodes)):
                for j in range(i+1, len(nodes)):
                    dist = tree.tree_distance(nodes[i], nodes[j])
                    print(f"d({nodes[i]}, {nodes[j]}) = {dist:.4f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```

## **8. Mathematical Appendix**

### **8.1 Proof of Theorem 3.6 (Boundary Dimension)**

Complete proof:

For regular tree $T_{N,q}$, consider boundary metric $d(\xi,\eta) = q^{-d(\xi \wedge \eta)}$ where $\xi \wedge \eta$ is deepest common ancestor.

Cover $\partial T_{N,q}$ by balls of radius $\epsilon = q^{-n}$. Each such ball corresponds to vertex at depth $n$, of which there are $(N+1)N^{n-1}$.

Thus covering number $N(\epsilon) \sim N^n = \epsilon^{-\log N/\log q}$.

Hausdorff dimension is:
$$\dim_H = \lim_{\epsilon \to 0} \frac{\log N(\epsilon)}{\log(1/\epsilon)} = \frac{\log N}{\log q}$$
∎

### **8.2 Proof of Theorem 5.3 (Continuum Limit)**

Detailed proof sketch:

Let $q_n = 1 + \epsilon_n$ with $\epsilon_n \to 0$, and $N_n = \lfloor q_n^D \rfloor$.

Consider scaled metric $d_n = \epsilon_n^{-1} d_{q_n}$ on $T_{N_n,q_n}$.

For large $n$, tree approximates $\mathbb{R}^D$ because:
1. Branching factor $N_n + 1 \approx q_n^D \approx 1 + D\epsilon_n$
2. Edge length $\log q_n \approx \epsilon_n$
3. Gromov-Hausdorff convergence to $\mathbb{R}^D$ with standard metric

The convergence follows from general results on Gromov-Hausdorff limits of trees. ∎

## **9. Research Questions and Directions**

### **9.1 Open Problems**

1. **Optimal embedding:** For given physical system, what $(N,q)$ parameters best approximate continuum physics?
2. **Quantum dynamics:** How do quantum systems evolve on $T_{N,q}$?
3. **Statistical mechanics:** What thermodynamic properties emerge from tree structure?

### **9.2 Physical Applications**

1. **Quantum gravity:** $T_{N,q}$ as discrete superspace for Wheeler-DeWitt equation
2. **Quantum computation:** Tree structure for error-protected qubits
3. **Cosmology:** Tree branching as model for cosmic expansion
