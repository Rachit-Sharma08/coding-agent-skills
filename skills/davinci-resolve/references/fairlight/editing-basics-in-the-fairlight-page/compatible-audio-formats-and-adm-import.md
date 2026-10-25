# Compatible audio formats and adm import

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing basics in the Fairlight page.
[Chapter index](INDEX.md) / [Next section](audio-selection-and-edit-modes.md)
<a id="source-adm-import"></a> <a id="source-choosing-parts-of-clips-to-edit-in-the-media-pool"></a> <a id="source-compatible-audio-formats"></a> <a id="source-dragging-audio-clips-into-the-timeline"></a> <a id="source-editing-audio-clips-into-the-timeline"></a> <a id="source-editing-basics-in-the-fairlight-page"></a> <a id="source-editing-basics-in-the-fairlight-page-part-1"></a> <a id="source-for-more-information-see-chapter-173-recording"></a> <a id="source-moving-audio-clips-to-embedded-timecode-position"></a> <a id="source-overwriting-vs-layering-clips-that-overlap"></a> <a id="source-support-for-mixed-audio-track-formats-from-source-clips"></a> <a id="source-the-preview-player-in-the-media-pool"></a>

### Editing Basics in the Fairlight Page

The Fairlight page serves to polish audio first laid out on the Edit page, and it equally lets you record and build audio programs entirely from nothing. Since audio clips carry traits that video clips lack, working with sound involves extra steps you won’t find on the Edit page. Throughout this chapter you’ll learn the core moves for cutting audio the Fairlight way.

### Compatible Audio Formats

On the format front, DaVinci Resolve handles WAVE, Broadcast WAVE, and AIFF; it reads MP3, AAC (M4A), and CAF (macOS only); and it accepts both MTS and QuickTime containers carrying the AC3 audio format, along with Enhanced AC-3 (macOS and Windows only). On the sample-rate side, DaVinci Resolve works with audio at 32, 44.1, 48, 88.2, 96, and 192 kHz. Anyone on Linux gains the extra capacity to encode and decode MP3 files within Fairlight. With DaVinci Resolve 17 comes the creation and handling of Dolby Atmos ADM files plus a way to export Dolby Atmos masters as IMF deliverables. IMF (Interoperable Master Format) refers to a SMPTE standard describing one master file format that bundles every piece of media and metadata required to deliver the result.

### ADM Import

Bringing an ADM file into a project loads the Bed mix or mixes plus any linked Object tracks into a timeline. Each lands on the track type that matches the audio files baked into the ADM. So if a Bed file happens to be 7.1.2, that file opens on import into a 7.1.2 track within Fairlight. Object files turn into their own separate Fairlight tracks, holding all of their panning data.

NOTE: Pulling a Dolby Atmos file in from the Media Pool renders it dynamically to your chosen output format right on the Timeline by way of the Dolby Renderer. Fairlight, though, can take in the complete Atmos file along with its beds and objects when you import from the Fairlight menu instead - Fairlight > Immersive > Audio > Import Master File. Importing through that route builds a timeline where the file’s entire Atmos program and dynamic metadata are correctly mapped and routed.

### Editing Audio Clips Into the Timeline

A full audio editing environment lives on the Fairlight page, where you can either record and build clips from nothing or refine tracks packed with audio clips assembled in various ways. Depending on the kind of work at hand, there are four routes for getting media onto the Timeline of the Fairlight page:

- Recording fresh audio into one or several tracks,.

### For more information, see Chapter 173, “Recording.”

- By dragging fresh audio clips out of the Media Pool and dropping them onto the Fairlight timeline
- By cutting audio clips into audio tracks over on the Edit page
- By importing a project that already holds audio clips
- By auditioning and approving sound effects out of the Sound Library No matter how audio clips end up on your timeline, the remainder of this chapter walks through the countless ways you can edit and sweeten what’s there.

### Overwriting Vs. Layering Clips That Overlap

As you place clips on the Timeline, the outcome of dropping one that overlaps a clip already sitting in your target track hinges on the Timeline > Layered Audio Editing setting. Out of the box, with Layered Audio Editing switched off, laying one audio clip over another causes the incoming clip to non-destructively erase the overlapping portion of the clip beneath it from the Timeline. Flip Layered Audio Editing on, however, and incoming clips stop overwriting the clips they overlap; instead they stack within the track, so the arriving audio clip wins out over what sat there before, yet the overlapping audio segments already on the Timeline survive — something you can view by selecting View > Show Audio Track Layers. That gives you the choice, as the job demands, of either overwriting clips you edited earlier or layering the newly edited ones, whether or not Audio Track Layers happen to be on screen. Audio layering is available on the Edit page and the Fairlight page alike. The topic of audio layering gets fuller treatment in a later section of this chapter.

### Choosing Parts of Clips to Edit in the Media Pool

Sitting atop the Media Pool is a preview player, a spot where you can open chosen source clips from the Media Pool, play them back, drop marks to log them, and set In and Out points before drag-and-dropping them onto the Timeline. In practice the Media Pool Preview Player stands in as a Source monitor for editing on the Fairlight page.

### The preview player in the Media Pool

- A range of viewing controls fills the title bar across the top. Up at the left, a dropdown menu lets you pick a zoom level for the audio waveform on display. Just right of it, a Timecode window reports either the clip’s length or the length bracketed by In and Out points. Continuing right, a real-time performance indicator reflects how playback is performing. Dead center sits the title of the clip you’ve currently selected, and a dropdown to its right surfaces the last 10 clips you browsed. Over at the far left, a Timecode field reports where the playhead currently rests (a right-click here brings up a contextual menu offering ways to swap the displayed timecode and to copy and paste timecode).
- The middle of the Media Pool Preview Player displays the waveforms for every channel of the selected clip, drawn at whichever zoom level you’ve chosen.
- Down at the bottom, the transport controls comprise a jog bar for scrubbing, Stop, Play, and Loop buttons, along with In and Out buttons.

