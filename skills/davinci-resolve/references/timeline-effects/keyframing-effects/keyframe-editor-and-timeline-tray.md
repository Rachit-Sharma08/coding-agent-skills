# The keyframe editor and opening the keyframe tray in the timeline

Version: DaVinci Resolve 20.3 Reference Manual. Context: Keyframing effects.
[Chapter index](INDEX.md) / [Previous section](imeline-playback-keyframing-and-curve-editor.md) / [Next section](curve-editor-open-in-the-timeline-and-curve-editor.md)
<a id="source-opening-the-keyframe-tray-in-the-timeline"></a> <a id="source-using-the-keyframe-editor"></a>

### Using the Keyframe Editor

With the Keyframe Editor open and the parameters you mean to animate revealed, you have plenty of ways to add, remove, and reshape the keyframes sitting on these tracks. Reading left to right, the Keyframe Track controls run: Toggle Curve Visibility, then Toggle Keyframe Lock, next Track Color, followed by Track Name, then Keyframe, then Reset Keyframes, and finally Keyframe position. The Keyframe Track Controls are:

Toggle Curve Visibility: Click this icon to switch this track’s curve visibility on or off in the Curve Editor.

Toggle Keyframe Lock: Click this icon to switch the keyframe lock on or off and guard against unintended changes.

Track Color: A tiny colored dot indicates the color of the track’s curve in the Curve Editor.

Track Name: The name of the track parameter.

Keyframe: Clicking the diamond drops a new keyframe at the present position. When a keyframe is active at that position the diamond shows orange, otherwise white. The left and right arrows jump to the previous and next keyframes respectively.

Reset Keyframes: Clears every keyframe in the track. Keyframe Position: Displays all the track’s placed keyframes and where they fall within the clip.

Methods of adding and selecting keyframes in the Keyframe Editor:

- To add new keyframes to the Keyframe Editor: Move the playhead to where the keyframe should go, then click the grey diamond beside the parameter’s name. The diamond shifts to orange to confirm a keyframe was added, and it also turns up on the parameter track at the playhead position. You can lay further keyframes on this track by pressing Command [ to add another keyframe.
- To select a single keyframe: Click a single keyframe to select it.
- To select multiple discontiguous keyframes: Command-click each keyframe you want, whether or not they sit beside one another.
- To select multiple contiguous keyframes: Drag a bounding box inside the keyframe track around several keyframes to grab them all together.
- To move one or more keyframes: Pick one or more keyframes and drag left or right.
- To nudge keyframes: Pick the keyframe(s) you intend to move. They can be nudged up/down/

left/right by one frame, via the Mark > Move Selected Keyframe … menu items. You can (and, for the sake of usability, probably should) bind these commands to keyboard shortcuts.

- To toggle all keyframe parameters at once: Shift click the lock or show curve icons in the curve editor.
- To “solo” a keyframe parameter: Option-click the lock or show curve icons in the curve editor to “solo” the chosen parameter exclusively. Option-click once more to exclusively switch off the chosen parameter and turn the rest back on.

Methods of Cutting, Copying, Pasting, and Deleting keyframes:

- To cut or copy, and paste one or more keyframes: Build a selection of keyframes, and reach for the Cut (Command-X) or Copy (Command-C) key shortcuts. Next, slide the playhead to where the first of the copied keyframes should begin, and hit Paste (Command-V).
- To delete one or more keyframes: Pick the keyframe(s) you want gone and press Delete.

IMPORTANT: Keyframes on the Timeline can live beyond a clip’s present extents. As an example, if you place several keyframes on a clip and then trim its Timeline duration past one of them, that keyframe shows up as a directional arrow rather than a point. You can still reach these keyframes through the Previous “[“ and Next “]” keyframe commands or via the keyframe controls in the Inspector.

From left to right, these Keyframe Editor controls appear: Curves Editor, then Keyframe Editor, next Detail Zoom, followed by Full Extend Zoom, then Zoom Slider, then Expand, and lastly Option Menu.

Curves Editor: Click this icon to open the Curves Editor.

Full Extend Zoom: Zooms the Keyframe Editor out far enough to show the whole clip’s range.

Parameters: Click this icon to open the Keyframe Editor.

Zoom Slider: Lets you pick a custom zoom level for the Keyframe Editor

Detail Zoom: Zooms the Keyframe Editor in around the playhead position.

Expand: Opens the Keyframe and Curves Editor in its own resizable window.

Option Menu:

- Display Time Ruler in Seconds: Renders the time ruler in HH:MM:SS:FF timecode format drawn from the timeline.
- Display Time Ruler in Frames: Renders the time ruler as a frame count measured from the timeline start.
- Snap Keyframes to Grid: Once turned on in the Curve Editor, this snaps keyframe control points onto the playhead position.
- Show Curve Tooltips: Once turned on in the Curve Editor, hovering the pointer over a curve reveals its track name and value at that point.

Parameters: Shows a list of keyframable parameters. Option Menu:

- Display Parameters with Keyframes: Reveals only tracks holding existing keyframes and hides the rest.
- Display All Video Parameters: Reveals every keyframable track from the Video Inspector and hides the rest.
- Display Selected Parameters (Video & Audio): Brings up a checkbox for switching individual track visibility on or off. Moreover, when you have added a keyframable Open FX or Resolve FX onto the clip, you can pick those parameters here.

Expand All Parameters: Throws open every group track to reveal its enclosed parameters. Collapse All Parameters: Shuts every group track to hide its enclosed parameters.

### Opening the Keyframe Tray in the Timeline

Apart from the dedicated Keyframe Editor panel, a keyframe tray can be summoned right on the timeline: on both the Cut and Edit pages, click the Show Keyframe Tray icon found on the main timeline toolbar. Every keyframe belonging to the timeline’s currently selected clip is laid out by this keyframe tray, which works just like the Keyframe Editor.

You can bring the Keyframe Editor up directly in the timeline by clicking the Show Keyframe Tray icon (circled red). Clicking the curves icon in the keyframe tray lets you tune the values and timings of a timeline keyframe using the very same keyframing controls found in the keyframe editor.

Reaching the Curves editor on the timeline is a matter of clicking this keyframe-tray icon
