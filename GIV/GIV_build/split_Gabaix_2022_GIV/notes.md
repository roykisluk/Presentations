# Granular Instrumental Variables (Gabaix and Koijen, 2022) - Structured Extraction

## 1. Research Question
How to construct valid and powerful instruments in "granular" economies—where a few large players (firms, industries, or countries) account for a significant share of economic activity. The goal is to estimate causal parameters (like elasticities and multipliers) using the idiosyncratic shocks of these large players as instruments for aggregate endogenous variables.

## 2. Audience
Economists specializing in macroeconomics, finance, and industrial organization who deal with identification challenges in settings where aggregate variables are influenced by a small number of large entities.

## 3. Method
**Granular Instrumental Variables (GIV)**:
- The method extracts idiosyncratic shocks to large players.
- The GIV is constructed as the size-weighted sum of these idiosyncratic shocks.
- The core idea is that idiosyncratic shocks to large actors affect aggregate outcomes and are valid instruments because they are (by definition) uncorrelated with other aggregate shocks.
- The GIV procedure isolates idiosyncratic shocks by adjusting weights to remove common factors. In the simplest case with common factor loadings, the GIV is the "size-weighted" minus the "equal-weighted" value of outcomes.

## 4. Data
The paper presents a general framework applicable to many datasets. Examples mentioned include:
- Supply and demand (e.g., oil market, Kuwait's production drop).
- Firm-level shocks and their transmission through banking systems.
- Asset portfolios and insurer equity valuations.
- Currency flows and exchange rates.
- Wage concentration and firm-level shocks.

## 5. Statistical Methods
- **OLS and IV estimation** using GIV.
- **Factor Models**: Used to capture demand-side aggregate shocks ($\lambda_i \eta_t$).
- **Weighting**: Derivation of optimal weights ($\Gamma$) to maximize instrument strength and minimize variance.
- **GMM Estimation**: Used when factor loadings ($\lambda$) are not known but estimated, taking into account the variance from estimating the generated regressor.
- **Diagnostics**: Power analysis (using excess Herfindahl and shock volatilities), narrative checks, and overidentification tests (e.g., comparing GIVs from different subsets of entities like developing vs. developed countries).

## 6. Findings
- GIVs are strong instruments when:
    1. A few large actors account for a substantial fraction of aggregate activity (large excess Herfindahl index $h$).
    2. Idiosyncratic shocks are volatile relative to aggregate shocks.
- The standard errors of GIV estimators are properly derived, showing that GIVs can achieve good precision in concentrated economies.
- GIV estimators are robust to:
    - Including only a subset of large actors (e.g., top $K$ entities).
    - Mismeasurement of size distributions (OLS might be biased, but IV remains valid).
    - Heterogeneity in demand elasticities (estimates reflect equal-weighted averages in basic IV/OLS).
- Main threats to identification stem from failing to properly control for common factors, especially if factor loadings are correlated with size.

## 7. Contributions
- Provides a systematic, novel identification strategy for "granular" settings.
- Formalizes the "Granular Instrumental Variable" approach.
- Extends the model to handle heterogeneous demand elasticities, unknown/estimated factor loadings, and heteroskedastic idiosyncratic shocks.
- Discusses extensions to structural VARs and compares GIVs with Bartik instruments (noting them as complements rather than substitutes).

## 8. Replication Feasibility
- (In progress) The paper provides the theoretical foundations, moment conditions, and variance estimators required to implement the procedure. It emphasizes the need for narrative checks to label and validate the idiosyncratic shocks used in the GIV.
