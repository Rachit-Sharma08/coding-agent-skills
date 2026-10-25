# Markers and source and timeline viewers

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the edit page.
[Chapter index](INDEX.md) / [Previous section](filtering-the-edit-index-and-exporting-the-edit-index.md) / [Next section](viewer-controls-overview.md)
<a id="source-how-each-clips-grade-looks-in-each-viewer"></a> <a id="source-markers"></a> <a id="source-previous-and-next-clips-or-timelines-in-viewers"></a> <a id="source-single-viewer-mode-turned-on"></a> <a id="source-source-and-timeline-viewers"></a> <a id="source-source-and-timeline-viewers-1"></a> <a id="source-source-and-timeline-viewers-vs-single-viewer-mode"></a> <a id="source-the-source-viewer"></a> <a id="source-the-timecode-toolbar-activated-in-the-source-monitor"></a> <a id="source-the-timeline-viewer"></a> <a id="source-timecode-toolbar-on-edit-viewers"></a>

### Markers

With the Marker Index you can readily view, edit, and organize every one of your timeline and clip markers from one handy spot. You reach the Marker Index by clicking the Index panel and choosing the Markers tab. Ways to work with markers in the Marker Index:

- To filter markers in the Marker Index: Open the Marker Index's Option menu, then pick Show All, or pick Show Only to single out one specific color. Every clip bearing a matching marker lands in a list, its columns mapping to the color(s), information, and notes of every timeline and clip marker. You can sort columns in ascending or descending order by clicking the column header. Individual columns can be switched on or off by right-clicking the column header and checking or unchecking the column name.
- To send the playhead to where a marker sits, working from the Marker Index: In the list, give that marker's entry a double-click.
- To edit marker information: You can alter a marker's values by clicking into the Name, Notes, or Keyword fields and editing the text field. Other values can't be edited in the Marker Index and ought to be changed in the timeline marker's Edit dialog.
- To search for a specific marker: Click the Search icon (magnifying glass) and type your search terms in. For now the search only looks at the Marker Name column; you can't search by notes and keywords.
- To switch between Thumbnail and List view: Click either the Thumbnail or List View icons up in the Marker Index's top bar.

The Marker Index's List View mode lets you edit and organize all of your timeline's markers from one spot.

### Source and Timeline Viewers

Out of the box, the Edit page offers a classic source/record style editing experience. The Source Viewer lets you look over individual clips from the Media Pool to ready them for editing. The Timeline Viewer, meanwhile, lets you play through your program, showing the frame at wherever the playhead sits in the Timeline.

### Source and Timeline Viewers

To choose a viewer, click it with the pointer or press Q (Source/Timeline Viewer); the viewer that currently holds focus has its name rendered in orange.

### How Each Clip's Grade Looks in Each Viewer

Owing to DaVinci Resolve's deep color and effects tools, how the image looks in each viewer of the Edit page hinges on several factors.

### The Source Viewer

The Source Viewer presents each clip the way it looks at the source. If Resolve Color Management (RCM) is switched on or source LUTs are applied, then the Source Viewer presents your clips as RCM and/or the source LUTs are processing them, since those operate as source-level color operations. Without RCM and source LUTs, though, the image in the Source Viewer matches exactly what's on disk. If your log-encoded media looks flat and low in contrast, that's just how it'll appear in the Source Viewer.

### The Timeline Viewer

The Timeline Viewer obeys every rule the Source Viewer does, plus it additionally shows how each Timeline clip looks once Fusion page and/or Color page operations are applied, since the Timeline Viewer is in fact presenting the Color page's output—so you can see each clip of your program in the context of how the DaVinci Resolve image processing pipeline is affecting the image. NOTE: The Color Viewer Lookup Table options found in the Project Settings' Color Management panel touch only the GUI Viewer in the Color page. They leave the Edit page's viewers alone. Turning Grades and/or Fusion Effects Off in the Timeline Viewer The Color page's Bypass Color Grades and Fusion Effects button/drop-down is on hand in the Edit page too, reachable either through the View > Bypass Color and Fusion drop-down or through a toggle button/ drop-down menu in the Timeline Viewer. Pick Bypass All Grades or click the Viewer control and you switch off whatever sits checked in the optional menu, which lets you decide whether to bypass both Color and Fusion or just one of the two.

(Left) The menu commands that bypass Color and Fusion, (Right) The Edit page's Timeline Viewer controls Switching color grades and Fusion effects off is a simple way to boost playback performance on low power systems when all you need is to knock out a quick set of edits, and it's a handy way to quickly size up the original source media as well.

### Timecode Toolbar on Edit Viewers

You can switch on the same Timecode toolbar from the Media page over in the Edit page. Inside the Edit page Source or Timeline Viewer, pick the Option (3-dot) menu and pick Show Timecode Toolbar from the drop-down. The Timecode Toolbar presents the In/Out point timecodes along with the total duration that's been set.

### The Timecode toolbar activated in the Source monitor

### Source and Timeline Viewers vs. Single Viewer Mode

Should you want to reshape the Edit page layout to tuck away the Source Viewer, you can pick Workspace > Single Viewer Mode so that just one viewer contextually shows either a chosen Source Clip or the Timeline's current frame.

Under Single Viewer mode, whatever you pick in the Media Pool or Timeline drives which controls turn up in the Viewer, letting you do nearly all of what you'd do with two viewers open at once.

### Single Viewer mode turned on

### Previous and Next Clips or Timelines in Viewers

Across the Media, Edit, and Color pages, the Viewer's Option (3-dot) menu lets you hop to the recent next/previous clip or timeline right out of its submenu. In the Edit page Source Viewer the entries read Previous/Next Clip; in the Edit page Timeline Viewer they read Previous/Next Timeline.

Selecting the next clip from the Viewer Option menu
