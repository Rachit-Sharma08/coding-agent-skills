# Inserting clips timecode handles and audio tracks

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing basics.
[Chapter index](INDEX.md) / [Previous section](nearest-edit-and-keyboard-shortcuts.md) / [Next section](manually-selecting-clips-in-the-timeline-overview.md)
<a id="source-audio-track-creation-while-editing"></a> <a id="source-example-assembling-clips-into-the-timeline-from-the-media-pool"></a> <a id="source-example-assembling-clips-into-the-timeline-from-the-source-viewer"></a> <a id="source-insert-selected-clips-to-timeline-using-timecode"></a> <a id="source-insert-selected-clips-to-timeline-with-handles"></a> <a id="source-inserting-multiple-clips-into-the-timeline-from-the-media-pool"></a> <a id="source-making-selections-in-the-timeline"></a> <a id="source-not-creating-new-tracks-when-adding-clips-to-a-timeline"></a> <a id="source-using-keyboard-shortcuts-and-three-point-editing-to-assemble-a-program"></a>

### Inserting Multiple Clips into the Timeline From the Media Pool

On certain high-volume editing projects, you can drop several clips from the Media Pool into a timeline in one go. How the clips get ordered and placed hinges on the method you use.

### Insert Selected Clips to Timeline Using Timecode

Clips can now travel directly out of the Media Pool into a timeline so that every clip's source timecode aligns with an equal record timecode value over in the Timeline. That can pay off on long-form multi-camera events, weddings or concerts say, where every camera shares one timecode to guarantee all edits sync perfectly. This function mirrors the Source Overwrite edit on the Cut page. IMPORTANT: For this edit to work, the Timeline's timecode has to overlap the clip(s)' timecode. That gets fixed within the New Timeline settings' Start Timecode field. Inserting selected clips to a timeline by timecode goes like this: 1 In the Media Pool, pick one or more clips to edit into the Timeline. Where In and Out points sit on a clip, the edit honors those bounds. With no In/Out points set, each picked clip gets edited in over its full duration. 2 Set a destination control to fix which Timeline track you're editing onto. 3 Right-click one of the picked clips and pick "Insert Selected Clips to Timeline Using Timecode" off the drop-down menu. 4 Every picked clip gets overwritten into the Timeline at its proper timecode location onto the destination track. IMPORTANT: Where several picked clips carry overlapping timecode, no edit happens.

### Insert Selected Clips to Timeline With Handles

