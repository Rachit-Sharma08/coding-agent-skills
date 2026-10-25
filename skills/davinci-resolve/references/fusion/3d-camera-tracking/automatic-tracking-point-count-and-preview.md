# Increasing auto generated tracking points and previewing tracking points

Version: DaVinci Resolve 20.3 Reference Manual. Context: 3D camera tracking.
[Chapter index](INDEX.md) / [Previous section](introduction-to-tracking-and-what-is-3d-camera-tracking.md) / [Next section](how-to-judge-track-accuracy-and-deleting-tracks.md)
<a id="source-choosing-a-tracking-algorithm"></a> <a id="source-cleaning-up-camera-solves"></a> <a id="source-how-do-you-know-when-to-stop"></a> <a id="source-increasing-auto-generated-tracking-points"></a> <a id="source-masking-out-objects"></a> <a id="source-matching-the-live-action-camera"></a> <a id="source-previewing-tracking-points"></a> <a id="source-running-the-solver"></a> <a id="source-sometimes-theres-nothing-you-can-do"></a> <a id="source-the-camera-tab-in-the-camera-tracker-tool"></a> <a id="source-tips-for-solving-camera-motion"></a> <a id="source-using-seed-frames"></a>

### Increasing Auto-Generated Tracking Points

Whereas you place tracking points yourself with the Tracker node, the Camera Tracker handles it fully automatically, though the Detection Threshold and Minimum Feature Separation sliders give you control over the rules used to locate tracking points. Drop those values and you raise how many tracking points turn up. That comes in handy when a scene yields too few points, leaving the solver unable to build an accurate camera and point cloud. Still, tread carefully with these tweaks, because piling on too many points can spawn redundant trackers that bog the whole process down while gaining you little.

### Previewing Tracking Points

To inspect the tracking points the clip currently has, view the Camera Tracker node and switch on the Preview AutoTrack Locations checkbox. Doing so paints green tracking points into the viewer while you scrub through the clip. That preview lets you judge whether the Detection Threshold or Minimum Feature Separation need tweaking to raise or lower how many tracking points appear on their own.

Green tracker dots appear on their own atop the features within an image Bi-Directional Tracking As you run a track, switching on the Bidirectional Tracking checkbox makes it track forward from the clip's beginning first, then run a reverse second pass. By revisiting points that the forward pass first found, this two-pass method may stretch out how long any given point lasts. Short of being pressed for time, there's hardly a reason to leave it off. Yes, bidirectional tracking eats more time, yet it generally pays off and runs fairly fast given what you gain.

### Choosing a Tracking Algorithm

You get three options for which tracking algorithm runs. Those three live in the New Track Defaults section of the Inspector:

- Optical Flow: Generally the pick to reach for, except when a clip is full of criss-crossing objects.
- Tracker: A solid fallback whenever motion-estimation trouble like criss-crossing objects rules out Optical Flow.
- Planar: Suited mainly to plainer clips, where most of the frame is made of flat surfaces like building facades.

### Masking Out Objects

As it tracks a clip, the Camera Tracker lays down trackers on feature details on its own. That said, not every feature that pops out in a clip suits camera tracking. The only features you want tracked are those "nailed to the set." Put another way, things that move on their own apart from the camera, such as cars and people in motion, introduce errors during camera tracking. Such objects have to be cut from the analysis. Masking is the main route to steering clear of these trouble spots. By wiring a mask into the Camera Tracker node's Track Mask input, you mark which regions of a scene the Camera Tracker is allowed to study. Take a shot of an airport runway beside a coastline: the water's waves and the drifting clouds overhead need masking because they travel independently of the camera. As you build the mask, the steady portions of the image meant for tracking analysis belong in the white part of the mask. Everything in motion that should be skipped belongs in the black part. That mask then gets wired into the Camera Tracker Track Mask input.

Masks keeping the drifting clouds and waves out of the Camera Tracker's analysis

With that in place, the tracker disregards the water's waves and the drifting clouds. This mask isn't like one you'd draw for an effect; it needn't be exact. Your only aim is to mark the approximate zone you want hidden from the tracking analysis.

On the left, the source image set for tracking; on the right, the occlusion mask covering the clouds and water

TIP: When a shot carries plenty of motion, the Tracker or Planar Tracker nodes can drive your occlusion mask so it rides along with the region you mean to track. Bear in mind, though, that once the PlanarTracker or PlanarTransform node has warped your mask, a Bitmap node is needed to convert it back into a mask suitable for the Camera Tracker node's Track Mask input.

### Matching the Live-Action Camera

With tracking behind you, the workflow's following stage calls for the controls on the Camera tab. Here you describe the real camera that was used on set, chiefly its film gate size and focal length. Ideally that detail was recorded on set so it's on hand during postproduction. With camera-original media, the file metadata will sometimes hold this information. Use the steps below to track down camera metadata:

