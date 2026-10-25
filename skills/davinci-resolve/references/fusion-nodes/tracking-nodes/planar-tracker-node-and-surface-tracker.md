# Planar tracker node and surface tracker

Version: DaVinci Resolve 20.3 Reference Manual. Context: Planar tracker node, Surface tracker.
[Chapter index](INDEX.md) / [Previous section](planar-tracker-node-steady-mode.md) / [Next section](surface-tracker-mesh.md) / [Continue Surface Tracker SFt / Track](surface-tracker-mesh.md) / [Planar Tracker Node PTRA](planar-tracker-node-what-the-planar-tracker-saves.md)
<a id="source-basic-node-setup"></a> <a id="source-bounds"></a> <a id="source-common-controls"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-options-tab"></a> <a id="source-parameters-to-smooth"></a> <a id="source-surface-tracker-node-introduction"></a> <a id="source-surface-tracker-sft"></a> <a id="source-the-bounds-tab-in-the-surface-tracker-controls"></a> <a id="source-the-planar-tracker-options-tab"></a> <a id="source-the-surface-tracker-node"></a>

### Parameters to Smooth

Specify which of the following parameters to smooth:

- X Translation
- Y Translation
- Rotation
- Scale

Smoothing Window As a given frame is stabilized, this sets how the input from neighboring frames is weighted. The options on offer are Box and Gaussian. Smoothing Radius (Frames) Sets how many frames have their transforms averaged together when the stabilization is computed. Raising the Smoothing Radius produces more smoothing but also brings in more transparent edges. Compute Stabilization A click on this button runs the stabilizer and replaces whatever any earlier stabilization produced. The moment the stabilization completes, the Planar Tracker node's output refreshes at once with the stabilization in effect. NOTE: To produce the Stable Track spline, the stabilizer draws on the Track spline (which the tracker made). The keyframes of both splines carry 4 x 4 matrices, and those keyframes can be edited in the Spline Editor.

Clipping Mode Decides what becomes of the parts of the background image pushed off frame by the stabilization:

- Domain: The off frame parts are kept.
- Frame: The off frames parts are thrown away.

Frame Mode This governs the handling of transparent edges. Its options are:

- Full: Do nothing. Leaves the transparent edges as is.
- Crop: Trims the transparent edges away. With this option chosen, the Planar Tracker's

output image ends up smaller than the input image. No image resamplings take place. While in Crop mode, click the Auto Crop button or set the crop window by hand with the X Offset, Y Offset, and Scale sliders. Auto Crop Button: A click on this button has the Planar Tracker survey every frame and choose the biggest crop window that clears all the transparent edges. That computed crop window stays centered in frame and pixel aligned. On click, Auto Crop refreshes the X/Y Offset and Scale sliders.

- Zoom: Enlarges the image until the transparent edges fall off frame. Picking this option triggers an image resampling. Its drawback is a drop in quality (a slight softening) of the output image. While in Zoom mode, click the Auto Zoom button or set the zoom window by hand with the X Offset, Y Offset, and Scale sliders.

Auto Zoom: A click on this button has the Planar Tracker survey every frame and choose the smallest zoom factor that clears all the transparent edges. That computed zoom window stays centered in frame. On click, Auto Zoom updates the Scale slider together with X/Y Offset. Right-Click Here for Stable Track Spline A right-click on this label opens a spline whose keyframes hold 4 x 4 matrices that in turn stand for the stabilization transforms. It is here chiefly for completeness and for advanced users.

### Options Tab

These controls shape the appearance of the onscreen controls in the viewer.

### The Planar Tracker Options tab

Darken Image Dims the image during Track mode so the controls and tracks read more clearly in the viewer. The Shift+D keyboard shortcut toggles this.

Show Track Markers Switches on or off the dots that mark where the trackers sit at the present time. Show Trails Switches on or off the trails that follow where the trackers go. Trail Length Lets you change how long the tracker trails are. When the pattern crawls along, lengthening them can make the trails easier to read in the viewer. When the pattern races, the tracks may resemble spaghetti in the viewer, and shortening them can help. Inlier/Outlier Colors During tracking, the tracker studies the frame and works out which of the countless tracks belong to the dominant motion and which represent odd, unaccountable motion. By default, the tracks tied to the dominant motion show green (these are the inliers) while those that do not belong show red (the outliers). Only the inlier tracks feed into the computation of the final resulting track.

### Common Controls

