# Dialogue processor and dialogue leveler and distortion and echo

Version: DaVinci Resolve 20.3 Reference Manual. Context: Dialogue processor, Dialogue leveler, Distortion, Echo.
[Chapter index](INDEX.md) / [Previous section](delay-controls.md) / [Next section](echo-and-eq-fairlight-eq-and-flanger.md)
<a id="source-dialogue-leveler"></a> <a id="source-dialogue-processor"></a> <a id="source-distortion"></a> <a id="source-echo"></a> <a id="source-the-dialogue-leveler-plugin"></a> <a id="source-the-dialogue-processor-plugin"></a> <a id="source-the-distortion-fairlight-fx"></a>

### Dialogue Processor

Within one plugin, the Dialogue Processor links six routine audio-treatment stages in series, with each stage geared toward the kinds of fixes that make recorded dialog sound better. Its dedicated De-Rumble, De-Pop, De-Ess, Comp(ressor), Expander, and Excite sections each expose a pared-down control set aimed at the typical corrections a clean-sounding dialogue track tends to need.

### The Dialogue Processor plugin

- De-Rumble: This stage is a high pass filter that lets you clear out subsonic rumble (the subharmonic low end) from a vocal microphone feed. For the bulk of condenser mics, 40 or 50Hz is a dependable setting. Pushing the value upward begins eating into legitimate low frequencies of the source, though that can occasionally be a handy creative trick.

Frequency: Places the high-pass filter anywhere from 40Hz to 235Hz.

- De-Pop: Governs the center frequency of a purpose-built filter that strips out vocal “popping,” or plosives — the bursts that happen when a speaker is right up on a microphone capsule on-axis.

Frequency: Places the filter anywhere from 50Hz to 200Hz. Amount: Dials in how strongly the filter acts on the signal; smaller numbers do less and larger numbers do more. A meter beside the amount knob displays the degree to which the signal is being treated.

- De-Ess: Fixes the center of a dedicated bandpass filter that tames vocal “Esses,” which tend to stand out too much because of sibilance. Removing those esses lets you push up the average level and add brightness to a vocal without harshness, since our hearing reacts strongly to excessive sibilance. For both male and female voices, 6 to 7 kHz is usually the sweet spot.

Frequency: Places the filter anywhere from 700Hz to 9000Hz. Amount: Dials in how strongly the filter acts on the signal; smaller numbers do less and larger numbers do more. A meter beside the amount knob displays the degree to which the signal is being treated.

- Compressor: Narrows a signal’s dynamic range by shrinking the gap in level between its loudest and softest moments. By doing so it can lift the whole signal upward, gaining without clipping and therefore sounding louder. It is a common way to bring voices forward in a mix and to even out tracks whose dynamic range is too wide for where they sit.

Threshold (dB): Marks the point, between –40dB and –8dB, where the signal begins to be affected. Amount: Dials in how much compression hits the signal; smaller numbers do less and larger numbers do more. A meter beside the amount knob displays the degree to which the signal is being treated. Fast/Slow: Chooses whether the processing engages quickly or slowly.

- Expander: Widens volume contrasts by pulling down the quieter portions of a signal relative to its louder ones, which is handy for suppressing noise while opening up a signal’s dynamic range.

Threshold (dB): Marks the point, between –40dB and –8dB, where the signal begins to be affected. Range: How far, in dB, the level drops as the expander pushes the softer passages down. Fast/Slow: Chooses whether the processing engages quickly or slowly.

- Excite: Manufactures extra high-frequency content on top of a source signal through several methods. Applied gently, it lends presence to sounds that might otherwise feel dull, with no need to reach for EQ.

Amount: Dials in how much the exciter acts on the signal; smaller numbers do less and larger numbers do more. A meter beside the amount knob displays the degree to which the signal is being treated. Female/Male: Biases the exciter’s behavior toward either a male or a female voice.

### Dialogue Leveler

