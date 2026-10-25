# Locator 3D locator 3D node introduction

Version: DaVinci Resolve 20.3 Reference Manual. Context: Locator 3D.
[Chapter index](INDEX.md) / [Previous section](fog-3d-and-image-plane-3d.md) / [Next section](locator-3d-and-merge-3d-and-override-3d.md)
<a id="source-3d-nodes-part-4"></a> <a id="source-locator-3d-3lo"></a> <a id="source-locator-3d-node-introduction"></a> <a id="source-the-locator-3d-node"></a>

### Locator 3D [3Lo]

### The Locator 3D node

### Locator 3D Node Introduction


The job of the Locator 3D node is to convert a point sitting in 3D space into 2D coordinates that other nodes can feed into expressions or modifiers. Hand the Locator a camera plus the output image's dimensions, and it maps a 3D control's coordinates into 2D screen space. That 2D position surfaces as a numeric output you can wire to or from other nodes. For instance, to tie an ellipse's center to the Locator's 2D position, right-click the Mask center control and pick Connect To > Locator 3D > Position.
