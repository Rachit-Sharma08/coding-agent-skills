# Compound motion paths using path centers and two motion paths working together

Version: DaVinci Resolve 20.3 Reference Manual. Context: Animating with motion paths.
[Chapter index](INDEX.md) / [Previous section](spline-motion-path-and-displacement-curve.md) / [Next section](recording-motion-paths.md)
<a id="source-compound-motion-paths-using-path-centers"></a> <a id="source-copying-and-pasting-motion-paths"></a> <a id="source-removing-motion-paths"></a> <a id="source-two-motion-paths-working-together"></a>

### Compound Motion Paths Using Path Centers

Each motion path owns a set center marked by a crosshair. Path centers let paths hook onto other controls and act hierarchically, which is a remarkably potent way to build intricate motion out of fairly simple paths. A handy illustration of the technique would be animating a bee’s flight path. A bee will often trace a steady figure eight even as it presses forward. The straightforward way to pull that off uses two paths in tandem. In the example that follows, the bee would tie to a first path inside a Transform node — a figure eight of the bee moving on the spot. The center of that first path would then tie, through a second Transform node, to another path describing the bee’s forward travel across the scene. To make a compound motion path: 1 Build a figure-eight motion path either by keyframing an object or by drawing a polyline mask. (With a polygon mask, you’ll have to strip off the auto-keyframing and publish the mask before the next step.) 2 Add a polyline mask and trace a smooth curve spline that runs across the screen. 3 At the bottom of the Inspector, right-click the “Right-click here for shape animation” label and pick Remove Polygon Polyline to clear the auto-animation behavior. 4 Right-click the label once more and pick Publish. 5 Pick the object’s Transform node and click the Modifiers tab.

6 Right-click over the Path1 Center X/Y parameter and pick Path. 7 Down at the bottom of Path2, pick Connect To > Polygon: Polyline. 8 Keyframe the Path2 Displacement so the object travels along the second path.

### Two motion paths working together

### Copying and Pasting Motion Paths

An entire motion path can be copied to the clipboard and then dropped onto a different node, path, or composition. Ways to copy and paste motion paths:

- To copy a motion path: Over in the Inspector’s Modifiers tab, right-click the path’s control header and pick Copy from the contextual menu.
- To cut a motion path away from a node: Inside the Inspector, bring up the contextual menu on the path’s control header and pick Cut.
- To paste the copied path over a different path: In the Inspector, right-click the path’s control header and pick Paste from the contextual menu.

As you paste a path, the clipboard’s version writes over the old motion path.

### Removing Motion Paths

Several routes lead to removing or deleting a path, each one running through a right-click contextual menu. Taking a path modifier away leaves the object and the spline shape intact; it merely strips the animation off the object and the modifier out of the Inspector’s Modifiers tab. To remove a path, do one of these:

- In the Modifiers tab, right-click over the Path1 header and pick Delete from the menu.
- In the Inspector, right-click over the Center XY parameter and pick Remove Path1 from the menu.
- In the viewer, on the center coordinate control belonging to the object you’re animating, right-click and pick Remove Path1 from the submenu under the NameOfObject; Center submenu.
