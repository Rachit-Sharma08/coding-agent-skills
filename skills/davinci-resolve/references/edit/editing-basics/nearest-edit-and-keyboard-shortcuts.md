# Keyboard shortcuts in this chapter and function select nearest edit to playhead

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing basics.
[Chapter index](INDEX.md) / [Next section](inserting-clips-timecode-handles-and-audio-tracks.md)
<a id="source-audio-only-and-video-only-insert"></a> <a id="source-controls-in-the-source-viewer"></a> <a id="source-drag-and-drop-editing"></a> <a id="source-drag-and-drop-editing-of-individual-clips-into-the-timeline"></a> <a id="source-drag-and-drop-editing-of-several-clips-into-the-timeline-at-once"></a> <a id="source-drag-and-drop-editing-of-video-only-or-audio-only-edits"></a> <a id="source-drag-and-drop-insert-editing"></a> <a id="source-dragging-clips-from-the-file-system-into-the-timeline"></a> <a id="source-editing-basics"></a> <a id="source-editing-basics-part-1"></a>

### Editing Basics

This chapter walks you through a host of the core techniques and commands you'll reach for as you start putting clips together in the Timeline. Covered here are drag-and-drop moves for kicking off a timeline assembly, assorted ways to select and deselect the clips you've edited as you prep for different jobs, holding sync between the audio and video halves of the clips you're editing, and clearing out clips and gaps you'd rather be rid of.

### Drag and Drop Editing

For anyone who's already worked in other editing programs, this section's procedures will almost surely feel like old news, but if editing is new to you, here we cover the most elementary ways of cutting a string of clips into the Timeline to get you going. The plainest editing method of all is to pull clips out of the Media Pool and drop them into the Timeline. You can manage this with single clips or with selected batches of clips.

### Drag and Drop Editing of Individual Clips Into the Timeline

When you're editing just one clip at a time to build an edited sequence in a timeline, here's how it goes. 1 Should you need to edit particular stretches of the clips you're working with, you can first place In and Out points in source clips by one of these means: Placing In and Out points while skimming a thumbnail in the Metadata View: While you skim across a clip's thumbnail in the Viewer, press I and O to drop In and Out points around the part of that clip you'll want to use. With Live Media Preview switched on in the Source Viewer, the Source Viewer will display what you're skimming so you can take a closer look. Don't care for the current In and Out points? Press Option-X to wipe them both. Placing In and Out points while skimming a thumbnail in the Media Pool: While you skim across a clip's thumbnail in the Viewer, press I and O to drop In and Out points around the part of that clip you'll want to use. With Live Media Preview switched on in the Source Viewer, the Source Viewer will display what you're skimming so you can take a closer look. Once you're done, a range indicator at the bottom of that clip's thumbnail shows how much of the clip you've picked. Don't care for the current In and Out points? Press Option-X to wipe them both. Working with the Media Pool Filmstrip while the Media Pool sits in List view: Switch the Media Pool to List view, pick Show Filmstrip from the option menu, then pick a clip to surface it in the Filmstrip atop the Media Pool; run the pointer along the Filmstrip to watch it play, and tap I and O to fix In and Out points around the range you want. The Filmstrip dims the heads and tails so you can see the span of media you've marked. With Live Media Preview switched on in the Source Viewer, the Source Viewer will display what you're skimming so you can take a closer look. Don't care for the current In and Out points? Press Option-X to wipe them both.

Working through the Source Viewer: Get a clip into the Viewer by giving it a double-click in the Media Pool, or by selecting it there and hitting the Return or Enter key. From there, drive the playhead with the transport controls, the jog bar, the control panel buttons, the Spacebar, or the JKL commands, and set In and Out points through the In and Out buttons sitting to the right of the transport controls, or simply by hitting the I or O keys. Don't care for the current In and Out points? Press Option-X to wipe them both. 2 Pull whichever clip you'd like to edit out of the Media Pool or the Source Viewer, then drop it onto your chosen spot in the Timeline to run an overwrite edit. Drag a clip atop another already in the Timeline and the clip you're dragging overwrites the portion of the clip that it laps over.

