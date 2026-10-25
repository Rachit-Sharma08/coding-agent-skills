# Resolve FX and immersive

Version: DaVinci Resolve 21 New Features Guide. Context: Color and keyframing.
[Chapter index](INDEX.md) / [Previous section](resolve-fx-and-resolve-fx-video-collage-updated.md) / [Next section](vr-180-360-delivery-preset-and-immersive.md)
<a id="source-immersive"></a> <a id="source-immersive-1"></a> <a id="source-immersive-2"></a> <a id="source-immersive-3"></a> <a id="source-immersive-4"></a> <a id="source-immersive-delivery"></a> <a id="source-immersive-project-settings"></a> <a id="source-immersive-transform"></a> <a id="source-immersive-transform-1"></a> <a id="source-immersive-viewer"></a> <a id="source-immersive-viewer-selection"></a> <a id="source-resolve-fx-4"></a> <a id="source-the-immersive-transform-tool-in-the-video-inspector"></a> <a id="source-vr180-and-vr360-standard-immersive-workflow-support"></a>

### RESOLVE FX

## Immersive

### Immersive

### VR180 and VR360 Standard Immersive Workflow Support

For standard immersive formats, DaVinci Resolve 21 now handles VR180 and VR360 workflows. That opens up editing and producing content for a broad range of VR headsets and platforms without locking you to one manufacturer. Within immersive timelines you can even blend VR180 and VR360 together, with cropping and refitting done automatically. That said, the wide spread of resolutions, formats, and frame rates that VR brings does call for some setup at the outset.

### Immersive Project Settings

Ahead of bringing VR media into the media pool, head into Project Settings and choose Master Settings > Immersive workflows > Standard Immersive. Flipping that switch turns on the immersive toolset in DaVinci Resolve. With the Standard Immersive Workflow chosen, set the resolution — VR180 uses a 1:1 ratio while VR360 uses a 2:1 aspect ratio.

### IMMERSIVE

Choose Standard Immersive for the Immersive workflows setting prior to loading clips into the media pool Clip Attributes With your project settings in place and all of your immersive clips imported into the media pool, you then have to flag them as VR clips by hand through the clip attributes. Select every clip, right-click one of them, and pick Clip Attributes from the context menu. Over in the Video tab of Clip Attributes, confirm that the Stereoscopic Mode and Projection Format attributes line up with your particular VR Camera's footage, then click OK.

Across all your clips, configure the Stereoscopic Mode and Projection format within Clip Attributes.

### Immersive Viewer

A new Immersive Viewer mode arrives in DaVinci Resolve 21, usable across the Media, Edit, Color and Fairlight pages. The mode swaps between an ordinary 2D view and, via Viewport mode, a simulated VR headset, so you can check your VR footage without strapping a headset on. While in this mode you can also click and drag within the viewer to spin the view around. Do note that it is purely a preview — it does not genuinely reorient your footage.

### IMMERSIVE

The Immersive Viewer (red rectangle) shown in LatLong view, presenting an equirectangular 360 image.

The Immersive Viewer (red rectangle) shown in Viewport mode, presenting that same 360 image as simulated within a headset.

### Immersive Viewer Selection

Determines the way VR content is presented within the Viewer.

- LatLong: Presents the content using an equirectangular projection.
- Viewport: Mimics a VR headset inside the viewer and lets you tweak head position and

field of view.

- Tilt: Pivots the head view about the Y (vertical) axis. Drag left or right within

the numeric field, or up and down inside the viewer, to shift the view.

- Pan: Pivots the head view about the X (horizontal) axis. Drag left or right

in the numeric field, or left and right inside the viewer, to shift the view.

- H. FoV: Adjusts the horizontal field of view to line up with the headset's FoV.

Clicking the little link icon ties the Horizontal and Vertical fields of view to one another.

- V. FoV: Adjusts the vertical field of view to line up with the headset's FoV. You can

tap that small link icon to bind together both the Horizontal and Vertical view fields.

### IMMERSIVE

### Immersive Transform

Choosing a Standard Immersive project setting brings the Immersive Transform tool to life in the Video Inspector. Its parameters point the VR video clip a particular way, letting you decide what greets the viewer when they first face forward in the headset. The tool is also handy for aligning two immersive clips so the cut between them feels visually right. Although the parameters are keyframable and can be animated, you're better off keeping them fixed and letting viewers tilt, pan, and roll through their own head movements — pushing forced directional motion in VR tends to bring on nausea.

### The Immersive Transform tool in the Video Inspector

### Immersive Transform

Sets where the footage starts out within the VR content.

- Tilt: Pivots the footage about the Y (vertical) axis. Drag the slider to reposition it.
- Pan: Pivots the footage about the X (horizontal) axis. Drag the slider to reposition

the footage.

- Roll: Pivots the footage about the Z (roll) axis. Drag the slider to reposition it.

### Immersive Delivery

The Deliver page now offers a new VR 180/360 delivery preset built to work with the broadest spread of VR headsets, Meta Quest among them. You're still free to adjust the settings to fit your specific headset more closely. This Delivery setting tacks extra VR format data onto the file name on its own, and that data cues the right playback behavior in most VR players.
