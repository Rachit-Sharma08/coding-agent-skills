# Krokodove toolset integrated into Fusion and edit effects and 3D mapped duplicate 3D

Version: DaVinci Resolve 21 New Features Guide. Context: Compositing.
[Chapter index](INDEX.md) / [Next section](macro-edior-and-enter-a-name-for-your-macro.md)
<a id="source-3d-mapped-duplicate-3d"></a> <a id="source-enter-a-name-for-your-macro"></a> <a id="source-fusion"></a> <a id="source-fusion-part-1"></a> <a id="source-image-color-tools-invert-match-color"></a> <a id="source-image-create-tools-blobs-generate-lines-pattern-shapes"></a> <a id="source-image-pixel-tools-average-bevel-channel-shifter"></a> <a id="source-image-tools-rasterize"></a> <a id="source-image-warp-tools-offset-radial"></a> <a id="source-improved-macro-editor"></a> <a id="source-krokodove-toolset-integrated-into-fusion-and-edit-effects"></a> <a id="source-recolor-replace-color-threshold"></a> <a id="source-relative-transform"></a> <a id="source-the-fusion-macro-editor"></a> <a id="source-time-mapper-worm"></a> <a id="source-using-the-macro-editor"></a>

### Fusion

### Krokodove Toolset Integrated into Fusion and Edit Effects

The well-liked third-party Krokodove Fusion tools now ship built straight into DaVinci Resolve and Fusion, adding well over a hundred fresh motion graphics effects and tools. What follows is a short rundown of the toolset:

### 3D Mapped Duplicate 3D

Builds a 3D grid of cloned objects spanning X, Y and Z space. Imagery can drive the offset, rotation, scale, and timing of those objects.

Image Tools Bounding Box Color Map Connect Dither Extend Fragments Grow Grow Color Microwaves Pack Painterly

Paints a rectangle out of a chosen channel, its dimensions governed by the Threshold controls. Maps a texture onto one or several flat colors, which you either pick by hand or have detected for you. Connect lays an unbroken line between separate points, each of which you can place on its own to form ‘way-points’ along that line. Dither is a filter that seeds a noise pattern to suggest shading; its various methods can yield a crisp, crunchy texture. Extend copies edge pixels along a horizontal or vertical axis for a repeating-pixel effect. Fragments slices an image into discrete pieces you can then fade in or out through the Range options. Grow lets an image expand or vanish outward from one or more seed locators. Grow Color pushes the color at an image’s edge outward, packing transparent regions by stretching those edges. Microwaves throws radiating highlights out from a center point, mimicking light beams and adding controls to reshape the whole form. Pack assembles patterns of stacked shapes inside a nominated color channel. Painterly is a filter effect that lays a stylized ‘artwork’ finish over an image or graphic.

### Image Tools Rasterize

### Time Mapper Worm

### Image Color Tools Invert Match Color

### Recolor Replace Color Threshold

### Image Create Tools Blobs Generate Lines Pattern Shapes

### Image Pixel Tools Average Bevel Channel Shifter

Rasterize is a filter effect that takes an image and recasts it as a run of shapes — dots, squares or diamonds — handy for producing a half-tone look. Time Mapper blends different moments of a sequence under the direction of an external image map. Worm assembles a mix of straight and curved lines from points you specify. Invert flips the color, luminance or hue. Reach for Match Color to grab a tonal band — shadows, midtones, or highlights — and swap it out for a color. Recolor hands you controls for substituting colors: nominate one or more source colors and replace those picks with new ones via the color swatch. Alternatively, nominate a single source color and trade it for a correction. Threshold isolates a tight, specific span of color or brightness within a nominated channel, with its controls letting you tune the selection’s tolerance. Blobs scatters circular shapes at the points you specify. Generate is a tool for adding texture to a source input; producing a greyscale image, it lays down what looks like a randomized noise pattern. The Lines tool forms patterns from one or several line sets and spawns multiple tiers of repeating lines. Pattern lays out an array of tessellated shapes for a full-frame design. The Shapes tool stacks several tiers of concentric shapes, squares and circles included. This tool averages a run of consecutive frames in a sequence for a frame-blending effect. The Bevel tool draws an inner bevel around an image to imply depth. Channel Shifter splits the RGBA channels apart and supplies controls to offset, blur, or scale them.

Image Pixel Tools Clean Edges Deflicker Duplicate Extrude Noise Plastic Positioner Push Rest Seamless Seamless Loop Sort Image Position Tools Contour Image Vector Tools Vector Visualisation Image Warp Tools Bend Directional Scale Kaleidoscope Mirror

