# Bands 2 through 5 and effects

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the inspector in the cut page.
[Chapter index](INDEX.md) / [Previous section](equalizer-and-clip-eq-in-the-audio-inspector.md) / [Next section](file-and-file-inspector-controls.md)
<a id="source-bands-2-through-5"></a> <a id="source-effects"></a> <a id="source-image"></a> <a id="source-the-effects-inspector-controls"></a> <a id="source-the-image-inspector-controls-for-braw-footage"></a> <a id="source-the-transition-inspector-controls"></a> <a id="source-transition"></a>

### Bands 2 through 5

A broad assortment of equalization adjustments is available through these band controls.

- Band enable button: Turns each band of EQ on and off.
- Band filter type: Four filtering options come with these Bands (running top to bottom): Lo-Shelf, Bell, Notch,

and Hi-Shelf.

- Frequency: Sets where the EQ adjustment's center frequency sits.
- Gain: Governs how strongly the affected frequencies get hit. Negative values

trim those frequencies down, whereas positive values lift those frequencies up.

- Q Factor: Surfacing once the Bell setting is chosen, this parameter sets the width of

affected frequencies. Lower values pull in a wider range of frequencies; higher values tighten the range of frequencies.

NOTE: The Audio FX library holds many more refined plugins and effects for audio clips. Apply any of those and their controls show up in the Inspector's Effects tab Audio section rather than here.

### Effects

### The Effects Inspector controls

Whatever Fusion FX, Open FX, or Audio FX filters have been laid over a clip can be tweaked here within their respective tabs. Which controls the Effects panel exposes varies from one Timeline effect to the next. Whatever panels show, the parameters inside each panel get grouped, a title bar carries that group's name plus other controls that let you act on every parameter inside the group together. These controls include:

- Enable button: To the left of the parameter group's name, a toggle control lets you disable and re-enable every parameter inside that group at once. Orange marks that track as enabled. Gray marks it disabled.
- Parameter group title bar: Double-click any parameter group's title bar to collapse or open it. More exciting still, Option-double-clicking one parameter group's title bar collapses or opens every parameter group at once.
- Keyframe and Next/Previous Keyframe buttons: This button lets you drop or pull keyframes at the playhead's position on or from each individual parameter inside the group. Where the button glows orange, a keyframe sits at the playhead's current position. Where it is dark gray, no keyframe is present. The left and right arrow buttons jump the playhead from keyframe to keyframe for further tweaking.
- Reset button: Sends every parameter inside that group back to its default setting.
- Use Alpha: Ticking this box lays the Open FX alpha channel over the selected clip,

compositing it atop any background elements showing in lower tracks. Where more than one alphamodifying effect lands on a single clip, the alpha channels blend together. For a full rundown of every Resolve FX plugin shipping with DaVinci Resolve, turn to Part 12, "Resolve FX Overview."

### Transition

### The Transition Inspector controls

Double-clicking a transition in the Timeline opens that Transition Panel inside the Inspector. Each transition carries the following editable properties.

- Transition Type: Whichever transition is currently selected. Swap to any other installed transition by picking one from the drop-down menu.
- Duration: How long the transition runs, given in both seconds and frames.
- Alignment: A drop-down letting you set where the transition sits relative to the edit point it is

applied to. Your options are "Start on Edit," "Center on Edit," and "End on Edit." Further properties tied to each particular transition type turn up in another group below. Because the Cross Dissolve transition is the one used most, its properties stand in as the example.

- Style: The various Dissolve transitions (Cross Dissolve, Additive Dissolve, and so on) surface this drop-down, which lets you pick different ways the outgoing clip blends into the incoming clip during the dissolve. Six options are on offer:

Video: A plain linear dissolve, where the outgoing clip fades out while the incoming clip fades in. Film: A logarithmic dissolve that mimics the film dissolves an optical printer would make. Additive: Here the outgoing and incoming clips cross fade through the Additive composite mode, so the transition appears to brighten at its midpoint. Subtractive: Here the outgoing and incoming clips cross fade through the Subtractive composite mode, so the transition appears to darken at its midpoint. Highlights: Here the outgoing and incoming clips cross fade through the Lighten composite mode, which plays up each clip's lightest areas as the transition runs. Shadows: Here the outgoing and incoming clips cross fade through the Darken composite mode, which plays up each clip's darkest areas as the transition runs.

- Start Ratio: Sets how complete the transition is at its first frame, on a 0 to 100 percent scale. Pushing the Start Ratio past 0 makes the transition show up already at a more fully cross-dissolved state right from that first frame.
- End Ratio: Sets how complete the transition is at its last frame. Pushing the End Ratio past 0 leaves the transition never fully dissolving through to the incoming shot at its last frame.
- Reverse: Reverses the transition. This parameter is disabled for Dissolve transitions.
- Ease: A drop-down letting you apply nonlinear acceleration to a transition's start, end, or whole

duration. The upshot is added inertia in the move from the outgoing clip to the incoming clip, giving a softer change into and out of the transition for each clip. None: In a linear way, the outgoing clip fades through to the next shot. In: The outgoing clip holds on, since the transition's opening dissolves at a slower pace than its close. Out: The outgoing clip drops away sooner, since the transition's opening dissolves at a quicker pace than its close. In & Out: At both the dissolve's opening and close, the outgoing and incoming clips alike ease off, which leaves the transition's dead center faster by comparison. Custom: Lets you reshape the fade's parameters by hand through the Transition Curves below.

- Transition Curve: Lets you place keyframes by hand that steer how the transition advances across its duration.

Transitions of other kinds show properties peculiar to that transition's own effect. CUT For a full rundown of every transition shipping with DaVinci Resolve, turn to Chapter 48, "Using Transitions."

### Image

### The Image Inspector controls for BRAW footage

Within the Image panel sit groups of parameters matching every camera raw media format DaVinci Resolve supports. By working these Image panel parameters, you can override the original camera metadata captured at the moment of recording and apply simultaneous adjustments to camera raw media across your whole project. For a full rundown of every RAW camera parameter that DaVinci Resolve supports, turn to Chapter 7, "Camera Raw Settings."
