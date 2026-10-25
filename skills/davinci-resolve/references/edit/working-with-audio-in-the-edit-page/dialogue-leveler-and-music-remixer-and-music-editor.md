# Dialogue leveler and music remixer and music editor

Version: DaVinci Resolve 20.3 Reference Manual. Context: Dialogue leveler, Music remixer studio version only, Music editor studio version only.
[Chapter index](INDEX.md) / [Previous section](voice-isolation-and-dialogue-leveler.md) / [Dialogue Leveler](voice-isolation-and-dialogue-leveler.md) / [Next section](dialogue-separator-track-fx-and-ducker-track-fx.md)
<a id="source-music-editor-studio-version-only"></a> <a id="source-music-remixer-studio-version-only"></a> <a id="source-the-dialogue-leveler-plugin"></a> <a id="source-the-music-editor-in-the-audio-inspector"></a> <a id="source-the-music-remixer-plugin"></a> <a id="source-working-with-audio-in-the-edit-page-part-3"></a>

### The Dialogue Leveler plugin

Time and again the Dialogue Leveler can “fix and mix” a recording cut with one boom mic — where a character stands nearer than the others or swings away from the mic — evening it out so the original relative dynamics survive even as intelligibility and average level rise. The Dialogue Leveler will run on an audio track in real time, yet it will not work on live audio input. Any mono, stereo, or dual-mono audio track can take it, but tracks carrying more than two channels are not supported. Dialogue Leveler controls:

- Dialogue Leveler: Enables or disables the plugin.
- Waveform Processing display: Here a scrolling waveform plays out, with a gray line marking Dialogue Leveler processing. That display is absent, though, when you reach for the Dialogue Leveler in the Inspector to treat audio clips on the timeline.
- Preset Menu: The options this menu hands you are:

Allow wider dynamics: The default, and the right pick for audio whose dynamic ranges widely from loud to soft and whose clip levels run medium to high. More lift for low levels: Reach for this when the source holds more low-level dialogue you wish to lift. Lift soft whispery sources: Reach for this when the source carries whispered dialogue alongside background noise. Optimize moderate levels: Reach for this when the source sits at medium levels from end to end.

- Reduce Loud Dialogue: Switched on, louder dialogue gets ridden down whenever it peaks, behaving like a “perfect limiter” that asks no fiddling with threshold or time parameters. Thanks to the “near real-time” design, the analysis runs ahead of audible playback so the results come out at their best.
- Lift Soft Dialogue: This control hunts out low-level dialogue and raises it, smoothing material that is quieter and more uneven in level. Since the work centers on dialogue, it rarely lifts background sounds unless they happen to sound at the very same moment as the dialogue.

Of the three, the Lift Soft Dialogue option is frequently the handiest, since it brings quieter lines of dialogue up and renders them naturally smooth while leaving background noise unboosted.

- Background Reduction: Working off whichever internal preset is chosen in the Preset menu, this option eases background noise away gently.
- Output Gain: With this control you set the output level, either by clicking and dragging it or by typing a figure into the numeric field. The Output Gain control spans 0.0 to +6.0 dB.

TIP: Ahead of running the Dialogue Leveler on a track, it pays to establish an ideal baseline level for the default “Allow wider dynamics” preset by normalizing the audio first.

For more on normalizing audio, turn to Chapter 176, “The Fairlight Inspector.”

### Music Remixer (Studio Version Only)

Built on the DaVinci Neural Engine, this AI plugin breaks music apart into separate stems — Vocals, Drums, Bass, Guitar, and “Other” (“everything else”) — so you can creatively rebalance or remix the track. The level controls let you set each stem’s volume, while the Mute buttons pull stems out of your mix or bring them back. You might, for one, drop or duck a vocal because it fights with a featured line of dialogue.

### The Music Remixer plugin

### Music Editor (Studio Version Only)

DaVinci Resolve 20 can lengthen or trim music to match your edit without any visible seams. You will find the new AI-driven Music Editor under the inspector’s audio tab. Type in the duration you want and hit the Adjust button to grow or shrink the clip to that length. NOTE: The Music Editor is an “intelligent edit” that performs well on beat-driven music (pop, dance, and so on). It is not meant for free-form, ambient, or non-beat material. Rather than relying on time compression/expansion or any pitch change, the Music Editor borrows the moves a human music editor would, cutting the material to fit the length your picture needs. It hunts for sensible spots to place transitions according to whether you are lengthening (by repeating sections) or cutting material, and tries to use the original composition’s ending or fade when the timing lines up. Should the ending land abruptly, building a fade out is left to you.

### The Music Editor in the Audio Inspector

To Use Music Editor to retime a music clip: 1 On the timeline, pick the clip you intend to retime; the material must be beat-driven music. 2 Within the Audio Inspector, beneath AI Music Editor, type the new Target Length matching the music duration you're after. 3 Click the Adjust button. 4 As another route, tick the Live Trim box so the Trim tools can resize the clip and retime the music live on the timeline. Clear that checkbox to go back to ordinary editing (such as trimming) for the clip once you've built the edit you wanted. When the analysis finishes, four candidate edits become available along the bottom, numbered 1-4, each taking a distinct approach. From there, further editing happens nearly instantly. Markers along the edited music identify the spots at which cuts and transitions land.
