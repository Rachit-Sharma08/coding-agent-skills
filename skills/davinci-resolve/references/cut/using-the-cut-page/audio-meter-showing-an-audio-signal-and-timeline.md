# Audio meter showing an audio signal and timeline

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the cut page.
[Chapter index](INDEX.md) / [Previous section](cut-viewer-modes-playback-and-navigation.md) / [Next section](edit-actions-and-all-of-the-edit-actions-functions.md)
<a id="source-all-of-the-timeline-actions-functions"></a> <a id="source-all-of-the-timeline-options-functions"></a> <a id="source-lower-timeline"></a> <a id="source-the-audio-meter-showing-an-audio-signal"></a> <a id="source-the-timeline"></a> <a id="source-timeline-actions"></a> <a id="source-timeline-options"></a> <a id="source-upper-timeline"></a>

### The Audio Meter showing an audio signal

### The Timeline

The term "timeline" covers two things: an edited sequence of clips, which forms a program kept in the Media Pool, and the region of the Cut page interface where you open that sequence of clips to view its contents, play it back, and edit it.

Timelines are built and held in the Media Pool right alongside your other clips. Each timeline, though, is put together and edited in what people sometimes call the Timeline Editor. The various pages of DaVinci Resolve present your timeline differently to suit each page's particular needs, with their focus shifting variously across editing, grading, compositing, and audio.

Yet while the Timeline Editor's interface shifts from page to page, what's actually in the Timeline stays the same, because every page's Timeline Editor is really displaying the very same Timeline you have open. So an advanced user can use each page of DaVinci to do different things to one Timeline, with only the interface shifting to enable different functions on different pages.

For the Cut page user, the Timeline splits into an Upper Timeline up top and a bigger, more

detailed Timeline Editor down below showing a zoomed-in slice of the Timeline around the playhead. Together,

these two views of your edited sequence let you move through your

whole project and cut in fine detail.

The Cut page Timeline, made up of the Upper Timeline together with the zoomed-in Lower Timeline

### Upper Timeline

Across the full width of your computer's display, the Upper Timeline always shows the whole program. Its playhead always runs free, so you can easily scroll around the entire program by dragging the pointer within the Timeline Ruler up top. It also doubles as a visual cue for tracking where you sit in your program while editing inside the zoomed-in Lower Timeline below. Small as the Upper Timeline is, you can still edit there, with most of the editing and trimming functions found in the Lower Timeline available in it too. Most intriguingly, you can also drag clips from one stretch of your program in the Lower Timeline over to another stretch in the Upper Timeline, and the reverse as well. Right-clicking a clip in the Upper Timeline brings up the same context menu as right-clicking one in the Cut page's main timeline, so you can carry out the same operations. A row of small numbers down the left side of the Upper Timeline lets you click a number to set the currently selected track; that pick is mirrored on the zoomed-in timeline below. Which track is selected affects where incoming clips drop in during editing, among other things.

### Lower Timeline

The zoomed-in Lower Timeline (often called simply "the Timeline") gives you a close-up of the part of the open timeline immediately around the playhead. Its zoom level is fixed and can't be changed. Detailed editing is what the zoomed-in lower timeline is for, though you can drag clips back and forth between the Timeline and Upper Timeline to swiftly reorder them across your whole program. Several editing functions sit in the Toolbar, gathered into Action and Option menus. You reach these functions by clicking the right icon and choosing a function from the drop-down menu. These tools get full coverage throughout the Cut section of the manual.

The Toolbar icons, left to right: Timeline Options, Timeline Actions, Edit Actions

### Timeline Options

The tools beneath this icon concern how the clips and timeline are shown, plus certain modes and tools applying to the whole timeline.

### All of the Timeline Options functions

- Ripple On: Flips ripple editing behavior on track V1.
- Snap: Switches playhead snapping behavior on or off.
- Trim to Audio: Brings up an expanded audio view on the timeline as you trim a clip.
- Trim with Safe Edit: Flips the Safe Edit function, which stops you from inadvertently overwriting neighboring clips during a trim.
- Display Clip Names: Switches the clip's name on the timeline clip on or off.
- Display Clip Status: Switches on or off the status icons for assorted operations on the timeline clip.
- Display Speed Keyframes: Switches the Speed Keyframes on or off for a clip carrying speed changes.
- Viewer Background: Sets how the empty regions of the Viewer background appear, whether Checkerboard, Black, Gray, or Alert Red.
- Set Default Transition: Brings up the Set Default Transition window, where you pick the default transition's type, duration, and alignment.
- Edit Using (Audio Track): Lets you settle on either every audio track or particular audio pairs to

edit with on the Cut page.

- Minimize Subtitle Track: Cuts down the subtitle tracks' vertical height so there's extra room in

the timeline.

- Fixed Playhead: Switches the fixed playhead on or off. On holds the playhead still as the timeline slides beneath it; off sends the playhead traveling along the timeline.
- Boring Detector: Activates the Boring Detector.

### Timeline Actions

The tools beneath this icon mostly serve to add fresh items to the Timeline or make changes to it.

### All of the Timeline Actions functions

- Create Subtitles from Audio: Builds subtitles automatically for every line of dialog on the timeline.
- Detect Scene Cuts: Runs a Detect Scene Cuts operation that breaks one long clip of a finished program back into separate clips.
- Audio Assistant: Leans on AI to mix your timeline's audio automatically against common deliverable requirements.
- Voice Convert: Leans on AI so you can swap the speaking voice from one person for another.
- Add Video Track: Puts a video track onto the timeline.
- Add Audio Track: Puts an audio track onto the timeline.
- Add Subtitle Track: Puts a Subtitle Track onto the timeline.
- Split Clips: Cuts the current clip into two at the playhead position.
- Join Match Edit Clips: Reunites two continuous clips that were split apart.
- Add Marker: Drops a marker at the playhead position.
- Set Color and Add Marker: Drops a marker and brings up the Markers editor, letting you change the color, add comments, and so on.
- Clear Transition from All Edits: Strips every existing transition off the timeline.
- Add Dissolve to All Edits: Puts a Cross Dissolve on every edit point along the timeline.
- Add Transition to All Edits: Puts the last-used transition on every edit point along the timeline.
