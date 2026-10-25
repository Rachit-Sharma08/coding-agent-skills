# Echo and eq Fairlight eq and flanger

Version: DaVinci Resolve 20.3 Reference Manual. Context: Echo, Eq Fairlight eq, Flanger.
[Chapter index](INDEX.md) / [Previous section](dialogue-processors-distortion-and-echo.md) / [Next section](flanger-and-foley-sampler.md) / [Echo](dialogue-processors-distortion-and-echo.md)
<a id="source-bands-1-and-6"></a> <a id="source-bands-2-through-5"></a> <a id="source-eq--fairlight-eq"></a> <a id="source-eq-graph"></a> <a id="source-fairlight-eq-graphical-display"></a> <a id="source-fairlight-eq-plugin"></a> <a id="source-flanger"></a> <a id="source-master-controls"></a> <a id="source-the-stereo-echo-fairlight-fx"></a>

### The stereo Echo Fairlight FX

The controls Echo offers are:

- Bypass: Flips this plugin on or off.
- Input Format: (Shows up only when Echo sits on a multi-channel track.) Decides how the

several channels feed into the echo. Stereo keeps the Left and Right channels apart. Mono folds Left and Right into both channels. Left feeds in just the Left channel, while Right feeds in just the Right channel.

- Filter: Changes which proportion of frequencies make it into the delay effect. Placing the Delay plugin on a Mono Channel collapses the Left and Right sections into one “Delay” section. Low Cut (Hz): Acts as a High Pass filter across the whole signal. High Cut (Hz): Acts as a Low Pass filter across the whole signal. Feedback: Tunes the cutoff of a damping filter on the fed-back signal.
- Left Channel: Settings that act on the Left Channel’s delay on their own. Placing the Echo plugin on a Mono Channel collapses the Left Channel and Right Channel sections into one “Echo” section carrying only the Delay Time, Feedback Delay, and Feedback controls. Delay Time: The Left Channel’s overall Delay time. Feedback Delay: The Left Channel’s Echo Delay time. Feedback: How much of the Left channel feeds back into itself, as a percentage. L > R Feedback: What percentage of the Left feedback signal crosses over into the Right Channel.
- Right Channel: Settings that act on the Right Channel’s delay on their own. Delay Time: The Right Channel’s overall Delay time. Feedback Delay: The Right Channel’s Echo Delay time. Feedback: How much of the Right channel feeds back into itself, as a percentage. R > L Feedback: What percentage of the Right feedback signal crosses over into the Left Channel.
- Output: A group of settings governing what this plugin finally sends out. Dry/Wet (%): A percentage that balances the mix of the untouched “dry” source against the processed “wet” result. At 0 it is fully dry; at 100% it is fully wet. Output Level (dB): Raises or lowers the overall level of the affected sound.

### EQ ‑ Fairlight EQ

The Fairlight EQ is a 6-band parametric equalizer offering controls to lift or cut various frequencies. Every band carries controls for its filter type — Bell, Lo-Shelf, Hi-Shelf, Notch — plus Frequency, Gain, and Q-factor (how sharp the band is).

### Fairlight EQ plugin

### Master Controls

Along the top portion of the interface, the Equalizer window holds these controls

- Preset Menu: Store your EQ settings as presets by hitting the Plus button just left of the Preset menu, then bring them back later by opening the menu and picking one. You can likewise step through the presets with the left or right “arrow” (< or >) sitting to the right of the drop-down.

TIP: Make an EQ setting the default by choosing Set as Default from the Options menu (three dots) at the upper-right corner, right of the Reset button. Fairlight EQ Presets copy and paste between separate instances of the plugin to speed up your workflow.

- Compare Buttons (A and B): These let you flip rapidly between two distinct EQ settings. Build an EQ setting or load a preset while button A glows red, then switch to button B and build or pick a different one; clicking back and forth between the buttons swaps instantly from one to the other.
- Bypass Button: Turns the Fairlight EQ on and off.
- Reset Button: Hitting the round Reset icon at the EQ’s upper-right corner reverses

whatever you most recently did inside the plugin interface.

### EQ Graph

This graph plots the present EQ curve, with a handle standing in for each EQ band. Even though each handle's place on the graph follows the parameter settings shown in the plugin interface, you can grab any numbered handle and drag it to lift or cut the frequency range that an active band controls, according to whichever equalization filter is currently chosen.

### Fairlight EQ graphical display

### Bands 1 and 6

With these parameters you tune the bottom-most and top-most frequencies of the audio. Band enable button: Turns each EQ band on or off. Band filter type: Bands 1 and 6 can each cycle through five filtering options, listed here:

- On Band 1, the choices run (top to bottom): Lo-Shelf, Notch, Hi-Shelf, and Hi-Pass.
- On Band 6, they run (top to bottom): Lo-Pass, Bell, Notch, and Hi-Shelf. Frequency: Sets where the center of the EQ adjustment sits.

Q Factor: This parameter governs how wide a band of frequencies is touched and shows up only when Bell is chosen. Smaller numbers span a broader frequency band; larger numbers tighten it. It has no effect on the audio whenever the Hi-Pass, Lo-Shelf, or Hi‑Shelf filter is active.

### Bands 2 through 5

The controls and parameters carried by these bands are: Band enable button: Switches each EQ band on or off. Band filter type: Each of these Bands offers four filtering options (top to bottom): Lo-Shelf, Bell, Notch, and Hi-Shelf. Frequency: Sets where the center of the EQ adjustment sits. Gain: Negative numbers cut the chosen frequency while positive numbers lift it. It has no effect on the audio when the Notch filter is active. Q Factor: This parameter surfaces once Bell is picked. It governs how wide a band of frequencies is touched. Smaller numbers span a broader frequency band; larger numbers tighten it. It has no effect on the audio whenever the Lo-Shelf, Notch, or Hi-Shelf filter is active.

### Flanger

An effect plugin that delivers that instantly recognizable Flanger sound, a throwback to the era of paired tape machines where a small periodic delay on one of them produced flanging as the two drifted back into sync. People reach for it to lend a warbling harmonic flavor to a signal in all sorts of ways. While you adjust the Modulation parameters, an animated graph refreshes to picture the warble being layered onto the signal.
