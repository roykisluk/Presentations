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
- The GIV procedure isolates idiosyncratic shocks by adjusting weights to remove common factors. In the simplest case with common factor loadings, the GIV is the "size-weighted" minus the "equal-weighted" value of outcomes ($z_t = y_{St} - y_{Et}$).
- **Optimal Weights**: The optimal GIV weights ($\Gamma^*$) maximize the squared correlation with the idiosyncratic shock component while remaining orthogonal to common factor loadings ($\Gamma' \lambda = 0$).

## 4. Data
The paper presents a general framework applicable to many datasets. Examples mentioned include:
- Supply and demand (e.g., oil market, Kuwait's production drop).
- Firm-level shocks and their transmission through banking systems.
- Asset portfolios and insurer equity valuations.
- Currency flows and exchange rates.
- Wage concentration and firm-level shocks.
- The method relies on panel data with $N$ entities and $T$ time periods, where $N$ is fixed and $T \to \infty$.

## 5. Statistical Methods
- **OLS and IV estimation** using GIV.
- **Factor Models**: Used to capture demand-side aggregate shocks ($\lambda_i \eta_t$).
- **GMM Estimation**: Used when factor loadings ($\lambda$) are not known but estimated, using specific moment conditions to identify elasticities and factor loadings simultaneously.
- **Diagnostics**: 
    - **Power analysis**: Calculated using excess Herfindahl ($h = \sqrt{\sum S_i^2 - 1/N}$) and shock volatilities.
    - **Narrative checks**: Comparing GIV realizations with historical events (e.g., policy announcements, wars).
    - **Overidentification tests**: Testing consistency across different subsets of entities.

## 6. Findings
- GIVs are strong instruments when:
    1. A few large actors account for a substantial fraction of aggregate activity (high concentration).
    2. Idiosyncratic shocks are volatile relative to aggregate shocks.
- The standard errors for GIV estimators are shown to be consistent even when the GIV is a generated regressor, provided common factors are correctly handled.
- GIV estimators are robust to mismeasurement of size weights and heterogeneity in elasticities.
- The main risk is "leaky" controls where common factors are not fully removed, creating bias proportional to the correlation between factor loadings and entity size.

## 7. Contributions
- Provides a systematic, novel identification strategy for "granular" settings.
- Formalizes the "Granular Instrumental Variable" approach as a bridge between micro-shocks and macro-outcomes.
- Extends the model to handle heterogeneous demand elasticities, latent factor estimation, and heteroskedasticity.
- Situates GIV within the "credibility revolution" by allowing for narrative validation of the underlying "treatments" (idiosyncratic shocks).

## 8. Replication Feasibility
- Highly feasible for researchers with panel data on size and outcomes.
- Requires estimating or assuming factor loadings ($\lambda$).
- The paper provides explicit formulas for optimal weights ($\Gamma = QS$) and asymptotic variances.
- A replication archive likely exists given the numerous applied examples cited (e.g., oil market, banking, exchange rates).
