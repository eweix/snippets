---
library: chemiinformatics
language: python
---


# Chemiinformatics

A suite of snippets for working with machine representations of chemical
structures and information. Mostly relies on rdkit for processing, though some
snippets involve pandas dataframes or other useful tools.

## Load molecule from SMILES

Use rdkit to load a molecule from a smiles string.

<!-- chem-smiles|chem-load-smiles|rd-smiles -->

```python
import rdkit.Chem as Chem

${1:mol} = Chem.MolFromSmiles(${2:smiles})$0
```

## Convert to canonical SMILES

Use rdkit to convert a SMILES string into a the canonical rdkit syntax.

<!-- chem-smiles-convert|rd-canon|rd-smiles-convert -->

```python
${1:mol} = Chem.MolFromSmiles(${2:smi})
${3:can_smi} = Chem.MolToSmiles(${1:mol}, canonical=True)
```

## Draw Morgan Bits

Use rdkit to draw the bits detected and encoded in the Morgan fingerprint of a
molecule.

<!-- chem-draw-struct|rd-draw -->

```python
import rdkit.Chem.Draw as Draw

${1:bi} = {}  # bit info
${2:fp} = AllChem.GetMorganFingerprintAsBitVect(${3:mol}, radius=${4:2}, nBits=${5:2048}, bitInfo=${1:bi})

idx = ${6:33} 
on_bits = [(mol, idx, bi)]
labels = [f"Bit {str(idx)}"]
Draw.DrawMorganBits(on_bits, molsPerRow=1, legends=labels)
radius = 2
length = 256
```

## Calculate chemical descriptors of a molecule

Use rdkit to obtain chemical descriptors of a molecule.

<!-- chem-desc|rd-desc -->

```python
import rdkit.Chem.Descriptors as Descriptors

${1:desc} = Descriptors.CalcMolDescriptors(${2:mol})
```

## Calculate Lipinski descriptors

Return a dictionary of the Lipinski characteristics of a molecule: molecular
weight, number of H-bond acceptors/donors, and solubility.

<!-- chem-lipinski|rd-lipinski -->

```python
import rdkit.Chem as Chem
import rdkit.Chem.Descriptors as Descriptors

${1:lipinski} = dict({
    "MolWt": Descriptors.MolWt(${2:mol}),
    "NumHAcceptors": Chem.Lipinski.NumHAcceptors(${2:mol}),
    "NumHDonors": Chem.Lipinski.NumHDonors(${2:mol}),
    ${3:# log solubility cannot be calculated purely from structure}
    })
$0
```

## One-hot Amino Acid Sequence Encoding

Create an encoder that converts a string of amino acids into a (21,n) one-hot
tensor encoding. Useful for machine learning tools, especially CNNs.

<!-- chem-enc-onehot|chem-seq2onehot -->
 
```python
def seq2onehot(sequence, max_length=${1:30}):
    """Convert a string of amino acids into a (21,n) one-hot encoding"""
    AMINOACIDS = "ACDEFGHIKLMNPQRSTVWY"
    onehot = np.zeros((max_length, len(AMINOACIDS) + 1))
    aa_to_idx = {aa: idx for idx, aa in enumerate(AMINOACIDS)}
    for i, aa in enumerate(sequence[:max_length]):
        if aa in aa_to_idx:
            onehot[i, aa_to_idx[aa]] = 1
        else:
            onehot[i, -1] = 1
    return onehot
$0
```

## Peptide Dataset Loader

Create a loader for a peptide dataset. Uses the seq2onehot encoder.

<!-- chem-pep-load -->

```python
class CNNPeptideDataset(Dataset):
    def __init__(
        self,
        df,
        encoder,
        seq_col="sequence",
        target_col="pct_conversion",
        normalize=False,
        target_mean=0.0,
        target_std=1.0,
    ):
        self.df = df
        self.encoder = encoder
        self.seq_col = seq_col
        self.target_col = target_col
        self.normalize = normalize
        self.target_mean = target_mean
        self.target_std = target_std

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        sequence = row[self.seq_col]
        onehot_sequence = self.encoder(sequence)
        onehot_sequence = np.transpose(onehot_sequence)
        label = row[self.target_col]
        if self.normalize:
            label = (label - self.target_mean) / self.target_std
        return torch.tensor(onehot_sequence, dtype=float), torch.tensor(
            label, dtype=float
        ).reshape(-1)
```


