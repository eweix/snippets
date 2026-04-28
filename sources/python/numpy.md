---
library: numpy
language: python
---

# numpy

## Arange

Make a numpy array over a range

<!-- np:arange -->

```python
np.arange(${1:0},${2:100},${3:1})$0
```

## Zeros

Initialize an array of zeros

<!-- np:zeros -->

```python
np.zeros((${1:shape}))$0
```

## Random

Initialize an array with random values

<!-- np:randn -->

```python
np.rand((${1:shape}))$0
```

## Einsum

Perform an einsum over an array

<!-- np:einsum -->

```python

```

## Masked where

Mask a numpy array

<!-- np:mask:where|np:where:mask -->

```python
${3:masked_array} = np.ma.masked_where(${2:condition}, ${1:array})$0
```

## Mean along 2 dimensions

Get the mean of a numpy dataframe along multiple axes

<!-- np:mean:2d -->

```python
${3:mean} = ${1:array}.mean(axis=(${2:1,2}))$0
```
