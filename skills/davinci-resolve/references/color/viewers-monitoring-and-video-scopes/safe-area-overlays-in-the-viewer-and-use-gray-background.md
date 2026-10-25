# Safe area overlays in the viewer and use gray background

Version: DaVinci Resolve 20.3 Reference Manual. Context: Viewers monitoring and video scopes.
[Chapter index](INDEX.md) / [Previous section](spacebar-jkl-playback-and-viewer-skimming.md) / [Next section](viewer-reference-wipes-and-timeline-clips.md)
<a id="source-comparing-clips-in-the-viewer"></a> <a id="source-copying-grades-from-stills-in-the-gallery"></a> <a id="source-hover-scrub-in-the-gallery"></a> <a id="source-monitor-calibration"></a> <a id="source-safe-area-overlays-in-the-viewer"></a> <a id="source-saving-and-wiping-stills-in-the-gallery-and-timeline"></a> <a id="source-the-different-wipe-customization-modes"></a> <a id="source-use-gray-background"></a> <a id="source-viewing-broadcast-safe-exceptions"></a>

### Safe Area Overlays in the Viewer

A set of safe area overlays can be shown or hidden within the Viewer. Every safe area overlay option lives in the View > Safe Area menu. Each one can be turned on or off on its own from that menu.

Viewer displaying extents, center, safe, action and title area overlays On/Off: Toggles all the currently selected safe area marker options on or off together. Extents: A boundary showing the precise outer edge of the frame. Particularly handy when the safe markers use an aspect ratio other than the one the Viewer is currently set to. Action: A boundary marking out the frame's outer 90% action safe area. Title: A boundary marking out the frame's outer 80% title safe area. Center: A crosshairs pinpointing where the frame centers. Aspect: Turns on the View > Select Aspect Ratio submenu so you can alter the aspect ratio of the safe area markers. The aspect ratios you can pick among are: 1.33 (a.k.a. 4:3), 1.66, 1.77 (a.k.a. 16:9), 1.85, and 2.35.

### Use Gray Background

Ticking the “Use gray background in viewers” box within the User Preference's UI Settings turns the Viewer's empty area (where there is any) a lighter gray, which makes it easier to tell which parts of the Viewer are black due to blanking from those that are merely empty because of how the image is zoomed or panned.

### Monitor Calibration

Those who calibrate displays with Light Illusion's LightSpace CMS or with SpectraCal's Calman can now press DaVinci Resolve into service as a sync-able pattern generator. That means DaVinci Resolve can put out color patches, synced by LightSpace, to your display over whichever video interface ties into your computer. A monitor probe — itself driven by LightSpace — reads these synchronized color patches, stores the probe data, and weighs it against the original color values of the output color values to characterize that display. To use the feature, you must first hold a licensed copy of LightSpace CMS, a Windows application. Syncing depends on a wired or wireless LAN being on hand so the LightSpace application can talk to DaVinci Resolve. To sync LightSpace CMS with DaVinci Resolve so it acts as a pattern generator client: 1 Launch LightSpace on whichever Windows computer hosts it. 2 With LightSpace open, click the Network Manager button. A window opens listing the two network IP addresses that LightSpace uses. Jot them down, then click the Enable button.

The Network Manager dialog in LightSpace CMS 3 Within DaVinci Resolve, pick Workspace > Monitor Calibration > LightSpace. 4 After the LightSpace dialog appears, enter the latter of those two network IP addresses LightSpace shows into the Remote Machine field, and verify that the Port number agrees. Next, click the Connect button.

The Calibration dialog in DaVinci Resolve, connected to LightSpace CMS via WiFi When all is working, the LightSpace dialog in DaVinci Resolve should display the word “Connected,” and the Network Manager dialog in LightSpace should report that there is 1 available client/s. You can then dismiss the Network Manager dialog in LightSpace and follow the steps laid out in the LightSpace CMS documentation for characterizing your display and for building and exporting a display LUT (in the .cube format) you can use as a display LUT in DaVinci Resolve. As an alternative, a display LUT exported from LightSpace can instead be loaded onto an external video processing device. 5 Once finished, hit Disconnect inside the LightSpace dialog, then hit Cancel to dismiss the window.

### Viewing Broadcast Safe Exceptions

Choosing View > Display Broadcast Safe Exceptions makes the Color page Viewer show a false-color overlay that flags in blue the parts of the picture breaching the currently selected broadcast safe level set in the Color Management panel of the Project Settings.

Areas of the image that violate broadcast safe are highlighted in blue To read further about how broadcast safe limiting works from the Project Settings' Color Management panel, consult Chapter 127, “Automated Grading Commands and Imported Grades.”

### Comparing Clips in the Viewer

Being able to weigh one clip against another is a core part of color correction work. DaVinci Resolve gives you three distinct ways to do it. The Gallery can show two clips side by side for split screen comparison. You can also draw on different reference modes to bring a timeline clip or reference movie straight into a split screen comparison. Lastly, the Split Screen controls let you lay out multi-frame arrangements within the Viewer.

