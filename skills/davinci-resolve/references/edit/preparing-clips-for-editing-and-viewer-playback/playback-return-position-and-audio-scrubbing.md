# Option to stop and go to last position and enabling and disabling audio scrubbing

Version: DaVinci Resolve 20.3 Reference Manual. Context: Preparing clips for editing and viewer playback.
[Chapter index](INDEX.md) / [Previous section](optimized-ui-layouts-for-vertical-editing.md) / [Next section](gang-viewers-playhead-ganging-and-adding-markers.md)
<a id="source-absolute-timecode-entry"></a> <a id="source-copy-and-paste-timecode-in-viewer-timecode-fields"></a> <a id="source-enabling-and-disabling-audio-scrubbing"></a> <a id="source-how-to-enter-timecode-values"></a> <a id="source-limiting-the-source-tape-scope-by-folder-structure"></a> <a id="source-moving-the-playhead-using-timecode"></a> <a id="source-option-to-stop-and-go-to-last-position"></a> <a id="source-playback-post-roll"></a> <a id="source-relative-timecode-entry"></a> <a id="source-source-tape-in-the-edit-page-source-viewer"></a> <a id="source-user-typed-value-20-3--5"></a>

### Option to “Stop and Go to Last Position”

Playback > Stop and Go to Last Position puts DaVinci Resolve into a mode that, each time you halt, sends the playhead back to the spot where playback originally kicked off. Audio editing is where this proves handiest, though you can call on it whenever you like. While driving the Viewer with the JKL keys under this mode, “K” holds the playhead at its current spot, whereas the space bar (stop) sends it to the last position. The same setting can be reached by right-clicking the Stop button found in the transport controls of any viewer. Doing so opens a contextual menu that lets you flip “Stop and go to last position” on or off as your default behavior.

### Enabling and Disabling Audio Scrubbing

Out of the box, audio scrubbing is turned on, so dragging the playhead forward and backward with the mouse produces sound. That behavior helps when you’re hunting for audio cues, yet it can pull your attention away when the picture alone is your concern. To switch audio scrubbing on or off: Choose Timeline > Audio Scrubbing (Shift-S).

### Playback Post-Roll

Lets the playhead keep rolling beyond the final clip in the Timeline, for a span matching the “Post-roll time” Project Setting found in the Editing panel. It suits editors who like to feel a brief stretch of playback once they’ve cut, or faded to black, past the last frame of picture and sound in the Timeline. To switch Playback Post-Roll on or off: Choose Timeline > Playback Post-Roll.

### Source Tape in the Edit Page Source Viewer

Source Tape, which originated on the Cut page, can likewise be reached from the Edit Page Source Viewer. Turning it on is a matter of picking a bin and then clicking the Source Tape icon at the upper right of the Source Viewer, or hitting Shift-Q. With this turned on, every clip held in the bin you currently have open, plus any subfolders nested inside it, of the Media Pool surfaces in the Source Viewer as a “stringout” within the scroll area along the bottom of the Viewer. There, the clips line up back to back in one long strip, sequenced according to the sort order. That arrangement makes scrubbing across an entire set of clips painless while you work out what you’d like to use. During playback, whatever clip the playhead happens to cross is highlighted in the Media Pool, so you always know which clip is on screen, and you can drop In and Out points onto any clip within the Source Tape.

Editing directly from the Source Tape is also possible on the Edit page. For that, click the Source Tape icon located in the Source Viewer (circled red). When you have a great deal of footage to watch and assess, the Fast Review button now sits at the lower left of the Source Viewer too. Clicking it bumps playback up to a quicker speed, scaled to the duration of whatever clip is showing in the Source Tape.

### Limiting the Source Tape Scope by Folder Structure

