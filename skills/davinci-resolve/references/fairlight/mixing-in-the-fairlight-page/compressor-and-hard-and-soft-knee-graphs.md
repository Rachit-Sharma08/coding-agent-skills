# Compressor and hard and soft knee graphs

Version: DaVinci Resolve 20.3 Reference Manual. Context: Mixing in the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](copying-and-pasting-effect-settings-and-effects-in.md) / [Next section](band-1-controls-active-and-band-6-controls-active.md)
<a id="source-bands-1-and-6"></a> <a id="source-compressor"></a> <a id="source-eq"></a> <a id="source-hard-and-soft-knee-graphs"></a> <a id="source-limiter"></a> <a id="source-master-eq-controls"></a> <a id="source-sidechain-module"></a> <a id="source-sidechaining-and-ducking-with-dynamics"></a> <a id="source-the-channel-strip-eq-window"></a> <a id="source-the-eq-graph"></a> <a id="source-the-eq-graph-1"></a>

### Compressor

The second group of dynamics parameters applies compression, which reads an audio signal's envelope in order to adjust its level automatically. A compressor narrows a signal's dynamic range by shrinking the level gap between the loudest and softest portions of the input. It can lift the overall level of the signal without clipping, raising perceived loudness. Compression often helps voices sit more present in a mix and evens out level swings on tracks whose dynamic range is too wide for the job at hand.

Yet "overcompressing" can strip away a sound's natural dynamics, or wipe out so many of the natural transients (the bursts of energy, or "attacks") that lend the original sound its character. Heavier compression can also be applied creatively, though, to reshape a sound's character toward more apparent attack, alter its release behavior, or shift the balance and blend of the space a sound was captured in (for instance, compressing a source signal with a higher ratio and quick release to bring up the presence of a room tone in which the source was recorded).

- Compressor: Enables the Compressor.
- Threshold: Defines the signal level above which compression takes effect; its default is –15 dB, with a

span of –50 to 0 dB.

- Ratio: Tunes the compression ratio. This fixes the gain reduction ratio (input to output) put on

signals climbing above the threshold level. The default is 2.0:1. The range is 1.0:1 to 10:1. Commonly used ratios for dialogue processing are 2.5:1 to 3:1. With a 3:1 ratio, for every 3 dB of increase in signal above the threshold, 1 dB is output.

- Knee: Shapes how signals sitting right around the threshold behave. The knee can ease the changeover from where no compression is audible to where the "hard compression" (the set ratio) begins.

The Knee: Control smooths the slope at the threshold point. You can watch the Knee's effect on the graph by using a ratio such as 4:1 and adjusting Knee; the line where compression "kicks in" rounds off as the Knee control rises. Ordinarily, compression starts immediately above the threshold, which is called a "hard knee." For a gentler, less noticeable approach to compression, dial in a softer knee so that compression comes on gradually as signals near the threshold and climb past it.

### Hard and Soft Knee graphs

Mix: Blends the compressed (0) and non-compressed input signal (100), so you can weigh the compressed signal against the original, untreated sound. Say you are building a big explosion impact effect; it can occasionally help to fold a touch of the original, uncompressed signal into a more compressed version, holding onto more of the original character alongside the compressed version. The default is 0 (all compression, no original signal). Attack: Controls how rapidly compression engages once a signal passes the threshold; it defaults to 1.4 ms and covers 0 to 100 ms.

Hold: Once the attack phase finishes, the Hold parameter governs how long that initial attenuation persists before the release phase begins; the default is 0 ms, with values from 0 to 4000 ms. Release: Sets how fast or slow the sidechain detector ceases applying compression as a signal drops back below the threshold; its default is 93 ms, spanning 50 to 4000 ms (4 seconds). Sidechain: This reworked section lets you build sidechain compression, or "ducking," from the parameters and controls listed below, rather than feeding the sidechain input via a Send from a track or bus:

### Sidechain module

- On: A click turns this button red, signaling that the Sidechain module is now active.
- Listen: A click on this button isolates the incoming signal for monitoring, which helps when you

want to verify that the right audio signal is reaching the Sidechain module.

- Source: This button picks which track or bus is supplying the incoming audio.

### Sidechaining and "Ducking" with Dynamics

