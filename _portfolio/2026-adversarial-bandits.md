---
title: "Adversarial Multi-objective Bandits"
excerpt: "<i>Georgia Tech, 2026 — arXiv:2609.23092</i>"
collection: portfolio
area: ml
date: 2026-09-19
---

When rewards are vectors chosen by an adversary, some coordinates may be easier than others, meaning some arm has a small cumulative loss on them. Can a learner exploit an easy coordinate to lower its Pareto regret, if it does not know which coordinate that is?

In this work (joint with Mengfan Xu), we show the answer is no in the worst case. We prove a minimax lower bound of &Omega;(min{T &minus; L<sub>0</sub>, &radic;(K(T &minus; L<sub>0</sub>))}), where K is the number of arms, T the number of rounds, and L<sub>0</sub> = min<sub>d</sub> L<sub>d</sub> is the smallest cumulative loss over all coordinates. The bound holds even when L<sub>0</sub> itself is known. We then show that the easiest coordinate is not needed to reach this rate. Poly-INF on a fixed coordinate matches the bound when L<sub>0</sub> is known, and a reward-doubling version of Poly-INF adapts when it is not.

**Key contributions:**
- A minimax lower bound showing an unknown easy coordinate cannot improve the worst-case order of Pareto regret
- Matching upper bounds with Poly-INF, plus a reward-doubling variant that adapts to an unknown L<sub>0</sub>
- No extra log T factor and no dependence on the number of coordinates

This is the adversarial companion to our [stochastic multi-objective bandits](/portfolio/2026-multiobjective-bandits/) work.

[Paper on arXiv](https://arxiv.org/abs/2609.23092)
