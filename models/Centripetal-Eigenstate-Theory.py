import numpy as npimport matplotlib.pyplot as pltdef generate_resonance_manifolds(iterations, state="WS"):
theta = np.linspace(0, 2 * np.pi, 2000)

if state == "WS":
# Floral Mandala Petals (432 Hz Resonance)
# Using cosine lobes for 'petal' flow
r = 0.5 + 0.5 * np.abs(np.cos(3 * theta))
for i in range(1, iterations + 1):
# Fractal stellation harmonics
r += (0.2 / i) * np.sin(6 * i * theta)
return theta, r, 'darkviolet', 'WS: Floral Mandala'

elif state == "ASD":
# Concentric Source (528 Hz Resonance)
np.random.seed(42)
r_base = 0.4 + 0.05 * np.sin(24 * theta)
# Fading signal toward periphery
noise = np.random.normal(0, 0.07, len(theta))
r = r_base + 0.05 + noise
return theta, np.maximum(r, 0.05), 'cornflowerblue', 'ASD: Concentric Source'

elif state == "Jagged":
# Jagged Edge (440 Hz Distortion / Cl-F Shielding)
np.random.seed(42)
r = 0.6 + 0.2 * np.sin(7 * theta)
for i in range(1, iterations + 1):
# High-entropy random spikes
r += (0.3 * np.random.normal(0, 1.0)) * np.sin(i * theta * 1.5)
return theta, r, 'crimson', 'Jagged Edge: Distorted Signaling'# Visualizing the Three Phases of the 7q11.23 Rheostat
plt.figure(figsize=(18, 6))for i, state in enumerate(["WS", "ASD", "Jagged"], 1):
t, r, color, label = generate_resonance_manifolds(12, state)
ax = plt.subplot(131 + (i-1), projection='polar')
ax.plot(t, r, color=color, lw=1.5, alpha=0.9)
ax.fill(t, r, color=color, alpha=0.15)
ax.set_title(label, pad=20, fontweight='bold')
ax.set_rticklabels([]); ax.set_xticklabels([])

plt.tight_layout()
plt.show()
