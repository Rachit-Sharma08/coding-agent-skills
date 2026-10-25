# Filters to delete problem tracks and exporting a 3D scene for efficiency

Version: DaVinci Resolve 20.3 Reference Manual. Context: 3D camera tracking.
[Chapter index](INDEX.md) / [Previous section](how-to-judge-track-accuracy-and-deleting-tracks.md)
<a id="source-exporting-a-3d-scene-for-efficiency"></a> <a id="source-realign-the-scene"></a> <a id="source-setting-the-ground-plane"></a> <a id="source-setting-the-origin"></a> <a id="source-setting-the-scale"></a> <a id="source-unalign-the-3d-scene-transforms"></a> <a id="source-using-filters-to-delete-problem-tracks"></a> <a id="source-viewing-the-exported-results"></a>

### Using Filters to Delete Problem Tracks

The Solve tab carries filters that let you grab groups of comparable tracks according to track length, track error, and solve error. With them you can swiftly isolate and discard underperforming tracks that might throw off the resulting camera, leaving behind a tidy set of dependable tracks.

Filters let you pick tracks, and the Operations On Selected Tracks buttons let you remove them As a rule, for example, it pays to run the solver on tracks of longer duration. Because shorter tracks tend to introduce error when computing the camera, you can strip them out via the Filter section in the Inspector. Raising the Minimum Track Length parameter establishes a bar each tracker has to clear. Whatever falls under that bar turns red. From there, click the Select Tracks Satisfying Filters button to grab the shorter tracks, then click Delete in the Options section of the Inspector.

### Exporting a 3D Scene for Efficiency

The Camera Tracker stores every one of its 2D tracks inside the composition, which can occasionally leave a fairly bulky file on disk. When you're working with a lengthy clip holding many 2D tracks across a long span, the saved composition may grow past a gigabyte. Keeping a Camera Tracker node within a composition can make loading and working with it sluggish. Although you can composite straight from the Camera Tracker node through its 3D output, exporting nets you better performance. After the solve reaches a quality you're happy with, the Export tab can spin up a “low memory” alternative by emitting separate Camera 3D, Point Cloud, Ground Plane, and 3D Renderer nodes. Before the 3D scene can be exported, however, you need to supply it with a little extra information. The controls on the Export tab are where you do that. Since cameras carry no tiltmeters, clips hold no metadata describing how the camera was tilted or oriented. That detail is essential when rebuilding the virtual camera. Pinpointing where the center of this 3D scene lies is also worthwhile. The Export tab supplies an assortment of translation, rotation, and scale controls for dialing in these settings.

### Unalign the 3D Scene Transforms

Out of the box, the Export tab sits on Aligned within the 3D Scene Transform section. The Aligned setting pins down the 3D scene's orientation and scale so they can't be altered by accident. As a result, before you can fix the ground plane and origin location, you have to flip the Camera Tracker to unaligned through the 3D Scene Transform menu on the Export tab. Once you've worked through the Export settings and arranged them to your liking, switch the menu back to Aligned ahead of exporting.

Switch the 3D Scene Transform menu over to Unaligned ahead of fixing the ground plane

### Setting the Ground Plane

The Camera Tracker can't tell whether the camera is lying on its side or tilted at some angle. That makes it your job to point out where the ground plane sits in a clip. Once you've selected Unaligned from the 3D Scene Transform menu, you can set about marking the ground plane.

Drag a selection box around marks that represent the ground

To set the ground plane, do the following: 1 Jump to a frame packed with green 3D locators where a sizable stretch of the ground is visible. 2 Inside the viewer, drag a selection box over the marks sitting on the ground in the clip. 3 Within the Inspector Orientation section, click the Set from Selection button. TIP: Now and then, the clip you're tracking won't have any ground in the frame. When that happens, you can switch the Selection menu to XY, signaling that the points you're picking lie on a wall.

### Setting the Origin

When the moment arrives to drop and place new objects into your 3D scene, you can smooth the task by pinning down the origin, or center, location. Follow these steps to establish the 3D scene's origin: 1 Jump to a frame that plainly reveals the region you mean to designate as the scene's center. 2 In the viewer, either click a lone point or drag a selection box over a handful of marks sitting where you'd like the 3D scene's center to land. 3 In the inspector Origin section, click the Set from Selection button.

### Setting the Scale

The Camera Tracker has no sense of how big the 3D scene actually is, which is why the scale parameter exists to rescale the scene output. That capability lets you line up the scale across two or more clips.

### Realign the Scene

Ahead of exporting the scene out of the Camera Tracker, return the 3D scene Transform menu to Aligned. With that done, you're set to export.

### Viewing the Exported Results

Clicking the Export button atop the Inspector builds a working 3D scene, dropping five fresh nodes into the node tree on its own.

- Camera 3D
- Point Cloud
- Ground Plane
- Merge 3D
- Camera Tracker Renderer (3D Renderer)

The five nodes that an export out of the Camera Tracker produces To dig into the 3D scene, pick the Merge 3D and send it to one of the viewers, then pick the Camera Tracker Renderer and send that one to a second viewer.

Viewing the Merge 3D shows the point cloud, ground plane, and camera

With the Merge 3D selected, a toolbar sitting above the viewer can drop in 3D test geometry such as an image plane or cube to confirm the accuracy of the 3D scene and camera. From there you can wire genuine 3D elements into the Merge 3D exactly as you would for any hand-built 3D scene. The point cloud serves to align and steer where objects go, and the CameraTracker Renderer amounts to a Renderer 3D node sharing every one of the same controls.

Lean on the point cloud to position the various elements precisely within a 3D scene From this point on, the Camera Tracker node serves no purpose unless you discover you have to run the solver again. Failing that, deleting the Camera Tracker node frees up some memory.
