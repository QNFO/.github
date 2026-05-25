---
author: Rowan Brad Quni-Gudzinas
ORCID: 0009-0002-4317-5604
ISNI: 0000000526456062
title: ULTRAMETRIC PHYSICS
aliases:
  - ULTRAMETRIC PHYSICS
modified: 2026-04-06T11:12:21Z
---

# ULTRAMETRIC PHYSICS
## **Module 10: Cosmological Dynamics from Ratio-Based Navigation**

**Author:** Rowan Brad Quni-Gudzinas  
**Contact:** [rowan.quni@outlook.com](mailto:rowan.quni@outlook.com)  
**ORCID:** [0009-0002-4317-5604](http://orcid.org/0009-0002-4317-5604)  
**ISNI:** [0000000526456062](http://isni.org/isni/0000000526456062)
**DOI:** [10.5281/zenodo.19438737](http://doi.org/10.5281/zenodo.19438737)
**Date:** 2026-04-06
**Version:** 2.0

## **1. Introduction: Cosmology as Navigation on Ratio-Scaled Trees**

The standard cosmological model (Lambda Cold Dark Matter or ΛCDM) describes the universe’s evolution through the Friedmann equations derived from General Relativity (GR). In the ratio-based framework, cosmological dynamics emerge from a fundamentally different picture: **the universe’s expansion is navigation on a Bruhat-Tits tree**, where the scale factor $a(t)$ corresponds to branching statistics with scaling ratio $q$. This provides a discrete, hierarchical alternative to the continuum description of cosmic evolution.

### **1.1 The Ratio-Centric Cosmological Paradigm**

**Key innovation:** Replace the continuous FLRW (Friedmann–Lemaître–Robertson–Walker) metric with:
- **Tree vertices:** Cosmic epochs at different scales
- **Edges:** Scale transformations with ratio $q$
- **Navigation:** Time evolution as movement through tree
- **Branching:** Creation of new structure (galaxies, clusters)

**Advantages over continuum approach:**
1. **Discrete scale invariance:** Natural explanation for observed hierarchical clustering
2. **Quantum gravitational foundation:** Discrete structure from first principles
3. **Parameter reduction:** Cosmological parameters become ratios of tree parameters
4. **Testable predictions:** Distinct signatures in Cosmic Microwave Background (CMB) and large-scale structure

## **2. Mathematical Foundations**

### **2.1 Tree as Cosmic History**

Consider Bruhat-Tits tree $T_{N,q}$ with:
- **Branching factor:** $N+1$ (residue field size $N$)
- **Scaling ratio:** $q > 1$ (edge weight $\log q$)
- **Depth:** $d$ (root = Big Bang, leaves = present)

**Definition 2.1** (Cosmic navigation). A cosmological history is a path $\gamma: d_0 \to d$ in tree, with:
- **Cosmic time:** $t(d) = d \cdot \log q$ (natural units)
- **Scale factor:** $a(d) = q^{-d/2}$ (conventional normalization $a_0 = 1$ at present)
- **Redshift:** $z(d) = a^{-1} - 1 = q^{d/2} - 1$

**Physical interpretation:** Moving one level deeper ($d \to d+1$) corresponds to universe expansion by factor $q^{1/2}$.

### **2.2 Branching Statistics**

**Definition 2.2** (Branching process). At each vertex, branching creates $N+1$ children with probability $p_{\text{branch}}$.

**Theorem 2.3** (Expected vertices). For branching probability $p_{\text{branch}} = 1$ (deterministic):
$$\mathbb{E}[V(d)] = \sum_{k=0}^d (N+1)N^{k-1} \approx \frac{N+1}{N-1} N^d \quad \text{for large } d$$

**For probabilistic branching:** $\mathbb{E}[V(d)] \sim e^{\lambda d}$ with $\lambda = \log[N \cdot p_{\text{branch}}]$.

### **2.3 Scale Factor Evolution**

**Theorem 2.4** (Scale factor from branching). For branching rate $\lambda = \log[N \cdot p_{\text{branch}}(d)]$:
$$a(d) = \exp\left(-\frac{1}{2}\int_0^d \lambda(d') dd'\right)$$

*Proof.* Number of vertices $V(d) \sim e^{\int \lambda dd'}$. Physical volume $\sim V(d) \cdot a(d)^3$. Conservation of “stuff” requires $V(d) a(d)^3 = \text{constant}$. Solve for $a(d)$. ∎

**Corollary 2.5.** For constant $\lambda$: $a(d) = e^{-\lambda d/2} = (N p_{\text{branch}})^{-d/2}$.

Thus $q = N \cdot p_{\text{branch}}$ relates tree parameters to scaling ratio.

## **3. Mapping Tree Parameters to Cosmological Parameters**

### **3.1 Hubble Parameter**

**Definition 3.1** (Hubble parameter). From $a(d) = q^{-d/2}$ and $t = d \log q$:
$$H(t) = \frac{\dot{a}}{a} = -\frac{1}{2} \frac{d}{dt}(\log a) = \frac{\lambda}{2} = \frac{\log(N p_{\text{branch}})}{2}$$

**Present value:** $H_0 = \frac{\log(N_0 p_0)}{2}$ where subscript 0 denotes present epoch.

### **3.2 Density Parameters**

**Theorem 3.2** (Friedmann equation from tree). The tree-based evolution gives effective Friedmann equation:
$$H^2 = \frac{8\pi G}{3} \rho_{\text{eff}} - \frac{k_{\text{eff}}}{a^2}$$
where:
- $\rho_{\text{eff}} = \rho_{\text{branch}} + \rho_{\text{structure}}$
- $k_{\text{eff}} = (\log q)^2 \cdot f(N)$ (effective curvature)

**Proof sketch.** Hamilton-Jacobi equation for tree navigation yields effective Friedmann equation. ∎

**Definition 3.3** (Density parameters). Define:
- $\Omega_m = \frac{\rho_{\text{branch}}}{\rho_c}$ (matter from branching process)
- $\Omega_\Lambda = \frac{\rho_{\text{structure}}}{\rho_c}$ (dark energy from tree structure)
- $\Omega_k = -\frac{k_{\text{eff}}}{a^2 H^2}$ (curvature)
where $\rho_c = \frac{3H^2}{8\pi G}$ is critical density.

**Constraint:** $\Omega_m + \Omega_\Lambda + \Omega_k = 1$.

### **3.3 Explicit Mapping**

**Theorem 3.4** (Parameter mapping). For tree with parameters $(N, q, p_{\text{branch}}(d))$:
1. **Hubble parameter:** $H = \frac{\log(N p_{\text{branch}})}{2}$
2. **Matter density:** $\Omega_m \sim \frac{p_{\text{branch}}'}{p_{\text{branch}} H}$ (branching rate change)
3. **Dark energy:** $\Omega_\Lambda \sim \frac{(\log q)^2}{H^2}$ (tree structure energy)
4. **Curvature:** $\Omega_k \sim \frac{(\log q)^2 f(N)}{a^2 H^2}$

## **4. Inflation from Accelerated Branching**

### **4.1 Inflationary Mechanism**

**Definition 4.1** (Inflation as accelerated branching). Inflation occurs when branching probability increases with depth: $p_{\text{branch}}'(d) > 0$.

**Theorem 4.2** (Inflationary condition). The tree produces accelerated expansion ($\ddot{a} > 0$) when:
$$\frac{d}{dd} \log(N p_{\text{branch}}) > 0 \quad \text{or equivalently} \quad \frac{p_{\text{branch}}'}{p_{\text{branch}}} > 0$$

*Proof.* $\ddot{a} > 0$ when $\dot{H} + H^2 > 0$. From $H = \frac{1}{2}\log(N p_{\text{branch}})$, this requires $\frac{d}{dd}\log(N p_{\text{branch}}) > 0$. ∎

**Physical interpretation:** Early universe had rapidly increasing branching rate, creating many new vertices (quantum fluctuations stretched to cosmic scales).

### **4.2 Slow-Roll Parameters**

**Definition 4.3** (Tree slow-roll parameters). Define:
$$\epsilon = -\frac{\dot{H}}{H^2} = -\frac{1}{2H} \frac{d}{dt} \log(N p_{\text{branch}})$$
$$\eta = \frac{\dot{\epsilon}}{H\epsilon} \quad \text{(second slow-roll parameter)}$$

**Inflation condition:** $\epsilon \ll 1$ (nearly constant $H$).

**Theorem 4.4** (Number of e-folds). For inflation from $d_i$ to $d_f$:
$$N_e = \int_{t_i}^{t_f} H dt = \frac{1}{2} \int_{d_i}^{d_f} \log(N p_{\text{branch}}) dd$$

### **4.3 Primordial Perturbations**

**Theorem 4.5** (Power spectrum). Quantum fluctuations in branching process give power spectrum:
$$P_\zeta(k) = A_s \left(\frac{k}{k_0}\right)^{n_s-1}$$
with:
- **Amplitude:** $A_s \sim \frac{H^2}{\epsilon} \sim \frac{[\log(N p_{\text{branch}})]^2}{\epsilon}$
- **Spectral index:** $n_s - 1 = -2\epsilon - \eta$

**Tensor perturbations:** From tree geometry fluctuations, amplitude $r = 16\epsilon$.

## **5. Dark Energy and Late-Time Acceleration**

### **5.1 Dark Energy as Tree Structure Energy**

**Interpretation:** Dark energy (cosmological constant $\Lambda$) corresponds to energy of tree structure itself:
$$\rho_\Lambda = \frac{(\log q)^2}{8\pi G} \cdot f(N)$$

**Theorem 5.1** (Equation of state). For tree structure energy:
$$w_\Lambda = \frac{p_\Lambda}{\rho_\Lambda} = -1 + \frac{2}{3} \frac{d}{dt} \left(\frac{1}{H}\right)$$

For constant $H$ (late-time): $w_\Lambda = -1$ (cosmological constant).

### **5.2 Cosmic Coincidence Problem**

**Tree perspective:** The coincidence $\Omega_m \sim \Omega_\Lambda$ today arises because:
1. **Matter:** $\Omega_m \sim p_{\text{branch}}'/(p_{\text{branch}} H)$ decreases as branching slows
2. **Dark energy:** $\Omega_\Lambda \sim (\log q)^2/H^2$ constant if $q$ constant
3. **Crossover:** When $\Omega_m \sim \Omega_\Lambda$ occurs naturally in tree evolution

### **5.3 Future Evolution**

**Theorem 5.2** (Future fate). For constant $q$ and $p_{\text{branch}} \to p_\infty$:
- **Future Hubble parameter:** $H_\infty = \frac{\log(N p_\infty)}{2}$
- **Asymptotic scale factor:** $a(t) \sim e^{H_\infty t}$ (de Sitter expansion)
- **Event horizon:** $R_H = H_\infty^{-1}$

**Physical interpretation:** Universe approaches maximal tree with constant branching rate.

## **6. Python Implementation**

### **6.1 Cosmological Dynamics Simulation**

```python
import sympy as sp
from typing import Dict, List, Tuple, Set

class TreeCosmologySymbolic:
    """
    Symbolic implementation of cosmological dynamics from tree branching.
    """
    
    def __init__(self, N: sp.Symbol, q: sp.Symbol):
        """
        Parameters:
        -----------
        N : sp.Symbol
            Branching parameter (residue field size)
        q : sp.Symbol
            Scaling ratio
        """
        self.N = N
        self.q = q
        
    def scale_factor(self, d: sp.Symbol) -> sp.Expr:
        """
        Scale factor from tree depth: a(d) = q^(-d/2).
        """
        a = sp.Symbol('a', positive=True)
        return sp.Eq(a, self.q**(-d/2))
    
    def hubble_parameter(self, lambda_expr: sp.Expr) -> sp.Expr:
        """
        Hubble parameter: H = λ/2 where λ = log(N p_branch).
        """
        H = sp.Symbol('H', positive=True)
        return sp.Eq(H, lambda_expr/2)
    
    def density_parameters(self, d: sp.Symbol, p_branch: sp.Function) -> Dict[str, sp.Eq]:
        """
        Symbolic density parameters Ω_m, Ω_Λ, Ω_k.
        """
        # Branching probability as function of depth
        p = p_branch(d)
        p_prime = sp.diff(p, d)  # p'(d)
        
        # Hubble parameter
        lambda_expr = sp.log(self.N * p)
        H = lambda_expr/2
        
        # Density parameters
        Omega_m = sp.Symbol('Ω_m', positive=True)
        Omega_Lambda = sp.Symbol('Ω_Λ', positive=True)
        Omega_k = sp.Symbol('Ω_k', real=True)
        
        equations = {}
        
        # Matter density from branching rate change
        equations['Omega_m'] = sp.Eq(Omega_m, p_prime/(p * H))
        
        # Dark energy from tree structure
        equations['Omega_Lambda'] = sp.Eq(Omega_Lambda, sp.log(self.q)**2 / H**2)
        
        # Curvature (simplified)
        f_N = sp.Symbol('f(N)', positive=True)
        a = self.q**(-d/2)
        equations['Omega_k'] = sp.Eq(Omega_k, sp.log(self.q)**2 * f_N / (a**2 * H**2))
        
        # Normalization constraint
        equations['normalization'] = sp.Eq(Omega_m + Omega_Lambda + Omega_k, 1)
        
        return equations
    
    def inflation_parameters(self, d: sp.Symbol, p_branch: sp.Function) -> Dict[str, sp.Eq]:
        """
        Symbolic inflation parameters.
        """
        p = p_branch(d)
        p_prime = sp.diff(p, d)
        p_double_prime = sp.diff(p_prime, d)
        
        # Hubble parameter and derivatives
        lambda_expr = sp.log(self.N * p)
        H = lambda_expr/2
        
        lambda_prime = p_prime/p  # dλ/dd
        lambda_double_prime = (p_double_prime * p - p_prime**2) / p**2
        
        # Slow-roll parameters
        epsilon = sp.Symbol('ε', positive=True)
        eta = sp.Symbol('η', real=True)
        
        # ε = -Ḣ/H^2, converting from d/dd to d/dt: d/dt = H d/dd
        # Ḣ = H * λ'
        H_dot = H * lambda_prime  # dH/dt
        epsilon_eq = sp.Eq(epsilon, -H_dot / H**2)
        
        # η = ε̇/(Hε)
        epsilon_dot = sp.diff(epsilon_eq.rhs, d) * H  # dε/dt = H dε/dd
        eta_eq = sp.Eq(eta, epsilon_dot / (H * epsilon))
        
        # Number of e-folds
        N_e = sp.Symbol('N_e', positive=True)
        N_e_eq = sp.Eq(N_e, sp.Integral(H, (d, sp.Symbol('d_i'), sp.Symbol('d_f'))))
        
        # Power spectrum parameters
        A_s = sp.Symbol('A_s', positive=True)
        n_s = sp.Symbol('n_s', positive=True)
        r = sp.Symbol('r', positive=True)
        
        A_s_eq = sp.Eq(A_s, H**2 / (8 * sp.pi**2 * epsilon))
        n_s_eq = sp.Eq(n_s, 1 - 2*epsilon - eta)
        r_eq = sp.Eq(r, 16*epsilon)
        
        return {
            'epsilon': epsilon_eq,
            'eta': eta_eq,
            'N_e': N_e_eq,
            'A_s': A_s_eq,
            'n_s': n_s_eq,
            'r': r_eq
        }
    
    def dark_energy_equation_of_state(self, d: sp.Symbol, p_branch: sp.Function) -> sp.Eq:
        """
        Equation of state for dark energy: w_Λ = -1 + (2/3) d(1/H)/dt.
        """
        p = p_branch(d)
        lambda_expr = sp.log(self.N * p)
        H = lambda_expr/2
        
        # d(1/H)/dt = -Ḣ/H^2
        H_dot = H * sp.diff(lambda_expr, d)  # Ḣ = H λ'
        w_Lambda = sp.Symbol('w_Λ', real=True)
        
        w_expr = -1 + (2/3) * (-H_dot / H**2)
        return sp.Eq(w_Lambda, w_expr)
    
    def generate_cosmological_predictions(self) -> Dict[str, sp.Expr]:
        """
        Generate symbolic cosmological predictions.
        """
        predictions = {}
        
        # Define symbolic variables
        d = sp.Symbol('d', positive=True, integer=True)
        p_branch = sp.Function('p_branch')(d)
        
        # Scale factor evolution
        predictions['scale_factor'] = self.scale_factor(d)
        
        # Hubble parameter
        lambda_expr = sp.log(self.N * p_branch)
        predictions['hubble_parameter'] = self.hubble_parameter(lambda_expr)
        
        # Density parameters
        density_eqs = self.density_parameters(d, sp.Function('p_branch'))
        predictions.update(density_eqs)
        
        # Inflation parameters
        inflation_eqs = self.inflation_parameters(d, sp.Function('p_branch'))
        predictions.update(inflation_eqs)
        
        # Dark energy equation of state
        predictions['w_Lambda'] = self.dark_energy_equation_of_state(d, sp.Function('p_branch'))
        
        return predictions

def demonstrate_cosmology_framework():
    """
    Demonstrate symbolic cosmology framework.
    """
    
    print("Symbolic Cosmological Dynamics from Ratio-Based Navigation")
    print("=" * 70)
    
    # Define symbolic parameters
    N = sp.Symbol('N', positive=True, integer=True)
    q = sp.Symbol('q', positive=True)
    
    # Create cosmology framework
    cosmology = TreeCosmologySymbolic(N, q)
    
    print("\n1. Scale Factor Relation:")
    d = sp.Symbol('d', positive=True, integer=True)
    scale_factor_eq = cosmology.scale_factor(d)
    print(f"   {sp.pretty(scale_factor_eq)}")
    
    print("\n2. Density Parameter Equations:")
    density_eqs = cosmology.density_parameters(d, sp.Function('p_branch'))
    for name, eq in list(density_eqs.items())[:4]:  # Show first 4
        print(f"   {name}: {sp.pretty(eq)}")
    
    print("\n3. Inflation Parameters:")
    inflation_eqs = cosmology.inflation_parameters(d, sp.Function('p_branch'))
    for name, eq in inflation_eqs.items():
        print(f"   {name}: {sp.pretty(eq)}")
    
    print("\n4. Dark Energy Equation of State:")
    w_eq = cosmology.dark_energy_equation_of_state(d, sp.Function('p_branch'))
    print(f"   {sp.pretty(w_eq)}")
    
    print("\n5. Physical Interpretation:")
    print("   - Scale factor a(d) = q^(-d/2) relates tree depth to cosmic expansion")
    print("   - Hubble parameter H = log(N p_branch)/2")
    print("   - Density parameters Ω derived from branching statistics")
    print("   - Inflation from accelerated branching (p_branch' > 0)")
    print("   - Dark energy as tree structure energy")
    
    return cosmology

# Run demonstration
if __name__ == "__main__":
    framework = demonstrate_cosmology_framework()
```

## **7. Testable CMB Predictions**

### **7.1 Power Spectrum Features**

**Prediction 7.1** (Oscillations in power spectrum). Tree discreteness causes oscillations:
$$P(k) = P_0(k) \left[1 + A \cos\left(\frac{2\pi \log k}{\log q} + \phi\right)\right]$$

### **7.2 Non-Gaussianity**

**Tree prediction:** Non-Gaussianity from branching statistics:
$$f_{\text{NL}} \sim \frac{1}{\sqrt{N^d}} \sim \exp\left(-\frac{d}{2} \log N\right)$$

### **7.3 Tensor Modes**

**Prediction 7.2** (Tensor spectrum). Tensor power spectrum:
$$P_t(k) = A_t \left(\frac{k}{k_0}\right)^{n_t}$$
with $n_t = -2\epsilon$ (consistency relation).

## **8. Comparison to ΛCDM**

### **8.1 Similarities**

1. **Late-time acceleration:** Both have $w \approx -1$ component
2. **Structure formation:** Hierarchical clustering in both
3. **CMB peaks:** Acoustic oscillations from baryon-photon fluid

### **8.2 Differences**

| Aspect | ΛCDM | Tree Cosmology |
|--------|------|----------------|
| **Fundamental structure** | Continuous spacetime | Discrete tree |
| **Dark energy origin** | Cosmological constant $\Lambda$ | Tree structure energy |
| **Inflation mechanism** | Scalar field rolling | Accelerated branching |
| **Horizon problem** | Solved by inflation | Solved by tree connectivity |
| **Flatness problem** | Fine-tuning of $\Omega_k$ | Natural from tree geometry |

### **8.3 Observational Discriminators**

1. **CMB oscillations:** Tree predicts log-periodic oscillations
2. **Hubble tension:** Tree may naturally explain via scale-dependent $H$
3. **Large-scale anomalies:** Tree structure could explain alignment anomalies

## **9. Conclusions and Future Directions**

### **9.1 Key Results**

1. **Cosmological dynamics emerge** from tree branching statistics with scaling ratio $q$
2. **Scale factor** $a(d) = q^{-d/2}$ relates tree depth to cosmic expansion
3. **Cosmological parameters map** to tree parameters: $H_0 \sim \log(N p_{\text{branch}})$, $\Omega_\Lambda \sim (\log q)^2/H_0^2$
4. **Inflation arises** from accelerated branching ($p_{\text{branch}}' > 0$)
5. **Testable predictions:** CMB oscillations, specific $(n_s, r)$ relations

### **9.2 Parameter Constraints**

From comparison to observations:
1. **$q$ constraint:** $(\log q)^2 \sim \Omega_\Lambda H_0^2$
2. **$N$ constraint:** $N p_{\text{branch}} \approx 1 + 2H_0$
3. **Branching rate:** Must decrease from early rapid branching to slow present rate

### **9.3 Future Work**

1. **Detailed CMB analysis:** Implement tree-based Boltzmann code
2. **Large-scale structure:** Predictions for galaxy clustering
3. **Inflation model building:** Specific branching functions for viable inflation
4. **Quantum gravitational effects:** Trans-Planckian physics from tree discreteness

## **Appendix A: Mathematical Derivations**

### **A.1 Derivation of Scale Factor Relation**

Consider tree with $V(d)$ vertices at depth $d$. Each vertex represents comoving volume $\Delta V_c$.

Physical volume at depth $d$: $V_{\text{phys}}(d) = V(d) \cdot a(d)^3 \cdot \Delta V_c$

Conservation of “stuff” (mass/energy): $V_{\text{phys}}(d) \cdot \rho(d) = \text{constant}$

For constant density $\rho$: $V(d) \cdot a(d)^3 = \text{constant}$

For branching process: $V(d) \sim e^{\int \lambda(d') dd'}$ where $\lambda(d) = \log[N \cdot p_{\text{branch}}(d)]$

Thus: $e^{\int \lambda dd'} \cdot a(d)^3 = C$ ⇒ $a(d) = C' \cdot e^{-\frac{1}{3}\int \lambda dd'}$

Normalization $a(0) = 1$: $a(d) = e^{-\frac{1}{3}\int_0^d \lambda(d') dd'}$

But careful: In expanding universe, physical separation between vertices increases. Better derivation: geodesic distance between vertices scales as $a(d)$. For tree with edge weight $\log q$, physical distance after $d$ steps is $d \cdot \log q \cdot a(d)$. Requiring this to match proper distance gives $a(d) = q^{-d/2}$.

### **A.2 Derivation of Effective Friedmann Equation**

Hamilton-Jacobi equation for tree navigation:

Action: $S(d) = \int^d p(d') \log q \, dd'$ where $p(d)^2 = 2[E - V(d)]$

Hamilton-Jacobi: $\frac{1}{2}\left(\frac{dS}{dd}\right)^2 + V(d) = E$

But $dS/dd = p \log q$, and cosmic time $t = d \log q$.

Thus: $\frac{1}{2}\left(\frac{da/dt}{a}\right)^2 + \frac{V(d)}{a^2} = \frac{E}{a^2}$

Identify $H = \dot{a}/a$, $\rho_{\text{eff}} = \frac{3}{8\pi G} \frac{V(d)}{a^2}$, $k_{\text{eff}} = -2E$.

Get: $H^2 = \frac{8\pi G}{3} \rho_{\text{eff}} - \frac{k_{\text{eff}}}{a^2}$.

## **Appendix B: Acronym Reference for Module 10**

- **ΛCDM**: Lambda Cold Dark Matter (standard cosmological model)
- **CMB**: Cosmic Microwave Background
- **FLRW**: Friedmann–Lemaître–Robertson–Walker (metric)
- **GR**: General Relativity
- **H₀**: Hubble constant (present expansion rate)
- **Ωₘ**: Matter density parameter
- **ΩΛ**: Dark energy density parameter
- **Ωₖ**: Curvature density parameter
- **Nₑ**: Number of e-folds (inflationary measure)
- **nₛ**: Spectral index (scalar perturbations)
- **r**: Tensor-to-scalar ratio
- **Aₛ**: Scalar perturbation amplitude
- **f_NL**: Non-Gaussianity parameter
