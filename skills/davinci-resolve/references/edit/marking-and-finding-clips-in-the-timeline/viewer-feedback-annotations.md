# Drawn annotations on the viewer and drawing annotations to highlight feedback

Version: DaVinci Resolve 20.3 Reference Manual. Context: Marking and finding clips in the timeline.
[Chapter index](INDEX.md) / [Previous section](marker-colors-ranges-and-properties.md) / [Next section](markers-in-the-media-pool-overview.md)
<a id="source-drawing-annotations-to-highlight-feedback"></a> <a id="source-drawn-annotations-on-the-viewer"></a> <a id="source-exposing-markers-in-lists"></a> <a id="source-marker-information-shown-in-the-source-viewer"></a> <a id="source-reading-marker-information"></a> <a id="source-using-markers-for-navigation"></a> <a id="source-using-markers-in-the-marker-index"></a> <a id="source-using-timeline-markers-for-chapters"></a>

### Drawn Annotations on the Viewer

These days the Timeline Viewer’s Annotations mode lets you sketch arrows, plus strokes of varying weights and colors, right on the video frame, so as to point out or highlight things needing a fix. Markers hold these annotations, much as they hold marker names and notes. To begin, just pick Annotations mode from the Timeline Viewer mode drop-down menu.

Choosing Annotations from the Viewer Mode drop-down menu. Once you’re in Annotations mode, an Annotations toolbar shows up presenting these options. Draw tool with line weight drop-down: hitting the Draw tool lets you freeform draw on the Viewer; the Line Weight drop-down beside it offers three line weights to pick among for drawing. Arrow tool: hitting the Arrow tool produces straight-line arrows that point at features you want to spotlight. Whatever weight you’ve set for the Line tool, arrows always emerge at one fixed weight. Line Tool: hitting the Line tool produces straight lines on the Viewer. Rectangle Tool: hitting the Rectangle tool produces boxes on the Viewer. Color drop-down: here you settle on a color for your drawing or lines. Ways to make and edit annotations:

- To make an annotation: Just switch Annotations mode on, rest the playhead on whatever Timeline frame you like, and begin drawing. At that frame, a marker is added to the Timeline automatically, and that marker holds the annotation data. Should the playhead sit over a marker that’s already in the timeline, the annotations attach to that marker.
- To edit a stroke or arrow you’ve drawn already: Move the pointer onto a stroke or arrow, click to select it, then pick a fresh line weight or color from the matching drop-down menu, or drag that stroke or arrow elsewhere to reposition it.
- To delete a stroke or arrow: Move the pointer onto a stroke or arrow, click to select it, then press the Delete or Backspace keys.

### Drawing annotations to highlight feedback

### Reading Marker Information

After you’ve set a number of markers carrying custom information, you have two ways to review that information short of opening the marker dialog. To read marker notes with your pointer:

- Double-click a marker to bring up its marker dialog.
- Hover the pointer over any marker in the Source Viewer or Timeline to surface a tooltip carrying that marker’s information.

Hovering the pointer over a marker brings its information up in a tooltip. To read marker information directly inside the Source and/or Timeline viewers: 1 From the option menu of the Source or Timeline Viewer, switch on Show Marker Overlays. 2 Halt playback and bring the playhead to a marker. That marker’s information then appears superimposed in the Viewer.

### Marker information shown in the Source Viewer

### Using Markers for Navigation

Markers can assist with navigation through two keyboard shortcuts that hop the playhead from one marker to the next. As the playhead travels among markers, Clip and Timeline markers get treated as one combined set. To send the playhead to the next or previous marker:

- Press Shift-Up Arrow to send the playhead to the next marker to the left in the Timeline.
- Press Shift-Down Arrow to send the playhead to the next marker to the right in the Timeline. Whichever marker the playhead lands on is then selected automatically.

To send the playhead to a particular marker via the Source or Timeline Viewer’s Marker list:

- On a source clip or timeline holding several markers, you can jump the playhead straight to a particular marker by opening the Source or Timeline Viewer’s Option menu and picking a marker from the Markers submenu, which lays out every marker on offer in that Viewer, by name and note.

