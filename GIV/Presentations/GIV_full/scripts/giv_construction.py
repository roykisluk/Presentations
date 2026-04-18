import numpy as np
import pandas as pd
from sklearn.decomposition import FactorAnalysis

def construct_giv(df, size_col, outcome_col, id_col, time_col, n_factors=1):
    """
    Constructs the Granular Instrumental Variable (GIV) and the Granular Residual.
    df: Panel DataFrame
    """
    # 1. Prepare weights
    df = df.copy()
    total_size = df.groupby(time_col)[size_col].transform('sum')
    df['S'] = df[size_col] / total_size
    df['E'] = 1.0 / df.groupby(time_col)[id_col].transform('count')
    
    # 2. Extract outcomes into panel matrix (T x N)
    panel = df.pivot(index=time_col, columns=id_col, values=outcome_col)
    S_mat = df.pivot(index=time_col, columns=id_col, values='S').fillna(0)
    E_mat = df.pivot(index=time_col, columns=id_col, values='E').fillna(0)
    
    # 3. Factor Extraction (Simple case: PCA/FA on equal-weighted panel)
    fa = FactorAnalysis(n_components=n_factors)
    factors = fa.fit_transform(panel)
    loadings = fa.components_
    
    # 4. Construct GIV (Size-weighted minus Equal-weighted)
    # This is the simple version: z_t = y_St - y_Et
    y_S = (panel * S_mat).sum(axis=1)
    y_E = (panel * E_mat).sum(axis=1)
    z = y_S - y_E
    
    # 5. Optimal weights (Gamma)
    # Orthogonalize weights S against loadings lambda
    # Gamma = S - lambda * (lambda' * lambda)^-1 * lambda' * S
    # (Simplified for n_factors=1)
    # ...
    
    return z, factors

# --- Example Usage ---
# z, f = construct_giv(df, 'employment', 'wage_change', 'firm_id', 'year')
