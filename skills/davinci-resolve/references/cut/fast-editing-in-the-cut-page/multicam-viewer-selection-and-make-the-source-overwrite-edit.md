# Multicam viewer selection and make the source overwrite edit

Version: DaVinci Resolve 20.3 Reference Manual. Context: Fast editing in the cut page.
[Chapter index](INDEX.md) / [Previous section](manual-clip-sync.md)
<a id="source-audio-transcription-and-text-based-editing-studio-version-only"></a> <a id="source-live-overwrite-with-a-mouse-drag"></a> <a id="source-make-the-source-overwrite-edit"></a> <a id="source-resync-misaligned-synced-clips"></a> <a id="source-the-multicam-viewer-selection"></a>

### The Multicam Viewer selection

### Make the Source Overwrite Edit

With the clip's edit points settled, click the Source Overwrite button and the camera clip you chose lands perfectly in sync along your timeline. The playhead then advances on its own to that clip's Out point and the Multi Viewer comes back, leaving you instantly set for the next edit.

Camera 2 chosen with the Playhead at the In point along the Timeline, set for a Source Overwrite edit.

The finished Source Overwrite edit, with Camera 2 now cut in and the Timeline awaiting the next edit

TIP: Since it's the actual media in the Sync Bin, rather than the Timeline, that fixes how far the clips can reach, you're able to scroll beyond the Timeline's end to perform an edit. Once you're out past the Timeline's end, the playhead stands in for the Out point instead, which lets the clip backfill itself to match the precise duration needed to fill the Timeline.

### Resync Misaligned Synced Clips

When you're cutting with synced Multicam clips and a shot drifts out of sync with the timeline by accident, a warning icon flags it down in the clip's lower left. Bringing that clip back into step with the timeline is easy: click the Edit Actions icon and pick Resync Clip from the contextual menu.

Should a clip slip out of sync within Multicam footage by accident, a red sync warning indicator surfaces in the clip's lower left.

### Live Overwrite with a Mouse Drag

Lacking a Speed Editor, you can still drive the paint on capability of Live Overwrite across multicam material with your mouse. Start by opening all your multi camera angles in either the Sync Bin or the Multi Source viewers. Then just click the angle you'd like and drag sideways across the image to live paint that angle onto the timeline at the playhead's spot. Click a different angle next and drag to lay down the following camera. Thanks to the Sync Bin's distinctive way of holding every bit of footage locked together, an entire multicam production comes together remarkably fast from nothing but plain mouse drags.

Clicking and dragging on camera angle 1 in the Viewer “paints” that angle onto the timeline across a stretch matching the length of the drag. Keep clicking and dragging further angles for a speedy multicam production.

### Audio Transcription and Text Based Editing (Studio Version Only)

Knowing exactly what people said in a clip is the single most important piece of metadata it can carry. Having a shot fully transcribed helps in narrative film, where it lets you track down particular clips by the dialog written in the script, yet a transcript matters even more in unscripted documentary and news work, both for grasping which parts of the story you genuinely got on tape and for meeting an assortment of organizational, creative, and legal needs. Not long ago, transcribing audio demanded plenty of effort: a person had to play a clip in real time and key out the spoken words into a log sheet. Owing to recent strides in the DaVinci Resolve Neural Engine, your machine now handles that tedious transcription of each clip for you automatically, and crucially, with accuracy. On top of that, attaching text transcripts to your project's clips unlocks powerful new text-based editing tools for selecting, searching, and dropping clips into your timeline. CUT For a fuller treatment of Text Based Editing, turn to Chapter 40 “Text Based Editing.“
