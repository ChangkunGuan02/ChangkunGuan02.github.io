---
title: "Proxy Benders Decomposition"
excerpt: "<i>Georgia Tech, 2026 — arXiv:2606.07403</i>"
collection: portfolio
area: mlxopt
date: 2026-06-05
---

Benders decomposition is a workhorse for large-scale optimization, but repeatedly solving subproblems to optimality is expensive. **Proxy-BD** (joint with El Mehdi Er Raqabi, Mathieu Tanneau, and Pascal Van Hentenryck) replaces subproblem optimization with certified optimization proxies: a self-supervised predict-project-and-complete mechanism that produces dual-feasible solutions, and therefore provably valid Benders cuts, without exact solves.

**Key contributions:**
- A certification layer that keeps the decomposition theoretically valid regardless of prediction accuracy
- Extensions to modern decomposition schemes beyond classical Benders
- Median optimality gaps below 0.5%, up to 161&times; median speedups, and over 240&times; fewer generated cuts on large uncapacitated facility location instances

[Paper on arXiv](https://arxiv.org/abs/2606.07403)
