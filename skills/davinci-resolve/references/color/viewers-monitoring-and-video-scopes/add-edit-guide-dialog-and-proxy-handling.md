# Add edit guide dialog and proxy handling

Version: DaVinci Resolve 20.3 Reference Manual. Context: Viewers monitoring and video scopes.
[Chapter index](INDEX.md) / [Previous section](the-viewer-and-viewer-title-bar.md) / [Next section](viewer-controls-external-displays-and-zoom.md)
<a id="source-bypass-color-grades-and-fusion"></a> <a id="source-proxy-handling"></a> <a id="source-showing-marker-overlays-and-annotations"></a> <a id="source-the-addedit-guide-dialog"></a> <a id="source-the-onscreen-control-menu-for-the-viewer"></a> <a id="source-the-onscreen-control-osc-menu"></a> <a id="source-the-project-settings-quick-menu"></a> <a id="source-the-viewer-toolbar"></a> <a id="source-timeline-resolution"></a> <a id="source-toggling-viewer-overlays-on-and-off"></a> <a id="source-viewing-isolated-channels"></a>

### The Add/Edit Guide dialog

To Show and Create a Guide Line: 1 Switch the Guides on via View > Guides > On, or by clicking the Guides Icon inside the Timeline Viewer's Viewer Guides dropdown. 2 Add a fresh Guide via View > Guides > Add Guide, or right-click the Ruler in the Viewer and pick Add Guides. 3 Within the Add Guide dialog, dial in the new guide's position and orientation, then click Add. Units: Pick the metric the guideline should follow. Pixel reports the pixel count out from the guide's origin point, whereas Percentage reports the percentage distance from the frame's top left at 0%,0%. Position: Type in a value for the spot in the frame where the guideline should cross. The line can also be click-dragged in the viewer to place it by eye (a small popup surfaces the exact position value while you move it). If you like, click the lock icon so this guide can't be nudged by mistake. Orientation: Pick a horizontal or vertical orientation for the line. Color: Pick the guideline's color from the choices on offer.

To Modify a Guideline:

- Click and drag the line anywhere within the viewer; a small pop-up window surfaces to report the exact position value to you.
- For better legibility you can recolor the Guidelines by right-clicking inside the Ruler and picking a fresh color off the Guide Color context menu.
- Remove a line by right-clicking it in the viewer and picking Remove Guide.
- Alter an existing line's position and orientation by right-clicking it in the viewer and picking Edit Guide.
- Remove every line, only the horizontal ones, or only the vertical ones via View > Guides > and choosing which lines to drop. Right-clicking the ruler achieves the same thing.
- Pin Guides in place against accidental drift by clicking the small lock icon at the ruler's upper-left, or through View > Guides > Lock Guides.

Right-click the Ruler and a context menu opens for tuning every parameter of the Rulers and Guidelines Snapping to Guidelines By default, as you reposition the clip within the frame through the Transform Viewer controls, an image edge that drifts close to a guideline snaps onto it automatically, the guideline going purple to confirm it sits exactly. To turn that behavior off, just keep the option key down as you drag the image around the viewer, and the snap is skipped.

The Guidelines go purple once an image edge snaps onto that spot

### Proxy Handling

In the Cut page you can flip between playing back your original source media and the proxy media via the Proxy Handling icon in the Viewer, picking one of these options:

- Disable All Proxies: Picking this shuts proxies off entirely and forces playback from the original media alone. Should the original media be missing, a Media Offline graphic stands in for the clip.
- Prefer Proxies: Picking this plays back from the proxy files, and where a clip has no proxy file, the original media steps in on its own.
- Prefer Camera Originals: Picking this plays back from the original media files, and where a clip has no original media file, the proxy media steps in on its own.

The Viewer's Proxy Handling icon lets you decide how proxy files get used

### Timeline Resolution

Sitting at the Viewer's top-right, this drop-down menu lets you swiftly pick which resolution to work at. A Custom option opens the Timeline Settings panel so you can set your own options.

