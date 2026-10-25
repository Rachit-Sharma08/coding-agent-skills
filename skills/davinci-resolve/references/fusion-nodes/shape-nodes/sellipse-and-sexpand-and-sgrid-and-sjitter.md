# Sellipse and sexpand and sgrid and sjitter

Version: DaVinci Resolve 20.3 Reference Manual. Context: Sellipse, Sexpand, Sgrid, Sjitter.
[Chapter index](INDEX.md) / [Previous section](schangestyle-and-sduplicate-and-sellipse.md) / [Next section](sjitter-and-smerge.md) / [sEllipse](schangestyle-and-sduplicate-and-sellipse.md)
<a id="source-basic-node-setup-4"></a> <a id="source-basic-node-setup-5"></a> <a id="source-common-controls-2"></a> <a id="source-common-controls-3"></a> <a id="source-controls-3"></a> <a id="source-controls-4"></a> <a id="source-controls-5"></a> <a id="source-external-inputs-3"></a> <a id="source-external-inputs-4"></a> <a id="source-sexpand"></a> <a id="source-sgrid"></a> <a id="source-sjitter"></a> <a id="source-style-tab-1"></a> <a id="source-the-sellipse-controls-tab"></a> <a id="source-the-sellipse-style-tab"></a> <a id="source-the-sexpand-controls-tab"></a> <a id="source-the-sexpand-node"></a> <a id="source-the-sgrid-controls-tab"></a> <a id="source-the-sgrid-node"></a> <a id="source-the-sjitter-node"></a>

### The sEllipse Controls tab

### Controls

You use the Controls tab to set the elliptical shape's traits—fill, border, size, and placement. Solid With the Solid checkbox on, the elliptical shape fills with whatever color you defined in the Style tab. With it off, only an outline drawn by the Border Width control shows, and the middle turns transparent. Border Width This parameter grows or shrinks the border running around the shape. Though usable while the Solid checkbox is on, its main job is governing outline thickness once the checkbox is off. Cap style With the Solid checkbox off, three cap style options appear. Those cap styles let lines end flat, rounded, or squared off. Flat caps finish with flat, squared ends, whereas rounded caps finish with semi-circular ends. Squared caps carry projecting ends reaching half the line width past the line's end. None of the caps show up unless the length sits below 1.0.

Position Only when the Solid checkbox is off does the position parameter appear. It lets you set the shape's starting point. Paired with the length parameter, it places the gap in the ellipse outline. Length Only when the Solid checkbox is off does the length parameter appear. A length of 1.0 yields a closed shape. Dropping the length under 1.0 opens a gap in the outline. Keyframing the length parameters lets you build write-on style animations. X and Y Offset You use these parameters to shift the shape left, right, up, and down across the frame. The shape begins at the frame's center, and the parameters offset that placement. The offset coordinates are normalized to the frame's width. An X offset of 0.0 sits centered, and a value of 0.5 drops the shape's center right onto the frame's right edge. Width/Height The width and height fix the vertical and horizontal size of the ellipse. When the values match, you've got a perfect circle. Angle The angle spins the shape, which on a perfect circle barely alters the image, but if you make an oval or a short-length outline, you can rotate the shape around its center axis.

### Style Tab

### The sEllipse Style tab

Style The Style tab handles assigning a color to the shape and managing its transparency. Color The color controls fix the color of both fill and border. To pick a shape color, click the color disclosure arrow, work the color swatch, or drag the eyedropper into the viewer to lift a color

out of an image. With the RGBA sliders or number fields you can key in each color channel's value or the Alpha channel's strength. Allow Combining With this checkbox on, the Alpha channel value holds steady even while passing through downstream nodes that might overlap the shape with copies of itself. With it off, the Alpha channel value can climb wherever the shape overlaps itself. For example, if an ellipse's Alpha channel reads .5, turning on the Allow Combining checkbox preserves that value even when the shape moves through a Duplicate or Grid node that overlaps it. Leaving the checkbox off lets the Alpha channel values compound at each spot of overlap.

With Allow Combining on (left) and off (right) Common Controls Settings Tab Every Shape node shares the Inspector's Settings tab. Those common controls get a full treatment at this chapter's close in the “The Common Controls” section.

### sExpand

### The sExpand node

The sExpand node serves to dilate or erode shapes. As with nearly every Shape node, the sExpand node's output is only viewable through a sRender node.

### External Inputs

The input below shows up on the node's tile within the Node Editor. Input1: [orange, required] This input takes the output of another shape node. Whatever shape or compound shape you wire here is eroded or dilated.

### Basic Node Setup

The sExpand node accepts one input, most often a compound shape. That said, it works on single shapes such as sStars and sNgons too. The sExpand's output may then head onward to a further shape node, or into a sRender node, for viewing or for compositing within the wider node tree.

A star and an ellipse merged within an sBoolean node, then sent to an sExpand for dilating or eroding Inspector

### The sExpand Controls tab

### Controls

Every parameter for the sExpand node lives on the Controls tab. Amount A positive value dilates the shape while a negative one erodes it. Border Style The border style governs how the expanded or contracted shapes meet at the corners. There are four styles to pick among. Bevel flattens each corner to a square. Round gives corners a curved finish. Miter together with Miter Clip keep edges pointed until they cross a set threshold. That Threshold is fixed by the Miter limit slider. Miter Limit Only when the Miter or Miter Clip border style is chosen does the Miter parameter appear. The miter limit decides when the pointed edges turn beveled, based on the shape's thickness.

### Common Controls

Settings Tab The Settings tab in the Inspector is shared across every Shape node. Those common controls get a full treatment at this chapter's close in the “The Common Controls” section.

### sGrid

### The sGrid node

The sGrid node duplicates the shape over an X and Y grid and throws in the ability to offset the rows and columns. As with nearly every Shape node, the sGrid node's output is only viewable through a sRender node.

### External Inputs

The node's tile within the Node Editor carries the input below. Input1: [orange, required] This input takes the output of another Shape node. Whatever shape you wire here is replicated across a custom grid.

### Basic Node Setup

The sGrid node accepts one input, a lone shape or a compound one coming from am sMerge or sBoolean node. The sGrid node lays the incoming shape onto a grid of rows and columns. The sGrid's output may then head onward to a further Shape node, or into a sRender node, for viewing or for compositing within the wider node tree.

An sEllipse shape feeding an sGrid and then routed to an sRender to view and blend with other elements Inspector

### The sGrid Controls tab

### Controls

The Controls tab is where you set the number of grid cells and their offset position.

Grid Cells X and Y These parameters fix how many cells the grid holds, both horizontally and vertically. As an example, entering 5 in the X and Y number field yields five rows of the shape and five columns. X and Y Offset Fixes how far apart the rows and columns sit along X and Y. With an offset value of 0.0, every row and column stacks directly on each other. Set X Offset to 1.0 and the columns spread out by the frame's full width.

### Common Controls

Settings Tab The Settings tab in the Inspector is shared across every Shape node. Those common controls get a full treatment at this chapter's close in the “The Common Controls” section.

### sJitter

### The sJitter node

The sJitter node most often serves to randomly position an array of shapes generated by a sGrid or sDuplicate node. Even so, it carries an auto-animating random mode that can distort and randomly jitter single shapes. As with nearly every Shape node, the sJitter node's output is only viewable through a sRender node.
