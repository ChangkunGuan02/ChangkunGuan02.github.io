---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
------
* **Ph.D. in Operations Research**, Georgia Institute of Technology, 2024–Present
  * H. Milton Stewart School of Industrial and Systems Engineering (ISyE)
* **B.S. in Applied Mathematics** (Honors, Concentration in Statistics) and **B.A. in Computer Science**, Bucknell University, 2020–2024
  * Graduated **Summa Cum Laude**

Research experience
------
* **Graduate Researcher**, Georgia Institute of Technology — ISyE (2024–Present)
  * Machine learning for operations research: deep learning-driven contextual stochastic optimization for real-time order fulfillment (NeurIPS ML&times;OR Workshop 2025)

* **Honors Thesis**, Bucknell University (2024)
  * *The Precedence-Constrained Quadratic Knapsack Problem* — developed exact and approximate solution methods, experimented with heuristics and metaheuristics, and generated difficult benchmark instances for this previously unstudied NP-hard problem
  * Advisor: Dr. Lucas Waddell

* **Undergraduate Researcher**, Bucknell University — Structure of Optimal Covering Arrays (2022–2024)
  * Studied optimization of combinatorial interaction testing with binary parameters and constraints; worked on proofs about the structure of optimal solutions and implemented models in Gurobi and algorithms in Python
  * Proposed and received funding from Bucknell's Program for Undergraduate Research
  * Principal Investigator: Dr. Thiago Serra

* **Undergraduate Researcher**, Bucknell University — Crouzeix's Conjecture (2022)
  * Co-authored a geometric analysis establishing the level set Crouzeix conjecture for classes of nilpotent matrices, published in *Concrete Operators* (2024); presented at the Joint Mathematics Meetings 2023 in Boston
  * Developed a Mathematica tool for fast visualization of numerical ranges
  * Principal Investigator: Dr. Kelly Bickel

Awards & honors
------
* **The Pi Mu Epsilon Society Prize**, Bucknell University, 2024 — awarded to the member of the graduating class with the most outstanding work in mathematics
* **INFORMS Undergraduate Scholarship**, INFORMS, 2023
* **Mathematics Scholarship**, Bucknell University, 2020–2024
* **The Professor George Morris Philips Prize**, Bucknell University, 2020 — outstanding academic performance in mathematics
* **Dean's List**, Bucknell University — all semesters
* Honor societies: **Pi Mu Epsilon** (mathematics, 2023), **Omega Rho** (operations research, 2023), **Tri-Alpha** (first-generation students, 2023)

Skills
------
* **Optimization**: integer programming, combinatorial optimization, stochastic optimization, Gurobi
* **Programming**: Python, R, Java, Mathematica
* **Machine learning**: deep learning for decision making, learning-to-optimize
* **Languages**: English, Mandarin Chinese

Publications
------
  <ul class="cv-list">{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Talks
------
  <ul class="cv-list">{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>

Teaching
------
  <ul class="cv-list">{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

<br>
A PDF version of my CV is available <a href="{{ base_path }}/files/cv.pdf">here</a>.