### The Project Settings quick menu

For more on the Timeline Settings, refer to Chapter 6, "Project Settings."

### Bypass Color Grades and Fusion

Through the Bypass Color Grades and Fusion Effects button/dropdown you can shut off every grade and effect you may have applied on the Color page and/or Fusion page, helping playback run better on lower-powered computers. Hit the button (Shift-D) to switch grading and effects off or back on, or right-click the button to reach a menu where you pick which things the button governs.

The Bypass Grades and Fusion button, pictured under a right-click that reveals its options

### Viewing Isolated Channels

Reach for the Show Viewer Channels submenu in the Viewer's option menu to flip the Color page Viewer between RGB, R, G, or B channels. That proves handy when judging one image channel for noise or other artifacts, or when color matching by comparing and tuning the individual red, green, and blue channels across two clips.

### The Viewer Toolbar

The Color page also lays out a toolbar above the image (just under the title bar) that makes enabling and disabling image wipe, split screen, and highlight viewing as easy as clicking one of these buttons, which then reveals further controls tied to each of those operating modes (covered elsewhere in this chapter). You can show or hide those options by clicking the Viewer option menu and unchecking Show Viewer Options.

The Color page Viewer toolbar, where the Wipe, Split Screen, and Highlight controls appear. You can spot the Highlight options in the bar beneath.

Along the way, these buttons give you an easy cue for when a comparison mode is on. Within each of these Viewer modes, the right controls for tailoring that view show up to the right of the Viewer toolbar.

### Showing Marker Overlays and Annotations

For Timeline and Clip markers, the Color page Viewer can display Marker Overlays and Annotations. Choose Show Marker Overlays off the Viewer's 3-dot option menu, or, via the Viewer overlay controls drop-down at bottom left, select the annotation mode.

With Show Marker Overlays checked, the Color Viewer renders any Marker Overlays (upper left) along with annotations.

### The Onscreen Control (OSC) Menu

Which onscreen controls you want to show and tune in the Viewer is your call through the Onscreen Control drop-down menu. Opening certain palettes switches on their matching onscreen controls automatically. As an example, opening the Window palette brings up the Power Window onscreen controls, and opening the Qualifier palette brings up the Qualifier onscreen controls.

### The onscreen control menu for the Viewer

A spread of choices awaits you, each one bound to a separate adjustment you can perform: Off: Every onscreen control drops out of sight, leaving the image in the Viewer free of clutter. Qualifier: Switches on the Color Sample cursor. To read more on using the Color Sample controls, see Chapter 135, "ColorSlice." Power Window: Switches the Power Windows onscreen control on and off. For deeper coverage of adjusting Viewer windows, refer to "Power Windows" see Chapter 138, "Secondary Windows." Image Wipe: Switches mouse-driven dragging of the split screen right on the Viewer on and off. For deeper coverage of split-screen work, see "Comparing Clips in the Viewer" later on here. Open FX Overlay: Reveals and hides whatever onscreen controls an Open FX plugin exposes within the currently selected node. Color Chart: Reveals and hides the color chart overlay, which lets you flag a color chart in the picture for use with the Color Match palette to build an automatic grade. Annotations: Brings the annotation tools into the toolbar. Annotating a frame that lacks a marker spawns a fresh Timeline marker. To read more on using Annotations, see Chapter 41, "Marking and Finding Clips in the Timeline."

TIP: As you work, you may sometimes want to briefly hide or reveal the onscreen controls for a clean, uncluttered look at the image you're tuning. Any set of onscreen controls can be toggled off and on without choosing Off in the menu by pressing Shift-` (tilde).

### Toggling Viewer Overlays On and Off

Hitting Shift-` (Tilde) flips the current Viewer overlay on and off. Commands for showing, hiding, and switching between overlays in the Color page Viewer live in the View > Viewer Overlay submenu. While most of this menu's options sit unassigned by default, you can map them to keys through the Keyboard Customization window.
