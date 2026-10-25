# Delta keyer node introduction and depth map

Version: DaVinci Resolve 20.3 Reference Manual. Context: Delta keyer node introduction, Depth map.
[Chapter index](INDEX.md) / [Previous section](delta-keyer-node-introduction-delta-keyer-key-tab.md) / [Next section](depth-map-and-difference-keyer.md) / [Delta Keyer Node Introduction](chroma-keyer-and-delta-keyer-node-introduction.md)
<a id="source-basic-node-setup"></a> <a id="source-common-controls"></a> <a id="source-depth-map-dmp"></a> <a id="source-depth-map-node-introduction"></a> <a id="source-garbage-mask"></a> <a id="source-inputs"></a> <a id="source-mask-tab"></a> <a id="source-the-delta-keyer-mask-tab"></a> <a id="source-the-depth-map-node"></a>

### The Delta Keyer Mask tab

### Mask Tab

On the Mask tab you decide how the solid and garbage mattes get folded into the key. Solid Source Alpha Serves to blend the source image's existing alpha together with the solid mask.

- Ignore: Leaves the source image's alpha out of the blend.
- Add: Wherever the source image alpha is solid, the solid mask becomes solid too.
- Subtract: Wherever the source image alpha is transparent, the solid mask becomes transparent too.

Solid Replace Mode Here you set how the solid mask puts color back into the image.

- None: Nothing gets recolored. Color stays untouched by the solid mask.
- Source: The hue lifted straight from the original image.
- Hard Color: A single flat color.
- Soft Color: A flat color scaled by the amount of background color that was stripped away to begin with.

Solid Replace Color The hue used by the Hard Color and Soft Color replace modes.

- Invert: Flips the solid mask before it merges with the source alpha.

### Garbage Mask

- Invert: By default, a garbage mask's solid regions cut the image out. Flip it, and instead the mask's transparent regions cut the image out.

### Common Controls

Settings Tab You'll find the Inspector's Settings tab mirrored across the other matte nodes as well. Full descriptions of these shared controls sit at this chapter's close, under "The Common Controls."

### Depth Map [DMp]

### The Depth Map node

### Depth Map Node Introduction

Depth Map builds an Alpha channel from how far away the objects in your clip appear to sit. Once you can single out a particular depth band, the range of ways to work on the resulting image grows enormously. Pair it with a Blur node, say, and you can fake a depth of field look that only touches the far background of the shot. A foreground element such as a person could be lifted with extra contrast, saturation, and sharpness, much as a qualifier would. A Depth Map can also patch up video problems: think of correcting a color temperature issue by singling out a distant window shot in daylight that has tinted the background actors blue, all while sparing the foreground subject lit by studio lighting. That resulting Depth Map Alpha channel reads as a black-and-white image, where white marks whatever the changes reach and black marks whatever is left alone.

### Inputs

Within the Node Editor, the Depth Map node carries two inputs. Input: That yellow input takes a 2D image holding the shot you want examined for depth. Effect Mask: The optional blue input looks for a mask shape drawn from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wiring a mask here confines which pixels the difference matte covers. The tool gets the effects mask only once its own processing has finished.

### Basic Node Setup

The Depth Map's purpose is to pull in an image source and forge an Alpha channel keyed to how far things appear from the camera, then pass that Alpha along to nodes further down the chain. The example that follows uses the Depth Map to single out the image's background and grade only that background, leaving the foreground actors untouched as they cross the frame.

An example Depth Map node layout that singles out subjects by how far they sit from the camera Inspector
