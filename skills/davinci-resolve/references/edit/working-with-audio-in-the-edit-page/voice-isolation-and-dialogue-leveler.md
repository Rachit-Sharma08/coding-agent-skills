# Voice isolation and dialogue leveler

Version: DaVinci Resolve 20.3 Reference Manual. Context: Voice isolation studio version only, Dialogue leveler.
[Chapter index](INDEX.md) / [Previous section](record-voiceover-tool-and-audio-settings-in-the-inspector.md) / [Next section](dialogue-leveler-and-music-remixer-and-music-editor.md)
<a id="source-audio-crossfades"></a> <a id="source-audio-fade-handles"></a> <a id="source-dialogue-leveler"></a> <a id="source-how-to-add-and-adjust-volume-keyframes"></a> <a id="source-overlay-controls-for-volume"></a> <a id="source-the-voice-isolation-plugin"></a> <a id="source-voice-isolation-studio-version-only"></a>

### Overlay Controls for Volume

Every audio clip on the Timeline carries a Volume overlay control sitting atop it, one that begins perfectly flat by default. As with comparable controls in other applications, this level curve lets you reshape a clip’s levels — either wholesale or dynamically by way of keyframes.

Volume curves shaping the level of a clip’s audio on the Timeline Beyond that, clicking a clip’s Audio Curve Editor button, tucked into the bottom right-hand corner of each audio clip, opens an audio-specific Curve Editor where volume can likewise be keyframed.

The button for opening an audio clip’s Curve Editor

### How to Add and Adjust Volume Keyframes

Mixing audio by placing and tweaking individual keyframes can be a quick, effective route to balancing clip levels against each other, ironing out level trouble inside a single clip, or even building modest mixes (though the Fairlight page’s mixing power runs far deeper). Whenever you edit any audio parameter curve by hand, the procedures below apply. Ways to place or select audio keyframes with the pointer:

- To add keyframes to the Volume curve: With the Option key held, click the curve to drop a keyframe at that frame. At least two keyframes are required before any automated Volume change can occur.
- To select one or more keyframes: A click on any keyframe selects it.
- To select multiple discontiguous keyframes: Command-click every keyframe you want, whether or not they sit side by side.
- To select multiple contiguous keyframes: Click the first keyframe in the run, then shift-click the last one, and everything between them is selected too.

Ways to adjust keyframes in the Volume overlay (or curve) with the pointer:

- To adjust any curve segment: For a clip with no keyframes, rest the pointer over the segment as a whole; otherwise rest it between any two keyframes, squarely on the stretch of curve you mean to raise or lower. Once the Move cursor shows, drag upward to lift the volume or downward to cut it.
- To adjust a keyframe in any direction: Bring the pointer onto a keyframe until the fourway cursor surfaces, then drag up or down to alter the volume, or side to side to alter its timing. Audio keyframe timing can be set in subframe increments for precision mixing.
- To adjust a keyframe in only one direction: Bring the pointer onto a keyframe until the fourway cursor surfaces, hold Shift, and drag along the direction you intend — vertically to change that frame’s clip volume, or horizontally to slide the keyframe to a fresh point in time. The moment you begin dragging a keyframe one way, its movement stays locked to that axis until you let go. Audio keyframe timing can be set in subframe increments for precision mixing.
- To turn a Linear keyframe (or several) into Ease In or Ease Out: An eased keyframe makes animated changes that start off slowly and build to full speed, or wind down gradually to a halt. This only takes effect once two or more keyframes form an animated effect. Highlight one or more keyframes, then right-click one of them and pick Ease In, Ease Out, or Ease In and Out, according to which keyframe you are editing and the effect you are after.
- To revert an eased keyframe (or several) back to Linear: Highlight one or more keyframes, then right-click one of them and pick Linear.

Methods of Cutting, Copying, Pasting, and Deleting keyframes:

- To cut or copy, and paste one or more keyframes: Highlight the keyframes, then hit the Cut (Command-X) or Copy (Command-C) shortcut. Next, park the playhead where the first copied keyframe should begin and hit Paste (Command-V).
- To delete one or more control points from a curve: Highlight the keyframe(s) you intend to remove and hit Backspace.

