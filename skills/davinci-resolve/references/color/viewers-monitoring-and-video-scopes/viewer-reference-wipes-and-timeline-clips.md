# Different viewer reference modes for wipes and wiping between clips in the timeline

Version: DaVinci Resolve 20.3 Reference Manual. Context: Viewers monitoring and video scopes.
[Chapter index](INDEX.md) / [Previous section](safe-area-overlays-in-the-viewer-and-use-gray-background.md) / [Next section](color-viewer-marker-overlays-and-navigation.md)
<a id="source-available-split-screen-modes"></a> <a id="source-different-viewer-reference-modes-for-wipes"></a> <a id="source-placing-three-playheads-in-the-mini-timeline"></a> <a id="source-using-split-screen-modes"></a> <a id="source-viewers-monitoring-and-video-scopes-part-3"></a> <a id="source-viewing-and-choosing-the-current-selection"></a> <a id="source-wiping-between-clips-in-the-timeline"></a>

### Different Viewer Reference Modes for Wipes

Although wiping against reference stills via the Gallery is common, changing the reference mode further opens up wiping against a Timeline clip, or — where one has been assigned to the current Timeline — against an Offline Reference Clip or Timeline. To switch the Viewer reference mode, do one of these:

- Within the Viewer's option menu, pick an entry from the Reference Wipe Mode submenu.
- Pick from the Reference Mode icons sitting along the top of the Viewer.

There are three reference modes:

- Gallery: The default reference mode. Wipes the current clip set against a Gallery still.
- Timeline: Wipes the current clip set against a different Timeline clip by means of the Wipe Timeline Clip command (see below).
- Offline: Wipes the current clip set against an offline video assigned to this Timeline.

For details on attaching Offline References to a timeline for comparison purposes, turn to Chapter 55, “Preparing Timelines for Import and Comparison.”

### Wiping Between Clips in the Timeline

If you'd like to wipe the current clip against another Timeline clip but skip saving a still to the Gallery first, a dedicated procedure exists. Wiping between two clips in the Timeline reference mode goes like this: 1 Click the thumbnail of whichever clip you wish to compare first. 2 (Optional) A “Gang timeline wipe with current clip” option, found in the Viewer option menu, holds steady the gap separating the current clip from the timeline clip being wiped against, even as you shift the current clip selection to other clips. With it on, the offset between the timeline wiped clip and the current clip holds as you move the clip selection. You can advance the timeline reference clip one frame by pressing Command-Option-Right Arrow, and step it back one frame with Command-Option-Left Arrow. This allows precise positioning. With the option off, the timeline wiped clip stays put no matter which clip you pick. 3 On the thumbnail of the second comparison clip, right-click and pick Wipe Timeline Clip out of the contextual menu. The two clips appear split screened against each other. NOTE: Wipe Timeline Clip surfaces in the contextual menu only when you right-click a Timeline thumbnail that hasn't been chosen as the current clip.

Change a Timeline Wipe Using the Timelines Album of the Gallery While Wipe Timeline Clip displays a wipe of the current clip against any other Timeline clip, the Gallery's Timelines album can be opened so that clicking among its clips changes which timeline clip serves as the wipe target (outlined in blue) while leaving the current clip untouched (outlined in orange).

### Using Split Screen Modes

A collection of split screen modes adds further ways to weigh several images in the Viewer at once. They give you grid and side-by-side comparisons spanning several shots and several versions, every one routed out to video for monitoring on your external video display. As an example, the Split Screen Versions mode can display every single version applied to the current clip in a grid, making them easy to evaluate. The clip currently selected in the Timeline is highlighted in gray, so you can keep your bearings. To turn on a split screen mode, do one of these:

- Click the Split Screen button on the top Viewer toolbar, and pick a split screen method from the drop-down menu that opens in the Viewer toolbar at the right.
- Within the Viewer's option menu, pick an entry from the Split Screen submenu.
- Press Option-Command-W to toggle Split Screen on and off, using the last chosen option.
- Right-click the Viewer and, from the contextual menu's Split Screen submenu, pick an entry.

NOTE: With any split screen mode active, the Viewer hides every other onscreen control — Power Window shapes among them — and won't show them again until split screen is switched off.

A four-shot grid produced by the Split Screen > Selected Clips mode

### Viewing and Choosing the Current Selection

In every split screen mode, the current selection carries a gray outline. For a cleaner comparison that outline can be turned off: within the Viewer's option menu, Split Screen > Show Outline toggles it on and off. Within certain modes, double-clicking a given frame of the split screen view also lets you swap the current clip, choose the active version, or lay on a gallery grade.

### Available Split Screen Modes

You can pick from among these split screen modes:

- Current Group: Displays as many as 16 clips sharing the group of the current clip. In this mode a double-clicked frame has no effect.
- Highlight Modes: Displays a four-up view in which you can, all at once, take in (going clockwise) the RGB image of the clip, then its gray matte, next the high contrast matte, and finally a difference matte that comes from weighing the node's input against its output. Here too, double-clicking a frame does nothing.

Viewing a key using the Split Screen > Highlight Modes

- Neighbor Clips: Displays the four clips that immediately bracket the current clip. The two prior clips take the upper left and upper right spots, the current clip lands at the lower lefthand corner, and the next one fills the lower right. A double-clicked frame does nothing here. How many neighboring clips appear in this mode is governed by the “Neighboring Clips in Split Screen” parameter found in the Color panel of the User Preferences.
- Playheads: Within the Color page Viewer, presents side-by-side views of as many as four playheads shown in the Mini-timeline after you select several playheads from the Color > Active Playhead submenu. For every playhead you reveal (up to 4), its frame shows in a 2-up, 3-up, or 4-up grid. When enabled, an outline in the Viewer flags which playhead is active at the moment. This serves both for weighing several clips and for weighing different frames inside one clip. Switching among the active playheads is done by clicking the clips in the split screen Viewer

### Placing three playheads in the Mini-timeline

- Selected Album: Choosing this option brings up in the Viewer a split screen of the grades from each still in that album, shown as they would look on the current clip. A double-clicked frame applies that gallery grade onto the current clip. As many as 16 grades can appear.
- Selected Clips: Displays every Timeline clip currently selected, up to 16 at a time. A click on a clip moves the playhead onto that clip's first frame.
- Selected LUTs: Lets you preview, all at once, how different LUTs affect the current clip — shown as a split screen in the Viewer — by Command-clicking up to 16 LUTs in the LUTs browser that you'd like to preview.

With the Selected LUTs split screen option you can audition a batch of LUT looks together

- Selected Still Grades: When you pick this option, selecting stills in the Gallery of the Color page shows each grade tied to those stills as it looks applied to the current clip, in a split screen layout. Double-clicking a frame applies that gallery grade to the current clip.

Previewing four gallery grades using the Split Screen > Gallery Grades mode

- Selected Still Images: Lets you compare the present clip against an assortment of other stills you pick out from the Gallery. Rather than a grading preview, what you're really getting is a split screen built from the selected still images in the Gallery.
- Version: Presents as many as 16 versions of the present clip simultaneously, which makes it simple to weigh a run of differing versions against each other. Should you keep more than 16 versions, an award of some kind is surely owed to you. Double-clicking a version makes it the active version.
- Versions and Original: Presents up to the first 15 versions of the present clip, plus the original ungraded clip tucked into the upper left-hand corner. Double-clicking a version makes it active, yet a double-click won't let you pick the original.
