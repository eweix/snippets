---
library: images
language: python
---

# images

## Load an image

Load an image from a tiff

<!-- im:load -->

```python
f = Path("${1:path}").expanduser()
tifffile.imread(f)
```

## Save an image

Save an image to a tiff file

<!-- im:save -->

```python
tifffile.imwrite("${2:path}", ${1:image})
```

## Return selected masked pixels

Take an image stored as a numpy array and set all pixels not selected by a particular mask value to zero

<!-- im:mask:selected -->

```python
${2:masked} = np.ma.masked_where(${1:mask} != 0, 0)
```

## Return all masked pixels

Take an image stored as a numpy array and set all unmasked pixels to zero

<!-- im:mask:all -->

```python
${2:masked} = np.ma.masked_where(${1:mask} == 0, ${1:mask})
```
