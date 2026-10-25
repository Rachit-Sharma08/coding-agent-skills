# Fusion panels toolbar focus and viewers

Version: DaVinci Resolve 20.3 Reference Manual. Context: Exploring the Fusion interface.
[Chapter index](INDEX.md) / [Next section](fusion-viewer-zoom-pan-and-node-loading.md)
<a id="source-choosing-which-panel-has-focus"></a> <a id="source-exploring-the-fusion-interface"></a> <a id="source-exploring-the-fusion-interface-part-1"></a> <a id="source-interface-toolbar"></a> <a id="source-the-fusion-user-interface"></a> <a id="source-the-fusion-user-interface-shown-completely"></a> <a id="source-the-ui-toolbar-of-fusion-studio"></a> <a id="source-the-ui-toolbar-of-the-fusion-page"></a> <a id="source-the-work-area"></a> <a id="source-viewers"></a>

### Exploring the Fusion Interface

Here you'll get your bearings in the Fusion user interface, taking a brisk walk through which tools you have on hand, where various things live, and how the panels mesh so you can build and polish compositions inside this capable node-based environment.

### The Fusion User Interface

Reveal it all at once and Fusion breaks down into four main regions meant to speed your node-based compositing along. Up top sit the viewer(s), the work area runs along the bottom, the Inspector occupies the right, and the Effects Library is the region over on the left. On DaVinci Resolve's Fusion page, the Effects Library and the Media Pool share that space. Working in concert, all these panels let you layer on effects, paint away problems, build motion graphics or title sequences, or assemble elaborate 3D and multi-layered composites.

### The Fusion user interface shown completely

That said, Fusion needn't be so involved; honestly, you can get along just fine with only the viewer, Node Editor, and Inspector showing for a pared-down setup.

A pared-down arrangement of Fusion controls for day-to-day work

### The Work Area

Odds are the phrase “the work area” won't come up often, since people name the particular panels inside it that they're actually using. Even so, what we call the work area is the zone filling the lower half of the Fusion user interface, the place where you can bring up the three principal panels for assembling compositions and editing animations in Fusion. Those would be the Node Editor, the Keyframes Editor, and the Spline Editor. Out of the box the Node Editor greets you first and is the main space you'll work in, yet it can sit alongside the Spline Editor and Keyframes Editor whenever you need. To hand these three panels more horizontal room on your display, you can drop the Effects Library and Inspector into a half-height mode if it helps.

The work area with the Node Editor, the Spline Editor, and the Keyframes Editor on display

### Interface Toolbar

Across the very top of Fusion runs a toolbar whose buttons reveal and hide the various parts of the user interface (UI). Each labeled button tells you which UI part it shows or hides. On DaVinci Resolve's Fusion page, a right-click anywhere on this toolbar gives you the choice of showing the bar with its text labels or without them.

### The UI toolbar of the Fusion page

### The UI toolbar of Fusion Studio

These buttons are as follows, from left to right:

- Media Pool/Effects Library Full Height: Lets the space taken by the Media Pool (DaVinci Resolve only) and/or Effects Library stretch to your display's full height, handing you more room to browse while squeezing the Node Editor and viewer area narrower. In half-height, the Media Pool/Templates/Effects Library stay penned into the UI's upper half next to the viewers (only one can show at a time), leaving the Node Editor to span your display's whole width.
- Media Pool: (DaVinci Resolve only): Reveals and conceals the Media Pool, out of which you can drag more clips into the Node Editor to put them in your Fusion page composition.
- Effects Library: Brings up or hides the store of every node tool Fusion has on offer. From here a click on a node adds it after whichever node is selected in the Node Editor, or you can drag and drop nodes onto any part of the node tree you please.
- Clips: (DaVinci Resolve only): Brings up and closes the Thumbnail timeline, your means of moving through the program, making and managing several versions of compositions, and resetting the current composition.
- Nodes: Brings up and closes the Node Editor, where the building and editing of your compositions happens.
- Console (Fusion Studio only): The Console is a window showing the error, log, script, and input messages that can shed more light on whatever Fusion is up to. It's also the place to read FusionScript outputs or type FusionScripts in directly.
- Spline: Brings up and closes the Spline Editor, where you shape the curves that interpolate keyframe animations so you can tune and nail their timing. Every keyframed parameter is nested under the effect it belongs to, within a list off to the left.
- Keyframes: Brings up and closes the Keyframes Editor, which renders each clip and effects node in your Fusion composition as its own layer. The Keyframes Editor lets you edit and fine-tune the timing of keyframes laid onto the various effects in your composition. It also lets you shift the relative timing of clips brought into Fusion and trim their In and Out points. A spreadsheet can be revealed or hidden in which you numerically edit keyframe values for the effects you've selected.
- Metadata (DaVinci Resolve only): Conceals or reveals the Metadata Editor, your tool for reading and editing the available clip and project metadata attached to any piece of media inside a composite.
- Inspector: Reveals or conceals the Inspector, which presents every editable parameter and control tied to the nodes you've selected in the Node Editor. You can display the parameters of several nodes together, and even pin the parameters of nodes you want to keep editing so they stay visible even when those nodes aren't selected.
- Inspector Height: Lets you set the Inspector to half height (matching the viewer area) or full height (matching your entire display). Half height frees up more space for the Node Editor, Spline Editor, and/or Keyframes Editor, while full height lets you edit more node parameters at once or holds enough room to show several nodes' parameters together.

### Choosing Which Panel Has Focus

Any time you click somewhere on the Fusion interface with the pointer, or use a keyboard shortcut to “select” a given panel, you grant that panel of the user interface “focus.” A focused panel grabs certain keyboard shortcuts to act within itself rather than somewhere else in the interface. So you can readily tell which panel holds focus, a highlight shows up along the top edge of whichever one it is. In DaVinci Resolve, that highlight only appears once you've enabled “Show focus indicators in the User Interface,” a checkbox living under the User Preferences within its UI Settings panel.

The focus indicator running along the Media Pool's top edge, set beside a viewer that lacks focus

### Viewers

Across the top of the Fusion page the viewer area presents one or two viewers, a count governed by the Viewer button at the far right of the Viewer title bar. Any viewer can show the output of one node drawn from anywhere in the node tree, and you decide which node lands in which viewer. That makes it simple to drop different nodes into each viewer side by side for comparison. You might, for example, put a Keyer node in the left viewer and the final composite in the right, letting you watch the image you're tweaking and the finished result together.

With dual viewers you can edit an upstream node in one while watching how it plays out on the whole composition in the other. As a rule, each viewer renders the 2D nodes of your composition as a single image. When you're looking at a 3D node, though, you get the choice of switching that viewer to one of several 3D views. A perspective view hands you a movable stage on which to lay out the elements of the world you're building. A quad view, on the other hand, shows your composition from four angles, which makes arranging and editing objects and layers along the XYZ axes of your 3D space easier.

Sending a 3D node to a viewer brings up a Perspective view

TIP: While in Perspective view, holding down the middle and right mouse buttons and then dragging in the viewer swings the view around the center of the world. Every other way of navigating viewers behaves just as it normally does. Viewers come with a range of abilities for comparing and assessing images. This section runs through a brief rundown of those viewer abilities to get you going.
