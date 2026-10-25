# Editing the duration field in the cut page viewer and change clip duration dialog

Version: DaVinci Resolve 20.3 Reference Manual. Context: Fast editing in the cut page.
[Chapter index](INDEX.md) / [Previous section](setting-in-and-out-points-using-the-pointer.md) / [Next section](ripple-overwrite-and-close-up.md)
<a id="source-append"></a> <a id="source-change-clip-duration-dialog"></a> <a id="source-drag-and-drop-editing"></a> <a id="source-editing-the-duration-field-in-the-cut-page-viewer"></a> <a id="source-overwrite"></a> <a id="source-ripple-overwrite"></a> <a id="source-setting-up-and-performing-edits"></a> <a id="source-smart-indicator-showing-where-an-edit-will-occur"></a> <a id="source-smart-indicators"></a> <a id="source-smart-insert"></a> <a id="source-using-cut-page-edit-commands"></a> <a id="source-video-only-and-audio-only-edits"></a>

### Editing the Duration Field in the Cut Page Viewer

As you edit on the Cut page, you drop In and Out points to bring in a particular span of video. How long that video span runs shows in the Duration field, tucked into the Viewer’s upper-right corner. That field can now be edited, and it shifts the Out point to agree with whatever value you type. You may key in a specific frame count outright, apply the + or - modifiers to bump the value by exactly that much, or work the hh:mm:ss:ff field straight away. The editable duration field in the top right of the Viewer

### Change Clip Duration Dialog

Through the Change Clip Duration dialog you reset a clip’s length outright — by entering frames, a timecode value, or by leaning on time- and frame-based presets. To bring the Change Clip Duration dialog up, pick one or more clips on the Timeline and go to Clip > Change Clip Duration (Command-D), or right-click a clip and pick Change Clip Duration off the contextual menu. This dialog runs on the Cut page as well as the Edit page. The fresh Change Clip Duration box shown in Timecode mode. Here are the options in the Change Clip Duration Dialog box: Format: Choose whether to work in Time (Timecode) or in Frame values. Duration: Enter the timecode value or frame count you want the selected clip’s new length to be. Preset: Set a length by clicking 1, 5, or 15 seconds (or the matching value in frames). End stretches the length out to the selected clip’s final frame, no matter what Out points are set. Extend Beyond Clip Length (Cut page only): This tacks black filler onto any clip whose length is pushed past the clip itself. Cancel/Change: Hit Cancel to back out without altering the clip’s length, or Change to commit the new length to the selected clip. TIP: You can adjust the length of several clips together by selecting multiple clips before you open Change Clip Duration. Every selected clip will then take on the single length entered in the Change Clip Duration dialog box.

### Video Only and Audio Only Edits

As a rule, every edit function on the Cut page pulls in both a clip’s Audio and Video sections when placing it on the Timeline. There are, however, a number of situations in which you would rather use only the Audio or only the Video portion.

For an Audio Only edit: Click the Audio Only icon over to the left of the Upper Timeline, and click it off again to go back to the usual audio-and-video edit. For a Video Only edit: Click the Video Only icon to the left of the Upper Timeline, then click it off to resume the usual audio-and-video edit.

(Left) The Audio Only icon, (Right) The Video Only icon

### Drag and Drop Editing

Editing by drag and drop offers a simple route to stitching clips into a rough cut. After you have marked a span of media with the Source Clip or the Source Tape, you can click and drag — from either the Viewer or the Media Pool — onto the Upper Timeline or the Timeline beneath it to drop a clip into your program. The manner and the spot in which you drag dictate how that clip ends up edited.

### Append

Drop a clip onto a bare timeline, or onto the dark gray region left of the clips in the Timeline, and it becomes the opening clip of your edit. Drop a clip against the extreme left or right edge of every other clip in the Timeline’s upper or lower zone, and you tack that clip onto the Timeline’s end or start.

(Top) A clip being dragged to the Timeline’s far right so it appends, (Bottom) That same clip now appended

### Ripple Overwrite

