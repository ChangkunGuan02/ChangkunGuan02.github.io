---
title: "Stochastic Multi-objective Bandits"
excerpt: "<i>2026 — arXiv:2604.07096</i>"
collection: portfolio
date: 2026-04-08
---

In multi-objective bandits, each arm's reward is a vector rather than a scalar, and performance is measured by Pareto regret. Whether the multi-objective setting is fundamentally harder than the classical one has been an open question in the stochastic regime.

In this work (joint with Mengfan Xu), we show that Pareto regret is governed by the largest objective-wise suboptimality gap g&dagger;: we prove a lower bound of order &Omega;(K log T / g&dagger;) and design an algorithm — confidence-bound estimators paired with a top-two racing mechanism — achieving matching O(K log T / g&dagger;) Pareto regret, with no dependence on the number of objectives.

**Key contributions:**
- Optimal upper and lower Pareto-regret bounds for stochastic multi-objective bandits
- An efficient algorithm with order-of-magnitude empirical regret improvements on synthetic and real datasets
- Evidence of a fairness–hardness tradeoff that has no single-objective analogue

[Paper on arXiv](https://arxiv.org/abs/2604.07096)