This command drops several clips into the Timeline one after another, going by the Media Pool's current sort order, with handles pared away from each clip's current In and Out points (drawing on the Default Handles Length found under the User Preferences' Editing panel). Paired with the Add Transition tool (Command-T), this function shines when you're quickly knocking out montages from a batch of clips. To insert clips with handles to the Timeline: 1 In the Media Pool, pick the clips to insert into the Timeline with handles. 2 Right-click any picked clip, then pick "Insert Selected Clips to Timeline With Handles." The clips slot in starting at the Timeline In point with the default handles length already worked out.

TIP: To round off the montage, pick the clips in the Timeline, then pick "Add Transition" (Command-T) off the Timeline menu. That lays the default transition across all the clips in one stroke.

### Audio Track Creation While Editing

When you drag an audio clip into the undefined gray zone of the Timeline below the audio tracks already there in order to build a new track, that new track gets a channel mapping mirroring the channel count of the audio clip you're dragging. That also means if you've used Clip Attributes to map a clip's audio into multiple tracks where each track carries a different channel mapping—one 5.1 track, one stereo track, and six mono tracks, say—then editing that clip into the Timeline so its audio portion spawns new tracks will automatically build eight tracks: one 5.1, one stereo, and six mono.

### Not Creating New Tracks when Adding Clips to a Timeline

Under Edit > Edit Options there's a menu item named Automatically Create Tracks on Edit. On by default, this option keeps DaVinci Resolve's standard behavior of adding new tracks to the timeline automatically whenever your source material holds more audio tracks than your timeline does. Switch it off and you can drag source clips onto the timeline without the timeline spawning new tracks for the extra audio or video elements. Where your source camera files carry more audio tracks than your timeline holds, switching this option off won't build extra new tracks and will pull in only the elements showing in the track destination controls. That can help if, for instance, you wanted to bring in just a single mixed track with a clip from a multitrack recorder and skip the independent microphone tracks.

### Using Keyboard Shortcuts and Three-Point Editing to Assemble a Program

Drag-and-drop editing may be plenty intuitive, yet there are other ways to cut clips into the Timeline—using the playhead to mark where those clips begin—that can run faster and more precisely. Every one of these examples leans on "overwrite" edits, which clear unwanted media out of the Timeline as you add in the clips you do want. Here are two examples showing how to do it.

### Example: Assembling Clips Into the Timeline From the Source Viewer

The example below shows how you can use the Edit page to throw together a quick first cut of edits, drawing on various features of the Media Pool, Viewers, and Timeline. Spelled out with every possible option, it may look like a great many steps, but once you've got these fundamentals down and built a little muscle memory for the keyboard shortcuts in play, these methods turn out really fast. 1 Hit Command-1 to bring up the Media Pool, then steer with the Arrow keys to land on a bin (Up and Down move which one is highlighted, Right and Left open and close bins). Next hit Command-2 to jump to the clip browser, and again work the Arrow keys to land on a particular clip.

2 Hit the Return or Enter key to load the chosen clip into the Source Viewer. 3 Either drag the playhead with the pointer or work the Spacebar or JKL keys to reposition it, then set In and Out points (I and O) bracketing the stretch of that clip bound for your program. 4 By default, the source destination controls are mapped to tracks V1 and A1. If need be, choose different video and audio tracks to edit the clip onto in the Timeline by one of these means:

- Drag the source destination controls from where they sit now to where you want them in the Source Track Selector.
- Right-click an empty source destination control in the Source Track Selector, and pick the source destination off the context menu.
- Shift the source destination controls upward and downward with the Command-Option Up and Down Arrow shortcuts (for audio) and the Command-Shift Up and Down Arrow shortcuts (for video).
- Assign the video and audio source destination controls to particular tracks with the Option-1–8 key shortcuts (for video) and the Command-Option-1–8 key shortcuts (for audio).

5 By default, every source destination control is enabled. Should you want clips edited into the Timeline as audio-only or video-only, any one of these will do:

- Click a source destination control itself to shut off its video or audio component.
- For the tracks currently mapped, hit Option-1–8 (for video) or Command-Option-1–8 (for audio)

to flip the destination controls on those tracks on and off.

- From the drop-down menu sitting under the Source Viewer, choose among a source clip's Video and Audio, Video-Only, and Audio-Only inserts.

6 Working in the Timeline Viewer or the Timeline itself, steer the Timeline playhead with the pointer, the Spacebar, or the JKL controls to the frame where the clip you're about to edit should begin. With no In or Out points set in the Timeline, the playhead's position stands in as the In point by default. 7 To pull off an overwrite edit, do one of these:

- Pull the clip out of the Source Viewer onto the Timeline Viewer and let it drop on the Overwrite overlay. Under single viewer mode, that overlay appears only as you drag a clip out of the Media Pool onto the Timeline Viewer.
- Click the Overwrite Clip button in the toolbar.
- Choose Edit > Overwrite (or press F10).

The chosen clip(s) get overwritten onto the selected track at the playhead's spot, and the playhead travels by itself to the tail of the just-edited clip, primed for your next edit. Where that clip happens to be the final one on the Timeline, the frame sitting to the playhead's left is the last frame (carried with a jagged overlay along the Timeline Viewer's right edge) in place of the black that is the genuine frame after that clip. That eases the job of squaring up the next edit. If not, the playhead displays whichever frame lands at that moment in time. 8 For the next clip, load it into the Source Viewer, set its In and Out points, and lean on the Overwrite Clip button or command to drop it into the Timeline. Carry on this way until the run of edits you're aiming for is assembled.

The Timeline playhead resting on the first frame past the clip you just edited; over in the Timeline Viewer a jagged overlay on the right signals that this frame isn't a genuine one

### Example: Assembling Clips Into the Timeline From the Media Pool

If you like, you can also edit clips straight into the Timeline from the Media Pool using an assortment of commands. That can be a quick way to tack clips onto the end of the Timeline (though you can pull off insert edits this way too).

Editing one or more clips out of the Media Pool onto the Timeline: 1 Using the pointer, click a clip within the Media Pool to select it. 2 For one or more of the Media Pool's clips, place In and Out points by one of these means:

- Under Metadata view, run the pointer across a clip's thumbnail and tap the I and O keys. Where Live Media Preview is turned on for the Source Viewer, dragging across that thumbnail echoes its content into the Source Viewer.
- Under Thumbnail view, slide the pointer over a clip's thumbnail and tap the I and O keys. Should Live Media Preview be active for the Source Viewer, dragging over the thumbnail reflects what it holds in the Source Viewer.
- Under List view, drag along the Media Pool Filmstrip Viewer and tap the I and O keys. Where Live Media Preview is on for the Source Viewer, dragging along the filmstrip echoes its content into the Source Viewer.

3 Reorder the Media Pool's browser area so the clips end up in the sequence you'd like shown. Thumbnail view offers the Sort Order menu for that, while List view lets you click any metadata column's header to sort on that column's data. 4 By clicking, by dragging, by way of the Command-Option as well as Command-Shift Up and Down Arrow Key shortcuts, or by way of the Option-1–8 and Command-Option-1–8 key shortcuts, map the video and audio source destination controls onto whichever tracks should receive the incoming clip(s)' video and audio. Want the clips edited in as audio-only or video-only? Click a source destination control itself to shut it off. 5 Choose the clip or clips you intend to edit. The insert, overwrite, place on top, ripple overwrite, and append at end edits each handle several clips together, whereas the replace and fit to fill edits take just one clip apiece and will edit in only the first of multiple chosen clips. 6 To carry out the edit, do one of these:

- Use any of the editing commands in the Edit menu.
- Drop the picked clips into the Timeline via the corresponding keyboard shortcuts: Insert with F9, Overwrite with F10, Replace with F11, Place On Top with F12, Ripple Overwrite with Shift-F10, Fit to Fill with Shift-F11, or Append To End of Timeline with Shift-F12.
- Right-click one or more picked clips in the Media Pool, and pick "Insert Selected Clips to Timeline" or "Append Selected Clips to Timeline."

The picked clip(s) get edited into the Timeline.

### Making Selections in the Timeline

After you've put together a sequence of clips in the Timeline, you'll likely need to work them over some more—moving, deleting, trimming, or otherwise tweaking the clips in the Timeline so the edit plays with the pacing and verve you're after.
