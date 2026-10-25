# Zooming and panning into viewers and loading nodes into viewers

Version: DaVinci Resolve 20.3 Reference Manual. Context: Exploring the Fusion interface.
[Chapter index](INDEX.md) / [Previous section](fusion-panels-toolbar-focus-and-viewers.md) / [Next section](fusion-time-ruler-and-transport-controls.md)
<a id="source-clearing-viewers"></a> <a id="source-controls-in-the-viewer-title-bar"></a> <a id="source-loading-nodes-into-viewers"></a> <a id="source-viewer-controls"></a> <a id="source-zooming-and-panning-into-viewers"></a>

### Zooming and Panning into Viewers

A set of conventional techniques exists for zooming into and panning around viewers when you want a tighter look at things. The very same techniques apply to the Node Editor, Spline Editor, and Keyframes Editor. Ways to pan viewers:

- Hold middle-click and drag to move around the viewer.
- Keep Shift and Command held and drag the viewer to pan.
- Drag two fingers across a track pad to pan.

Ways to scale viewers:

- Click a viewer; from there the equals key (=) zooms you in, while the minus key (-) pulls you back out.
- Push the middle and left mouse buttons together and drag left or right to resize the viewer.
- Keep the Command key held and spin your pointer's scroll control to zoom the viewer in and out.
- Keep the middle mouse button held, then click the left mouse button to zoom in or the right button to zoom out. Each step scales by a set amount, centered where the cursor sits.
- Click a viewer and press Command-1 to size the viewer's image to 100 percent.
- Click a viewer and press Command-2 to size the viewer's image to 200 percent.
- Click a viewer and press F to snap the viewer's image back to fit the viewer.
- Click the Scale viewer menu and pick Fit or a percentage.
- Right-click a viewer and pick something from the contextual menu's Scale submenu. That includes a Custom Scale command letting you type your own scale percentage.
- Keep the Command key held while dragging two fingers on a track pad to zoom the viewer in and out.

Ways to spin 3D viewers:

- While in 3D Perspective view, hold the middle and right mouse button, then drag to whirl the stage around.
- While in 3D Perspective view, hold the Shift key and drag two fingers on a track pad to whirl the stage around.

### Loading Nodes Into Viewers

On your first visit to the Fusion page in DaVinci Resolve, viewer 2 typically holds the output of the present empty composition (the MediaOut1 node). In Dual-viewer mode, viewer 1 sits empty until you give a node to one of them. Over in Fusion Studio, neither viewer holds anything until you assign a node to one of them.

To put particular nodes into particular viewers:

- Rest the pointer on a node and click one of the two buttons that surface at its lower left.
- Click once to select a node, then press 1 (for the left viewer) or 2 (for the right viewer).
- Right-click a node and pick View On > None/Left View/Right View from the contextual menu.
- Right-click a node's control header in the Inspector and pick View On > None/Left View/ Right View from the contextual menu.
- Drag a node and let it drop over the viewer you want it in (a real boon for tablet users).

While a node is being viewed, a View Indicator button shows up at its lower left. It's the very control that appears whenever you hover the pointer over a node. Beyond telling you which nodes occupy which viewer, this control also reveals small round buttons for flipping between viewers.

The viewer assignment buttons along the bottom of nodes signal when those nodes are being viewed.

### Clearing Viewers

