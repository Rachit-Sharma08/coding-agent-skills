# The viewer and viewer title bar

Version: DaVinci Resolve 20.3 Reference Manual. Context: Viewers monitoring and video scopes.
[Chapter index](INDEX.md) / [Next section](add-edit-guide-dialog-and-proxy-handling.md)
<a id="source-custom-guides-and-snapping-in-the-timeline-viewer"></a> <a id="source-safe-area"></a> <a id="source-the-timeline-viewer-with-guides-and-rulers-enabled"></a> <a id="source-the-viewer-title-bar"></a> <a id="source-using-the-viewer"></a> <a id="source-viewer-guides"></a> <a id="source-viewers-monitoring-and-video-scopes"></a> <a id="source-viewers-monitoring-and-video-scopes-part-1"></a>

### Viewers, Monitoring, and Video Scopes

A Viewer shows you what you're working on, supplies a UI for transport controls and image comparison, lets you draw windows and drag on-screen controls, and surfaces an assortment of warnings and information you won't find elsewhere. Yet professional pipelines also demand real-time monitoring on a calibrated display through supported video I/O hardware. Finally, video scopes deliver a sharper read on the condition of the video signal in front of you, and DaVinci Resolve ships with built-in scopes you can lean on for creative calls and troubleshooting alike. The pages here go deeper on the Color page Viewer, external monitoring with display calibration, and video scopes.

### Using the Viewer

Your window onto the Timeline is the Viewer. Whatever clip and frame sit at the playhead's current spot show up in the Viewer. The Viewer also doubles as a workspace for sampling colors, tuning Windows, leaning on split screen stills for reference, and a host of other display-centered jobs. When a video out interface is hooked to a broadcast display or projector, the video output usually mirrors what the Viewer holds.

### The Viewer Title Bar

Controls and indicators along the Viewer title bar make it simple to steer and stay aware of exactly what you're looking at.

The Color page Viewer title bar with its controls Here is what the Viewer title bar's controls do: Zoom and Fit menu: Lets you zoom to an exact percentage, or pick Fit to size the image to the Viewer's whole available area. Viewer Mode: Flips the Viewer type over to the Image Wipe. Split Screen, or Highlight modes. Viewer Mode: Flips the Viewer type over to Split Screen Viewer Mode: Flips the Viewer type over to Highlight Playback frame rate indicator: This dot reads green while playback stays in step with the project's frame rate, and red once playback drops under real time. The present frame rate appears just to its right. Timeline name and selection drop-down: It shows the name of whatever timeline happens to be open at the moment. The drop-down beside it lets you bring in any other timeline belonging to the current project. Timecode viewer and drop-down: Through a second timecode viewer you can pick an alternate timecode/frame count/KeyKode value, shown at the same time as the timecode viewer beside the transport controls below. A drop-down lets you set whether source (clip) or record (timeline) timecode is shown. Viewer Guides: Lets you arrange Safe Area together with custom Guides and Rulers. Proxy Handling: Lets you go with either proxies or original media as playback runs. Switch Timeline Resolution: Lets you alter which timeline resolution preset is active. Bypass Color and Fusion and drop-down: Switches off grades and/or Fusion effects on command. Expand Viewer drop-down: Stretches the Viewer to fill your workstation display's full area above the palettes. Option menu: Holds options affecting how the Viewer behaves.

The Color Viewer's option menu, showing all the Viewer-related commands

- Highlight: Carries options that switch on the Highlight, Black and White, and Difference views.
- Show RGB Picker Values In: Pick whether the RGB picker reports its values on an 8-bit or 10-bit scale.
- Show Viewer Channels: Offers options to pick every channel, or just R, G, or B individually, in the Viewer.
- Split Screen: Holds options for switching the Split Screen view on or off and for what it shows.
- Timeline Sort Order: Offers options governing the order of the timelines within the drop-down menu at the

top of the Viewer. The choices are: Alphabetical, Creation Date, or Recently Used (which lists the 10 most recently active timelines).Previous Timeline: Opens whichever timeline precedes the current one in the Timeline drop‑down menu list.

