# Sstar and stext and stransform

Version: DaVinci Resolve 20.3 Reference Manual. Context: Sstar, Stext, Stransform.
[Chapter index](INDEX.md) / [Previous section](sstar-basic-node-setup.md) / [Next section](stransform-controls.md) / [sStar](srectangle-and-srender-and-sstar.md)
<a id="source-basic-node-setup"></a> <a id="source-common-controls"></a> <a id="source-common-controls-1"></a> <a id="source-common-controls-2"></a> <a id="source-controls"></a> <a id="source-controls-1"></a> <a id="source-external-inputs"></a> <a id="source-fusion-2712"></a> <a id="source-introduction"></a> <a id="source-stext-stxt"></a> <a id="source-stransform"></a> <a id="source-style"></a> <a id="source-style-tab"></a> <a id="source-the-sstar-controls-tab"></a> <a id="source-the-sstar-style-tab"></a> <a id="source-the-stext-node"></a> <a id="source-the-stransform-controls-tab"></a> <a id="source-the-stransform-node"></a>

### The sStar Controls tab

### Controls

On the Controls tab you set the star shape’s attributes: how many points it has, its depth, fill, border, dimensions, and where it sits. Points This slider sets how many points (arms) the star carries. Depth The depth slider governs the inner radius, or arm thickness. Set depth to 0.001 for razor-thin arms; push it to 1.0 to get a faceted circle instead. Solid Tick the Solid checkbox and the star fills with whatever color you set on the Style tab. Untick it and you get an outline drawn by the Border Width control, with a transparent middle. Border Width This control grows or shrinks the border ringing the shape. It works whether or not Solid is ticked, but its real job is setting outline thickness once the checkbox is cleared. Border Style The Border Style parameter dictates the way the star’s sides meet at each corner. Three style choices are offered. Bevel flattens the corners. Round gives you rounded corners. Miter keeps the corners pointed. Cap style With the Solid checkbox cleared, three cap style choices appear. These caps end the lines with flat, rounded, or squared finishes. A flat cap ends square and abrupt, whereas a rounded cap finishes in a semicircle. A squared cap juts past the line’s end by half the line width. You won’t see any caps unless length drops under 1.0. Position The Position parameter shows up only while the Solid checkbox is cleared. Use it to set where the shape’s starting point lands. Paired with the length parameter, it moves where the gap in the outline falls. Length The Length parameter also appears only with the Solid checkbox cleared. At a length of 1.0 the shape is closed. Drop length under 1.0 and you carve an opening or gap into the outline. Keyframe the Length parameters and you can build write-on style animations. X and Y Offset These parameters slide the shape left, right, up, and down across the frame. Because the shape begins centered in the frame, these parameters shift it away from that center. Offset coordinates scale to the frame width, so an X offset of 0.0 sits dead center while 0.5 drops the shape’s center right onto the frame’s right edge. Width/Height The Width and Height parameters fix the star’s vertical and horizontal extent. Match the two values and every arm of the star comes out the same length. Angle The Angle parameter spins the shape around its center axis.

### FUSION 2712

### Style Tab

### The sStar Style tab

### Style

Use the Style tab to give the shape its color and dial in transparency. Color The Color controls set the fill and border color coming out of the sStar node. Pick a shape color by clicking the color disclosure arrow and working the color swatch, or by dragging the eye dropper over the viewer to sample a color straight from an image. With the RGBA sliders or number fields you type in a value for each color channel, or set how strong the Alpha channel is. Allow Combining Tick this checkbox and the Alpha channel value holds steady, even after the shape flows through downstream nodes that let it overlap duplicates of itself. Leave it cleared and overlapping the shape with itself can drive the Alpha channel value upward. Say a star’s Alpha channel reads .5: turning on the Allow Combining checkbox keeps that reading intact even when the shape runs through a duplicate or grid node that overlaps the shape and its Alpha channel. Clear the checkbox instead and the Alpha channel values stack up wherever the overlaps occur.

Allow Combining Enabled (left), Allow Combining Disabled (right)

### Common Controls

Settings Tab Every Shape node shares the Settings tab found in the Inspector. The “The Common Controls” section, at this chapter’s close, walks through those shared controls thoroughly.

### sText [sTxt]

### The sText node

### Introduction

Built for the Fusion Shape environment, the sText node is a powerful character generator that handles many styles, 3D transformations, and multiple shading layers. Think of the sText node as the “Shape” counterpart to the 2D Text+ node. Its controls line up almost exactly with the 2D version across the board, the one exception being that sText offers no gradient colors.

The sText controls

### sTransform

### The sTransform node

The sTransform node layers a further set of transform controls on top of those already built into Shape nodes. Those extra transforms let you build hierarchical animations. As an example, a sStar’s own Angle control can spin the star in place. You then feed that star out to an sTransform node. From there the sTransform’s rotation control sends the star orbiting around the frame. As with nearly every Shape node, the sStar node’s output is only visible once it runs through a sRender node.

### External Inputs

On the node’s tile in the Node Editor you’ll find this input: Input1: [orange, required] It takes in the output coming from a second Shape node. Whatever shape you wire here gets moved, scaled, and rotated according to the sTransform settings.

### Basic Node Setup

Fed by another Shape node’s input, the sTransform node tacks on a further set of transforms, or hierarchical animation. Route the sTransform’s output into a sRender to view it and carry on compositing.

Inspector view of an sStar node wired into an sTransform node, with the result shown through an sRender node

### The sTransform Controls tab

### Controls

Use the Controls tab to apply a set of transform controls to the shape coming in. X and Y Offset These parameters move the shape left, right, up, and down within the frame. Since the shape begins at the frame’s center, these parameters nudge it off that center. Offset coordinates scale to the frame width, so an X offset of 0.0 stays centered while 0.5 drops the shape’s center onto the frame’s right edge. X and Y Size The X and Y Size fix how the incoming shape scales vertically and horizontally. Make the two values differ and the shape skews away from its original form. Rotation Turning the dial rotates the shape around the pivot controls. X and Y Pivot These parameters set where the rotation axis sits for the incoming shape. You can spot the pivot point in the viewer as a red X. Drag that X inside the viewer to reposition it. Transform Axis Tick this box to apply the transform onto the shape’s axis.

### Common Controls

Settings Tab All Shape nodes carry the same Settings tab inside the Inspector. You’ll find a full account of these shared controls in the “The Common Controls” section that closes out this chapter.

### Common Controls

In the Inspector, the various Shape-operation nodes hold a set of matching controls. What follows covers the controls that Shape nodes have in common.
