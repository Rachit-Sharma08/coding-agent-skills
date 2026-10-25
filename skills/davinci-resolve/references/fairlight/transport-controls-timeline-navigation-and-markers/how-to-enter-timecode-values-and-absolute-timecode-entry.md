# How to enter timecode values and absolute timecode entry

Version: DaVinci Resolve 20.3 Reference Manual. Context: Transport controls timeline navigation and markers.
[Chapter index](INDEX.md) / [Previous section](transport-controls-and-jkl-navigation-and-transport-controls.md) / [Next section](flags-and-markers.md)
<a id="source-absolute-timecode-entry"></a> <a id="source-clip-marker-and-track-navigation"></a> <a id="source-how-to-enter-timecode-values"></a> <a id="source-moving-the-clip-selection"></a> <a id="source-moving-the-track-selection"></a> <a id="source-relative-timecode-entry"></a> <a id="source-scrolling-through-the-timeline"></a> <a id="source-selecting-tracks"></a> <a id="source-setting-the-zoom-level-of-the-timeline"></a> <a id="source-the-playhead"></a> <a id="source-user-typed-value-20-3-5"></a> <a id="source-zooming-and-scrolling"></a>

### How to Enter Timecode Values

To enter timecode, type each pair of hour, minute, second, and frame values going left to right, where a period stands in for a pair of zeros to speed entry. Whatever numbers you type show up in the Timecode field at the upper right-hand corner of the focused Viewer. Once you've finished typing, hit the Enter key to run the timecode command. These are the rules for timecode entry:

- Whatever right-most pair of timecode values (or period) you type always stands for the frame number.
- A period sitting to the left or the right of any number you type counts as a pair of zeroes.
- One period set between two numbers counts as either a single zero, or is disregarded when it falls

between two pairs of numbers.

- Any value pairs left untyped to the left of your entry are taken to be whatever those values

held before the timecode you typed; this lets you type partial timecode values easily even where the Timeline begins at hour one.

- Typing colons or semicolons isn't required.

IMPORTANT: On full length keyboards, the number pad supports implicit timecode entry without your having to trigger the Go To Timecode action (=). During a multicam or printer light operation, any number pad key that's already mapped keeps triggering actions such as swapping angles or stepping color values. With the number keys above the letters on a keyboard, you must first pick Go To Timecode (=), or click inside the field you mean to alter, ahead of typing a fresh value.

### Absolute Timecode Entry

You enter absolute timecode just by typing the timecode value you'd like the playhead moved to, and once you press the Return key, the playhead jumps to that timecode value.

Below are a few examples of absolute timecode entry done this way:

Original TC Value 01:10:10:10 01:10:10:10 01:10:10:10 01:10:10:10 01:10:10:10 01:10:10:10 01:10:10:10

User-Typed Value 15245218 2.. 15 12 1.2 1115.. 23...

New TC Value 15:24:52:18 01:02:00:00 01:10:10:15 01:10:10:12 01:10:01:02 11:15:00:00 23:00:00:00

### Relative Timecode Entry

You enter relative timecode by leading the timecode value off with a plus (+) or minus (–). Putting a plus means the value you type gets added onto the current timecode value, so as to offset the playhead away from where it currently sits. Putting a minus means the value you type gets taken off the current timecode value. Below are three examples of relative timecode entry:

### User-Typed Value +20. +3.. –5

Result 00:00:20:00 is added to the current timecode value. 00:03:00:00 is added to the current timecode value. 00:00:00:05 is subtracted from the current timecode value.

### Clip, Marker, and Track Navigation

The Up and Down Arrow keys serve to shift the playhead between one edit point and the next on the Fairlight page Timeline, exactly as on the Edit page Timeline. But holding Command-Option while you work the Arrow keys hands you Fairlight page-specific behaviors meant for moving among clips, markers, and tracks on the Fairlight page in a manner unlike the other DaVinci Resolve pages yet well suited to how the Fairlight page works. This section runs through the basics.

### Selecting Tracks

The behavior of the Arrow keys is set by which tracks you've selected.

