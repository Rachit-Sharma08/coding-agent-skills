# Modifying clip duration via timecode and resizing or trimming clips in the source viewer

Version: DaVinci Resolve 20.3 Reference Manual. Context: Modifying clips in the timeline.
[Chapter index](INDEX.md) / [Previous section](selection-mode-move-resize-and-roll.md) / [Next section](disabling-copying-and-pasting-timeline-clips.md)
<a id="source-a-through-edit-seen-in-the-timeline"></a> <a id="source-doing-a-slip-edit-in-the-viewer"></a> <a id="source-enabling-and-disabling-clips-and-tracks"></a> <a id="source-modifying-clip-duration-via-timecode"></a> <a id="source-resizing-or-trimming-clips-in-the-source-viewer"></a> <a id="source-shuffleswap-insert-edits"></a> <a id="source-splitting-and-joining-clips"></a> <a id="source-through-edits"></a> <a id="source-using-the-selection-tool"></a> <a id="source-using-the-trim-tool"></a>

### Modifying Clip Duration Via Timecode

There are two numeric routes to adjusting a clip’s duration. To adjust a chosen clip’s duration: 1 Decide first whether altering the duration should ripple the Timeline or write over the adjacent clips. To ripple the Timeline, pick the Trim tool. To overwrite the neighbors or open a gap, pick the Selection tool. 2 Carry out one of these:

- Highlight a clip, then go to Clip > Change Clip Duration.
- Right-click whichever clip in the Timeline you like and pick Change Clip Duration out of the contextual menu. 3 Once the Edit Duration Change dialog opens, type a fresh duration into the Timecode field and click Change.

For further detail on entering timecode, consult “Moving the Playhead Using Timecode” in Chapter 35, “Preparing Clips for Editing and Viewer Playback.”

A dialog used to revise how long a Timeline clip runs

### Resizing or Trimming Clips in the Source Viewer

A clip can additionally be sent from the Timeline into the Source Viewer so you can trim it by other means. Two approaches accomplish this:

- Double-click whichever Timeline clip you want and it opens up in the Source Viewer.
- Park the playhead over a Timeline clip, hit Shift-V to grab that clip, and then press the

Return or Enter key to load it into the Source Viewer. After a clip lands in the Source Viewer, that Viewer takes focus, which lets you run the Spacebar or JKL commands to steer the playhead through the Viewer as you make edits. Whether those edits ripple the Timeline turns on which tool you’re holding — the Selection tool or the Trim tool. TIP: To pull up a match frame of a Timeline clip with the pointer instead, keep Option pressed while you double-click a clip.

### Using the Selection Tool

With the Selection tool active, you’re free to drag the In and Out markers, or lean on the playhead together with the I and O keyboard shortcuts to resize that clip back in the Timeline.

A Timeline clip loaded into the Source Viewer, where dragging its out point resizes the clip and opens a gap (red arrows).

### Using the Trim Tool

With the Trim tool active, dragging the In and Out points — or placing fresh ones via the I and O keys — resizes the clip and ripples the Timeline left or right as required.

### Doing a Slip Edit in the Viewer

Keep Shift pressed as you drag the In or Out point of a timeline clip loaded in the Source Viewer, and both the In and Out points travel as a pair, producing a slip edit of that clip’s content within the Timeline. Either the Selection or the Edit tools can do this.

### Shuffle/Swap Insert Edits

A Shuffle Insert edit (occasionally called a Swap Insert edit) gives you a quick way to reorder one or several chosen clips in the Timeline just by Command-Shift dragging them left or right. As you do, the clips on either side slide right or left on their own to trade positions with whatever you’re dragging. It’s a remarkably fast method for reordering clips while testing different layouts, and you never have to first park clips on extra tracks to clear them out of the way. There’s plenty of latitude in how the shuffling works. You may pick a single clip or a run of consecutive clips to shuffle. Choose several consecutive clips and they travel together as one block. You can even grab several consecutive clips spanning multiple tracks and shuffle them around the Timeline as a single object. On top of that, you can select clips belonging to split edits, where the audio and video In and Out points begin or finish on different frames. Here, how the other clips reposition themselves in the Timeline to clear room for the split-edit clip you’re dragging hinges on whether you grabbed the video or the audio half of the clip to begin the drag:

