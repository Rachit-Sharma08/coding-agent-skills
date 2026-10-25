# Special purpose playback commands and custom guides and snapping in the timeline viewer

Version: DaVinci Resolve 20.3 Reference Manual. Context: Preparing clips for editing and viewer playback.
[Chapter index](INDEX.md) / [Previous section](single-viewer-and-source-clip-preparation.md) / [Next section](optimized-ui-layouts-for-vertical-editing.md)
<a id="source-custom-guides-and-snapping-in-the-timeline-viewer"></a> <a id="source-snapping-to-guide-lines"></a> <a id="source-special-purpose-playback-commands"></a> <a id="source-the-addedit-guide-dialog"></a> <a id="source-the-timeline-viewer-with-guides-and-rulers-enabled"></a>

### Special-Purpose Playback Commands

Beyond the usual transport controls sit several extra playback commands — reachable through keyboard shortcuts or the Playback menu — that carry out different playback actions.

- Loop: Command-Forward Slash (/). Flips looped playback on or off. With looping active, anything you start using the commands below keeps repeating on its own until you halt playback.
- Play around selection: Forward Slash (/). The behavior of this command shifts with whatever is chosen in the Timeline. It plays a stretch of the Timeline reaching from x frames before to y frames after (a) the playhead (when nothing is chosen), (b) the chosen edit point, (c) the chosen clip, (d) the chosen transition, (e) a multi-clip selection. It’s handy for seeing how the current selection sits among the clips right around it. You can adjust the pre-roll and post-roll time in the Editing panel of the User Preferences.
- Play around current frame: Plays a stretch of the Timeline from x frames before to y frames after wherever the playhead now sits. It’s handy for seeing how edits sit among the clips right around them. You can adjust the pre-roll and post-roll time in the Editing panel of the User Preferences.
- Play around current clip: (no default key assigned). Plays a stretch of the Timeline from x frames before to y frames after the clip the playhead is currently crossing. You can adjust the pre-roll and post-roll time in the Editing panel of the User Preferences.
- Play Around In: Option-Space. Plays a stretch of the Timeline from x frames before to y frames after the In point now assigned, so you can preview the handoff from one clip to the next. You can adjust the pre-roll and post-roll time in the Editing panel of the User Preferences.
- Play Around Out: Shift-Space. Plays a stretch of the Timeline from x frames before to y frames after the Out point now assigned, so you can preview the handoff from one clip to the next. You can adjust the pre-roll and post-roll time in the Editing panel of the User Preferences.
- Play In to Out: Option-Forward Slash (/). When a portion of a clip or timeline carries In and Out points, this command previews how that portion will play.
- Play to In: (no default key assigned). Starts playback and halts at the current In point.
- Play to Out: Option-Command-Forward Slash (/). Starts playback and halts at the

current Out point.

### Custom Guides and Snapping in the Timeline Viewer

The timeline viewer lets you lay down guides of your own. With them you can pin down precise spots in the frame and then have the image snap to those spots during other work. There are Guides — colored lines running across the frame either horizontally or vertically — and Rulers, which lay out measurement marks along the frame’s edges. Guides and Rulers alike are overlay aids for tweaking your video’s placement, and they appear only inside the viewer, never in the finished project output.

### The Timeline Viewer with Guides and Rulers enabled

Each of Guides and Rulers can be displayed on its own by clicking its icon within the Ruler Guides section of the Timeline viewer’s Viewer Guides dropdown menu. They may likewise be switched on separately through the View > Rulers and View > Guides menus.

Within the Viewer Guides dropdown sits its Ruler Guides section To Show and Modify a Ruler: 1 Turn the Ruler on by selecting View > Rulers > On, or by clicking the Ruler Icon in the Viewer Guides dropdown of the Timeline Viewer. 2 Pick the metric the Ruler should use under View > Rulers, or by right-clicking the Ruler in the Viewer. Pixel: Renders the ruler as a pixel count from the origin point (0,0) at the frame’s center on a conventional x/y cartesian grid, mirroring the Position field found in the Video Inspector. Percentage: Renders the ruler as a percentage distance from the origin point (0%, 0%) at the frame’s top-left. The upper ruler spans 0% on the left to 100% on the right, and the side ruler reads 0% at the top down to 100% at the bottom. As an example, a point dead-center in the frame would land at (50%, 50%).

### The Add/Edit Guide dialog

To Show and Create a Guide Line: 1 Turn the Guides on by selecting View > Guides > On, or by clicking the Guides Icon in the Viewer Guides dropdown of the Timeline Viewer. 2 Add a fresh Guide via View > Guides > Add Guide, or by right-clicking the Ruler in the Viewer and choosing Add Guides. 3 within the Add Guide dialog, set the position and orientation you’d like for the new guide, then click Add. Units: Pick the metric the guide line should follow. Pixel reports how many pixels lie from the guide’s origin point, while Percentage reports the percentage distance from the frame’s top left at 0%,0%. Position: Type a value for where across the frame the guide line should sit. You can also drag this line in the viewer to place it by eye (a little popup will surface the exact position value while you drag). If you like, click the lock icon so the guide can’t be nudged by accident. Orientation: Set the line to run horizontally or vertically. Color: Pick the guide line’s color from the choices on offer. To Modify a Guide Line:

- Drag the line wherever you want inside the viewer; a small pop-up window surfaces to report the exact position value.
- For better legibility, recolor the Guide Lines by right-clicking in the Ruler and picking a new color from the Guide Color context menu.
- Remove a line by right-clicking it in the viewer and selecting Remove Guide.
- Adjust an existing line’s position and orientation by right-clicking it in the viewer and selecting Edit Guide.
- Clear all lines, only the horizontal ones, or only the vertical ones through View > Guides > and choosing which lines to drop. Right-clicking the ruler does the same.
- Pin Guides down against accidental movement by clicking the little lock icon at the ruler’s upper-left, or via View > Guides > Lock Guides.

A right-click on the Ruler brings up a context menu where you can tune every parameter of the Rulers and Guide lines

### Snapping to Guide Lines

Out of the box, as you reposition the clip in the frame with the Transform Viewer controls, the image edge will snap to a guideline the moment it draws near one, and the guide line turns purple to confirm exact placement. To switch this off, just keep the option key held while moving the image in the viewer and the snapping is skipped.

When the image edge snaps onto a spot, the Guide Lines there shift to purple.
