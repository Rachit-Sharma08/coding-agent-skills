# Selecting moving and deleting keyframes and moving keyframes

Version: DaVinci Resolve 20.3 Reference Manual. Context: Animating in Fusion s spline editor.
[Chapter index](INDEX.md) / [Previous section](displaying-marker-with-the-timeline-and-autosnap.md) / [Next section](copying-and-pasting-keyframes.md)
<a id="source-moving-keyframes"></a> <a id="source-selecting-moving-and-deleting-keyframes"></a> <a id="source-showing-key-markers"></a>

### Selecting, Moving, and Deleting Keyframes

Where you put keyframes does much to shape the style of the animation. Through the graph, you can pick keyframes and shift them up or down to alter their value, or left and right to alter the timing. Keyframes copy and paste across splines and parameters. Ways to select keyframes:

- Click a keyframe right where it sits on the spline, or rope it inside a dragged bounding box.
- Drag a bounding box wide enough to take in several keyframes to grab more than one at a time.
- To toss a keyframe into or out of the current selection, hold the Command key as you select keyframes. That drops the keyframes already selected and picks up the ones not yet selected.
- Press Command-A, or right-click in the graph area and pick Select Points > Select All from the contextual menu, to grab every keyframe across the active splines.

### Moving Keyframes

Keyframes move freely under the mouse, the keyboard, or the edit point controls. They can even slide past existing points while you move them. Say keyframes sit on frame 5 and frame 10, with the one at frame 5 then carried out to frame 15. To move keyframes with the mouse:

- Drag the selected keyframe to its new place in the graph. With more than one keyframe selected, all of them travel together.
- Hold the Option key before you start dragging the keyframe to pin its motion to a single axis.

To move keyframes with the keyboard:

- The Up and Down Arrow keys nudge the keyframes’ value a little at a time.
- How far each key press shifts the value vertically follows the graph’s current scale. The tighter your zoom on the spline, the finer the adjustment.
- Hold the Shift key as you press the Up or Down Arrow keys to step the value in bigger jumps.

To move keyframes via edit fields:

- The Value and Time Editors live at the far right of the toolbar. Into these number fields you can type exact values for the selected keyframes. These controls get a fuller treatment further on in this chapter.

To delete one or more keyframes:

- With one or more keyframes selected, hit Delete or Backspace on the keyboard. That clears only the keyframes; the spline stays, even once it holds no keyframes. To get rid of the spline, right-click the parameter in the Inspector and pick Remove [parameter name].

### Showing Key Markers

By turning to the key markers, you can retime the keyframes without bothering to handle splines at all. The horizontal time axis is able to display markers pointing out where each keyframe sits. To switch these markers on, right-click in the graph and pick Show > Key Markers from the contextual menu, or click the Show Key Markers button on the toolbar.

In the horizontal axis, the key markers depict keyframes in the same color the splines wear
