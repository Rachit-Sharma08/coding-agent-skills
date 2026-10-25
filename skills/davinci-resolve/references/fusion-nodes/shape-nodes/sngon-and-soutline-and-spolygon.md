# Sngon and soutline and spolygon

Version: DaVinci Resolve 20.3 Reference Manual. Context: Sngon, Soutline, Spolygon.
[Chapter index](INDEX.md) / [Previous section](sngon.md) / [Next section](spolygon-and-srectangle.md) / [sNGon](sngon.md)
<a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-common-controls"></a> <a id="source-controls"></a> <a id="source-controls-1"></a> <a id="source-external-inputs"></a> <a id="source-external-inputs-1"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-soutline"></a> <a id="source-spolygon-sply"></a> <a id="source-style"></a> <a id="source-style-tab"></a> <a id="source-the-sngon-controls-tab"></a> <a id="source-the-sngon-style-tab"></a> <a id="source-the-soutline-controls-tab"></a> <a id="source-the-soutline-node"></a> <a id="source-the-spolygon-node"></a>

### External Inputs

This node generates shapes and does not have any inputs.

### Basic Node Setup

Being a shape generator, the sNGon node produces a shape and so carries no inputs. The sNGon's output can feed a sRender for viewing and further compositing, or—more commonly—hook into another Shape node such as sGrid or sDuplicate.

An sNGon node feeding an sDuplicate node, with the result viewed by way of an sRender node.

### Inspector

### The sNGon Controls tab

### Controls

You use the Controls tab to set the many-sided shape's traits—fill, border, size, and placement. Solid With the Solid checkbox on, the NGon shape fills with whatever color you defined in the Style tab. With it off, only an outline drawn by the Border Width control shows, and the middle turns transparent. Border Width This parameter grows or shrinks the border running around the shape. Though usable while the Solid checkbox is on, its main job is governing outline thickness once the checkbox is off. Border Style The Border Style parameter dictates the way the NGon's sides meet at the corners. You get three styles to pick among. Bevel flattens each corner to a square. Round gives corners a curved finish. Miter keeps corners sharp and pointed. Cap style With the Solid checkbox off, three cap style options appear. Those cap styles let lines end flat, rounded, or squared off. Flat caps finish with flat, squared ends, whereas rounded caps finish with semi-circular ends. Squared caps carry projecting ends reaching half the line width past the line's end. None of the caps show up unless the length sits below 1.0. Position Only when the Solid checkbox is off does the Position parameter appear. It lets you set the shape's starting point. Paired with the Length parameter, it places the gap in the outline. Length Only when the Solid checkbox is off does the Length parameter appear. A length of 1.0 yields a closed shape. Dropping the length under 1.0 opens a gap in the outline. Keyframing the Length parameters lets you build write-on style animations.

X and Y Offset You use these parameters to shift the shape left, right, up, and down across the frame. The shape begins at the frame's center, and the parameters offset that placement. The offset coordinates are normalized to the frame's width. So an X offset of 0.0 sits centered, and a value of 0.5 drops the shape's center right onto the frame's right edge. Width/Height The Width and Height parameters fix the vertical and horizontal size of the ellipse. When the values match, every side runs equal in length. Angle The Angle parameter spins the shape around its center axis.

### Style Tab

### The sNGon Style tab

### Style

The Style tab handles assigning a color to the shape and managing its transparency. Color The Color controls fix the color of both fill and border. To pick a shape color, click the color disclosure arrow, work the color swatch, or drag the eyedropper into the viewer to lift a color out of an image. With the RGBA sliders or number fields you can key in each color channel's value or the Alpha channel's strength. Allow Combining With this checkbox on, the Alpha channel value holds steady even while passing through downstream nodes that might overlap the shape with copies of itself. With it off, the Alpha channel value can climb wherever the shape overlaps itself. For example, if a NGon Alpha channel reads .5, turning on the Allow Combining checkbox preserves that value even when the shape moves through a duplicate or grid node that overlaps it. Leaving the checkbox off lets the Alpha channel values compound at each spot of overlap.

With Allow Combining on (left) versus off (right) Common Controls Settings Tab Every Shape node shares the Inspector's Settings tab. Those common controls get a full treatment at this chapter's close in the “The Common Controls” section.

### sOutline

### The sOutline node

The sOutline node serves to draw outlines from merged or boolean compound shapes. Each individual shape keeps its own style, color, size, position, and remaining traits. The lone difference is that the border thickness, border style, position, and length apply uniformly across all incoming shapes within the sOutline node. As with nearly every shape node, the sOutline node's output is only viewable through a sRender node.

### External Inputs

On the node's tile within the Node Editor you'll find the input below: Input1: [orange, required] This input accepts the output of another shape node, but usually a compound shape arriving from a sMerge or sBoolean. The compound shape wired here is what the outline gets drawn from.

### Basic Node Setup

The sOutline node accepts one input, most often a compound shape, though now and then it helps on single shapes to make double outlines. From there, the sOutline's output may pass to another Shape node, or to a sRender node, for viewing or for compositing into the wider node tree.

Wiring a compound shape out of an sBoolean node into an sOutline produces an intricate outlined shape Inspector

### The sOutline Controls tab

### Controls

The Controls tab is where you set the outline thickness, border and cap style, position, and length applied to the compound shape wired to the input. Thickness This parameter governs the outline's width. Border Style The Border Style parameter dictates the way the outline meets at the corners. There are three styles you can pick. Bevel flattens each corner to a square. Round gives corners a curved finish. Miter keeps corners sharp and pointed. Cap style Three Cap Style options let lines end flat, rounded, or squared off. Flat caps finish with flat, squared ends, whereas rounded caps finish with semi-circular ends. Squared caps carry projecting ends reaching half the line width past the line's end. None of the caps show up unless the length sits below 1.0. Position The Position parameter lets you set the shape's starting point. Paired with the Length parameter, it places the gap in the outline.

Length The Length parameter fixes where the outline ends. A length of 1.0 yields a closed shape. Dropping the length under 1.0 opens a gap in the outline. Keyframing the Length parameters lets you build write-on style animations.

### Common Controls

Settings Tab The Settings tab in the Inspector is shared across every Shape node. Those common controls get a full treatment at this chapter's close in the “The Common Controls” section.

### sPolygon [sPly]

### The sPolygon node

The sPolygon tool lets users draw custom shapes. By way of intuitive point manipulation, the tool lets users readily produce intricate forms, curves, and lines that mesh with Fusion's existing shape tools. It hands you the latitude to design custom elements, which makes it a worthwhile tool in motion graphics design.

### Inputs

This node generates shapes and does not have any inputs.