Once a project balloons, keeping a whole film’s media loaded in the Source Tape at all times grows cumbersome. You can, however, confine the Source Tape’s reach at the bin level. Clicking straight on bins within the Bin list lets you widen or tighten the Source Tape’s reach in a hurry. Click a bin called Scene02, for instance, and the Source Tape narrows down to display only the clips housed in that folder. Click back onto Master and the Source Tape widens out once more to present clips across every folder. The same trick helps when you’re moving through bin hierarchies that mirror the camera’s original file system. Picture a camera that writes each memory card to its own folder, then stores every individual clip in a separate folder nested within that one. Pull that file system into the Media Pool through the Create Bins option, and those nested tiers carry over into the Media Pool bin hierarchy. From then on, clicking a card bin in the Source tape takes you straight to all of that card’s clips, instead of presenting a heap of separate sub-bins.

### Moving the Playhead Using Timecode

Both absolute and relative timecode entry are at your disposal, either to shift the playhead within the Source and Timeline Viewers, or to nudge or trim whichever edit points or clips you’ve selected. As you work through the Timeline, typing timecode lets you reposition the playhead with great precision, or leap to particular timecode values in an instant. TIP: The timecode-entry approach laid out here underpins a wide range of commands that call for timecode entry, and it’s built around fast, efficient editing.

### How to Enter Timecode Values

As you enter timecode, work left to right through each pair of hour, minute, second, and frame values, leaning on a period to stand in for a pair of zeros and speed things up. Whatever numbers you key in show up in the timecode field at the top right of whichever Viewer holds focus. Once you’ve finished typing, hit the Enter key to carry out the timecode command. These are the rules that govern timecode entry:

- Whatever pair of timecode values (or period) sits farthest to the right in your entry is always taken as the frame number.
- Place a period on either side of a number you type and it counts as a pair of zeroes.
- One period sitting between two numbers reads as a single zero, or gets disregarded when it falls

between two pairs of numbers.

- Any pairs of values to the left that you leave untyped are presumed to keep whatever they held

before the timecode you just entered; that lets you type partial timecode values with ease, even on a Timeline that begins at hour one.

- There’s no requirement to type colons or semicolons.

IMPORTANT: On a full-length keyboard, the number pad supports implicit timecode entry without your having to trigger the Go To Timecode action (=) first. During a multicam or printer light operation, any number pad key that’s already mapped keeps firing its assigned action, such as flipping between angles or stepping color values up. With the number keys that sit above the letters, though, you have to choose Go To Timecode (=) first, or click into the field you mean to change, before you key in a fresh value.

### Absolute Timecode Entry

Entering absolute timecode is just a matter of typing a timecode value. Provided nothing in the way of clips or edit points is selected at the instant you press the Return key, the playhead jumps to that timecode value. Should an edit point or clip be selected, it gets moved or trimmed to the matching timecode value where that’s feasible. Below are a few examples of absolute timecode entry done this way:

Original TC Value 01:10:10:10 01:10:10:10 01:10:10:10 01:10:10:10 01:10:10:10 01:10:10:10 01:10:10:10

User-Typed Value 15245218 2.. 15 12 1.2 1115.. 23...

New TC Value 15:24:52:18 01:02:00:00 01:10:10:15 01:10:10:12 01:10:01:02 11:15:00:00 23:00:00:00

### Relative Timecode Entry

To enter relative timecode, lead the timecode value with either a plus (+) or a minus (–). A plus causes whatever value you type to be tacked onto the current timecode value, so as to offset the playhead or shift a selection. A minus instead deducts the value you type from the current timecode value. Two examples of relative timecode entry follow:

### User-Typed Value +20. +3.. -5

Result 00:00:20:00 gets tacked onto the current timecode value. 00:03:00:00 gets tacked onto the current timecode value. 00:00:00:05 gets taken away from the current timecode value.

### Copy and Paste Timecode in Viewer Timecode Fields

Across the Media, Edit, and Color pages, right-clicking most Viewer timecode fields brings up a contextual menu with Copy and Paste commands for moving timecode values around. Alternatively, click into the timecode fields and lean on the usual Copy (Command-C) and Paste (Command-V) keyboard commands. It even carries over from one page to another. Whatever timecode value you paste has to be valid timecode; you can’t, say, drop 0 hour timecode onto a 1 hour timeline.

Right-clicking on a timecode field to use the Copy Timecode command
