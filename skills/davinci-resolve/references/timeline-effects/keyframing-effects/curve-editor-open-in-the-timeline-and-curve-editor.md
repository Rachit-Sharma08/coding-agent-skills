# Curve editor open in the timeline and curve editor

Version: DaVinci Resolve 20.3 Reference Manual. Context: Keyframing effects.
[Chapter index](INDEX.md) / [Previous section](keyframe-editor-and-timeline-tray.md) / [Next section](curve-editor-controls-and-view-shortcuts.md)
<a id="source-keyframing-effects-part-2"></a> <a id="source-the-curve-editor"></a> <a id="source-the-curve-editor-open-in-the-timeline"></a>

### The Curve Editor open in the timeline

Opening the Keyframe and Curve Editor in Its Own Window When your keyframing work in the Edit page is extensive (this is not offered in Cut), you can pop the Keyframe and Curve editor out into its own resizable window for more room to operate. To do that, click the Expand icon at the upper right of the Keyframe Editor.

You can expand the Keyframe and Curve Editor out into a resizable window all its own.

### The Curve Editor

When you need to handle keyframes in even finer detail, the Curve Editor is the tool. On a click, the the Curve Editor opens out to fit a large graph where you can freely tune both the timing and the value of selected keyframes, while also offering optional Bezier spline controls for building smooth curves to shape the acceleration of animated transitions from one value to another.

Here the Curve Editor displays the timing and values for the parameters you have selected. To open the Curve Editor: At the upper left of the Keyframe Editor, click the Curve icon. Once open, every track holding keyframes shows up as a colored line on the graph, with control points sitting along the line at each keyframe position. Hovering the pointer over a line brings up its track name (and its present value) in a pop up. The line’s color also mirrors the track color in the Keyframe Editor. You can reveal and hide several parameters in the Curve Editor through the Parameters menu, which lets you toggle which tracks appear via checkboxes. Along the bottom of the Curve Editor runs a keyframe track matching the Keyframe Editor that shows the keyframes for the chosen curve. You can only edit one curve at a time, but you choose which one is selected by clicking any dimmed curve in the Curve Editor. Through the control points each curve exposes, you can edit parameters, reposition keyframe timing, and reset each control point’s interpolation to craft custom easing effects that govern how the change speeds up as it travels between adjacent keyframes. Ways to add and select keyframes within the Curve Editor:

- To change which curve you’re editing: Click the Parameters menu and pick which curves to bring up for work. With several curves open at once in the Curve Editor, clicking any dimmed background curve brings it forward for editing.
- To add new keyframes to a curve: Option-click anywhere along a curve to drop a new control point. You can also choose the Add Keyframes icon at the top of the toolbar, which lets you add several keyframes to a curve just by clicking on it.
- To duplicate one or more keyframes: Build a selection of keyframes, then press Command-C to copy, slide the playhead to your paste point and press Command-V. This can be a handy way to swiftly loop a repeating animated effect you have built.
- To select a single keyframe: A single click on one control point selects it. That same action also works on the keyframe track running along the very bottom of the Curve Editor.
- To select multiple discontiguous keyframes: Command-click each control point you want, whether or not they sit beside one another. The same move works on the keyframe track running along the very bottom of the Curve Editor.
- To select multiple contiguous keyframes: Click the first keyframe you want, then shift-click the last keyframe you want, and every keyframe in between joins the selection too; or drag a bounding box inside the Curve Editor around several keyframes to grab them all together. The same move works on the keyframe track running along the very bottom of the Curve Editor.
- To select all keyframes: When the Keyframe Editor is open and has focus (from clicking somewhere inside it), pressing Command-A selects every keyframe within that Keyframe Editor.

Ways to tweak keyframes inside the Curve Editor:

- To drag one or more keyframes freely on a curve: Pick one or more control points, then pull them left or right to shift their timing and up or down to change their value. A small popup follows the move, reporting the track name alongside the new value.
- To restrict the drag of one or more curve keyframes to a single axis: Pick one or more control points, and while you drag — whether up-and-down or side-to-side — keep the Shift key held to lock the keyframe change to that one axis.

Ways to alter keyframe interpolation/easing/smoothing:

- To convert a Linear keyframe (or several) into Ease In or Ease Out: Eased keyframes give you animated transitions that ramp up slowly into full speed, or taper off bit by bit until they come to rest. This is only possible once you have two or more keyframes forming an animated effect. Pick one or more keyframes, then — based on which keyframe is being edited and the result you’re after — reach for Ease In, Ease Out, or Ease In and Out on the toolbar.
- To change one or more eased keyframes to Linear: Pick one or more keyframes, then reach for Linear on the toolbar.
- To change the interpolation of multiple keyframes: Grab several keyframes at once by Commandclicking or dragging a bounding box around them, then hit one of the four Bezier interpolation buttons on the Curve Editor title bar to retune every selected keyframe’s interpolation in a single step.
- To adjust a Bezier handle: Pull the Bezier handle whichever way you need to reshape the curve.

Ways to Cut, Copy, Paste, and Delete keyframes:

- To cut or copy, and paste one or more keyframes: Highlight the keyframes you want and reach for the Cut (Command-X) or Copy (Command-C) shortcuts. Next, park the playhead where the first pasted keyframe should land, and hit Paste (Command-V).
- To delete one or more keyframes from a curve: Highlight whichever keyframe(s) should go, then hit Delete.
