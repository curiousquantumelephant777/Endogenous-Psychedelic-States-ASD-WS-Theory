import numpy as np
import matplotlib.pyplot as plt

# 1. Define the categories for our "Mirror" states
categories = ['ASD-like\n(High INMT / High GTF2I)', 'WS-like\n(High PEA / Low GTF2I)']

# 2. Data Points (Normalized 0.0 to 1.0)
# ASD: High Master Regulator (GTF2I) -> High Enzyme (INMT) -> Low Trace Amine (PEA)
# WS: Low Master Regulator (Deletion) -> Low Enzyme (INMT) -> High Trace Amine (PEA)
gtf2i_activity = [0.90, 0.15]
inmt_activity = [0.85, 0.25]
pea_levels = [0.20, 0.95]

x = np.arange(len(categories))  # Label locations
width = 0.25                    # Width of the individual bars

fig, ax = plt.subplots(figsize=(10, 6))

# 3. Create the bars with the blue, purple, pink color palette
# Royal Blue for the Master Regulator, Medium Purple for the Enzyme, Hot Pink for the Amine
rects1 = ax.bar(x - width, gtf2i_activity, width, label='GTF2I Activity', color='royalblue', alpha=0.85)
rects2 = ax.bar(x, inmt_activity, width, label='INMT Activity', color='mediumpurple', alpha=0.85)
rects3 = ax.bar(x + width, pea_levels, width, label='PEA Levels', color='hotpink', alpha=0.85)

# 4. Styling and Labels
ax.set_ylabel('Relative Intensity (0.0 - 1.0)', fontsize=12)
ax.set_title('The GTF2I-INMT-PEA Shunt: ASD vs. Williams Syndrome', fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=11)
ax.set_ylim(0, 1.1)
ax.legend(frameon=True, loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3)
ax.grid(axis='y', linestyle='--', alpha=0.4)

# 5. Helper function to add value labels on top of each bar
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9, fontweight='bold')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.tight_layout()
plt.show()
