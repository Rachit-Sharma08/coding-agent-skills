# Noise reduction and phase meter and pitch and reverb and soft clipper

Version: DaVinci Resolve 20.3 Reference Manual. Context: Noise reduction, Phase meter, Pitch, Reverb, Soft clipper.
[Chapter index](INDEX.md) / [Previous section](modulation-and-multiband-compressor-and-noise-reduction.md) / [Next section](stereo-fixer-and-stereo-width-and-surround-analyzer.md) / [Noise Reduction](modulation-and-multiband-compressor-and-noise-reduction.md)
<a id="source-phase-meter"></a> <a id="source-pitch"></a> <a id="source-reverb"></a> <a id="source-soft-clipper"></a> <a id="source-the-noise-reduction-fairlight-fx-in-action"></a> <a id="source-the-phase-meter-plugin"></a> <a id="source-the-pitch-fairlight-fx"></a> <a id="source-the-reverb-fairlight-fx"></a> <a id="source-the-soft-clipper-fairlight-fx"></a>

### The Noise Reduction Fairlight FX in action

Noise Reduction has the following controls:

- Bypass: Toggles this plugin on and off.
- Listen to Noise Only: Found at the top right, this checkbox isolates just the noise being

removed for monitoring. It is invaluable for judging whether you’re stripping out too much signal or whether you can push the attenuation harder.

- Threshold (in dB): Tied to the signal-to-noise ratio (SNR) of the original recording. Where that ratio is poor, a higher threshold value is needed, which in turn produces more aggressive noise reduction.
- Attack (in ms): Chiefly relevant in Auto Speech mode, this governs the window over which the noise profile is sampled. Ideally the attack time tracks how much the unwanted noise varies. A small value means the noise profile refreshes faster and suits rapidly changing noise; a large value refreshes more slowly and suits noise that stays fairly steady.
- Sensitivity: Raising this overstates the noise profile that was detected; consequently more noise gets stripped away, though more of the dialogue you’d rather preserve may suffer too.
- Ratio: Sets the signal profile’s attack time relative to that of the noise profile. A quicker ratio catches and keeps speech transients more readily, though the resulting speech profile turns out less precise.
- Frequency Smoothing: Evens out the resulting signal across the frequency domain to offset harmonic ringing that lingers once the noise has been pulled out.
- Time Smoothing: A toggle that additionally applies smoothing to the resulting signal across the time domain.
- Dry/Wet: As output, a percentage blend between the “dry” original signal and the “wet” processed one. 0 is completely dry, 100% is completely wet.
- Level: So you can make up for any level lost to the noise reduction you’re applying, this adds pre-gain, ranging from -6dB to +18dB, just ahead of the dry/processed blend.

### Phase Meter

Phase cancellation is the effect in which the two waveforms of a stereo recording — say a stereo capture of a live music performance — slip out of sync for some reason and start canceling one another in erratic ways, leaving the audio sounding odd. The upshot is degraded sound that can be troublesome when you try to encode a mix to a delivery format such as AAF or MP3. The Phase Meter plugin offers a visual gauge for judging whether a signal is in phase; it is intended for a bus, so you can assess the phase of a whole mix and fix any issues that crop up. Where a green dot sits inside a horizontal meter tells you the signal’s phase: with no signal, or with signal on only one side of a stereo bus, the dot rests in the center (0); when the signal is out of phase it swings fully to the left (–); and when it is in phase it swings fully to the right (+).

### The Phase Meter plugin

### Pitch

An effects plugin that shifts audio pitch without altering clip speed.

### The Pitch Fairlight FX

Pitch has the following controls:

- Bypass: Toggles this plugin on and off.
- Semitones: A “coarse” control that moves audio pitch by as much as +/- 12 semitones.
- Cents: A “fine” control that nudges audio pitch by as little as +/-100th of a semitone.
- Dry/Wet: As output, a percentage blend between the “dry” original signal and the “wet” processed one. 0 is completely dry, 100% is completely wet.

