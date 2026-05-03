import numpy as np
import matplotlib.pyplot as plt
import os

# Create figures directory if it doesn't exist
os.makedirs('BLM/figures', exist_ok=True)

# Warm Professional Palette
colors = {
    'DeepNavy': '#2E4057',
    'Teal': '#048A81',
    'WarmOrange': '#E85D04',
    'Cream': '#FBF8F1',
    'WarmGray': '#6C757D'
}

firm_classes = np.arange(1, 11)

# Additive
high_type_additive = 10.5 + 0.05 * firm_classes
low_type_additive = 10.0 + 0.05 * firm_classes

# BLM Finding (Low types gain more from higher-wage firms)
high_type_blm = 10.5 + 0.02 * firm_classes
low_type_blm = 9.5 + 0.1 * firm_classes

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), facecolor=colors['Cream'])

for ax in [ax1, ax2]:
    ax.set_facecolor(colors['Cream'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(colors['DeepNavy'])
    ax.spines['bottom'].set_color(colors['DeepNavy'])
    ax.tick_params(colors=colors['DeepNavy'])
    ax.set_xlabel('Firm Class (ordered by mean wage)', color=colors['DeepNavy'], fontsize=12)
    ax.set_ylabel('Mean Log-Earnings', color=colors['DeepNavy'], fontsize=12)
    ax.set_xticks([2, 4, 6, 8, 10])

ax1.plot(firm_classes, high_type_additive, color=colors['Teal'], lw=3, marker='o')
ax1.plot(firm_classes, low_type_additive, color=colors['WarmOrange'], lw=3, marker='o')
ax1.text(10.2, high_type_additive[-1], 'High Type', color=colors['Teal'], va='center', fontsize=12, fontweight='bold')
ax1.text(10.2, low_type_additive[-1], 'Low Type', color=colors['WarmOrange'], va='center', fontsize=12, fontweight='bold')
ax1.set_title('AKM Assumption: Additive\n(Parallel wage gains)', color=colors['DeepNavy'], fontsize=14, pad=15)
ax1.set_xlim(0.5, 12.5)
ax1.set_ylim(9.0, 11.5)

ax2.plot(firm_classes, high_type_blm, color=colors['Teal'], lw=3, marker='o')
ax2.plot(firm_classes, low_type_blm, color=colors['WarmOrange'], lw=3, marker='o')
ax2.text(10.2, high_type_blm[-1], 'High Type', color=colors['Teal'], va='center', fontsize=12, fontweight='bold')
ax2.text(10.2, low_type_blm[-1], 'Low Type', color=colors['WarmOrange'], va='center', fontsize=12, fontweight='bold')
ax2.set_title('BLM Finding: Complementarity\n(Low types gain most from moving up)', color=colors['DeepNavy'], fontsize=14, pad=15)
ax2.set_xlim(0.5, 12.5)
ax2.set_ylim(9.0, 11.5)

plt.tight_layout()
plt.savefig('BLM/figures/figure_2.pdf', bbox_inches='tight')