- In Pointer mode: Tracks get selected by clicking or Command-clicking (for several tracks at once) anywhere across the background area or on the track number within the track headers. Clicking and dragging in the track header lets you draw a bounding box to grab several tracks. Pointer mode won't make selections in the Timeline's empty areas.
- In Range or Focus mode: You select tracks by clicking or Command-clicking anywhere, whether over the header's background, on the header's track number, or across any unused portion of the track itself inside the Timeline. A click-and-drag here lets you draw a bounding box to grab several tracks.

### Moving the Clip Selection

The Command-Option-Left and Command-Option-Right Arrow key shortcuts serve to shift the playhead left and right within the Timeline, hopping clip to clip or marker to marker. The way these keys behave turns on whether or not one or more tracks sits selected in the Timeline.

- If no tracks are selected: The Left and Right Arrow keys leap the playhead from one Timeline marker to the next. Clip markers get skipped.
- If one or more tracks are selected: The Left/Right Arrow keys leap the playhead among clip In points, clip Out points, and Timeline markers.

### Moving the Track Selection

The Command-Option-Up and Command-Option-Down Arrow key shortcuts serve to shift the track selection up and down within the Timeline, altering which tracks are selected. By altering which tracks sit selected, you change which clip's In and Out points get used to leap the playhead around the Timeline. With no tracks selected, nothing occurs.

### Zooming and Scrolling

The Fairlight page offers several ways to zoom into and out of the Timeline, plus scrolling once you're zoomed far enough that your edited run of clips spills past the left and right edges of the visible timeline.

### The Playhead

Zooming always centers on wherever the Playhead sits. By default the Playhead travels along the Timeline during playback. Fairlight, though, gives you the choice of a Fixed Playhead, where the Timeline shifts while the Playhead stays centered.

You'll find the Playhead options inside the Timeline Scrolling panel.

### Setting the Zoom Level of the Timeline

Your working style dictates which of the several Timeline zoom-in and zoom-out methods suits you. Using the Vertical Zoom slider: Two sliders sitting at the toolbar's right edge handle both vertical and horizontal zoom. The first scrolls you vertically, surfacing more detail across your waveforms' height. Where no tracks sit selected, the zoom centers on the Timeline's top audio track. Where one or more tracks sit selected, the zoom centers on the uppermost selected audio track. Using the Horizontal Zoom slider: That same right-side toolbar pair of sliders covers vertical and horizontal zoom alike. The second zooms you horizontally, surfacing more detail across your waveforms' width. Pressing Command-Equal (=) and Command-Minus (–): Both Command-Equal (which also goes by Command-Plus) and Command-Minus zoom you horizontally into the Timeline. Use Shift-Z to Zoom to Fit: Horizontal zooming via Command-Z shrinks every clip in your program to whatever width the Timeline has on hand. Using scroll controls of your pointing device to scroll horizontally: Hold the Option key as you spin the scroll wheel (or scroll control) on your pointing device and you zoom horizontally into the Timeline. Hold the Command key as you spin the scroll wheel and the Timeline slides to a time earlier or later than now, leaving the Playhead put. Using scroll controls of your pointing device to scroll vertically: Hold the Shift key as you spin the scroll wheel (or scroll control) to zoom vertically inside the Timeline. In this case, where no tracks sit selected, the zoom centers on the Timeline's top audio track. Where one or more tracks sit selected, the zoom centers on the uppermost selected audio track. Using the Fairlight panel's Jog/Edit wheel: With a Fairlight panel on hand, holding the ZOOM button down as you spin the Jog/Edit wheel zooms into the Timeline at the playhead's location.

### Scrolling Through the Timeline

No matter how tightly you're zoomed into the Timeline, once you're zoomed far enough that clips run past the Timeline's visible area, scroll bars show up below. Should the playhead be offscreen, a little orange tic mark flags where it sits relative to the whole timeline, which the full width of the scroll bar's background stands in for. When you drag the playhead, or use any of the transport controls or playback key shortcuts to travel through the Timeline, the Timeline's contents refresh each time the playhead strikes the left or right edge of what's on view.
