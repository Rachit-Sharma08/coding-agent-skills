# Modulation and multiband compressor and noise reduction

Version: DaVinci Resolve 20.3 Reference Manual. Context: Modulation, Multiband compressor, Noise reduction.
[Chapter index](INDEX.md) / [Previous section](frequency-gain-lfe-limiter-and-meter-effects.md) / [Next section](noise-phase-pitch-reverb-and-soft-clip-effects.md)
<a id="source-modulation"></a> <a id="source-multiband-compressor"></a> <a id="source-noise-reduction"></a> <a id="source-the-default-setting-of-the-multiband-compressor"></a> <a id="source-the-modulation-fairlight-fx"></a>

### Modulation

This is an effect plugin — a versatile modulation tool aimed at sound effects and sound design. Its four effects bring together an LFO, FM adjustment, AM adjustment, Sweep and Gain filters so that frequency, amplitude, and spatial modulation can happen all at once. Together with the Rotation controls, you can fold straightforward Tremelo and Vibrato effects into auto-filter and auto-Pan tools to lend a sound texture and motion. As you tweak the Modulator, Frequency, and Amplitude parameters, an animated graph charts the outcome, giving you a picture of the kinds of modulation about to hit the signal. Output meters reveal the level leaving the plugin.

### The Modulation Fairlight FX

Modulation has the following controls:

- Bypass: Toggles this plugin on and off.
- Modulator: A low frequency oscillator (LFO), drawn in blue on the animated graph.

Shape: Picks the waveform the LFO uses to modulate the audio. Six choices are on offer: Sine, Triangle, Saw1, Saw2, Square, Random. Rate (Hz): Sets how fast the modulating LFO runs. Slower settings produce a warbling tone, whereas pushing it very high turns the audio into a buzz whose color depends on the shape you picked.

- Frequency: Frequency modulation (FM) driven by a secondary oscillator, rendered green on the animated graph.

Level (%): Behaves like a Dry/Wet knob that sets how much Frequency Modulation is layered on, dialing the effect up or back. Phase: Because all four core effects in this plugin may run together — and because modulation with level components (Tremelo/Rotation/Filter) can either reinforce or cancel one another — phase controls are provided. Shifting one effect’s phase lets you steer that interaction (for example, canceling a strong level change or offsetting a cancellation).

- Filter: Sweep and gain filters.

Filter (%): Behaves like a Dry/Wet knob governing how much filter sweep and gain is applied on top to reshape the signal. A 1D graph alongside previews the amount you’ve dialed in. Tone: Adjusts the center frequency of sweep. Phase: Because all four core effects in this plugin may run together — and because modulation with level components (Tremelo/Rotation/Filter) can either reinforce or cancel one another — phase controls are provided. Shifting one effect’s phase lets you steer that interaction (for example, canceling a strong level change or offsetting a cancellation).

- Amplitude: Amplitude modulation (AM) driven by a secondary oscillator, rendered green on the animated graph.

Level (%): Behaves like a Dry/Wet knob setting how much Amplitude modulation is applied. (Disabled in Ring Modulation Mode.) Phase: Because all four core effects in this plugin may run together — and because modulation with level components (Tremelo/Rotation/Filter) can either reinforce or cancel one another — phase controls are provided. Shifting one effect’s phase lets you steer that interaction (for example, canceling a strong level change or offsetting a cancellation). Ring Modulation Mode: Switches on a Ring Modulation effect, in which the carrier is multiplied by the modulator instead of being modulated by it.

- Rotation: This set of controls becomes accessible solely on a multi-channel track.

Rotate: How much Rotation is applied. Offset: The starting offset of the rotation, used to position the signal further out in space. Phase: Because all four core effects in this plugin may run together — and because modulation with level components (Tremelo/Rotation/Filter) can either reinforce or cancel one another — phase controls are provided. Shifting one effect’s phase lets you steer that interaction (for example, canceling a strong level change or offsetting a cancellation).

- Output: Controls that shape what finally leaves this plugin.

Dry/Wet (%): A percentage blend, as output, between the “dry” untouched signal and the “wet” processed one. 0 is completely dry, 100% is completely wet. Output Level (dB): Trims the overall level of the processed sound on its way out.

### Multiband Compressor

This is a dynamics processor that applies compression across precisely defined frequency bands. Its graph lays out frequencies in Hertz along the horizontal and gain in decibels along the vertical. That arrangement enables compression targeted at specific bands, which is handy when you only need to rein in one or a few portions of a signal.

### The default setting of the Multiband Compressor

Every band carries dynamics control across the set Low, Med, and High frequency ranges, and you adjust them either by dragging the intersection mark on each band’s graph or by entering a frequency directly. Bands 1 – 4: Controls for each band.

- Threshold: Caps how loud the output may get. The default is –25dB. The range is from –50 to 0dB.
- Gain: Lets you boost or cut by as much as 12 dB of gain.
- Ratio: Tunes the compression ratio. This is the gain reduction ratio (input to output) imposed on

signals climbing past the threshold level. The default is 1.5.0:1. The range is 1.0:1 to 7:1.

- Limit: Caps the output by as much as 15 dB. The default is 4.5 dB.
- Attack: Tunes the sidechain detector’s attack rate time constant. The default is 1.4 mS. The

range is 0.1 to 100 mS.

- Hold: Prevents the dynamics from firing again until a set interval has elapsed, expressed in mS

(milliseconds). Defaults to 0mS. The range is from 0 to 4000 mS.

- Release: Tunes how fast the sidechain detector ceases applying dynamics once a signal drops

down past the threshold once more. It defaults to 150 mS and spans 50 mS through 4.0 S. Master: A group of controls governing what finally exits this plugin.

- Gain (dB): Trims the processed sound’s overall level, adding or removing up to 18 dB of gain.
- Q: Tunes how wide a band of frequencies is affected. Smaller values cover a broader span, larger values a narrower one.

### Noise Reduction

This is a repair plugin built to suppress many varieties of noise across all sorts of recordings. A graph presents a spectral view of the targeted audio, with a purple overlay marking which noise is being acted on. A pair of audio meters — input on the left, output on the right — let you weigh how much signal the noise reduction is costing you. Three default presets ship with it: De-Hiss, De-Rumble, and De-Rumble and Hiss.