- Working in DaVinci Resolve, pick the MediaIn node holding the camera clip, bring up the Metadata Editor, and look at the Camera metadata preset.
- Working in Fusion Studio, bring up the metadata subview using the viewer toolbar.

### The Camera tab in the Camera Tracker tool

When you don't have the real figures, make your best estimate. Because the solver hunts for a camera in the vicinity of these settings, handing it values as near to the live action as you can manage helps it along. Better input on your part yields a more precise solver result. As a bare minimum, at least pick the right camera model in the Film Gate menu. Choose the wrong film gate and the odds of the Camera Tracker nailing the lens focal length drop sharply. Unlike the Track and Solve tabs, the Camera tab carries no button at the top of the Inspector to kick off a process. Once the camera settings are in place, the Camera tab has nothing further to run. Having dialed the camera settings to match the live-action camera, you head over to the Solve tab.

### Running the Solver

This phase of the workflow centers on the controls living in the Solve tab. Solving is a heavy computation where the Camera Tracker studies the tracks that currently exist to build a 3D scene. Out of it come a virtual camera mirroring the live action and a point cloud of 3D locators that reproduce the tracked features in 3D space. Driving the analysis is the frame's parallax, the effect whereby features nearer the camera appear to travel faster than those farther off. Picture gazing out a car's side window, where distant scenery drifts by more slowly than whatever sits near the road's edge. Whether the solver succeeds or fails hinges heavily on the trackers gathered during the Track phase, so handing it the finest set of tracking points from the outset is essential. Even though the occlusion masking you set up earlier strips out troublesome tracking points, you'll nearly always have to thin and remove low-quality tracks further inside the Solver tab. That's why, from your vantage point, solving is best approached as something you repeat. To work out a camera's motion: 1 Press the Solve button so the solver runs. 2 Screen out and remove weak tracks. 3 Run the solver once more.

The Solver tab once a run has finished, yielding an average solve error of 04367 pixels

### How Do You Know When to Stop?

Once solving wraps, an Average Solve Error (also referred to as a reprojection error) shows up at the top of the Inspector. That number is the key gauge of how well the computation turned out. For HD material, anything under 1.0 counts as a good Average Solve Error. Read a value of 1.0 as a one-pixel offset, meaning the track might be off by a single pixel at any moment. As resolution climbs, the solve error ought to drop. On 4K footage, aim to land the solve error under 0.5.

### Tips for Solving Camera Motion

Feeding the solver precise live-action camera details, like focal length and film gate size, can lift the camera solve's accuracy considerably during this stage. As an illustration, a focal length that strays too far from the true physical figure can leave the solver unable to converge and the result worthless. Beyond that, to let the solver triangulate and rebuild the camera and point cloud accurately, you'll want:

- Tracks spread sensibly over objects at assorted depths, without overloading the far background or sky (those add no extra perspective cues for the solver).
- Tracks scattered uniformly across the frame rather than bunched onto a handful of objects or just one side.
- Track beginnings and endings spaced out across time, so few of them finish on the very same frame.

### Using Seed Frames

To begin, the solver assembles a partial solution spanning a pair of seed frames. Normally those seed frames are chosen for you. That automatic pick, however, tacks extra time onto the process. The amount shows up in the solve summary at the top of the Inspector after you run the solver. Picking your own seed frames can trim that time and may yield a stronger solve on tougher clips. From this intermediate solution built on the seed frames, the solver then grows it both forward and backward across the whole clip. Hand-picking seed frames isn't really advised unless camera tracking is already familiar territory for you. Leaving the default Auto Select Seed Frames checkbox turned on in the Solve Options section of the Solver tab picks the optimal frames the bulk of the time. You can, though, clear the checkbox and reach for the Seed Frame 1 and Seed Frame 2 slider to land on frames you think will do better. Two key qualities matter when you settle on seed frames:

- Seed frames should have lots of tracks in common.
- Seed frames should be far apart in perspective.

### Sometimes There's Nothing You Can Do

When a shot lacks the camera motion needed to triangulate where features sit, no reconstruction will reach any worthwhile accuracy. Making a shot camera-trackable starts during the shoot, through the right use of track markers and by making certain the camera moves carry enough shifts in perspective for the solver to extract something useful.

### Cleaning Up Camera Solves

At times the very first solve is already fine. On other occasions you might burn several hours pruning tracks to reach a solid solve, and once in a while it simply can't be done. Over time you develop an instinct for which tracks ought to go and which to keep, and for which shots will prove easy, hard, or hopeless. Watch out, though: stripping away too many tracks can drive the Average Solve Error up, since the solver ends up starved of data. Specifically, with under eight tracks on a frame, the math just doesn't carry enough information to solve the clip. That said, for a sturdy, accurate solve you'll want comfortably more than eight tracks in play. IMPORTANT: When camera tracking is new to you, there's a pull toward reaching straight into the Spline Editor and reshaping the solved 3D splines to better a camera's motion path. Treat that path as a true last-ditch option. The smarter move is to adjust the 2D tracks you're feeding the solver.
