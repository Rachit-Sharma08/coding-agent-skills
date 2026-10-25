# Audio effects and generators

Version: DaVinci Resolve 20.3 Reference Manual. Context: Video and audio effects in the cut page.
[Chapter index](INDEX.md) / [Previous section](transition-editing-removal-and-defaults.md) / [Next section](speed.md)
<a id="source-audio-effects"></a> <a id="source-clip-tools"></a> <a id="source-composite"></a> <a id="source-composite-controls-in-the-viewer"></a> <a id="source-crop"></a> <a id="source-dynamic-zoom"></a> <a id="source-dynamic-zoom-controls-in-the-viewer"></a> <a id="source-generators"></a> <a id="source-interactive-resolve-fx-and-fusion-effect-overlays-in-the-viewer"></a> <a id="source-onscreen-crop-controls-in-the-viewer"></a> <a id="source-onscreen-transform-controls-in-the-viewer"></a> <a id="source-shared-controls"></a> <a id="source-the-tools-button"></a> <a id="source-transform"></a>

### Audio Effects

Audio plugins let you treat your audio in various ways—shaping the tone with equalization, reworking dynamics through compression, or layering on effects such as echo, reverb, flange, or modulation. To turn on a particular audio effect for a clip, just drag the chosen effect's thumbnail onto a clip in the upper or lower Timelines on the Cut page; on the Edit page, drag it onto a clip sitting in an audio track. As soon as the effect lands on a clip, its audio plugin controls open so you can tune the plugin's parameters.

### Generators

The assorted video generators bundled with DaVinci Resolve can be previewed when you rest your pointer on any Generators-tab thumbnail. To bring a generator into your Timeline, just grab the thumbnail of the generator you want and set it into your Timeline on the Edit page, or into either the upper or lower Timelines on the Cut page.

To read more on putting all the bundled video and audio effects of DaVinci Resolve to use,

see Chapter 47, "Editing, Adding, and Copying Effects and Filters."

### Interactive Resolve FX and Fusion Effect Overlays in the Viewer

When you've applied a Resolve or Fusion effect that relies on on screen controls, those controls become usable within the Cut Page viewer. The way in: open the Tools panel on the Cut page and pick the Effects Overlay icon at the far right. Two options below let you handle either the Open FX or Fusion Overlays; pick the version that fits your effect. The on screen controls then show up in the Viewer.

A click on the Effects Overlay icon (circled) switches on the on screen controls belonging to Resolve or Fusion effects within the Cut Screen viewer.

### Clip Tools

Clicking the Tools button in the Viewer toolbar opens further categories of controls that let you put various effects on the current clip, or adjust whatever effect already sits on the current clip. Many of these effects' parameters carry matching onscreen controls that let you make visual adjustments right in the Viewer.

### The Tools button

### Shared Controls

Every effect category along the bottom of the Viewer carries two shared controls. Over at the far

left, a toggle control lets you turn an effect on or off without dropping whatever custom adjustments you've made. Over at the far right, a reset control returns every parameter inside a given category of controls to

its default settings.

The Toggle button (at left) and Reset button (at right)

### Transform

Pick Transform and onscreen transform controls surface, letting you work the image directly in the Viewer. A drag anywhere within the clip's bounding box adjusts pan and tilt; a drag on any diagonal corner resizes proportionally; a drag on any top/bottom/left/right side squeezes or stretches the width or height; and a drag on the center handle rotates.

### Onscreen Transform controls in the Viewer

TIP: As you drag a clip with the onscreen controls to reposition it, holding the Shift key down pins movement to just the X or Y axes. Those onscreen controls also match the editable parameters below, the same ones you can edit over in the Video Inspector as well as in the Edit Sizing mode of the Color page's Sizing palette: Zoom Width and Height: Enlarges the image or scales it down. Link the X and Y parameters to lock the image's aspect ratio, or unlink them to stretch or squeeze the image along a single direction. Position X and Y: Repositions the image inside the frame for pan and scan adjustments. X slides the image left or right; Y slides it up or down. Rotation Angle: Spins the image about the anchor point.

Pitch: Tilts the image toward or away from the camera about an axis that runs through the image center, left to right. Positive values send the image's top backward and draw its bottom forward. Negative values draw the top forward while sending the bottom back. Larger values stretch the image to a greater extreme. Yaw: Tilts the image toward or away from the camera about an axis that runs through the image center from top to bottom. Positive values draw the image's left side forward and send its right side back. Negative values send the left side back and bring the right side forward. Larger values stretch the image to a greater extreme. Flip Image: A pair of buttons lets you flip the image across different dimensions.

- Flip Horizontal control: Mirrors the image along the X axis, left to right.
- Flip Vertical control: Mirrors the clip along the Y axis, flipping it upside down.

### Crop

The Cut page carries a set of onscreen controls for cropping the image straight in the Viewer. Each side of the image has its own handle for cropping that side alone. These parameters are likewise editable in the Video Inspector and the Color page Sizing palette.

### Onscreen Crop controls in the Viewer

The Crop effects also match an extra set of cropping parameters, with one more control for softness: Crop Left, Right, Top, and Bottom: Trims the image's four sides by a chosen number of pixels. Because cropping a clip introduces transparency, whatever lies beneath shows through. Softness: Blurs a crop's edges. A negative value softens the edges within the crop box, whereas a positive value softens the edges beyond the crop box.

### Dynamic Zoom

The Dynamic Zoom controls, off by default, make pan and scan effects that zoom into or out of a clip quick and easy. A pair of onscreen controls lets you build a Dynamic Zoom effect. A green box marks where the animated transform starts in size and position, while a red box marks where it ends. Drag anywhere inside either bounding box to reposition the start or the end of the animated effect, and drag any corner to set the size at the start or end. A motion path surfaces to show you the motion being built. Touching the Dynamic Zoom controls turns dynamic zoom on automatically. These controls live in the Video Inspector as well.

### Dynamic Zoom controls in the Viewer

These controls match two parameters in the toolbar (Dynamic Zoom is editable in the Video Inspector too). Zoom/Pan/Angle Presets: Let you turn preset positions on or off for this effect's zoom level, pan location, and angle. Swap: This button flips the start and end transforms that make the dynamic zoom effect. Ease Buttons: Let you set how the motion these controls build speeds up. The choices are Linear, Ease In, Ease Out, and Ease In and Out. TIP: As you drag dynamic zoom outlines to reposition them, holding the Shift key down pins movement to just the X- or Y-axis.

### Composite

Two controls let you build transparency and apply composite modes for different compositing effects (also known as Blend modes or Transfer modes). These controls are editable in the Video Inspector too.

### Composite controls in the Viewer

Composite Modes: Composite modes blend two superimposed clips on the Timeline through different kinds of math to land on differing results, building transparency effects, lifting image exposure, and merging several clips into one image in many inventive and useful ways. Every Composite mode acts in concert with the Opacity slider. For a rundown of what the individual Composite modes do, see Chapter 50, "Compositing and Transforms in the Timeline." Opacity: Across a span from 0 (totally transparent) up to 100 (totally opaque), this slider renders a clip more transparent. Set under 100, the chosen clip blends with whatever video clip lies beneath it on the Timeline, following the Composite mode currently selected. Where no clip appears under the Timeline, the clip blends with black and behaves much like a fade.

TIP: Where a superimposed video or still image clip in the Timeline carries an alpha channel, that alpha channel automatically introduces transparency within the clip, compositing it against whatever sits in the track beneath. You don't need to do a thing for this to work.
