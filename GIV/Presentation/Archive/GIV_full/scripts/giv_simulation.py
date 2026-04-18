import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# --- Palette: Warm Professional ---
DEEP_NAVY = "#2E4057"
TEAL = "#048A81"
WARM_ORANGE = "#E85D04"
WARM_GRAY = "#6C757D"
SOFT_WHITE = "#FAFAFA"

def run_simulation(N=100, T=500, alpha=1.0):
    """
    alpha: Zipf parameter for firm size distribution. Higher = more concentration.
    """
    # 1. Firm Size Distribution (Zipf-like)
    ranks = np.arange(1, N + 1)
    sizes = 1 / (ranks ** alpha)
    S = sizes / sizes.sum()
    
    # Herfindahl (Excess H)
    h_sq = np.sum(S**2) - (1/N)
    h = np.sqrt(max(0, h_sq))
    
    # 2. Shocks and Parameters
    phi = -0.5  # Demand elasticity
    psi = 1.0   # Supply elasticity
    
    u = np.random.normal(0, 1, (T, N))
    eta = np.random.normal(0, 1, T)
    eps = np.random.normal(0, 1, T)
    
    # Aggregate idiosyncratic shocks
    u_S = u @ S
    u_E = u.mean(axis=1)
    
    # 3. Solve for endogenous p_t
    # p_t = (psi*eta + psi*u_S + eps) / (1 - psi*phi)
    denom = 1 - psi * phi
    p = (psi * eta + psi * u_S + eps) / denom
    
    # 4. Aggregate outcomes
    y_S = phi * p + eta + u_S
    y_E = phi * p + eta + u_E
    
    # 5. GIV construction
    z = y_S - y_E
    
    # 6. First stage regression: y_S ~ z
    # (In a real model, we'd control for factors, but here factors are homogeneous)
    X = z.reshape(-1, 1)
    y = y_S
    reg = LinearRegression().fit(X, y)
    
    # Manual F-stat calculation for first stage
    y_pred = reg.predict(X)
    ssr = np.sum((y - y_pred)**2)
    s_sq = ssr / (T - 2)
    var_beta = s_sq / np.sum((z - z.mean())**2)
    f_stat = (reg.coef_[0]**2) / var_beta
    
    return h, f_stat

def main():
    alphas = np.linspace(0.1, 2.0, 30)
    results = [run_simulation(alpha=a) for a in alphas]
    h_vals, f_vals = zip(*results)
    
    # --- Plotting ---
    plt.figure(figsize=(10, 6), facecolor=SOFT_WHITE)
    ax = plt.gca()
    ax.set_facecolor(SOFT_WHITE)
    
    plt.plot(h_vals, f_vals, 'o-', color=TEAL, linewidth=2, markersize=8)
    
    plt.title("GIV Instrument Strength Increases with Market Concentration", 
              fontsize=18, fontweight='bold', pad=20, color=DEEP_NAVY)
    plt.xlabel("Excess Herfindahl Index ($h$)", fontsize=14, color=DEEP_NAVY)
    plt.ylabel("First-Stage $F$-statistic", fontsize=14, color=DEEP_NAVY)
    
    # Aesthetic cleanup
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    for spine in ['left', 'bottom']:
        ax.spines[spine].set_color(WARM_GRAY)
    
    ax.tick_params(colors=DEEP_NAVY)
    plt.grid(True, linestyle='--', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("figures/giv_concentration.pdf")
    print("Generated figures/giv_concentration.pdf")

if __name__ == "__main__":
    main()
