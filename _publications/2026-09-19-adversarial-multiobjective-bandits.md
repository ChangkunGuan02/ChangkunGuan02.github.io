---
title: "The Role of Coordinates in Pareto Regret for Adversarial Multi-Objective Bandits"
collection: publications
permalink: /publication/2026-adversarial-multiobjective-bandits/
excerpt: 'In adversarial multi-objective bandits, an easier coordinate cannot lower the worst-case order of Pareto regret when the learner does not know which coordinate it is. We prove a minimax lower bound and match it with Poly-INF and an adaptive reward-doubling variant.'
date: 2026-09-19
venue: 'arXiv preprint arXiv:2609.23092'
paperurl: 'https://arxiv.org/abs/2609.23092'
citation: '<b>Changkun Guan</b>, Mengfan Xu. &quot;The Role of Coordinates in Pareto Regret for Adversarial Multi-Objective Bandits.&quot; <i>arXiv preprint arXiv:2609.23092</i>, 2026.'
---

In adversarial multi-objective bandits, each arm's reward is a vector chosen by an adversary, and performance is measured by Pareto regret. Measure how easy a coordinate is by the smallest cumulative loss of any arm on it. Earlier work suggested that an easier coordinate can reduce Pareto regret. In practice, though, the learner may not know which coordinate is the easy one.

**Negative result.** Without that knowledge, a smaller cumulative loss does not improve the worst-case order of Pareto regret. For at least 4 arms, at least 6 rounds, and at least 2 coordinates, we prove a minimax lower bound of &Omega;(min{T &minus; L<sub>0</sub>, &radic;(K(T &minus; L<sub>0</sub>))}) on expected Pareto regret, where K is the number of arms, T the number of rounds, and L<sub>0</sub> = min<sub>d</sub> L<sub>d</sub> is the smallest cumulative loss over all coordinates. The bound holds even when L<sub>0</sub> itself is known.

**Positive result.** Coordinates other than the easiest one can still achieve the optimal rate. When L<sub>0</sub> is known, running Poly-INF on a fixed coordinate gives a matching upper bound. When it is unknown, a reward-doubling version of Poly-INF adapts to it and still attains the minimax rate, with no extra log T factor and no dependence on the number of coordinates.

This is the adversarial companion to our paper on [stochastic multi-objective bandits](/publication/2026-multiobjective-bandits/).

[Paper on arXiv](https://arxiv.org/abs/2609.23092)
