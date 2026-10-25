# Flanger and foley sampler

Version: DaVinci Resolve 20.3 Reference Manual. Context: Flanger, Foley sampler.
[Chapter index](INDEX.md) / [Previous section](echo-and-eq-fairlight-eq-and-flanger.md) / [Next section](playing-and-recording-sound-effects.md) / [Flanger](echo-and-eq-fairlight-eq-and-flanger.md)
<a id="source-a-footsteps-recording-loaded-into-the-foley-sampler"></a> <a id="source-adding-sound-effects"></a> <a id="source-foley-sampler"></a> <a id="source-setting-up-the-foley-sampler"></a> <a id="source-splitting-sound-effects"></a> <a id="source-the-flanger-fairlight-fx"></a>

### The Flanger Fairlight FX

The controls the Flanger offers are:

- Bypass: Flips this plugin on or off.
- Input mode: (Appears only when the Flanger sits on a multi-channel track.) Decides

how the several channels feed into the Flanger. Stereo keeps the Left and Right channels apart. Mono folds Left and Right into both channels. Left feeds in just the Left channel, while Right feeds in just the Right channel.

- Modulation: A low frequency oscillator (LFO) that powers the Flanger effect.

Waveform (Hz): Sets the LFO shape that modulates how fast the Flanger sweeps. There are three options: Sine, which eases the rate up and down smoothly; Triangle, whose rate shifts more abruptly; and Sawtooth, which jumps the rate suddenly. It governs the timing of the warble layered onto the sound. Rate: The LFO speed, which drives how quickly that warble moves. Small rate numbers yield a slow warble, while large ones turn it into more of a buzz. Depth: Governs the “length” of the warble added to the sound. Small numbers add only the warble's leading edge; large ones add a more fully formed warble.

- Width: Holds a single parameter, Expansion, which sets the length difference between the Left/Right channels along with the phase offset of the modulators.
- Feedback: These controls largely decide how extreme the Flanging effect becomes.

Amount (%): What percentage of the signal routes back into the Delay Line. The value may be positive or negative, defaulting to 0 (no effect). Raising it pours more of the Flange effect into the signal; lowering it pours in more of the inverted Flange effect. At values near 0, you hear only a faint phase shift in the audio, but the farther the value moves from 0 (topping out at +/- 99), the more a steadily growing warble emerges. Which warble you get hinges on the Modulation controls. High Ratio: Sets how the echo fades out over time.

- Output: A group of settings governing what this plugin finally sends out.

Dry/Wet (%): A percentage that balances the mix of the untouched “dry” source against the processed “wet” result. At 0 it is fully dry; at 100% it is fully wet. Output Level (dB): Raises or lowers the overall level of the affected sound.

### Foley Sampler

The Foley Sampler is a sampler built into the application that simplifies dropping in sound effects you intend to trigger from a keyboard, pad, or any other MIDI performance device hooked up to your computer, so you can place timed effects in sync with what is happening on screen. Its whole design is to streamline capturing performed audio cues onto the current track that hosts the sampler.

### Setting Up the Foley Sampler

Capturing samples through a MIDI controller with the Foley Sampler is straightforward. 1 Make an audio track to hold your sound effects or instrument recording. 2 Drop the Foley Sampler onto the track header to bind it to that track. The Foley Sampler window opens on its own. Because the Fairlight page recognizes this as an instrument with no plugin inputs, the effect gets patched straight to that track’s input, set to record. 3 When a MIDI controller of any sort is connected and correctly set up, it shows up in the MIDI dropdown at the top-right of the Foley Sampler window (beside the Keyboard button). Pick your device there, and the Keyboard button lights up to confirm it is on. The Foley Sampler is now usable, yet out of the box it holds no samples to play. Adding sound effects comes next.

### Adding Sound Effects

There are several routes for loading prerecorded sound effects or instruments into the Foley Sampler:

- From the file system, drag a supported-format audio file and drop it onto the Foley Sampler window
- Pull a sound effect out of the Sound Library and drop it on the Foley Sampler window
- Open the Option menu of the Foley Sampler window and bring sounds in from your connected drives.

As soon as some sound effect is loaded, it maps itself to the four highest keys of your instrument, beginning at C2. Hitting a key or pad on your controller fires that sound. Click the Sample button atop the Sound panel to view the sound’s waveform. For this walkthrough, we have a run of continuous footsteps recorded back to back to work with.

### A footsteps recording loaded into the Foley Sampler

### Splitting Sound Effects

A frequent practice is to grab pre-recorded library effects — a string of recorded footsteps, cloth rustles, punches, or similar “foleyed” recordings — so you can trigger variations of one repetitive effect in time with on-screen action. The Foley Sampler makes that simple. 1 With a sound effect already loaded, open the Foley Sampler window’s Option menu and pick Split Sample; this carves the current sample into slices by analyzing its noise floor and parks each slice on a group of keys or pads on your chosen MIDI device. Picking up the earlier example, each footstep is now split off onto its own key.

2 To fine-tune the timing of any split-off slice, click the assignment text above the keyboard along the bottom of the window to bring that slice up in the Sample view. 3 Use the Range Start and Range End parameters to take in as much or as little of that slice as you wish to play. 4 Should you want a sample to loop while a note is held, switch on the Loop button and then set the Loop Start and Loop End parameters to decide how much of each slice loops. 5 To clear out slices you don’t need, select one you dislike and press Shift-Delete to wipe it from the virtual keyboard.

One isolated slice from that footsteps recording once the Foley Sampler has split it, its effect range now tweaked Assigning Sound Effects Manually The first sound effects you load into the Foley Sampler land automatically across a run of notes. Every further effect you load drops onto the next run of notes off to the right. Once every note is taken, new effects push all earlier assignments leftward. You may also assign loaded effects by hand. That comes in handy when you want to load an assortment of different effects in one go (say, a mix of punch sounds, human grunts, and cloth rustles for a fight scene) and drop them onto notes you specify. 1 Bring in the sound effect you intend to place. 2 Hit the Mapping button to change which span of notes it covers. 3 Use the Low and High parameters to pick a note range for the chosen sound.

4 Where needed, you also have the option of tuning the pitch of particular sound effects.

Using the Mapping controls to pin a sound onto a specific group of notes Adjusting Sound Effects To take a sample or slice further, select it above the virtual keyboard and reach for the Level panel controls to shape the dynamics of playback, or the Filter panel controls to EQ the sound. TIP: When a sample or slice is set to loop, hold the Control key and click a key on the virtual keyboard to kick off looping, letting you hear the adjustments as you dial them in.