The Dialogue Leveler studies the source to locate speech, then proceeds to “ride down” the louder stretches, “lift up” the quieter ones, and pull down non-dialogue background. It achieves this without the telltale “pumping” of a normal dynamics processor (compression/limiting) or other obvious artifacts, landing close to what you would get from meticulous manual clip-gain work or from carefully “riding” a fader as automation. It can frequently “fix and mix” a single-boom-mic recording in which one actor sits nearer than another or swings off-axis at points, evening it out so the original relative dynamics survive while clarity and average level both climb. You can run it on track audio as it plays, though not on a live input, and it accepts any mono or stereo (or multi-mono) track — but tracks wider than stereo are not supported.

### The Dialogue Leveler plugin

The controls offered by Dialogue Leveler are:

- Dialogue Leveler: Switches the Dialogue Leveler processing on or off.
- Waveform Processing display: Presents a scrolling waveform readout and marks the Dialogue Leveler

activity with a gray line. Bear in mind, though, that this readout is absent from the clip-based variant of Dialogue Leveler.

- Preset Menu: The choices available from the preset menu are:

Allow wider dynamics: The default pick, suited to material whose loud-to-soft swings are broad and whose clip levels run medium to high. More lift for low levels: Reach for this when the source carries a lot of quiet dialogue you would like to bring up. Lift soft whispery sources: Use this for material that combines whispered speech with background noise. Optimize moderate levels: Choose this when the whole source sits at moderate levels.

- Reduce Loud Dialogue: With this on, the louder speech is ridden down at its peaks, behaving rather like a “perfect limiter” that frees you from setting any threshold or time constants. Because of its “near real time” nature, the analysis runs ahead of what you hear so the result is optimal.
- Lift Soft Dialogue: With this on, it locates quiet speech and raises and smooths out passages that are softer and more uneven, yet because its focus stays on dialogue it generally leaves background sounds alone (unless they coincide with the speech itself). In most cases this is the handiest of the three, since it pulls faint lines of dialogue up into audibility and natural smoothness without lifting background noise.
- Background Reduction: With this on, it trims background sounds by concentrating on the dialogue and easing the rest out according to the built-in presets (Preset menu).
- Output Gain: Set the Output Gain either by dragging on the Output Gain control or by typing a number into the field (the Output Gain control runs in dB across a 0 to +6 dB range at .1dB resolution).

### Distortion

An effects plugin. It generates audio distortion handy for sound design and effects work, spanning everything from gentle harmonic distortion that mimics a signal passing through crude or broken electronics (think poor speakers, old telephones, or outdated recording gear) up to imitating an overdriven feed undergoing varying degrees of hard clipping (picture someone shouting into a cheap bullhorn, megaphone, or PA rig). A soft tube emulation sits in the output stage. As you tweak the Distortion parameters, an animated graph updates to picture the harmonic distortion, waveshaping, and clipping about to reshape the signal. Input and Output meters reveal what is happening to the levels.

### The Distortion Fairlight FX

The controls Distortion offers are:

- Bypass: Flips this plugin on or off.
- Filters: A pair of filters lets you mimic gear that only reproduces a narrow band of frequencies. LF Cut: Shapes the distortion at the low end. HF Cut: Shapes the distortion at the high end.
- Distortion: Three control groups let you dial in the character and severity of distortion you are after. Mode buttons: Toggle which distortion mode is running. The left one, Distortion, yields harmonic distortion. The right one, Destroy, is a harsher polynomial waveshaper. Distortion: Sets how much distortion lands on the signal, with bigger numbers distorting harder. Ceiling: Sets the input level at which clipping kicks in.
- Output: A group of settings governing what this plugin finally sends out. Dry/Wet (%): A percentage that balances the mix of the untouched “dry” source against the processed “wet” result. At 0 it is fully dry; at 100% it is fully wet. Output Level (dB): Raises or lowers the overall level of the affected sound. Auto Level button: Automatically compensates for the gain the distortion adds to the signal. Leaving it on keeps the signal from jumping up wildly and unexpectedly, while switching it off lets you chase whatever you want — including a heavy dose of distortion.

### Echo

An effects plugin. A traditional Echo effect that recreates sound reflections arriving some delay after the direct sound reaches the ear. Whether it runs in stereo or mono follows the track you place it on. A graph plots the timing and strength of the echoes the plugin produces per channel, and an Output meter shows the output level of the resulting signal.