Drag a clip over an existing one in the Timeline or Upper Timeline so the whole clip lights up, then drop it at once, and you carry out a Ripple Overwrite edit, swapping the old clip in the Timeline for the new one. Once you have ripple overwritten a clip on Track 1, every clip to its right shifts along — opening room when the incoming clip runs longer, or closing the gap when it runs shorter.

(Top) Clip DD being dragged over clip BB on the Timeline so as to Ripple Overwrite clip BB, (Bottom) Because clip DD runs shorter than clip BB, the Timeline shrinks after the edit completes

### Overwrite

Drag a clip over an existing one in the Timeline or Upper Timeline and pause for a beat, and the Timeline overlay shifts from lighting up the entire clip to lighting up only the slice of the incoming clip that sits over the existing one. Release the clip and you carry out an Overwrite edit, which paints the incoming clip’s media over whatever media already occupies the Timeline. An Overwrite edit leaves the Timeline unrippled.

(Top) Clip DD being dragged over clip BB on the Timeline with a pause to trigger an Overwrite, (Bottom) Clip DD paints over the middle of clip BB, splitting it in two even as the Timeline keeps its length

### Using Cut Page Edit Commands

Along the bottom of the Media Pool sit five buttons that open up other kinds of edits. A few of these carry keyboard shortcuts and also have dedicated keys on the DaVinci Resolve Editor Keyboard.

### Smart Indicator showing where an edit will occur

The edit buttons beneath the Media Pool run in this order: first Smart Insert, then Append and Ripple Overwrite, followed by Close Up, then Place On Top, and finally Source Overwrite

### Smart Indicators

Several of the smart tools on the Cut page spare you from setting explicit In and Out points in the Timeline; instead they read where the playhead sits over a clip to infer the spot you probably mean to edit. Wherever DaVinci Resolve plans to land that edit is flagged by a Smart Indicator icon along the Timeline Ruler. So the edit points read more easily on the Timeline, after a few seconds the Smart Indicator bobs up and down on the Timeline ruler while the actual edit point pulses green (or red, should the clip have hit its first or last frame).

### Setting Up and Performing Edits

Whatever sort of edit you have in mind, the routine for setting it up and carrying it out stays identical. What this section lays out is that general routine, while the sections after it explain how each individual edit operates. To set up and perform an edit: 1 To begin, find a clip you want to drop into the Timeline. Two broad approaches exist: a) Open a bin holding the clips you want, then click the Source Tape in the Viewer to lay out a stringout of every clip in the current bin and its subfolders, ordered by the sort you currently have chosen. From there, scrub through them all with JKL or the DaVinci Speed Editor’s shuttle/jog/ scroll wheel until you spot the media you are after. b) Open a bin holding the clips you want and work through the thumbnails, filmstrips, or columns to pick the one you need, calling on the Search field when it helps you track the clip down. 2 Scrub a thumbnail or filmstrip, work the controls in the Viewer, or use your DaVinci Speed Editor’s controls to find the frames where you want In and Out points marking an edit range, then press the I (In) and O (Out) keys to lay those points down.

3 Where it matters, pick the video track you want to edit onto by clicking its track header to select it; selected tracks show highlighted. 4 Carry out an edit that drops the source clip’s chosen range onto the selected video track at the frame you want, using either the buttons along the bottom of the Media Pool or keyboard shortcuts. Each edit command lands the source clip somewhere different. 5 With your edit committed, press Q (or click the Timeline Viewer button) to flip the Viewer over to the Timeline so you can play back and review what you just cut, then press Q once more to return to the Source Clip or Source Tape (whichever you used last) and hunt down the next clip to edit, beginning the whole cycle again at Step 1.

### Smart Insert

Drops the incoming clip in on its own at whichever edit point lies nearest the playhead (flagged by the Smart

Indicator) along the chosen track, shoving every clip beyond that edit point forward to open space

for the incoming clip when you have inserted onto Track 1. Since this counts as a smart operation, it bars you

from dropping a clip at just any frame you please; incoming clips only land at the nearest already

present edit point.

(Top) Ahead of a Smart Insert, (Bottom) Once clip DD has been inserted between clips AA and BB Append Here the playhead’s position carries no weight; incoming clips always go in right after the final clip on the Timeline.

Performing an Append edit of clip DD to the Timeline
