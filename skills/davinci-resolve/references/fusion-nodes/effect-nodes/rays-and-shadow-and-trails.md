# Rays and shadow and trails

Version: DaVinci Resolve 20.3 Reference Manual. Context: Rays, Shadow, Trails.
[Chapter index](INDEX.md) / [Previous section](object-removal-and-pseudo-color-and-rays.md) / [Continue Trails TRLS / Controls Tab](trails-accumulation-and-blending-controls.md) / [Rays CIR](object-removal-and-pseudo-color-and-rays.md)
<a id="source-basic-node-setup-2"></a> <a id="source-basic-node-setup-3"></a> <a id="source-basic-node-setup-4"></a> <a id="source-common-controls-2"></a> <a id="source-common-controls-3"></a> <a id="source-controls-tab"></a> <a id="source-controls-tab-1"></a> <a id="source-controls-tab-2"></a> <a id="source-input"></a> <a id="source-input-1"></a> <a id="source-inspector-2"></a> <a id="source-inspector-3"></a> <a id="source-rays-node-controls"></a> <a id="source-shadow-node-controls"></a> <a id="source-shadow-node-introduction"></a> <a id="source-shadow-sh"></a> <a id="source-the-shadow-node"></a> <a id="source-the-trails-node"></a> <a id="source-trails-node-controls"></a> <a id="source-trails-node-introduction"></a> <a id="source-trails-trls"></a>

### Basic Node Setup

The Rays node performs best when whatever image or graphic you feed into the orange input carries an Alpha channel for the rays to radiate from.

Rays node set up to emit from a line of text Inspector

### Rays node controls

### Controls Tab

All the main controls you need to tailor the rays sit on the Controls tab. Center X and Y This pair of coordinate controls, along with their viewer crosshair, places the center point of the light source.

Blend Sets what percentage of the original image mixes in with the light rays. Decay Determines how long the rays extend. Weight Governs the rays’ falloff. Exposure Dials in the brightness of the rays. Threshold Marks the luminance level above which the rays begin to form.

### Common Controls

Settings Tab The controls on the Settings tab are shared by all Effect nodes, so you’ll find them described within the “The Common Controls” section near this chapter’s end.

### Shadow [SH]

### The Shadow node

### Shadow Node Introduction

Shadow is a flexible node for building a drop shadow off of an image’s Alpha channel. If you wish, a second image can serve as a depth matte that warps the shadow according to the changing depth in a background image.

### Input

The Shadow node’s three inputs let you attach a 2D image that produces the shadow. A depth map input plus an effect mask can each rein in the area where trails show up. Usually the shadow’s output then gets merged over the real background within the composite. Input: The orange input handles the main 2D image carrying the Alpha channel that originates the shadow. Depth: Fed a 2D image, the green Depth map input pulls a depth matte out of a chosen channel. From there, the light Position and Distance controls reshape the shadow’s look based on depth. Effect Mask: The blue input takes a mask shape made from polylines, basic primitive shapes, paint strokes, or bitmaps out of other tools. Wiring a mask in here restricts where the shadow shows up. That effects mask is applied to the tool after the tool finishes processing.

NOTE: The Shadow node is meant for plain 2D drop shadows. For genuine 3D shadow casting, reach for a Spot Light node together with an Image Plane 3D node.

### Basic Node Setup

In the example below, the Shadow node draws on the output of an image with Alpha and feeds into the foreground of a Merge, with the shadow appearing over the Merge’s background input.

### Inspector

A Shadow node is generated from the MediaIn2 and shown over MediaIn1

### Shadow node controls

### Controls Tab

Every main control you need to shape the shadow’s appearance lives on the Controls tab. Shadow Offset This control places the shadow at an X and Y position. With the Shadow node selected, you can also nudge the Shadow Offset’s position via the crosshair in the viewer. Softness Softness dictates how blurry the shadow’s edges look. Shadow Color Pick the shadow’s color with this control; the most believable shadows tend not to be pure black or perfectly sharp. Light Position This control situates the light relative to the object casting the shadow. The Light Position only matters while the Light Distance slider sits at something other than infinity (1.0). Light Distance This slider shifts the light’s apparent distance anywhere from infinity (1.0) down to zero distance from the shadow-casting object. Dialing in the Light Distance pays off in a more lifelike shadow, where the parts of the shadow farther away stretch longer than the nearer parts. Minimum Depth Map Light Distance This control becomes available once an image is wired into the shadow’s Depth Map input. Its slider sets how much the depth map feeds into the Light Distance. Darker regions of a depth map deepen the shadow, while white regions pull it nearer the camera. Z Map Channel Through this menu you choose which color channel of the image attached to the node’s Depth Map input builds the shadow’s depth map. Choices cover the RGB and A, Luminance, and Z-buffer channels. Output This menu decides whether the output image holds the picture with its shadow applied or just the shadow alone. The shadow-only route comes in handy when color correction, perspective, or other effects must hit the resulting shadow before it’s merged back onto the object.

### Common Controls

Settings Tab The Settings tab’s controls turn up identically on all Effect nodes, so look for their descriptions over in the “The Common Controls” section closing out this chapter.

### Trails [TRLS]

### The Trails node

### Trails Node Introduction

The Trails node makes a ghostly after-trail follow the image. Applied to moving images that carry an Alpha channel, it yields a striking effect. In contrast to a directional blur, the effect surfaces only the image’s earlier motion. Because the trail effect draws on an image buffer, you have to play it or kick off the pre-roll across a number of frames before the effect becomes visible.

### Input

The Trails node’s two inputs let you hook up a 2D image plus an effect mask that can confine where the trails turn up. Input: The orange input handles the main 2D image that the trails get applied to. Effect Mask: The blue input takes a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps out of other tools. Wiring a mask in here confines where the trails effect shows. This effects mask gets applied to the tool once the tool has been processed.

### Basic Node Setup

Here the output of an animated Text node feeds into the Trails node’s input, and trails arise from how the text moves. Be sure to press the Reset button in the Inspector between previews; otherwise the trails pile up.

A Trails node generates trails for the animation in the Text node

### Inspector

### Trails node controls

### Controls Tab

All the primary controls for shaping the trails reside on the Controls tab. Restart This control wipes the image buffer and shows a clean frame free of any ghosting. Preroll This has the Trails node pre-render the effect across however many frames the slider specifies. Reset/Preroll on Render With this checkbox on, the Trails node resets itself whenever a preview or final render begins, pre-rolling the set number of frames. This Time Only Ticking this checkbox limits the pre-roll to the current frame alone, ignoring the earlier frames. Preroll Frames This fixes how many frames to pre-roll. Lock RGBA Ticking this checkbox lets the Gain of each color channel be steered on its own, which makes tinting the Trails effect possible.