### Audio Fade Handles

Rest the pointer squarely over an audio clip and a pair of Audio Fade handles surface at the In and Out points. Drag either handle in toward the middle of the clip and you fade the clip volume up at its head and fade it down at its tail.

Audio Fade handles at either end of an audio clip

NOTE: Bringing in a Final Cut Pro X project carries each clip’s fade handles across automatically too. Where a precise transition calls for it, Audio Fade Handles can also be set in subframe increments.

Tuning an Audio Fade handle by subframe increments, viewed inside the shadow cast by a single frame of the playhead

Adjusting the curve of the fade Both the Edit and Fairlight pages let you build and refine fade effects.

With a fade effect in place, you reshape its curve by dragging the handle perched right over the fader curve. Drag that handle up or down to change the curve’s angle, and drag it left or right to change the curve’s shape. By this means, every sort of fade effect is within reach.

### Audio Crossfades

Pick an edit point that holds both video and audio, with Linked Selection on so the video and audio edit points are both caught, and applying a video transition to that edit drops a crossfade onto the audio as well. Cross Fade transitions can be added to any edit point between two audio clips bearing enough handles, much as video transitions are added — drag one out of the Effects Library and drop it, right-click an edit to pick an option from its contextual menu, or highlight an audio edit point and reach for Timeline > Add Audio Only Transition (Shift-T). A Cross Fade transition is a fast, painless way to ease the outgoing clip’s volume down while the incoming clip’s volume climbs up at the same time, giving you a smooth aural handoff between the two audio clips. For precision work, a crossfade’s start and end points can be edited in sub-frame increments.

An audio Cross Fade transition applied between two clips

Double-click a Cross Fade transition to load it into the Inspector, which lays bare these parameters:

- Duration: How long the transition runs, given in both seconds and frames.
- Alignment: A drop-down for choosing where the transition sits relative to the edit point it is

attached to. The options are “End on Edit,” “Center on Edit,” and “Begin on Edit.”

- Transition style: Pick –3dB, 0dB, or +3dB to lock the Fade In and Fade Out levels

both to a single value. To grasp what these levels signify, see the parameter just below.

- Fade In/Fade Out levels: Three options act on the incoming and outgoing halves of

the Cross Fade effect on their own. 0dB lays on a linear fade (the default). +3dB lays on a boosted curve; applied to both Fade In and Fade Out, it can make up for sagging levels in the heart of a Cross Fade. –3dB lays on an attenuating curve that intentionally drops the Cross Fade’s level. Crossfades can be built and refined on both the Edit and Fairlight pages. TIP: For an asymmetrical crossfade, you “checkerboard” clips across two tracks with overlapping handles at head and tail, then work the Fader handles to dial in precisely the timing and curves the effect demands.

### Voice Isolation (Studio Version Only)

Voice Isolation draws on an AI model trained across every sort of human voice — male or female, young or old — which lets you strip loud, unwanted sounds out of existing voice recordings to striking effect. Background noise of all kinds can be banished, from air conditioners and fans to jackhammers, restaurant clatter, music bleeding under a featured line of dialogue, and beyond. The Amount control balances the blend between the untouched source and the isolated voice. Set to 50, that blend sits roughly even. Settings from 70 to 80 tend to give natural results while still isolating the source hard. Voice Isolation will run on an audio track in real time, yet it will not work on live audio input. Any mono, stereo, or dual-mono audio track can take it, but tracks carrying more than two channels are not supported.

### The Voice Isolation plugin

### Dialogue Leveler

The Dialogue Leveler studies the source material to spot dialogue, then “rides down” the louder stretches, “lifts up” the softer ones, and pulls down background sounds that are not dialogue. It manages this free of the usual “pumping” and other unwanted artifacts of dynamics processors (compression/limiting), turning out results on par with painstaking, by-hand clip gain moves or “riding” the track via fader automation.
