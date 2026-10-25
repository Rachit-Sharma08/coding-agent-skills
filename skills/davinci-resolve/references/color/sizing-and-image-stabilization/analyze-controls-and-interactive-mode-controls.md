# Analyze controls and interactive mode controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Sizing and image stabilization.
[Chapter index](INDEX.md) / [Previous section](sizing-presets-and-node-channel-effects.md) / [Next section](classic-point-tracker-stabilization.md)
<a id="source-analyze-controls"></a> <a id="source-classic-stabilization-with-the-cloud-tracker"></a> <a id="source-interactive-mode-controls"></a> <a id="source-sizing-and-image-stabilization-part-2"></a> <a id="source-stabilization-parameters-and-controls"></a> <a id="source-stabilization-selections"></a>

### Analyze Controls

The Analyze controls sweep through the whole clip on their own, picking out trackable features that can serve to steady the shot. A set of four checkboxes lets you switch on and off the axes you want stabilized. These checkboxes have to be ticked before you run an analysis so the data that gets generated stays limited.

- Pan: Enables horizontal stabilization.
- Tilt: Enables vertical stabilization.
- Zoom: Enables stabilization of size.
- Rotate: Enables stabilization of orientation.

NOTE: After stabilization is done, switching these checkboxes off does nothing to change the outcome. To make changes you first need to tick or untick the relevant checkboxes, then reanalyze the clip. The five direction buttons let you run the stabilization analysis.

- Track One Frame Reverse: Kicks off tracking from the present frame, going back one frame’s worth.
- Track Reverse: Kicks off tracking from the present frame going backward, stopping at the clip’s first frame.
- Pause: Halts tracking (provided you’re quick enough to hit this button before tracking wraps up).
- Track Forward: Kicks off tracking from the present frame going forward, stopping at the clip’s last

frame.

- Track One Frame Forward: Kicks off tracking from the present frame, going ahead one

frame’s worth.

### Interactive Mode Controls

The Interactive controls let you tweak by hand the tracking point cloud DaVinci Resolve builds on its own, so you can try out different approaches to landing better stabilization results in tricky situations.

- Interactive Mode checkbox: Flips the Interactive stabilization mode on and off. Step into Interactive mode and you can reshape by hand the point cloud DaVinci Resolve uses to steady the image. You then run your analysis while still in Interactive mode. Step back out of Interactive mode and your hand-made changes to the point cloud are dropped, with DaVinci Resolve once more using automatically placed point clouds for all stabilization.
- Insert: Lets you drop tracking points onto whatever analyzable features sit inside a bounding box you’ve drawn in the Viewer. Inserted stabilization points get placed on their own.
- Set Point: Lets you use the cursor (via the DaVinci Resolve control panel) to place individual tracking points by hand, one at a time, to track a feature with. If no trackable pixel group sits at the coordinates where you set the cursor, a tracking point lands on the nearest trackable pixel group. You have to set no fewer than two tracking points across separate pixel groups to track rotation, and no fewer than three for tracking zoom.
- Delete: Clears every stabilization point that falls inside a bounding box you’ve drawn in the Viewer.

The steps for using Interactive mode to stabilize match the ones for tracking. To read more, refer to Chapter 140, “Motion Tracking Windows.”

### Stabilization Parameters and Controls

The Stabilization group holds five controls:

### Stabilization selections

