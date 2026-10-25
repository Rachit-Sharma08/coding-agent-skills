# Trim operations that are targeted using the playhead and trim start and trim end

Version: DaVinci Resolve 20.3 Reference Manual. Context: Trimming.
[Chapter index](INDEX.md) / [Previous section](dynamic-trimming-or-jkl-trimming-overview.md)
<a id="source-extend-editing-edit-points"></a> <a id="source-extend-edits"></a> <a id="source-resize-ripple-and-roll-start-and-end-commands"></a> <a id="source-slip-and-slide-playhead-to-in-and-out-commands"></a> <a id="source-trim-operations-that-are-targeted-using-the-playhead"></a> <a id="source-trim-start-and-trim-end"></a>

### Trim Operations that are Targeted Using the Playhead

This next group of Trim editing commands gives you several distinct ways to trim clips and edits, relying on where the playhead sits to steer the outcome.

### Trim Start and Trim End

With the Trim > Trim Start (Shift-[) and Trim End (Shift-]) commands you can shift the In or Out point of every clip crossing the playhead, doing so as a ripple operation (in Trim mode) or as a resize operation (in Selection mode). Since no selection is required to invoke Trim Start and Trim End, these commands are quick to reach for in the right moment. Trim End shines, for example, when you've stacked several clips of varying lengths and want them all to begin or end together.

- Trim Start either resizes or ripples (whichever mode you happen to be in) every clip crossing the playhead, relocating each clip's In point to wherever the playhead currently sits.

A Trim Start operation shown before and after; every clip crossing the playhead gets trimmed

- Trim End resizes or ripples the crossing clips such that each intersecting clip's Out point lands at the current playhead position.

A Trim End operation shown before and after; every clip crossing the playhead gets trimmed, while clips that miss the playhead stay as they were

Any clip that fails to cross the playhead stays untouched. On top of that, you can leave clips on certain tracks out of the operation by switching off the Source Track Selector controls for those tracks.

### Resize, Ripple, and Roll Start and End Commands

A further collection of commands within the Trim menu rolls the Trim Start and Trim End behavior together with picking Selection or Trim mode, plus resize, ripple, or roll capability, all bundled into single commands.

- Resize Start to Playhead
- Resize End to Playhead
- Ripple Start to Playhead (Command-Shift-[)
- Ripple End to Playhead (Command-Shift-])
- Roll Start to Playhead
- Roll End to Playhead

Much like Trim Start and Trim End, these commands consult the Timeline Auto Select controls to decide, among the clips crossing the playhead, which ones on which tracks get trimmed. Most of them ship without keyboard shortcuts assigned, yet if this style suits you, you can bind them to shortcuts of your own choice through the Keyboard Mapping Customization tool (Option - Command - K).

### Slip and Slide Playhead to In and Out Commands

Still another batch of commands in the Trim menu lets you slip a clip from whatever frame the Playhead currently rests on over to that clip's In or Out point.

- Slip Playhead to In
- Slip Playhead to Out

TIP: The Slip Playhead to In command behaves exactly the same as performing an extend edit while the playhead crosses a selected clip. As with Trim Start and Trim End, these commands rely on the Timeline Source Track Selector controls to work out, among the clips crossing the playhead, which ones on which tracks to trim. By default these commands carry no keyboard shortcuts, though if this approach appeals to you, you can attach shortcuts of your own through the Keyboard Mapping Customization tool (Option - Command - K).

### Extend Edits

The Extend Edit command (reached via Trim > Extend Edit, or by pressing E) resizes or ripples one or several selected edit points or clips. In contrast to Trim Start and Trim End, whether the playhead happens to cross any clips is irrelevant during an extend edit.

### Extend Editing Edit Points

Select one item per track from any mix of In or Out points, then tap the E key to send those edit points to wherever the playhead currently sits.

Before and after a multi-track extend edit performed in Selection mode. Beforehand, the red selections signal that you've grabbed the first frame of media for those clips. Afterward, those selections shift to green, signaling that extra frames sit at the head of the edit ready for trimming. Within Trim mode, selected edit points ripple rather than resizing the clips they touch. To keep multi-track extend edit operations manageable while the Trim tool is active, though, the lowest-numbered video track that has auto-select on dictates how far the extend edit ripples the remainder of the Timeline; every other selected edit point on the other tracks merely resizes to the playhead's position.

A multi-track extend edit performed in Trim mode, shown before and after; notice how the lowest-numbered track holding a selection sets the extent to which the Timeline ripples Using Extend Edits to Slide Clips The Extend Edit command can also slide the contents of one selected clip with either the Selection or Ripple tools. Just pick a clip, park the playhead over the frame of that clip you'd like to slip to the In point of that clip's spot in the Timeline, then press E to carry out the slip. This even works during playback, should you want to watch the clip roll and press E to slip that frame back at the instant it feels right.

Using the extend edit to slip a clip within the Timeline; the red marker indicates the frame under the playhead being slipped back to that clip's In point in the Timeline