- Next Timeline: Opens whichever timeline follows the current one in the Timeline drop-down menu list.
- Show Viewer Options: Reveals or hides that second row of icons across the top of the Viewer, according to the mode you happen to be in.
- Show Marker Overlays: Any markers the paused playhead lands on show up superimposed over the Viewer.
- Window Outline: Carries options for how a Power Window's window outline is drawn. On, Off, or confined to the UI viewer while staying off your video output.
- Video Output Options: Offers options for what your video output signal carries, namely Flags, Markers, Keyer Overlays, plus the choice to Gang the Zoom level with the Viewer.
- Markers: Shows whatever markers have been placed on the timeline. Pick one from the list to jump to that marker.
- Show Reference Wipe: Switches the reference wipe on or off.
- Reference Wipe Mode: Carries options that alter which sources feed the reference wipe.
- Wipe Style: Carries options that alter which kind of reference wipe gets used.
- Invert Wipe: Flips the current reference wipe.
- Reference Reposition: Brings up the Reference Sizing controls, which let you resize and reposition the reference clip.
- Gang Timeline Wipe With Current Clip: Keeps the gap between the current clip and a timeline clip you're wiping against intact as you shift the current clip selection onto other clips.

### Viewer Guides

### Safe Area

A whole set of handy framing guides drops over the Viewer from this drop-down menu, showing you which slice of the image stays and which gets cropped away should you alter the Timeline's aspect ratio. You toggle the framing guides on and off via the Safe Area Framing Guide icon in the Viewer, and the precise guides come from the drop-down menu. Social Media: 1:1, 4:5, 9:16, 1.91:1, 16:9. Broadcast and Film: Default (your current timeline aspect ratio), 1.33, 1.66, 1.77, 1.85, 2.35. "Safe Area Guides: These choices lay extra guide lines over the Viewer that shield your composition against getting clipped at the outermost edges of a physical cathode ray tube. Although a bit of a relic now that flat-screen digital televisions rule, plenty of legacy programs still hold to these guidelines. Even so, Safe Areas remain useful guides for keeping your image from being unintentionally clipped across the assortment of mobile devices and social media sites people rely on today.

- Extents: Show the full boundary of the frame.
- Action: Keep all movement and important action within this box.
- Title: Keep all on screen text within this box.
- Center: Designates the exact middle of the image.

Alongside the Action, Title, and Center overlays, you can switch the extents safe area overlay on or off. These features live at View > Safe Area > Extents."

The Safe Area Framing Guide icon and the possible framing options

### Custom Guides and Snapping in the Timeline Viewer

The timeline viewer lets you build guides of your own. That way you can fully tailor and pin down particular geographic spots in the frame, then have the image snap onto those spots during other operations. You can lay down Guides, the colored lines crossing the frame horizontally or vertically, plus Rulers, which line measurement metrics along the frame's edges. Both Guides and Rulers act as overlay tools for tuning your video position, appearing only in the viewer rather than your finished project output.

### The Timeline Viewer with Guides and Rulers enabled

You can show Guides or Rulers separately by clicking the relevant icon, found under Ruler Guides inside the Timeline viewer's Viewer Guides drop-down menu. Each can likewise be switched on by itself through the View > Rulers and View > Guides menus.

The Ruler Guides section of the Viewer Guides dropdown

To Show and Modify a Ruler: 1 Turn the Ruler on by choosing View > Rulers > On, or by clicking the Ruler Icon in the Viewer Guides dropdown of the Timeline Viewer. 2 Decide which metric the Ruler should use through View > Rulers, or by right-clicking the Ruler in the Viewer. Pixel: Marks the ruler as a pixel count out from the origin point (0,0) at the frame's center, on a standard x/y cartesian coordinate graph that mirrors the Position field in the Video Inspector. Percentage: Marks the ruler as a percentage distance out from the origin point (0%, 0%) at the frame's top-left. Across the top, the ruler goes from 0% on the left to 100% on the right, while down the side it reads 0% at the top down to 100% at the bottom. So a point sitting dead center in the frame lands at (50%, 50%).
