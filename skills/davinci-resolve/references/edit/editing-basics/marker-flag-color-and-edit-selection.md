# Selecting clips based on markers flags and clip color and selecting edits in the timeline

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing basics.
[Chapter index](INDEX.md) / [Previous section](manually-selecting-clips-in-the-timeline-overview.md) / [Next section](track-selection-locking-and-destinations.md)
<a id="source-a-practical-example-of-keyboard-driven-selections"></a> <a id="source-defining-selections-with-the-help-of-destination-track-selector-controls"></a> <a id="source-selecting-an-edit-point-to-roll"></a> <a id="source-selecting-clips-based-on-markers-flags-and-clip-color"></a> <a id="source-selecting-edits-in-the-timeline"></a> <a id="source-using-destination-track-selector-controls-to-define-selections"></a>

### Selecting Clips Based on Markers, Flags, and Clip Color

You can also grab several clips at once when they share a given marker color, flag color, or clip color. This comes in handy any time you've been leaning on those organizational aids to track clips carrying particular traits that you may later want to round up for batch operations. As an illustration, you could tag a run of audio clips with purple markers because they call for distinct EQ treatment. Afterward, picking Timeline > Select Clips By Marker Color > Purple grabs every one of those clips so you can relocate them to a different track and treat them all with one track-level audio filter. Three different routes exist for grabbing clip groups this way. To select groups of clips based on marker, flag, or clip color:

- Choose Timeline > Select Clips By Flag Color > Blue – Cream
- Choose Timeline > Select Clips By Marker Color > Blue – Cream
- Choose Timeline > Select Clips By Clip Color > Orange – Chocolate

### Selecting Edits in the Timeline

Many of the editing and trimming techniques expect you to first grab an edit point, or one side of an edit point, before you can resize, ripple, or roll it. Either the mouse or the keyboard will get the job done. Methods for selecting edit points using the mouse:

- To select an edit to roll: Bring the mouse over the middle of an edit point, and once the ripple cursor shows up, click to grab the edit.

### Selecting an edit point to roll

- To grab only one side of an edit point, the incoming or the outgoing, for resizing or rippling: Bring the mouse just left or right of an edit's center, and once the resize/ripple cursor shows up, click to grab that side of the edit.

Grabbing an edit point's incoming or outgoing half to resize or ripple it

To select multiple edit points, do one of the following:

- To select multiple roll points: Command-click the middle of several edit points. To drop one you've already grabbed, Command-click that edit point again.

Command-clicking the middle of multiple edits in readiness to roll the whole set

- To select multiple ripple points: Command-click either the left or the right side of several edit points.

Command-clicking either side of multiple edits to ripple the whole set

- To drag to select many edit points: Pick the Trim tool (T), then drag a bounding-box across the edit points you'd like to grab. Pressing U cycles every chosen edit point through rippling incoming edits, rippling outgoing edits, and rolling edits.

With the Trim tool you can drag a bounding box across several edits to grab them. A versatile collection of keyboard shortcuts also stands ready, making it simple to grab edit points ahead of various operations whenever you'd sooner skip the mouse.

Keyboard shortcuts for selecting edits: V — grabs the edit point closest to the playhead on the lowest track that has Source Track Selector switched on, taking the clip's audio and video edit points as a pair. Option-E — grabs the closest video edit point to the playhead on that same lowest track carrying Source Track Selector enabled, while leaving any linked audio edit points untouched. Shift-E — on the lowest track whose Source Track Selector is on, grabs the audio edit point nearest the playhead, while leaving any linked video edit points untouched. U — after an edit point is grabbed, this shortcut cycles through grabbing the outgoing half, the incoming half, or the whole edit. Option-U — after an edit point is grabbed, this shortcut cycles through grabbing the edit's video+audio, the video only, or the audio only.

To move the selection to another edit:

- Grab a single edit point, then move the selection to whichever edit point precedes or follows it across every track by pressing Up Arrow key (Previous Edit) or, for the one after, Down Arrow key (Next Edit).

To deselect all edit points:

- Using the mouse: Click any empty area of the Timeline.
- Using the keyboard: Press Shift-Command-A.

### A Practical Example of Keyboard-Driven Selections

What follows shows how these shortcuts chain together into a single run of steps. To select an edit point using the keyboard: 1 Hit Command-4 to hand focus to the Timeline. 2 Bring the Timeline playhead near the edit point you're after by working the JKL keys. 3 Hit the V key to grab the nearest edit point to the playhead on the lowest track that has Destination Track Selector enabled. Should superimposed clips overlap on several tracks, switch off the Destination Track Selector controls for tracks whose edits you'd rather skip, using Option-F1 through Option-F8, which line up with the Destination Track Selector controls on tracks 1–8. With the mouse, Option‑clicking a track's Destination Track Selector button solos that track's Destination Track Selector state. (Option-F9 flips the Destination Track Selector controls for every video track.) 4 At first the whole edit is grabbed, set up for a roll edit. Press the U key to cycle among grabbing the outgoing half, the incoming half, and the full edit. 5 Press Option-U to cycle among grabbing the edit's video+audio, only the video, or only the audio. 6 Carry out whatever you came to do. Once done, shift the selection earlier or later in the Timeline with Up-Arrow or Down-Arrow, or hit Command-Shift-A to clear it.

### Using Destination Track Selector Controls to Define Selections

The Timeline Destination Track Selector controls are remarkably handy, flexible controls that fill numerous roles. Put simply, they let you declare which tracks get acted on or weighed when you run an operation across multiple superimposed clips spread over several Timeline tracks. On top of that, the Timeline Destination Track Selector controls really shine when you're editing by keyboard and would rather not reach for the mouse just to pick out a single clip, given that Destination Track Selectors can be switched on or off through keyboard shortcuts.

### Defining Selections With the Help of Destination Track Selector Controls

Here's the most straightforward case showing why the Destination Track Selector controls matter. Picture an example holding two superimposed video clips alongside three superimposed audio clips. Say you intend to clear the media off tracks V2, V1, and A1 while leaving whatever sits on A2 and A3 untouched; you'd switch off the Destination Track Selector controls for tracks A2 and-A3, then place Timeline In and Out points marking the span of clips you mean to remove. Pressing the Delete key then clears only the media on the tracks whose Destination Track Selector is enabled.

Before and after a clip is deleted, with the Destination Track Selectors (red) switched on for Tracks V2, V1, and A1 and switched off for Tracks A2, and A3 TIP: When you've placed In and Out points for an operation yet spot no shading in the Timeline marking which stretches will and won't be touched, odds are some other selected clip is lurking out of view in the Timeline and overriding the Destination Track Selectors. Hit Command-Shift-A to de-select everything and matters should return to normal.
