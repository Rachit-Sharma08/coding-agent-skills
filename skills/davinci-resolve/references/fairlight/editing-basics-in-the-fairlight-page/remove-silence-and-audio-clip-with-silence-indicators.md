# Remove silence and audio clip with silence indicators

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing basics in the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](audio-selection-extension-and-track-locks.md) / [Next section](trim-start-and-trim-end-and-trim-to-selection.md)
<a id="source-ai-checkerboard-to-new-tracks-studio-version-only"></a> <a id="source-audio-clip-with-silence-indicators"></a> <a id="source-linked-clips-in-the-fairlight-page"></a> <a id="source-manually-split-clips-in-pointer-or-range-mode"></a> <a id="source-multi-point-editing-overview"></a> <a id="source-new-track-timeline-clips-for-each-speaker"></a> <a id="source-remove-silence-dialog"></a> <a id="source-remove-silence-parameters"></a> <a id="source-remove-silence-studio-version-only"></a> <a id="source-resizing-the-in-and-out-points-of-a-clip"></a> <a id="source-trimming-clips-without-rippling-the-timeline"></a>

### Remove Silence (Studio Version Only)

This feature spots the silent stretches within a timeline clip and strips them out non-destructively, making your workflow leaner.

### Audio clip with silence indicators

### Remove Silence Parameters

- Threshold: Fixes the loudest audio level (in dB) still counted as silence. Anything beneath that level is judged silent and cut, so raising the threshold removes more audio.
- Pre Head: Sets how much silence, or pre-roll, sits ahead of each audible section.
- Minimum to Strip: This parameter sets the shortest span of silence (in milliseconds) that gets

be stripped from selected timeline clips.

- Bigger figures leave more silent patches in place. Smaller ones strip more, though you may notice some of the leftover audio sounding “chopped up” where it cuts off abruptly.
- Fade Head and Tail: Tick this checkbox and fades go onto the start and end of every surviving clip, sized by the Pre Head and Post Tail values.

### Remove Silence dialog

To remove silences from a timeline clip: 1 Pick a clip or a group of clips on a track. 2 Right-click that selection and pick Remove Silence from the contextual menu. 3 The selected audio's look shifts, gaining vertical red stripes that mark where the resulting silences fall and how long they run, according to the parameter values set in the Remove Silence dialog.

### AI Checkerboard to New Tracks (Studio Version Only)

Suppose several actors were captured by one boom mic on a single track and you need them split apart: this feature studies and transcribes the original audio, then sorts the resulting clips onto a dedicated track for each voice. To break speakers out onto fresh tracks: 1 Right-click the timeline clip, or a range within it, and pick AI Tools > Checkerboard to New Tracks from the contextual menu.

AI Tools contextual menu

2 As the Transcribing Audio dialog appears, Fairlight leans on AI to examine the audio and pick out each voice.

Transcribing Audio dialog 3 Every speaker gets a fresh track holding their new clips, while the original timeline clip is muted and kept whole.

### New track timeline clips for each speaker

NOTE: Recoloring the new timeline clips and tracks and timeline clips can be a handy way to keep them straight.

To learn how to recolor a timeline clip, see “Changing Clip Color in the Timeline” further along in this chapter. To learn how to recolor a track, consult “Using the Fairlight Page” at Chapter 170.

### Manually Split Clips in Pointer or Range Mode

To split one or more clips while in Pointer or Range mode: 1 Pick every track that holds a clip you intend to split. 2 Park the playhead across those clips on the precise frame where the split should fall. 3 Take either route: a) Use the Timeline > Split Clip menu item, or its shortcut Command-\ (backslash). b) Reach instead for Timeline > Razor, or hit Command-B. Split a clip on the Edit page and a through edit shows up, signaling that you now have an edit whose timecode runs unbroken from the outgoing half into the incoming one. That through edit is drawn on the Edit page with a dotted line along its edge to flag it as special. As of this writing, the Fairlight page doesn't render through edits.

### Linked Clips in the Fairlight Page

The Fairlight page lets you bind clips together. Once clips are linked, Fairlight's editing commands handle the whole set as though it were one clip — whatever you'd do to a lone clip happens to every linked clip together. Selecting any member of a linked clip selects all of them, and editing the In point of one member edits every one. To bind two or more clips: 1 Pick all the clips you want joined. 2 Right-click one of those selected clips and pick Link Clips from the contextual menu. A link indicator at the lower left of each newly linked clip signals their fresh linked status.

### Trimming Clips Without Rippling the Timeline

On the Fairlight page, most everyday adjustments touch only the selected clip or region of the Timeline. Whatever lies to the right of the adjusted area usually stays put, so sync isn't thrown off when you least expect it. What follows covers the foundational pieces of the Fairlight page's “seven-point editing” paradigm.

### Multi-Point Editing Overview

Every Timeline clip carries a handful of draggable handles and click targets that let the pointer carry out different editing chores.

- In point: Drag the clip's left edge to resize where the clip begins.
- Out point: Drag the clip's right edge to resize where the clip ends.
- Fade In handle: A handle in the clip's top-left corner that surfaces only while the

mouse hovers over that clip; drag it rightward to fade the audio in, or use it as one side of a crossfade between two audio clips. Double-click the fade handle to reset (clear) the fade.

- Fade In curve: A handle at the midpoint of the Fade In curve, visible only once the curve is exposed, for shaping the fade-in's strength. Drag it up or down to change the fade's X-Level, and left or right to change its X-Point. Double-click the curve handle to reset a fade curve.
- Fade Out handle: A handle in the clip's top-right corner that surfaces only while the mouse hovers over that clip; drag it leftward to fade the audio out, or use it as one side of a crossfade between two audio clips. Double-click the fade handle to reset (clear) the fade.
- Fade Out curve: A handle at the midpoint of the Fade Out curve, visible only once the curve is exposed, for shaping the fade-out's strength. Drag it up or down to change the fade's X-Level, and left or right to change its X-Point. Double-click the curve handle to reset a fade curve.
- Level: Treated as an editorial trait, any audio clip's level is adjustable through a level overlay stretching across the clip. Double-click that overlay to send the level back to its default 0.0 dB.
- Position: Click anywhere in a clip's middle in Pointer or Range mode, or along the bottom in Focus mode, and you can drag the clip earlier or later in time, or onto another track.

### Resizing the In and Out Points of a Clip

On the Fairlight page, trimming a clip's head or tail amounts to resizing its In or Out point, lengthening or shortening the clip to suit. To resize the beginning or end of a clip:

- To shorten or lengthen clips: Hover the pointer over a clip's start or end, and once it becomes the Resize cursor, drag the In or Out point left or right to alter the clip's length. While you drag the In or Out point of a Fairlight-page audio clip, an overlay pops up showing the waveform of every available frame at the head (when you drag the In point) or the tail (when you drag the Out point) of the clip being resized.

The overlay that shows up while you resize a Fairlight-page audio clip's In point To snap a clip's start or end straight to the outermost edge of its available media:

- Double-click the clip's In point to snap that In point to the very start of the clip's media.
- Double-click the clip's Out point to snap that Out point to the very end of the clip's media.

Resize a clip's In or Out point so it laps over one or more neighboring Timeline clips, and the overlapping stretches of those neighbors get overwritten by the clip you just resized.
