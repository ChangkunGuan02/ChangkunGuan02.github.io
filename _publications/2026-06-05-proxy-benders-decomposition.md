---
title: "The Proxy Benders Decomposition"
collection: publications
permalink: /publication/2026-proxy-benders-decomposition/
excerpt: 'A decomposition framework that replaces Benders subproblem optimization with certified optimization proxies, producing provably valid cuts via a self-supervised predict-project-and-complete mechanism. Up to 161&times; median speedups on large facility location instances.'
date: 2026-06-05
venue: 'arXiv preprint arXiv:2606.07403'
paperurl: 'https://arxiv.org/abs/2606.07403'
citation: '<b>Changkun Guan</b>, El Mehdi Er Raqabi, Mathieu Tanneau, Pascal Van Hentenryck. &quot;The Proxy Benders Decomposition.&quot; <i>arXiv preprint arXiv:2606.07403</i>, 2026.'
---

Classical Benders decomposition relies on repeatedly solving subproblems to optimality. The Proxy Benders Decomposition (Proxy-BD) replaces subproblem optimization with **certified optimization proxies**: a self-supervised predict-project-and-complete mechanism that produces dual-feasible solutions and therefore provably valid Benders cuts. A certification layer maintains theoretical validity regardless of prediction accuracy, and the approach extends to modern decomposition schemes.

On large uncapacitated facility location instances, Proxy-BD achieves median optimality gaps below 0.5%, yields up to 161&times; median speedups, and reduces the number of generated cuts by more than 240&times; on the largest instances.

[Paper on arXiv](https://arxiv.org/abs/2606.07403)
