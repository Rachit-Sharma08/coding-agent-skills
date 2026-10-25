# Viewer overview and single vs dual viewers

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using viewers.
[Chapter index](INDEX.md) / [Next section](viewer-divider-bar-and-zooming-and-panning-into-viewers.md)
<a id="source-clean-feed"></a> <a id="source-clearing-viewers"></a> <a id="source-floating-viewers-in-fusion-studio"></a> <a id="source-loading-nodes-into-viewers"></a> <a id="source-position-and-layout"></a> <a id="source-single-vs-dual-viewers"></a> <a id="source-the-singledual-viewer-toggle-button"></a> <a id="source-the-viewer-divider"></a> <a id="source-using-viewers"></a> <a id="source-using-viewers-part-1"></a> <a id="source-video-output"></a> <a id="source-viewer-overview"></a>

### Using Viewers

This chapter walks through how you work with viewers in Fusion: putting onscreen controls and toolbars to use, building groups and subviews, handling viewer Lookup Tables (LUTs), operating the 3D viewer, and configuring viewer preferences along with options.

### Viewer Overview

Fusion's viewers present the current frame of the current composition in numerous ways, helping you watch your progress and judge the end result of your compositing craft. While viewers present 2D images, they're equally able to present a 3D environment by way of a 3D View, along with a dedicated Quad viewer that helps you work in three dimensions to good effect.

Side-by-side dual viewers, a 3D viewer at left and a 2D viewer at right On top of that, you can surface "subviews" such as color inspectors, magnifiers, waveforms, histograms, and vectorscopes, all to help you study the image as you work.

Viewer carrying a 3D Histogram subview up in its top-left corner

### Single vs. Dual Viewers

Out of the box, a pair of viewers sit side by side along the top of the window. That said, the Single/Dual Viewer button flips you between showing one viewer or showing two viewers laid out side by side.

### The Single/Dual Viewer toggle button

### Floating Viewers in Fusion Studio

On top of the dual views above the Node Editor, Fusion Studio lets you call up any number of floating viewers. These floating viewers work wonderfully for getting the most out of a dual monitor setup. You can also switch floating viewers into full-screen mode to squeeze the most from your screen real estate. To spawn a fresh floating display view, pick Window > New View from the menu bar atop the screen. Should you need it, the new view's position and configuration can be stored in the layout preferences.

### Video Output

In DaVinci Resolve or Fusion Studio, where Blackmagic video hardware sits in the machine, you can pick a node to preview straight on that display. Video output won't let you work onscreen controls like center crosshairs or spline control points, yet it proves invaluable for judging your composition through the output format and for gauging image accuracy on a properly calibrated display. You configure the video hardware from the DaVinci Resolve and Fusion Studio preferences.

### Clean Feed

Running DaVinci Resolve across dual computer monitors, you can throw a full-screen viewer onto the secondary monitor from the Fusion page. That puts a third view indicator button beneath every node, governing what shows up on the second display. To switch this monitor on, confirm Dual Screen is off beneath the Workspace menu, then choose Workspace > Video Clean Feed and, from the submenu, point it at your second computer display.

### Loading Nodes into Viewers

When you first launch each application, the Fusion page in DaVinci Resolve and the one in Fusion Studio present different things. Opening the Fusion page for the first time, you'll usually see the output of the current empty composition (the MediaOut1 node) showing in viewer 2. While in dual-viewer mode, viewer 1 stays empty until you hand a node to one of them. Over in Fusion Studio, since no nodes exist as you start a fresh comp, the viewers show nothing. To load specific nodes into specific viewers, do one of the following:

- Hover the pointer over a node, then click one of the two buttons that surface at the node's bottom-left.
- Click once to select a node, then press 1 (for the left viewer) or 2 (for the right viewer).
- Right-click a node and pick View On > None/Left View/Right View out of the contextual menu.
- Right-click a node's control header in the Inspector, then pick View On > None/Left View/ Right View out of the contextual menu.
- Drag a node and drop it onto whichever viewer you want it loaded into (tablet users will love this one).

While a node is on view, a View Indicator button shows up at its bottom left. It's the very same control that appears when you hover the pointer over a node. Beyond telling you which nodes sit in which viewer, these controls also surface tiny round buttons for switching which viewer a node lands in.

Viewer assignment buttons at a node's bottom left flag when it's on view, and whichever dot lights up tells you which viewer holds that node.

### Clearing Viewers

To wipe an image out of a viewer, click inside the viewer to make it active; a light purple outline frames the active panel. With that viewer active, press the ` (accent) key. On U.S. keyboards you'll usually find this key just left of the 1 key. The quickest route to clearing every image from every viewer is to see that none of the viewers is the active panel, then press the accent key.

### Position and Layout

Over in Fusion Studio, whenever you resize and rework a composition's viewer layout, that arrangement always saves alongside the composition. So every time you reopen the composition, its size and layout come back. To stop this from happening, switch off the Recall Layout checkbox in the Fusion Global Layout preferences. Should you want every new composition to open with a given viewer layout, set up the layout of the two primary viewers, then hit the Grab Document Layout button in the Fusion Global Layout preferences to lock that layout in for any new compositions. To preserve the position and size of floating viewers, you reach for the Grab Program Layout button. And lastly, to have the floating viewers open by themselves whenever you launch Fusion, switch on the Create Floating Views checkbox.

### The Viewer Divider

You can shift the relative sizes of the left and right viewers by way of the horizontal viewer divider running between them. Drag the viewer divider to grow or shrink how much room one viewer takes. Its neighbor adjusts to make room for the new layout. To set how much vertical room both viewers get, drag the horizontal scrollbar sitting between the viewers and the work area beneath them.
