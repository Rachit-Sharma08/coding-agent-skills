# Planar tracker node controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Planar tracker node.
[Chapter index](INDEX.md) / [Previous section](planar-tracker-node-what-the-planar-tracker-saves.md) / [Planar Tracker Node PTRA](planar-tracker-node-what-the-planar-tracker-saves.md) / [Next section](planar-tracker-node-steady-mode.md)
<a id="source-track-mode"></a> <a id="source-tracking-nodes-part-3"></a>

### Track Mode

What separates Track mode from the Operation menu’s other three choices is that it alone sets the planar tracking in motion; the rest simply consume the tracking data Track mode has produced. Tracker You get two trackers to choose between:

- Point: Follows points across successive frames. Under the hood, this tracker is not really chasing points as such but small patterns, much as Fusion’s Tracker node does. The point tracker can build its own internal occlusion mask on its own, spotting and discarding outlier tracks that fall outside the dominant motion. In the viewer, tracks show up green or red according to whether the point tracker judges them part of the dominant motion or casts them out. If you like, you can hand it an external occlusion mask to steer the Point tracker further.
- Hybrid Point/Area: Puts an Area tracker to work on every pixel in the pattern. The Area tracker, unlike the Point tracker, cannot on its own throw out portions of the pattern that stray from the dominant motion, so you have to feed it an occlusion mask yourself. For the sake of performance the Hybrid tracker quietly runs the Point tracker first, which explains why the point tracks remain visible in the viewer. No single tracker wins outright; each brings its own trade-offs:

Artist Effort (occlusion masks): The Point tracker spins up its own internal occlusion mask without your help, whereas the Hybrid tracker has you putting in extra time crafting occlusion masks by hand. Accuracy: Because it tracks every pixel in the pattern instead of a handful of standout feature points, the Hybrid tracker comes out more accurate and less given to wobble, jitter, and drift. Speed: The Hybrid tracker runs slower than the Point tracker. As a rule, do a fast first pass on the shot with the Point tracker and study the outcome; if it does not hold up, then reach for the Hybrid tracker. Motion Type Sets how the Planar Tracker models, internally, the distortion of the flat surface under track. There are five distortion models:

- Translation.
- Translation, Rotation (rigid motions).
- Translation, Rotation, Scale (squares stay squares, with scale held uniform across x and y).
- Affine - covers translation, rotation, scale, and skew (turns squares into parallelograms).
- Perspective (turns squares into arbitrary quadrilaterals).

Every model in turn is broader than the last and folds in all the earlier ones as special cases. Unsure which to use? Go with Perspective for your first track attempt. Where the footage carries perspective distortions and you pin the Planar Tracker to a simpler motion type, the track can wind up sliding and wobbling. On stubborn shots, stepping down to a simpler motion model can occasionally help — say when a lot of track points bunch up on one edge of the tracked region, or when you are tracking a small region thin on trackable pixels.

Output Governs what the Planar Tracker node sends out while it is running in the Track operation mode.

- Background: Passes the input image through untouched.
- Background - Preprocessed: Ahead of tracking, the Planar Tracker runs assorted preprocessing on the

input image (converting it to luma, for one), and seeing that can help you settle on which track channel to use.

- Mask: Emits the pattern as a black-and-white mask.
- Mask Over Background: Emits the pattern mask composited over the background.

Track Channel Picks which image channel of the background image gets tracked. Aim for a channel rich in contrast and trackable features but light on noise. The permitted values are red, green, blue, and luminance. Tracking Controls This is the set of controls that drives the Tracker. Keep in mind that, during tracking, you should only advance to a new frame when the current one is already tracked or is the reference frame.

- Track to start: Runs the track backward from the current frame to the start (set by the current render range).
- Step tracker to previous frame: Advances the track one frame back, from the current frame to the prior one.
- Stop tracking: Halts whatever tracking operation is underway.
- Step tracker to next frame: Advances the track one frame forward, from the current frame to the following one.
- Track to end: Runs the track forward from the current frame to the end (set by the

current render range).

- Trim to start: Clears every bit of tracking data ahead of the current frame.
- Delete: Wipes all tracking data across all times. Reach for this to throw away every current result and begin

tracking afresh.

- Trim to end: Clears every bit of tracking data after the current frame. It comes in handy, for instance, to

cut off the tail of a track that has drifted out of accuracy once the pattern begins sliding off frame. Show Splines Located just to the right of the "Trim to end" button, this control brings up the Spline Editor and displays the splines tied to the Planar Tracker node. It helps when, by hand, you need to delete points belonging to the Track as well as the Stable Track splines. Right-Click Here for Track Spline During tracking, a spline is built that holds 4 x 4 matrices at every keypoint. It goes by the name "Track spline," or simply "Track." Those matrices fully describe the distortions of the tracked pattern. Create Planar Transform Once footage has been tracked, pressing this button spawns a Planar Transform node in the Node Editor. The present tracking data is baked into the Planar Transform node so it can reproduce the planar distortions that the Planar Tracker node captured. Unless your composite involves a full frame foreground matching the raster's dimensions exactly, the best practice is to make a Planar Transform and drive the foreground's motion with it.
