---
library: matplotlib
language: python
---

# matplotlib

## Initialize figure

Initialize a figure with layout settings applied

<!-- plt-fig -->

```python
fig = plt.figure(constrained_layout=True, tight_layout=True)
```

## Make gridspec figure

initialize a figure with gridspec axes

<!-- plt-grid -->

```python
fig = plt.figure(constrained_layout=True)
G = fig.add_gridspec(nrows=${1:1},ncols=${2:2})
$0
```

## Add gridspec subplot

add a subplot to gridspec

<!-- plt-grid-sub -->

```python
${1:ax} = fig.add_subplot(${2:G[0,0]},title={$3:title})
$0
```

## Save figure

Save the current plot to a figure

<!-- plt-save -->

```python
plt.savefig("${1:figure.svg}")$0
```

## Remove ticks

Define a keyword dictionary that can be used to remove tickmarks from axes

<!-- plt-style-noticks -->

```python
ticks = dict(which=both,bottom=False,left=False,labelbottom=False,labelleft=False)
```

## Make double axis plot

Twin the current axis to allow for plotting two types of data concurrently

<!-- plt-ax-twin -->

```python
${1:ax2} = ${2:ax1}.twin${3:x}()$0
```

## Plot image without axes

Display an image in matplotlib, without axes

<!-- plt-image -->

```python
${3:ax}.imshow(${1:image}, cmap="${2:viridis}")
${3:ax}.axis(False)
```

## Define matplotlib stylesheet

Make the outline of a matplotlib stylesheet that can be saved, shared, and reused. Use this to make a good, consistent style system!

<!-- plt-style-sheet -->

```python
import matplotlib as mpl
# Set custom colors. All colors are in web style hex format.
axes.prop_cycle: cycler('color', ['1879CE', 'FC4F30', '3EBCD2', '379A8B', 'EBB434', '758D99'])

# Style spines
axes.linewidth: 1 # Spine edge line width
axes.spines.top: False # Display axis spines (True or False)
axes.spines.left: False # We only want the bottom spines
axes.spines.right: False
axes.spines.bottom: True

# Set line styling for line plots
lines.linewidth: 4 # line width in points
lines.solid_capstyle: butt # Makes a square ending of the line stopping at datapoint

# Grid style
axes.grid: true # display grid or not
axes.grid.axis: y # which axis the grid should apply to
grid.linewidth: 1 # in points
grid.color: A5A5A5 # grid color
axes.axisbelow: True # Sets axis gridlines below lines and patches.

# Move tick labels to right side
ytick.labelleft: False # draw tick labels on the left side
ytick.labelright: True # draw tick labels on the right side
ytick.alignment: bottom # alignment of yticks

# Setting font sizes and spacing
axes.labelsize: 18 # font size of the x and y labels
xtick.labelsize: 18 # font size of the x tick labels
ytick.labelsize: 18 # font size of the y tick labels
font.size: 18 # default font size for text, given in points.
xtick.major.pad: 8 # distance to major tick label in points
ytick.major.pad: -40 # distance to major tick label in points

# Remove major and minor ticks except for on the x-axis.
xtick.major.size: 5 # major tick size in points
xtick.minor.size: 0 # minor tick size in points
ytick.major.size: 0
ytick.minor.size: 0

# Title styling
axes.titlelocation: left # alignment of the title: {left, right, center}
axes.titlepad: 20 # pad between axes and title in points
axes.titlesize: 28 # font size of the axes title
axes.titleweight: bold # font weight of title

# Set spacing for figure and also DPI.
figure.subplot.left: 0.08 # the left side of the subplots of the figure
figure.subplot.right: 0.95 # the right side of the subplots of the figure
figure.subplot.bottom: 0.07 # the bottom of the subplots of the figure
figure.figsize: 16, 11 # figure size in inches
figure.dpi: 150 # figure dots per inch

# Properties for saving the figure. Ensure a high DPI when saving so we have a good resolution.
savefig.dpi: 300 # figure dots per inch or 'figure'
savefig.facecolor: white # figure face color when saving
savefig.bbox: tight # {tight, standard}
savefig.pad_inches: 0.2 # padding when bbox is set to tight

# Legend Styling
legend.framealpha: 1
```