Every marker belonging to the clip you have open, shown via the Markers list in the Source Viewer Option menu.

### Using Timeline Markers for Chapters

A handful of file types, QuickTime among them, support chapter-based navigation in the finished video. That lets a viewer jump back and forth through the video, landing on precise points the video’s creator laid out. Such chapter-based navigation pays off especially in instructional videos or lengthy presentations. In DaVinci Resolve, timeline markers define the chapter points. For now, only the QuickTime and MP4 formats handle chapter markers in DaVinci Resolve. To build a chapter marker in the Timeline:

- Park the playhead at the spot in the Timeline where you want a chapter point, then choose Add Marker (M).
- Edit the marker by double-clicking it, or by picking Modify Marker (Command-M).
- Edit the Name field to set the chapter name that will appear in the player.
- Pick a color for the marker. Every chapter marker has to share the same color.

To export embedded chapter markers in a QuickTime movie:

- On the Deliver page, set Quicktime or MP4 as the Format in the Video Panel.
- Tick the box beside Chapters from Markers, then pick the chapter marker color you settled on earlier from the drop-down menu.

Within the Deliver page, the QuickTime Export Video settings hold the Chapters from Markers checkbox.

### Using Markers in the Marker Index

The Marker Index gives you a single handy spot to view, edit, and organize all your timeline and clip markers. You reach the Marker Index by clicking the Index panel and selecting the Markers tab. Ways to work with markers in the Marker Index:

- To filter markers in the Marker Index: From within the Marker Index, open the Option menu; pick Show All there, or pick Show Only to settle on a particular color. Every clip carrying a matching marker turns up in a list, where the columns map across to each timeline and clip marker’s color(s), information, and notes. Clicking a column header sorts the columns in ascending or descending order. You can switch individual columns on or off by right-clicking the column header and ticking or unticking the column name.
- To send the playhead to where a marker sits via the Marker Index: In the list, double-click that marker’s entry.
- To edit marker information: You can revise a marker’s values by clicking into the Name, Notes, or Keyword fields and changing the text. The Marker Index won’t let you edit the other values; change those in the timeline marker’s Edit dialog.
- To hunt for a particular marker: Click the search icon (magnifying glass) and type your search terms. The search pulls results from every field in the Markers window, the Name, Notes, and Keywords fields included.
- To flip between Thumbnail and List view: Up in the Marker Index’s top bar, click whichever you want of the Thumbnail or List View icons.

The Marker Index in List View mode gives you one place to edit and organize all your timeline’s markers.

### Exposing Markers in Lists

The Edit Index, too, can sift out a list of the markers that fall within the current Timeline. You can filter every marker at once, in which case columns reveal the notes and colors on each marker. You can instead filter by a particular marker color when you only care to see one kind of marker. Ways to work with markers in the Edit Index:

- To filter all marker-bearing clips through the Edit Index: Within the Edit Index, click the Markers tab; from the Option menu, then choose Show All or single out a particular color. Every clip carrying a matching marker turns up in a list, where the columns map across to each Timeline and Clip marker’s color(s) and notes.
- To send the playhead to a marker’s position in the Edit Index: Click that marker’s entry in the list.
- To reveal hidden marker columns: Right-click any column header and switch on any of the selections to surface that column. Where needed, you can reorder columns by dragging them left or right.

You can also export marker lists as an EDL, a .txt, or a .csv file. Exporting marker lists:

- To export Timeline markers as an EDL: In the Media Pool, right-click that timeline; from the menu, choose Timelines > Export > Timeline Markers to EDL. The Export Edit Index dialog then lets you pick a location and an export format, after which you click Save. Every Timeline marker shows up in the resulting EDL, any notes riding along plus a duration where applicable.
- To send every filtered Edit Index marker out as a .txt or .csv file: Having already chosen Show Markers in the Edit Index option menu, reopen that Option menu and choose Export Edit Index. The Export Edit Index dialog then lets you pick a location and an export format, after which you click Save.
