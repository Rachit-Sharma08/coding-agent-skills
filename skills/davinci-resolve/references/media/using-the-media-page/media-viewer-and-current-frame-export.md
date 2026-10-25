# Media page viewer and export the current frame from the viewer

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the media page.
[Chapter index](INDEX.md) / [Previous section](list-view-and-thumbnail-view.md) / [Next section](thumbnail-list-and-metadata-views-in-the-media-pool.md)
<a id="source-bins-power-bins-and-smart-bins"></a> <a id="source-export-the-current-frame-from-the-viewer"></a> <a id="source-filtering-bins-using-color-tags"></a> <a id="source-live-media-preview"></a> <a id="source-media-pool"></a> <a id="source-media-pool-bins-opened-as-new-windows"></a> <a id="source-media-pool-with-the-bin-list-open"></a> <a id="source-showing-bins-in-separate-windows"></a> <a id="source-sorting-the-bin-list"></a> <a id="source-the-bin-list"></a> <a id="source-the-media-page-viewer"></a> <a id="source-using-color-tags-to-identify-bins"></a>

### The Media page Viewer

Underneath the jog bar you will find basic transport controls: among them Jump to First Frame, then Play Backward, Stop, Play Forward, plus Jump to Last Frame. Sitting just left of those buttons, a jog control helps you crawl through a lengthy clip; click it and drag leftward or rightward to advance a clip one frame at a time. Clicking the speaker icon toggles audio playback on or off, while right-clicking that icon and dragging the slider sets the level. Over on the right side of the transport controls sit In and Out buttons, which mark In and Out points on the current clip. The clip's timecode is shown at the top right as well.

Directly below the image runs a jog or scrubber bar, letting you drag the playhead about with the pointer. The whole span of the jog bar stands for the clip's entire duration in the Viewer. You can skim footage in any viewer across the Media, Cut, Edit, Color, and Deliver pages by holding the C key down and sweeping the pointer back and forth in the viewer. The Media Viewer carries an option menu shaped like three dots in the upper right corner. Clicking that menu opens the options below.

An optional info bar that reports the timecode along with the duration of a media section you have marked Media Viewer Option menu: Holds the following commands:

- Live Media Preview: On by default, it lets thumbnails you skim in the Media Pool show the skimmed frame inside the Viewer. While you skim with Live Media Preview on, the playhead shown in the thumbnail stays tied to the playhead displayed in the Viewer's jog bar.
- Show All Video Frames: When the processing power on hand cannot play the clip or clips at the playhead position owing to the grade, transforms, or effects applied at that point in the Timeline, you get to decide exactly how DaVinci Resolve performance falls off. Turned off, DaVinci Resolve favors audio playback and drops video frames when processing power runs short, yielding a more conventional playback experience. Turned on, audio quality takes a hit while every video frame plays in slower-than-real time to hold playback together.
- Show Timecode Toolbar: The Timecode Toolbar displays the In/Out point timecodes along with the total duration set.
- Show Audio Waveforms in Source Clip: Once enabled, it lays an audio waveform overlay along the bottom of the Source Viewer that shows the audio across the clip's whole duration.
- Show Audio Waveforms Zoomed In: Once enabled, it lays an audio waveform overlay along the bottom of the Source Viewer showing a zoomed-in slice of the audio around the playhead's current position.
- Previous Clip: Jumps to the previous clip in the Media Pool.
- Next Clip: Jumps to the next clip in the Media Pool.
- Clear Recently Viewed Clips: Wipes the memory of recent clips in the Source Viewer.
- Show Marker Overlays: On by default, markers that meet the playhead while playback is paused appear overlaid in the Viewer.
- Markers submenu: Whenever one or more markers sit on the clip in the Source Viewer, they list here in chronological order by Name and Note. Picking a marker from this menu sends the playhead to that marker in the Source Viewer.

You can also drop the Viewer into Cinema Viewer mode by picking Workspace > Viewer Mode > Cinema Viewer (Command-F), so that it covers the whole screen. That command switches Cinema Viewer mode on and off.

### Export The Current Frame from The Viewer

Across the Media, Cut, and Edit pages, you can now push out a still frame from the Viewer. To Export a Still Frame from the Viewer: 1 With the Viewer’s playback controls, move to whichever frame you intend to export. 2 Select File > Export > Current Frame as Still. 3 Within the File System viewer, type a name for the still frame. 4 Within the File System viewer, set the format you want for the still frame. 5 Press the Export button.

### Live Media Preview

