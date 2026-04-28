---
library: ssqueezepy
language: python
---

# ssqueezepy

## Ssqueezepy Imports

Import common dependencies from ssqueezepy

<!-- ssq-imports -->

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ssqueezepy import cwt, ssq_cwt, Wavelet
$0
```

## Set environment

Set the ssqueezepy environment for processing

<!-- ssq-env -->

```python
os.environ["SSQ_GPU"] = "0"
os.environ["KMP_DUPBLICATE_LIB_OK"] = "True"
$0
```

## Continuous Wavelet Transform

Get the continuous wavelet transform of a time series x

<!-- ssq-cwt -->

```python
W${1:x}, scales, dW${1:x} = cwt(${1:x}, wavelet=${2|'gmw', ('gmw', {'beta': 6})|})
W${1:x} = (W${1:x}.T).reshape(t, Wx.shape[1], dims[0], dims[1])
```

## Synchrosqueezed CWT

Get the synchrosqueezed wavelet transform of a time series x

<!-- ssq-scwt -->

```python
T${1:x}, W${1:x}, ssq_freqs, scales = ssq_cwt(${1:x}, wavelet=${2|('gmw', {'beta': 6}), 'gmw'})
```

## Preprocess image

Reshape wave data for cwt processing

<!-- ssq-data -->

```python
t, *dims = ${1:data}.shape
${2:waves}=${1:data}.reshape(t,-1)
x = waves.T
```

## Plot scalogram

plot a scalogram of a pixel from a wavelet transform

<!-- ssq-scales -->

```python
plt.imshow(${1:Wx.T}$2)$0
```
