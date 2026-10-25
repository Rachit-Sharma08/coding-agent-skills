# Five color page sizing modes and sizing order of processing on the color page

Version: DaVinci Resolve 20.3 Reference Manual. Context: Sizing and image stabilization.
[Chapter index](INDEX.md) / [Next section](sizing-presets-and-node-channel-effects.md)
<a id="source-blanking-controls"></a> <a id="source-resetting-the-sizing-palette"></a> <a id="source-sizing-and-image-stabilization"></a> <a id="source-sizing-and-image-stabilization-part-1"></a> <a id="source-sizing-controls"></a> <a id="source-sizing-order-of-processing-on-the-color-page"></a> <a id="source-the-five-color-page-sizing-modes"></a> <a id="source-the-sizing-palette"></a>

### Sizing and Image Stabilization

For geometric transforms, DaVinci Resolve carries a capable toolset that leans on advanced algorithms to deliver optical-quality sizing. This section digs into how resolution independence works in DaVinci Resolve, plus how to work the Sizing palette. The chapter also walks through putting the Tracker palette’s Stabilizer mode to use for taming unwanted camera wobble.

### The Five Color Page Sizing Modes

On the Color page, the Sizing Palette can be switched into any of five modes, each handling its own job.

- Edit Sizing: These controls echo the ones living in the Edit page’s Inspector.
- Input Sizing: With these controls you size individual clips in ways that touch their

overall geometry (pan, tilt, zoom, and rotation). They come in handy for clip-by-clip pan and scan tweaks.

- Output Sizing: These controls are virtually the same, save that they touch every clip across the whole timeline at once. Output sizing helps when you want to reformat a whole timeline, say turning an HD timeline into an SD timeline with quick tweaks that crop and pan the resulting framing.
- Node Sizing: Lets you drop pinpoint sizing tweaks anywhere along the node tree. As with Input Sizing, Node Sizing applies to one particular clip. In contrast to Input Sizing, Node Sizing is influenced by operations that break apart color channels (like the splitter/combiner nodes) and confine the image (like qualifiers and windows). You can also stack as many node sizing tweaks onto a clip’s grade as you require.
- Reference Sizing: A group of sizing controls that lets you shift the still while a wipe comparison is underway. With these controls you can nudge the still image to line it up better against the clip you’re wiping it against. The Reference Sizing controls function only while you have a wipe switched on.

### Sizing Order of Processing on the Color Page

Input Sizing tweaks take effect ahead of every bit of image processing happening in the node graph, Node Sizing included, whereas Output Sizing tweaks take effect once the node graph’s image processing is done.

### Sizing Controls

Input, Node, and Output Sizing have a lot of the same controls in common. With the Sizing palette switched to Input Sizing mode, the controls reshape each clip on its own. When you’re merely pushing in on a clip or two, or making one-off pan and scan tweaks to handle a format change, these are the controls to reach for.

### The Sizing palette

- Pan: Slides the clip along the horizontal X axis. Positive figures push the clip rightward; negative ones push it leftward.
- Tilt: Slides the clip along the vertical Y axis. Positive figures push the clip upward; negative ones push it downward.
- Zoom: Tunes the clip’s overall dimensions. The range is from 0.250 (1/4x size) to 4.000 (4x size). Normal size is 1.000.
- Rotate: Positive figures spin the clip clockwise. Negative figures spin it counter-clockwise.
- Width: Stretches the picture broader or thinner. The range is from 0.250 (1/4x width) to

  4.000 (4x width). Normal width is 1.000.

- Height: Stretches the picture so it grows taller or squatter. The range is from 0.250 (1/4x height) to

  4.000 (4x height). Normal height is 1.000.

- Pitch: Spins the image toward or away from the camera around an axis that runs through its

middle, from left to right. Positive values shove the image’s top away and draw its bottom forward. Negative values draw the top forward and shove the bottom away. The bigger the value, the harder the image is stretched.

- Yaw: Spins the image toward or away from the camera around an axis that runs through its middle, from top to bottom. Positive values draw the image’s left side forward and shove its right side away. Negative values shove the left side away and draw the right side forward. The bigger the value, the harder the image is stretched.
- Key Lock: (Node Sizing only) Lets you decide how regions of the image fenced off by one or more windows get transformed. Two options exist:

Off: While off, the transform controls shift the windowed region over to a different part of the frame, in effect cloning the windowed area. On: While on, the transform controls draw other parts of the frame into the windowed regions, in effect masking the windowed area with another slice of the picture.

- Flip Image: Two buttons let you flip the image in different dimensions.

Flip Horizontal control: Mirrors the image along the X axis, left to right. Flip Vertical control: Mirrors the clip along the Y axis, flipping it upside down.

- Lens Correction: (Edit Sizing only) A pair of controls let you fix lens distortion in the picture, or introduce lens distortion of your own (offered only in the Studio version).

Analyze: On its own, examines the frame at the playhead’s spot in the Timeline for edges bent by a wide angle lens. Pressing the Analyze button reshapes how the Distortion slider behaves so it lands a more accurate result, though it carries out no correction itself. Distortion: Drag this slider rightward to lay a warp onto the picture that straightens the bent regions wide angle lenses can introduce. You don’t have to press the Analyze button before reaching for this slider, but pressing it can sharpen the accuracy of the outcome.

### Blanking Controls

Output Sizing mode further carries a group of Blanking controls you can put to use adding custom blanking onto a clip or project. As an example, these controls let you put nonstandard letterboxing or pillarboxing onto an image. Like every other Output Sizing tweak, blanking enters the image processing pipeline last, so none of the color or contrast tweaks you make touch it.

- Top: Adjusts the top letterbox.
- Right: Adjusts the right pillarbox.
- Bottom: Adjusts the bottom letterbox.
- Left: Adjusts the left pillarbox.
- Smooth: A checkbox that switches on edge anti-aliasing for source blanking. It overrides the

Anti-alias Edges drop-down menu sitting in the Image Scaling panel of the Project Settings.

NOTE: You may have to switch anti-aliasing off if black blurring shows up along the edges of the blanking laid onto an image. Blanking presets can also be reached by picking from the Timeline > Output Blanking submenu. Picking one of these entries sets the Blanking parameters of the Sizing palette’s Output Sizing mode automatically. Here’s what you can pick from: 1.33: SD or 4:3 1.66: the European theatrical ratio 1.77: HD or 16:9 1.85: the theatrical flat aspect ratio 2.00: Univisium, an aspect ratio built to serve both theatrical wide-screen alongside HD delivery. 2.35: original anamorphic (scope) theatrical wide-screen 2.39: current 35mm anamorphic (scope) theatrical wide-screen 2.40: a current 35mm anamorphic (scope) theatrical wide-screen ratio (rounded up for Blu‑Ray) Reset: returns the clip to the aspect ratio it began with. Edge anti-aliasing on the blanking is governed by an Anti-Alias Edges setting sitting in the Project Settings’ Image Scaling panel. To read more, refer to Chapter 4, “System and User Preferences.”

### Resetting the Sizing Palette

At any moment you can clear every control inside the Sizing palette by pressing the reset button up in the palette’s top right-hand corner.
