# Selecting a node to edit and inserting keyframes

Version: DaVinci Resolve 20.3 Reference Manual. Context: Animating in Fusion s keyframes editor.
[Chapter index](INDEX.md) / [Previous section](spreadsheet-editor.md)
<a id="source-customizing-the-keyframes-editor"></a> <a id="source-display-point-values"></a> <a id="source-displaying-audio-waveforms"></a> <a id="source-inserting-keyframes"></a> <a id="source-line-size"></a> <a id="source-selecting-a-node-to-edit"></a> <a id="source-selecting-multiple-nodes-to-edit"></a> <a id="source-the-options-submenu-for-changing-display-point-values"></a>

### Selecting a Node to Edit

If you want a node’s timing shown in the Spreadsheet, click that node’s name within the Keyframes Editor header; its Start and End points then show up on the keyframe’s row in the Spreadsheet. Similarly, to work on an animation parameter inside the Spreadsheet Editor, pick the parameter from the Keyframes Editor header. Each frame number that holds a keyframe gets its own box along the keyframe row, and the keyframe’s value sits in the cell directly beneath that frame number. By clicking a cell you can reassign which frame the keyframe lands on, or alter the parameter’s value at that keyframe.

Clicking a parameter’s keyframe value lets you edit it. TIP: Typing a frame number with a decimal (for instance 10.25 or 15.75) places keyframes at a subframe level, which helps produce smoother, more natural animation.

### Inserting Keyframes

Adding fresh keyframes to an animation is also possible: click inside a blank keyframe cell and type the time you want for it. Then, in the cell beneath that new keyframe, supply the parameter’s value.

### Selecting Multiple Nodes to Edit

The Spreadsheet lets you work on several splines and nodes at once. Normally, picking a different parameter from the Timeline header swaps out whatever parameter and keyframes the Spreadsheet Editor is currently showing. To instead append more, hold Command while clicking extra parameters on other nodes, and they join what’s already in the Spreadsheet.

### Customizing the Keyframes Editor

Several adjustments let you tailor how the Keyframes Editor looks to suit your workflow. Each of them lives in the contextual menu that pops up when you right-click anywhere inside the Keyframes Editor.

### Line Size

Use the Line Size option to govern how tall each Timeline segment is on its own. Making a Timeline bar taller is frequently handy, particularly while you edit or shape intricate splines. You can grow or shrink a segment’s height in two ways. For a single segment, right-click anywhere inside the Keyframes Editor and select a size from the Line Size submenu; the choices are Minimum, Small, Medium, Large, and Huge. To resize every segment at once, right-click anywhere inside the Keyframes Editor and pick a size from the All Line Size submenu, where the choices are again Minimum, Small, Medium, Large, and Huge.

### Display Point Values

Some people find keyframes easier to grab when they appear as control points rather than upright bars, which is the more conventional representation. To switch their look, open the Timeline contextual menu by right-clicking anywhere inside the Keyframes Editor and select Options > Display Point Values.

### The Options submenu for changing Display Point Values

A side-by-side look at the two choices follows.

On the left, keyframes shown as bars; on the right, the same keyframes shown as Point Values.

### Displaying Audio Waveforms

The Keyframes Editor can show the audio waveform belonging to a MediaIn node, giving you a visual reference while you place and reposition keyframes.

Within the Keyframes Editor, waveforms appear for every MediaIn node

Showing a clip’s waveform: 1 Launch the Keyframes Editor. 2 Click the disclosure arrow beside the MediaIn node so that clip’s waveform becomes visible. Resizing a waveform’s drawn height: 1 Bring up the Keyframes Editor. 2 Within it, select the audio track whose waveform needs adjusting. 3 Over the audio waveform, right-click and pick Line Size > Minimum/Small/Medium/Large/Huge. 4 Working in Fusion Studio instead, you make the audio waveforms appear once the Saver node is displayed. Revealing the Audio Waveform under Fusion Studio: 1 Start the Keyframes Editor. 2 Expand the Saver track until its audio waveform shows. To home in on the exact spot of an audio beat, transient, or cue, drag gently across the waveform so it plays back. Need crisper detail in the rendering? Just make it bigger. Resizing a waveform’s drawn height once more: 1 Reopen the Keyframes Editor. 2 With the cursor over the audio waveform, right-click and select Line Size > Minimum/Small/Medium/Large/Huge. TIP: Right-clicking any track here and then choosing All Line Size > Minimum/Small/Medium/Large/Huge rescales every track plus its audio waveforms throughout the Keyframes Editor.
