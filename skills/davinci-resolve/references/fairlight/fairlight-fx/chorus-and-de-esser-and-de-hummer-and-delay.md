# Chorus and de esser and de hummer and delay

Version: DaVinci Resolve 20.3 Reference Manual. Context: Chorus, De esser, De hummer, Delay.
[Chapter index](INDEX.md) / [Previous section](chain-fx-and-chorus.md) / [Next section](delay-controls.md) / [Continue Delay](delay-controls.md) / [Chorus](chain-fx-and-chorus.md)
<a id="source-de-esser"></a> <a id="source-de-hummer"></a> <a id="source-delay"></a> <a id="source-the-chorus-fairlight-fx"></a> <a id="source-the-de-esser-fairlight-fx"></a> <a id="source-the-de-hummer-fairlight-fx"></a>

### The Chorus Fairlight FX

Chorus has the following controls:

- Bypass: Flips this plugin on or off.
- Input Format: (Shows up only when Chorus sits on a multi-channel track.) Decides

the way several channels feed into the Chorus. Stereo keeps the Left and Right channels apart. Mono folds Left and Right onto both channels. Left routes in the Left channel alone, while Right routes in the Right channel alone.

- Delay: The gap, in delay, separating the dry sound from the Chorus effect. Delay Time: How long the Chorus delay lines run. Separation: The spacing in time between the delay voices. Expansion: Dictates L/R length differences along with the phase offset of the modulators.
- Modulation: This bank of controls shapes, in several ways, the low frequency oscillator (LFO) behind the chorus effect’s tremolo. Waveform: Names the shape of the LFO that drives the Chorus rate and so colors the timing of the oscillations. The oscillator gives you six shapes to pick from:

Sine (Smooth oscillations)

Saw2 (Jerky oscillations)

Triangle (Sudden oscillations)

Square (Hard stops between oscillations)

Saw1 (Jerky oscillations)

Random (Randomly variable oscillations)

Frequency: Rate of the LFO steering the Chorus. Dial it low for a warble, high for a tremolo.

Pitch: How much frequency modulation there is, which bends the Chorus pitch. Level: Depth of level modulation, governing the “length” of the slice of Chorus folded into the sound. At low settings only the very onset of the Chorus effect comes through; at high ones a fuller Chorus warble or tremolo emerges.

- Feedback: A signal routed back into the Chorus Delay Line Amount (%): The share of signal sent back to the Chorus Delay Line. The value may be positive or negative, defaulting to 0 (no effect). Push it up and more of the Chorus effect joins the signal; pull it down and more of the inverted Chorus effect joins instead. Near 0 only a faint trace of Chorus reaches the audio, whereas farther from 0 (topping out at +/- 99) a steadily stronger Chorus comes through. Blend (%): The amount of feedback that spills into the opposite channel (Stereo mode only).
- Output: The controls that shape this plugin’s final output. Dry/Wet (%): A percentage blend of the “dry” or original signal against the “wet” or processed one; 0 is fully dry, 100% fully wet. Output Level (dB): Sets the overall output level of the treated sound.

### De-Esser

A repair plugin aimed at dialog. The De-Esser is a purpose-built filter meant to tame harsh sibilance — hissing “s” sounds or sharp “ts” sounds — within dialogue or vocals. A graph points out which slice of the signal the controls are tuned to act on, and reduction and output meters reveal which part of the signal is affected and at what level it leaves the plugin.

### The De-Esser Fairlight FX

The De-Esser has the following controls:

- Bypass: Switches the plugin on and off.
- Listen to Ess Only: With this top-right checkbox you hear nothing but the ess being

stripped out — a great help in judging whether too much signal is going or whether more ess attenuation is warranted.

- Frequency Range: A pair of controls homes in on the “s” frequency of a given speaker. Target Frequency: A knob that zeroes in on the frequency of the troublesome sibilance, which usually falls between 5 - 8kHz. Range: flips the De-Esser’s operating mode; reading top to bottom, the three choices are Narrow Band, Wide Band, and All High Frequency, the last of which treats every bit of audio above the source frequency.
- Amount: Sets how much de-essing gets applied.
- Reaction Time: Sets how abruptly the de-essing comes on, offering three options.

Slow: Like a slow attack. Medium: Like a medium attack. Fast: Like a fast attack.

### De-Hummer

A repair plugin you can bring to bear on any recording. It wipes out hum noise, the kind that frequently arises when audio gear picks up electrical interference through faulty cabling or grounding. As a rule, 50 or 60 cycle hum is a harmonic noise built from a fundamental frequency plus partial harmonics that begin at twice that fundamental. A graph reveals the frequency and harmonics under fire as you work this plugin’s controls.

### The De-Hummer Fairlight FX

De-Hummer has the following controls:

- Bypass: Turns this plugin off or back on.
- Listen to Hum only: This top-right checkbox lets you monitor solely the hum being

taken out — handy for gauging whether too much signal is leaving or whether further hum attenuation is needed.

- Frequency: Targets the source’s fundamental frequency. A knob handles a free-form frequency choice, while radio buttons offer the common 50Hz/60Hz electrical-mains values that are the usual cause of hum.
- Amount: Sets how much De-Hum extraction is applied.
- Slope: Tunes the balance of fundamental frequency against partial harmonics, and shifting it

makes it possible to go after various kinds of hum. A value of 0, for example, tilts hum extraction toward the fundamental frequency, 0.5 pulls all harmonics out evenly (up to 4), and 1.0 zeroes in on the higher-frequency partials.

### Delay

An effects plugin. An all-purpose stereo delay effect that covers jobs from track doubling to early reflection generation to plain harmonic enhancement. It works in stereo or mono, depending on the track it lands on. A graph charts the timing and strength of the echoes this plugin produces on each channel, while an Output meter reports the output level of the resulting signal.
