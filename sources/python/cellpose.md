---
library: cellpose
language: python
---

# cellpose

## Import Cellpose dependencies

Import the main libraries used in cellpose segmentation

<!-- cellpose-import|cp-import|import cellpose -->

```python
from cellpose import io, models
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import tifffile
import ssqueezepy
from itertools import product


Model = models.CellposeModel(gpu=True)
```

## Generate static mask via Cellpose

Input an image, then generate masks using cellpose

<!-- cellpose-mask|cp-m -->

```python
masks, flows, style = ${1:Model}.eval(${2:image}, cellprob_threshold=${3:0.4})
```

## Generate time-series mask via Cellpose

Convert a TYX image into a list of length T of 2D YX images, then generate masks using cellpose and collapse masks back into a new image of TYX

<!-- cellpose-mask-time|cp-mt -->

```python
${2:image_list} = list(${1:image})
masks, flows, style = ${3:Model}.eval(${2:image_list}, cellprob_threshold=${4:0.4})
```

## Get individual cell masks

Get the number of unique cells in a mask, then generate individual masks on a per-cell basis.
Saves output masks as tiffs, but a little editing gives other filetype options.

<!-- cellpose-get-masks|cp-get-masks -->

```python
num_cells = np.unique(${1:mask})
for cell in num_cells:
	cell_mask = np.ma.masked_where(${1:mask} != cell, 0)
	masked = np.where(cell_mask != cell, ${2:image}, ${1:mask})
	tifffile.imwrite(f"masks/{cell}.tif", masked)
```