Strips off frame-edge pixels, either by duplicating them or filling with a solid color. Frame border. Deflicker irons out flickering — local or across the whole frame — over consecutive frames. Repeats the incoming image along a chosen pattern or shape. The Extrude tool warps an image’s edge to fake a sense of depth. The Noise tool lays down a pixellated pattern whose colors are either randomly generated or hand-picked. Plastic is a filter tool that produces a synthetic bevel effect, draping a plastic film or sheen across the source image. Positioner is a corner-pinning tool offering source and destination controls. Push yields a ‘slide’ effect: hook up a second image and one slides into the other. Rest nudges pixels so they settle onto a single line, bending an image’s upper or lower portion along a path you set. Seamless mirrors the opposite edge and blends it with the original. Seamless Loop hands you controls to retime a comp into an unbroken looping sequence. Sorts pixels by color value. The Contour tool traces an outline around an image, spawning repeating lines across a gradient. Produces an overlay that shows motion-vector direction and velocity. Bend is a radial warp tool that flexes an image with a three-point spline. Directional Scale is a one-sided scaling tool that stretches an image at a chosen angle. Kaleidoscope is a classic filter tool that radially mirrors the image for a kaleidoscopic result. Reflects the image about an arbitrary axis, flipping it along a line you specify.

### Image Warp Tools Offset Radial

### Relative Transform

Listed here are Segment, Transform, Shear, Shuffle, Spherize, and Stretch; then the Modifiers — Beat, Color Switcher, and Random; and the Text Modifiers — Formula From File, Juggle, and Write.

Offset slides image pixels under the control of another image, shoving the image along the horizontal or vertical axis. Drives pixels radially outward or inward rather than scaling them, yielding a dent-like distortion. Draws on a second input to warp or distort via position, rotation, and scale controls. Its transformation pivot is read off the incoming image and can be placed relative to the actual pixel data. Splits the frame into square segments, each one taking its own angle and scale distortion. The Shear tool imposes an angular shear, with the extra input governing how strong that shear is; the subdivided frame is then shifted around inside the image. Spherize is a radial and cylindrical deformation tool that bends a round-style warp into a chosen region. The Stretch tool elongates an image along any preset axis, stretching pixels along a line you specify. The Beat modifier supplies controls to animate in Frames per Beat or Beats per Minute, alongside Start and End time, Attack, Decay, Sustain, and Release. Faced with several color palettes, this modifier makes hopping between them — or rotating colors inside one palette — straightforward; setting it up means wiring individual channels (RGBA) to the separate outputs. (A script here would be handy). The Random modifier bolts a random-value generator onto any control, letting you bound the Min and Max range of values to randomize, plus controls that spread new random values across a frame range for a smooth glide from one value to the next over time. Custom tool acting as a modifier. A modifier that lets the user pull in a txt-format file or type entries by hand, with controls to reveal text one line at a time for a fixed or custom span. A modifier that shuffles characters at random. A Write On-style modifier offering to append a cursor or caret at the text’s tail, as though it were being keyed in from a device; it can also tack on a Prefix that stays permanently visible, IE untouched by the write-on effect.

### Improved Macro Editor

DaVinci Resolve 21 sharpens the Fusion macro editor considerably, making it more intuitive and showing a live preview in the inspector of how your macro will look while you assemble it. That preview lets you put together even the trickiest macros with faster iteration feedback and greater clarity. Certain effects don’t come from a single tool but from a whole chain of operations, occasionally across tangled branches whose parameter controls interlink. Fusion offers plenty of individual effects nodes to work with, yet also lets you repackage them in varied combinations as self-contained “bundles” — either macros or groups. Such “bundles” bring a few benefits:

- They cut down on visual clutter throughout your node tree.
- They safeguard sound user interaction by letting you limit which controls from each node of

the macro are available to the user.

- They lift productivity by letting artists rapidly reuse ready-made answers to common compositing

challenges and creative adjustments that have already been built and saved.

### Using the Macro Editor

Every macro begins from the individual tools sitting in the node editor. Pick out the tool or tools there that you want a macro built from, then right click one of them and choose Macro > Create Macro off the context menu. Up comes the Macro Editor.

### The Fusion Macro Editor

Three principal areas make up the Macro Editor:

### Enter a name for your macro

Up top sits the Macro Name field, where you title your macro for the tool list; right-clicking the magic wand icon lets you pick an image to serve as the new macro’s thumbnail icon.
