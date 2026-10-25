# Viewer settings and LUT curves

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using viewers.
[Chapter index](INDEX.md) / [Previous section](fuse-luts-and-viewer-luts.md)
<a id="source-locking-the-viewer-command-l"></a> <a id="source-lut-files"></a> <a id="source-settings-and-macros"></a> <a id="source-the-viewer-options-menu"></a> <a id="source-using-lut-curves"></a> <a id="source-using-viewer-settings"></a> <a id="source-viewer-preferences-and-settings"></a> <a id="source-viewer-settings"></a>

### Using Viewer Settings

After you've altered a LUT, picking Settings > Save New out of the viewer's contextual menu will store the whole of the viewer's settings, every LUT curve and gain/gamma value included. You can store these under various names, and each settings file can be reloaded whenever you like by picking Settings > filename out of the viewer's contextual menu. Picking Save Default off that same menu will turn these settings into the standard for every new comp.

### Using LUT Curves

The Viewer LUT Edit dialog serves to import and export LUT curves. You can export the LUT curves in either ASCII or Saved format. The ASCII (.alut) file format comes in handy for passing LUT curves to other software, whereas the Saved (.lut) file format gets the nod for Fusion, since it stays more compact, accurate, and amenable to later tweaking. So as to export a LUT, work through these: 1 Click the viewer LUT button so it switches on. 2 Click the viewer LUT menu, then pick Edit. 3 Right-click on the LUT Curve Editor, then pick Export LUT. 4 Pick a LUT format down at the bottom of the file browser window. 5 Type in a name for the LUT, then click Save. Via the Import LUT option, LUT files get loaded back into the Curve Editor; or else, after the file has landed inside Fusion's LUTs folder, it surfaces within the LUT drop-down menu list. TIP: That makes one route for moving LUTs between viewers, or back and forth with the Color Curves node, or with whatever other LUT Editor sits inside Fusion.

### LUT Files

Whatever supported LUT files sit in the LUTs folder can be used by picking them either off the LUT dropdown menu or the viewer's contextual menu. This covers 1D and 3D LUTs like Fusion's .lut, .alut and .alut3 formats, plus .cube, .shlut, .look, .3dl, and .itx formats. That makes a handy route to reach standard format LUT files across different projects.

### Settings and Macros

Because LUTs amount to a form of color correction, you can on top of that press any node, macro, or cluster of nodes into service as a viewer LUT. So as to press a node, group, or macro into use as a viewer LUT, work through these: 1 Pick the node, group, or macro. 2 Right-click over the chosen node, then pick Settings > Save As off the menu. 3 Inside the file browser, navigate over to the LUTs folder named under Preferences > Global > Path Map > LUTS. 4 Hit Save so the .settings file gets stored. That lets nearly any blend of nodes serve as a viewer LUT. While this is the most flexible route, it's also potentially the slowest. Those LUT nodes have to render solely on the CPU, whereas other approaches are GPU-accelerated. Setting a Default LUT The default LUT that goes on once a new composition gets made can be assigned within the Viewer panel of the Fusion Settings window. Ticking the Enable Display LUT checkbox lets you pick a LUT out of the Display LUT plugins list.

The default LUT settings sitting within the View panel of the Fusion Settings window

### Viewer Preferences and Settings

Each viewer's default settings can be changed via the Viewer panel within the Preferences. The position plus size of every floating viewer can additionally be stored via the Layout menu within the Preferences.

### Viewer Settings

Frequently it's preferable to flip between wholly different viewer configurations as you work. For instance, while keying, the image might sit in the main viewer with the alpha channel in a subview. Toward a project's close, viewer settings may take in the histogram, vectorscope, and waveform, plus the image in a view set to Quad view. Fusion gives you a fast way to load and store viewer settings, trimming the work involved in swapping between one layout and the next. So as to store a viewer setting, proceed thus: 1 Over the viewer you'd like to keep, right-click. 2 From the contextual menu, pick Setting > Save New. 3 Type a name for the settings, then click Save. So as to load a viewer setting, proceed thus: 1 Over the viewer you'd like to load a setting into, right-click. 2 From the contextual menu, pick Settings > filename. Loading and Saving Defaults for a Viewer: the viewer is able to keep fresh defaults and be reverted to its defaults using the Load Defaults plus the Save Defaults options that sit in the Settings portion of the View contextual menu.

### The Viewer Options Menu

The viewer's Options menu holds several ways you can tailor the viewer's look and behavior. Many of these options live in the viewer contextual menu too. Show Controls Whenever onscreen controls aren't needed or are obstructing your view of the image, you can briefly hide them via the Show Controls option. This option toggles using Command-K. Checker Underlay The Checker Underlay puts a checkerboard underneath transparent pixels to make spotting transparent areas easier. This is the default option for 2D viewers. Turning this option off swaps the checkerboard for black. Show Pixel Grid Switching this option on will display a faint black grid tracing the precise pixel boundaries within the image once the image gets scaled past a certain threshold. The default is Off.

Smooth Resize The Smooth Resize option applies a smoother bilinear interpolated resizing method as you zoom into an image inside the viewer. With Smooth Resize switched off, scaling falls back on the nearest neighbor method and reveals obvious aliasing artifacts but proves more helpful for seeing the actual pixels of the viewed image once you zoom all the way down to a pixel level, since no interpolation occurs. This option is switched on by default and toggles by clicking the SmR button within the viewer toolbar. Show Square Pixels Hinging on the frame format preferences and the kind of footage loaded, many images may carry pixels that are rectangular rather than square. The NTSC and PAL video standards alike, plus certain anamorphic film formats, rely on rectangular pixels. A computer monitor relies on perfectly square pixels. To make up for this, aspect correction runs automatically while you view non-square pixels. That keeps non-square pixel images from looking squashed or stretched within the viewer. You can switch on the Show Square Pixels option to trump the aspect correction. Show Square Pixels likewise toggles on and off via the 1:1 button within the viewer toolbar. Gain/Gamma Surfaces or conceals a plain pair of Gain and Gamma sliders that let you tune the viewed image. Particularly handy for “gamma slamming” a composite so you can gauge how well it holds together under a spread of differing gamma values. The default leaves things unchanged. 360° View Configures the Fusion page viewer so spherical imagery shows correctly across a spread of formats you pick out of this submenu. Disable flips 360 viewing on or off, whereas the Auto, LatLong, Vert Cross, Horiz Cross, Vert Strip, and Horiz Strip choices let you render the various formats of 360º video properly.

### Locking the Viewer (Command-L)

You can lock a viewer so it won't update. The node loaded into that viewer keeps processing and the fresh image gets queued for display within the viewer, but until you unlock it, the viewer holds still. By default, the viewer sits unlocked.
