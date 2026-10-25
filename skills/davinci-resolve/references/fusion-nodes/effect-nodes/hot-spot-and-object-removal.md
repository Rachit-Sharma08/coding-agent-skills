# Hot spot and object removal

Version: DaVinci Resolve 20.3 Reference Manual. Context: Hot spot, Object removal.
[Chapter index](INDEX.md) / [Previous section](hot-spot-color-tab.md) / [Next section](object-removal-and-pseudo-color-and-rays.md) / [Hot Spot Hot](highlight-and-hot-spot.md)
<a id="source-basic-node-setup"></a> <a id="source-common-controls"></a> <a id="source-hot-spot-radial-tab"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-l1-l2-and-l3-tab"></a> <a id="source-l1-tab"></a> <a id="source-l2-tab"></a> <a id="source-l3-tab"></a> <a id="source-lens-reflect-tabs"></a> <a id="source-object-removal-node-introduction"></a> <a id="source-object-removal-orm"></a> <a id="source-radial-tab"></a> <a id="source-the-object-removal-node"></a>

### Hot Spot Radial tab

### Radial Tab

Radial On Turning this on switches the Radial splines into effect. With it off, the splines’ radial matte never reaches the hot spot, and the color controls’ Mix spline leaves the hot spot alone as well. Radial Mode Working much like the Color mode menu, this one lets you pick whether the radial hot spot tweaks are animated or held static, all through the compact curves editor in the Inspector.

- No Animation: As the default, this keeps one fixed curve adjustment across the whole range.
- Animated Points: With this picked, the radial curves within the spline area can change over time.

After choosing it, jump to whatever frame you want and edit something in the Spline Editor to drop a keyframe. The Interpolated Values option is largely outdated and sticks around only for backward compatibility. Radial Length and Radial Density Splines Inside the Spline window you’ll find curves describing the hot spot’s Length and Density — it functions as a scaled-down Spline Editor. What unlocks these splines is grasping that the horizontal axis in the Inspector’s Spline Editor maps to a location around the hot spot’s circumference. Here, 0.0 corresponds to 0 degrees and 1.0 to 360 degrees. Given that, length governs the radius of the light forming the hot spot around the circumference, while density reflects the brightness of that light around the circumference. Radial Repeat This control plays back the radial splines’ effect x number of times. As an example, a repeat of 2.0 makes the spline act between 0 and 180 degrees rather than 0 and 360, then echoes the spline from 180 to 360. Length Angle This spins the Radial Length spline’s effect around the hot spot’s circumference.

Density Angle This one spins the Radial Density spline’s effect around the hot spot’s circumference. NOTE: A right-click within the spline area brings up a contextual menu whose options relate to editing the spline curves. For an exhaustive account of what the LUT Editor offers, turn to Chapter 107, “LUT Nodes,” within the DaVinci Resolve Reference Manual; the parallel coverage sits in Chapter 47 of the Fusion Reference Manual.

### L1, L2, and L3 Tab

### L1 tab

### L2 tab

### L3 tab

### Lens Reflect Tabs

You use the three Lens Reflect tabs to switch on and shape extra lens flare elements that go beyond the primary and secondary hot spots. Lens Reflect 1-3 Ticking any of these three checkboxes turns on a pair of lens reflection elements you can then adjust with the controls in that tab. Every parameter here acts on all of the active Lens reflection elements within the tab. Element Strength This sets how bright the element reflections are. Element Size This sets how large the element reflections are.

Element Position This sets how far the element reflections sit from the axis, where the axis runs as a line drawn between the hot spot position and the image center. Element Type This bank of buttons picks the shape and density of the element reflections, with the available presets listed below.

- Circular: Produces reflections shaped as circles with mildly soft edges.
- Soft Circular: Produces circular reflections whose edges are extremely soft.
- Circle: Produces a circle shape with a crisp, hard edge.
- NGon Solid: Produces a solid-filled polygon whose side count can vary.
- NGon Star: Produces a star shape with very soft edges and a variable side count.
- NGon Shaded Out: Produces circular shapes with soft edges.
- NGon Shaded In: Produces a polygon of variable side count carrying a very soft

reversed (dark center, bright radius) circle.

- NGon Angle: This control fixes the angle at which the NGon shapes sit.
- NGon Sides: This control fixes how many sides are used whenever the Element Type is

set to Ngon Star, Ngon Shaded Out, and Ngon Shaded In.

- NGon Starriness: This control warps polygons toward star shapes; raising the value makes

the shape more star-like. Lens Color Controls These controls set the lens color, which in turn tints the colors of the reflections. To set a lens color, sample one from a shown image or type RGBA values into the sliders or input boxes.

### Common Controls

Settings Tab Because every Effect node shares the controls on the Settings tab, you’ll find them documented in the “The Common Controls” section that closes this chapter.

### Object Removal [ORm]

### The Object Removal node

### Object Removal Node Introduction

Object Removal leans on the DaVinci Neural Engine to take out an object in the frame with as little manual effort as it can manage. The node performs best at erasing a moving object that travels across a background that stays steady over time, or lens dirt in a shot where the camera itself is moving. You’ll see better outcomes with smaller objects than larger ones, though much of the result hinges on the footage itself.

### Inputs

The Object Removal node accepts both masks and clean plates. Input: Feed the orange input the main footage from which you intend to erase an object. Clean Plate: The magenta input takes a clean plate image source when one is chosen in the controls. Mask: The green input takes a mask shape — polygon, ellipse, rectangle, and the like — that you’ve drawn around whatever object is leaving the scene. Effect Mask: Into the optional blue effect mask input goes a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps coming from other tools. Wiring a mask into this input confines the filter to just the pixels inside the mask. Such an effects mask gets applied to the tool only once the tool has finished processing.

### Basic Node Setup

Wire the footage you want the object erased from into the yellow Input, then send either a polygon shape into the green Mask input or an object-free frame into the clean plate input. The Object Removal tool node structure. What you need is either a polygon or some other shape on the green Mask input, or a clean plate on the pink clean plate input. To set up the Object Removal: 1 In the Polygon node, draw a polygon around whatever object you mean to take out of the scene. 2 Track that polygon by hand or with a tracker so the object you’re removing stays within its bounds for the whole length of the clip. 3 Click the Scene Analysis button found in the Object Removal tool controls. Those steps cover most basic object removal jobs; should trouble arise, you can fine-tune the tool’s parameters in the Inspector. The Object Removal tool doesn’t suit every scene and does its best work on small objects that drift across the frame rather than passing in front of or behind other objects.

Once a polygon is drawn and tracked around the cyclist and the Scene Analysis button in the Object Removal controls is clicked, the cyclist disappears from the background.

### Inspector

The Object Removal controls assist in stripping unwanted objects out of an image.
