# Schangestyle and sduplicate and sellipse

Version: DaVinci Resolve 20.3 Reference Manual. Context: Schangestyle, Sduplicate, Sellipse.
[Chapter index](INDEX.md) / [Previous section](sboolean-and-sbspline-and-schangestyle.md) / [Next section](sellipse-and-sexpand-and-sgrid-and-sjitter.md) / [sChangeStyle sCS](sboolean-and-sbspline-and-schangestyle.md)
<a id="source-basic-node-setup-1"></a> <a id="source-basic-node-setup-2"></a> <a id="source-basic-node-setup-3"></a> <a id="source-common-controls-1"></a> <a id="source-controls-1"></a> <a id="source-controls-2"></a> <a id="source-duplicate-jitter-tab"></a> <a id="source-external-inputs-1"></a> <a id="source-external-inputs-2"></a> <a id="source-inspector"></a> <a id="source-inspector-1"></a> <a id="source-jitter-tab"></a> <a id="source-sduplicate"></a> <a id="source-sellipse"></a> <a id="source-the-schangestyle-controls"></a> <a id="source-the-sduplicate-controls-tab"></a> <a id="source-the-sduplicate-node"></a> <a id="source-the-sellipse-node"></a>

### Basic Node Setup

Wire the output of the shape whose style you want to alter into the input. The node's output then carries on to the rest of the shape node tree.

A basic node tree where the sChangeShape node receives an sEllipse shape's output, applies the style change, and forwards it onward to the sRender node.

### Inspector

### The sChangeStyle controls

### Controls

The Style tab handles assigning color to the shape and managing its transparency. Color The Color parameter controls fix the color of both fill and border coming from the sPolygon node. To pick a shape color, click the color disclosure arrow and work the color swatch, or drag the eye dropper into the viewer to lift a color out of an image. With the RGBA sliders or number fields you can key in the value of each color channel or the Alpha channel's strength. Allow Combining With this checkbox on, the Alpha channel value holds steady, even while passing through downstream nodes that might overlap the shape with copies of itself. With it off, the Alpha channel value can climb wherever the shape overlaps itself. For example, if a rectangle Alpha channel reads .5, turning on the Allow Combining checkbox preserves that value, even when the shape moves through a duplicate or grid node that overlaps the shape and Alpha channel. Leaving the checkbox off lets the Alpha channel values compound at each spot of overlap.

Allow Combining enabled (left), Allow Combining disabled (right)

### sDuplicate

### The sDuplicate node

The sDuplicate node makes copies of the input shape, shifting each copy's position, size, and rotation. As with nearly every shape node, the sDuplicate node's output is only viewable through a sRender node.

### External Inputs

On the node's tile inside the Node Editor sits the input below: Input1: [orange, required] This input takes the output of another Shape node. Whatever shape you wire here gets copied and offset per the controls in the Inspector.

### Basic Node Setup

The sDuplicate node accepts one input, typically a lone shape or a compound one arriving out of a sMerge or sBoolean node. The sDuplicate node copies the incoming shape and offsets the copies to form a pattern. Its output may then head onward to a further shape node, or into a sRender node, for viewing or for compositing within the wider node tree.

An sEllipse shape feeding an sDuplicate and then routed to an sRender to view and blend with other elements

### Inspector

### The sDuplicate Controls tab

### Controls

The Controls tab is where you set the number of copies and dial in their position, size, and rotation offset. Copies This slider fixes how many copies the node makes. That number leaves out the original shape, so entering a value of five gives you five copies on top of the original. Copy Probability This slider tunes the likelihood of a duplicate shape. Time Offset Reach for the Time Offset slider to shift any animation applied to the source geometry by a set amount per copy. For instance, set the value to –1.0 with a cube rotating on the Y-axis as the source. The first copy displays the animation from one frame earlier; the second copy displays animation from a frame before that, and so on. This can pay off nicely on textured planes—for instance, where consecutive frames of a clip get shown. X and Y Offset These sliders fix the X and Y distance separating the copies. Each copy is offset from the one before it by whatever value you entered in the X and Y number fields. The copies all begin at 0, the center of the original shape, and offset outward from there. With Fusion's normalized coordinate system, entering X Offset at 0.5 would push each copy half the frame's width rightward. Entering -1.0 would slide each copy leftward by a full frame width.

X and Y Size Fixes the X and Y size offset relative to the previous shape's size. As an example, an X and Y value of 1.0 makes copies the same size as the original but. Entering an X and Y of 0.5 makes each copy half the size of the one before it. Axis Mode The Axis mode menu hands you four options governing how each copy works out its rotational pivot point.

- Absolute: Lets you fix an X and Y position for the rotation axis relative to where the original shape sits. That rotation axis is then copied and offset along with each duplicated shape.
- Origin Relative: Every copy takes its own center point as its rotation axis.
- Origin Absolute: Every copy takes the original shape's center as its rotation axis.
- Progressive: Builds up each shape copy by transforming it step by step from the

position, rotation, and scale of the shape before it. X and Y Pivot The X and Y pivot controls surface once the Axis mode reads Absolute. These position controls let you set where the rotation axis lands. Rotation Sets an offset rotation laid on each copy. That rotation is figured from the offset rotation of the copy preceding it. To spin every copy the same way, turn to the Angle parameter on the original shape or bring in a sTransform node. Style A set of color-picking tools for tinting the duplicate shapes.

### Duplicate Jitter tab

### Jitter Tab

The options in the Jitter tab let you randomize the position, rotation, size, and color of every copy made over in the Controls tab.

Random Seed The Random Seed slider together with the Reseed button generate a random starting point governing how much jitter falls on the duplicated objects. A pair of Duplicate nodes sharing identical settings but holding different random seeds produce two completely distinct outcomes. Click Reseed to mint a new random starting point. Center X and Y This pair of controls adjusts the amount of variation entering each duplicate's X and Y position. Pivot X and Y This pair of controls adjusts the amount of variation entering each duplicate's rotational pivot center. It affects only the extra jitter rotation, leaving alone whatever the Rotation settings on the Controls tab produce. Size This control adjusts the amount of variation entering each duplicate's Scale. Tick the Lock size box to pin this parameter. Angle This dial adjusts the amount of variation entering each duplicate's Z rotation. Gain The Gain RGBA controls multiply the image channel values at random, in a linear fashion. Blur Edits here randomize the blur from one object to the next.

### Common Controls

Settings Tab The Settings tab in the Inspector is shared across every Shape node. Those common controls get a full treatment at this chapter's close in the “The Common Controls” section.

### sEllipse

### The sEllipse node

The sEllipse node serves to build circular shapes. As with nearly every shape node, the sEllipse node's output is only viewable through a sRender node.

### External Inputs

This node generates shapes and does not have any inputs.

### Basic Node Setup

Being a shape generator, the sEllipse node produces a shape and so carries no input. The sEllipse's output can feed a sRender for viewing and further compositing, or—more commonly—hook into another shape node such as sGrid or sDuplicate. An sEllipse node feeding an sGrid node, the result then viewed by way of an sRender node Inspector