### Saving and Wiping Stills in the Gallery and Timeline

The Gallery on the Color page gives quick reach to stills you've saved off the various clips in the Timeline. While the dedicated Gallery page offers a fuller interface for browsing presaved “looks” and for importing stills out of other projects, you can save, organize, and browse stills right inside the Gallery of the Color page. Stills get saved in the DPX file format. After you've saved one or more stills, you can arrange split screen wipes in the Viewer, which mirror across to your external display.

Holding a Gallery still up against the current shot eases the job of matching grades What follows is a condensed rundown of still store and split screen behavior to get you up and running fast. To save a still, do one of these:

- Choose Color > Stills > Grab Still (Option-Command-G).
- Right-click on the Viewer and choose Grab Still.

To wipe a still, do one of these:

- Pick a still in the Gallery, then on the top Viewer toolbar click the Image Wipe button.
- Choose Color > Stills > Play Still (Command-W); alternatively, right-click within the Viewer and pick Toggle Wipe.
- Double-click a still in the Gallery.

To adjust a wipe in the Viewer, do one of these:

- Drag the pointer within the Viewer to move the wipe.

### The different wipe customization modes

To customize a wipe in the Viewer: On the Viewer toolbar, click any of the Wipe mode buttons. The modes available are: Horizontal: Lets you set the wipe's two halves on either side of a vertical border. Dragging the pointer shifts the wipe border left and right. Vertical: Lets you set the wipe's two halves above and below a horizontal border. Dragging the pointer shifts the wipe border up and down. Diagonal: Lets you set the wipe's two halves across an adjustable diagonal border. Dragging the pointer moves the wipe to the left and right. Hold the Option key and drag, circling the pointer around, to spin the wipe's border to whatever angle you like. Mix: Lets you blend the two images together for comparison. As you drag the pointer, the fade balance between one image and the other shifts. Alpha: Lets you employ a qualifier to set transparency within the current clip's image while weighing it against a Gallery still acting as the backdrop. Drop a node onto the grade and let the qualifier key a particular color you want turned transparent (the green of a green screen, say). Then route that node's KEY output to the Alpha Output that turns up in the Node Editor. The portion of the foreground image the key isolates becomes transparent, so the Gallery still behind shows through. This can help when previewing how the lighting or grade of a foreground VFX plate reads once the image is composited over a particular background image held in the Gallery. Difference (A/B): Lets you see only the pixels that shift because of an operation on the node. For instance, if you pick this highlight and tweak the gain, only the pixels the gain altered would appear in the Viewer. Box: Lets you present the current clip as a picture-in-picture overlay sitting on the still behind. Dragging the pointer resizes the crop box around the edge of the reference image. Venetian Blind: Lets you weigh the two wiped images via alternating horizontal strips. Drag the pointer up or down to resize the alternating strips. Good for quickly checking vertical color uniformity, zeroing in on color and contrast shifts from top to bottom. Checkerboard: Lets you weigh the two wiped images via an alternating checkerboard. Drag the mouse left or right to flip between images by squeezing each check horizontally. Good for checking color uniformity across the width and height of two images.

Within the Viewer's option menu, pick one of these out of the Wipe Style submenu. Wipe Style: Steps through these modes in turn — Horizontal, Vertical, Diagonal, Mix, Alpha, Difference, Box, Venetian Blind, and Checkerboard. Invert Wipe: Swaps each half of the wipe (Option-W).

### Hover Scrub in the Gallery

When Live Preview is turned on in the Gallery option menu, the Hover Scrub Preview submenu lets you decide how Live Preview appears via a thumbnail in the Gallery and in the Viewer while your pointer hovers above a still, or above a LUT within the LUT Browser:

- You can opt to scrub both the thumbnail under your pointer and the Viewer, so you preview the current still's grade or a LUT over the span of the current clip in both the thumbnail and Viewer.
- You can opt to scrub the thumbnail alone, leaving the Viewer to display only the grade or LUT over the frame where the playhead sits.
- You can switch off scrubbing entirely, in which case both the thumbnail and the Viewer show only the grade or LUT over the frame at the playhead's position.

### Copying Grades from Stills in the Gallery

Stills also carry the grade of the clip they came from, so they can serve to copy grades between clips or to bank grades you may want later. To copy a grade off a still onto a clip, do one of these:

- With one or more Timeline clips selected, right-click a Gallery still and pick Apply Grade.
- With one or more Timeline clips selected, middle-click a Gallery still.

When you copy a still this way, the saved grade fully replaces the grade in the target clip, unless you've engaged the “Preserve number of nodes” option found in the Gallery's contextual menu. For fuller guidance on working with the Gallery — including ways to organize the Gallery browser, instructions for Albums, Power Grades, and Memories, plus other methods of copying grades and handling advanced grade management — see Chapter 141, “Using the Gallery.” and see Chapter 142, “Grade Management.”
