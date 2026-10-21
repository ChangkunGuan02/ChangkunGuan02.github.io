---
title: "OPTAgent: LLM Agents for Solver Ecosystems"
excerpt: "<i>Georgia Tech, 2026 — NeurIPS 2026 ML&times;OR Workshop</i>"
collection: portfolio
area: mlxopt
date: 2026-12-11
---

The optimization toolbox keeps growing: more solver methods, more configurations, more complementary procedures. Each is usually developed and benchmarked on its own, which leaves practitioners with a hard question. Which method should be used on this instance, and with what share of a limited, shared compute budget?

**OPTAgent** (joint with Hanyang Jiang and Miao Li as co-first authors, and with Danlin Li, Sikai Cheng, Pascal Van Hentenryck, and Russell Bent) is an agentic policy-synthesis framework. During offline discovery, a large language model proposes and searches a space of compact decision-tree policies. Each policy selects and configures optimization methods and allocates the computational budget across a whole collection of problems.

**Key ideas:**
- Shift the unit of design from a standalone solver to a deployment-aware ecosystem of solvers
- Use an LLM as a search engine over interpretable decision-tree policies rather than as a solver itself
- Treat compute availability as a first-class part of method selection and configuration

[Paper on OpenReview](https://openreview.net/forum?id=ydWJ4mL4nu)
