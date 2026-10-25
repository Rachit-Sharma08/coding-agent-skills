# Speed change control in the inspector and parametric equalizer

Version: DaVinci Resolve 20.3 Reference Manual. Context: The Fairlight inspector.
[Chapter index](INDEX.md) / [Previous section](clip-mode-vs-track-mode-and-audio-tab.md) / [Next section](audio-tab-track-mode-and-effects-tab.md)
<a id="source-eq-graph"></a> <a id="source-parametric-equalizer"></a> <a id="source-speed-change-control-in-the-inspector"></a> <a id="source-the-channel-strips-eq-indicator"></a> <a id="source-the-eq-graph-with-user-draggable-handles"></a> <a id="source-track-mode"></a>

### Speed Change control in the Inspector

These are the overall controls in the Speed Change window:

- Enable button: Flips the whole Speed Change effect off and on

without clearing the controls.

- Reset button: Restores every control of the Speed Change window to its default.
- Direction: The Right Arrow keeps the waveform running forward, the Left Arrow

flips the waveform’s direction, and the Snowflake icon makes a freeze frame.

- Speed %: A flywheel control that shifts the speed by a percentage of plus or minus 100%.
- Frames Per Second: A flywheel control linked to the Speed % control that displays the

FPS in relation to the speed change.

- Duration: Shows the clip’s revised timing.
- Ripple Sequence: Tick this and every bit of media past the action ripple-edits over to

the new duration.

- Pitch Correction: Tick this and the clips keep their original pitch through the

speed change. Leave it unticked and the audio speeds up or slows down along with the speed move. A slower speed change drops the pitch; a faster one raises it.

NOTE: Inside the Speed Change controls, steer clear of the freeze frame option, as it will harm the chosen audio file.

### Parametric Equalizer

Offering graphical as well as numeric controls, this four-band equalizer boosts or cuts assorted frequency ranges inside a clip even before that signal reaches the EQ built into the Mixer. Every band carries controls covering its filter type (Bell, Lo-Shelf, Hi-Shelf, Notch), plus Frequency, Gain, and a Q-factor (the band’s sharpness); which controls a band offers shift according to its filter type. Switch on a channel strip’s EQ and the Mixer shows the equalization curve in force. Because a channel strip’s EQ settings hit every clip on that track, you have to open the EQ window to make those changes.

### The channel strip’s EQ indicator

Master EQ Controls Up in the top right and left corners, the Equalizer window holds these overall controls.

- Enable button: Flips the whole EQ effect off and on, leaving the controls as they were.
- Reset button: Returns every control of the EQ window to its default.

### EQ Graph

Here the present EQ curve appears, fitted with handles tied to each active EQ band listed beneath. Drag any numbered handle to boost or cut the frequency range that band rules, applying whichever equalization type that band has been assigned.

### The EQ graph with user-draggable handles

When you drag the numbered handles on this graph, the matching band’s parameters change, and reshaping a band’s parameters likewise reshapes the EQ graph, which doubles as a visual picture of the equalization being put on that track. Bands 1 and 4 The pair of outer band control sets handle high-pass and low-pass moves when you need them.

- Band enable button: Switches each EQ band on and off.
- Band filter type: For Bands 1 and 4 you can pick among six particular filtering options

aimed at the signal’s lowest or highest frequencies. Running top to bottom these are: Hi-Shelf, Hi-Pass, Bell, Notch, Lo-Pass, and Lo-Shelf. For Bands 2 and 3 the picks are Lo-Shelf, Bell, Notch, and Hi-Shelf.

- Freq: Sets where the center frequency of the EQ move sits.
- Gain: Sets how strongly the targeted frequencies are hit. Negative figures cut those frequencies, while positive figures lift them.

Bands 2 and 3 The pair of middle band control sets let you perform a broad assortment of equalization moves.

- Band enable button: Switches each EQ band on and off.
- Band filter type: For Bands 2–5 you can pick among four distinct filtering options, running top

to bottom: Lo-Shelf, Bell, Notch, and Hi-Shelf.

- Frequency: Sets where the center frequency of the EQ move sits.
- Gain: Sets how strongly the targeted frequencies are hit. Negative figures

cut those frequencies, while positive figures lift them.

- Q Factor: Sets the span of frequencies affected. Smaller figures take in a broader band of

frequencies; larger figures take in a narrower one.

NOTE: It may go without saying, but not every parameter exists for every curve type. A Bell curve filter, say, has Frequency, Gain, and Q adjustments, yet a Lo-Pass or Hi‑Pass filter leaves only Frequency open to adjust.

### Track Mode

As you work with audio tracks or busses (Track mode), the Audio tab lets you set the volume level plus switch on and tune Fairlight Track FX. To read more about Fairlight Track FX, turn to Chapter 181, “Fairlight FX.”
