# Source clip and viewer showing source clip

Version: DaVinci Resolve 20.3 Reference Manual. Context: Fast editing in the cut page.
[Chapter index](INDEX.md) / [Previous section](creating-and-modifying-timelines-and-creating-new-timelines.md) / [Next section](snapping-to-guide-lines-and-proxy-handling.md)
<a id="source-custom-guides-and-snapping-in-the-timeline-viewer"></a> <a id="source-source-clip"></a> <a id="source-the-addedit-guide-dialog"></a> <a id="source-the-timeline-viewer-with-guides-and-rulers-enabled"></a> <a id="source-the-viewer-showing-source-clip"></a> <a id="source-the-viewer-showing-source-tape"></a> <a id="source-the-viewer-showing-the-multi-source"></a> <a id="source-the-viewer-showing-the-timeline"></a>

### Source Clip

This option displays the clip currently selected in the Media Pool. It's the mode the Viewer automatically

switches into whenever you double-click a clip in the Media Pool. Within Source Clip, a scroll area shows up

at the bottom of the Viewer, its width standing in for the duration of the currently open clip.

Within the scroll area a playhead lets you scrub the clip as a zoomed-in waveform while playing back

whatever audio falls within the clip. Handles at the left and right of the scroll area let you reposition

In and Out points within the clip to pick a section you'd like edited into the Timeline. These In and Out

points can also be set with the I and O keys. Once they're set, you can drag In and Out points to shift them.

### The Viewer showing Source Clip

The Source Clip option's scroll area, In and Out points placed on either side of the playhead Source Tape Under this option, every single clip in the currently open bin of the Media Pool, plus any subfolders within that bin, is presented in the Viewer as a "stringout" within the scroll area running along the Viewer's bottom. Within that scroll area, each clip follows the next in a long strip, ordered by the Sort order. This makes scrubbing through a whole batch of clips easy while you figure out what to use. As you play through, whichever clip the playhead crosses is selected in the Media Pool, so you know which clip is on screen.

### The Viewer showing Source Tape

The Source Tape's scroll area, a thin line dividing each clip from the next Timeline This option displays the current frame wherever the playhead sits in the Timeline. The instant you click, drag, or adjust a clip within the timeline area, the Viewer flips over to the Timeline. With this option there's no scroll area; you have to use the timeline area to scrub through your program. However, where the scroll area would otherwise sit, icons appear to signal when the playhead lands on the first or last frame of a clip in the Timeline.

### The Viewer showing the Timeline

Multi Source Where you have multiple clips synced either by timecode or waveform, you can view them all together, even across multiple bins in your project. Picking this option opens the Multi Source viewer within the Source Tape. It lays every synced media item out in a grid, with all media ganged together as you scrub through. In this mode, the In and Out points you set hold constant across the various angles, so swapping cameras leaves those same In and Out points valid on every clip. Such features let you rapidly settle on the best angle for a multi-camera shoot.

### The Viewer showing the Multi Source

In and Out points set within the Multi Source. They stay put as you change camera angles. Along the right side sit these Viewer controls, in order: Safe Area first, followed by Proxy Handling, next the Timeline Resolution control, and finally Bypass Color Grades and Fusion Safe Area This drop-down menu drapes a host of helpful framing guides across the Viewer so you can see which portion of the image stays in and which portion gets cropped off should the Timeline's aspect ratio change. Toggling the Safe Area Framing Guide icon in the Viewer switches the framing guides on and off, while the exact guides are picked from the drop-down menu.

Social Media: 1:1, 4:5, 9:16, 1.91:1, 16:9. Broadcast and Film: Default (your current timeline aspect ratio), 1.33, 1.66, 1.77, 1.85, 2.35. Safe Area Guides: These options drop additional guide lines onto the Viewer so your composition isn't at risk of being clipped at the outermost edges of a physical cathode ray tube. Though a touch anachronistic in this era of flat screen digital televisions, plenty of legacy programs still observe these guidelines. Safe Areas can still serve as useful guides for making sure your image isn't unintentionally cropped by the range of mobile devices and social media sites around today.

