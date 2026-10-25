# Resolve FX and resolve FX video collage updated

Version: DaVinci Resolve 21 New Features Guide. Context: Color and keyframing.
[Chapter index](INDEX.md) / [Previous section](aces-amf-and-dolby-hdr-analysis-reset.md) / [Next section](resolve-fx-and-immersive.md)
<a id="source-content"></a> <a id="source-picture-in-picture"></a> <a id="source-position"></a> <a id="source-resolve-fx"></a> <a id="source-resolve-fx-1"></a> <a id="source-resolve-fx-2"></a> <a id="source-resolve-fx-3"></a> <a id="source-resolve-fx-video-collage-updated"></a> <a id="source-style"></a> <a id="source-the-picture-in-picture-output-in-the-viewer"></a>

## Resolve FX

### Resolve FX

### Resolve FX Video Collage Updated

The Video Collage Resolve FX now carries independent tile fill and border controls, much like the Picture in Picture effect covered above.

### Picture in Picture

Picture in Picture is a fresh Resolve FX that drops a smaller video window over a full-frame video clip beneath it. With Picture in Picture you can watch several subjects together, each lending context to the others. The trick goes back nearly to the dawn of television as an analog effect, and it now arrives fully reworked in the digital realm, packed with settings and parameters for tuning the exact look you're after. Start in either the Cut or Edit pages by laying out a timeline whose full-sized background video sits on the main track and whose intended smaller picture rides a track above it. Reaching into the effects tools, drop the Picture in Picture effect onto the upper clip — the one meant to shrink — and tweak it in the inspector. The inspector's parameters then let you land precisely the framing and shape you want. The Open FX Overlay view also lets you reposition, change the ratio of, and scale the Picture in Picture right inside the viewer. Arranging the clips on the timeline: the background footage sits on the lower track, with the smaller picture stacked above.

### RESOLVE FX

Another route is the Color page, where you bring the Picture in Picture effect into the node tree from the Effects Library; at first, though, the node's background renders black rather than transparent. To carry the transparency through to the timeline, an Alpha Output has to be added to the node graph. Right-click anywhere in the Node Graph and pick Add Alpha Output from the context menu, which drops a small blue output box onto the node graph; then wire the Picture in Picture node's blue alpha output across to that Alpha output to finish the effect, as the example below shows. Adding an Alpha Output, then routing the blue alpha channel of the Picture in Picture into it. The inspector's parameters then let you nail the precise framing and shape you want. As before, the Open FX Overlay view lets you move, re-ratio, and scale the Picture in Picture straight inside the viewer.

### RESOLVE FX

### The Picture in Picture output in the viewer

### Content

Tunes the source video feeding the smaller picture.

- Zoom: Pushes the PiP source in or pulls it out.
- Pan: Slides the PiP source side to side.
- Tilt: Shifts the PiP source up or down.

### Position

Sets where the Picture in Picture sits and how large it is. These same parameters can be nudged in the viewer by dragging while in Open FX Overlay mode.

- Position X/Y: Places the PiP window within the frame.
- Width: Sets how wide the PiP window is.
- Height: Sets how tall the PiP window is.

### Style

This set of tools shapes and lays out the window itself.

- Rounding: Sets how rounded the PiP window's corners are, running from right angles (0) up to a circle (1).
- Rotation: Lets you spin the PiP window.
- Opacity: Fixes the PiP window's opacity.
- Border: Ticking this box wraps a colored border around the PiP window and

activates the toolset below. Border Width: Sets how thick the window's border is. Border Color: Picks the hue of the window's border. Border Opacity: Sets how opaque the window's border is.

- Fill Matches Border: Tick this box to make the window's background take on the same color as the border.
- Fill: Tick this box to paint a background behind transparent content in the frame, which reveals the toolset below. Fill Color: Picks the fill's hue. Fill Opacity: Sets how opaque the fill is.
- Drop Shadow: Tick this box to lay a drop shadow beneath the PiP window, opening the toolset below. Strength: Governs how pronounced the drop shadow is. Color: Sets the drop shadow's hue. Drop Angle: Sets the direction from which the drop shadow falls. Drop Distance: Sets the gap separating the PiP window from its drop shadow. Expand: Enlarges or contracts the drop shadow. Blur: Controls how soft the drop shadow's blur is.
- Use Alpha: Tick this box to draw on the tool's alpha channel during compositing.
