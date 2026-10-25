# Voice dialogue and music processing

Version: DaVinci Resolve 20.3 Reference Manual. Context: Voice isolation studio version only, Dialogue leveler, Music remixer studio version only, Music editor studio version only, Dialogue separator track FX studio version only.
[Chapter index](INDEX.md) / [Previous section](voice-isolation-speed-effects-controls-in-the-viewer.md) / [Next section](dialogue-separator-track-fx-and-ducker-track-fx.md) / [Voice Isolation (Studio Version Only)](voice-isolation-speed-effects-controls-in-the-viewer.md)
<a id="source-dialogue-leveler"></a> <a id="source-dialogue-leveler-controls"></a> <a id="source-dialogue-separator-track-fx-studio-version-only"></a> <a id="source-music-editor-studio-version-only"></a> <a id="source-music-remixer-studio-version-only"></a> <a id="source-the-dialogue-leveler-plugin"></a> <a id="source-the-initial-music-is-too-long"></a> <a id="source-the-music-editor-in-the-audio-inspector"></a> <a id="source-the-music-remixer-plugin"></a> <a id="source-the-voice-isolation-plugin"></a>

### The Voice Isolation plugin

You can clear away all manner of background noise, whether it's air conditioners or fans, jackhammers, restaurant ambience, music playing under a featured line of dialogue, and beyond. The Amount control sets the blend between the original source and the isolated voice. At 50, the blend is roughly even. Settings between 70 and 80 deliver natural results while still isolating the source firmly. Even though Voice Isolation can run on an audio track in real time, it won't work on live audio input. It works on any mono, stereo, or dual-mono audio track, but tracks carrying more than two channels aren't supported.

### Dialogue Leveler

The Dialogue Leveler examines source material to find dialogue, then “rides down” the louder stretches, “lifts up” the softer ones, and pulls down background sounds that aren't dialogue. It does this without the usual “pumping” or other unwanted side effects that come with dynamics processors (compression/limiting), arriving at results akin to those you'd get from careful, manual clip gain tweaks or from “riding” a track via fader automation. Often the Dialogue Leveler can “fix and mix” a recording made on a single boom mic, where one character sits closer than another or turns away from the mic. The Dialog Leveler evens it out so that the original relative dynamics stay intact while intelligibility and average level both rise. Even though Dialogue Leveler can run on an audio track in real time, it won't work on live audio input. It works on any mono, stereo, or dual-mono audio track, but tracks carrying more than two channels aren't supported.

### The Dialogue Leveler plugin

### Dialogue Leveler controls

Dialogue Leveler: Turns the plugin on or off. Waveform Processing display: This presents a scrolling waveform alongside a gray line marking Dialogue Leveler processing. That said, the display goes missing whenever you reach for the Inspector's Dialogue Leveler to process timeline audio clips. Preset Menu: This menu hands you the following options:

- Allow wider dynamics: The default choice, and the strongest pick for audio whose dynamic spans a wide range from loud down to soft, with clip levels running medium to high.
- More lift for low levels: Reach for this option where the source carries more low-level dialogue you'd like to lift.
- Lift soft whispery sources: Reach for this option where the source holds whispered dialogue together with background noise.
- Optimize moderate levels: Reach for this option where the source sits at medium levels from start to finish.

Reduce Loud Dialogue: With this on, louder dialogue is ridden downward as it peaks, behaving like a “perfect limiter” where there's no threshold or time parameter for you to set. Thanks to the “near real-time” design, analysis happens ahead of audible playback for the best outcome. Lift Soft Dialogue: This setting locates and raises low-level dialogue, smoothing out material that is quieter yet more variable in level. Since the process zeroes in on dialogue, it tends not to push up background sounds unless they're audible at the same moment as the dialogue. The Lift Soft Dialogue option is frequently the handiest of the three, since it makes quieter dialogue lines louder and naturally smooth without lifting background noise. Background Reduction: This option softly removes background noise according to the internal preset chosen in the Preset menu. Output Gain: Reach for this control to set the output level, either by clicking and dragging or by typing a value into the numeric field. The Output Gain control ranges from 0.0 to +6.0 dB.

