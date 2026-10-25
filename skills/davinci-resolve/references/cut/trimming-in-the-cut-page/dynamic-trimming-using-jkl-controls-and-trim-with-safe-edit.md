# Dynamic trimming using jkl controls and trim with safe edit

Version: DaVinci Resolve 20.3 Reference Manual. Context: Trimming in the cut page.
[Chapter index](INDEX.md) / [Previous section](trimming-edits-in-the-viewer.md)
<a id="source-dynamic-trimming-using-jkl-controls"></a> <a id="source-trim-with-safe-edit"></a>

### Dynamic Trimming Using JKL Controls

The Cut page has picked up the Edit page’s Dynamic Trim mode, driven by the keyboard’s JKL controls, to make keyboard-based trimming fast. In Dynamic Trim mode you resize whatever edit points and clips you’ve selected by way of the JKL transport-control shortcuts. Put differently, you set up the right selection in the Timeline and then trim it as it plays, keeping an ear on the audio and an eye on the video the whole time. Trimming as the chosen clip or edit point rolls by lets you become emotionally invested in what’s on screen and feel a clip’s timing as it runs — both of which sharpen your sense of exactly how a given cut needs trimming. Throughout dynamic trimming, the same two-up display, the same Timeline overlays, and the same live-updating timeline you’d get from the mouse-driven Trim tool are all present. What sets it apart is simply that the trimming happens while your program is playing.

(Top) The Dynamic Trim icon in the Timeline toolbar

(Left) A yellow playhead is your cue that Dynamic Trim mode is on. The green highlight signals that only the first clip’s Out point is live. Tapping the keyboard’s JKL keys then nudges that edit point ahead or back. Here’s how to put Dynamic Trim mode to work on one or more selected clips or edits: 1 On the timeline, select the edit point or points you mean to trim. Skip that and the edit nearest the smart indictor gets picked for trimming. 2 Hit W to drop into Dynamic mode, or go through Trim > Dynamic Trim Mode and click the Dynamic Trim tool on the toolbar. As soon as Dynamic Trim mode is active, the playhead tool goes yellow as a standing reminder that trimming clips is the only thing this mode permits. 3 Right-click the toolbar’s Dynamic Trim tool to pick which Dynamic Trim mode you want. Slip: Leaves a clip parked where it is on the Timeline while swapping out the stretch of media shown there. A Slip edit leaves the whole Timeline’s duration untouched. Slide: Holds a clip’s media range fixed but slides the clip left or right, trimming the outgoing clip on its left as it grows the incoming clip on its right, or the reverse. 4 Green highlighting on the edit point marks which clip edges are queued for trimming. Tap U to cycle through the edit point types on offer, or go to Trim > Edit Point Type. 5 Reach for any mix of the JKL keyboard shortcuts to kick off playback and trimming, such as:

- J+K or K+L to trim at a slow-motion pace, complete with slow-motion audio
- Holding K while tapping J or L to step the trim one frame at a time
- A press of J or L to trim at real-time playback speed
- Repeated presses of J or L to trim in fast-reverse or fast-forward across an assortment of speeds

6 During dynamic trimming, every audio clip on every audio track sounds out as the playhead sweeps over it, letting you take in your whole mix while you trim. 7 Once a trim is in, a press of the Spacebar fires off Play Around Current Selection so you can judge how the trim sits. Within Dynamic Trim mode the Spacebar does nothing but a Play Around Current Selection pass — it won’t roll forward the way it normally would.

8 When you’re done, the Up and Down Arrow keys carry both the selection and the playhead to another edit point or clip you fancy trimming, or a second press of W flips Dynamic Trim mode off. Make a habit of switching Dynamic mode off (W) once finished; leave it on and the JKL keys will keep trimming whatever edits or clips are selected rather than playing the Timeline.

### Trim with Safe Edit

Cutting on the Cut Page timeline can get quick and frantic, so to keep from clobbering a neighboring clip by accident while you trim, switch on “Trim with Safe Edit” among the timeline options.

Within the Timeline options, enabling Trim with Safe Edit guards against accidental overshoots. With the mode on, you trim and stretch an edit point just as usual right up until it runs into another clip. The moment the trim cursor hits the next clip’s edge, it halts the trim and places a small timer on the cursor instead of barreling ahead with the overwrite. Should you genuinely intend to overwrite the neighboring clip, keep dragging with the mouse or spin the Speed Editor dial to push past the timer and let the trim overwrite that adjacent clip.

The Safe Edit cursor holding you back from overwriting the next clip; keep dragging the clip if you want the overwrite to happen anyway.
