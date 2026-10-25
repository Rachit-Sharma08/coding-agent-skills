# Planar tracking and introduction to tracking

Version: DaVinci Resolve 20.3 Reference Manual. Context: Compositing overview.
[Chapter index](INDEX.md) / [Next section](open-fx-resolve-fx-and-fuse-plugins-and-what-are-open-fx.md)
<a id="source-a-basic-planar-tracker-match-move-workflow"></a> <a id="source-check-for-lens-distortion"></a> <a id="source-different-ways-of-using-the-planar-tracker-node"></a> <a id="source-introduction-to-tracking"></a> <a id="source-overview"></a> <a id="source-planar-tracking"></a> <a id="source-planar-tracking-1"></a> <a id="source-planar-tracking-using-open-fx-resolve-fx-and-fuse-plugins"></a> <a id="source-setting-up-to-use-the-planar-tracker"></a> <a id="source-the-analyze-buttons-of-the-planar-tracker"></a> <a id="source-tips-for-choosing-good-planes-to-track"></a> <a id="source-using-the-planar-tracker"></a>

## Overview

Covers: Planar Tracking; Using Open FX, Resolve FX, and Fuse Plugins.

## Planar Tracking

### Planar Tracking

This chapter walks through working with the Planar Tracker node and leaning on it to keep match moves painless. For a deeper look at the Planar Tracker node, the spot to check is Chapter 119, “Tracking Nodes,” found in the DaVinci Resolve Reference Manual — alternatively Chapter 59 of the Fusion Reference Manual.

### Introduction to Tracking

Fusion ships with three separate Tracking nodes, each suited to studying a particular flavor of motion. After motion has been tracked across a clip, the data that comes back can drive stabilization, motion smoothing, pinning one object's movement to another's, plus countless other bread-and-butter jobs. Every tracker variety gets its own chapter within this manual. Here, the focus stays on the tracking methods built around the Planar Tracker node.

### Using the Planar Tracker

The Planar Tracker node exists to handle the match-moving headaches that crop up on flat, uniform surfaces throughout post-production. Such flat, uniform surfaces might be clips that feature a license plate, a road sign, or a brick wall — surfaces that frequently call for images laid over them, like swapping the digits on the license plate, rewording the city on the road sign, or pasting a billboard poster across the bare brick wall. What the Planar Tracker does automatically is study how the perspective of a planar surface on a background plate warps as time passes, then map those identical perspective shifts onto a separate foreground. TIP: Working with the Planar Tracker also means recognizing the moment to throw in the towel and retreat to Fusion's Tracker node or to hand keyframing. Certain shots just won't track, or the track you get is plagued by excessive jitter or drift. Think of the Planar Tracker as a time-saver in the artist's kit — it handles the bulk of shots, yet no tracker delivers a 100% solution.

### Different Ways of Using the Planar Tracker Node

As with the other tracking nodes Fusion offers, the Planar Tracker can study the footage and hold the resulting image tracking data inside itself, and it can equally turn that tracking data toward transforming a separate image, paint strokes, or a polygon mask shape. The Planar Tracker offers four operating modes: Track: Employed to isolate a planar surface and follow how it shifts as time passes. From there, you can build a Planar Transform node that draws on this data to match move a different clip in assorted ways. Steady: Once a planar surface has been analyzed, this mode strips every bit of motion and distortion off the planar surface — typically to set up a paint or roto pass — before the clip is “unsteadied” to put the motion back. Corner Pin: Once a planar surface has been analyzed, this mode works out and lays a matching perspective warp onto a foreground image you wire into the foreground input of the Planar Tracker node, then merges it over the tracked footage. Stabilize: Once a planar surface has been analyzed, it permits smoothing of how a clip translates, rotates, and scales as time passes. Handy for scrubbing out unwanted vibration while preserving the deliberate overall camera motion.

### Setting Up to Use the Planar Tracker

Much like the Tracker node, performing a planar track means wiring the output of the image you intend to track into the background input of a Planar Tracker node.

Connecting an image to the background input of a PlanarTracker node

### Check for Lens Distortion

Should the image carry barrel distortion, or lens distortion of any other sort, your track can suffer for it. The heavier the lens distortion in the footage, the more the track that results will slip and wobble. Whenever you spot distortion in the image or run into trouble with the track, it's worth slotting the Lens Distort node between the image and the Planar Tracker to clear up the problem. Fusion's Lens Distort node serves to strip out or introduce lens distortion within an image. Wiring the MediaIn or Loader node into the Lens Distort node brings up controls for hand-correcting lens distortion. Should you work with Synth Eyes, PFTrack or 3D Equalizer software, you can additionally pull in lens data from those packages so the corrections happen more automatically.