Overwriting a Timeline clip by dragging one over from the Media Pool TIP: Drag a clip into the empty zone above an existing video track or below an existing audio track and a fresh track gets built for you automatically.

### Drag and Drop Editing of Several Clips Into the Timeline At Once

That same procedure applies when several clips need to go into the Timeline together, dragged out of the Media Pool in one motion. 1 Reorder the Media Pool's browser area so the clips fall into the sequence you'd like them shown in. Thumbnail view gives you the Sort Order menu for this, whereas List view lets you click any metadata column's header to sort on that column's data. Where you've leaned on the Metadata Editor to attach Scene, Shot, Take, or other identifying details per clip, sorting by those metadata criteria is possible. 2 Turn to one of three tools—the Media Pool thumbnails, the Filmstrip in the Media Pool's List view, or the Source Viewer—to drop In and Out points around the slice of each clip headed for the Timeline. 3 Choose the Media Pool clips bound for the Timeline by drawing a bounding box, by Command-dragging a few bounding boxes across different sets of clips, by Shift-clicking a span of clips, or by Command-clicking separate non-contiguous clips. 4 Drag any one of the chosen clips to your target spot in the Timeline to run an overwrite edit.

Reordering the Media Pool's clips by way of the Sort Order menu

Pulling several clips into the Timeline following the Media Pool's sort order Whatever clip(s) you drag overwrite any other clips they lap over in the Timeline. Several clips pulled from the Media Pool get edited in whatever order they're sorted into in the Media Pool, drawing on each clip's In and Out points.

### Drag and Drop Editing of Video-Only or Audio-Only Edits

Editing just a clip's video or just its audio is easy enough by switching off the audio or video destination control in the Timeline ahead of any edit (covered later in Chapter 39, "Three- and Four-Point Editing"); still, there's also a pair of keyboard modifiers that pull off the exact same thing while you drag.

For a clip's video alone out of the Media Pool: Option-drag clips into the Timeline from the Media Pool/ Filmstrip, the Source Viewer, or the Finder. For a clip's audio alone out of the Media Pool: Shift-drag clips into the Timeline from the Media Pool/ Filmstrip, the Source Viewer, or the Finder. For just the video or just the audio of a Source Viewer clip: Load a clip into the Source Viewer, then hover the pointer over the Source Viewer and drag off whichever of the Video-only or Audio-only overlays appear along the bottom of the image.

Inside the Source Viewer, Video- and Audio-only overlay controls turn up that let you pull just the video or just the audio across into the Timeline

### Drag and Drop Insert Editing

In the same way, at any frame of the current timeline you can pull several clips from the Timeline, or a lone clip from the Source Viewer, to either tuck the selection between a pair of clips or drop it amid an existing clip—nudging (rippling, in truth) every bit of media past the new edit point you create so the arriving media has somewhere to go. Shuffle inserting several clips out of the Media Pool or Source Viewer into the Timeline goes like this: 1 In the Media Pool, choose one or more clips (their sort order decides how the edited clips end up ordered), or load a clip into the Source Viewer. 2 Keep the Command and Shift keys held, then drag your selection from the Media Pool or Source Viewer over into the Timeline. 3 While you drag, the clips in tow get tucked into the Timeline wherever the pointer rests. Release the mouse to seal the edit.

Making an Insert Edit while dragging clips from the Media Pool

### Audio-Only and Video-Only Insert

### Controls in the Source Viewer

Over in the Edit page, a drop-down menu beneath the Source Viewer holds persistent choices for a source clip's Video and Audio, Video-Only, and Audio-Only inserts.

The fresh persistent Video / Audio insert controls down along the foot of the Source Viewer

### Dragging Clips From the File System Into the Timeline

On supported platforms you can also drag a clip straight out of your file system to the Timeline.

Dragging multiple clips into the Timeline from the macOS Finder