To wipe an image out of a viewer, click in the viewer so it goes active; a slim red highlight shows along the top of the active viewer. With it active, hit the ` (accent) key, which on U.S. keyboards usually sits just left of the 1 key. The quickest route to clearing every image from every viewer is to ensure no viewer is the active panel and then press the Tilde key. Another option is to select the node currently displayed in the viewer and press that viewer's number once more (1 or 2 as the case may be) to empty it.

### Viewer Controls

A row of buttons and pop-up menus in the viewer's title bar gives you a handful of fast ways to tailor what the viewer shows.

### Controls in the viewer title bar

- Zoom menu: Lets you push in on the viewer's image for a tighter look, or pull back to open up space around the frame's edges for rotoscoping or placing different layers. Pick Fit and the whole image is sized automatically to whatever room the viewer has.
- Split Wipe button and A/B Buffer menu: Using a viewer's A/B buffers, you really can load two nodes into one viewer: pick a buffer from the menu and load a node into the viewer. Switch on the Split Wipe button (press Forward Slash) and a split wipe appears between the two buffers, which you can slide left or right by the handle of the onscreen control, or spin

by dragging anywhere along the dividing line of that onscreen control. Or you can flip between each full-screen buffer to compare them (or to clear a split-screen) by pressing Comma (A buffer) and Period (B buffer).

- SubView type: (Not on offer in 3D viewers.) A click on the icon itself turns the “SubView” option you've picked on or off, while the menu is where you choose which SubView is active. The menu does one of two jobs. With ordinary 2D nodes on display, it opens up SubViews, viewer “accessories” living in a small pane that let you size up images in assorted ways. Among them are an Image Navigator (for getting around when zoomed deep into an image), the Magnifier, the 2D viewer (which gives you a miniature look at the image), plus a 3D Histogram scope, a Color Inspector, a Histogram scope, an Image Info tooltip, a Metadata tooltip, and either a Vectorscope or a Waveform scope. Hitting the Swap option (Shift-V) trades what's in the viewer for what's in the Accessory pane. With 3D nodes on display, this button instead grants you a second mini 3D viewer.
- Node name: Whatever node you're currently viewing has its name shown in the middle of the viewer's title bar.
- ROI controls: A click on the icon itself turns RoI (Region of Interest) limiting in the viewer on or off, while the menu is where you set the RoI's region. RoI marks out the part of the viewer whose pixels genuinely have to be refreshed. As a node renders, it overlaps the current RoI with the current Domain of Definition (DoD) to work out which pixels ought to change. With it on, you can place a rectangle that pens rendering to a small slice of the image, which can give performance a real lift when you're tackling very high resolution or complex compositions. Auto (the default) ties the region to whatever's on screen at the viewer's present zoom/pan level. Pick Set and you draw a custom region inside the frame by dragging a rectangle that starts at the viewer's size and resizes by dragging the corners or sides of the onscreen control. Pick Lock and the current RoI is frozen against changes. Pick Reset and the RoI snaps back to the whole viewer.
- Color controls: Lets you decide which color and/or image channels the viewer shows. A click on the icon itself flips between Color (RGB) and Alpha, the two things you most often want to see (pressing C or A flips between Color and Alpha as well). Open the menu and it lists every channel the node you're viewing can display, commonly RGB, Red, Green, Blue, and Alpha (reachable from the keyboard with R, G, B, or A). With certain media and nodes, further auxiliary channels can be viewed too, such as Z-depth, Object ID, Material ID, XYZ Normals, and the like.
- Viewer LUT: A click on the icon itself flips LUT (LookUp Table) display on or off, while the menu lets you pick which of the many available color space conversions to put on the viewer. The top entries offer Fusion controls you can customize through the Edit item at this menu's top. The rest of the menu lists all LUTs installed in the LUT directory for use in viewing.

By default in DaVinci Resolve, the Fusion page viewers present the image before any grading happens on the Color page, because the Fusion page sits ahead of the Color page in the DaVinci Resolve image processing pipeline. When your clips have been converted to linear color space for compositing, you'll want to composite and adjust the image against a normalized version that looks close to the eventual final. Switching on the LUT display lets you do exactly that as a preview, without baking color adjustments permanently into the image.

- Option menu: Inside this menu live assorted settings governing Fusion's viewers.

Snap to Pixel: As you draw or tweak a polyline mask or spline, the control points lock onto pixel positions. Show Controls: Flips on or off whatever onscreen controls belong to the node you've got selected. Region: Holds all the settings for the viewer's Region of Interest.

Smooth Resize: This setting applies a gentler bilinear interpolated resizing approach as you zoom into a viewer's image; without it, scaling falls back on the nearest neighbor method and shows obvious aliasing artifacts. The nearest neighbor approach, though, proves handier for zooming to the pixel level, since nothing gets interpolated. Show Square Pixels: Steps over the automatic aspect correction when you work with formats whose pixels aren't square. Checker Underlay: Flips on a checkerboard underlay that makes transparent areas easy to spot. Normalized Color Range: Lets you see brightness values lying beyond the usual viewing range, which is especially handy with floating-point images or auxiliary channels. Gain/Gamma: Brings out a plain pair of Gain and Gamma sliders for adjusting the viewer's brightness. 360 View: Serves to correctly show spherical imagery across a range of formats you pick from this submenu. Stereo: Serves to correctly show stereoscopic imagery across a range of formats you pick from this submenu.
