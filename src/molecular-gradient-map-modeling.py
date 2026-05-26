# Modeling the molecular vector gradient map: start with the SMILES string for 2C-B (replace it with whichever molecule you are interested in mapping the electron density as a vector gradient field for, e.g., bufotenine, oxytocin, MDMA, octopamine, or beta-phenethylamine) 
smiles_2cb = "COc1cc(c(cc1OC)Br)CCN"
mol_2cb = Chem.MolFromSmiles(smiles_2cb)
mol_2cb = Chem.AddHs(mol_2cb)
AllChem.EmbedMolecule(mol_2cb, AllChem.ETKDG())

# Extract 2D coordinates
conf_2cb = mol_2cb.GetConformer()
atom_positions_2cb = [[conf_2cb.GetAtomPosition(i).x, conf_2cb.GetAtomPosition(i).y] for i in range(mol_2cb.GetNumAtoms())]

# Generate the simulated electron density
rho_2cb = simulate_electron_density(X, Y, atom_positions_2cb)

# Calculate the gradient of the electron density
grad_y_2cb, grad_x_2cb = np.gradient(rho_2cb, y_range[1]-y_range[0], x_range[1]-x_range[0])

fig_2cb, ax_2cb = plt.subplots(figsize=(10, 8), facecolor='#301934')
ax_2cb.set_facecolor('#000033')

contour_plot_2cb = ax_2cb.contourf(X, Y, rho_2cb, levels=50, cmap='magma', alpha=0.8)
cbar_2cb = fig_2cb.colorbar(contour_plot_2cb, ax=ax_2cb)
cbar_2cb.set_label('Electron Density (ρ)', color='#FFD1DC')
cbar_2cb.ax.tick_params(colors='#FFD1DC')

ax_2cb.quiver(X[::skip, ::skip], Y[::skip, ::skip], grad_x_2cb[::skip, ::skip], grad_y_2cb[::skip, ::skip],
           color='#FFD1DC', alpha=0.7, scale=50, width=0.003, headwidth=3, headlength=4)

ax_2cb.set_title('Simulated Electron Density and its Gradient Vector Field (2C-B)', color='#FFD1DC')
ax_2cb.set_xlabel('X-coordinate', color='#FFD1DC')
ax_2cb.set_ylabel('Y-coordinate', color='#FFD1DC')

ax_2cb.tick_params(axis='x', colors='#FFD1DC')
ax_2cb.tick_params(axis='y', colors='#FFD1DC')

ax_2cb.set_aspect('equal')
plt.show()
