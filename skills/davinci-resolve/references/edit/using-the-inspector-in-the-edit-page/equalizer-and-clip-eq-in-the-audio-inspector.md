# Equalizer and clip eq in the audio inspector

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the inspector in the edit page.
[Chapter index](INDEX.md) / [Previous section](audio.md) / [Next section](transition-and-transition-inspector-controls.md)
<a id="source-bands-1-and-6"></a> <a id="source-bands-2-through-5"></a> <a id="source-clip-eq-in-the-audio-inspector"></a> <a id="source-effects"></a> <a id="source-equalizer"></a> <a id="source-the-clip-eq-graph-with-user-draggable-handles"></a> <a id="source-the-effects-inspector-controls"></a>

### Equalizer

Carrying both graphical and numeric controls, this six-band parametric equalizer boosts or cuts assorted frequency ranges within that clip before the signal even reaches the EQ built into the Mixer. Every band hands you its own controls — the filter type (Bell, Lo-Shelf, Hi-Shelf, Notch), then Frequency, then Gain, and a Q-factor (sharpness of the band) — while which controls a given EQ band reveals depends on the filter type. TIP: Clip EQ settings copy and paste across, whether between two Clip EQ instances or from a Clip EQ over to a Track EQ.

### Clip EQ in the Audio Inspector

Master EQ Controls Up in the Equalizer window's upper‑right and left corners sit these overall controls:

- Enable button: Switches the whole EQ effect on or off, leaving the controls unreset.
- Reset button: Returns every control of the EQ window to its default.

Clip EQ Graph What this graph plots is the current EQ curve, its handles matching each enabled EQ band listed below. Drag any numbered handle to boost or cut the band of frequencies that handle governs, in whatever equalization type that band carries.

### The Clip EQ graph with user-draggable handles

As you drag a numbered handle on this graph, the matching band's parameters shift in turn, and adjusting any band's parameters reshapes the EQ graph too — which doubles as a visual readout of the equalization being laid over that track.

### Bands 1 and 6

The two outer sets of band controls let you carry out high-pass and low-pass adjustments where needed.

- Band enable button: Turns each band of EQ on and off.
- Band filter type: Across five specific filtering options, Bands 1 and 6 can be switched to process the signal's lowest or highest frequencies. Over on Band 1, the lineup (top to bottom) runs: Lo-Shelf, Bell, Notch, Hi-Shelf, and Hi-Pass. Over on Band 6, the lineup (top to bottom) runs: Lo-Pass, Lo-Shelf, Bell, Notch, and Hi-Shelf.
- Freq: Sets where the EQ adjustment's center frequency sits.
- Gain: Governs how strongly the affected frequencies get hit. Negative values pull those frequencies down, whereas positive values push those frequencies up.
- Q Factor: Showing up once the Bell option is picked, this parameter sets how wide the affected frequencies span. Lower values draw in a wider band of frequencies; higher values keep that band of frequencies narrower.

### Bands 2 through 5

A broad assortment of equalization adjustments is available through these band controls.

- Band enable button: Turns each band of EQ on and off.
- Band filter type: Four filtering options come with these Bands (running top to bottom): Lo-Shelf, Bell, Notch, and Hi-Shelf.
- Frequency: Sets where the EQ adjustment's center frequency sits.
- Gain: Governs how strongly the affected frequencies get hit. Negative values trim those frequencies down, whereas positive values lift those frequencies up.
- Q Factor: This parameter shows up once the Bell setting is chosen. It governs how wide the affected frequencies span. Lower values draw in a wider band of frequencies; higher values tighten the band of frequencies.

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
