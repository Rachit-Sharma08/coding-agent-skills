# Lighting and shadows in 3D viewers and transparency in 3D viewers

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using viewers.
[Chapter index](INDEX.md) / [Previous section](display-red-channel-and-display-green-channel.md) / [Next section](viewer-guides-and-frame-format.md)
<a id="source-a-quad-view-of-a-3d-scene"></a> <a id="source-grid"></a> <a id="source-guides"></a> <a id="source-lighting-and-shadows-in-3d-viewers"></a> <a id="source-quad-view"></a> <a id="source-quad-view-layouts"></a> <a id="source-the-guides-submenu-in-the-viewers-contextual-menu"></a> <a id="source-the-normals-viewed-in-a-3d-scene"></a> <a id="source-transparency-in-3d-viewers"></a> <a id="source-using-quad-views-for-2d-scenes"></a> <a id="source-vertex-normals"></a>

### Lighting and Shadows in 3D Viewers

Default lighting is supplied before you place any lights in a 3D scene. This flat, basic lighting lets you make out the shading on objects without having to add and configure lights as you work in the 3D Viewer. Shadows, moreover, are hidden by default. As soon as you begin adding your own lights, you’ll need to change modes to observe what they affect while working.

To see the effects of the default light on the scene:

- Inside the 3D Viewer, right-click and pick 3D Options > Default Lights off the contextual menu. Once you’re set to add your own lighting, you can wire light nodes in assorted ways to a Merge 3D node for the scene at hand. After you connect a light to a Merge 3D node, you must switch the 3D Viewer over to display the new, proper lighting.

To toggle lighting rendering within a 3D scene: inside the 3D Viewer, right-click and pick 3D Options > Lighting off the contextual menu.

A 3D scene lit by default lights (top), and that same scene once lighting is switched on (bottom) TIP: Trying to load a Light node into a viewer on its own yields an empty scene, lit by nothing. To witness the lights’ effects you have to view the Merge 3D node that the light is connected to. As with lights, the default 3D Viewer keeps shadows switched off. To see shadows thrown by the lighting you’ve built, you have to enable them.

To toggle shadows rendering within a 3D scene: inside the 3D Viewer, right-click and pick 3D Options > Shadows off the contextual menu. Switching shadows on also switches lighting on automatically, unless it already was.

A 3D scene with shadows enabled along with the lights

### Transparency in 3D Viewers

Whether image planes and 3D objects hide one another in a scene depends on each object’s X, Y, and Z position coordinates in 3D space. The default scheme for working out which polygons are concealed and which are visible from those coordinates is called Z-buffering. Z-buffering is exceptionally fast, though it isn’t always precise when several transparent layers occupy a scene. Happily, a different option exists for trickier 3D scenes that involve transparency: Sorted. The Sorted approach can run considerably slower in some scenes, but it delivers more accurate results regardless of how many transparency layers the scene contains. The viewer defaults to Z-buffering, yet you can readily switch over if your scene needs the Sorted approach. To choose a Sorted method of 3D compositing:

- Right-click anywhere inside the 3D Viewer and select one of the entries in the contextual menu’s Transparency submenu; Full Sort: Draws each polygon in Z order, giving the most precise transparency result. Quick Sort: Reshuffles the scene’s polygons one after another, back to front, giving a fairly precise transparency result.

### Grid

The 3D Viewer shows a grid that supplies a plane of reference within the 3D scene. By default that grid measures 24 x 24 units, is centered on the origin at (0,0,0), and is divided into large squares of 2 units containing small squares of 0.25 units apiece. You can change these defaults in the 3D View panel of the Fusion Settings window, reachable from the Fusion menu.

To toggle the grid on and off: right-click anywhere inside the 3D Viewer and pick 3D Options > Grid off the contextual menu.

The 3D Viewer’s default grid, its origin sitting at x = 0, y = 0 and z = 0

### Vertex Normals

A normal records which way each vertex of a piece of 3D geometry points, and normals feed into the lighting and texturing calculations for an object. When viewing any sort of 3D geometry — an image plane or a complete FBX mesh alike — a scene’s per-object normals can be displayed. To bring up those normals: right-click anywhere inside the viewer and pick 3D Options > Vertex Normals off the contextual menu.

### The normals viewed in a 3D scene

### Quad View

3D compositing often has you looking at the scene from several vantage points to better manage transformations across three dimensions. You can switch the 3D Viewer between vantage points, but doing it repeatedly grows tedious. Luckily, you can instead turn on a Quad view that carves the viewer into four panes. Those panes can then present four different angles of the scene at once. Toggling the Quad view on or off is done one of these ways:

- Right-click anywhere inside the viewer and pick Views > Quad View off the contextual menu.
- Press Shift-Q.

### A Quad view of a 3D scene

Although a Quad view holds four panes, all of them display the same scene. As you assign views within a Quad view, your options run to the Front, Left, Top, Bottom, and Perspective orthographic views, or the view seen through any camera or spotlight present in the scene. Assigning different views to a Quad view’s panes is done one of these ways:

- Right-click straight on the POV label in the lower-left of whichever pane you’re reassigning, and pick a different camera, light, or Point of View off the contextual menu.

### Quad View Layouts

Quad view layouts come in several arrangements, from four equally sized panels to three small panels along the bottom of one larger panel. To move to a different Quad view layout, do this: 1 Turn on the Quad view. 2 Right-click anywhere inside the viewer and select an entry from the contextual menu’s Views > Quad Layouts submenu.

### Using Quad Views for 2D Scenes

Quad views serve 3D scenes, but they aren’t limited to them — they work with 2D scenes too, where each pane shows a different image channel or subview type. One pane could carry the image while the rest carry the alpha channel, a vectorscope, and a histogram. To hand different channels or subviews to the panes of a Quad view set up for a 2D scene: 1 In a viewer, right-click and pick Views > Quad View. 2 Click once inside the pane you’re reassigning. 3 Then do one of these: a) Pick a channel off the Channel Viewer menu. b) Right-click in the viewer, pick Views, and then pick a Subview from the submenu.

### Guides

Guides are onscreen overlays that help you arrange elements within a boundary or along the central vertical and horizontal axes. Displayed in the viewer, they are not rendered into the scene itself. Four guides see common use and can be shown: Monitor Safety, Safe Title, Center, and Film.

### The Guides submenu in the viewer’s contextual menu

Methods of using guides:

- To display guides in a viewer: right-click in the viewer, then pick Guides > Show Guides off the contextual menu, or press Command-G.
- To alter the aspect ratio of the guides on screen: right-click in the viewer, then pick an entry from the Guides > Frame Aspect submenu. Frame aspect usually sits at Default, which locks the frame aspect to the resolution of the image being shown. Set it to a particular value, though, and the guides snap to the precise edges of the chosen format, with any image area beyond that rendered dark gray.
- To show or hide specific guides: right-click in the viewer, then pick an entry from the Guides submenu. A selection of specific guides is on offer, each able to be turned on or off on its own.

Monitor Safety: Monitor Safety marks the safe action region that most monitors and TV screens can display. Safe Title: Safe Title marks the safe zone for titles across all TV and monitor screens. Center: Center draws a crosshair at the center point along with the view’s x- and y-axis. Film: Certain frame formats arrive with film guides already preset, while others need customizing. You can customize the film guides in the Preferences > Frame Format window.