- Extents: Show the full boundary of the frame.
- Action: Keep all movement and important action within this box.
- Title: Keep all on screen text within this box.
- Center: Designates the exact middle of the image.

The extents Safe Area overlay can be toggled on or off, as can the Action, Title, and Center overlays. You can reach these features at View > Safe Area > Extents.

The Safe Area Framing Guide icon and the possible framing options

### Custom Guides and Snapping in the Timeline Viewer

The Timeline Viewer is where you can build your own custom guides. That gives you full customization to set specific geographic spots in the frame, then have the image snap to those spots during other operations. You can build Guides, which are colored lines crossing the frame either horizontally or vertically, plus Rulers, supplying measurement metrics down the frame's edges. As overlay tools for tuning your video position, both Guides and Rulers appear in the viewer alone, never in your final project output.

### The Timeline Viewer with Guides and Rulers enabled

Each of Guides and Rulers can be displayed separately by clicking its icon within the Ruler Guides section of the Timeline Viewer's Viewer Guides drop-down menu. Switching them on separately is also possible by way of the View > Rulers menu and the View > Guides menu. The Ruler Guides part of the Viewer Guides dropdown To Show and Modify a Ruler: 1 Turn the Ruler on by choosing View > Rulers > On, or by clicking the Ruler Icon in the Timeline Viewer's Viewer Guides dropdown. 2 Choose the metric the Ruler should use within View > Rulers, or by right-clicking the Ruler in the Viewer. Pixel: Renders the ruler as a pixel count measured out from the origin point (0,0) sitting at the frame's middle on a standard x/y cartesian coordinate graph, echoing the Position field in the Video Inspector. Percentage: Renders the ruler as a percentage distance measured out from the origin point (0%, 0%) at the frame's top-left. From left to right the top ruler spans 0% to 100%, while top to bottom the side ruler gauges 0% to 100%. To take an example, a point dead center in the frame would land at (50%, 50%).

### The Add/Edit Guide dialog

To Show and Create a Guide Line:

1 Activate the Guides by choosing View > Guides > On, or by clicking the Guides Icon in the Viewer

Guides dropdown on the Timeline Viewer.

2 To produce a fresh Guide, either choose View > Guides > Add Guide, or right-click the Ruler within the Viewer and pick Add Guides.

3 In the Add Guide dialog, pick the position and orientation you want the new guide to have, and click Add.

Units: Choose the metric the guide line should adopt. Pixel reports the pixel count out from the guide's origin point, whereas Percentage reports the percentage distance out from the frame's top left at 0%,0%. Position: Type a value for the spot in the frame the guide line should cross. The line can also be clicked and dragged in the viewer to place it by eye (as you move it, a small popup surfaces the exact position value). If you like, click the lock icon so this guide can't be nudged by accident. Orientation: Choose a horizontal or vertical orientation for the line. Color: Choose the guide line's color out of the available options.

To Modify a Guide Line:

- Drag the line wherever you like in the viewer, and a small pop-up window surfaces to reveal the exact position value.
- For legibility, recolor the Guide Lines by right-clicking within the Ruler and choosing a fresh color out of the Guide Color context menu.
- Delete a line by right-clicking it in the viewer and choosing Remove Guide.
- Reposition and reorient an existing line by right-clicking it in the viewer and choosing Edit Guide.
- Remove all lines, the horizontal ones only, or the vertical ones only, by choosing View > Guides > and picking the relevant lines to clear. The ruler's right-click menu does this too.
- Pin Guides in place against accidental movement by clicking the small lock icon at the Ruler's upper-left, or by choosing View > Guides > Lock Guides.

A right-click on the Ruler opens a context menu through which every parameter of the Rulers and Guide lines can be tuned
