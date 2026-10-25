# Marker colors ranges and properties

Version: DaVinci Resolve 20.3 Reference Manual. Context: Marking and finding clips in the timeline.
[Chapter index](INDEX.md) / [Previous section](flags-and-markers.md) / [Next section](viewer-feedback-annotations.md)
<a id="source-a-marker-with-duration-in-the-timeline"></a> <a id="source-changing-marker-timing"></a> <a id="source-copy-and-paste-multiple-markers-in-the-viewers-and-timeline"></a> <a id="source-editable-properties-in-the-marker-dialog"></a> <a id="source-editing-marker-information-and-keywords"></a> <a id="source-individually-mappable-marker-color-commands"></a> <a id="source-marker-notes-in-data-burn-ins"></a> <a id="source-saving-in-and-out-point-ranges-as-markers-with-duration"></a>

### Individually mappable marker color commands

### Saving In and Out Point Ranges As Markers with Duration

You can also build markers with duration to keep tabs on any stretch of a clip or timeline you’ve bounded with In and Out points. This gives you a way to flag several stretches of a clip you might later cut into a program. To turn a pair of In and Out points into a duration marker: 1 On the Source Viewer jog bar, set In and Out points to mark out a region you’d like to log for later reference.

Setting In and Out points so as to log that portion of the clip. 2 Then do one of these:

- Right-click the jog bar and pick Convert In and Out to Duration Marker
- A marker with duration shows up above the In and Out points. Want to revise its name or notes? Double-click the marker, hit Shift-M, or else choose Mark > Modify Marker.

A marker with duration is created from the In and Out points. By this means you can log several stretches within one clip for later use.

A clip with multiple logged sections identified via markers with duration. This logging technique earns its keep for a couple of reasons. For one, you can search markers with duration in the Media Pool through the All Fields, Marker Name, and Marker Notes Filter by options. For another, Smart Bins can filter them via the Marker Name and Marker Notes Media Pool Properties options.

### Editing Marker Information and Keywords

After you’ve set a few markers, you may want to revise their contents to make them more useful. To bring up a marker’s edit dialog and change its properties: 1 Do one of these:

- Press Command-M to set a marker during playback and open its edit dialog at once.
- Double-click whichever marker you want to edit.
- Bring the playhead to the frame holding the marker you want to annotate using Shift-Up

Arrow/Down Arrow, then press M.

- Select a marker anywhere in the Source Viewer or Timeline, then press Shift-M.

2 With the marker dialog open, you can change several properties across separate fields. For quick editing, press Tab to jump to the next field, or Shift-Tab to jump to the previous one.

### Editable properties in the Marker dialog

Time: The frame at which the marker sits relative to that clip or timeline. It’s editable, letting you reposition a marker numerically. Duration: Optional; the length of a marker that’s carrying a duration. This too is editable, so you can hand a marker a duration numerically, or adjust one that already has duration. Name: The marker’s name; by default this reflects where the marker fell in the sequence of additions (Marker 1, Marker 2, etc.). Notes: A field for typing whatever information you want to track. Color: A row of buttons for picking the marker’s color. Keyword: A keyword field that lets you keyword markers the same way you keyword clips in the Metadata Editor, which can be a potent means of flagging clip sections you’ll want to locate later in Smart Bins or Search operations. As you type into the Keyword field, it searches the dictionary for matching keywords on its own. Press Return to take a found keyword (the Arrow keys let you pick from a list), or press the Up Arrow key back up to the Keyword field to type your own fresh variation by hand instead. For more on working with and editing Keywords, see Chapter 16, “Using Variables and Keywords.” Remove Marker: Wipes out that marker. Done: Shuts the marker edit dialog. 3 Once you’re done, click Done. After you add notes to a marker, a small symbol appears over that marker to indicate it holds information.

A small dot on a marker is the sign that it holds notes.

### Changing Marker Timing

After you’ve set one or more markers, several routes let you shift them around to better align with key events in source footage or the Timeline, or remove them once they’ve outlived their use. On top of that, you can switch on or off whether markers ripple alongside other clips in parts of the Timeline touched by rippling operations. To shift one or more markers in the Timeline or Source Viewer:

- Click one marker, or Command-click several markers you want to shift, and drag them somewhere new.
- Drag a bounding box up from the Timeline into the Timeline ruler to grab several markers, then drag them somewhere new.
- Open a marker’s edit dialog and edit the time and duration timecode fields by hand to move that marker numerically, or to build a marker of a particular duration. Beyond that, the timecode in these fields can be copied out of or pasted into.

To enable marker rippling:

- Choose Timeline > Ripple Timeline Markers. With it checked, every marker sitting to the right of a clip that’s being ripple edited, trimmed, or ripple deleted ripples leftward together with the rest of the Timeline. This behavior is yours to switch on and off whenever you like.

### A marker with duration in the Timeline

To modify marker duration:

- Option-drag any marker rightward or leftward to turn it into a marker with duration.
- Bring the playhead to the frame holding the marker you want to change and press M, or double-click the marker you mean to edit, then enter a number in the duration field and click Done.
- A marker with duration shows up as a bar in the Timeline ruler or on the Source Viewer’s jog bar. Drag the middle of such a marker to shift it, or drag its left or right edge to resize its duration.
- To strip a marker of its duration, open the marker dialog and key its numeric duration down to 00:00:00:00, or else drag one end until it meets the other as a single marker.

Ways to delete markers:

- To remove one or more markers with the mouse: Click to select a marker, or Command-click to select several; then press the Delete key. Another route is to double-click a marker, which opens its dialog, and from there click the Delete button.
- To remove a marker with the keyboard: Bring the playhead to the marker you want gone and press Option-M.
- To clear every marker off a clip: Pick the clip or clips whose markers you want removed, then either press the Backspace key or open the Marker drop-down in the Toolbar and choose Clear All.
- To clear every marker out of the Timeline: First deselect all clips. Then either choose Clear All out of the marker drop-down menu sitting in the Toolbar, or instead right-click the Timeline ruler and, from the contextual menu, choose Remove All Markers.

### Copy and Paste Multiple Markers in the Viewers and Timeline

On the Edit page, you can grab several markers at once by Shift- or Command-Clicking them, or by dragging a boundary box around them. With them selected, pressing Command-C copies these markers to the clipboard. From there, pressing Command-V pastes them all into another clip, timeline, or compound clip at the playhead position. When a timeline clip is selected for Paste, DaVinci Resolve lays clip markers onto the clip. With nothing selected, DaVinci Resolve produces timeline markers instead. This comes in handy for keeping essential marker information easy to share across various iterations of media and across timelines. You can run the copy and paste operations in either the Source and Timeline Viewers, or in the Timeline itself.

### Marker Notes in Data Burn-Ins

Marker notes can be surfaced through Data Burn-Ins. Here’s how: 1 Build a Marker, then drop a word or two into its Notes section. 2 Head to Workspace > Data Burn-In. 3 Tick one of the Custom Text options. 4 In the field that appears, type the “%” sign, then begin spelling out the word “marker.” 5 Pick Marker Notes from the list. 6 Tune the font/position/opacity parameters as needed. From now on, whatever text you place in the Marker Notes section displays as a Data Burn-In. Should you want the notes to persist beyond one frame, be sure to switch the marker to a duration marker instead.

The marker note “Stock Footage” now appears as a Burn-In, by way of the % metadata tags in a Custom Text field.
