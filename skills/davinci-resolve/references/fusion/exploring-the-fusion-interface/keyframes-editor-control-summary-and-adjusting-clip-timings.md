# Keyframes editor control summary and adjusting clip timings

Version: DaVinci Resolve 20.3 Reference Manual. Context: Exploring the Fusion interface.
[Chapter index](INDEX.md) / [Previous section](navigating-the-node-editor-and-vertical-node-editor-layouts.md) / [Next section](spline-editor-controls-and-parameter-visibility.md)
<a id="source-adjusting-clip-timings"></a> <a id="source-adjusting-effect-timings"></a> <a id="source-adjusting-keyframe-timings"></a> <a id="source-editing-keyframes-in-the-spreadsheet"></a> <a id="source-keyframe-editing-essentials"></a> <a id="source-keyframe-tracks-exposed"></a> <a id="source-keyframes-editor-control-summary"></a> <a id="source-spline-editor"></a> <a id="source-the-keyframe-spreadsheet"></a> <a id="source-time-stretching-keyframes"></a> <a id="source-time-stretching-keyframes-1"></a>

### Keyframes Editor Control Summary

Up top, a row of zoom and framing controls lets you adjust the work area holding the layers.

By way of these controls you can work the Keyframes Editor view. Scaling the editor's size is handled through a Horizontal zoom control.

- A Zoom to Fit button sizes the full width of every layer to match how wide the Keyframes Editor currently is.
- A Zoom to Rect tool has you draw out a rectangle, marking a region of the Keyframes

Editor to zoom in on.

- A Sort pop-up menu offers a handful of ways to sort or filter the tracks.
- An Option menu opens the door to plenty of other approaches for filtering tracks and

steering which options show. For a time reference—and a spot to scrub the playhead through—there's a timeline ruler. Over at the left, each layer's name lives in a track header, which also carries the controls that govern that layer.

- A lock button keeps a given layer safe from being altered.
- Any node that's been keyframed carries a disclosure control; open it and a

keyframe track appears for every animated parameter. The actual editing area in the center shows all the layers and keyframe tracks the current composition holds. Down at the bottom-left, Time Stretch and Spreadsheet mode controls hand you further ways to work keyframes. Over at the bottom right, the Time/TOffset/TScale drop-down menu together with its value fields let you shift the position of selected keyframes by the numbers—whether absolutely, relatively, or according to how far they sit from the playhead.

### Adjusting Clip Timings

Each Loader or MediaIn node standing for a clip used in a composition shows up as a layer in this scaled-down timeline. You can edit a layer's In or Out points by setting the pointer over a segment's start or end and using the resize cursor to drag that point somewhere new. A layer can be slid by dragging it left or right, helping it sit in sync with how other pieces of your composition are timed. The Keyframes Editor likewise lets you adjust the timing of elements you've added straight from inside Fusion.

### Adjusting Effect Timings

Every effect node turns up as a layer too, the same as clips do. You can resize an effect layer's In and Out points, and slide the whole layer forward or back in time, exactly as with a Loader or MediaIn layers. Trim an effect layer shorter than the composition's duration and the effect cuts in at whichever frame the layer starts, then cuts out following that layer's last frame, just like a clip on a timeline.

### Adjusting Keyframe Timings

Once you've animated an effect by laying keyframes onto a parameter in the Inspector, the Keyframes Editor becomes the place to edit the keyframe timing with ease. By default, every keyframe placed on parameters within a given node's layer is stacked together into a single flat track laid across the top of that layer. To get at the keyframes for editing, click the disclosure control sitting to the left of any animated layer's name over in the track header; that opens out a keyframe track for each keyframed parameter held by that layer.

### Keyframe tracks exposed

### Keyframe Editing Essentials

Here's a brief rundown of keyframe editing methods to get you going. Methods of adjusting keyframes:

- Clicking a lone keyframe selects it.
- Dragging a bounding box across a run of keyframes selects the whole bunch.
- Dragging keyframes to the left or right shifts where they fall in time.
- Right-click one or more selected keyframes and the drop-down menu's commands let you alter keyframe interpolation, copy and paste keyframes, or even spawn brand-new ones.
- Command-drag one or more selected keyframes and you'll drag a copy of them off to a different spot in the keyframe track.

To reposition a keyframe by way of the toolbar, take one of these steps:

- Pick a keyframe, then key a fresh frame number into the Time Edit box.
- Out of the Time Editor pop-up choose T Offset, then with one or more keyframes selected, supply a frame offset.
- Out of the Time Editor pop-up choose T Scale, then with one or more keyframes selected, supply a multiplier that's tacked onto the current playhead frame position. As an instance, with the playhead on frame 10 and the keyframe on frame 30, supplying the TScale value of 2 lands the keyframe on frame 50. Since the gap between the playhead and the original keyframe is 20, (20 x 2) = 40, which then gets added onto the playhead position.

### Time Stretching Keyframes

Select a span of keyframes within a keyframe track and you can switch on the Time Stretch tool, which brings up a box for squeezing and stretching the whole span of keyframes against one another. The Time Stretcher reshapes the overall timing across a run of keyframes while holding on to the relative timing from each keyframe to the next. As an alternative, you can switch on Time Stretch and draw a bounding box around whichever keyframes you want to adjust to set up a time-stretching boundary that way. Click the Time Stretch tool a second time to switch it off.

### Time stretching keyframes

### The Keyframe Spreadsheet

Switch on the Spreadsheet and then click a layer's name in the keyframe track, and for each keyframe its numeric time position together with its value—or values, where the parameter is multi-dimensional—turn up as entries within the Spreadsheet's cells. Each column stands for one keyframe, while each row stands for a single aspect of every keyframe.

### Editing keyframes in the Spreadsheet

As an example, when you're animating a motion path, the "Key Frame" row reports the frame each keyframe lands on, and the "Path1Displacement" row reports the position along the path at each keyframe. Alter the Key Frame value of any keyframe and you'll shift that keyframe to a new frame of the Timeline.

### Spline Editor

The Spline Editor lays out a finer-grained space for editing the timing, value, and interpolation of keyframes. By way of control points at each keyframe joined up by splines (also known as curves), you can shape how animated values shift over time. The Spline Editor breaks into four main areas: the Zoom and Framing controls up top, the Parameter list off to the left, the Graph Editor in the center, and the toolbar along the bottom.

The Spline Editor breaks down into Zoom controls along the top, a Parameter list on the left, the Graph Editor, plus the toolbar.
