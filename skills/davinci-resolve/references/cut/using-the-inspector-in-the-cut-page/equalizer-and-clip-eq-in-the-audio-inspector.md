# Equalizer and clip eq in the audio inspector

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the inspector in the cut page.
[Chapter index](INDEX.md) / [Previous section](retime-and-scaling-and-super-scale.md) / [Next section](bands-2-through-5-and-effects.md)
<a id="source-bands-1-and-6"></a> <a id="source-clip-eq-graph"></a> <a id="source-clip-eq-in-the-audio-inspector"></a> <a id="source-equalizer"></a> <a id="source-the-clip-eq-graph-with-user-draggable-handles"></a>

### Equalizer

Carrying both graphical and numeric controls, this six-band parametric equalizer boosts or cuts assorted frequency ranges within that clip before the signal even reaches the EQ built into the Mixer. Every band hands you its own controls — the filter type (Bell, Lo-Shelf, Hi-Shelf, Notch), then Frequency, then Gain, and a Q-factor (sharpness of the band) — while which controls a given EQ band reveals depends on the filter type. CUT TIP: Clip EQ settings copy and paste across, whether between two Clip EQ instances or from a Clip EQ over to a Track EQ.

### Clip EQ in the Audio Inspector

Master EQ Controls Up in the Equalizer window's upper‑right and left corners sit these overall controls:

- Enable button: Switches the whole EQ effect on or off, leaving the controls unreset.
- Reset button: Returns every control of the EQ window to its default.

### Clip EQ Graph

What this graph plots is the current EQ curve, its handles matching each enabled EQ band that is listed below. Drag any numbered handle to boost or cut the band of frequencies that handle governs, in whatever equalization type that band carries.

### The Clip EQ graph with user-draggable handles

As you drag a numbered handle on this graph, the matching band's parameters shift in turn, and adjusting any band's parameters reshapes the EQ graph too — which doubles as a visual readout of the equalization being laid over that track.

### Bands 1 and 6

The two outer sets of band controls let you carry out high-pass and low-pass adjustments where needed.

- Band enable button: Turns each band of EQ on and off.
- Band filter type: Across five specific filtering options, Bands 1 and 6 can be switched

to process the signal's lowest or highest frequencies. Over on Band 1, the lineup (top to bottom) runs: Lo-Shelf, Bell, Notch, Hi-Shelf, and Hi-Pass. Over on Band 6, the lineup (top to bottom) runs: Lo-Pass, Lo-Shelf, Bell, Notch, and Hi-Shelf.

- Freq: Sets where the EQ adjustment's center frequency sits.
- Gain: Governs how strongly the affected frequencies get hit. Negative values

pull those frequencies down, whereas positive values push those frequencies up.

- Q Factor: Showing up once the Bell option is picked, this parameter sets how wide the

affected frequencies span. Lower values draw in a wider band of frequencies; higher values keep that band of frequencies narrower.
