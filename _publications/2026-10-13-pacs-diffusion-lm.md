---
title: "Match the Canvas, Not Just the Answer: Predictability-Aware SFT for Diffusion Language Models"
collection: publications
permalink: /publication/2026-pacs-diffusion-lm/
excerpt: 'PACS, a supervised fine-tuning method for diffusion language models that uses the model&rsquo;s own predictability to better match training to inference, with gains of up to 12.84 percentage points over vanilla SFT on individual reasoning and code benchmarks.'
date: 2026-10-13
venue: 'arXiv preprint arXiv:2610.18001'
paperurl: 'https://arxiv.org/abs/2610.18001'
citation: 'Miao Li, Hanyang Jiang, Hengyu Fu, Baihe Huang, Yating Liu, Yuhang Cai, <b>Changkun Guan</b>, Zhongzhu Chen, Jiecheng Lu, Michael A. Boateng, Pascal Van Hentenryck. &quot;Match the Canvas, Not Just the Answer: Predictability-Aware SFT for Diffusion Language Models.&quot; <i>arXiv preprint arXiv:2610.18001</i>, 2026.'
---

Diffusion language models generate text in parallel, revealing tokens in the order the model finds them predictable rather than strictly left to right. That flexibility creates training choices that autoregressive teacher forcing never faces: which reference tokens are visible when a target is supervised, and how much generation space is allocated. Standard supervised fine-tuning (SFT) typically makes these choices by random masking, independently of how the model decodes at inference.

The paper shows how this training-inference mismatch can misdirect supervision. Random masking can hide prediction errors or penalize uncertainty that decoding would have resolved, and the visible input length can change which formulation of a response the model prefers. **PACS** (Predictability-Aware Canvas Selection and Supervision) uses the model's own predictability to choose each example's visible input length, and supervises reference tokens just before decoding would reveal them. Across reasoning and code-generation benchmarks, PACS has the highest mean accuracy among the compared SFT methods, with gains of up to 12.84 percentage points over vanilla SFT on individual benchmarks.

[Paper on arXiv](https://arxiv.org/abs/2610.18001)
