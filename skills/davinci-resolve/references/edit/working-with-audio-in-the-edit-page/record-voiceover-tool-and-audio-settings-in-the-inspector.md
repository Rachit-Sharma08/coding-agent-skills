# Record voiceover tool and audio settings in the inspector

Version: DaVinci Resolve 20.3 Reference Manual. Context: Working with audio in the edit page.
[Chapter index](INDEX.md) / [Previous section](eliminating-subframe-audio-edits.md) / [Next section](voice-isolation-and-dialogue-leveler.md)
<a id="source-adjusting-audio-in-the-inspector"></a> <a id="source-adjusting-audio-in-the-timeline"></a> <a id="source-adjusting-volume-using-keyboard-shortcuts"></a> <a id="source-audio-settings-in-the-inspector"></a> <a id="source-keyframing-audio"></a> <a id="source-normalize-audio-volume-command"></a> <a id="source-record-voiceover-tool"></a> <a id="source-setting-volume"></a> <a id="source-showing-the-volume-overlay-in-the-curve-editor"></a> <a id="source-the-record-voiceover-tool"></a>

### Record Voiceover Tool

Come DaVinci Resolve 20, the Cut page and the Edit page alike can lay voiceovers straight onto a timeline track through a pared-down interface. When the job is serious, exacting ADR, Fairlight’s ADR toolset is the better fit, but for plain VO and scratch tracks the Record Voiceover tool is fast and handy.

### The Record Voiceover tool

You bring up the Record Voiceover tool by choosing Timeline > Record Voiceover, or by clicking the Voiceover icon (that little microphone) on the Timeline Toolbar. To Record Voiceover 1 File Name: Key in a meaningful file name for the new Voiceover file, or simply leave the default. 2 Audio Input: Point this at whichever audio interface on your computer holds your microphone. 3 Record Track: Name the timeline audio track your voiceover should land on. Alternatively pick Auto and let DaVinci Resolve decide from your current track layout. After that, set the playhead on the timeline at the spot the audio should begin. 4 Press the Record Icon to begin laying the recording straight onto the track. 5 Press the Record Icon a second time to halt it. As soon as recording stops, the playhead jumps back on its own to where it started, so you can either play the voiceover clip back in place or fire off a fresh take at once by clicking the Record Icon again. That fresh take overwrites the earlier clip on the track automatically. Every earlier take, however, remains on hand in the Media Pool.

Further options live in the Voiceover Tool’s 3-dot option menu. Input Monitoring: Switch this on and the microphone audio plays back as it records, though with a touch of lag. It gives the voiceover artist, or the audio engineer, a way to hear the audio as it is captured. Turning it on also brings a Mic Monitor Level slider into the main Voiceover tool, by which you govern how loud that playback sits in the headphones. Enable 3 Seconds Countdown: Switch this on and a silent three-second countdown shows in the timeline viewer ahead of recording, granting your talent a moment to ready themselves to speak. No audio beep accompanies this countdown — it is purely a visual cue. Mute Timeline Audio While Recording: Choose this and every audio track on the timeline is muted as you record, sparing you any other distracting sounds. To silence only some of the tracks, do it by hand with the mute buttons in the audio track timeline header. Stereo Input: Choose this and, with a stereo microphone in use, the capture goes to a stereo track rather than mono. Hide Options: Choose this and the File Name, Audio Input, and Record Track fields drop out of the Voiceover Tool, leaving just the Record icon to toggle. It comes in handy when you would rather your voiceover talent not stumble into your settings.

### Audio Settings in the Inspector

Every clip and every track carries a handful of audio-related parameters within the Inspector’s Audio panel. For finer detail on these controls, turn to Chapter 37, “Using the Inspector in the Edit Page.”

### Setting Volume

Every audio clip — or audio item, where a clip’s linked audio spans several tracks — holds its own Volume level. The upshot is that a multi-channel audio clip draws on one shared Volume setting. A few easy methods exist for adjusting these levels.

### Adjusting Audio in the Inspector

With one or more audio clips selected, each clip exposes its own Volume parameters in the Inspector’s Audio panel. Pick a single audio clip in the Timeline and tweak its volume and only that clip changes, which is how you set baseline levels for individual clips across your program. The Volume control acts on every channel inside that clip at the same moment.

The Volume parameter offered for audio clips within the Inspector Select several Timeline clips at once and dragging the Volume sliders or virtual sliders for the whole group applies a relative shift to them all, holding their offsets from one another intact. Should you instead want every clip brought to one level, a numeric adjustment drops all the selected clips to the same absolute level.

