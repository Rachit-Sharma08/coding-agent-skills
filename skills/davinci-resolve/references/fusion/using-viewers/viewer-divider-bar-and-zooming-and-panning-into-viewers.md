# Viewer divider bar and zooming and panning into viewers

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using viewers.
[Chapter index](INDEX.md) / [Previous section](viewer-overview-and-single-vs-dual-viewers.md) / [Next section](playing-flipbook-previews-and-removing-flipbook-previews.md)
<a id="source-a-fusion-viewer-with-show-guides-enabled"></a> <a id="source-creating-flipbook-previews"></a> <a id="source-custom-guides-in-fusion-viewers"></a> <a id="source-flipbook-previews"></a> <a id="source-snapping-to-guide-lines"></a> <a id="source-the-add-guide-dialog"></a> <a id="source-the-viewer-divider-bar"></a> <a id="source-zooming-and-panning-into-viewers"></a>

### The viewer divider bar

### Zooming and Panning into Viewers

There's a standard set of techniques for zooming into and panning around viewers whenever you want a closer look. These same techniques carry over to the Node Editor, Spline Editor, and Keyframes Editor. Methods of panning viewers:

- Middle-click and drag to pan around the viewer.
- Hold down Shift and Command, then drag the viewer to pan.
- Drag two fingers across a track pad to pan.

Methods of scaling viewers:

- Click a viewer, then press the Equals key (=) to zoom in or the Minus key (-) to zoom out.
- Hold the middle and left mouse buttons together, dragging left or right to resize the viewer.
- Hold down the Command key and work your pointer's scroll control to resize the viewer.
- Hold down the Command key and drag two fingers across a track pad to resize the viewer.
- Hold the middle mouse button down, then click the left mouse button to zoom in, or the right button to zoom out. The scaling moves by a fixed amount, centered where the cursor sits.
- Click a viewer, then press Command-1 to size the image in the viewer to 100 percent.
- Click a viewer, then press Command-2 to size the image in the viewer to 200 percent.
- Click a viewer, then press Command-F or Command-1 to snap the image in the viewer back to fit the viewer.
- Click the Scale Viewer menu and pick Fit or a percentage.
- Right-click a viewer and pick an option out of the contextual menu's Scale submenu.

Among these sits a Custom Scale command, which lets you key in a scale percentage of your own Methods of spinning 3D viewers:

- While in 3D Perspective view, hold down both the middle mouse button and the right mouse button, then drag to spin the stage around.

### Custom Guides in Fusion Viewers

The Fusion page viewers let you build custom guides of your own. With them you can fully tailor and lay down specific geographic spots in the frame, then have the image snap to those spots during other operations. You can build Guides, which are colored lines crossing the frame either horizontally or vertically. Guides serve as overlay tools for tuning your video position, and they show up in the viewer alone, never in your final project output.

### A Fusion Viewer with Show Guides enabled

To bring up Guides, right-click in the viewer and pick Guides > Show Guides, or else press Command-G. To Show and Create a Guide Line: 1 Switch on the Guides by right-clicking in the viewer and picking > Guides > On (Command-G). Up comes a default batch of guidelines you can click and drag through the frame. 2 Build a fresh Guide by right-clicking in the viewer and picking Guides > Add Resolve Guide. Adding a Resolve Guide makes the guideline show up on other pages within DaVinci Resolve.

3 Within the Add Guide dialog, pick the position and orientation you'd like the new guide to take, then click OK. Units: Pick either pixel or percentage as the metric governing where the line goes. Position: Key in a value marking where in the frame you want the guideline to cross. Later on you can likewise drag this line about in the viewer, placing it by eye. Orientation: Pick either a horizontal or a vertical orientation for the line.

### The Add Guide dialog

To Modify Delete, or Lock a Guide Line:

- Click and Drag the line wherever you like in the viewer.
- Delete a line by right-clicking it in the viewer and picking Remove Guide.
- Adjust an existing line's position and orientation by right-clicking it in the viewer and picking Edit Guide.
- To guard against accidental movement, lock Guides down by right-clicking the line and picking Lock Guide, or lock every guide together by right-clicking in the viewer and picking Guides > Lock All Resolve Guides.

### Snapping to Guide Lines

Right-click in the viewer and pick Guides > Snap to Guides to switch snapping on. As you move the clip around the frame with the Fusion tools, the image edge snaps to a guideline on its own each time it nears one.

### Flipbook Previews

As your compositions grow more involved, and you find you need to preview particular branches of your node tree to gauge how the various details you're working on are shaping up, it can pay to build targeted RAM previews at assorted quality levels right inside the viewer through a RAM Flipbook. A RAM Flipbook Preview is a preview render that lives wholly within RAM, letting you render a node's output at varying quality levels for fast processing so you can watch a real-time preview.

### Creating Flipbook Previews

Building a Flipbook Preview goes fairly quickly, provided you know where to look.

To create a Flipbook Preview: 1 Pick the node in your node tree you'd like to preview by doing one of the following:

- Hold the Option key down while dragging a node into the viewer.
- Right-click a node and pick an option out of the Create/Play Preview submenu in the

contextual menu. 2 Once the Preview Render dialog opens, pick the quality, resolution, and motion blur settings you'd like the Flipbook Preview to use.

The Flipbook Preview Render dialog 3 With your settings chosen, click Start Render. The Time Ruler's current frame range renders using the settings you picked, and the outcome shows up in whichever viewer you selected or dragged into. After you've built a Flipbook Preview inside a given viewer, a right-click on that viewer surfaces Flipbook-specific commands and options: Play, Loop, or Ping-Pong the Flipbook; throw it Full Screen; Show Frame Numbers; or do away with it. TIP: To build a Flipbook Preview while skipping the Render Settings dialog, relying instead on either the default setting or whatever was last chosen, hold Shift-Option down as you drag a node into the viewer. The Settings dialog stays away, and the preview starts rendering immediately.
