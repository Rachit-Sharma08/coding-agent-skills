# Gradient extrapolation and gradient extrapolation applied to the spline

Version: DaVinci Resolve 20.3 Reference Manual. Context: Animating in Fusion s spline editor.
[Chapter index](INDEX.md) / [Previous section](selection-states-and-reshaping-splines-using-the-toolbar.md) / [Next section](ease-in-out.md)
<a id="source-gradient-extrapolation"></a> <a id="source-shape-box"></a> <a id="source-the-gradient-extrapolation-applied-to-the-spline"></a> <a id="source-the-shape-box-button-in-the-toolbar"></a> <a id="source-the-shape-box-in-the-graph"></a> <a id="source-the-time-stretch-bars-in-the-graph"></a> <a id="source-the-time-stretch-button-in-the-toolbar"></a> <a id="source-time-stretching"></a>

### Gradient Extrapolation

You reach Gradient Extrapolation by right-clicking in the graph area and picking it from the contextual menu. This option carries on the path traced by the last two keyframes.

### The Gradient Extrapolation applied to the spline

### Time Stretching

Time Stretching lets a selected batch of keyframes be stretched or squashed proportionally. This gives you a way to change the animation’s duration while holding the relative spacing between each keyframe. To switch spline stretching on, select the batch of keyframes you want to time stretch; from there, either pick Modes > Time Stretching out of the graph’s contextual menu, or just click the Time Stretch button sitting in the toolbar.

### The Time Stretch button in the toolbar

With more than one keyframe selected on the spline, switching Time Stretch on wraps the outer keyframes in two vertical white bars. Pull on those white vertical bars to lengthen or compress the timing of whatever spline segments fall between them. Slide these bars back and forth to stretch or squash the spline segment.

### The Time Stretch bars in the graph

TIP: With no keyframes selected as you switch Time Stretch on, drag out a rectangle to mark the boundaries of the Time Stretch. To turn the Time Stretching mode off:

- Click the Time Stretch button in the toolbar once more, or pick Modes > Time Stretching again from the contextual menu.

### Shape Box

The Shape Box transform mode resembles Time Stretching, but it can scale keyframe values vertically on top of adjusting time. To switch the Shape Box on, do one of these:

- Select a batch of keyframes, then pick Modes > Shape Box from the contextual menu.
- Select a batch of keyframes, then click the Shape Box button in the toolbar.
- Select a batch of keyframes, then press Shift-B to switch the Shape Box mode on or off.

### The Shape Box button in the toolbar

A white rectangle frames the selected points once the mode is on. To scale, skew, or stretch the spline, drag any of the control points sitting around the box. To shift all the keyframes, drag the box edges.

### The Shape Box in the graph

TIP: When no points are selected, or whenever you’d like to grab a fresh batch of keyframes, you can drag out a new rectangle at any moment.