Placing a Lens Distort node along the path from a MediaIn1 to the Planar Tracker so lens distortion gets cleared For fuller detail on the Lens Distort node, the place to look is Chapter 123, “Warp Nodes,” within the DaVinci Resolve Reference Manual — or else Chapter 63 of the Fusion Reference Manual. Within DaVinci Resolve, the Lens Corrections control on the Cut page or Edit page is available to you. That correction follows through onto the Fusion page. Lens correction inside DaVinci Resolve automatically inspects the frame shown in the Timeline viewer, hunting for edges bent by a wide angle lens. Pressing the Analyze button drives the Distortion slider to deliver an automatic fix. After that, the MediaIn node on the Fusion page carries the correction, and your planar tracking can begin.

### A Basic Planar Tracker Match Move Workflow

Working with the Planar Tracker takes a few stages, yet it feels simple once the technique clicks. The walkthrough below aims to spell out that workflow as plainly as it can. To track a surface using the Planar Tracker: 1 Confirm the Operation Mode sits on Track, since an image has to be analyzed to track a surface before anything else happens. 2 With the background input of the Planar Tracker wired to an image and the Planar Tracker showing in a viewer, drag the playhead to a video frame where the planar surface you mean to track appears largest, sits unoccluded, and reads plainly as a plane, then press the Set button in the Track panel of the Inspector to lock that in as the reference frame steering the track.

Pressing the Set button so the analysis uses your chosen reference frame 3 After that, pin down the exact pattern inside the image you want tracked. Usually that's a rectangle, though any closed polygon you like will work. Whatever pixels sit within this region become the pattern hunted for across the other frames. Bear in mind it matters that the pattern be drawn on the reference frame. Here, our aim is to track the wall behind the man, so we trace a polygon over a stretch of wall the man won't cross as he moves through the shot.

Tracing a polygon over the image area you intend to track, ideally a flat plane that tracks well TIP: Don't mix up the pattern you're marking out with the region you mean to corner pin (which always carries four corners and gets its own separate definition in Corner Pin mode.

4 (Optional) When moving objects partly hide or occlude the planar surface, it can help to wire a mask that rings and flags those occlusions into the white “occlusion mask” input of the Planar Tracker. Doing so lets the Planar Tracker disregard detail that would otherwise cause trouble. With the Hybrid Tracker, supplying a mask to cope with occluding objects is all but required, whereas with the Point Tracker the advice is to attempt the track with no mask first. 5 If you need to, drag the playhead back onto the reference frame, which here was the first frame. Then press the Track To End button and let the track finish.

### The Analyze buttons of the Planar Tracker

While the clip tracks, track markers and trails (assuming they're switched on in the Options tab of the Inspector) become visible, showing you how much detail feeds the track along with the direction of motion under analysis.

As the track runs, the track markers and trails on display let you gauge how it's progressing 6 With the track finished, run through the clip to eyeball it and judge its accuracy. Does it cling to the surface? Flipping over to Steady mode is useful here, since scrubbing the clip in Steady mode surfaces any unwanted motion in the track right away. 7 Because we're after a match move, press the Create Planar Transform button to spit out a Planar Transform node that will automatically transform images or masks so they ride along with the analyzed motion of the plane you tracked.

Pressing Create Planar Transform to spawn a node that will go on to transform separate images or masks

Here, the Planar Transform node lands after a pairing of Background and Paint nodes that are busy slapping some painfully fashionable tech-jargon graffiti onto the wall. The Planar Transform automatically transforms the Paint node's output wired into its background input so it tracks the wall's movement. Placing the PlanarTransform node downstream of a Paint node so it match moves onto the background image, then joining the two through a Merge node The upshot is a flawless match move of the bogus graffiti wedded to the wall in the original clip.

The end product, with the paint layer cleanly match moved onto the background TIP: Should you wish to composite see-through paint strokes onto the wall, or pair Apply modes with paint stroke, you can hook a Paint node up to a Background node dialed to 100 transparency. The image you get back is simply whatever paint strokes you lay against transparency, and it composites easily.

### Tips for Choosing Good Planes to Track

You specify the region to track by drawing a polygon on the reference frame. Be sure the region you pick sits on a genuinely planar surface within the shot. Now and then a region that's only roughly planar can serve. Broadly, the less planar the surface is, the worse the track that results. As a rough guide, the more pixels packed into the pattern, the better the track turns out. Concretely, that means on the reference frame, the pattern you mean to track should:

- Be as large as possible.
- Be as much in frame as possible.
- Be as unoccluded as possible by any moving foreground objects.
- Sit at the biggest scale it reaches (for instance, with a road sign coming toward camera, favor a later

frame in which it measures 400 x 200 pixels over one at just 80 x 40 pixels).

- Carry as little distortion as possible (for instance, as the camera circles a flat stop sign, lean toward a

frame where the sign sits face-on parallel to the camera instead of one where it leans at a steeply oblique angle). When the pattern holds too few pixels or lacks enough trackable features, trouble can follow in the track that results — jitter, wobble, and slippage. At times, stepping down to a simpler motion type can rescue the situation.
