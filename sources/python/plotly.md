---
library: plotly
language: python
---

# Plotly

## Line plot

Create a plotly line object.

<!-- px-line -->

```python
import plotly.express as px

${1:fig} = px.line(x=${2:x_vals}, y=${3:y_vals}, title="${4:title}")$0
```

## Scatter plot

Create a plotly scatter plot.
Rendering in the browser can be accelerated by enabling render_mode='web_gl'

<!-- px-scatter -->

```python
${1:fig} = px.scatter(${2:df}, x='${3:x_label}', y='${4:y_label}', render_mode='web_gl')$0
```

## Scatter 3D

Create an interactive 3-D scatter plot.

<!-- px-scatter-3d -->

```python
${1:fig} = px.scatter_3d(${2:df}, x='${3:x_label}', y='${4:y_label}', z='${5:z_label}')$0
```

## Parallel coordinates

Create a parallel coordinates plot.
Parallel coordinates are useful for visualizing many-dimensional data.

<!-- px-parallel|px-pc -->

```python
${1:fig} = px.parallel_coordinates(${2:df}, labels={$3:labels})$0
```

## Export plotly image

Export a plot as an image file. 
Plotly supports png, jpeg, webp, svg, and pdf formats. 
Path extension can be left blank if format argument is specified.
Static image generation requires [kaleido][https://github.com/plotly/Kaleido] installed in path.

<!-- px-save|px-export|px-svg -->

```python
${1:fig}.write_image("${2:image_path}", format="${3:svg|png|jpeg|svg}")$0
```
