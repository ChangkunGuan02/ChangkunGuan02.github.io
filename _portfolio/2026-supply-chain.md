---
title: "End-to-End Supply Chain Planning in the Paper Industry"
excerpt: "<i>Georgia Tech, 2026 — arXiv:2607.16618</i>"
collection: portfolio
area: optimization
date: 2026-07-18
---

Large-scale paper manufacturing runs on a chain of decisions — production scheduling, trimming, vehicle loading, and multi-period demand fulfillment — that are traditionally optimized one stage at a time, leaving efficiency on the table. Integrating them into a single model is computationally daunting.

In this project (joint with Amira Hijazi and Pascal Van Hentenryck), we develop an exact model of the integrated end-to-end planning problem and a hybrid **BDCG-DP** framework: column generation with dynamic programming handles supply decisions, Benders decomposition handles fulfillment, and the two are coupled through the aggregate supply availability that links upstream and downstream stages.

**Key contributions:**
- An exact formulation of end-to-end paper-industry planning spanning four coupled stages
- A hybrid decomposition (column generation + dynamic programming + Benders) exploiting the problem's structure
- On proprietary industry instances: 24.4% cost reduction versus traditional CG-DP on eight-week problems, four-week runtimes cut from five hours to under one hour, and implementable integer-feasible plans within 2.3–6 hours

[Paper on arXiv](https://arxiv.org/abs/2607.16618)
