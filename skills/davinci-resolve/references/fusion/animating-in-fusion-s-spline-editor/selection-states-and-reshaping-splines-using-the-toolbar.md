# Selection states and reshaping splines using the toolbar

Version: DaVinci Resolve 20.3 Reference Manual. Context: Animating in Fusion s spline editor.
[Chapter index](INDEX.md) / [Previous section](time-and-value-editors-and-time-offset.md) / [Next section](spline-gradient-extrapolation.md)
<a id="source-a-looped-section-in-the-graph"></a> <a id="source-a-ping-pong-section-in-the-graph"></a> <a id="source-a-relative-loop-section-in-the-graph"></a> <a id="source-interpolation"></a> <a id="source-linear"></a> <a id="source-linear-interpolation-between-keyframes"></a> <a id="source-looping-backward"></a> <a id="source-looping-splines"></a> <a id="source-ping-pong"></a> <a id="source-relative-loop"></a> <a id="source-repeating-splines-x-number-of-times"></a> <a id="source-reshaping-splines-using-the-toolbar"></a> <a id="source-reversing-splines"></a> <a id="source-selection-states"></a> <a id="source-set-loop"></a> <a id="source-smooth-interpolation-between-keyframes"></a> <a id="source-step-instep-out"></a> <a id="source-the-reverse-button-in-the-toolbar"></a> <a id="source-the-various-loop-buttons-in-the-toolbar"></a>

### Selection States

There are three selection options here. Their labels — Select All Tools, then Deselect All Tools, plus Select One Tool — govern how the entries in the Spline Editor header act when you select a checkbox or label to switch a spline on. You’ll find these states in the Options menu at the upper-right corner of the Spline Editor. Select All Tools: Picking this option switches every spline on for editing. Deselect All Tools: Picking this one sets all spline checkboxes to disabled. As for Select One Tool, it works as a toggle. With Select One Tool picked from the menu, just one spline in the header stays active and visible at a time. Clicking any spline’s checkbox sets it active and clears all the others. While it’s off, several splines can be active in the header at once.

The Options menu selection states make selecting and deselecting all the header’s parameters simpler. Selection Groups: You can save the splines’ current selection state in the header, forming selection groups that reapply readily whenever you need them. To form a selection group, right-click over any header parameter or in a blank part of the graph and pick Save Current Selection from the contextual menu. A dialog opens for naming the new selection. To bring the selection group back, pick it by name from the Set Selection menu within that same contextual menu. Further context menu options let you rename or delete selection groups.

### Reshaping Splines Using the Toolbar

A spline’s shape can be reworked in several ways, which in turn changes the animation that spline produces. Beyond adjusting Bézier handles by hand, you can rapidly squish, stretch, loop, and reverse a spline. You can likewise switch the interpolation between keyframes from the default linear motion over to more natural smooth motion in a hurry. Every one of these options sits at the bottom of the Spline Editor in the toolbar. That toolbar breaks into separate groups: one sets interpolation, another reverses splines, another loops them, another handles time stretching, and a final one reshapes splines.

### Interpolation

Keyframes are particular frames in an animation at which control points hold exact values for a given parameter. Interpolation is the technique that fills in the unknown values lying between two keyframes. Fusion interpolates between two keyframes on its own. Still, you might want to adjust the interpolation to land a particular style of animation. The Spline Editor offers several interpolation methods you can pick from via the toolbar.

The toolbar’s interpolation buttons are these five: Smooth, Linear, Invert, Step In, and Step Out. Smooth: A smoothed segment eases how the curve enters and leaves the keyframe, achieved by gently lengthening the direction handles on the curve. The result slows the animation as it runs through the keyframe. To smooth whichever keyframe(s) you’ve selected, hit Shift-S, or else click that Smooth button on the toolbar.

### Smooth interpolation between keyframes

### Linear

A linear segment essentially follows the most direct path between two control points, namely a straight line. To set the selected keyframe(s) to linear, press Shift-L or click the Linear button in the toolbar.

### Linear interpolation between keyframes

TIP: Invert applies solely to non-animated LUT splines, which for now exist only inside the LUT Editor window.

### Step In/Step Out

Now and then you don’t want any interpolation at all between two keyframes. Instead, one keyframe’s value may stay put until a later keyframe changes it. In those situations, reach for the Step In or Step Out mode. Step In holds the previous keyframe’s value, then leaps directly to the next keyframe’s value.

Step In keeps a value steady until the comp reaches the next keyframe.

Step Out makes the selected keyframe’s value hold all the way up to the next keyframe.

Step Out jumps straight to the next keyframe value within a comp. You can apply Step In and Step Out modes to selected keyframes by clicking each mode’s toolbar button, or by right-clicking and picking the matching option from the contextual menu. The keyboard shortcuts I and O also serve to switch on Step In and Step Out for selected keyframes.

### Reversing Splines

Reverse flips the horizontal direction of a stretch of an animation spline. To run reverse, pick a cluster of points within a spline. Then take any one of these actions: click the Reverse button; right-click and choose Reverse off the contextual menu; or simply hit the V key. That cluster of points mirrors horizontally in the graph at once. Points neighboring the reversed selection can be affected too.

### The Reverse button in the toolbar

### Looping Splines

Repeating an animated section often comes in handy, whether endlessly or for a set number of passes, as you’d need to build a strobing light or a spinning wheel. Fusion supplies an assortment of ways to repeat a selected segment.

### The various Loop buttons in the toolbar

### Set Loop

To repeat or loop a chosen spline segment, first select the keyframes you mean to loop. Pick Set Loop from the contextual menu, or click the Set Loop button in the toolbar. The chosen part of the spline then repeats forward in time up to the end of the global range, or until a later keyframe caps the repeating segment.

### A looped section in the graph

Changing and Removing the Loop: You can alter the looped segment by tweaking any of the keyframes or control points that originally formed the loop. Just select one of the originating key points, apply whatever changes you need, and the looped segment refreshes. To drop the loop, select the keyframes you used to build it, then click the Loop button in the toolbar.

### Ping-Pong

The Ping-Pong Loop mode repeats the selected segment, flips each following loop around, and then keeps going. You can switch ping-pong looping on for the selected segments from the context menu or the toolbar.

### A ping-pong section in the graph

### Relative Loop

The Relative Loop mode repeats the segment much as the Loop does, except every repetition builds onto the final point of the prior loop, so the values climb steadily as time passes.

### A Relative Loop section in the graph

### Looping Backward

You reach Set Pre-Loop by right-clicking in the graph area and picking it from the contextual menu. This option holds the same looping choices as the Loop option buttons in the toolbar, the difference being that the selected segment repeats backward in time instead of forward.

### Repeating Splines X Number of Times

You can copy splines and repeat them a fixed number of times by right-clicking in the graph area and picking Duplicate from the contextual menu. Duplicated splines resemble looped splines, except the selected segment runs through only as many repeats as you specify, and every repeat is itself a copy rather than an instance. Changes you make to the original segment leave the shape of its repetitions untouched. You reach the Duplicate modes solely through the Duplicate contextual menu, which opens a submenu listing all the looping modes covered above. Picking any of these modes brings up a dialog where you type the number of repetitions.
