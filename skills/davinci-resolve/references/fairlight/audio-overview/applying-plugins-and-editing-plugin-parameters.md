# Applying plugins and editing plugin parameters

Version: DaVinci Resolve 20.3 Reference Manual. Context: Audio overview.
[Chapter index](INDEX.md) / [Previous section](group-menu-on-a-mixer-channel-strip-and-audio-effects.md) / [Next section](bus-audio-plugins-and-processor-load.md)
<a id="source-applying-plugins"></a> <a id="source-editing-plugin-parameters"></a> <a id="source-sidechain-controls"></a> <a id="source-sidechaining"></a> <a id="source-to-use-sidechaining"></a> <a id="source-working-with-plugins-in-the-inspector"></a>

### Applying Plugins

Methods of applying audio plugins to clips on the Fairlight page:

- Putting an audio effect on a clip: From the Audio FX panel of the Effects Library, drag any effect onto whichever Timeline clip you want it on.
- Putting an audio effect on several clips: Highlight every clip you want the audio effect on, then drag any effect out of the Audio FX panel of the Effects Library onto any one of the highlighted clips. Once a plugin lands on a clip, a badge shows up to the left of that clip's name bar in the Timeline, signaling that an effect is on it.

A badge marks Timeline clips that carry applied audio plugins. Ways to apply audio plugins to tracks on the Fairlight page:

- Putting an audio effect on a whole track in the Timeline: Drag any effect from the Effects Library straight onto the track header.

Applying an audio effect to a whole track via the Timeline

- Putting an audio effect on a track or bus in the Mixer: From the Audio FX panel of the Effects Library, drag any effect onto whichever Timeline clip you want it on.

Adding an audio effect across an entire track by dragging and dropping onto the Mixer

- Putting an audio effect on a track or bus through the Mixer controls: Click the plus button on the channel strip of the track you're effecting, then pick an effect from the dropdown menu that opens. Every filter sits within categories so they're easier to track down. If you've starred any filters in the Effects Library as favorites, those favorite filters land at the top of the plus button's dropdown list.
- Copying audio effects from one mixer channel onto another: Hold the Option key while you click and drag the effect to the channel and slot you want it copied to.
- Reordering audio effects within the Mixer: Click and drag the audio effect over to whatever slot position you want.

Adding an audio effect across a whole track using the Mixer's built-in controls TIP: The categories that VST and Audio Units effects fall under inside the Mixer are editable over in the Audio Plugins panel of the DaVinci Resolve System Preferences window. Each plugin on a workstation lists in the Available Plugins list, and a click within the Category column gives you a dropdown menu for changing categories.

NOTE: This does not apply to Fairlight FX plugins.

### Editing Plugin Parameters

To edit a clip’s audio plugins:

- Select that clip and open the Inspector. Every audio plugin applied to that clip turns up in the Effects tab, with that effect's controls showing directly in the Inspector.

To edit a track’s audio plugins, do one of the following:

- Click an empty spot in the Timeline header to select that track, then open the Inspector. Click that effect's custom UI button to bring up its controls.

The custom UI button for audio plugins in the Inspector

- Hover the pointer over the plugin's name in the Mixer's Effects area, then click the custom UI button to bring up its controls.

The custom UI button for audio plugins in the Mixer Almost every Fairlight FX, VST, and Audio Unit audio plugin carries a custom user interface that makes handling that effect's controls far easier. These can be opened from inside DaVinci Resolve.

The custom audio effect interface for iZotope RX Voice De-noise

### Working with Plugins in the Inspector

Methods of working with audio plugins in the Inspector:

- Reordering several audio effects on a clip: Reach for the move up or move down buttons sitting in an effect's title bar, just left of that effect's Trash Can button.
- Switching an effect off or back on: Click the toggle button sitting at the far left of each effect's title bar.
- Getting rid of an effect: Click the Trash Can button.
- Resetting any effect parameter: Click the Reset button over at the far right of whichever parameter you're resetting.
- Expanding or collapsing one effect's parameters: Double-click the title bar.
- Expanding or collapsing the parameters of every effect: Hold down the Option key and double-click any effect's title bar.

Once you've put them on a clip or track, audio plugins can also be keyframed or automated exactly like volume and pan settings, to build dynamic audio effects that shift over time.

### Sidechaining

DaVinci Resolve supports sidechaining for compatible Fairlight FX, AU, and VST plugins, which lets you momentarily pull down a target track or bus's level by way of the audible signal off a source track or bus. Known too as “ducking,” the technique earns its keep when multiple tracks jostle for space in a mix because they share part or all of the same frequencies—say, a track or bus holding dialogue next to a bus where a crowd cheers at a sports event. Above, the dialogue is routed into the sidechain input of a compatible dynamics plugin (a compressor or limiter, in other words) on the crowd-noise Mixer channel. With the dynamics controls set up right, the Dialogue channel's voices gently and modestly drop, or attenuate, the crowd noise's level, so the voices stand out more sharply in the mix. As soon as the dialogue stops, the cheering rises back to where it started.

### Sidechain controls

### To use sidechaining

- Bring up the compressor or limiter on the Mixer channel carrying the crowd noise.
- Pick the Dialogue channel from the source dropdown up top in the plugin,

just right of the Listen button. That's the audio you're leaning on to attenuate the cheering crowd's level. Choosing a bus as the ducking source lets several sources drive the changes in your target track.

- Click the On button—it goes red—signaling that the Sidechain (S/C) function is now active.
- Adjust the controls to taste as your mix plays, keeping the effect natural-sounding throughout. Feel free to experiment with the Channel Dynamics plugin's Compressor section, or with the Fairlight FX Limiter.

To dig deeper into sidechaining via the Channel Dynamics plugin, turn to Chapter 177, “Mixing in the Fairlight Page.” To dig deeper into sidechaining via the Fairlight FX Limiter, turn to Chapter 181, “Fairlight FX.”

- A click on the Listen button lets you monitor the incoming signal whenever you need to verify that the right input signal is reaching the Limiter. The button glows yellow while active.
