---
title: "Stochastic Multi-objective Bandits"
excerpt: "<i>Georgia Tech, 2026 — arXiv:2604.07096</i>"
collection: portfolio
area: ml
date: 2026-04-08
---

In multi-objective bandits, each arm's reward is a vector rather than a scalar, and performance is measured by Pareto regret. Whether the multi-objective setting is fundamentally harder than the classical one has been an open question in the stochastic regime.

In this work (joint with Mengfan Xu), we show that Pareto regret is governed by the largest objective-wise suboptimality gap g&dagger;, so the multi-objective problem is surprisingly no harder than the single-objective one. Our algorithm keeps upper and lower confidence-bound estimators for every arm-objective pair, uses top-two races within each objective, and applies an uncertainty-greedy rule that steers exploration toward g&dagger;. It achieves O(log T / g&dagger;) Pareto regret with no dependence on the number of objectives, and a matching &Omega;(log T / g&dagger;) lower bound shows this is optimal.

**Key contributions:**
- Optimal upper and lower Pareto-regret bounds for stochastic multi-objective bandits
- An efficient algorithm with order-of-magnitude empirical regret improvements on synthetic and real datasets
- Evidence of a fairness–hardness tradeoff that has no single-objective analogue

Our follow-up studies the [adversarial setting](/portfolio/2026-adversarial-bandits/).

[Paper on arXiv](https://arxiv.org/abs/2604.07096)
