# Frequency analyzer and gain and lfe filter and limiter and meter

Version: DaVinci Resolve 20.3 Reference Manual. Context: Frequency analyzer, Gain, Lfe filter, Limiter, Meter.
[Chapter index](INDEX.md) / [Previous section](playing-and-recording-sound-effects.md) / [Next section](modulation-and-multiband-compressor-and-noise-reduction.md)
<a id="source-frequency-analyzer"></a> <a id="source-frequency-analyzer-plugin-waterfall-view"></a> <a id="source-frequency-analyzer-spectrum-view"></a> <a id="source-gain"></a> <a id="source-lfe-filter"></a> <a id="source-limiter"></a> <a id="source-limiter-controls"></a> <a id="source-limiter-sidechaining"></a> <a id="source-meter"></a> <a id="source-sidechain-controls"></a> <a id="source-the-fairlight-gain-plugin"></a> <a id="source-the-lfe-plugin"></a> <a id="source-the-limiter-plugin"></a> <a id="source-the-meter-fairlight-fx"></a> <a id="source-using-the-limiter-sidechain"></a>

### Frequency Analyzer

Presenting your clips or tracks as either a Spectrum or Waterfall graph, the Frequency Analyzer gives you a visual readout that exposes potential tonal problems and helps you refine the sound. Using the Mode menu at the top right, you can inspect the entire frequency range of the signal (the default) or zoom into Low, Midrange, or High frequency regions.

### Frequency Analyzer Spectrum view

### Frequency Analyzer plugin Waterfall view

### Gain

Use this plugin when you need to raise or lower an audio signal’s loudness by an exact decibel amount. It comes in handy across many situations — for instance, quickly tweaking the overall level of a track that already carries a lot of mixer or plugin automation. Use this plugin when you need to raise or lower an audio signal’s loudness by an exact decibel amount. It comes in handy across many situations — for instance, quickly tweaking the overall level of a track that already carries a lot of mixer or plugin automation.

### The Fairlight Gain plugin

### LFE Filter

This is a low-pass filter you can place on a FlexBus or Main carrying a surround sound format, used to route low-frequency content to an LFE channel within a surround mix. Anything above the frequency you choose is held back from the audio fed to a sub-woofer on the LFE channel. The result is cleaner playback, since superfluous content never reaches the sub-woofer. A Frequency control selects the low band you want passed through, and a Trim control sets the level of the resulting LFE channel. When the source is multi-channel yet lacks an LFE channel — a 5.0 layout, for example — the plugin simply has no effect.

### The LFE plugin

### Limiter

By detecting and taming peaks, the Limiter lets you push the overall level higher without clipping, while compressing the dynamic range much as a compressor would. As a genuine true peak limiter, it can look 64 samples ahead of the incoming signal, which yields an exceptionally smooth limiting action. Adjust the incoming level with the Input control, and use the Threshold and Release to govern when limiting kicks in and how long it lasts. The graph highlights the portions of the signal currently being acted upon.

### The Limiter plugin

### Limiter controls

- Bypass: Toggles this plugin on and off.
- Input Meter: Shows the level of the incoming signal.
- Input Level: Sets the level of the signal coming in, spanning from -18 dB up to +18 dB.

Switching on the Soft button makes the limiter apply a more gradual attack.

- Ceiling: Fixes the point (level) above which the Limiter begins pulling the incoming signal down.

At a setting of -24 dB, everything louder than that point is limited; at 0 dB, nothing is limited.

- Release: Governs the duration of the limiting (signal reduction). Dialing this

control down to 0.01 milliseconds produces a very fast release, while the longer 1000 milliseconds value is the slowest on offer.

- Reduction Meter: Displays how much level (gain) reduction is currently hitting the incoming signal.
- Output Meter: Shows the output level after the limit.

### Limiter Sidechaining

Sidechaining is supported by the Fairlight FX Limiter, letting you momentarily pull down the level of a destination track or bus driven by the audible content of a source track or bus. It proves quite useful when several tracks compete for room in a mix because they occupy some or all of the same frequencies — say, a dialogue track alongside a bus carrying traffic and crowd ambience. In essence it is yet another flavor of “ducking”: in that scenario the dialogue lowers the traffic and crowd noise until the speaking stops, so the voices come through with greater clarity.

### Sidechain controls

### Using the Limiter Sidechain

Picking up the earlier scenario: 1 On the destination track or bus carrying the traffic and crowd noise, open the Limiter. 2 From the source dropdown beside the Listen button, pick the Dialogue track or bus.

- This is the source signal whose content drives the level reduction on the target track.
- Choosing a bus as your source means several inputs can drive the changes on the target track. Pressing the Listen button plays back the incoming signal, which is handy for verifying that the right input is actually reaching the Limiter. When active, this button glows yellow.

### Meter

This is a sample peak processing meter, handy for momentarily attaching a meter to one particular track or FlexBus. Such meters earn their keep whenever you want a sizable meter trained on a single bus or track during your work.

### The Meter Fairlight FX

The display is deliberately spare: a gray bar tracks the level while a red peak line holds for two seconds to mark the loudest peak. A numeric readout at the meter’s top reports the precise level in dB, and that figure keeps holding to indicate the highest level reached over any span of playback. You can resize the Meter by dragging from its lower-right corner, and the option menu carries these controls:

- Reset Peak on Play: With this on, the numeric peak figure clears each time you stop and restart playback. With it off, that figure stays put until a louder peak replaces it.
- Reset: Resets the numeric peak level.
