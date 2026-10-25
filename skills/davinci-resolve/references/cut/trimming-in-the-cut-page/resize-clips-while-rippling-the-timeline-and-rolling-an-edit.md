# Resize clips while rippling the timeline and rolling an edit

Version: DaVinci Resolve 20.3 Reference Manual. Context: Trimming in the cut page.
[Chapter index](INDEX.md) / [Previous section](overwriting-the-edges-of-other-clips-and-swapping-clips.md) / [Next section](trimming-edits-in-the-viewer.md)
<a id="source-clicking-an-edit-between-clips-cc-and-dd"></a> <a id="source-resize-clips-while-rippling-the-timeline"></a> <a id="source-roll-and-trim-audio-edit-points-to-add-split-edits"></a> <a id="source-rolling-an-edit"></a> <a id="source-slipping-clip-content"></a> <a id="source-trim-or-extend-clip-to-playhead"></a>

### Resize Clips While Rippling the Timeline

In the Timeline or the Upper Timeline, move the pointer onto a clip's far left or right edge and it turns into a Resize icon, signaling that you can drag that clip's In or Out point to shorten or lengthen it, rippling every clip to the right along the Timeline to fit the clip's new length. As you drag, a tooltip reports how many frames you've shifted the clip plus its new duration. Meanwhile the audio scrubs along with the Resize cursor. Resize a clip in Track 1 and the rest of the edited timeline ripples automatically to absorb your changes, with clips right of the altered area sliding left to fill the gap of a deleted or shortened clip, or sliding right to make space for an inserted or lengthened one. Clicking clip DD's Out point in Track 1 Dragging inward to shorten clip DD ripples the Timeline, and a tooltip shows you the number of frames resized Moving or resizing a clip on Track 2 or higher touches only that one clip; the Timeline's other clips stay put and no rippling happens.

Clicking the out point of clip HH in Track 2

Dragging to lengthen the clip doesn’t ripple the Timeline

TIP: If you resize the Out point of a Track 1 clip that sits under a superimposed clip, and that superimposed clip's In point sits rightward of where the resized clip's In point is, then dragging the trimmed clip's Out point leftward past the superimposed clip's In point will delete that superimposed clip from the Timeline.

### Rolling an Edit

Any edit point dividing two clips — whether in the Timeline or the Upper Timeline — can be grabbed and dragged to “roll” it, which essentially resizes the outgoing clip's Out point together with the incoming clip's In point at once. This moves an edit point while leaving the overall timeline's duration unchanged. As you drag, a white overlay in the Timeline shows how much media is on hand for rolling (based on the handles available in the source media). Meanwhile the audio scrubs along with the right clip's In point.

### Clicking an edit between clips CC and DD

Dragging rightward rolls the edit forward, resizing both clip CC and clip DD at the same time

### Slipping Clip Content

Every clip in the Timeline carries a Slip handle at its center. Drag this handle to slip that clip's contents so a different stretch of media shows, all without altering the clip's position or duration, and without touching any other part of the Timeline. You can even pick several clips — two superimposed clips, say, or a run of consecutive clips — and slip them all together. As you drag, a white overlay in the Timeline shows how much media is on hand for slipping (based on the source clip's duration).

(Top) A click on a clip's slip handle, (Bottom) Dragging that slip handle so the stretch of media inside the clip changes

### Roll and Trim Audio Edit Points to Add Split Edits

On the Cut page you can trim a video clip's audio channel on its own. That lets you build a split edit (L-cut or J-cut), where one video clip's audio carries on beneath the video of a different clip. With this you can shape a scene's flow and rhythm through reaction shots and more natural-sounding dialogue.

To Trim Only the Audio and Build a Split Edit on a Cut Page Timeline:

- Enlarge the track on the Cut page by clicking the Enlarge Track icon at the left of the track header. It isn't strictly required, but it makes the tool's trigger point easier to hit and the audio waveform easier to see while you trim.
- Hover the pointer over the edit point in the track's lower audio area. Once the trim icon displays a musical note on its right, you can slide that edit point back and forth so only the clip's audio portion stretches forward or backward.
- The Trim View also shows in the Viewer as you edit, alongside enlarged audio waveforms zoomed to the frame level for accuracy.

Setting the pointer within the track's audio area brings up the trim indicator carrying the musical note icon. With it, you can slide only the audio edit point back and forth along the Timeline while the video stays put.

### Trim or Extend Clip to Playhead

Trimming or extending a clip to a precise length is simple: set the playhead on the Timeline right where the video should begin or end, then choose the matching operation by clicking the Edit Actions icon. To Trim or Extend Clip to Playhead:

- Set the playhead at the spot you want to either extend the clip to or trim the clip off at.
- Click the Edit Actions icon.
- Pick Trim Start to Playhead on the contextual menu to trim or extend the clip's left side to the playhead position.
- Pick Trim End to Playhead on the contextual menu to trim or extend the clip's right side to the playhead position.

The starting Timeline, its playhead landing between the second and third group of “BB’s,”

(Top) How the clip ends up after picking Trim Start to Playhead, (Bottom) How it ends up after picking Trim End to Playhead