Settings Tab The Inspector's Settings tab is mirrored across the other Tracking nodes as well. Full descriptions of these common controls appear in this chapter's closing "The Common Controls" section.

### Surface Tracker [SFt]

### The Surface Tracker node

### Surface Tracker Node Introduction

The Surface Tracker applies textures and effects onto flexible or deformable moving surfaces such as cloth and skin. It makes sure the texture or effect folds and deforms in a way that convincingly tracks the folding and deforming of the surface it is pinned to in the image. As a complex effect, the Surface tracker carries plenty of options and controls aimed at the most realistic composites achievable. Even so, you always work left to right through the buttons in the effect's settings. 1 Click the Bounds button, then click on the screen to mark out the area of the surface where the new texture should go. Have the bounds enclose just one surface at a time and avoid crossing or sitting on object edges. 2 Click the Mesh button to lay down control points along the surface's natural folds and curves inside the bounds.

3 Click the Track button to analyze how the surface moves over time, drawing on the mesh you just laid down. 4 Click the Result button to composite the texture over the moving mesh. Throughout every Surface Tracker tab, the Tracked Range reports the first and last frame numbers of your clip that hold tracking data. Changing the bounds or the mesh layout resets any existing tracking data, and you will have to track it again.

The Surface Tracker at work, laying the logo over the shirt (left) and bending and fitting it believably to the shirt's folds (right). To read more about working with the Surface Tracker, turn to Chapter 168, "Resolve FX Transform."

### Inputs

The Surface Tracker node carries four inputs. Input: The yellow input takes in the media holding the surface you intend to track and composite onto. Overlay: The green input takes in still graphics, video, or a node tree's output. This is the image you want laid over the surface. Occlusion Mask: The pink occlusion mask input serves to mask off regions that need no tracking. Wherever this mask reads white, no tracking happens. For instance, a person passing in front of and hiding portions of the scene can throw off the tracker, so a quick rough mask around that person can instruct the tracker to skip the masked-out portions. Effect Mask: The optional blue effect mask input takes a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps coming from other tools. Wiring a mask here confines the filter to just the pixels inside the mask. An effects mask is applied to the tool once the tool has been processed.

### Basic Node Setup

Wire the media holding the surface you want to composite onto into the main yellow input. Wire the media holding the graphic or video to be overlaid onto the surface into the green overlay input. If you need them, optionally wire effect or occlusion masks into their matching inputs.

A simple node tree showing a video clip of a guitar player, where the surface tracker lays a small graphic of a bee onto his shirt.

### Inspector

### The Bounds tab in the Surface Tracker controls

### Bounds

Here you are asked to draw an area on the image where the texture should be applied. The ideal pick is a frame in the clip where the surface you want to track sits as near and as square-on to the camera as it can. That frame turns into the effect's default reference frame. Just click on the image to drop several points around the area you mean to define (three points is the minimum), and the effect will link them up into a polygon for you. Place boundary points on the surface meant for tracking, not surrounding it. Dropping points by mistake on object edges or the background instead will introduce tracking errors. The same image can carry several boundaries and several holes, with all boundaries fusing into a single shape before the holes are subtracted out. Several boundaries and holes exist so you can mask off complex surfaces while leaving out regions that should not be tracked. For instance, you might draw a boundary around a person's face yet use several holes to leave out the eyes and mouth, since those shift appearance fast as the subject blinks and speaks, which makes them notoriously hard to track. Several boundaries are meant to operate on one and the same surface; putting several boundaries across different surfaces in the image yields poor results. To track separate surfaces, it is better to use several instances of the Surface Tracker. The boundary serves to analyze a surface's motion, not to rotoscope objects. Foreground objects can be rotoscoped as the Tracking Using a Mask section below explains. Click to Add Points: These are the controls for building boundary areas on the image.

- Boundary: The boundary area presently selected on the image. The drop-down menu lets you switch which boundary or hole is current. When the boundary has problems (such as crossed edges, too few points, and so on), an error message shows up beside the boundary name.
- - Bound: Drops a boundary polygon onto the image. Several boundaries can be defined for one surface, and they merge into a single shape.
- - Hole: Adds a region to keep out of the surface tracking. Handy for pulling overly complex, shifting portions of a surface out of the effect's calculations.
- Delete: Removes whichever boundary or hole is selected in the Boundary field. For now this action cannot be undone, so take care with this button.
- Clear All: Removes every boundary and hole in the effect.
