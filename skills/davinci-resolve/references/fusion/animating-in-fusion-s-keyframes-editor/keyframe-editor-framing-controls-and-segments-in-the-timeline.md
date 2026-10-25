# Keyframe editor framing controls and segments in the timeline

Version: DaVinci Resolve 20.3 Reference Manual. Context: Animating in Fusion s keyframes editor.
[Chapter index](INDEX.md) / [Previous section](fusion-keyframes-editor-and-inspector-animation.md) / [Next section](keyframe-spreadsheet-and-editing-keyframes-in-the-spreadsheet.md)
<a id="source-drag-and-drop-keyframe-editing"></a> <a id="source-holding-the-first-or-last-frame"></a> <a id="source-keyframe-editing-using-the-time-editor"></a> <a id="source-moving-segments-in-the-timeline"></a> <a id="source-the-keyframe-editor-framing-controls"></a> <a id="source-the-move-cursor"></a> <a id="source-the-trim-cursor"></a> <a id="source-trimming-segments"></a> <a id="source-working-with-keyframes-in-the-timeline"></a> <a id="source-working-with-segments-in-the-timeline"></a>

### The Keyframe Editor framing controls

A Horizontal zoom control lets you resize the editor. A Zoom to Fit button sizes the width of every track to match the Keyframes Editor’s current width. A Zoom to Rect tool lets you sketch a rectangle that marks out which region of the Keyframes Editor to magnify. Ordering or filtering the tracks in assorted ways is the job of a Sort pop-up menu. An Option menu opens the door to many further ways of filtering tracks and steering which options are visible.

### Working with Segments in the Timeline

The lion’s share of Timeline work comes down to trimming and lining up clip segments. Picking a single segment in the Timeline can be done in either of these ways:

- Click the node’s name in the header.
- Click the node’s segment in the Timeline.

To add another segment to the selection, do one of the following:

- Hold Command and click further segments to build discontiguous selections.
- Pick a segment, then hold Shift and click a second segment to make a contiguous selection spanning everything between.

To remove a segment from the selection, do the following:

- Hold Command and click a selected segment to drop it from the selection.

TIP: Picking a node’s name from the Timeline header likewise selects that node’s tile in the Node Editor, with its controls shown in the Inspector.

### Moving Segments in the Timeline

To reposition a segment, drag on the node’s segment within the Keyframes Editor. The cursor takes on the look of a bar with arrows pointing both ways. Moving a segment shifts where that clip starts and stops in the composition.

### The Move cursor

### Trimming Segments

Trimming segments plays out differently on Loaders, MediaIn and Effect nodes:

- Trimming a Loader or MediaIn node parallels trimming clips in an editing application, since you are reshaping the in and out points of the media range that clip lends to your composition.
- Trimming an effect node’s segments instead reshapes how far that node’s effect reaches in the composition. Beyond the trimmed region, that effect node acts as though it were switched off.

TIP: Cutting back how long effects nodes run can streamline processing. Picture a Loader or MediaIn node standing for a clip that runs 100 frames long and feeds a Defocus node animated across frames 80–100. There is barely any payoff in processing the defocus node across frames 0–79, so trimming the defocus segment so that it opens at frame 80 in the Timeline effectively keeps it from rendering and eating either memory or processor time until it is actually needed.

To trim a segment in the Timeline, do the following:

- Drag on either end of the node’s segment in the Timeline. Once the cursor reaches the right spot to trim, it becomes a vertical bar carrying a single arrow.

### The Trim cursor

### Holding the First or Last Frame

To freeze a clip on a Loader’s opening or closing frame for a chosen number of frames — what is called a freeze frame — hold Command while dragging past the segment’s first or last edge in the Timeline.

### Working with Keyframes in the Timeline

There are two ways keyframes get drawn. With keyframe tracks closed, they appear over the node’s segment. Clicking the disclosure icon left of the node’s name in the track header opens the display so each keyframed parameter gets a track of its own in the Timeline, making precise editing possible. Beyond that, each keyframe track — open or closed — carries a miniature curve overlay that visually conveys how the keyframed values rise and fall. You cannot edit this little overlay directly.

Here the Drip1 segment shows its keyframe tracks opened out, whereas the Text1 segment keeps its keyframe tracks folded down so that they sit inside the segment.

### Drag and Drop Keyframe Editing

Below are pointer-driven keyframe editing approaches to get you going. Ways to select keyframes:

- Click a single keyframe to select it.
- Drag a bounding box across a string of keyframes to grab them all.
- Command-click to pick out discontiguous keyframes.
- Shift-click the first and last keyframe of a range to capture a contiguous range.

Ways to adjust keyframes:

- Keyframes can be dragged left and right to shift them in time.
- Right-click one or more selected keyframes and lean on contextual menu commands to alter keyframe interpolation, copy/paste keyframes, or even spawn new keyframes.

### Keyframe Editing Using the Time Editor

Down at the lower right of the Keyframes Editor, a drop-down paired with an editing field lets you numerically edit any selected keyframe’s timing, in frames, making precise tweaks simple. Shifting a keyframe’s position by way of the toolbar can be done in any of these ways:

- Pick a keyframe, then type a fresh frame number into the Time Edit box.
- From the Time Editor drop-down pick T Offset, select one or more keyframes, then type a frame offset.
- From the Time Editor drop-down pick T Scale, select one or more keyframes, then type a frame offset.

For relocating keyframes, the Time button can be flipped over to Time Offset or Time Scale.
