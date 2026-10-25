# Copying and pasting effect settings and effects in

Version: DaVinci Resolve 20.3 Reference Manual. Context: Mixing in the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](copying-and-pasting-effects.md) / [Next section](compressor-and-hard-and-soft-knee-graphs.md)
<a id="source-copying-and-pasting-effect-settings"></a> <a id="source-dynamics"></a> <a id="source-effects-in"></a> <a id="source-expandergate"></a> <a id="source-master-dynamics-controls"></a> <a id="source-the-channel-strip-dynamics-indicator"></a> <a id="source-the-dynamics-control-window"></a> <a id="source-the-dynamics-graph"></a>

### Copying and Pasting Effect Settings

When a single effect has settings you invested considerable time perfecting, and you realize the same settings might serve another track's effect equally well, you can copy and paste only those settings. Say a Reverb on a dialogue track has been tuned just right, and you notice those very settings would suit a different dialogue track elsewhere on your timeline. Instead of rebuilding the settings from scratch, you can clone them.

- Press and hold the option key while dragging the Reverb plugin you wish to clone to its new spot. Doing so produces a copy at the destination and keeps the source untouched.
- You may instead use Copy and Paste from the plugin's three dot Options menu. To carry those settings onto the other track, pick Copy from the source Reverb effect's Options menu, then bring up the target Reverb effect's Reverb plugin window, open its Options menu, and paste. Every parameter is now matched across both plugins.

For more information on using audio effects, see Chapter 180, "Audio Effects."

TIP: Whole channel-strip presets can be built and recalled, then reused across any project or timeline by way of the Fairlight > Presets Library.

### Effects In

With a single control, the Effects In button bypasses every Fairlight FX, AU, or VST effect plugin on a channel. Lit (orange) means all effects are active; unlit means all effects are bypassed. NOTE: The built-in Dynamics and EQ processors, along with Track FX (Voice Isolation with Resolve Studio and Dialogue Leveler), stay unaffected by Effects In.

### Dynamics

A built-in Dynamics processor sits on every Mixer channel strip, and a small Dynamics Indicator graph shown on the strip doubles as the button that opens it. Double-click that Dynamics Indicator to open the Dynamics processor window, which holds three modules: an Expander/Gate, a Compressor, and a Limiter. You can run each one on its own or combine them to shape the dynamics of the audio on the chosen track.

### The Dynamics control window

### The Dynamics Graph

As you switch on whichever combination of Dynamics window modules a track calls for, the Dynamics graph redraws with curves illustrating how the Expander/Gate, Compressor, and/or Limiter settings in use are shaping the signal. The Dynamics graph additionally gives you a live animated readout that meters the actual behavior of the input/output signals against the graphic showing the underlying response curve.

- The X axis (horizontal scale) represents the input signal level.
- The Y axis (vertical scale) represents the output level.
- The blue line represents the threshold.
- The light green line represents the dynamics curve (which depends on the process type and the setting;

this will shift).

- Animating across the top portion of the graph, the light green balls trace how the Dynamics control

settings shape the signal as it rises above or sinks below the threshold. Because the balls respond to the attack and release settings, they let you picture how the compressor is acting on the input signal.

- Along the input and output X-Y lines, smaller markers let you read precisely where the input/output levels sit.

In real time, the Dynamics graph shows the response curve and how the current settings are shaping the signal. That same curve appears on the channel strip's Dynamics Indicator, so a quick look tells you what is happening on the channel (minus the live animated display). You cannot adjust this indicator; open the Dynamics window when you need to make changes.

### The channel strip Dynamics Indicator

### Master Dynamics Controls

At the top of the Dynamics window you will find these overall controls:

- Enable button: Switches the overall dynamics effect on and off while leaving the controls untouched.

NOTE: Dynamics can also be toggled on and off with a single click on the Dynamics button (the mini graph) located on the channel strip.

- Reset button: Sitting at upper right beside the three dot Options menu, the circular reset icon returns every control in the Dynamics window to its default.
- Preset Menu: This is where Dynamics presets show up. Presets can be made, edited, and saved, and the supplied defaults work well as starting points tailored to what your track needs.
- Make Up Gain control: A level control placed after the dynamics stage, letting you raise the signal to offset any drop in overall level that the dynamics settings introduced.

### Expander/Gate

First among the three dynamics modules, the Expander/Gate controls toggle between expansion and gating. Expansion accentuates volume contrasts by pulling down the level of a signal's quiet passages relative to its loud ones, and it serves to suppress noise while widening a signal's dynamic range. Gating lowers the level of, or fully mutes, portions of a signal that drop beneath the chosen threshold so as to cut down or remove noise during the quiet stretches of a recording.

- Expander: This button enables the Expander.

Threshold: Defines the signal level beneath which expansion takes place; its default is –35 dB, adjustable across –50 to 0 dB. Range: How much the signal level drops, in dB, with both threshold and ratio influencing it. A higher ratio lets range exert more pull. With ratios on the low side, raising threshold strengthens what range does. Ratio: Establishes the attenuation ratio (input to output) put on signals dropping below the threshold level. While Range governs how far the signal falls, this governs how fast it falls; the default here is 1:1.1, spanning 1:1.1 up to 1:3.0. Attack: Controls how rapidly expansion kicks in once a signal passes the threshold; it defaults to 1.4 ms (milliseconds) and covers 0 to 100 ms. Hold: Determines, in ms, how long the Expander stays open once the input drops beneath the threshold; the default is 0 ms, with values from 0 to 4000 ms (4 seconds). Release: Sets how fast or slow the Expander attenuates as the input signal returns below the threshold; its default is 93 ms, spanning 50 to 4000 ms (4 seconds).

- Gate: This button enables the Gate.

Threshold: Defines the signal level beneath which gain reduction takes place, adjustable across –50 to 0 dB. Hold: Determines, in ms, the length of time the Gate remains open once the input drops beneath the threshold; it defaults to 0 ms and covers 0 to 4000 ms (4 seconds). Range: Establishes the largest amount of gain reduction applied as the signal drops below the gate threshold. No gain reduction occurs once the signal sinks under the level given by the gate threshold minus the gate range. Here the default is 18 dB, spanning 0 to 60.2 dB. Ratio: Unused for gate. Attack: Controls how rapidly gating engages once a signal passes the threshold; it defaults to 1.4 ms and covers 0 to 100 ms. Hold: Prevents dynamics from retriggering until a set interval, in ms (milliseconds), has elapsed; the default is 0 ms, with values from 0 to 4000 ms (4 seconds). Release: Sets how fast or slow the sidechain detector ceases attenuating as the input signal returns below the threshold; its default is 93 ms, spanning 50 to 4000 ms (4 seconds).
