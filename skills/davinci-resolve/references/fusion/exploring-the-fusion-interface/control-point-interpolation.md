# Control point interpolation and control point interpolation controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Exploring the Fusion interface.
[Chapter index](INDEX.md) / [Previous section](essential-spline-editing-tools-and-modes.md) / [Next section](bins-in-fusion-studio-and-bins-window.md)
<a id="source-control-point-interpolation"></a> <a id="source-control-point-interpolation-controls"></a> <a id="source-importing-media-into-the-media-pool-on-the-fusion-page"></a> <a id="source-spline-editing-controls"></a> <a id="source-spline-editing-tools"></a> <a id="source-spline-loop-modes"></a> <a id="source-spline-loop-modes-1"></a> <a id="source-the-contextual-menu-for-the-thumbnail-timeline"></a> <a id="source-the-media-pool-in-the-fusion-page"></a> <a id="source-thumbnail-timeline-in-the-fusion-page"></a>

### Control Point Interpolation

Those first six buttons let you reshape the interpolation across one or more chosen control points.

### Control point interpolation controls

Smooth: Builds Bézier curves that adjust on their own to yield smoothly interpolating animation. Linear: Builds straight-line interpolation running between control points. Invert: Flips the vertical placement of LUT splines that aren't animated. It has no effect on animation splines. Step In: At each keyframe, produces abrupt value jumps at the keyframe immediately to its right. Much like a hold keyframe in After Effects® or a static keyframe over on the DaVinci Resolve Color page. Step Out: Produces abrupt value jumps at every keyframe where the value shifts at the next keyframe to its right. Much like a hold keyframe in After Effects or a static keyframe over on the DaVinci Resolve Color page. Reverse: Flips the chosen keyframes' horizontal placement in time, leaving the keyframes running backward.

### Spline Loop Modes

The three buttons that follow let you arrange spline looping past the final control point on a parameter's spline, letting a small run of keyframes animate across a vastly longer span. Looping touches only the control points you've selected.

### Spline Loop modes

Set Loop: Plays back the identical keyframe pattern again and again. Set Ping Pong: Plays a reversed copy of the chosen keyframes followed by a straight copy of them, knitting a smoother run of animation. Set Relative: Plays back the identical pattern of chosen keyframes, but bumps the values of each repeated pattern up or down by the overall trend across every keyframe in the selection. The upshot is a keyframe loop whose value climbs or falls steadily with each fresh loop.

### Spline Editing Tools

The five buttons after that supply purpose-built Spline editing tools.

### Spline editing controls

Select All: Grabs every keyframe presently on hand in the Spline Editor. Click Append: One click turns this tool on, another click turns it off. The tool lets you add or rework keyframes and spline segments (the stretches of spline between two keyframes), according to whichever keyframe mode you're in. Under Smooth or Linear keyframes, clicking anywhere over or under a spline segment drops a fresh keyframe onto the segment right where you clicked. Under Step In or Step Out keyframes, clicking anywhere over or under a line segment shifts that segment to the spot you clicked. Time Stretch: Once you've chosen a range of keyframes, flipping on the Time Stretch tool brings up a box for squeezing and stretching the whole keyframe range against one another, reshaping the broad timing of a keyframe sequence while holding the relative spacing from keyframe to keyframe. As an alternative, you can flip on Time Stretch and drag a bounding box over the keyframes you mean to adjust, making a time‑stretching boundary that way. A second click on Time Stretch shuts it off. Shape Box: Flip on the Shape Box to drag a bounding box over a cluster of control points you want to work, so you can squish and stretch them horizontally (via the top/bottom/ left/right handles), corner pin (via the corner handles), move (by hauling on the box edge), or stretch a corner (Command-drag a corner handle). Show Key Markers: Flipping this control on surfaces keyframes up in the top ruler matching the frame where each visible control point sits. Those keyframes take on the color of the control points they point to.

### Thumbnail Timeline in the Fusion Page

Over on the Fusion page of DaVinci Resolve, the Thumbnail timeline (which stays hidden by default) opens up when you click the Clips button in the UI toolbar, and it shows beneath the Node Editor while open. The Thumbnail timeline puts every clip in the current Timeline on view, handing you a way to move from clip to clip. Each thumbnail carries a pop-up menu for building and flipping among several composition versions, and for resetting the current composition whenever that's needed.

Through the Thumbnail timeline you move around the Timeline and handle the various composition versions.

Right-clicking any thumbnail brings up a contextual menu.

### The contextual menu for the Thumbnail timeline

To open another clip:

- Click any thumbnail to leap to that clip's composition. An orange outline marks the current clip.

To navigate the Thumbnail timeline:

- Middle-click and drag the Timeline either way to scroll across the clips in the Timeline.
- Click and drag the slider down at the foot of the Thumbnail timeline to scroll across the clips in the Timeline.

To create and manage versions of compositions:

- To spin up a fresh composition version: Right-click the current thumbnail and pick Create New Composition off the contextual menu.
- To load a different composition: Right-click the current thumbnail and pick “NameOfVersion” > Load off the contextual menu.
- To delete a composition: Right-click the current thumbnail and pick “NameOfVersion” > Delete off the contextual menu.
- To rename a composition: Right-click the current thumbnail and pick “NameOfVersion” > Rename off the contextual menu.

To reset the current composition:

- Right-click the current thumbnail and pick Reset Current Composition off the contextual menu.

To change how thumbnails are identified:

- Double-click the strip beneath any thumbnail to cycle among clip format, clip name, and the composition version name.

### The Media Pool in the Fusion Page

On DaVinci Resolve's Fusion page, the Media Pool keeps right on doing its job as the home for all the media you've brought into your project. That makes pulling extra clips into your compositions a snap — just drag whichever clip you want out of the Media Pool and into the Node Editor. Media you bring in lands as a fresh MediaIn node in your composition, set to be worked into your node tree however suits you. TIP: Should you drag one or several clips from the Media Pool onto a connection line linking two nodes in the Node Editor, the clips wire onto that line automatically by way of enough Merge nodes to join them all.

To dig into the countless capabilities of the Media Pool, turn to Chapter 18, “Adding and Organizing Media with the Media Pool.”

The Media Pool in Thumbnail mode showing video clips

### Importing Media Into the Media Pool on the Fusion Page

Should you be sitting on the Fusion page and need to bring in a few clips fast for immediate use, a couple of routes are open to you. Bringing media in by dragging a clip or several out of the Finder onto the Fusion page Media Pool (macOS only) goes like this: 1 Pick one or more clips over in the Finder. 2 Drag those clips into DaVinci Resolve's Media Pool, or onto a bin in the Bin list. Those clips join your project's Media Pool. Leaning on the Import Media command within the Fusion page Media Pool goes like this: 1 With the Fusion page on screen, right-click anywhere in the Media Pool and pick Import Media. 2 Through the Import dialog, pick one or more clips to bring in, and click Open. Those clips join your project's Media Pool.

To dig into bringing media in through the countless capabilities of the Media page, turn to Chapter 18, “Adding and Organizing Media with the Media Pool.”
