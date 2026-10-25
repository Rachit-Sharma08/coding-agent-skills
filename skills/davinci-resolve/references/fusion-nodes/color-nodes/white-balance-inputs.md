# White balance inputs

Version: DaVinci Resolve 20.3 Reference Manual. Context: White balance.
[Chapter index](INDEX.md) / [Previous section](set-canvas-color-and-white-balance.md) / [Next section](white-balance-and-common-controls.md) / [White Balance WB](set-canvas-color-and-white-balance.md)
<a id="source-color-nodes-part-6"></a> <a id="source-inputs-6"></a>

### Inputs


Two inputs sit on the White Balance node: one carries the main image, the other takes an effect mask that pens in where the white balance gets applied. Input: Only this orange input has to be connected. Into it goes a 2D image for the white balance. Effect Mask: This optional blue effect mask input takes a mask shape built from polylines, simple primitive shapes, paint strokes, or bitmaps coming off other tools. Wire a mask here and the white balance reaches only the pixels lying inside that mask. An effect mask of this sort hits the tool once the tool itself has been processed.
