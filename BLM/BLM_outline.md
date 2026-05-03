# BLM 2019 Presentation — Outline

## Audience and rhetoric
- **Audience:** PhD macro lab group (Academic seminar / research reading group).
- **Tone/Aesthetic:** Scott's house style (Warm Professional — DeepNavy, Teal, WarmOrange).
- **Rhetorical balance:** 50% Logos, 40% Ethos, 10% Pathos.
- **Focus:** Model setup, intuition for identification, and the core methodological contribution, as requested.
- **Code Language for conceptual figures:** TikZ for diagrams, Python for conceptual plots.
- **Format:** Beamer (default).
- **One Sentence Takeaway:** "By reducing firm heterogeneity to classes via clustering, we can tractably identify complex sorting and dynamic wage effects in matched data without the incidental parameter bias of two-way fixed effects."

## Theme
Scott's Warm Professional Beamer style. Clean, rigorous, sans-serif typography, with a focus on clear mathematical notation and uncluttered diagrams.

## The arc
### Act I (Slides 1–3): The Tension
  1. **Title:** A Distributional Framework for Matched Employer Employee Data
  2. **The Opening Hook:** Estimating wage dispersion with two-sided unobserved heterogeneity in short panels suffers from severe incidental parameter bias.
  3. **The Stakes:** We want to measure sorting and complementarities (as in search and matching models), but our standard empirical tools force us to assume them away to achieve tractability.

### Act II (Slides 4–11): The Model and Intuition (The Core)
  4. **The Baseline:** The AKM Model. $y_{it} = \alpha_i + \psi_{j(i,t)} + X_{it}'\beta + \varepsilon_{it}$. Additive separability and its implications (exogenous mobility, no complementarities).
  5. **The Framework:** Modeling worker types ($\alpha$) and firm classes ($k$). Why classes instead of individual firm fixed effects?
  6. **The Static Model:** Allowing for non-additive interactions. $Y_{it} = a_t(k_{it}) + b_t(k_{it})\alpha_i + X_{it}'c_t + \varepsilon_{it}$.
  7. **The Dynamic Model (Setup):** Endogenous mobility (mobility depends on current earnings) and state dependence (new wage depends on previous firm's class).
  8. **Intuition for Identification (Picture):** The "connecting cycle". How observing the same worker moving between different firm classes identifies the wage function. (Visual diagram of a cycle).
  9. **The Identification Rank Condition (Technical):** Formalizing the intuition — why we need asymmetric mobility patterns across classes.
  10. **Estimation Strategy:** Step 1. $k$-means clustering on empirical cdfs of firm earnings to group firms. 
  11. **Estimation Strategy:** Step 2. Grouped fixed-effects estimation using the EM algorithm.

### Act III (Slides 12–14): Resolution and Implications
  12. **Application Findings (Brief):** Applied to Swedish data, wages are mostly additive, but sorting is strong (correlation 30-50%). Mobility is endogenous to low earnings.
  13. **Implications for Macro/Labor:** We now have a tractable bridge between reduced-form AKM and fully structural search models.
  14. **Closing Slide:** "By reducing firm heterogeneity to classes, we can tractably identify complex sorting and dynamic wage effects without the incidental parameter bias of AKM."

## Figures and tables (code-first)
  - **Figure 1 (TikZ):** A connecting cycle diagram showing worker mobility between Firm Class $k$ and Firm Class $k'$ to illustrate the identification intuition.
  - **Figure 2 (Python/Matplotlib):** A conceptual plot illustrating additive vs. complementary wage structures across firm classes.
