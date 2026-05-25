# PDF Pipeline Test

**Date:** 2026-05-25

## Purpose

This file exists solely to trigger the `build-pdfs.yml` GitHub Actions workflow in the QNFO/.github repository.

## Test Content

The Bruhat-Tits tree $T_p$ is a $(p+1)$-regular tree whose vertices correspond to homothety classes of $\mathbb{Z}_p$-lattices in $\mathbb{Q}_p^2$. The boundary $\partial T_p$ is homeomorphic to $\mathbb{P}^1(\mathbb{Q}_p)$.

The strong triangle inequality $|x + y|_p \leq \max(|x|_p, |y|_p)$ ensures that errors propagate only within their tree branch, never crossing branches.

## Math Rendering Test

$$d(x, y) = p^{-v_p(x - y)}$$

$$\int_{\mathbb{Q}_p} f(x) \, d\mu(x) = \sum_{n=-\infty}^{\infty} \int_{|x|_p = p^n} f(x) \, d\mu(x)$$

## Verification

If this PDF builds successfully, the GitHub Actions pipeline is operational.
