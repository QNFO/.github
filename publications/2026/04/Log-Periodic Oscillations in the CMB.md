---
modified: 2026-04-13T13:12:08Z
---
**To:** CMB-S4, Simons Observatory, and Planck Legacy Archive
**From:** Rowan Brad Quni-Gudzinas
**Date:** 2026-04-13
**Subject:** Log-Periodic Oscillations in the CMB

**1. Theoretical Motivation:**
The Syntactic Token Calculus (STC), a pre-geometric theory of physics, posits that the universe is fundamentally a discrete, hierarchical structure (a Bruhat-Tits tree). This structure exhibits discrete scale invariance, not continuous scale invariance. A direct consequence is that the primordial power spectrum of fluctuations, and therefore the CMB angular power spectrum $C_\ell$, should not be a simple power law but should be modulated by log-periodic oscillations.

**2. The Predicted Signature:**
The angular power spectrum $C_\ell$ is predicted to have the form:
$$ \ell(\ell+1)C_\ell = A \left(\frac{\ell}{\ell_0}\right)^{1-n_s} \left[1 + B \cos\left(\frac{2\pi}{\ln q} \ln\left(\frac{\ell}{\ell_0}\right) + \phi\right)\right] $$
where $q$ is the fundamental scaling ratio of the cosmic web (hypothesized to be related to $e$ or $\pi$), $B$ is the oscillation amplitude, and $\phi$ is a phase. The key signature is a periodic oscillation in the logarithm of the multipole moment $\ell$.

**3. Data Analysis Protocol:**
We propose a three-step protocol to search for this signature in existing and future CMB data:

*   **Step 1: Logarithmic Re-sampling.**
    Take the cleaned, foreground-subtracted $C_\ell$ data. Instead of plotting it against $\ell$, plot it against $x = \ln(\ell)$. Interpolate the data to create a new dataset that is uniformly sampled in $x$. This transforms the log-periodic signal into a standard periodic signal.

*   **Step 2: Fourier Analysis.**
    Perform a Fourier transform (or, for unevenly sampled/gapped data, a Lomb-Scargle periodogram) on the log-sampled data from Step 1. The power spectrum of this transformed data will reveal the frequencies present in the log-domain.

*   **Step 3: Peak Detection and Significance.**
    Search the resulting power spectrum for statistically significant peaks. A peak at frequency $\omega$ corresponds to a scaling ratio $q = \exp(2\pi/\omega)$. The significance of any peak must be evaluated against the null hypothesis (standard $\Lambda$CDM with cosmic variance) using Monte Carlo simulations.

**4. Falsification Criterion:**
If a comprehensive search of the Planck, ACT, SPT, and future CMB-S4 data reveals no statistically significant ($>3\sigma$) log-periodic oscillations, this would place strong constraints on the STC, potentially falsifying its simplest cosmological predictions.

**5. Conclusion:**
This search represents a direct, powerful, and low-cost test of a fundamental prediction of a new physical theory. A confirmed detection would provide the first evidence for a discrete, hierarchical structure of spacetime. We urge the experimental community to undertake this analysis.
