# Frame average and keyframe stretcher and run command

Version: DaVinci Resolve 20.3 Reference Manual. Context: Frame average, Keyframe stretcher, Run command.
[Chapter index](INDEX.md) / [Previous section](fields-and-frame-average.md) / [Next section](run-command-and-set-domain-and-switch.md) / [Frame Average Avg](fields-and-frame-average.md)
<a id="source-basic-node-setup-2"></a> <a id="source-basic-node-setup-3"></a> <a id="source-controls-tab-1"></a> <a id="source-inputs-2"></a> <a id="source-inputs-3"></a> <a id="source-inspector-1"></a> <a id="source-keyframe-stretcher-kfs"></a> <a id="source-keyframe-stretcher-node-introduction"></a> <a id="source-keyframes-tab"></a> <a id="source-original-50-frame-animation"></a> <a id="source-run-command-node-introduction"></a> <a id="source-run-command-run"></a> <a id="source-the-frame-average-controls-tab"></a> <a id="source-the-keyframe-stretcher-keyframes-tab"></a> <a id="source-the-keyframe-stretcher-node"></a> <a id="source-the-run-command-node"></a>

### Inspector

### The Frame Average Controls tab

### Controls Tab

Within the Controls tab live the parameters that govern the span and direction of the averaged frames. Sample Direction The Sample Direction menu decides whether the averaged frames come from before the current frame, after it, or some blend of both.

- Forward: Averages however many frames the Frames slider specifies following the current frame.
- Both: Averages however many frames the Frames slider specifies, drawing frames from both before and after the

current frame.

- Backward: Averages however many frames the Frames slider specifies preceding the current frame. Missing Frames This control sets what happens when a frame is absent from the clip.
- Duplicate Original: Holds on the last original frame until the next frame becomes available.
- Blank Frame: Leaves any missing frames empty. Frames This slider sets how many frames get averaged.

### Keyframe Stretcher [KFS]

### The Keyframe Stretcher node

### Keyframe Stretcher Node Introduction

You place the Keyframe Stretcher node downstream of animated nodes, so that as the comp’s duration changes the keyframes stretch along with it. Its job is to rescale the keyframes on the animation curve to the clip’s current duration. This proves especially valuable when you’re building title templates in Fusion meant for use on DaVinci Resolve’s Edit or Cut page.

TIP: To target just one parameter with the Keyframe Stretcher, apply the Keystretcher modifier.

### Inputs

The lone input on the Keyframe Stretcher node is where you connect a 2D image carrying keyframe animation. Input: The orange input accepts any node bearing keyframed animation. That input might be a Merge node that itself isn’t animated yet holds animated foreground and background nodes.

### Basic Node Setup

Place the Keyframe Stretcher right ahead of the Media Out or Saver node. Every node holding animation upstream of the Keyframe Stretcher gets reshaped whenever the comp’s duration shifts. A Keyframe Stretcher altering the animation across two text nodes. In the diagram below, a 50-frame original animation has been applied to a parameter. You’d set the Keyframe Stretcher Start and End to 0 and 50. Frame 10 holds the second keyframe, and frame 40 holds the third. Putting the Stretch Start at frame 11 and the Stretch End at frame 39 preserves the existing keyframes at their original speed (number of frames.) Everything in the middle then gets stretched.

### Original 50-frame animation

For the example below, the clip’s duration grows to 75 frames. The animation’s opening 10 frames and closing 10 frames keep the same speed as the original, whereas whatever sits in the middle is stretched to take up the extra length. NOTE: Within the Spline Editor itself, only the keyframe positions from the original are displayed. The Keyframe Stretcher leaves the splines untouched; what it alters is purely the animation.

Animation reworked to 75 frames yet only its middle portion stretched Inspector

### The Keyframe Stretcher Keyframes tab

### Keyframes Tab

The Keyframes tab carries Source controls that establish the source duration plus Stretch controls that pin down which region of the animation gets reshaped. Source Start/Source End You define a source range through the Source Start and Source End controls. As a rule these are dialed in to span the entire animation spline on the Keyframes control. Stretch Start/Stretch End With the Stretch Start and Stretch End controls you mark off a central band in which keyframes get stretched or compressed. Handles lying beyond that range escape scaling. Whatever keyframes fall outside the Stretch Start and End range hold a constant frame distance from the Start and End. Any tweak you make to a keyframe on the original control is scaled back onto the source curve accordingly, and it lines up with the original timing just as you’d expect. Stretch Edges Instead Ticking the Stretch Edges Instead checkbox supersedes the Stretch Start and Stretch End controls and instead stretches the animation’s edges.

### Run Command [Run]

### The Run Command node

### Run Command Node Introduction

The Run Command node fires off an external command or batch file at chosen moments throughout a render. A command can be set to run when a render begins or when it ends. Alternatively, you can have it fire once per frame. Among its many uses, the Run Command can net render other command line applications by way of the Fusion Render Manager.

### Inputs

The sole input on the Run Command node simply passes a 2D image through. Input: The optional orange image input isn’t needed for the node to function. That said, when it’s wired to a node‘s output, the Run Command holds off until that connected node finishes rendering before it launches. This often helps when it’s tied to a Saver, guaranteeing the output frame is fully written to disk beforehand. Should the launched application come back with a non-zero result, the node fails too.

### Basic Node Setup

You can wire the Run Command node downstream of a Saver and have it fire as soon as the last frame is done.

Run Command positioned downstream of a Saver node.
