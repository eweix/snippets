---
library: numpy
language: python
---

# numpy

## Arange

Make a numpy array over a range

<!-- np-arange -->

```python
np.arange(${1:0},${2:100},${3:1})$0
```

## Zeros

Initialize an array of zeros

<!-- np-zeros -->

```python
np.zeros((${1:shape}))$0
```

## Random

Initialize an array with random values

<!-- np-randn -->

```python
np.rand((${1:shape}))$0
```

## Einsum

Perform an einsum over an array

<!-- np-einsum -->

```python

```

## Masked where

Mask a numpy array

<!-- np-mask-where|np-where-mask -->

```python
${3:masked_array} = np.ma.masked_where(${2:condition}, ${1:array})$0
```

## Mean along 2 dimensions

Get the mean of a numpy dataframe along multiple axes

<!-- np-mean-2d -->

```python
${3:mean} = ${1:array}.mean(axis=(${2:1,2}))$0
```

## Mesh grid 2D

Create a 2D mesh grid based on a set of bounds.

<!-- np-mesh-2d|np-grid -->

```python
${1:xx}, ${2:yy} = np.mgrid[${3:0}:${4:10}:${5:100},${6:0}:${7:10}:${8:100}]$0
```