### Adjusting Audio in the Timeline

Every clip (or item) of audio on the Timeline wears a Volume overlay, and by dragging it up or down with the pointer you set that clip’s level. Hold the Shift key as you drag for more delicate moves. An Option-click on the level drops a keyframe right there so levels can shift dynamically. This overlay maps to the Inspector’s Volume parameter.

Dragging a Volume overlay to set the clip level Alternatively, click the Curve Editor button down in the audio clip’s bottom right-hand corner, which brings up the Audio Curve Editor. As of this writing, volume and pan are the only parameters this Curve Editor lets you edit.

### Showing the Volume overlay in the Curve Editor

### Adjusting Volume Using Keyboard Shortcuts

Keyboard shortcuts give you yet another way to set the volume of selected clips, and they work even as the Timeline plays. You can rig this up in a handful of ways.

- To adjust just one clip: Highlight it, then issue one of the volume-change commands.
- To adjust any clip at the position of the playhead: Switch on Timeline > Selection Follows Playhead

so that whatever clip the playhead crosses becomes the selected one, then issue a volume-change command. Where several clips meet the playhead, the chosen clip is the one riding the highest track.

- To adjust multiple clips all together: Highlight every clip you mean to change in one go, then issue a volume-change command. Where the clips you picked carry unequal Volume levels, those gaps are kept intact as you adjust.

Here are the commands that change volume. To move volume in steps of 1dB, do one of these:

- Clip > Audio > Increase Audio Level 1dB (Option-Command-Equals)
- Clip > Audio > Decrease Audio Level 1dB (Option-Command-Minus)

To move volume in steps of 3dB, do one of these:

- Clip > Audio > Increase Audio Level 3dB (Option-Shift-Equals)
- Clip > Audio > Decrease Audio Level 3dB (Option-Shift-Minus)

### Normalize Audio Volume Command

What the Normalize Audio Levels command does is drive clip levels automatically toward a stated target, and you get to pick the method by which each audio clip’s levels are analyzed to decide how its volume should be normalized. Among the choices are a range of loudness normalization algorithms keyed to assorted international standards, handy for evening out the perceived overall loudness of several clips against one another no matter the transient levels running through each. Peak normalization is also on the table, with both Sample Peak and True Peak on offer. The loudness choices set out to judge an audio signal by how loud it seems to the listener, which yields a truer automatic balancing of one clip’s audio levels against another’s, regardless of transient peaks cropping up here and there. For gauging maximum “true peak,” the target peak meter now follows the BS.1774 standard, meaning it can read “inter-sample peaks” instead of just the peaks at each waveform sample. You can still opt for Sample Peak, though — the older approach that measures the literal peak of the samples within a media file. Because the Normalize Audio Volume command only shifts volume and lays on no dynamics, the outcome is that the loudest stretches of each selected clip line up with one another at the target level. This command turns up on the Fairlight page as well.

To normalize one or more chosen audio clips: 1 Right-click any of the selected clips and pick Normalize Audio Levels. Up comes the Normalize Audio Level dialog.

The Normalize Dialog on the Edit page 2 Settle on the Normalization Mode you intend to use. The field is open to a range of standardized loudness measurement algorithms, plus Sample Peak and True Peak. 3 Settle on the reference level you want the selected clips’ peak volume to meet. 4 Decide how the level of several selected clips gets set: With Set Level on Relative, every selected clip is handled as though it were a single clip, so the loudest peak across them all sets the adjustment and each clip’s volume shifts by that same amount. This suits a run of clips — a dialog recording, say — whose levels already agree and which you wish to normalize as a group. With Set Level on Independent, each clip’s own peak level dictates that clip’s adjustment, so every selected clip moves by an amount peculiar to itself. The upshot can be a spread of wildly different volume shifts meant to bring each audio clip’s peak levels into line. This suits cases like balancing a batch of disparate sound effects whose starting levels are all over the map. For more on loudness normalization, turn to Chapter 182, “Audio Meters and Audio Monitoring.”

### Keyframing Audio

Audio can be keyframed two ways on the Edit page. One is each audio clip’s volume curve in the Timeline; the other is the Inspector’s keyframe controls, with which an individual clip’s Volume parameter gets animated the same way any other clip attribute would be — easing the level upward or downward, panning side to side from left, or dynamically reworking any of a whole host of filter controls, right down to subframe increments where the need arises. For more on keyframing within the Inspector, turn to Chapter 53, “Keyframing Effects in the Edit Page.” Whatever keyframes you lay down with the Inspector’s Keyframe controls show up automatically on that audio clip’s volume curve in the Timeline.
