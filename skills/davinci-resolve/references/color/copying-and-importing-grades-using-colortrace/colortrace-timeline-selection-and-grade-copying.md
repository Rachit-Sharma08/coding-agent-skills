# Copying grades using colortrace and choosing colortrace for a selected timeline

Version: DaVinci Resolve 20.3 Reference Manual. Context: Copying and importing grades using colortrace.
[Chapter index](INDEX.md) / [Next section](colortrace-manual-window-and-cdl-import.md)
<a id="source-choosing-colortrace-for-a-selected-timeline"></a> <a id="source-copying-and-importing-grades-using-colortrace"></a> <a id="source-copying-and-importing-grades-using-colortrace-1"></a> <a id="source-copying-grades-using-colortrace"></a> <a id="source-selecting-the-automatic-or-manual-colortrace"></a> <a id="source-the-colortrace-window-shown-in-automatic-mode"></a> <a id="source-using-colortrace-in-automatic-mode"></a> <a id="source-using-colortrace-in-manual-mode"></a>

### Copying and Importing Grades Using ColorTrace

ColorTrace ranks among DaVinci Resolve's standout features: it lets you shift grades fast and painlessly off the clips of one timeline onto the clips inside another, keyed to each clip's source timecode (or to clip names while you're in Automatic mode). ColorTrace can even carry grades across timelines that share one project, and it can ColorTrace a single stereo timeline onto another.

### Copying Grades Using ColorTrace

Whichever version of a clip's grade got applied in the Source timeline you copy from — local or remote — is what ColorTrace brings across, decided by which grades each clip in that Source timeline is set to draw on. On top of that, ColorTrace carries Group Pre-Clip and Group Post-Clip grades along with Fusion compositions. Thanks to these gains, the tool is a thoroughly dependable way to move grades from one timeline onto another across all sorts of scenarios. To use ColorTrace: 1 Open the Media page and pick, out of the Media Pool, the Timeline you intend to run ColorTrace against, then open it and head to Timelines > ColorTrace > ColorTrace From Timeline.

### Choosing ColorTrace for a selected Timeline

Up comes the ColorTrace Setup window, laying out every project library, user, project, and timeline in one nested list. 2 Through the Project List browser, pick the exact Timeline whose grades you want to copy. To get at it, you'll have to click the disclosure triangle beside the project library, user name, and project that holds that Timeline.

ColorTrace project and Timeline selection window

3 (Optional) When you run ColorTrace on a project loaded with VFX clips, in a workflow where each of those VFX clips carries a distinct reel name marking it, you can type those names — with asterisks (_) serving as wildcards standing in for the parts of each reel name that may shift — into the “Effects Shot Definitions” field. Doing so quickens automatic ColorTrace runs, letting DaVinci Resolve lean on fuzzy string matching once a clip's reel number flags it as a VFX shot, so the strongest match surfaces at the top of the list. You're free to enter several VFX reel names with wildcards, one to a line, for string matching all at once. Whatever reel name text fits your workflow will do; a few sample VFX reel names look like this: **COMP** VFX_ EFFECTS\* 4 Click Continue. The ColorTrace window opens carrying two tabs that set how you work. 5 Pick your working mode by clicking either the Automatic or Manual tab:

- Under Automatic mode, ColorTrace hunts on its own for clips that line up between the chosen Timeline and the current Timeline. Every clip gets color coded by the correspondence it lands.
- Under Manual mode, you handle the grade copying yourself, by way of the Copy and Paste procedures, or by dragging and dropping with your mouse.

There's a lot to the ColorTrace window; how each mode runs gets its own treatment in the sections below. 6 Once you're done with ColorTrace, click Close.

### Using ColorTrace in Automatic Mode

Under Automatic mode, ColorTrace works out on its own the links between the clips in the chosen Timeline you're pulling grades from (the Source timeline) and those in the current Timeline you're pushing grades to (the Target timeline).

### Selecting the Automatic or Manual ColorTrace

A colored outline rings each clip in the Target Timeline Thumbnail timeline, signaling its status. Red: Nothing matched whatsoever. Usually the case for clips in the current Timeline that went unused in the Timeline you're ColorTrace matching against. Blue: Owing to timecode and reel names that overlap, several links turned up (much like a reel conflict), and you have to point out the right one per clip. This crops up often with VFX and motion graphics clips you brought in with timecode beginning at 00:00:00:00. Green: Something matched.

ColorTrace Thumbnail outlines indicate matching, overlapping, and non matching clips. Under Automatic mode, the link between every clip in the Source timeline and each one in the Target timeline ought to form by itself. That said, timecode and reel names that overlap can throw it off. The remaining controls in the ColorTrace window are there to help you tackle the handful of clips that won't match on their own, or that matched wrongly. Those controls are:

### The ColorTrace window shown in Automatic mode

Matching Source Clips list: Presents a scrollable set of thumbnails that may line up with the clip you've chosen in the Target timeline. Target Timeline: Presents each clip in the Timeline you're pushing grades to, color coded by how strong a match it is. Clip Info pane: Lays out two columns of properties covering the source clip alongside the target clips you picked. Among those properties, for each clip, are its reel, source timecode, record timecode, clip name, project names, plus timeline names — all laid out for easy side-by-side checking. Attributes and options checkboxes: A row of checkboxes lets you spell out which clip attributes ride along in the ColorTrace operation.

- Color: Enables the copying of grades.
- Preserve Num Nodes: As grades copy across, this keeps the leading X nodes belonging to the target clip's

grades safe from being clobbered by the leading X nodes of the source clip's grades.

- Input Sizing: Enables the copying of Input Sizing attributes.
- Convergence: Enables the copying of Convergence for Stereo 3D projects.
- Floating Windows: Enables the copying of Floating Windows for Stereo 3D projects.
- Auto Align: Switches on carrying the Auto Align settings across, for Stereo 3D projects.
- All Versions: Brings every version across from source to target, not solely the current one,

for the clips. The version currently chosen on each source clip always copies across correctly.

- Version Camera Raw Settings: Switches on copying of versioned Raw settings, in place of merely

the present Raw setting.

- Track Marks: Enables the copying of keyframes.
- Flags and Markers: Enables copying of all flags and markers.
- Hide Matching Clips: Tucks away every clip that matched cleanly, leaving on view only the clips with multiple matches or none. That lets you zero in on the troublesome subset inside a potentially lengthy timeline.
- Ignore Reel Names: Should you suspect the reel names are wrong, switching this checkbox on disregards them, lining up all source and target clips by timecode by itself.

Copy Grades: Carries the matched source grades onto each green and purple target clip. Copy Grades & Exit: After you've made all the grade matches you can, click this button to carry the matched source grades onto each green and purple target clip and shut the ColorTrace window. Here's the way to wield these controls to work out which source clips feed each blue and red target clip in the Target timeline. To hand-pick the source grades that should land on particular target clips: 1 Click any blue clip thumbnail over in the Target timeline.

Surfacing several candidate links over within the Matching Source Clips Timeline Up turns a batch of clips sharing overlapping timecode and reel names. Should you wish to set the reel names aside because you suspect they're wrong, switch on the Ignore Reel Names checkbox. 2 If holding the Source and Target thumbnails side by side doesn't settle the choice, then click any clip in the Matching Source Clips timeline to bring up its metadata for comparison across the source/target columns underneath.

Source and Target clip metadata for comparison

3 With a clip link settled on, double-click the Matching Source Clip thumbnail you mean to copy from. When no clip in the Matching Source Clip pane fits well, double-click the “Set As New Shot” box. Both the Source and Target thumbnails go purple, marking the link you've forged.

The matching Source and Target clips now both marked with purple outline Keep working through every thumbnail bearing Blue and Red Xs until you've turned up matches for as many clips in the Timeline as can be done. 4 Once finished, click Copy Grades & Exit.

### Using ColorTrace in Manual Mode

Manual mode shines whenever you need to carry grades between programs whose clips share no timecode or reel name link at all. The Manual ColorTrace interface is built to walk you across two separate timelines, either one clip at a time or in matched batches of clips, carrying grades off the Source timeline onto the Target timeline. Say you're trying to bring grades over from a timeline conformed out of individual media files onto a second timeline conformed from a single flattened master media file — the ColorTrace Manual mode gets that done. Two banks of controls make up the manual interface, one tied to the Source timeline (its label reads “Timeline to copy from”) and one to the Target timeline (its label reads “Timeline to paste to”). Broadly, you step through both timelines a single clip at a time, or in matched batches, ferrying grades off the “Copy from” timeline onto the “Paste to” timeline.