- Grab and drag the video half of the clip, and every clip reshuffles around the length of that video item on its track, letting all the video items on that track reorganize themselves without writing over one another or opening gaps. While you drag the selection through the Timeline, any overlapping linked audio items will either overwrite the audio on the clips beside them or open a gap.
- Grab and drag the audio half of the clip, and every clip reshuffles around the length of that audio item on its track, letting all the audio items on that track reorganize themselves without writing over one another or opening gaps. While you drag the selection through the Timeline, any overlapping linked video items will either overwrite the video on the clips beside them or open a gap.

With those rules in mind, shuffling clips becomes quite simple, and there are two ways to go about it. To shuffle insert clips alongside their neighbors in the Timeline: 1 Switch snapping on. 2 Pick one or more consecutive clips to shuffle. 3 Hold down the Command and Shift keys and drag the video or audio half of the chosen clips left or right.

Provided you bring clips up to the In or Out points of their neighbors, those neighbors will trade places with the dragged selection on their own. Snapping helps keep the clip(s) you’re dragging lined up with edit points that already exist until you release them in the spot you want.

Before and after clip L gets shuffled among clips I, K, and J in a scene to reorder the sequence To shuffle insert a single clip into its neighbors in the Timeline: 1 Switch snapping off. 2 Pick one or more consecutive clips in the Timeline to shuffle. 3 Hold down the Command and Shift keys and drag the video or audio half of the chosen clips left or right. 4 With snapping off, the selection you’re dragging slots more readily into the middle of the adjacent clips, and the cut piece of each clip slides into the gap the dragged clip(s) leave behind. Release the clip at the spot you want once you’re done.

Before and after clip L gets dropped into the middle of Clip K, which splits in two to make room for it To shuffle insert several clips to another spot in the Timeline: 1 Pick every clip you want relocated to another spot on the Timeline. 2 Hold down the Command and Shift keys and drag the clips left or right. Be sure the item you click to drag sits on the same track as most of the clips you’re reordering; the item you click sets which track governs how the clips get reordered. In the example below, the video item of Clip C is chosen on track V1, so as it’s dragged rightward, the clips on every other track reorder themselves to match the length and placement of clips B and C on track V1. Consequently, clips on tracks apart from V1 may be overwritten or may open gaps, whatever it takes for the items on track V1 to reorder cleanly.

Before and after a batch of clips gets shuffled leftward; the clip you clicked to drag dictates how all the others reorder themselves To shuffle insert several clips, sourced from the Media Pool (or from the Source Viewer), down into the Timeline: 1 Either pick one or more clips sitting in the Media Pool, or load a single clip up in the Source Viewer. 2 Hold down the Command and Shift keys, then drag that selection — whether out of the Media Pool or straight from the Source Viewer — down onto the Timeline. 3 During the drag, each moving clip settles onto the Timeline right where the pointer happens to be. Let go of the mouse to complete the edit.

### Splitting and Joining Clips

There are plenty of moments when you’ll wind up splitting clips (adding edits) so as to break apart several clips that got accidentally fused into one, or to chop clips into segments you intend to treat with separate effects or grade differently. Ways to split and join clips:

- To split a clip a single time: Drag the playhead onto the frame where the split should land, then hit Command-Backslash (\) to cut every clip on a track whose Auto Select is on.
- To split a lot of clips: Click the Razor Edit mode button (or hit B), then click clips in the Timeline to split as many of them as you please.

TIP: Applying the Blade Edit Mode or the Split Clip command to a clip that’s already selected keeps the selection on the front half of the clip once the cut is made.

### Through Edits

Splitting a clip produces a through edit, signaling that the edit you’ve just made carries continuous timecode from the outgoing half into the incoming half. Such an edit is known as a through edit, and it’s marked by a dotted line tracing its edge so its special nature is obvious.

### A through edit seen in the Timeline

To get rid of a through edit, carry out one of these:

- Highlight it in the Timeline and tap Delete.
- Right-click a through edit within the Timeline and pick Delete Through Edit.

TIP: To view a standalone roster of every through edit in the Timeline, open the Edit Index and pick “Show Through Edits” from the Edit Index Option menu. Click any entry in the roster and the playhead leaps to that through edit, which makes it simple to review all the through edits in a timeline and judge whether each is needed.

### Enabling and Disabling Clips and Tracks

While working in the Timeline, you’ll run into moments where you’d like to switch off clips that shouldn’t show up during playback, yet you don’t actually want them gone from the edit. As an instance, a client’s notes might lead you to turn off superimposed clips placed as insert shots partway through a scene, though you’d rather not delete those clips in case the client reverses course.
