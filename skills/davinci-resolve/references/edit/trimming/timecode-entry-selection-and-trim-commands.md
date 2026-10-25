# How to enter timecode values and commands to make selections and trim

Version: DaVinci Resolve 20.3 Reference Manual. Context: Trimming.
[Chapter index](INDEX.md) / [Previous section](two-up-roll-and-ripple-display.md) / [Next section](ripple-trim-and-sync-lock.md)
<a id="source-commands-to-make-selections-and-trim"></a> <a id="source-how-to-enter-timecode-values"></a> <a id="source-ripple-editing-rules"></a> <a id="source-trimming-clips-in-the-source-viewer"></a> <a id="source-trimming-part-2"></a>

### How to Enter Timecode Values

To enter timecode, type each pair of hour, minute, second, and frame values working left to right, using a period to stand for a pair of zeros so entry goes faster. Whatever numbers you type show up in the timecode field at the top right of the Viewer that has focus. Once you've finished typing, press the Enter key to run the timecode command. These are the rules for timecode entry:

- Whatever pair of timecode values (or period) you type furthest to the right always stands for the frame number.
- Placing a period on either side of any digit you type counts as a pair of zeroes.
- A lone period set between two digits counts as a single zero, or is dropped altogether when it falls

between two pairs of numbers.

- Any pairs of values you leave untyped to the left of your entry default to whatever those values

held before the timecode you entered; that lets you key in partial timecode values with ease, even where the Timeline starts at hour one.

- There's no need to type colons or semicolons.

IMPORTANT: On full length keyboards, the number pad supports implicit timecode entry without you having to invoke the Go To Timecode action (=). During a multicam or printer light operation, any number pad key that's already mapped keeps invoking actions such as switching angles or incrementing color values. With the number keys above the letters on a keyboard, you have to first choose Go To Timecode (=) or click in the field you want to change before you type a new value.

To enter absolute timecode you simply type in a timecode value. As long as no clips or edit points are selected at the moment you press the Return key, the playhead jumps to that timecode value. When an edit point or clip is selected, it gets moved or trimmed to match the timecode value, where that's possible. Below are several examples of absolute timecode entry done this way:

Original TC Value 01:10:10:10 01:10:10:10 01:10:10:10 01:10:10:10 01:10:10:10 01:10:10:10 01:10:10:10

User-Typed Value 15245218 2.. 15 12 1.2 115.. 23...

New TC Value 15:24:52:18 01:02:00:00 01:10:10:15 01:10:10:12 01:10:01:02 01:15:00:00 23:00:00:00

You enter relative timecode by beginning the timecode value with a plus (+) or minus (–). A plus causes the value you type to be added to the current timecode value when offsetting the playhead or moving a selection. A minus causes the value you type to be subtracted from the current timecode value.

Here are two examples of relative timecode entry: +20. 00:00:20:00 is added to the current timecode value. -5 00:00:00:05 is subtracted from the current timecode value.

### Commands to Make Selections and Trim

A group of commands in the Trim menu makes it quick to automatically pick the In or Out point of whichever clip sits nearest the playhead's current position, and to drop into either Selection or Trim mode ready to resize or ripple trim that edit point. The commands are:

- Select Nearest Edit to Resize In
- Select Nearest Edit to Resize Out
- Select Nearest Edit to Ripple In
- Select Nearest Edit to Ripple Out
- Select Nearest Edit to Roll
- Select Nearest Clip to Move
- Select Nearest Clip to Slip
- Select Nearest Clip to Slide

These commands resemble combining the Edit Selection (V) or Clip Selection (Shift-V) keyboard shortcuts with those for picking the Selection (A) or Trim tool (T) all in one move, to set you up for trimming the way you intend. They carry the extra advantage, in some instances, of letting you specifically pick the In or Out points of the clip closest to the playhead's current position. None of these commands have keyboard shortcuts by default, but if this style suits you, you can map them to shortcuts of your choosing via the Keyboard Customization tool (Option - Command - K).

### Trimming Clips in the Source Viewer

Another option is to double-click a clip in the Timeline so it loads into the Source Viewer for trimming. While the Selection tool is active, dragging the In and Out markers, or working with the playhead plus the I and O keyboard shortcuts, resizes that clip back in the Timeline. While the Trim tool is active, the clip's In and Out points can be rippled.

Ripple-resizing a Timeline clip after loading it into the Source Viewer, dragging its In point with the Trim tool

To slip the clip's contents, keep the Shift key held and drag either the In or Out point.

Slipping a Timeline clip after loading it into the Source Viewer, Shift-dragging its In point with the Trim tool

NOTE: To bring a match frame of a clip that belongs to an edited sequence into the Source Viewer with the pointer, hold the Option key down as you double-click a clip in the Timeline.

### Ripple Editing Rules

Ripple operations are the lone trim functions that alter the duration of the overall Timeline and that may potentially shift the sync relationship across multiple clips on different tracks. That makes them tremendously handy, but it's important to grasp which portions of the Timeline will move during a ripple operation and which won't. These are the operations that ripple the Timeline:

- Ripple deleting a gap or clip (Forward-Delete)
- Ripple cutting any clip (Shift-Command-X)
- Rippling a single edit or several edits or gaps via the Trim tool (press T for the Trim tool)
- Issuing the Extend Edit (E), Trim Start (Shift-[), or Trim End (Shift-]) commands while in Trim mode
- Issuing Ripple Start (Command-Shift-[) or Ripple End (Command-Shift-]) from within any mode
- Carrying out an insert edit (F9) or a ripple overwrite edit (Shift-F10)
- Applying the Retime controls to accelerate or decelerate a clip while in Trim mode
- Working in the Change Speed dialog with the Ripple Sequence checkbox switched on
- Swapping clips inside a Take Selector while the Ripple control is enabled

The Edit page timeline's ripple behaviors aim to keep sync intact across the majority of scenarios. Practically, that means lengthy overlapping superimpositions like titles, graphics, and music beds hold their position as you ripple individual clips inside a montage that's being cut against those longer elements. Any track whose relative sync you wish to maintain must have its Sync Locks (covered further down) switched on in the Track Header. Once Sync Locks are turned on:

- Ripple trimming will keep sync intact automatically for every clip lying both ahead of and behind the ripple edit point.
- To let you carry out insert trims, clips sitting on other tracks may be cut.
- At the ripple trim edit point, clips on the remaining tracks are trimmed automatically so they don't

occlude the tracks beneath them.
