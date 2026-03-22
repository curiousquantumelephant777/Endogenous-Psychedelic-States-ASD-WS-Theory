!pip install rdkit py3Dmol -q
from rdkit import Chem
from rdkit.Chem import AllChem, Draw
import py3Dmol
print("RDKit & py3Dmol ready") #Installing the necessary packages

smiles = "CN(C)CCC1=CNC2=C1C=C(O)C=C2"  # bufotenin (5-HO-DMT)

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)

AllChem.EmbedMolecule(mol, randomSeed=42)
AllChem.MMFFOptimizeMolecule(mol)

mol_block = Chem.MolToMolBlock(mol)

view = py3Dmol.view(width=800, height=500)
view.addModel(mol_block, "mol")
view.setStyle({"stick": {}})
view.setBackgroundColor("#EBE8FC")
view.zoomTo()
view.setStyle({"atom": "O"}, {"stick": {"color": "purple", "radius": 0.25}})
view.show()