### Reverb

A spatial simulation plugin able to reproduce multichannel reverberation for rooms of varying size, which you steer through a graphical 3D cube control. With it, a “dry” recording can be made to seem as though it were captured inside a vast cathedral, a bare room, a tiled bathroom, or any number of other spaces.

### The Reverb Fairlight FX

It helps, when learning this plugin’s controls, to recognize that the signal travels along three paths that combine into the final effect:

- A direct path.
- An early reflection path (ER) that models the early reflection rays produced by the first several

bounces off the walls as sound travels from the virtual source toward the virtual listener.

- A late reverberation path (Reverb) that models how an acoustic representation of the room behaves.

A graph offers a rough picture of how the reverb shapes the frequencies of the audio signal. Reverb has the following controls:

- Bypass: Toggles this plugin on and off.
- Room Dimensions: By setting how large the virtual room the sound occupies is, these

parameters jointly drive how both Early Reflection and Late Reverberation processing are configured. The room’s computed acoustic modes are routed into Late Reverberation processing, while the shape, gain, and delay of those first reflections are computed and routed into Early Reflection processing. Height, Length, Width: Sets each dimension of the reverberant space, measured in meters. Room Size: The computed Room Width x Length, given in meters.

- Reverb: Extra controls for fine-tuning how Early Reflection and Late Reverberation processing are configured.

Pre Delay: Lengthens or cancels the travel time from the virtual source to the virtual listener, thereby changing the opening gap between the source signal and its first reflection. Reverb Time: The decay time of the Reverb tail; it drives the overall decay of the acoustic modes coming out of late reverberation processing. Distance: Alters how far apart the virtual source and the virtual listener sit. It touches only how the early reflections processing is configured. Brightness: Shapes how decay time varies with frequency. At full brightness, every frequency decays in the same time; at minimum brightness, the higher frequencies decay faster and so sound duller. Modulation: Introduces random low-frequency phase modulation taken from the ER processing tap point. At 0%, no modulation occurs.

- Early Reflection Tone: A set of four post-equalization controls that shape the tone of the early reflections to match a given room. Low Gain: The gain applied to the low band. Low Frequency: Covers a band from 150 Hz to 500 Hz. High Gain: The gain applied to the high band. High Frequency: Covers a band from 1k Hz to 16k Hz.
- Reverb Tone: A set of four post-equalization controls that shape the tone of the reverb tail to match a given room. Reverb Tail Low Gain: The gain applied to the low band. Reverb Tail Low Frequency: Covers a band from 150 Hz to 500 Hz. Reverb Tail High Gain: The gain applied to the high band. Reverb Tail High Frequency: Covers a band from 1k Hz to 16k Hz.
- Output: These controls fold the three audio processing paths back together into one output. Dry/Wet: As output, a percentage blend between the “dry” original signal and the “wet” processed one. 0 is completely dry, 100% is completely wet. Direct Level: How much of the direct level is folded into the final signal. Early Reflection Level: How much early reflection is folded into the final signal. Reverb Level: How much reverb is folded into the final signal.

### Soft Clipper

The Soft Clipper is a limiting processor that pulls down output above a set threshold in a rounded fashion, so peaks are attenuated more gently. Driven hard past that threshold, the Soft Clipper plugin introduces saturation, lending the sound warmth and a touch of distortion. A graph illustrates the curve this plugin applies to the audio. Pairing a soft clipper with a conventional limiter is a common way to boost a track’s perceived loudness while avoiding harshness.

### The Soft Clipper Fairlight FX

Threshold: Adds input gain ahead of the clipper, driving audio peaks past the threshold by that amount, which in turn fuels the saturation and distortion. Shape: The clipper’s shape can be swept to alter the soft clipper’s character, from full soft-clipping (fully right, where peaks are rounded) to full hard-clipping (fully left, where peaks are squared off). Output Level: Lets you trim the output gain to make up for any signal lost during soft clipping when needed.
