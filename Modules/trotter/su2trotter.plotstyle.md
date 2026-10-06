---
type: "module"
package: "su2qc-trotter"
file: "src/su2trotter/plotstyle.py"
lines: 96
generated: True
as_of: "2026-10-06"
tags: ["module", "trotter"]
---
# su2trotter.plotstyle

Module of [[su2qc-trotter]] · `src/su2trotter/plotstyle.py` · 96 lines

## What it does (from the module docstring)

> Shared finishing step for all comparison plots.
>
> * Axis limits come from the plotted data, never fixed: on a log axis the range is at least
>   [smallest / 2, largest x 2]; on a linear axis the data range is padded by 8 % on each side
>   (so points at the ends, e.g. a probability of 0 or the first and last time step, are not drawn on
>   the frame).  Shared axes use the union of their panels' data.
> * Values that are exactly zero cannot be drawn on a log scale; plotting code masks them (see `mag`)
>   and names such series in the legend instead of drawing them on the axis.
> * All legends are collected into one figure legend below the panels, so no legend covers data.

## Public names

`mag`, `note_handle`, `fit_axes`, `figure_legend`, `finish`
