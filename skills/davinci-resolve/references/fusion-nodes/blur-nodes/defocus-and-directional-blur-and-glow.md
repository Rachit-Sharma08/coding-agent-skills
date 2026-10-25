# Defocus and directional blur and glow

Version: DaVinci Resolve 20.3 Reference Manual. Context: Defocus, Directional blur, Glow.
[Chapter index](INDEX.md) / [Previous section](blur-and-defocus.md) / [Next section](glow-and-sharpen.md) / [Defocus Dfo](blur-and-defocus.md)
<a id="source-a-defocus-node-applied-to-a-mediain1-node"></a> <a id="source-basic-node-setup-2"></a> <a id="source-common-controls"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab-1"></a> <a id="source-controls-tab-2"></a> <a id="source-defocus-controls"></a> <a id="source-directional-blur-controls"></a> <a id="source-directional-blur-drbl"></a> <a id="source-directional-blur-node-introduction"></a> <a id="source-glow-glo"></a> <a id="source-glow-node-introduction"></a> <a id="source-inputs-2"></a> <a id="source-inspector-1"></a> <a id="source-inspector-2"></a> <a id="source-the-directional-blur-node"></a> <a id="source-the-glow-nozzde"></a>

### Inspector

### A Defocus node applied to a MediaIn1 node

### Defocus controls

### Controls Tab

Inside the Controls tab live all the main controls for shaping the defocus. Filter Reach for this menu to pick the precise method used to build the defocus. Gaussian delivers a basic effect, while Lens mode produces a more lifelike defocus. Lens mode runs considerably longer than Gaussian. Lock X/Y With Lock X/Y picked, the same amount of defocus is applied to both the X- and Y-axis of the image. Deselect it for separate command. Defocus Size The Defocus Size control sets how big the defocus effect grows. Bigger values blur the image more heavily and yield larger blooms. Bloom Level The Bloom Level control governs how intense and how large the blooming is on pixels sitting above the bloom threshold. Bloom Threshold Pixels whose values sit above the chosen Bloom Threshold get defocused and pick up a glow (blooming). Pixels under that value are only defocused. The four lens options that follow show up solely when the Filter is set to Lens.

- Lens Type: The base shape used to build the “bad bokeh” effect. The Angle, Sides, and Shape sliders let you refine it further.
- Lens Angle: Sets the rotation of the shape. Most visible on NGon lens types. Owing to a circle's round nature, this slider has no effect you can see when the Lens Type is set to Circle.
- Lens Sides: Sets the number of sides an NGon shape carries. Most visible on NGon lens types. Owing to a circle's round nature, this slider has no effect you can see when the Lens Type is set to Circle.
- Lens Shape: Sets how pointed the NGons turn out. Higher values yield a more pointed, starry look. Lower values yield smoother NGons. Most visible on NGon lens types with Lens Sides between 5 and 10. Owing to a circle's round nature, this slider has no effect you can see when the Lens Type is set to Circle.

Clipping Mode This setting governs how edges get treated during domain-of-definition rendering. It carries real weight for nodes such as Blur, which may need to sample parts of the image lying beyond the current domain.

- Frame: Frame is the default, and it automatically forces the node's domain of definition to span the image's whole frame, in effect disregarding the present domain of definition. Where the upstream DoD falls short of the frame, the leftover frame area is taken as black/ transparent.
- Domain: Choosing Domain honors the upstream domain of definition as the node's effect is applied. This can lead to unwanted clipping wherever the node reaches for a large filter.
- None: Choosing None skips source image clipping altogether. So whatever data the node's effect needs that would normally fall outside the upstream DoD is taken as black/transparent.

### Common Controls

Settings Tab The Settings tab in the Inspector also recurs across the other Blur nodes. These shared controls get a full treatment at this chapter's close, under the “The Common Controls” section.

### Directional Blur [DrBl]

### The Directional Blur node

### Directional Blur Node Introduction

You use this node to produce Directional and Radial blurs. It comes in handy for faking motion blur and light ray-type effects. Directional Blur acts on every channel (RGBA).

### Inputs

A Directional Blur node carries two inputs, one for a 2D image and one for an effect mask which can hold the blur to a chosen region. Input: The orange input takes the main 2D image that the directional blur is applied to. Effect Mask: The blue input accepts a mask shape built from polylines, simple primitive shapes, paint strokes, or bitmaps coming out of other tools. Wiring a mask here confines the directional blur to the pixels inside that mask. An effect mask gets applied once the tool has processed.

### Basic Node Setup

A Directional Blur node accepts a 2D image such as the MediaIn1 pictured below. Its output carries the node tree onward by feeding another 2D image-processing node or a Merge node.

A Directional Blur node applied to a MediaIn1 node

### Inspector

### Directional Blur controls

### Controls Tab

Inside the Controls tab live all the main controls for shaping the directional blur. Type Reach for this menu to pick which type of directional blur lands on the image.

- Linear: Linear smears the image along a straight line, much like the view through the window of a train at full speed.
- Radial: Radial spreads a distortion outward from some chosen center, the way the scene would look to someone riding up front and gazing ahead.
- Centered: The Centered button gives a result close to linear, except the blur spreads evenly to either side of the original.
- Zoom: Zoom warps the scale of the image smear to mimic the zoom streak of a camera shooting at a slow shutter speed.

Center X and Y This coordinate control, along with its viewer crosshair, touches only the Radial and Zoom Motion Blur types. You use it to set where the blurring effect begins. Length Length tunes the strength and heading of the effect. Values under zero send blurs in the direction opposite the angle control. Values past the slider's top can be entered by hand right in its edit box. Angle Whenever you're in Linear or Center mode, this control steers the heading of the directional blur. In the Radial and Zoom modes, the result is like the camera spinning while it stares at one spot. When the length slider sits at anything other than zero, the result builds a whirlpool effect. Glow This lays a Glow over the directional blur, useful for reproducing the extra light exposure a camera picks up with longer shutter speeds.

Clipping Mode This setting governs how edges get treated during domain-of-definition rendering. It carries real weight for nodes such as Blur, which may need to sample parts of the image lying beyond the current domain.

- Frame: Frame is the default, and it automatically forces the node's domain of definition to span the image's whole frame, in effect disregarding the present domain of definition. Where the upstream DoD falls short of the frame, the leftover frame area is taken as black/transparent.
- Domain: Choosing Domain honors the upstream domain of definition as the node's effect is applied. This can lead to unwanted clipping wherever the node reaches for a large filter.
- None: Choosing None skips source image clipping altogether. So whatever data the node's effect needs that would normally fall outside the upstream DoD is taken as black/transparent.

### Common Controls

Settings Tab The Settings tab in the Inspector also recurs across the other Blur nodes. These shared controls get a full treatment at this chapter's close, under the “The Common Controls” section.

### Glow [Glo]

### The Glow nozzde

### Glow Node Introduction

A Glow comes about by blurring an image, then brightening that blurred result and mixing it back over the original. The Glow node serves up a range of takes on this idea. A Bartlett glow, for instance, is a high-quality glow with a gentler falloff, though it asks more of the processor at bigger sizes.
