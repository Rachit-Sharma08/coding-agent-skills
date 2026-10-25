# Floating window controls and animating floating windows

Version: DaVinci Resolve 20.3 Reference Manual. Context: Stereoscopic workflows.
[Chapter index](INDEX.md) / [Previous section](stereo-auto-alignment-and-color-match.md) / [Next section](macos-apple-spatial-video.md) / [Continue Apple Spatial Video (MacOS Only) / Using Apple Spatial Video in DaVinci Resolve](macos-apple-spatial-video.md)
<a id="source-animating-floating-windows"></a> <a id="source-apple-spatial-video-macos-only"></a> <a id="source-floating-window-controls"></a> <a id="source-outputting-stereo-3d-media-in-the-deliver-page"></a> <a id="source-rendering-frame-compatible-media"></a> <a id="source-rendering-individual-left--and-right-eye-clips"></a>

### Floating Window controls

The point of Floating Windows is to shape the illusion of the viewer’s “window into the scene.” Beyond repairing Window violations, some have suggested that Floating Windows can serve as a creative device, the geometry of this Window being reshaped to subtly shift how the viewer reads the screen’s orientation.

- Trimming the right-eye frame along its right-hand side produces the illusion that the

“window into the image” has its right edge leaning farther forward toward the viewer.

- Trimming the left-eye frame along its left-hand side produces the illusion that the Window’s

left edge is leaning toward the viewer.

- Crop the left-eye frame on its left edge while also cropping the right-eye frame on its

right edge, and the whole plane of the “virtual screen” seems to advance toward you.

- Apply oppositely angled Windows across the left- and right-eye clips at either edge of the frame (or both), and the screen seems to “tilt” toward or away from the viewer.

### Animating Floating Windows

You can animate Floating Windows via the Float Window keyframing track, located inside the Sizing track of the Keyframe Editor, pushing the frame edge inward when required and then drawing it back out once the partly occluded subject has fully entered frame. To read more about animating keyframing tracks, turn to Chapter 148, “Keyframing in the Color Page.” The controls and parameters offered by Floating Windows are these.

- L/R/T/B buttons: Lets you pick an edge on which to place a Floating Window. Click the button for the edge you wish to adjust. Each edge carries its own position, rotate, and softness settings.
- Position: Brings masking to the currently selected edge.
- Rotate: Turns the currently selected edge so you can build an angled Window.
- Softness: Feathers the currently selected edge so you can build a soft Window that viewers notice less.

To add a Floating Window to fix a Window violation: 1 Decide which eye should receive the Floating Window.

- For a Window violation on the screen’s right-hand side, click the right eye view to put a Floating Window there.
- For a Window violation on the screen’s left-hand side, click the left eye view to put a Floating Window there.

2 Pick the edge you’ll adjust by clicking the L or R buttons.

- To clear a Window violation on the right-hand side, click R.
- To clear a Window violation on the left-hand side, click L.

3 Tune the Position parameter however much is needed to crop away the strip along the selected eye’s edge that the other eye can’t see. 4 If you decide the Window tweak you just made stands out too much, raise the Softness parameter so that edge becomes harder to notice.

### Outputting Stereo 3D Media in the Deliver Page

For full frame media, each stereo 3D eye has to be rendered on its own through the Deliver page controls, exported in whichever media format the client demands.

### Rendering Frame-Compatible Media

Frame-compatible media packs both left- and right-eye images, anamorphically squeezed, into one media file. To produce it, pick the “Both eyes as” option among the Render Stereoscopic 3D controls sitting beneath the Deliver page’s File output options, then select an output method from the Mesh Options pop-up menu.

Stereoscopic 3D mesh render options on the Deliver page Your choices are Side-by-Side, Line-by-Line, or Top-Bottom. Anaglyph is another choice when you need a classic red/cyan anaglyph stereo 3D image that any display can show.

### Rendering Individual Left- and Right-Eye Clips

When your pipeline calls for delivering separate left- and right-eye media sets, this is simple: either configure a render job with “Render Stereoscopic 3D” set to “Right eye” or “Left eye,” or pick “Both eyes as” and choose the “Separate files” option.

### Apple Spatial Video (MacOS Only)

Newer Apple iPhone models include a Spatial Video mode that records 3D videos meant for viewing in a VR headset. DaVinci Resolve recognizes these spatial videos automatically and lets you apply every DaVinci Resolve feature to them, the complete 3D toolset described above included.

Grading an Apple Spatial Video on the Color page with Anaglyph (B/W) mode engaged (the colorist’s goofy 3D glasses not shown)
