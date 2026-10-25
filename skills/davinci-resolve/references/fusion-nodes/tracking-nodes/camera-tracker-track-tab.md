# Camera tracker track tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Camera tracker.
[Chapter index](INDEX.md) / [Next section](camera-tracker-solve-tab.md) / [Continue Camera Tracker CTra / 3D Scene Transform](camera-tracker-3d-scene-transform.md)
<a id="source-basic-node-setup"></a> <a id="source-camera-tab"></a> <a id="source-camera-tracker-ctra"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-new-track-defaults"></a> <a id="source-the-camera-tracker-camera-tab"></a> <a id="source-the-camera-tracker-node"></a> <a id="source-the-camera-tracker-tab"></a> <a id="source-the-camera-tracker-with-occlusion-masks"></a> <a id="source-track-tab"></a> <a id="source-tracking-nodes"></a> <a id="source-tracking-nodes-part-1"></a>

### Tracking Nodes

This chapter walks through the Tracking nodes that Fusion provides.

Each node name carries an abbreviation beside it; those shortcuts work in the Select Tool dialog while you hunt for a tool, and they apply in scripting references too. Throughout this document, treat any node tree that displays MediaIn nodes within DaVinci Resolve as equivalent to Loader nodes inside Fusion Studio, except where a note says otherwise.

### Camera Tracker [CTra]

### The Camera Tracker node

Match moving is what camera tracking does, and it forms a crucial bridge between 2D and 3D so that compositors can drop 3D renders into footage shot live. You rely on the Camera Tracker node to work out where a real camera traveled and to build a matching virtual camera inside 3D space. The plan is for that virtual camera to move exactly the way the physical camera moved while filming the scene. Once you have the virtual camera's solved position and travel, you gain the freedom to layer 3D elements into a live-action shot. On top of that, the Camera Tracker produces a point cloud out in 3D space, handy for lining up objects and additional 3D models with the filmed scene. To learn more about working with the Camera Tracker, refer to Chapter 86, "3D Camera Tracking," in the DaVinci Resolve Reference Manual, or to Chapter 26 in the Fusion Reference Manual.

The original video clip

3D objects layered onto the video clip, relying on the camera tracker so they stay locked to the frame's objects while the picture shifts

### Inputs

Two inputs feed the Camera Tracker: Background: A 2D image you intend to track is fed into the orange image input. Occlusion Mask: Use the white occlusion mask input to block off areas the tracker should skip. Wherever this mask reads white, no tracking happens. As an example, someone walking across the foreground and hiding parts of the scene can throw off the tracker, so sketching a quick rough mask around that person tells the tracker to disregard those masked-out areas.

### Basic Node Setup

Hook the image you want tracked into the Camera Tracker background input. Feed polygon masks into the occlusion mask input to flag the areas you'd like the tracker to skip.

### The Camera Tracker with occlusion masks

### Inspector

### The Camera Tracker tab

### Track Tab

You'll find the controls for setting up a first pass over the scene in the Track tab. Auto Track Spots trackable features on its own and follows them across the source footage. A track ends automatically once its track error climbs too high, while fresh tracks spin up as

needed. Dialing the Detection Threshold and Minimum Feature Separation sliders lets you govern how many auto tracks appear and how they spread out. Reset Wipes every piece of data stored inside the Camera Tracker node, spanning the tracking data along with the solve data (camera motion path and point cloud). When you only want to clear the solve data, reach for the Delete button on the Solve tab. Preview AutoTrack Locations Switching this checkbox on reveals where the auto tracks would land across the shot. It comes in handy for judging whether the Detection Threshold and Minimum Feature Separation require tweaking to spread trackers evenly. Detection Threshold Governs how sensitively features get detected. Tracks generated automatically are placed on the shot, and the Detection Threshold pushes them toward either high-contrast or low-contrast spots. Minimum Feature Separation Sets how far apart the auto-generated tracking points sit. Lowering this slider yields a greater number of auto tracks. Bear in mind that piling on tracking points also stretches out the solve. Track Channel Picks a color channel to follow: red, green, blue, or luminance. As you pick a channel, favor one carrying plenty of contrast and detail. Track Range Sets which frames get tracked:

