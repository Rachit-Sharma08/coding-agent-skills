# Gang viewers playhead ganging and adding markers

Version: DaVinci Resolve 20.3 Reference Manual. Context: Preparing clips for editing and viewer playback.
[Chapter index](INDEX.md) / [Previous section](playback-return-position-and-audio-scrubbing.md) / [Next section](edit-point-storage-and-duration-markers.md)
<a id="source-adding-markers"></a> <a id="source-adding-markers-to-clips"></a> <a id="source-clearing-and-navigating-in-and-out-points"></a> <a id="source-gang-viewers-playhead-ganging"></a> <a id="source-markers-placed-on-a-clip-in-the-timeline"></a> <a id="source-markers-placed-on-a-source-clip"></a> <a id="source-setting-clip-in-and-out-points-in-the-media-pool"></a> <a id="source-setting-clip-in-and-out-points-in-the-source-viewer"></a> <a id="source-setting-in-and-out-points"></a> <a id="source-the-properties-found-in-the-marker-dialog"></a>

### Gang Viewers (Playhead Ganging)

By default, playhead motion runs separately in the Source and Timeline Viewers. Click the Option menu at the top right of either Viewer and switch Gang Viewers on, though, and the two playheads become locked so that they travel together in lockstep. That comes in handy while, within the Source Viewer, you set a clip’s In and Out points so they line up with the length of a clip or some other event in the Timeline. Even with the Source and Timeline Viewers ganged, you can still pass focus between the Source and Timeline Viewers, and your video output device will reliably output whichever Viewer currently holds focus.

### Adding Markers

Markers, flags, and clip labels get fuller treatment in other parts of the editing section, yet markers matter enough that a quick rundown of adding and editing them belongs right here. You use markers to flag a specific frame inside a particular clip. Each marker can carry its own color along with custom name and note text. The moment you type any text into a marker, that marker shows a tiny dot signaling that there’s more detail held inside. After they’re placed, markers snap, when snapping is on, to In and Out points, edit points, the playhead, and to other markers, which makes them handy for “measuring” the edits and trims you perform on the Timeline.

### Adding Markers to Clips

Markers can be dropped onto the jog bar of source clips within the Source Viewer (or within the Media Page Viewer), as well as onto clips you’ve selected inside a timeline.

### Markers placed on a source clip

### Markers placed on a clip in the Timeline

To set a marker on a source clip within the Source Viewer or Media Page Viewer, take one of these approaches:

- To drop a marker and nothing more, bring the playhead to the frame you’d like marked, then press M.
- To drop a marker and have its dialog open right away so you can add a name or note mid-playback, press Command-M. Playback holds until you’ve typed the text you want and shut the marker dialog again, whereupon playback resumes.
- Bring the playhead to the frame you’d like marked, then right-click within the jog bar and pick a marker color out of the Add Marker submenu in the contextual menu.

After you’ve dropped a few markers, you might wish to tweak what’s inside them to make them more useful. To bring up a marker’s edit dialog and change its properties: 1 Do one of the following:

- Press Command-M to drop a marker mid-playback and have its edit dialog open at once.
- Double-click whichever marker you’d like to edit.
- Using Shift-Up Arrow/Down Arrow, bring the playhead to the frame that holds the marker you want

to annotate, then press M.

- Pick any marker in the Source Viewer or Timeline, and press Shift-M.

2 Once the marker dialog is open, several properties become editable.

### The properties found in the marker dialog

For a great deal more on markers, turn to Chapter 41, “Marking and Finding Clips in the Timeline.”

### Setting In and Out Points

With your clips reviewed via the playback commands, you’re ready to drop In and Out points that define the portion of each clip you mean to edit into the Timeline. Leave In or Out points unset and the whole clip lands in the Timeline. Set them, and those points get stored in the Media Pool, ready for the next time you edit that clip.

### Setting Clip In and Out Points in the Media Pool

