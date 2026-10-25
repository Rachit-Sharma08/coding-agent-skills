# Trim start and trim end and trim to selection

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing basics in the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](remove-silence-and-audio-clip-with-silence-indicators.md) / [Next section](conventional-cut-copy-and-paste-overview.md)
<a id="source-cut-copy-and-paste"></a> <a id="source-deleting-audio-clips-and-regions"></a> <a id="source-disabling-and-re-enabling-clips-in-the-timeline"></a> <a id="source-duplicating-clips"></a> <a id="source-moving-and-overwriting-clips"></a> <a id="source-option-dragging-to-duplicate-a-clip-in-the-timeline"></a> <a id="source-slipping"></a> <a id="source-snap-to-playhead"></a> <a id="source-subframe-nudging"></a> <a id="source-sync-offset-indicator"></a> <a id="source-trim-start-and-trim-end"></a> <a id="source-trim-to-selection"></a>

### Trim Start and Trim End

The Trim > Trim Start (Shift-[) and Trim End (Shift-]) commands shift the In or Out point of every clip the playhead crosses; in Trim mode that happens as a ripple, while in Selection mode it happens as a resize. Since neither one needs a selection first, they're quick to reach for in the right moment. A textbook job for Trim End is a stack of superimposed clips of varying lengths that you want lined up to start or end together.

- Trim Start resizes or ripples — whichever your mode dictates — all clips crossing the playhead, dragging each clip's In point to the playhead's current spot.
- Trim End resizes or ripples the crossing clips so each one's Out point lands at the playhead's current spot.

Clips the playhead never crosses go untouched. You can also keep clips on certain tracks out of the operation by locking those tracks.

### Trim to Selection

The Trim > Trim to Selection (Shift-Command-T) command lops off the heads and tails lying outside a selection of one or more clips in one stroke, leaving just the selection behind. You'll find it in the Timeline contextual menu after right-clicking a clip.

(Left) a selection spanning parts of two clips; (Right) what Trim to Selection leaves once the heads and tails beyond that selection are cut away.

### Moving and Overwriting Clips

There's more than one way to relocate clips in the Timeline. A clip can be nudged or dragged within its track to retime where it sits in the edit, or it can be shifted up or down onto other tracks. To reposition Timeline clips, take any of these routes:

- To move one or more selected clips in the Timeline: Drag any Timeline clip wherever you like. In Focus mode you have to drag from the lower half of the selection. Drag a clip so it laps another, and the clip you're dragging overwrites the one beneath.
- To frame-nudge selected clips from the keyboard: Make a selection, then tap the Comma key to roll the edit one frame left or the Period key to roll it one frame right. Shift-Comma and Shift-Period jump by 5 frames.
- To shift selected clips onto tracks above or below all at once: Make a selection, then keep Shift held as you drag one of those clips up or down the Timeline, which pins their timing while they cross to other tracks. Alternatively, hold Option and press the Up or Down Arrow.

### Sync Offset Indicator

When a Fairlight-page audio clip drifts out of sync with the video item it's linked to, the clip shows an “out-of-sync” or sync offset indicator.

### Snap to Playhead

In Focus Mode, you can pin an audio clip's head (beginning) or tail (end) to wherever the playhead sits (the destination). That comes in handy for matching audio to an onscreen moment, like a ball shattering a window. The “Automation follows edit” option does cooperate with this, but keep a few points in mind:

- It still works even when the playhead is off the visible screen.
- A clip can only be snapped one at a time, and only to a spot on the same track.
- A “snapped” clip overwrites whatever audio already lives at the destination, even when that audio sits on a layered clip's

top layer.

- A set of clips on one track, picked in Range mode by the playhead position, can serve as a destination as well.

That said, you'd want to snap the clip toward the side of the playhead free of any existing audio you mean to keep. For more information Range Mode, see “Using Range Mode.”

To pin a clip's head onto the playhead: 1 Turn on Focus Mode and park the playhead at the destination you want. 2 Hold Command-Option and click the clip you'd like to move. The Audio now sits in its new spot with the clip's head pinned to the playhead. To pin a clip's tail onto the playhead: 1 With Focus Mode running, park the playhead at the destination you want. 2 Hold Command-Option-Control and click the clip you'd like to move. The Audio sits in its new spot with the clip's tail pinned to the playhead.

### Subframe Nudging

Within the Preferences/User/Editing panel, under General Settings, you can set the Fairlight page's nudge amount in either subframes or milliseconds. Both are fully user-definable, so just type the nudge amount you want into the matching box. Take the time to explore this whole settings panel, since it holds pre-roll and post-roll settings along with other handy Fairlight tweaks.

### Slipping

Once known as re-syncing, slipping an audio clip leaves the clip parked where it is in the Timeline while swapping out the stretch of media shown there. A slip edit alters neither the overall Timeline's length nor the clip's place relative to its neighbors; all it changes is the range of media the clip stands for. NOTE: Though earlier versions of Fairlight offered it, slipping isn't available as of this writing.

### Duplicating Clips

The Duplicate Selection command copies one or more selected clips and drops the copies right after the selection's Out point. When you duplicate a region of a clip that has tails, or a clip wedged between others, the duplicate overwrites whatever sits to the right of the current selection for as long as the copy runs.

Using the Duplicate Selection command to duplicate a selected region Hold Option while dragging a Timeline clip and you'll drop a duplicate of it at the spot where you release.

### Option-dragging to duplicate a clip in the Timeline

### Disabling and Re-Enabling Clips in the Timeline

Now and then a Timeline holds one or more audio clips you'd rather not play with the rest of the edit, yet you don't want to toss them out either in case you reconsider down the line. That's why you can disable clips, switching them off without deleting them. Earlier Fairlight versions called this Mute clip. A disabled clip dims in the Timeline — it won't play, won't render, and won't reach the video output — but its place in the Timeline is kept, so you can re-enable it whenever you decide you want it after all. Disabled clips show up gray in the Timeline. To disable or re-enable one or more selected clips:

- Right-click part of the selection and pick Enable Clip from the contextual menu.
- Choose Clip > Enable Clip.
- Press D.

### Deleting Audio Clips and Regions

Any selected clips or clip regions can be removed in either Pointer or Range mode by hitting the Delete key, or by right-clicking a clip and picking Delete Selected from the contextual menu. On the Fairlight page, a deletion leaves a gap by default. Through the Edit Menu > Ripple Delete you can ripple delete the selected clips, which reshuffles where every following clip lands.

### Cut, Copy, and Paste

The Fairlight page brings its own approach to copy and paste, built around the “ghost” overlays that stand in for the waveforms of selected audio clips. The approach makes copying and pasting clips simple via keyboard shortcuts and the JKL keys.
