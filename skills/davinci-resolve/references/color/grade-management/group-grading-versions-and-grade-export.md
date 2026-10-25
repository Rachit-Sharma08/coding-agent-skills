# Group grading versions and grade export

Version: DaVinci Resolve 20.3 Reference Manual. Context: Copying clip settings using display node graph.
[Chapter index](INDEX.md) / [Previous section](display-node-graph-and-shared-node-copying.md) / [Copying Clip Settings Using Display Node Graph](display-node-graph-and-paste-attributes.md)
<a id="source-an-example-of-grading-a-group-of-clips"></a> <a id="source-clips-made-into-a-group"></a> <a id="source-collapse-group-grades"></a> <a id="source-exporting-grades-and-luts"></a> <a id="source-groups-and-versions"></a> <a id="source-saving-stills-and-grades-in-groups"></a> <a id="source-scene-balancing-adjustments-made-using-the-clip-mode"></a> <a id="source-using-undo-in-groups"></a>

### An Example of Grading a Group of Clips

What follows walks through one way you might tackle grading a group of clips by drawing on the various Node Editor modes on offer. Bear in mind this is merely one route among many you could take with groups, picked here because it puts everything you can do to a single grade through its paces. To kick off, pick a run of clips you’d like to group, right-click one of them, and choose Create New Group to bind them together, typing in a name and clicking OK when asked. A handy upside of just building groups out of a selection is that you aren’t boxed into picking an unbroken stretch of clips along the Timeline. A further upside is that the View > Timeline Thumbnail Mode > Source (C-mode) command, or Timeline filtering, can isolate the span of clips you want to draw on while creating a group. You’ve got several routes for binding clips into a group:

- All clips within a particular scene
- All clips recorded from a specific camera
- All headshots of a particular person
- All clips from a particular angle of coverage
- All exteriors of a particular location

The list could run on forever, but you catch the drift. Any batch of clips with cause to share one common grade can be bound together. Here, a run of shots from an exterior scene gets picked and turned into a group.

### Clips made into a group

After you’ve built a group, pick Group Pre-Clip out of the Node Editor mode drop-down. This is the earliest grade laid down, acting as the foundational grade touching the whole group. Within this node tree, dropping in a LUT to normalize the clips, a Color Wheel move, and a handful of Curve moves to fine-tune the color delivers a primary grade that now reaches every single clip across the group.

A primary adjustment applied to the Group Pre-Clip mode With that done, you’ll notice a bit of variance among the scene’s clips that needs sorting so every clip lines up. Pick Clip out of the Node Editor mode drop-down. Grades you lay down in Clip mode touch only the clip they’re applied to, so now you can go clip by clip, leaning on the Image Wipe and Split-Screen controls to weigh clips against each other and make whatever moves it takes so each one fits the scene’s main look.

### Scene balancing adjustments made using the Clip mode

After all the clips sit balanced against one another, you can pick Post-Clip Group out of the Node Editor mode drop-down. This lets you stack one more grade atop the Pre-Clip and Clip grades you’ve already laid down, which you can put toward all sorts of ends. Here, a lone stylistic move gets applied that now touches every clip simultaneously. Should a client ask to see something else, you can readily make the needed change on one clip, and every other clip in that group shifts right along with it.

A stylistic adjustment applied to the Group Post-Clip mode By now the scene is graded through a neatly arranged set of corrections. If the client later asks for a change touching the underlying primary grade everything rests on, you can tweak the Pre-Clip grade. Should you catch an inconsistency in your shot matching anywhere along the way, you can make a quick fix to the relevant Clip grade. And if the client wants a stylistic shift, you can make whatever moves you need on the Post-Clip grade to recast the overall look of the entire scene. Each time, groups hand you full command over which moves spread across the whole group and which stay clip-specific.

### Using Undo in Groups

Every Node Editor mode keeps its own undo stack, which means separate multi-level undo is held for Group Pre-Clip, Clip, and Group Post-Clip.

### Saving Stills and Grades in Groups

Save a still for a clip belonging to a group and the still mirrors the combined look of the Pre-Clip, Clip, and Post-Clip node trees, yet the grade stored within hinges on whichever Node Editor mode was active as you saved the still. Say the Node Editor sits on Group Pre-Clip: then only the Pre-Clip grade gets saved; the Clip, Group Post-Clip, and Track grades are passed over. Copy a saved grade onto a clip in a group and that grade lands in the node tree of whatever Node Editor mode happens to be open.

### Collapse Group Grades

Should you want to pull a clip out of a group while keeping its grade folding in every move made across the Pre-Group and Post-Group Node Editor modes, the Collapse Group Grades command can copy all nodes from the Pre-Group and Post-Group grades onto the Clip grade. Once you do, the Pre-Group nodes slot in ahead of whatever nodes already sat in the Clip grade, with all Post-Group nodes slotting in afterward, so the proper order of operations holds.

The Clip node tree,

Here is what the Clip node tree looks like once the Collapse Group Grades command folds the PreGroup along with the Post-Group nodes down into it To collapse every group grade down into one Clip mode node tree: Right-click a clip’s thumbnail along the Thumbnail timeline, and choose Collapse Group Grades off the contextual menu. Running Collapse Group Grades on a clip always lifts that clip out of whatever group it used to belong to. This can also serve as a quick path to building a single flat node tree ahead of saving a grade to the Gallery for use on other clips that aren’t themselves grouped.

### Groups and Versions

Whatever Local or Remote versions you build pertain only to the Clip grade. The Group Pre-Clip and Group Post-Clip grades can’t be versioned.

### Exporting Grades and LUTs

Should you ever need to pass grades around between workstations, two routes let you do it directly: exporting grades, or LUTs. This section covers exporting Grades. For fuller details on exporting LUTs, refer to Chapter 150, “Using LUTs.” Here’s how to export a grade: 1 Within the Gallery, save as a still the grade you intend to export. 2 Right-click the saved still inside the Gallery, and choose Export. 3 Pick the image format you’d like to save the still in. The options run to: DPX, Cineon, TIFF, JPEG, PNG, PPM, BMP, and XPM. 4 Settle on a location for the resulting still image and saved grade files, enter a name into the Save As field, and click Save.

A pair of files lands. The image file holds the still picture of the frame that got stored. A DRX (DaVinci Resolve eXchange) file holds every bit of the grading information. To Import a grade: 1 Right-click somewhere in the gray expanse of the Gallery, and choose Import. 2 Hit the Options button to pick the exact file type you’d like to import, or pick “All Files” to cover several formats. 3 Pick the image file that was exported off your own DaVinci Resolve workstation, or off someone else’s. Its companion DRX file has to live in the same spot. Should you misplace the original image file, you can still bring in the DRX file on its own. It retains the still’s node structure, though you won’t be able to wipe against it. The still you brought in turns up within the Gallery, carrying the grading information you set out to import.