### Dragging Audio Clips Into the Timeline

With the Media Pool open on the Fairlight page, you can cut whole audio clips onto the Timeline by dragging single clips and dropping them on whichever audio track should hold them. Any clip can go onto any track, no matter whether the clip’s channels line up with the track’s channel mapping. That said, dropping a clip carrying more channels than the track supports (say, a stereo clip onto a mono track) outputs only the channels the track can handle and mutes every other channel in that clip. Should that occur, you can always re-map the audio track by right-clicking its track header and selecting a fresh mapping from the Change Track Type To submenu.

TIP: Dropping one or more clips into the open space below the Timeline’s existing audio tracks spawns new tracks, and each one is mapped automatically to as many channels as the audio clip being edited calls for. With Ambisonics files, dragging a clip to the timeline — or making a new timeline that references a clip — produces a track of the right type, matched to the file’s Ambisonic order and channels. When you intend to drag several clips out of the Media Pool and edit them onto the Timeline together, a little prep usually pays off to ensure they land in the proper order. Dragging several clips onto the Timeline as one unbroken run of edited clips: 1 Adjust the sort order in the Media Pool’s browser area so the clips fall into the sequence you want them shown. Thumbnail view offers the Sort Order menu, whereas List view lets you click any metadata column header to sort by that column’s contents.

Reordering Media Pool clips by way of the Sort Order menu 2 Rely on the Media Pool thumbnails, the Filmstrip in Media Pool List view, or the Source Viewer to set In and Out points that mark which portion of each clip should go onto the Timeline.

3 Choose the Media Pool clips bound for the Timeline by dragging a bounding box, Command-dragging several bounding boxes across different groups of clips, Shift-clicking a run of clips, or Command-clicking separate non-adjacent clips. 4 Drag any of those chosen clips to the spot you want in the Timeline to carry out an overwrite edit. Whatever clips you drag overwrite any other clips they land on top of in the Timeline. When several clips come from the Media Pool, they edit in the same sequence as their Media Pool sort order, each honoring its own In and Out points. You can also cut audio clips onto the Timeline so that every clip’s timecode aligns with the Timeline Ruler. That comes in handy when you’re arranging multiple source audio recordings you want synced together across several tracks. Dragging several clips to edit them into a track at their timecode positions: 1 Choose the Media Pool clips bound for the Timeline by dragging a bounding box, Command-dragging several bounding boxes across different groups of clips, Shift-clicking a run of clips, or Command-clicking separate non-adjacent clips. 2 Keep Command-Shift held and drag the chosen clips into the track that should hold them to carry out an overwrite edit.

A series of audio clips edited into the Timeline by timecode position Every clip placed into that track lands at the timecode position carried in its own embedded timecode. So if you had been recording time-of-day timecode, each clip turns up on the Timeline at the moment it was captured. A batch of clips taped between hours 10 and 13 will spread out across hours 10-13 of your timeline. Two or more audio clips can likewise be edited onto the Timeline as a stack, setting you up to layer several sound effects for sound design work. Dragging several clips to edit them into a track as a parallel stack: 1 Choose the Media Pool clips bound for the Timeline by dragging a bounding box, Command-dragging several bounding boxes across different groups of clips, Shift-clicking a run of clips, or Command-clicking separate non-adjacent clips. 2 Command-drag the chosen clips into a track of the Timeline. The first of the chosen clips drops into the track you dragged onto, while the rest land either in audio tracks below that first one or, when no audio tracks are free, in newly created audio tracks made to hold them. Everything you’ve edited shows up as a parallel stack, spread across separate tracks one above another.

### Moving Audio Clips to Embedded Timecode Position

Every clip carries a timecode tucked into its metadata. Using that metadata, you’re given ways to drop clips onto the Timeline either from the Media Pool or within the Timeline itself. A right-click on a clip in the Timeline offers Move to Embedded Start Timecode. Clicking it spots the clip onto a chosen track of the Timeline at that timecode. Keep in mind both the embedded audio timecode and the Timeline’s own timecode. Unless the two overlap, the function won’t do anything. As an example, a clip whose embedded timecode reads 00:00:00:00 could prove hard to locate on a Timeline beginning at 00:59:58:00. If you’ve spotted a clip with these tools yet still can’t find it, inspect the embedded timecode in the Inspector’s Metadata panel together with the Timeline’s timecode.

A right-click on a clip in a Timeline surfaces the Move to Embedded Start Timecode option.

A right-click on a clip in the Media Pool surfaces the Insert Selected Clips to Timeline option.

When you right-click a clip in the Media Pool, one option is Insert Selected Clips to Timeline Using Timecode. Choosing it spots the clip onto a chosen Timeline track at the embedded timecode.

NOTE: A clip’s embedded timecode is shown in the Inspector’s File tab beneath timecode.

The Timecode metadata lives within the Inspector window on the File tab.

Clip Attributes now lets you hand channels out across different tracks carrying different channel assignments

### Support for Mixed Audio Track Formats from Source Clips

Media holding several audio tracks whose embedded channels follow different formats is supported by DaVinci Resolve. Take a clip carrying one stereo track, one 5.1 surround track, and six mono tracks: every one of them can be set up correctly in the Audio panel of Clip Attributes once that clip is imported. The Audio panel of Clip Attributes governs which format (Mono, Stereo, 5.1, 7.1, Adaptive) the channels inside a given audio track are configured as. As a result, you can build clips with multiple tracks, each running a different audio format and a different mix of channels — handy when preparing imported audio mix files you intend to output while mastering a program.
