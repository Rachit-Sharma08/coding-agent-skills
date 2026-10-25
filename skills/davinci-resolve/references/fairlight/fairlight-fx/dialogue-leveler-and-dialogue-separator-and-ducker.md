# Dialogue leveler and dialogue separator and ducker

Version: DaVinci Resolve 20.3 Reference Manual. Context: Dialogue leveler, Dialogue separator studio version only, Ducker.
[Chapter index](INDEX.md) / [Next section](ducking-music-voice-and-audio-chain-effects.md)
<a id="source-automation-activated-and-available-to-the-fairlight-fx"></a> <a id="source-common-controls-for-all-fairlight-fx"></a> <a id="source-common-controls-for-all-fairlight-fx-1"></a> <a id="source-dialogue-leveler"></a> <a id="source-dialogue-separator-studio-version-only"></a> <a id="source-ducker"></a> <a id="source-fairlight-fx"></a> <a id="source-fairlight-fx-part-1"></a> <a id="source-the-dialogue-leveler-plugin"></a> <a id="source-the-dialogue-separator-plugin"></a> <a id="source-the-mixer-menu"></a> <a id="source-track-fx"></a>

### Fairlight FX

Fairlight FX are audio plugins built specifically for DaVinci Resolve; they run natively across macOS, Windows, and Linux and bring high-quality audio effects with professional features to every DaVinci Resolve user. You will find these plugins on both the Edit and the Fairlight pages, where they hand you a range of options for mending broken audio, building effects, and conjuring spaces. Over on the Fairlight page they fall into one of two groups — Track FX or Audio Effects — according to where they sit in the Fairlight Mixer’s signal path.

To dig deeper into the Fairlight Mixer’s signal path, turn to Chapter 177, “Mixing in the Fairlight Page.” The pages here lay out what these plugins do and how you put them to use.

### Common Controls For All Fairlight FX

Ahead of the controls unique to each Fairlight FX plugin, a handful of controls are shared by every plugin, sitting along the top of each plugin’s custom GUI window.

### Common controls for all Fairlight FX

- Presets: A grouping of controls through which you save and call back presets tied to each individual plugin.

Add Preset button: Press this to store the present settings of the Fairlight FX in use. A dialog box prompts you for a Preset name, after which you click OK. Preset dropdown menu: Every preset belonging to the plugin you have open shows up in this menu. Previous/Next preset buttons: With these you step through presets one at a time, moving up and down the list as you weigh how each sounds.

- A/B Comparison: A group of buttons for weighing two differently tuned takes on the same plugin against each other. The A and B buttons let you keep two distinct sets of adjustments for that plugin and flip between them to hear which sounds better. The arrow button copies the adjustments from one button onto the other, preserving the take you prefer while you go on tinkering.
- Reset: One reset control returns every parameter of the current plugin to its default. With Automation switched on, an automation button shows at the upper right of each plugin, and that effect’s automatable parameters become available through the Plugin dropdown menu for that track.

### Automation activated and available to the Fairlight FX

NOTE: Default may be the preset that loads at first, yet a good number of the plugins ship with presets already in place. Reverb, for one, comes with Cathedral, Concert Hall, and Studio presets built in. These make fine jumping-off points that you can alter, rename, and save to fit your own needs, and any such new presets also turn up in the Preset dropdown menu. TIP: Fairlight FX allow “granular” control tweaks: hold the Option or Shift key while you click into and drag left or right across the numerical value fields of the virtual sliders, whether in a Fairlight FX plugin or the Inspector.

### Track FX

You get at these built-in Fairlight FX plugins through the Track FX section of Audio Track channel strips, or from the Inspector. Should the Track FX section be missing from the Mixer, click the three dots at the Mixer’s upper-right corner and pick Track FX. This category holds the following plugins: Voice Isolation, Dialogue Leveler, Dialogue Separator, Music Remixer, and Ducker. Every one of them sits at a fixed, dedicated insert point within the Track FX section, with Voice Isolation and Dialogue Leveler shown by default. To surface the rest, click those three dots at the Mixer’s upper-right corner and choose each plugin from the “Visible Track FX” submenu down at the bottom. TIP: Track effects will work on stereo-linked groups (stereo-linked tracks).

### The Mixer menu

### Dialogue Leveler