- Global: The global range, which is the full duration of the Timeline.
- Render: The render duration set on the Timeline.
- Valid: The valid range is the duration of the source media.
- Custom: A user-determined range. Picking this reveals its own range slider for fixing

the start and end of the track range. Bidirectional Tracking Switching this on makes the tracker run backward once the first forward pass finishes. While tracking in reverse, no new tracks begin; instead the tracks you already have stretch backward through time. Leaving this on is advisable, since lengthy tracks tend to yield stronger solved cameras and point clouds. Gutter Size Trackers grow shaky once they near the picture's edge, where they may drift, jitter, or drop their pattern entirely. The Camera Tracker shuts down any track that crosses into the gutter zone. The gutter size figure is stated as a percentage of pattern size. Out of the box it sits at 100% of pattern size, which makes a 0.04 pattern translate into a 0.04 gutter.

### New Track Defaults

The Camera Tracker node can study the scene by three different methods, and each plays to its own strengths against particular kinds of camera movement. Tracker: Under the hood, every Tracker relies on the Optical Flow Tracker to follow features through time, then sharpens those tracks further with the dependable Fusion Tracker or Planar Tracker. With the Planar Tracker method, the pattern is free to warp over time through several kinds of transforms as it seeks the best fit. Those transforms are:

- Translation
- Translation and Rotation Translation, Rotation, and Scale Affine
- Perspective

Sticking with the default TRS setting is advisable whenever you work with the Planar Tracker. Both the Affine and Perspective settings require sizable patterns to track reliably.

- Close Tracks When Track Error Exceeds: A track ends on its own once the tracking error climbs too high. As a feature gets tracked, the pixels surrounding it are captured at the track's reference time. That capture is termed a pattern, and the software then looks for the identical pattern of pixels at later times. The gap between the pattern at the present time and the pattern at the reference time is what's called the track error. Pushing this option higher yields longer tracks that grow steadily less precise.
- Solve Weight: Out of the box, every track carries equal weight during the solve process. Bumping up a track’s weight makes it pull harder on the solved camera path. Consider this an advanced option that rarely needs touching.

Auto Track Defaults Assign a custom prefix name and/or color to the tracks generated automatically. That custom color shows up whenever Track Colors in the Options tab is set to User Assigned.

### Camera Tab

### The Camera Tracker Camera tab

The Camera tab's controls let you describe the physical traits of the live-action camera, which serve as a launching point as the solver hunts for parameters matching the real-world camera. The more precise the data you supply here, the more precise the resulting camera solve. Within the Camera tab sit controls covering the lens and gate properties of the camera being solved for.

Focal Length State the known fixed focal length that filmed the scene, or supply a guess when the Refine Focal Length option is switched on in the Solve tab. Film Gate Pick a film gate preset from the drop-down menu, or type the film back size by hand into the Aperture Width and Aperture Height inputs. Keep in mind that these figures are in inches. Aperture Width Should the camera that shot the scene be missing from the preset drop-down menu, key in the aperture width (inches) yourself. Aperture Height Should the camera that shot the scene be absent from the preset drop-down menu, key in the aperture height (inches) yourself. Resolution Gate Fit This sets how the picture maps onto the sensor size. Film sensors are frequently built to span several formats, with only a slice of the sensor area captured into a picture. As an illustration, a 16:9 image gets pulled from a full aperture-sized sensor. As a rule, fitting to Width or Height works best. The remaining fit modes are Inside, Outside, or Stretched. Center Point This marks where the camera lens lines up with the camera. It defaults to (0.5, 0.5), the dead center of the sensor. Use Source Pixel Aspect This adopts the squeeze aspect of the pixels carried in the loaded image. HD uses square pixels, whereas NTSC carries a pixel aspect ratio of 0.9:1, and Anamorphic CinemaScope runs a 2:1 aspect. Turning this option off reveals Pixel X and Y number fields where you can tailor the source pixel aspect. Auto Camera Planes With this on, the camera’s image plane and far plane shift automatically to wrap around the point cloud each time a solve finishes. Now and then, though, the solver will oddly hurl points way off deep into the scene, which in turn shoves the image plane far away. That leaves the resulting scene awkward to handle within the 3D views. When that happens, switch this option off to bypass the default behavior (or remove the troublesome tracks).
