# GIV Presentation — Outline

## Audience and rhetoric
- **Audience:** Macro lab group (Working Deck / Academic Seminar hybrid — 80% Logos, 10% Ethos, 10% Pathos).
- **Tone:** Scott's House Style (Warm Professional).
- **Figures/Code:** No code, stick to equations and TikZ diagrams for the theory.
- **Key Takeaway:** "A few large actors (like major firms or industries) significantly impact aggregate outcomes."

## Theme
- **Palette:** Warm Professional (DeepNavy core, Teal/WarmOrange accents).
- **Typography:** Sans-serif (lmodern), minimum 24pt body text, no justified text.
- **Style:** Assertion titles, minimal bullets, generous whitespace, one idea per slide.

## The arc

### Act I: Setup (Slides 1–3)
  1. **Title Slide:** Granular Instrumental Variables (GIVs)
  2. **Opening:** Idiosyncratic shocks to large firms are not just noise
  3. **The Stakes:** Endogeneity prevents the estimation of aggregate elasticities

### Act II: The Simple Model (Slides 4–8)
  4. **The Setup:** A simple model of supply and demand with a single common factor
     - *Notation:* $p_t = \psi y_{St} + \varepsilon_t$ (Supply), $y_{it} = \phi^d p_t + \eta_t + u_{it}$ (Demand)
  5. **The Problem:** OLS fails because prices and aggregate shocks are correlated
     - *Intuition:* $\eta_t$ and $\varepsilon_t$ confound standard estimation
  6. **The Solution:** Constructing the Granular Instrumental Variable ($z_t$)
     - *Notation:* $z_t := y_{\Gamma t} = y_{St} - y_{Et}$
  7. **The Mechanism:** The GIV isolates purely idiosyncratic shocks
     - *Notation:* $z_t = u_{\Gamma t} = u_{St} - u_{Et}$
  8. **The Estimation:** The same instrument yields both supply and demand elasticities
     - *Notation:* $\psi = \frac{\mathbb{E}[p_t z_t]}{\mathbb{E}[y_{St} z_t]}$ and $\phi^d = \frac{\mathbb{E}[y_{Et} z_t]}{\mathbb{E}[p_t z_t]}$

### Act III: Resolution (Slides 9–10)
  9. **Implications:** GIV precision relies on concentration and volatile micro-shocks
     - *Concept:* Requires a large excess Herfindahl index
  10. **Closing:** A few large actors (like major firms or industries) significantly impact aggregate outcomes.
