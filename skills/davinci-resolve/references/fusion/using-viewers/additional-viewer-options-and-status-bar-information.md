# Additional viewer options and status bar information

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using viewers.
[Chapter index](INDEX.md)
<a id="source-additional-viewer-options"></a> <a id="source-status-bar-information"></a> <a id="source-using-viewers-part-4"></a>

### Additional Viewer Options

Right-clicking inside any viewer exposes a few more commands through the plainly titled Options submenu. Alpha Overlay With this turned on, the viewer paints the alpha channel over the top of the color channels. Seeing this can make it easier to judge exactly where one layer ends and the next starts inside a composite. By default it stays off. Overlay Color The white tint is what the overlaid alpha region uses out of the box once the alpha overlay is active. Depending on how the picture is colored, white sometimes blends in too much to read well. To fix that, pick a different shade from the available Overlay Color choices. Follow Active Switch on Follow Active and the viewer keeps showing whichever node is currently active over in the Node Editor. It ships off, which lets you inspect one node here while steering a separate one from the Control Panel. Show Controls Whenever the onscreen handles aren't needed or are obscuring your read on the image, the Show Controls option lets you briefly tuck them away. Pressing Command-K flips this on and off. Show Full Color Range With floating-point images you'll now and then want a look at values sitting beyond the usual luminance span. Clicking the toolbar button for Show Full Color Range will normalize whatever picture the viewer is currently presenting. After normalization the brightest pixel in any channel lands at 1.0 (white) while the darkest drops to 0.0 (black), and everything in between is rescaled to sit inside that span. The same trick helps with Z-buffer and similar auxiliary channels, since those frequently carry value ranges nothing like the color channels do. Show Labels Use the Show Labels option to switch the accompanying caption text on or off for onscreen controls, all without shutting down whatever functions those overlays drive and without removing the controls from view.

### Status Bar Information

Running along the lower edge of the Fusion window, the status bar reports precise RGBA and Z readings for whatever pixel the pointer sits over while it hovers inside a viewer. It additionally shows the cursor's X and Y coordinates together with the precise pixel position.

The status bar showing coordinates and color information
