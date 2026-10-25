# Playing stills and setting up image wipes and timeline wipes

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the gallery.
[Chapter index](INDEX.md) / [Previous section](color-page-gallery-and-saving-stills.md) / [Next section](gallery-options-and-organizing-stills-using-albums.md)
<a id="source-all-stills-are-numbered-trackshotversion"></a> <a id="source-automatic-labeling"></a> <a id="source-change-a-timeline-wipe-using-the-timelines-album-of-the-gallery"></a> <a id="source-gang-timeline-wipe-with-current-clip"></a> <a id="source-labeling-and-searching-for-stills-and-sources"></a> <a id="source-manual-labeling"></a> <a id="source-match-reference-wipe-frame"></a> <a id="source-playing-stills-and-setting-up-image-wipes"></a> <a id="source-searching-for-stills"></a> <a id="source-timeline-wipes"></a> <a id="source-you-can-also-label-stills-for-easier-identification"></a>

### Playing Stills and Setting Up Image Wipes

Plenty of routes exist for playing a still on the Color page, surfacing it as an image wipe in the Viewer and on the external display wired to your video interface. To play a still, showing it as an image wipe or full screen, take one of these actions:

- Double-click a still in the Gallery.
- Select a still in the Gallery, then click the Image Wipe button on the top Viewer toolbar.
- Click a still in the Gallery, after which you right-click within the Viewer and pick Show Reference Wipe.
- Out of the Color > Stills menu, pick Next Still (Option-Command-N), or pick Previous Still (OptionCommand-B), to select a still within the Gallery, and after that pick Wipe On/Off (Command-W) so it plays.
- On the DaVinci Resolve Advanced Search Dial panel—or else on the DaVinci Resolve Advanced control panel—press PREV STILL or NEXT STILL to select a still, then hit PLAY STILL. Hitting PLAY STILL a second time sends the still away.

Any time you play a still, the Viewer mode's drop-down menu shifts to Split mode. After it appears, you can slide and reorient, in various ways, the wipe separating the current clip from the still under reference. When you want a full-screen view so you can toggle back and forth between the still and the current clip, just nudge the split until the still takes over the whole Viewer. To adjust a wipe in the Viewer, take one of these actions:

- Drag the pointer inside the Color page's Viewer to move the wipe.
- On the DaVinci Resolve Advanced control panel's T-bar panel, push the T-bar lever up and down.

To tailor the kind of image wipe shown in the Viewer, take one of these actions:

- Click whichever of the controls sit at the top right of the Viewer toolbar to select among Horizontal, Vertical, Mix, Alpha, Box, and Difference types of wipe.
- Out of the Reference Wipe Mode submenu within the Viewer's option menu, pick Gallery, Timeline, or Offline.
- Pick from Horizontal, Vertical, Mix, Alpha, Difference, and Box by way of either the Wipe Style submenu within the Viewer's option menu, or else the style icons up at the top of the Viewer.
- Pick Invert Wipe (Option-W) from the Viewer's option menu.

### Timeline Wipes

A timeline wipe happens when you reach for the Wipe Timeline Clip command in the Thumbnail timeline (you'll find it in the contextual menu after right-clicking a clip other than the current one) to wipe the current clip against another clip in the Timeline, with no need to store a still beforehand. Switch a timeline wipe on and the timeline clip being wiped gets outlined in blue.

### Gang Timeline Wipe With Current Clip

A "Gang timeline wipe with current clip" option, reachable from the Viewer option menu, holds steady the offset separating the current clip from whatever timeline clip you're wiping against as you shift the current clip selection onto other clips. With this option switched on, the offset between the timeline wiped clip and the current clip holds steady as you move the clip selection. With this option switched off, the timeline wiped clip stays put no matter which clip you select.

### Change a Timeline Wipe Using the Timelines Album of the Gallery

As you lean on the Wipe Timeline Clip to display a wipe of the current clip set against any other Timeline clip, opening the Gallery's Timelines album and clicking different clips swaps which Timeline clip you wipe against (outlined in blue) while leaving the current clip alone (outlined in orange). Just confirm that the same timeline is selected across both the Timeline album and the Color page.

### Labeling and Searching for Stills and Sources

By default, a three-number code tags every still. That opening number names the video track carrying the clip, the next number gives the clip's position number within the current Timeline, and the final number gives the grade's version number. Once you've stored a heap of stills, it can pay to label the important ones with whatever text proves helpful. After labeling, you can hunt down stills by label through the Search field, over at the upper right-hand corner of the Gallery.

### All stills are numbered Track.Shot.Version

### Automatic Labeling

If you prefer, the Color group inside the General Options panel of the Project Settings offers options to "Automatically label Gallery stills" along assorted lines. The choices run deep:

- Clip Name: Stores the Clip Name, which falls back to the File Name unless you've customized it.
- Clip Version Name: Automatically stores the name of the current version.
- Source timecode (HH.MM.SS.FF): Stores the source timecode of the current frame.
- Timeline timecode (HH.MM.SS.FF): Stores the timecode for where the playhead sits

in the Timeline.

- Timeline Name: Stores the name of the Timeline currently open.
- Display LUT Name: Stores the name of the Display LUT currently in use, where one is applied.
- Custom label using tags: Pick this option and a field appears where you can either type custom

text or drop in metadata variables to store automatically updated information tied to the currently selected clip and timeline. For fuller detail on working with metadata variables, see Chapter 16, "Using Variables and Keywords." Across all options, there's also a checkbox you can flip:

- Append still number on export: Switch this checkbox on and you can decide how to fold in the default still number while exporting stills with the "Use labels on export" option active, either as a prefix or a suffix.

### Manual Labeling

Sometimes the simplest move is just to hand a given still a custom name that captures what that still stands for, like "SeemedLikeAGoodIdea." While naming stills by hand, steer clear of the forward slash character in case you end up exporting these stills with file names. As a matter of fact, it's wise to dodge the forward slash character for nearly any text you key into DaVinci Resolve. To label a still by hand: 1 Right-click a still in the Gallery and pick Change Label, or instead double-click in the area just below the Still ID. 2 Key a name into the Change Still Label dialog, then click OK.

The new label turns up beneath the still number.

### You can also label stills for easier identification

### Searching For Stills

After labeling, you can track down the stills you need in the Gallery. To hunt a still by its label: Click the Magnifying Glass button so the Search field opens, click once to set the cursor inside it, then type whatever name or description you're after. The moment you begin typing, DaVinci Resolve starts filtering the results of the currently selected album in the Gallery down to match what you've keyed in.

### Match Reference Wipe Frame

You can right-click any Gallery still and pick Match Reference Wipe Frame to automatically jump the playhead to the precise frame matching that still, and select that clip in the Color page Timeline.
