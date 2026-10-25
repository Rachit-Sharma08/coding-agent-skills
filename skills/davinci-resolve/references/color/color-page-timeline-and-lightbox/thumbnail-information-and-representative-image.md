# Thumbnail info and dragging a thumbnail to change the representative image

Version: DaVinci Resolve 20.3 Reference Manual. Context: Color page timeline and lightbox.
[Chapter index](INDEX.md) / [Previous section](color-timeline-navigation.md) / [Next section](project-options-flags-clip-colors-and-markers.md)
<a id="source-a-and-c-mode-sorting"></a> <a id="source-a-mode-sorting-ie-record-order"></a> <a id="source-c-mode-sorting-ie-source-clip-order"></a> <a id="source-changing-timelines"></a> <a id="source-dragging-a-thumbnail-to-change-the-representative-image"></a> <a id="source-sorting-and-filtering-clips-in-the-thumbnail-timeline"></a> <a id="source-thumbnail-contextual-menu-commands"></a> <a id="source-thumbnail-info"></a>

### Thumbnail Info

Because the thumbnails always render the media in its current graded state, they make spotting the clips you need a visual breeze. The single most evident detail is whichever frame stands in for each clip's thumbnail. Should you decide a given clip's thumbnail doesn't really capture its content, it can be swapped. To change the current thumbnail:

- Hover the pointer over a thumbnail, drag rightward or leftward to scrub the clip, and halt once you reach a frame you'd like as the replacement thumbnail.

### Dragging a thumbnail to change the representative image

When media gets swapped partway through a color correction timeline, or once you copy or ripple a grade across a span of clips, the thumbnails might not refresh right away to faithfully mirror each clip's present condition. Should that happen, you can refresh the thumbnails by hand.

To refresh all thumbnails in the Timeline:

- Right-click any spot in the Thumbnail timeline and pick Update All Thumbnails. You also have the option to show the codec, clip names, and the version each Timeline clip is using.

To switch the Thumbnail timeline between showing clip names, codecs, and versions:

- Double-click any clip's thumbnail clip name to rotate through that clip's codec, clip name, and version. Extra detail shows up over and under every thumbnail, offering a way to monitor which clips are graded, which run different versions, which have been cached, and the like.

Every clip thumbnail carries several useful markers that make rapid comparison against other shots easy. The list below clarifies each detail that may turn up over, inside, or beneath the Timeline's thumbnails.

- Clip number: (top left) The number of each clip shows above its thumbnail. Numbering climbs from left to right based on where each clip's first frame falls, no matter which video track holds the clip.
- Grade indicator: (top left) Once a clip has been graded, a slim rainbow ring wraps the clip number.
- Source Timecode: (top center) Above every thumbnail you'll find the source timecode taken from each clip's opening frame.
- Cache indication: (red timecode) Whenever a clip is flagged for caching — be it by the Smart cache automatically or by hand — its timecode goes red to signal it's headed for caching. After the cache completes, that timecode shifts to blue.
- Track number: (top right) Above the thumbnail appears the video track on which a clip is cut.
- Clip Color dot: (upper right) Should a clip carry an assigned clip color, a tinted dot lands atop its thumbnail.
- Flag icon: (upper left) When a clip carries a flag, a flag icon in the matching color sits over its thumbnail. Where a clip holds several flags, as many as will fit are drawn along the top.
- Linked media or group icon: (bottom right) Where clips are set to draw on remote versions, and where several clips draw on one shared source media file, their remote version 1 grade links up automatically by default. When the current clip is linked, a tiny link icon shows under the thumbnail of every other Timeline clip linked to it. Pick a clip that isn't linked and those linked-clip icons go away.
- Tracker icon: (bottom right) If any node inside a given clip's grade has been tracked, a tiny crosshairs tracker icon turns up beneath the thumbnail.
- 3D indicator: (bottom right) Each stereo 3D clip on the Timeline carries this icon under its thumbnail. Its color tells you which eye you're watching; red marks the left eye, blue the right.
- Version name/Source format: (bottom left) You can alter what shows beneath each thumbnail by double-clicking the area under it. Several choices exist; keep double-clicking to rotate among them: Clip format or codec: This is the default display. Clip Name: Based on the View > Show File Names setting, either the clip name or the file name shows. Working with multicam clips means the multicam name or angle appears. Version name or number: Tells you whether a clip draws on a remote version or a local one, the latter shown by an (L). Should you have named the current version, that name appears; if not the version reads "Version" followed by its number.

### Thumbnail Contextual Menu Commands

A right-click on any clip's thumbnail within the Thumbnail Timeline opens a contextual menu packed with the Color page's many media and grade management commands. Those choices fall into roughly these groupings:

- Commands for managing grade versions
- Commands for managing groups
- Commands for editing flags, markers, and clip colors
- A command for displaying the Node Graph of a clip's grade
- Options for controlling the render cache
- Resolve Color Management clip assignments
- LUT Management commands
- Commands that show clip details, edit Clip Attributes, and locate clips within the Media Pool
- A command that refreshes clip thumbnails which lag in updating by themselves

The chapters elsewhere in this manual cover these abilities at greater length, but the takeaway is that Color page artists have plenty of clip management choices on hand without ever leaving for other pages.

### Sorting and Filtering Clips in the Thumbnail Timeline

Out of the box, the Thumbnail Timeline lays out every clip of the Edit page's currently chosen edit, ordered in A mode (your edit's record order). That said, you can reorder and filter both the sort and the Timeline's contents to make tracking down particular clusters of clips for grading simpler.

### Changing Timelines

Should your project hold more than a single timeline, you can swap timelines without leaving the Color page. Swapping timelines from the Color page works like this: Pick a different timeline out of the Timelines drop-down menu sitting at the Viewer's top.

Timeline selection at the top center of the Viewer

### A and C Mode Sorting

By default the Timeline runs Record mode sorting, which also goes by the name A mode sorting. Under it, clips line up in the Timeline following the sequence in which they were cut. That lets you preview the clip order exactly as it'll show in the finished program.

### A Mode sorting, i.e., record order

You can, however, flip the Timeline's clip sort to Source mode, otherwise called C mode sorting. With C mode sorting, every clip is reordered left to right in climbing order by its source timecode, while record timecode is set aside for the moment.

### C Mode sorting, i.e., source clip order

Sorting via C mode makes pinpointing a band of like clips straightforward. Take a narrative project: clips from each coverage angle of the scene will gather together on their own. For another case, applying C mode sorting in a documentary lines up all the head shots of one subject from a given interview back to back, since every one stems from the same timecode range on the same source tape. In each case, the way C mode pulls similar clips near one another makes it simple to share grades across them, ripple edits, or group them. Once you're done, you can flip the Timeline back to A sort mode, and all the clips return to the sequence in which they were cut. Flipping back and forth between A and C mode sorting is done by either of these:

- Choose an option from the View > Timeline Thumbnail Mode submenu.
- Hit Command-Page Down to flip into C mode sorting. Whenever C mode is active, the word "SOURCE" shows up on the right side within the Mini-Timeline's Timeline Ruler.

Source mode indicated at the right of the Timeline ruler
