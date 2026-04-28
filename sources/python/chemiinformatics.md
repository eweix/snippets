---
library: chemiinformatics
language: python
---


# Chemiinformatics

A suite of snippets for working with machine representations of chemical
structures and information. Mostly relies on rdkit for processing, though some
snippets involve pandas dataframes or other useful tools.


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


