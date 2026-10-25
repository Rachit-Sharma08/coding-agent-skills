# Delay controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Delay.
[Chapter index](INDEX.md) / [Previous section](chorus-and-de-esser-and-de-hummer-and-delay.md) / [Delay](chorus-and-de-esser-and-de-hummer-and-delay.md) / [Next section](dialogue-processors-distortion-and-echo.md)
<a id="source-fairlight-fx-part-2"></a> <a id="source-the-delay-fairlight-fx"></a>

### The Delay Fairlight FX

Delay has the following controls:

- Bypass: Toggles the plugin between on and off.
- Input Format: (Appears only once Delay is placed on a multi-channel track.) Governs

the way several channels feed into the delay. Stereo holds the Left and Right channels separate. Mono blends Left and Right onto both channels. Left brings in the Left channel by itself, and Right brings in the Right channel by itself.

- Filters: Reshapes how much of each frequency makes it into the delay effect. Should the Delay plugin land on a Mono Channel, the Left and Right sections give way to one combined “Delay” section.

Low Cut (Hz): Acts as a global High Pass filter. High Cut (Hz): Acts as a global Low Pass filter.

- Delay: Tunes how the delay is timed. Left/Right Delay (ms): The per-channel delay duration. Left/Right Feedback (%): What percentage of the Left or Right channel routes back into itself. Going negative makes that feedback percentage arrive phase-reversed relative to the source.
- Feedback: A cluster of settings that govern how much channels bleed into each other. High Ratio: Tunes the cutoff of a damping filter acting on the fed-back signal. Stereo Blend: Sets how much of each side's feedback crosses over to drive the opposite channel. Inserting the Delay plugin on a Mono channel hides the Stereo Blend control entirely.
- Output: A group of settings governing what this plugin ultimately sends out. Dry/Wet (%): A percentage that balances the mix between the untouched “dry” source and the processed “wet” result. At 0 the output is purely dry; at 100% it is purely wet. Output Level (dB): Raises or lowers the overall level coming out of the processed sound.
