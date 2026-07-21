---
title: "Optimal Combinatorial Testing with Constraints: The Balancing Act"
collection: publications
permalink: /publication/2026-combinatorial-testing/
excerpt: 'Revisits pairwise-coverage combinatorial testing on binary parameters, contrasting the unconstrained and NP-hard constrained cases, with the first exact integer-programming algorithm and a fast, often-optimal heuristic.'
date: 2026-07-19
venue: 'arXiv preprint arXiv:2607.17083'
paperurl: 'https://arxiv.org/abs/2607.17083'
citation: 'Thiago Serra, <b>Changkun Guan</b>, Hunter Gehman, Sumit Dhar, Mikey Ferguson, John Hooker, Marcel Schoppers. &quot;Optimal Combinatorial Testing with Constraints: The Balancing Act.&quot; <i>arXiv preprint arXiv:2607.17083</i>, 2026.'
---

Testing a system with many on-off components exhaustively is prohibitive, but most bugs can be isolated to interactions among few components — so test suites covering every pairwise configuration are a practical foundation. The problem goes from easy to NP-hard as soon as some pairwise configurations are forbidden.

This paper revisits unconstrained combinatorial testing with pairwise coverage on binary parameters and contrasts it with the constrained case, showing and conjecturing properties that either are upheld or change between the two — in particular, the extent to which it remains a good idea (and sometimes provably optimal) to have every parameter set on almost as often as off. We propose the first exact algorithm based on integer programming and a faster heuristic that often produces optimal solutions, both outperforming or competitive with their baselines.

This paper grew out of my undergraduate research on the structure of optimal covering arrays at Bucknell.

[Paper on arXiv](https://arxiv.org/abs/2607.17083)
