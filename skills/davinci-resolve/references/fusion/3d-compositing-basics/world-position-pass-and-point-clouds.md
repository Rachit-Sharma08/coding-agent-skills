# World position pass and point clouds

Version: DaVinci Resolve 20.3 Reference Manual. Context: 3D compositing basics.
[Chapter index](INDEX.md) / [Previous section](fbx-exporter-and-text3d.md)
<a id="source-finding-naming-and-publishing-points"></a> <a id="source-point-cloud-in-the-viewer"></a> <a id="source-point-clouds"></a> <a id="source-publishing-a-point"></a> <a id="source-publishing-a-point-using-the-viewer-contextual-menu"></a> <a id="source-renaming-a-point-in-the-cloud"></a> <a id="source-world-position-pass"></a>

### World Position Pass

The World Position Pass — WPP for short — is a render pass that comes out of 3D applications. Every pixel gets the XYZ position in world coordinates of the spot where it was generated. So when the face a pixel came from sits at (0,0,0) in the scene, that pixel ends up with a Position value of (0,0,0). Picture that as RGB and the pixel reads black. Place a face at (1,0,0) within the original scene and the RGB pixel it yields reads red. Given the vast spread of possible positions across a typical 3D scene — with 7⁄8 of those holding negative coordinates — the Position channel always renders in 32-bit float.

A World Position Pass render of a scene whose center sits at (0,0,0); the real image is up in the top left 3D Scene Input Nodes drawing on the World Position channel live under the Position category. VolumeFog and Z to WorldPos call for a camera input that matches the camera which rendered the Position channels, which may be either a Camera3D or a 3D scene that holds a camera. As in the Renderer3D, you get to pick which camera to use when several are in the scene. The VolumeFog can render with no camera input from the Node Editor as long as its world space Camera Position inputs hold the right value. VolumeMask takes no camera input. The nodes that support the World Position Pass, found under the Position category, each provide a Scene input, which may be either a 3D Camera or a 3D scene containing a camera. Three Position nodes can make use of World Position Pass data.

- Nodes > Position > Volume Fog
- Nodes > Position > Volume Mask
- Nodes > Position > Z to World
- The “Dark Box”

Across empty stretches of the render, the Position channel comes up wrongly initialized to (0,0,0). To recover proper Position data, drop a bounding sphere or box into your scene so it supplies distant values and lets the Position nodes render as they should.

Lacking a bounding mesh to produce Position values, the fog wrongly fills the background

### Point Clouds

The Point Cloud node is built to handle locator clouds that come out of 3D tracking software. 3D camera tracking tools, SynthEyes and PF Track among them, frequently spit out hundreds or even thousands of tracking points. Viewing those points in the scene and reading their place in 3D and screen space matters for aligning live action with CG, yet pulling each one in as a separate Locator3D would tank performance and crowd the node tree.

### Point cloud in the viewer

The Point Cloud node can pull in point clouds saved into scene files by match moving or 3D scanning software. Importing a point cloud goes like this: 1 Drop the PointCloud3D node into your composition. 2 In the Control panel, click the Import Point Cloud button. 3 Navigate to the scene file and choose one of its clouds to bring in. The whole point cloud arrives as a single object, which is a markedly faster route.

### Finding, Naming, and Publishing Points

A lot of 3D trackers let you name individual tracking points and place tracking points on features of interest. The Point Cloud 3D locates those points fast and publishes them. Once published, a point in the cloud can drive the animation of other parameters.

Locating a point inside the point cloud goes like this: 1 Right-click somewhere within a viewer. 2 Pick Find from the Point Cloud’s submenu in the contextual menu. 3 Enter the point’s name and click OK.

Finding a point cloud using the viewer contextual menu Should a point matching the name you typed turn up, it gets selected in the point cloud and lit yellow. TIP: The Point Cloud Find function searches with case sensitivity. A point called “tracker15” won’t turn up when you search for “Tracker15”.

### Renaming a Point in the Cloud

The Point Cloud contextual menu lets you rename a point you’ve selected. It applies to one point only. You can’t rename a group of points at once.

### Publishing a Point

When you want a point’s XYZ positions available to wire to other controls in the scene, publish the point. That’s handy for tying objects to how a single tracker moves. To publish a point, right-click it and pick Publish from the contextual menu.

### Publishing a point using the viewer contextual menu