- Strong: Lets you set how tightly the stabilization track is used to clear motion out of a shot. At a value of 100, stabilization peaks in a bid to “lock” the shot in place and wipe out every bit of camera motion. This value works as a multiplier. Because certain clips can feel more natural with looser stabilization, picking a figure under 100 leaves a slice of the original camera motion visible. Zero (0) shuts stabilization off entirely. On top of that, you can flip the stabilization around by picking –100, as laid out in the section on running a match move below, and you can apply a negative value either below or above –100 to under- or overcompensate while inverting the stabilization, faking the parallax effect where foreground and background planes travel together yet at differing rates.
- Smooth: Lets you lay mathematical smoothing onto the analyzed data the clip is stabilized with, and is intended for use once the Strong parameter drops below 100, leaving camera motion in the shot while clearing out unwanted wiggle. Lower values smooth less, letting more of the original camera move’s character come through, whereas higher values smooth the shot more aggressively.
- Zoom: With this checkbox switched on, the image is enlarged by enough of a percentage to clear the blanking (black edges) left behind by repositioning the image to cancel unwanted camera motion. The higher Smooth Frames is set, the more DaVinci Resolve has to zoom into an image to clear those blanked edges. Switch this off and the image isn’t zoomed at all, so whatever blanking creeps into the frame goes out alongside the image, on the premise that you’ll have dedicated compositing artists handle clearing that blanking by painting in the missing image data through more elaborate means. You can also keep this checkbox off if you mean to animate the Input Sizing Zoom parameter to push into and out of a stabilized shot, clearing blanking only at the spots it shows up, using no more zoom than each part of the shot demands.
- Tracker Type: A drop-down menu beneath the Tracker graph lets you pick whether to go with the Cloud Tracker or the Point Tracker. The default Cloud Tracker on its own rounds up as many trackable points as it can across the image and figures stabilization from all of them. That’s fast, but it can run into trouble when too many prominent subjects in the frame move along different vectors. The Point Tracker, by contrast, lets you set one or more individual crosshairs by hand on image features you pick. That takes more steps, but it carries the upside of letting you pick exactly which features carry the motion you’re out to stabilize.

To learn more about putting the Point Tracker to work for window tracking, turn to Chapter 140, “Motion Tracking Windows.”

- Stabilize: Once you’ve tracked the clip and dialed in the previous two controls, you need to press Stabilize to work out the combined effect of the Strong, Smooth, and Zoom controls on your clip. Any time you change the Strong, Smooth, or Zoom parameters, you need to press Stabilize to recompute the resulting effect on your clip.

### Classic Stabilization With the Cloud Tracker

Classic Image stabilization in DaVinci Resolve is straightforward, but landing it right means following a particular sequence of steps. To stabilize an image: 1 Open the Tracker palette and pick Stabilizer from the Palette mode drop-down menu. Pick Classic Stabilizer in the option menu. Confirm that the Tracker Type drop-down menu at the lower right of the Tracker palette is set to Cloud Tracker. 2 Switch off any of the Analyze checkboxes (Pan, Tilt, Zoom, Rotate, Perspective 3D) tied to transform axes you don’t want smoothed. 3 Hit the Track Forward button so the clip tracks forward (or pick Track Reverse if you’d sooner begin at the clip’s end and work back).

Several tracking points get dropped on their own to study how the image moves for stabilization purposes This studies the clip, though as yet no stabilization gets applied. 4 Set the Strong parameter to match the sort of stabilization you’re after. To strip every trace of motion out of the shot, keep Strong at 100. To use stabilization for taking the edge off the shot while still leaving a bit of motion in frame, pull the strong parameter below 100 yet above 0. Because this parameter acts as a multiplier, larger figures mean a greater share of smoothing gets applied across the clip’s range of motion, while smaller figures mean a smaller share of smoothing gets applied across the original range of motion. 5 Having dialed the Strong parameter under 100 to settle the shot’s motion instead of locking it down outright, you can additionally turn to the Smooth parameter to mathematically even out whatever motion is left over. That gives you a way to flatten unwanted “wobbling” while holding on to the camera movement you’d like to keep. Since the Strong and Smooth parameters operate in tandem, try out a range of values across both until the outcome suits you. 6 Decide how the edges of the stabilized clip ought to be treated by way of the Zoom checkbox:

- Should you want DaVinci Resolve to push into the image as far as it takes to keep blanking (black edges) from creeping into the frame (a side effect of shifting the image to even out camera motion), then switch on the Viewer Zoom checkbox.
- Should you prefer the image scale untouched, letting blanking (black edges) creep into the frame so that you can either (a) hand the job of patching those gaps to an effects artist down the line, or (b) keyframe the Input Sizing Zoom parameter yourself to remove blanking dynamically, then switch off the Viewer Zoom checkbox.

7 Once all of those controls are set, press Stabilize. Right away the clip gets reshaped to deliver whatever degree of stabilization you dialed in through the Smooth Frames slider. 8 Run the clip and look over how the stabilization turned out. Should adjustments be in order, pick fresh Strong and Smooth Frames values and press Stabilize once more. Each time you alter any of the Stabilization parameters, pressing Stabilize is required so the resulting transform on your clip gets recomputed.
