# Summarizing trim operations and selection based trimming using the trim tool

Version: DaVinci Resolve 20.3 Reference Manual. Context: Trimming.
[Chapter index](INDEX.md) / [Next section](two-up-roll-and-ripple-display.md)
<a id="source-4-up-display-when-sliding-a-clip"></a> <a id="source-four-up-display-when-slipping-a-clip"></a> <a id="source-how-the-trim-tool-differs-from-the-selection-tool"></a> <a id="source-rippling-gap"></a> <a id="source-selected-edit-point-before-roll"></a> <a id="source-selecting-edit-points"></a> <a id="source-selection-based-trimming-using-the-trim-tool"></a> <a id="source-summarizing-trim-operations"></a> <a id="source-trimming"></a> <a id="source-trimming-part-1"></a> <a id="source-using-the-trim-tool-with-the-mouse"></a>

### Trimming

Ask most cutters and they'll tell you that trimming accounts for roughly half of an editor's work. The Timeline lets you adjust your cut in plenty of ways with the selection and razor blade tools, but there's also a separate Trim mode that handles the more involved trim operations in fewer steps, driven by either the pointer or the keyboard according to your preference. Getting comfortable with DaVinci Resolve's trimming operations pays off in saved time during the unavoidable work of polishing a cut.

### Summarizing Trim Operations

Ahead of covering the various trimming approaches on offer, anyone just starting out with editing may find it helpful to read a short rundown of what each trimming operation does. Every trim operation exists to let you reposition edits and clips relative to their neighboring clips by carrying out a handful of operations together. There are five primary methods of trimming:

- Resize: Trims back or extends an outgoing clip's tail or an incoming clip's head, either overwriting an adjacent clip or leaving behind a gap as required. Although it's not normally counted among the "trim" operations, it's really the most basic form of trimming there is.
- Roll: Moves an edit point to the left or right, either by shortening the outgoing clip as it lengthens the incoming clip, or the reverse. Such edits leave the overall Timeline's duration unchanged.
- Ripple: Trims back or extends an outgoing clip's tail or an incoming clip's head and, at the same time, shifts every clip either rightward (when you ripple to lengthen a clip) or leftward (when you ripple to shorten a clip), so as to close the gap or avoid the overwriting that a resize operation would otherwise cause. This kind of edit does alter how long the overall Timeline runs and, if you're careless, can disturb the sync relation between different tracks.
- Slip: Pins a clip in place on the Timeline while swapping out the range of media shown at that location. A slip leaves the overall Timeline's duration as it was.
- Slide: Holds a clip's range of media constant but shifts the clip left or right, either shortening the outgoing clip on its left as it lengthens the incoming clip on its right, or the reverse.

### Selection-Based Trimming Using the Trim Tool

What sets Trim mode apart from Selection mode is that actions that would shift clips with the Selection tool instead slip or slide clips with the Trim tool. Likewise, actions that the Selection tool would treat as resizing edits will instead ripple the Timeline to close gaps automatically when the Trim tool is active. The sections that follow walk through the various trim operations on offer, covering both pointer use and keyboard use. Getting into Trim Edit mode is a matter of one action: Click the Trim Edit button, or press the T key.

### How the Trim Tool Differs From the Selection Tool

Beyond the trimming operations themselves, a handful of other meaningful distinctions separate the Trim tool from the Selection tool.

### Selecting Edit Points

With the Trim tool active, dragging a bounding box across a run of clips in the Timeline picks the edit points that join clips together rather than the clips themselves. That makes it quick and convenient to grab several edit points you intend to work on at the same time.

Using the Trim tool to select Timeline edit points. Rippling the Timeline With Different Operations. While the Trim tool is active, any other commands and controls that would otherwise resize one or more clips and leave gaps behind will instead shift (ripple) the clips positioned to the right of whichever clip or edit you trim over, moving them leftward, so that no gaps open up whenever clips or edits are repositioned or resized.

Resizing Clip L by rippling its incoming edit point, where the clips on the right (Clips P, L, and N) shift over to the left so no gap shows up. Take, for instance, these: the Retime controls, the Extend and Trim Start/End commands, plus the Nudge keyboard shortcuts. Each one behaves differently according to whether the Selection or Trim tool is in use. So one set of tools can carry out distinct operations based on what you're trying to accomplish.

### Rippling Gap

A gap's start and end in the Timeline can likewise be rippled with the Trim tool, or with the other trim operations described later in this chapter. When you ripple a gap, you enlarge or contract it while whatever portion of the Timeline lies past the gap on its right slides forward or backward in time. Any time you ripple against a gap, a 2-up display appears so you can see both the clip you're trimming and whatever superimposed clips happen to be visible through the gap.

Narrowing a gap by rippling its Out point with the Trim tool. TIP: While running these operators, you can briefly switch between the selection (A) and trim tools (T) to observe what they do. Letting go of the key returns you to whichever mode was originally chosen.

### Using the Trim Tool With the Mouse

Trimming with the pointer lets you carry out every available kind of trim operation from one tool: just click the Trim mode/tool button and then drag on the appropriate part of whichever Timeline clip you're working on. Here are the pointer-driven trimming methods available in Trim Edit mode:

- To slip a clip: To slip a clip's range of content while it stays put on the Timeline, click on a clip's middle top region, then drag left or right to "slip" the clip so it holds a different range of frames. A dashed overlay indicates the full duration of media you have available to slip with, shifting left and right as you drag.

Before a slip, clicking the upper clip area brings up an overlay that shows the media range a clip has available.

Once dragged to slip, the clips stay put, though the slipped clip now draws on a different media range. When you slip clips, a 4-up display presents all the relevant outgoing and incoming frames so you can judge how the action carries from one clip to the next. Mid-slip, the top two frames refresh to reveal the clip's new incoming and outgoing frames as it's slipped, set against the fixed outgoing frame of the clip on the left and incoming frame of the clip on the right.

TIP: You can briefly turn off this four-up display by holding the Shift key as you slip, leaving only the frame at the playhead position visible. That lets you watch which frame crosses the playhead while you ripple the Timeline. To switch this two-up display off entirely, select View > Enable Multiview Edit Preview.

### Four-up display when slipping a clip

- To slide a clip: To slide a clip, moving it somewhere else along the Timeline while, to absorb the dragged clip's shift in position, the previous clip's Out point together with the next clip's In point adjust in tandem, grab the clip's bottom-middle name bar and drag it to a fresh spot.

Once dragged to slide, the chosen clip occupies a new location and the neighboring clips have closed the gap. When you slide clips, a 4-up display presents all the relevant outgoing and incoming frames so you can judge how the action carries from one clip to the next. Mid-slide, the bottom two frames refresh to reveal the new outgoing frame of the clip on the left and the new incoming frame of the clip on the right of the clip being slid.

TIP: You can briefly turn off this four-up display by holding the Shift key as you slide, leaving only the frame at the playhead position visible. That lets you watch which frame crosses the playhead while you ripple the Timeline. To switch this two-up display off entirely, choose View > Enable Multiview Edit Preview.

### 4-up display when sliding a clip

- To roll an edit point: To roll an edit, moving in unison the outgoing clip's Out point along with the incoming clip's In point, take an edit point that sits between two clips and drag it leftward or rightward. (Selection mode supports roll edits as well.)

### Selected edit point before roll

The edit point shifted rightward, with both neighboring clips resized so no gap forms

When you roll an edit, a 2-up display reveals how the action's continuity shifts from the outgoing frame of the clip on the left to the incoming frame of the clip on the right, and you'll hear the audio scrubbing of the right clip.