You’re able to drop In and Out points straight inside the Media Pool to get ready for editing. While skimming a thumbnail in Metadata view, here’s how to mark In and Out points: Put the Media Pool into Metadata view, hover the pointer over the Thumbnail, and pause a beat until dragging the pointer starts skimming that clip. As it skims, tap I and O so the In and Out points bracket whatever stretch of that clip you mean to use. Skimming instead inside Thumbnail view, the steps run thus: Switch the Media Pool over to Thumbnail view, rest the pointer on a clip, and wait a moment until a drag of the pointer kicks off skimming through it. With it skimming, tap I and O so the In and Out points bracket whatever stretch you plan to keep. When that’s done, a range indicator along the foot of the clip’s thumbnail reveals how much you’ve picked out. The List view Filmstrip offers a third route for marking In and Out points: Switch the Media Pool over to List view, choose a clip so it surfaces in the Filmstrip running atop the Media Pool, sweep the pointer through the Filmstrip to watch it roll, and tap I and O so the In and Out points span the range you’re after.

Marking In and Out points via the List view Filmstrip of the Media Pool The Filmstrip greys out the heads and tails, letting you take in the span of media you’ve marked. Once In and Out points sit in the Filmstrip, a leftward or rightward drag moves them around.

### Setting Clip In and Out Points in the Source Viewer

For a closer look at your footage, you can lay down In and Out points in the Source Viewer ahead of editing.

Here’s the routine for marking In and Out points within the Source Viewer: 1 With Live Media Preview enabled via the Source Viewer’s option menu, either skim a thumbnail from the Media Pool, or else load a clip in. 2 Reach for JKL, the Spacebar, the transport controls, or a jog-bar drag to bring the playhead to wherever an In or Out point belongs. 3 Take one of these paths: For plain In and Out points, click the In and Out buttons just right of the transport controls, or hit the I or O keys. For split In and Out points, ahead of a split edit, right-click the Jog Bar; out of the Mark Split submenu, the video side gives you Mark Video In (Shift-Option-I) and Mark Video Out (Shift-Option-O), while the audio side gives you Mark Audio In (Command-Option-I) and Mark Audio Out (Command-Option-O).

Placing In and Out points within the Source Viewer, shown both as simple (Left) and as split edits (Right) With plain In and Out points, the picture and sound of two clips meet at a single shared edit point on the Timeline. Lay down split In or Out points, on the other hand, and you’re set up to craft split edits in which the video runs offset from the audio in one move.

### Clearing and Navigating In and Out Points

After they’re set, you can also wipe away In and Out points you no longer want, and send the playhead to In and Out points you may want to edit. To clear In and Out points:

- To clear In or Out points: With the pointer resting on a marked thumbnail in the Media Pool, or on the Media Pool film strip, or with a clip open in the Source Viewer, press Option-I to wipe the In point you’ve set, or Option-O for the Out point.
- To clear Split In or Split Out points: A press of Shift-Option-X wipes the Video In and Video Out points; Command-Option-X wipes the Audio In and Audio Out points.
- To clear both the In and Out points together: Rest the pointer on a marked thumbnail in the Media Pool, or on the Media Pool film strip, or activate the Source Viewer, then press Option-X.

To send the playhead, within either the Source or Timeline Viewer, onto the current In or Out points:

- Press Shift-I to carry the playhead to the current In point (Playback > Go To > In).
- Press Shift-O to carry the playhead to the current Out point (Playback > Go To > Out).

The Go to In and Go to Out commands can drop the playhead onto the implied (yet unmarked) In and Out points that a three point edit you’re building defines, even while Preview Marks stay switched off. Say you drop In and Out points on the Timeline, and afterward, within the Source Viewer, set a clip’s In point; a press of Shift-O (Go to Out) will, all by itself, bring the Source Viewer playhead onto the frame destined to be that clip’s Out point were you to run the edit.

A three point edit takes shape from In and Out points placed on the Timeline together with an In point placed in the Source Viewer,

Go to Out, used here to bring the Source Viewer playhead onto the implied Out point that a three point edit defines