On by default, the Live Media Preview setting in the Viewer options menu (the three-dots menu at the Viewer's upper right-hand corner) lets thumbnails you skim within either the Media Storage browser or Media Pool show the skimmed frame inside the Viewer. While you skim with Live Media Preview on, the playhead shown in the thumbnail stays tied to the playhead displayed in the Viewer's jog bar. You can flip Live Media Preview on or off.

With Live Media Preview switched on via the Viewer options menu, thumbnail skimming is echoed in the Viewer

### Media Pool

The Media Pool sits at the heart of the DaVinci Resolve experience. It holds every piece of media you bring into the current project, along with all the timelines you build. It also holds whatever media gets imported alongside Projects, Timelines, or Compositions that have themselves been brought into DaVinci Resolve. On the Media page, the Media Pool is granted ample room, making it a fine place to sort, sift through, and arrange your project's clips. That said, the Media Pool is also mirrored across the Cut, Edit, Fusion, Color, and Fairlight pages, so you can reach clips while you assemble timelines, composites, grades, and sound design.

### Media Pool with the Bin list open

### The Bin List

Normally, every piece of media brought into a project lands in the Master bin, which always sits at the top of the Bin list and takes in everything across a given project. You can, however, add bins of your own, and the Media Pool can be arranged into as many user-definable bins as you wish, depending on what you need. Media moves freely from one bin to another right inside the Media Pool. When your project holds several bins, two approaches let you bring the bin structure into view: Bin list open: Found at the Media Pool's upper left-hand corner, the Bin List button opens a separate List view that shows every bin in your project, hierarchically. Bins holding other bins display a disclosure button to their left, which you use to reveal or hide the contents. With the Bin list surfaced, arranging clips across a large set of bins is easy. Bin list closed: Once the Bin list is shut, all bins vanish, and the contents of whichever bin is currently picked fill the Media Pool browser.

### Showing Bins in Separate Windows

When you right-click a bin in the Bin list, you can pick “Open As New Window” to throw that bin into a window of its own. Every such window is a Media Pool in its own right, with its own Bin, Power Bins and Smart Bins lists, plus display controls. This proves most handy when two displays are hooked up to your workstation, since, with DaVinci Resolve running in single screen mode, you can pull these separate bins over onto the second display. Hiding the Bin list not only buys you more room for clips, it also keeps you from accidentally flipping bins when all you really want is to view one particular bin's contents in that window. You can keep as many extra Bin windows open as you please, on top of the main Media Pool docked in the primary window interface.

### Media Pool bins opened as new windows

### Bins, Power Bins, and Smart Bins

In truth the Media Pool offers three sorts of bins, and each turns up in its own part of the Bin list. You can reveal or hide the Power Bin and Smart Bin regions of the Bin list through the Media Pool option menu by selecting or deselecting Show Smart Bins and Show Power Bins. Here is how the various kinds of bins differ: Bins: Plain, hand-filled bins. Drop whatever you like into a bin, and there it stays until you decide to shift it to another bin. Bins can be nested hierarchically, so you can build a Russian dolls stack of bins if you wish. Spawning new bins takes no more than a right-click inside the Bin list followed by picking Add Bin off the contextual menu. Power Bins: Off by default. They too are hand-filled bins, yet they get shared across every project sitting in your current project library, which makes them ideal for things like shared title generators, graphics movies plus stills, sound effects library files, music files, and whatever other media you want within quick, easy reach from any project. To build a new Power Bin, surface the Power Bins region of the Bin list, then right-click within it and pick Add Bin. Smart Bins: These bins fill themselves procedurally — that is, custom rules drawing on metadata dynamically sift through the Media Pool's contents the moment you pick a Smart Bin. That turns Smart Bins into fast ways to organize the contents of projects where you (or an assistant) have invested time tagging your clips with metadata through the Metadata Editor, supplying Scene, Shot, plus Take information, along with keywords, comments and description text, and a host of other details so that locating what you seek happens faster when the need arises. To build a new Smart Bin, surface the Smart Bin region of the Bin list (if it is not already shown), then right-click within it and pick Add Smart Bin. Up comes a dialog where you set that bin's name together with the filtering rules it applies to clips, then click Create Smart Bin.

### Filtering Bins Using Color Tags

When you are on a project loaded with bins, you can apply color tags to flag particular bins with one of eight colors. Tagging bins is as simple as right-clicking any bin and picking the color you want from the Color Tag submenu.

### Using Color Tags to identify bins

Using Color Tag filtering to isolate the blue bins

As an example, you might flag the bins holding the clips you reach for most often with a red tag. A bin's color tag then shows up as a colored backdrop behind that bin's name. Once one or more Media Pool bins carry tags, you can rely on the Color Tag Filter drop‑down menu — that drop-down control sitting just right of the Bin List button — to hide every bin save a single color. To return to seeing all available bins, pick Show All from the Color Tag Filter drop-down.

### Sorting the Bin List

The Media Pool's Bin list (and Smart Bin list) can be ordered, ascending or descending, by one of bin Name, Date Created, or Date Modified. Simply right-click somewhere inside the Bin list and, from the contextual menu's Sort by submenu, choose the options you are after. That same contextual menu also offers User Sort, which turns you loose to hand-drag every bin in the Bin list into any order you fancy. While you drag bins this way, an orange line marks where a bin will land once dropped. Should you use User Sort in the Bin list to reorder your bins manually, switching among the remaining sorting methods — Name, Date Created, Date Modified — and User Sort keeps your hand-set User Sort order intact, so leaning on whichever bin sorting method suits the moment costs you none of your customized bin organization.

Relocating a bin within the Bin list while User Sort mode is active

The Media Pool now lets you enable waveform thumbnails, which Live Media Preview can scrub.
