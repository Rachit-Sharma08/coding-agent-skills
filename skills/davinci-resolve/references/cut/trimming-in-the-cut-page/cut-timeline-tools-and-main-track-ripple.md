# Tools that help you work in the timeline and ripple on main track option to disable ripple trims

Version: DaVinci Resolve 20.3 Reference Manual. Context: Trimming in the cut page.
[Chapter index](INDEX.md) / [Next section](cut-timeline-markers-and-selection.md)
<a id="source-audio-trim-view"></a> <a id="source-fixed-or-free-playhead"></a> <a id="source-locking-muting-and-disabling-tracks"></a> <a id="source-ripple-on-main-track-option-to-disable-ripple-trims"></a> <a id="source-snapping"></a> <a id="source-timeline-markers"></a> <a id="source-tools-that-help-you-work-in-the-timeline"></a> <a id="source-trimming-in-the-cut-page"></a> <a id="source-trimming-in-the-cut-page-part-1"></a>

### Trimming in the Cut Page

After you've strung a series of clips into a roughly edited timeline, the Cut page gives you many ways to reshape them within the Timeline. CUT The point of these tools is to tighten your program's pacing by refining how each clip is timed, along with the edits dividing them. The goal is to keep adjustments like these effortless, so your program reads clearly and plays back with timing that feels right. Reworking the edits within a timeline this way goes by the name “trimming.”

### Tools That Help You Work in the Timeline

As you set about trimming clips within the Timeline, a row of buttons up at the Timeline's top left assists you in aligning clips and keeping tabs on key frames as you go.

### Ripple on Main Track Option to Disable Ripple Trims

While trimming the main track (track 1) on the Cut page, you're able to switch off the automatic rippling of that track's clips. That gives you the choice of making simple trim adjustments while leaving the Timeline's other clips from shifting up and down the Timeline.

To Enable or Disable Rippling on a Cut Page Timeline:

- Click the Timeline Options icon and pick Ripple On in the contextual menu, or click

straight on the Ripple On icon at the left of the Timeline ruler. Click once more to toggle Rippling

on or off.

- You can instead hold the Option key down while you trim with the mouse on the main

track to suspend rippling for the moment.

The Ripple On control toggles r ippling on the main track.

### Fixed or Free Playhead

You get to decide whether the Cut timeline keeps its default fixed playhead (the video runs beneath the playhead), or instead lets it travel along with the video (the playhead runs over the video). Pick the mode by clicking the Timeline Options icon and ticking or clearing Fixed Playhead,

- With it ticked, the playhead stays pinned at the Timeline's center; your edited clips glide past it whenever you play (press the Spacebar), jog, or shuttle (the JKL keys) in any direction. Locked mode pairs beautifully with the DaVinci Resolve Editor Keyboard, since the Timeline runs past the playhead as you work the Jog/Shuttle/Scroll wheel. You can likewise scroll the Timeline with your pointer by dragging the Timeline Ruler up top left or right, which carries all your clips left or right along with it.
- With it cleared, the playhead rides over the clips whenever you play (press the Spacebar), jog, or shuttle (the JKL keys) in any direction, while the clips hold still. This mode helps when you're doing precision trimming in the Timeline with a pointing device, since the clips stay put as you drag pieces of clips to adjust them. As soon as the playhead reaches the Timeline's right or left edge, the Timeline pages over to show the next portion of your edit. You can also reposition the playhead by clicking in the Timeline Ruler to send it to that frame, or by hovering the pointer above the playhead's top handle (or above the playhead itself) and then dragging it anywhere you like.

### Snapping

Toggle Snapping on or off by clicking the Timeline Options icon and ticking or clearing the magnet-shaped Snap icon, or hit N to switch snapping on or off. With snapping active, clip in and out points, markers, and the playhead all snap into alignment with each other, which makes it simple to join clips at their boundaries or to align clips against markers or the playhead as a reference for key frames you mean to cut to. As a clip's boundary snaps, a white line indicates the edges being lined up together.

The indicator that appears when clip boundaries are snapping to another edge

NOTE: While the playhead is locked, clips won't snap to it. Even so, you'll want to be able to disable snapping whenever the behavior gets in the way of making fine adjustments to Timeline clips. Hit N to switch snapping on or off momentarily as you're dragging a clip in the Timeline, or while scrubbing the playhead with the pointer.

- If you toggle snapping mid-drag of a clip, an edge, or the Timeline, that counts as a temporary change, and snapping returns to its prior state once you let go of the mouse button.
- If you toggle snapping between drag operations, the snapping state holds until you next change it.

### Locking, Muting and Disabling Tracks

While working in the Timeline, it can help to lock tracks holding clips you'd rather not change by accident as you go. As an example, you could lock an audio track holding an edited music piece against which you're currently cutting your other video and audio, so you don't unintentionally alter or trim the music underpinning your program. Clips on locked tracks show up stippled to signal they're protected from changes.

A locked audio track; here the Lock icon shows closed and that track's clips appear stippled

It can also help to mute the audio or disable the video on tracks you don't care to see during Timeline playback. For instance, you might disable a track packed with title graphics when you want a clearer look at the video beneath it. Every track carries Mute and Enable controls, whereas audio-only tracks have just Mute controls. Enabled controls are white; disabled ones are gray.

Here Track 1 is disabled; its Enable button glows orange and the track's clips look dimmed

### Audio Trim View

While trimming on the Cut page, you can opt to enlarge the audio

waveform of a Timeline clip during the trim. This mode delivers a far more precise look at the audio,

making it simpler to land on an exact edit point between words, beats, and so on.

To toggle Audio Trim view: Click the Timeline Options icon and tick Trim to Audio. With this turned on, an enlarged waveform appears for audio/video clips you're trimming in the Timeline as the trim happens. It collapses back once you finish the trim.

The Audio Trim view, with an enlarged audio waveform on display as a Timeline trim is underway

### Timeline Markers

Markers can be dropped into the Timeline Ruler — found in the Upper Timeline as well as the Timeline Editor — to track key frames of clips you want to recall, alternate edit points you're weighing, pivotal moments in the edit, or to jot notes about things still to do. Marker text — which displays as an overlay in the Viewer — can be edited, and you can recolor markers to tell them apart.
