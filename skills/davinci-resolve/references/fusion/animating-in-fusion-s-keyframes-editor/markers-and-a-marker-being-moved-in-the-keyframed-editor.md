# Markers and a marker being moved in the keyframed editor

Version: DaVinci Resolve 20.3 Reference Manual. Context: Animating in Fusion s keyframes editor.
[Chapter index](INDEX.md) / [Previous section](keyframe-spreadsheet-and-editing-keyframes-in-the-spreadsheet.md) / [Next section](spreadsheet-editor.md)
<a id="source-a-marker-being-moved-in-the-keyframed-editor"></a> <a id="source-autosnap"></a> <a id="source-autosnap-markers"></a> <a id="source-autosnap-points"></a> <a id="source-deleting-markers"></a> <a id="source-jumping-to-markers"></a> <a id="source-markers"></a> <a id="source-renaming-markers"></a> <a id="source-show-marker-list"></a>

### Markers

Markers serve to flag key frames in a project that could bear on how you keyframe animation. They might pinpoint the frame where a dragon breathes fire at a protagonist, the instant someone steps through a portal, or any other crucial frame in a composition you need to keep tabs on. Markers placed on the Timeline in the Cut, Edit, Fairlight, or Color page surface in the Keyframes Editor and Spline Editor of the Fusion page. While you work in Fusion Studio or the Fusion page, the Keyframes Editor or the Spline Editor lets you add them as well. Within Fusion, a selected marker appears as a small handle with a line running vertically through the graph view.

### A marker being moved in the Keyframed Editor

Here is how to create a marker: at a frame on the Keyframes Editor’s Timeline Ruler, right-click and pick Add Marker out of the contextual menu. A marker’s position is its most vital attribute. To be worth anything, a marker has to land on the frame you meant it for. Hovering the cursor over a marker pops a tooltip reporting its current frame position. Should it land on the wrong frame, dragging it along the Time Ruler will reposition it. Markers placed on the Time Ruler stay editable in the Fusion page, and the edits flow back into the other DaVinci Resolve pages. From within Fusion’s Keyframes or Spline Editor, Time Ruler markers can be added, moved, deleted, renamed, and tagged with descriptive notes. NOTE: Markers tied to clips in the Edit page Timeline show up on MediaIn nodes in Fusion’s Keyframes Editor yet cannot be edited there. They do not appear in the Spline Editor.

### Jumping to Markers

A double-click on a marker sends the playhead to that marker’s position.

### Renaming Markers

By default a marker carries the frame number in its name, but you can hand it a more descriptive name alongside the frame number to make it easier to spot. To rename a marker in Fusion, right-click over the marker and pick Rename Guide from the contextual menu. Type a name into the dialog and click OK.

Right-clicking over a marker, or over the Keyframe Editor Time Ruler, brings up the Marker contextual menu.

### Show Marker List

You can use markers to leap to particular spots in a composition by way of the Marker List. Right-click over a marker or inside the Keyframe Editor Time Ruler to summon the contextual menu, and you can pick Show Marker List, or press Shift-G, to bring up the Marker List dialog. The Marker List is a floating dialog that stays above the main window until you close it. The Marker List presents every current marker in the composition, ordered by their position in time along with whatever custom name you gave them. Double-click a marker’s name in the list and the playhead leaps to the marker’s location.

By way of markers, the Marker List dialog lets you move around within a composition. A pair of checkboxes sits beside each marker’s name. One belongs to the Spline Editor, the other to the Keyframes Editor. By default markers appear in both the Spline Editor and Keyframes Editor, but you can clear the relevant checkbox to hide the markers in that view.

### Deleting Markers

To delete a marker, drag it upward past the Time Ruler and let go of the mouse. You can also reach for the marker’s contextual menu and pick Delete Marker.

### Autosnap

To place keyframes and a segment’s start and end precisely while you drag in the Timeline, you can have them snap onto a field, onto a frame, or onto markers. Inside the Options section of the Keyframes Editor’s contextual menu sits the Autosnap option. Two submenu options come with autosnapping. The first dictates how snapping works while you drag keyframes, control points, or a segment’s opening and closing edges. The second dictates how markers snap.

### Autosnap Points

As you drag keyframes or the edges of segments, you often want them to land on a particular frame. By default Autosnap pins the placement of keyframes and segment edges to frame boundaries, but the contextual menu offers other choices. To configure autosnapping for keyframes and segment edges, right-click somewhere within the Keyframes Editor and choose Options > Autosnap Points off the contextual menu. The Autosnap Points submenu then appears, carrying choices that govern how snapping behaves. Those choices are:

- None: With None, keyframes and segment edges may be placed freely at subframe precision.
- Frame: With Frame, keyframes and segment edges are pulled onto the closest frame.
- Field: With Field, keyframes and segment edges latch onto the closest field — that being 0.5 of a frame.
- Guides: Once switched on, keyframes and segment edges latch onto markers.

### Autosnap Markers

When you click to make a fresh marker, its default behavior is to snap to the nearest frame. Reposition that marker and it likewise snaps to the closest frame as you drag. This behavior can be changed via the Keyframes Editor’s contextual menu, picking from within the Options > Autosnap Markers submenu. The choices are:

- None: Markers may sit anywhere at subframe precision.
- Frame: With Frame, every marker is pulled onto the closest frame.
- Field: With Field, every marker latches onto the closest field.
