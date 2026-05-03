# BLM 2019

## Research question
Identifying the contributions of worker and firm heterogeneity to earnings dispersion. Specifically, what is the nature of sorting patterns between heterogeneous workers and firms, and what are the sources of earnings inequality?

## Audience
Labor economists and econometricians interested in the sources of wage inequality, firm wage premiums, sorting in the labor market, and structural/reduced-form estimation of matched employer-employee data.

## Method
The authors propose an empirical framework to identify and estimate earnings distributions and worker composition on matched panel data, allowing for two-sided worker-firm unobserved heterogeneity and complementarities. They introduce two models:
1. **Static model**: Allows for nonlinear interactions between workers and firms.
2. **Dynamic model**: Allows for Markovian earnings dynamics and endogenous mobility (mobility depending on earnings).

They use a dimension reduction technique and a two-step estimation approach:
1. **Classification step**: Group firms into a finite number of classes ($K$) using $k$-means clustering based on their empirical earnings distributions (cdfs).
2. **Estimation step**: Estimate the model parameters (worker type proportions, earnings distributions) conditional on the estimated firm classes using maximum likelihood, treating worker types as a finite mixture.

## Data
Swedish matched employer-employee administrative panel data. The application focuses on males for the 2002–2004 period (for the static model) and the 2001–2005 period (for the dynamic model).
Specific registries used include:
- RAMS (labor market statistics) and ANST for employment and employers.
- LOUISE/LINDA for worker information.
- SBS for accounting and balance sheet information for non-financial corporations.
- Unemployment Register.
Sample selection is conservative, focusing on fully employed males in the private sector, resulting in low mobility rates (e.g., 3.3% for the 2002-2004 sample).

## Statistical methods
- $k$-means clustering on empirical cumulative distribution functions (cdfs) of log-earnings to classify firms.
- Finite mixture models to represent discrete worker types.
- Two-step grouped fixed-effects estimation.
- Expectation-Maximization (EM) algorithm to maximize the likelihood function for both static and dynamic models.
- Nonparametric identification proofs based on the existence of "connecting cycles" of job movers between firm classes.
- Parametric bootstrap for standard errors.
- Robustness checks estimating persistence parameters in first differences, and reclassifying firms.

## Findings
- Log-earnings are approximately additive in worker and firm heterogeneity, although there is evidence of some complementarities between firms and lower-type workers.
- Firm heterogeneity (net of worker composition) accounts for a small share of the overall variance in log-earnings (less than 5%).
- The largest share of variance is explained by worker heterogeneity (around 60%).
- There are strong sorting patterns between workers and firms: the correlation between worker and firm heterogeneity is estimated to be between 30% and 50%.
- Dynamic findings: Low earnings realizations (conditional on worker and firm heterogeneity) make workers more likely to move, violating the exogenous mobility assumption of static models. Specifically, workers in the first conditional decile of earnings are much more likely to move than those in the tenth decile.
- State dependence: Earnings after a job move depend directly on the previous employer (up to a 9% wage premium for coming from the highest class of firms).
- Network effect: The identity of the previous firm also matters because it influences the distribution of the class of the new firm.
- The results are robust to variations in the number of worker types ($L$) and firm classes ($K$), different model specifications (interactive regression, linear regression), and reclassification strategies.

## Contributions
- Bridges the gap between the tractable but restrictive AKM (two-way fixed effects) approach and complex structural models of sorting.
- Provides a computationally tractable framework that nests various theoretical mechanisms (complementarities, sorting, dynamics, Markovian match effects) without needing to fully specify a structural model.
- Establishes conditions for nonparametric identification of complementarities and sorting patterns in short panels (2 periods for static, 4 periods for dynamic), primarily relying on the mobility patterns and earnings of job movers.
- Demonstrates empirically that while log-earnings are mostly additive, sorting is strong, and mobility decisions are endogenous to earnings.
- Highlights that the large variance of firm effects often found with the standard AKM estimator in short panels is likely driven by incidental parameter bias (which their grouped fixed-effects estimator mitigates).

## Replication feasibility
- The theoretical framework and estimation strategy are well documented.
- The data is Swedish administrative data, which is typically confidential and requires special access permissions from IFAU, making direct replication of the empirical application difficult for researchers without such access.
- The paper mentions using simulated data based on Shimer and Smith (2000) to validate the estimator, which could be replicated.
