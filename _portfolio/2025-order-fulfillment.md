---
title: "Deep Learning for Real-Time Order Fulfillment"
excerpt: "<i>Georgia Tech, 2025–2026 — NeurIPS ML&times;OR 2025 &amp; arXiv:2606.25362</i>"
collection: portfolio
area: mlxopt
date: 2026-06-24
---

Order fulfillment is a fundamental challenge in large-scale e-commerce: every incoming order requires a real-time decision about where and how to fulfill it, under uncertainty in delivery timeliness and future inventory consumption.

In this project (joint with Tinghan Ye, Shuaicheng Tong, Beste Basciftci, and Pascal Van Hentenryck), we introduce a two-stage contextual stochastic optimization framework that captures both sources of uncertainty, and develop deep neural networks that approximate its solutions for real-time deployment during peak hours, when traditional solvers are computationally prohibitive.

The extended version, [*Learning Optimization Proxies for Sequential Contextual Stochastic Programs: An Order Fulfillment Application*](https://arxiv.org/abs/2606.25362) (2026), shows the learned proxies decide roughly 2,800&times; faster than solvers while improving fulfillment cost and halving late deliveries relative to established policies.

**Key contributions:**
- Two-stage contextual stochastic optimization formulation for real-time order fulfillment
- Deep learning models that approximate optimization solutions at deployment scale
- Presented at the NeurIPS 2025 Workshop on Machine Learning in Operations Research (ML&times;OR)

[Paper on OpenReview](https://openreview.net/forum?id=uhF4sYW6Nd)
