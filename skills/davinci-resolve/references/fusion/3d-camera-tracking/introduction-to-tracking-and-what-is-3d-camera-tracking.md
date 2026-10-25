# Introduction to tracking and what is 3D camera tracking

Version: DaVinci Resolve 20.3 Reference Manual. Context: 3D camera tracking.
[Chapter index](INDEX.md) / [Next section](automatic-tracking-point-count-and-preview.md)
<a id="source-2d-view"></a> <a id="source-3d-camera-tracking"></a> <a id="source-3d-camera-tracking-part-1"></a> <a id="source-3d-view"></a> <a id="source-auto-tracking-in-the-camera-tracker"></a> <a id="source-clips-that-dont-work-well-for-camera-tracking"></a> <a id="source-how-camera-tracking-works"></a> <a id="source-introduction-to-tracking"></a> <a id="source-outputting-from-the-camera-tracker"></a> <a id="source-the-camera-tracker-tab"></a> <a id="source-the-camera-tracking-workflow"></a> <a id="source-what-is-3d-camera-tracking"></a>

### 3D Camera Tracking

These pages walk through how the Camera Tracker node operates and the workflow built around it. The point of camera tracking is to derive a virtual camera inside Fusion's 3D environment from how a real camera moved through a live-action clip. With that virtual camera in hand, you can drop 3D models, text, or flat 2D images into a live‑action shot whose camera is in motion.

To read up on Fusion's remaining tracking methods, turn to Chapter 82, "Using the Tracker Node," within the DaVinci Resolve Reference Manual, or to Chapter 22 in the Fusion Reference Manual.

### Introduction to Tracking

Few compositing techniques are as valuable or as fundamental as tracking. Loosely speaking, it means producing a motion path by studying how a chosen region behaves across the frames of a clip. To handle the various kinds of motion you might encounter, Fusion ships several distinct tracking nodes, and every tracker type is documented in its own chapter here. The material below concentrates on tracking by way of the Camera Tracker node.

### What Is 3D Camera Tracking?

Match moving relies on camera tracking, which bridges 2D footage and 3D scenes so that artists can drop 3D CGI elements into live-action clips. By working out where the real camera traveled, the Camera Tracker node produces a virtual camera positioned in 3D space. The aim is for that virtual camera to behave just like the one that originally filmed the shot, reproducing both its movement and its lens focal length. Getting that virtual camera's location and motion right is what makes 3D elements sit convincingly against the live action.

An example of 3D elements integrated in a live-action scene

### How Camera Tracking Works

The starting point for camera tracking is following stationary features as they shift from frame to frame. Said differently, the algorithms latch onto features that are "nailed to the set." Anything that travels on its own apart from the camera, like passing cars or pedestrians, degrades the tracks, which is why masks can rein in which features get tracked and sharpen the outcome. It also pays to supply concrete camera metadata, for instance the sensor dimensions and the lens focal length. Feeding that data into the scene-reconstruction step, known as a solver, steers it toward a truer virtual camera. What the Camera Tracker ultimately delivers is an animated 3D camera plus a point cloud of the scene. That point cloud is a dense collection of points the solver produces, approximating where the tracked features sit in 3D. You can then lean on the point cloud to line up other 2D or 3D elements beside the live-action footage.

### The Camera Tracking Workflow

There are two principal stages to camera tracking: 1 Tracking, the act of examining a scene. 2 Solving, which works out the virtual 3D scene. After both stages are finished, an animated camera and point cloud get pushed from the Inspector into a 3D composite. All of this lives inside the single Camera Tracker tool. Across the top of the Inspector sit five tabs, ordered loosely to match the sequence you'll follow. The five tabs are:

- Track: Used to track a clip.
- Camera: Configures the basic Camera parameters.
- Solve: Works out where the 2D tracking points belong in 3D and rebuilds the camera.
- Export: Produces a Camera 3D node, a Point Cloud node, plus a 3D scene within the node tree.
- Options: Used to customize the look of the onscreen overlays.

### The Camera Tracker tab

### Clips That Don't Work Well for Camera Tracking

While the Camera Tracker runs largely on its own, there are moments when it leans on you. Spotting likely trouble up front, before any tracking or solving, can spare you a great deal of effort. Some footage is far harder on the tracking process than other footage. A few of these cases can be repaired; with others you simply concede and reach for a different approach. Below is a roster of shot types worth watching for, since each one tends to be a real thorn for camera tracking:

- Lack of depth: For the process to function, a clip has to contain parallax. As the camera travels, you need to be able to tell nearer objects apart from ones farther off. With everything sitting an equal distance away, depth simply can't be derived. Here you're better off bypassing the Camera Tracker node and looking for a different route.
- Locked-off shots: A camera that never moves leaves no basis for working out which objects sit nearer and which sit farther. Once more, don't sink much effort into this case; bypassing the Camera Tracker node and finding another route is the wiser move.
- Tripod pans: Much like a locked-off shot, a pan that stays fixed atop a stationary tripod offers no basis for sorting nearer objects from farther ones. Bypass the Camera Tracker node and look for a different route.
- No detail: Footage such as green screens lacking tracking markers simply doesn't carry enough detail to track. Should you be fortunate enough to take part in filming these kinds of shots, dropping in tracker markers makes a solid track far simpler to obtain. Lacking detail, the tracking will fall apart and you'll have to turn to a more hands-on fix.
- Motion blur: Quick camera moves or long shutter exposures can bring on motion blur, which complicates the hunt for patterns to track. Footage like this is worth a try to gauge whether enough detail survives for a good solve, but recognize the moment to abandon it for another route.
- Rolling shutter: With CMOS-based cameras, the shutter records separate lines at marginally different instants, which can throw in distortion. For camera tracking, that distortion can spell serious trouble. On occasion you can build motion vectors via the Optical Flow node, synthesizing fresh in-between frames that drop the rolling shutter's wobble. The fixed-up footage can then feed into the Camera Tracker.
- Parallax issues: Where objects at varying distances overlap within the frame, that overlapping region risks being read as a corner. A tracker placed on such an overlapping angle will throw errors once the parallax begins shifting and that overlap region drifts. The remedy in Fusion is deleting that tracker ahead of the solve.
- Moving objects: Capturing a shot in which nothing moves is tough. Crowds, vehicles, animals, and the like can drift into and out of frame. Since these objects travel apart from the camera, they must be removed or they'll trigger solving errors. The fix is masking off anything not "nailed to the set." Those masks then route into the Track Mask input on the Camera Tracker node.

TIP: Footage that defeats Fusion's Camera Tracker can sometimes be handled by purpose-built 3D camera-tracking packages such as 3D Equalizer and PF Track. The tracking data those programs produce can later be brought into Fusion through the Camera3D node.

### Outputting from the Camera Tracker

In contrast to nearly every other Fusion node, the Camera Tracker node provides two separate outputs:

- The first one, a 2D view, serves you while you lay out the Track, fine-tune the camera, and carry out your initial solve.
- The other, a 3D output, comes into play once that initial solve is done, letting you survey the camera path and point cloud throughout 3D space. It proves useful while you polish tracks for a more accurate solve and square up your ground plane. You can run it alongside the 2D output in side-by-side views.

Keep in mind that whatever tracks you select in the 2D view stay linked to their matching locators in the point cloud over in the 3D view. On top of that, both the 2D and 3D views carry viewer menus that put fast control of this tool's behavior at your fingertips.

### 2D View

For this node, the 2D view serves as the main display. When you view the node you see the footage under analysis along with overlaid tracker markers and the paths they trace. A purpose-built toolbar puts the everyday tracking and solving controls within reach.

The Camera Tracker 2D output with toolbar and auto-track points

### 3D View

A 3D scene comes out of the Camera Tracker node's second output. Seeing it requires routing that 3D output into a 3D Transform or Merge 3D node, then viewing the latter.

After solving, routing the Camera Tracker node's second output into a Merge 3D shows the point cloud in 3D. Following an initial solve, that 3D output presents the point cloud together with the camera and the image wired to it. Picking points brings up the Camera Tracker toolbar over the viewer, handing you control over assorted actions like renaming, deleting, and recoloring the point-cloud points.

3D output of a point cloud and a solved camera path

### Auto-Tracking in the Camera Tracker

The word tracking covers the job of watching or examining a run of frames (in other words, a clip). Before it can pin down where the virtual camera sits and how it moves, the Camera Tracker node has to account for how the original footage moves. On its own, the Camera Tracker tool hunts down high-contrast patterns in the clip and pins trackers onto those features. The strongest track comes from spreading tracking points broadly over the frame and from points that persist for a long duration.
