# Animating in fusions keyframes editor and keyframing in the inspector

Version: DaVinci Resolve 20.3 Reference Manual. Context: Animating in Fusion s keyframes editor.
[Chapter index](INDEX.md) / [Next section](keyframe-editor-framing-controls-and-segments-in-the-timeline.md)
<a id="source-animating-in-fusion-s-keyframes-editor-part-1"></a> <a id="source-animating-in-fusions-keyframes-editor"></a> <a id="source-attaching-a-parameter-to-an-existing-animation-curve"></a> <a id="source-collapseopen-all"></a> <a id="source-editing-keyframes-in-the-spreadsheet"></a> <a id="source-keyframes-editor-overview"></a> <a id="source-keyframes-editor-tracks"></a> <a id="source-keyframing-in-the-inspector"></a> <a id="source-removing-animation-in-the-inspector"></a> <a id="source-scaling-and-panning-the-timeline"></a> <a id="source-spreadsheet"></a> <a id="source-the-keyframes-editor"></a> <a id="source-the-playhead"></a> <a id="source-the-timeline-header"></a> <a id="source-the-timeline-header-area"></a> <a id="source-the-timeline-tracks"></a>

### Animating in Fusion’s Keyframes Editor

The focus of this chapter is keyframing effects from within Fusion’s Inspector, plus editing clips, effects, and keyframes inside the Keyframes Editor.

### Keyframing in the Inspector

Across most effects nodes, the bulk of parameters accept keyframes, letting you build animated effects — animated transforms, rotoscoping by way of splines, warping behaviors that shift on the fly, and beyond; there is no end to the possibilities. As a convenience, a cluster of keyframing controls sits in the Inspector beside every keyframable parameter. Those controls are:

- A gray Keyframe button to the right each keyframable parameter. A click on this gray button drops a keyframe at wherever the playhead currently rests and flips the button to orange.
- Any time the playhead lands squarely on a keyframe, this button shows orange. A click on an orange Keyframe button strips out the keyframe at that frame and returns the button to gray.
- Small navigation arrows show up on the right and left when more keyframes lie in those directions. A click on the navigation arrows flanking the keyframes sends the playhead over to them.

In the Inspector, orange Keyframe buttons signal that a keyframe exists at that very frame After you have keyframed one or more parameters, provided Show Modes/Options is switched on, the node holding the parameters you keyframed shows a Keyframe badge to signal that the node carries animation. After you begin keyframing node parameters, their timing becomes editable in the Keyframes Editor and/or Spline Editor.

A keyframed node displays a Keyframe badge in the Node Editor

### Removing Animation in the Inspector

To strip a keyframed spline off a parameter: 1 On the parameter whose animation you wish to drop, right-click its keyframe control. 2 From the contextual menu, pick Remove [Name of parameter].

### Attaching a Parameter to an Existing Animation Curve

You can tie several parameters to one shared animation curve. That can be a priceless time-saver when you are animating different parameters in a node identically. To wire a second parameter onto that same animation curve: 1 Give the second parameter you mean to attach a right-click. 2 Within the contextual menu, hover over the Connect To submenu. 3 Out of the Connect To submenu, pick the animated parameter by name.

### Keyframes Editor Overview

At its core the Keyframes Editor is a timeline-style view of your composition, where every clip and effect node in that composition shows up as a track. The color coding on these tracks matches the nodes they stand for, and they carry labels where it makes sense. Across the top a Time Ruler conveys your composition’s timing, while a range of controls let you govern what the Keyframes Editor holds. There are two jobs the Keyframes Editor handles:

- To set the timing of a project’s elements, be they clips or effects. You can trim, slide, and stretch clips, set the timing of an animation spline, or trim how long an effects node runs. The order of nodes in the Timeline is yours to reshuffle freely without disturbing your composition’s layering order. Every compositing operation lives in the Node Editor, whereas the Keyframes Editor looks after your composition’s timing.
- To build and/or revise keyframes you have applied to effects in a track-based fashion, you can retime keyframes, add and remove keyframes, and even change keyframe values

### The Keyframes Editor

To show the Keyframes Editor, do one of the following:

- Click the Keyframes Editor button in the UI toolbar to flip the Keyframes Editor’s visibility on or off.
- Press F7 on the keyboard.

### Keyframes Editor Tracks

Although a track stands in for every clip and effect node in your composition, keyframed parameters surface in one of two ways — either as keyframes laid over the track they belong to (as you see on the MOVEMENT track), or split out onto tracks of their own for finer editing, one keyframe track for each keyframed parameter, by clicking a disclosure control left of that track’s name in the Timeline header (as you see beneath the “Drip1” track).

### The Timeline tracks

### The Timeline Header

Sitting on the Timeline’s left side, the Timeline header area is a hierarchical roster of every track in a composition. Each track shows the name of the node it belongs to, a lock button, and a disclosure control that reveals keyframe tracks for each keyframe animation, modifier, and mask attached to it.

### Collapse/Open All

One fast route to opening or closing every available keyframe track in one go is the Expand/Collapse Tool Controls commands found in the Keyframe Timeline Option menu.

### The Timeline header area

### The Playhead

Just as it does throughout Fusion, the playhead shows up as a red vertical bar cutting across the Timeline view to mark where the current frame or time sits. Because the Keyframes Editor playhead is tied to the viewer playhead, the image in front of you stays in sync.

The playhead about to be dragged by the pointer

Dragging the playhead requires clicking it directly, the Timeline ruler included (click and drag anywhere else on the Timeline ruler and you scale the Timeline instead). On top of that, you can send the playhead straight to a new spot by holding the Command-Option keys while clicking in the track area (not the Timeline ruler).

### Spreadsheet

Switch on the Spreadsheet, then click a layer’s name in the keyframe track, and each keyframe’s numeric time position and value (or values, for a multi-dimensional parameter) turn up as entries within the Spreadsheet cells. One keyframe occupies each column, while one facet of each keyframe occupies each row. As an example, while you animate a blur, the Key Frame row reports the frame on which each keyframe sits, and the Blur1BlurSize row reports the blur size at each keyframe. Alter the Key Frame value of any keyframe and you shift that keyframe onto a different frame of the Timeline.

### Editing keyframes in the Spreadsheet

### Scaling and Panning the Timeline

Across the top, a row of zoom and framing controls lets you reshape the work area that holds the layers.