The Dialogue Leveler studies the source material to pick out dialogue, then “rides down” the louder passages, “lifts up” the quieter ones, and pulls down background sounds that are not dialogue. It does this free of the usual “pumping” and other unwelcome artifacts of dynamics processors (compression/limiting), arriving at results like what you would get from painstaking, hand-tuned clip gain moves or from “riding” the track with fader automation.

Often the Dialogue Leveler can “fix and mix” a take captured on a lone boom mic — one where a character sits nearer than another or swings away from the mic — smoothing it so the original relative dynamics survive even as intelligibility and average level climb.

### The Dialogue Leveler plugin

While the Dialogue Leveler runs on an audio track in real time, it will not operate on live audio input. Any mono, stereo, or dual-mono audio track is fair game, yet tracks carrying more than two channels are not supported. Dialogue Leveler controls:

- Dialogue Leveler: Enables or disables the plugin.
- Waveform Processing display: Here you see a scrolling waveform alongside a gray line that marks Dialogue Leveler processing. This display, however, does not appear when you reach for the Dialogue Leveler in the Inspector to treat audio clips on the timeline.
- Preset Menu: The choices this menu offers are these: Allow wider dynamics: The default, suited best to audio whose dynamic swings broadly from loud to soft and whose clip levels run medium to high.

More lift for low levels: Pick this when the source carries a lot of low-level dialogue you would like raised. Lift soft whispery sources: Pick this when the source holds whispered dialogue together with background noise. Optimize moderate levels: Pick this when the source stays at medium levels all the way through.

- Reduce Loud Dialogue: Switch this on and the louder dialogue gets ridden down at its peaks, behaving like a “perfect limiter” with no threshold or time parameters for you to set. Thanks to the “near real-time” design, the analysis runs ahead of the audible playback for the best outcome.
- Lift Soft Dialogue: This control locates and raises low-level dialogue, smoothing out material that runs quieter and more uneven in level. Since the work is centered on dialogue, it tends to leave background sounds alone unless they happen to sound at the same moment as the dialogue.

Of the three, Lift Soft Dialogue tends to prove the handiest, since it brings quieter lines of dialogue up and renders them naturally smooth while leaving background noise untouched.

- Background Reduction: Working from whichever internal preset you picked in the Preset menu, this option eases background noise away gently.
- Output Gain: Set the output level with this control either by clicking and dragging it or by typing a figure into the numeric field. Its Output Gain range spans 0.0 to +6.0 dB.

TIP: Ahead of running the Dialogue Leveler on a track, it pays to normalize the audio so you have an ideal baseline level for the default “Allow wider dynamics” preset. For more on normalizing audio, see Chapter 176, “The Fairlight Inspector.”

### Dialogue Separator (Studio Version Only)

Drawing on DaVinci Neural Engine AI, Dialogue Separator hands you separate command over the level of the dialogue, the background sounds, and the reverberant field or ambient room sound (“ambience”).

### The Dialogue Separator plugin

The Dialogue Separator shines when, for instance, a source file boasts a lovely roomy sound yet has music or crowd noise lurking behind it. Here you can rebalance the audio to dial the background sounds back, or tweak the room sound so the dialogue reads more clearly. Another scenario: someone walks toward the camera in a roomy space while talking. You might lean on automation to rebalance the audio so the ambient room sound grows steadily “drier” as they near, all while the background stays put. For now the Dialogue Separator handles mono only. A stereo source has to be split into dual-mono, with each mono track treated on its own.

### Ducker

With this plugin you take the audible signal off one track or several and use it to pull down the level of another. Creative uses abound, but the classic “ducking” move is to automatically drop a music or sound effects bed so dialogue or a VO track sits more clearly out front in the mix — and it does so without compressing the incoming signals. Dial the Ducker interface in correctly, or work through the Inspector’s Audio tab, and your audio tracks come close to “mixing themselves.” In a plain case, the Ducker reads the level swings of one incoming dialogue or VO track to turn down the sound effects bed of a noisy freeway. In a trickier one — a scene where three characters chat beside that same noisy freeway — a lone Ducker plugin can take each dialogue track’s level swings and use them to tame the traffic noise. Fed by only a single input source (Dialogue 1), the Ducker would respond solely when the first character talks. This new feature, though, lets you bring the other two dialogue tracks (Dialogue 2 and Dialogue 3) on board as input sources for knocking the traffic noise back.