TIP: Ahead of running the Dialogue Leveler on a track, you may find it worthwhile to establish a solid baseline

level—suited to the default “Allow wider dynamics” preset—by normalizing the audio first.

To learn more about normalizing audio, consult Chapter 176, “The Fairlight Inspector.”

### Music Remixer (Studio Version Only)

This DaVinci Neural Engine AI-based plugin separates music into individual stems: Vocals, Drums, Bass, Guitar, and “Other” (“everything else”), so you can creatively rebalance or remix the track. The level controls let you set each stem's volume, and the Mute buttons let you drop stems out or bring them back into your mix. For instance, you might want to pull down or remove a vocal because it competes with a featured line of dialogue.

### The Music Remixer plugin

### Music Editor (Studio Version Only)

DaVinci Resolve 20 can seamlessly stretch or trim music to match the length of your edit. You'll reach the new AI powered Music Editor through the Inspector's Audio tab. Type in a desired duration and hit the Adjust button so the clip stretches or trims to fit it. NOTE: As an “intelligent edit,” Music Editor performs well on beat-driven music such as pop or dance. Free-form, ambient, or material lacking a beat falls outside what it's built for. Rather than using time compression/expansion or shifting the music's pitch, Music Editor borrows the techniques a music editor would use to fit material to a desired length against picture. It hunts for sensible spots to build transitions depending on whether you're lengthening (by repeating sections) or trimming material, and it tries to use the original composition's ending or fade when the timing lands well. Where the ending is abrupt, it's left to you to craft a fade out by hand.

### The Music Editor in the Audio Inspector

To Use Music Editor to retime a music clip: 1 On the timeline, pick the clip you intend to retime; bear in mind it has to be beat-driven music. 2 Within the Audio Inspector, beneath AI Music Editor, type in a fresh Target Length matching the music duration you're after. 3 Hit the Adjust button. 4 As another route, tick the Live Trim box so the Trim tools can resize the clip and retime the music on the timeline on the fly. Untick the checkbox to drop back into ordinary editing (trimming, say) for that clip once you've built the edit you wanted. Once the analysis finishes, four candidate edits open up at the bottom for you to choose among, each going about the edit a different way and numbered 1-4. Any editing you do afterward can happen almost instantly. The edited stretches of music carry indicators on the clip flagging where the cuts and transitions land.

### The initial music is too long

Here the Music Editor has retimed the audio clip so it lines up with the video's length. Notice the jagged lines along the audio clip flagging where the original got cut. Within the waveform, you can spot that the music's ending survives in the retimed clip.

TIP: Timings often land very close, yet now and then they won't be spot-on. Should you need precise timing once you're done with AI Music Editor, the Elastic Wave tool on the Fairlight page is worth a try—pick its general-purpose (music) algorithm.

The edited clip is in fact a specialized Music Editor clip, which lets you keep trimming your edit. If

you'd like to reach the underlying edit, you can also right-click the clip and decompose, which exposes

the edit points along with any crossfades that were created. Bear in mind, though, that once you've decomposed it, you can't

trim the clip's length as a single entity, since each editing snippet is now its own separate clip.

### Dialogue Separator Track FX (Studio Version Only)

Powered by DaVinci Neural Engine AI, Dialogue Separator hands you separate control over the level of the dialogue, the background sounds, and the reverberant field—or ambient room sound (“ambience”). Dialogue Separator earns its keep when, say, a source file has a wonderful roomy sound but carries music or crowd noise underneath. Here you can rebalance the audio to cut down the background sounds or shape the room sound to make the dialogue clearer. Another scenario: someone walks toward the camera in a roomy space while talking. Automation could then rebalance the audio so the ambient room sound steadily turns “drier” as they draw nearer, all without touching the background. For now, Dialogue Separator is a mono-only plugin. Where your source is stereo, you'll need to break it into dual-mono and process each mono track on its own.