The Dynamics module lets you build "sidechain" compression, where a source track or bus uses its audible signal to briefly pull down the level of a target track or bus. For instance, dialogue may live on one track or bus (the source) while music lives on another (the target), and you want that dialogue to stand out more. The procedure: 1 On the music track or bus, open the Dynamics plugin and turn on the Compressor. 2 Open the Source dropdown and pick the dialogue track or bus. TIP: Choosing a bus as the ducking source lets several sources drive changes in your target track. 3 Press the On button; it turns red to show the Sidechain section is now active. 4 As a section of your mix plays back, dial in the gain reduction by dropping the Threshold and lifting the Ratio until the target audio is pulled down enough to make the dialogue more audible. 5 If required, tweak the Hold parameter so the gain reduction does not swing around too erratically. 6 You might also need to tune the Release parameter so the gain reduction does not cut off too sharply. A click on the Listen button isolates the incoming signal when you need to verify that the right input signal is reaching the Limiter. This button goes yellow when active.

### Limiter

The third group of dynamics parameters applies limiting, which sets a targeted ceiling on the level a signal is allowed to reach. Limiting resembles compression but works essentially at a very high ratio.

- Limiter: Enables the Limiter.

Threshold: Defines the threshold above which limiting takes place. Since the Limiter is built to hard limit the output, this effectively also fixes the highest permissible output level; its default is –21 dB, adjustable across –50 to 0 dB. The best approach is to judge the amount of limiting by ear, watching the gain reduction shown on the meter. Overdoing limiting can "squash the life out of the sound," since a mix can shed all of its internal dynamics. Applied well, it smooths out the final mix and lifts the average level. The yellow animated balls in the display also let you observe how the controls shape the real time limiting response. Attack: Governs the attack rate time constant of the sidechain detector; it defaults to 0.71 ms and covers 0 to 100 ms. Hold: After the input level drops beneath the threshold, Hold sustains limiting until the hold time runs out, at which point release time begins; the default is 0 ms, with values from 0 to 4000 ms. Release: Governs how fast the sidechain detector ceases applying limiting as the signal sinks below the threshold; its default is 90 ms, spanning 50 to 4000 ms.

NOTE: With limiting placed on your channel's final output (or across a whole mix), the Makeup Gain slider is frequently needed, either to push the output level to its maximum (on a master) or to restore an individual track's original level (unity). To compare the level change, bypass the Limiter alone or the entire Dynamics module.

### EQ

A 6-band equalizer EQ lives on every Mixer channel strip, accompanied by a mini-EQ graph that shows the present EQ curve, bypasses the plugin, and opens it on a double-click. Among the plugin's choices are high and low shelving, response curves that are parametric or notch, plus high and low pass filters reaching slopes of 24dB/octave, together with controls that lift or cut across various frequency ranges. On each band you get controls for the filter type (Bell, Lo-Shelf, Hi-Shelf, Notch), along with Frequency, Gain, and Q-factor (which sets the band's sharpness); whichever filter type is selected decides which of these controls a band exposes. There is also a selection of four response curves, running from the Native Fairlight response curve to emulations of classic EQs.

The EQ Indicator on the channel strip. (Left) EQ has been adjusted; (Right) EQ sits flat (no EQ).

### The channel strip EQ window

### Master EQ Controls

These overall controls are found in the Equalizer window:

- Enable button: Switches the plugin on and off.
- Reset button: Found at the EQ's upper right, the circular Reset icon restores every parameter to its default setting and value.
- Equalizer Type: From this dropdown you can pick the Native Fairlight response curve or any of three classic mixing-console EQ emulations. The Earth option gives you the Native Fairlight response (Default); Air emulates the SSL 4K; Ice models the Neve V; and Fire stands in for the Focusrite.
- Preset Menu: To store your EQ settings as presets, click the Plus button positioned to the left of the Preset menu.
- Gain fader: Placed after the EQ stage, this fader lifts or trims the processed signal so as to offset the EQ changes you made.

### The EQ Graph

A visual picture of the current EQ settings is what the EQ graph delivers, with numbered "handles" for each active EQ band that you can drag any direction to alter the matching frequency and level. Your mouse wheel can additionally adjust each band's Q (bandwidth).

### The EQ graph

When you drag the numbered handles on this graph, you change the parameters of the matching band in turn, and the reverse holds too: altering a band's parameters also reshapes the EQ graph, which serves the extra role of giving a graphical picture of the equalization curve applied to that track. A mouse wheel, if you have one, can be used to control Q.

### Bands 1 and 6

These outermost two sets of band parameters handle the lowest or highest frequencies in an audio signal.
