# User interface and view

Version: DaVinci Resolve 20.3 Reference Manual. Context: Preferences.
[Chapter index](INDEX.md) / [Previous section](preferences-overview-and-global-and-composition-preferences.md) / [Next section](auto-tools-and-global-range.md)
<a id="source-3d-view-1"></a> <a id="source-avi"></a> <a id="source-default-animate"></a> <a id="source-default-lights"></a> <a id="source-defaults-1"></a> <a id="source-fit-to-view"></a> <a id="source-grid"></a> <a id="source-import"></a> <a id="source-orthographic-views"></a> <a id="source-perspective-views"></a> <a id="source-preferences-in-depth"></a> <a id="source-the-3d-view-preferences"></a> <a id="source-the-defaults-preferences"></a> <a id="source-user-interface"></a> <a id="source-view"></a> <a id="source-vr-headsets"></a>

### User Interface

These preferences govern how the user interface window looks and how the Inspector is shown. Video Monitoring (Fusion Studio Only) The Video Monitoring preferences are the spot to configure Blackmagic video display hardware so monitoring runs on an HD, Ultra HD, or DCI 4K display.

### View

The View preferences span the viewer settings, reaching the default control colors, the Z-depth channel viewing ranges, default LUTs, the padding applied for fit, zoom, and the rest.

### VR Headsets

The VR Headsets preferences let you configure whatever Virtual Reality headsets are attached, taking in the way stereo and 3D scenes get viewed. Bins (Fusion Studio Only) Three panels make up the Bins preferences: a Security panel for assigning users plus passwords that serve the local bins; a Servers panel for choosing which remote Bin servers connect; and a Settings panel devoted to stamp rendering.

### Import

The Import settings carry options for EDL Import that shape how flows are built from the data in an EDL.

### Preferences In Depth

Each category holds a deep set of controls for tuning Fusion so it fits your working environment better. The preferences span both software and hardware options that touch every newly created comp. The section below explains every option found across the preferences categories.

### 3D View

The 3D View preferences hold settings for assorted defaults in the 3D Viewers, taking in grids, the default ambient light setup, and Stereoscopic views.

### The 3D View preferences

### Grid

The Grid section of the 3D View preferences sets up the way the grid in 3D Viewers is drawn.

- Grid Antialiasing: Certain graphics hardware and drivers cannot handle antialiased grid lines, which causes them to sort incorrectly in the 3D Viewer. Clearing this checkbox switches off antialiasing of the grid lines. To shut the grid off entirely, right-click in a 3D Viewer and choose 3D Options > Grid.
- Size: Raising the Size value adds more grid lines. Fusion does not pin down the units used for the spacing between grid lines. A “unit” is whatever you decide it is.
- Scale: Tuning the overall scaling factor for the grid helps, for instance, when the grid area looks too small next to the size of your geometry.

### Perspective Views

The Perspective Views section governs how the perspective view looks in both a normal and a stereoscopic project.

- Near Plane/Far Plane: These values fix the closest and farthest distance any object may reach toward or away from the camera before it gets clipped. The minimum setting is 0.05. Putting Near Plane too low and Far Plane too far costs you depth precision in the viewer.
- Eye Separation/Convergence/Stereo Mode: This cluster of settings establishes the defaults applied once stereo is switched on in the 3D Viewer.

### Orthographic Views

In a manner that echoes the Perspective Views, the Orthographic Views section — covering the front, top, right, and left views — pins down how near or far an object may travel relative to the viewer before clipping kicks in.

### Fit to View

The Fit to View section has two value fields governing how much empty space surrounds objects in the viewer when the F key is pressed.

- Fit Selection: Fit Selection governs the empty margin left once one or more objects are picked and you press the F key.
- Fit All: Fit All governs the empty margin left when F is pressed with nothing picked.

### Default Lights

These three settings govern the default light setup in the 3D Viewer. The default ambient light comes into play once lighting is switched on and you have added no light to the scene. The directional light travels with the camera, so when the directional light is set to “upper left,” the light seems to arrive from the upper-left side of the image/camera.

### AVI

The AVI preference shows up only in Fusion Studio on Windows. It sets up the default AVI codec settings whenever you pick AVI as the rendering file format in the Saver node.

- Compressor: This drop-down menu lists the AVI codecs your computer offers. Fusion checks each codec as the application starts, so some may be missing if those checks find them unfit for use within Fusion.
- Quality: This slider sets how much compression the codec applies. Higher values yield cleaner images but bigger files. Not every codec honors the Quality setting.
- Key Frame Every X Frames: When ticked, the codec lays down keyframes at the interval you set. Keyframes are not compressed against earlier frames, which makes them faster to seek within the finished movie. Not every codec honors the keyframe setting.
- Limit Data Rate To X KB/Second: When ticked, the rendered file’s data rates are capped at the amount you give. Not every codec honors this option. Enter, in kilobytes (kB) per second, the data rate that caps the AVI, where applicable. This control leaves the file alone unless the Limit Data Rate To option is selected.

### Defaults

What you choose here shapes Fusion’s behavior as fresh tools land in the Node Editor and as parameters get animated.

### The Defaults preferences

### Default Animate

The Default Animate section lets you change which kind of modifier attaches to a parameter once the Animate option is picked from its contextual menu. The default option is Nothing, which reaches for a Bézier spline when animating numeric parameters and turns to a path modifier where positional controls are concerned.

- Number With and Point With: These drop-down lists let you pick a different modifier as the new default. For instance, change the default used to animate position by setting Point with the drop-down menu to XY Path. The choices in this menu come from installed modifiers valid for that parameter type. They take in third-party plug-in modifiers along with the native modifiers that ship with Fusion.
