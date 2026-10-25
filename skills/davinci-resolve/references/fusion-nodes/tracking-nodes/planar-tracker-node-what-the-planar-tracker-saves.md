# Planar tracker node what the planar tracker saves

Version: DaVinci Resolve 20.3 Reference Manual. Context: Planar tracker node.
[Chapter index](INDEX.md) / [Previous section](camera-tracker-color.md) / [Next section](planar-tracker-node-controls.md) / [Continue Planar Tracker Node PTRA / Track Mode](planar-tracker-node-controls.md)
<a id="source-a-typical-planar-tracker-workflow"></a> <a id="source-basic-node-setup"></a> <a id="source-controls-tab"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-planar-tracker-node-ptra"></a> <a id="source-the-planar-tracker-controls-tab"></a> <a id="source-the-planar-tracker-node"></a> <a id="source-what-the-planar-tracker-saves"></a>

### Planar Tracker Node [PTRA]

### The Planar Tracker node

The Planar Tracker node exists to tackle a match-moving challenge that turns up all the time in post-production. Picture live-action footage holding a flat surface — a license plate or a road sign, say — where you need fresh numbers on the plate or a different city’s name on the sign. The wrinkle is usually that the camera is on the move during the shot, so the plate or sign keeps shifting perspective. Simply compositing a new license plate over the old one will not do unless you account for those perspective distortions. One slow route would be to reach for a Corner Pin node and hand-keyframe all four corners. The Planar Tracker takes that keyframing off your hands, following a flat surface’s perspective distortions through time. It then lays that tracking data, along with the very same perspective distortions, onto a separate foreground. For deeper guidance on the Planar Tracker, turn to Chapter 83, "Planar Tracking," in the DaVinci Resolve Reference Manual, or to Chapter 23 in the Fusion Reference Manual.

TIP: Working with a Planar Tracker also means recognizing when to quit and retreat to Fusion’s Tracker node or to keyframing things by hand. Certain shots just will not track, or the track that comes out is plagued by too much jitter or drift. As a time-saver in the artist’s kit the Planar Tracker earns its place, yet even though it handles most shots, it is not a 100% solution.

### What the Planar Tracker Saves

The Planar Tracker writes the finished final track into the composition on disk, but it leaves out the temporary tracking information — things like the individual point trackers (unlike the Camera Tracker, which does keep the individual point trackers). A few things follow from that:

- Save and reload a comp that holds a Planar Tracker node and the point trackers vanish from the viewer.
- You may be unable to pick tracking back up once a comp with a Planar Tracker node has been saved and reopened — and that holds for auto saves as well, which is why finishing all your planar tracking in a single sitting is wise.
- Composition file sizes stay sensible (there are cases where a Planar Tracker would otherwise spit out hundreds of megabytes of temporary tracking data).
- Comps save and load more quickly and feel more responsive.

### Inputs

Four inputs sit on the Planar Tracker: Background: This orange background image input takes a 2D image carrying the flat surface you mean to track. Corner Pin 1: The green corner pin 1 input takes a 2D image to be laid on top of the background; there can be several such inputs, named Corner Pin 1, Corner Pin 2, and so on. Occlusion Mask: The white occlusion mask input serves to block out regions that need no tracking — wherever this mask reads white, nothing is tracked. For instance, someone walking in front of and hiding parts of the pattern could throw the tracker off, so a quick, rough rotomask drawn around that person tells the tracker to skip the masked-out parts. Effect Mask: The blue input takes a mask shape made from polylines, basic primitive shapes, paint strokes, or bitmaps out of other tools. Wire a mask into it and the Planar Tracker’s output is confined to particular areas.

### Basic Node Setup

A bare-bones Planar Tracker arrangement needs only two nodes: a MediaIn feeds the background input, while the Planar Tracker sits on its own branch apart from the rest of the node tree. After tracking wraps up, you should spin off a Planar Transform node to put the planar tracking data to work.

A Planar Tracker may be set apart on a branch all its own within the node tree.

### A Typical Planar Tracker Workflow

Here is how the Planar Tracker workflow unfolds, step by step: 1 Remove lens distortion: The heavier the lens distortion in your footage, the more the finished track will slip and wobble. 2 Connect footage: Wire a Loader or MediaIn node holding a flat surface into the orange background input, then bring the Planar Tracker node up in a viewer. 3 Select a reference frame: Jump to a frame where the flat surface you want to track is clear of occlusion and press the Set button to make it the reference frame. 4 Choose the pattern: With the onscreen controls showing in the viewer, trace a polygon around the flat surface you intend to track — this is the so-called “pattern.” Usually a rectangle does the job, though any closed polygon will work. The pixels inside that boundary become the pattern hunted for across the remaining frames. Keep in mind the pattern has to be drawn on the reference frame, and do not mix it up with the region you corner pin (which is always four-cornered and gets specified separately in Corner Pin mode). 5 Adjust render range: Over in the Keyframes Editor, set the render range so it lines up with the span of frames where the flat surface shows.

6 Adjust track options: The settings you will tweak most often are Tracker, Motion Type, and Track Channel. 7 Mask out occluders: Should moving objects partly hide the flat surface, consider wiring an occlusion mask into the Planar Tracker. With the Hybrid tracker, handing it a mask to cope with occluding objects is strongly advised; with the Point tracker, you are better off attempting the track without a mask first. 8 Track: Hit the Go button to jump back to the reference frame, press the Track To End button, and let the track finish. Hit Go once more to land on the reference frame again, press the Track To Start button, and again wait for completion. Bear in mind that, unlike in a Camera Tracker, the tracks shown in the viewer can be neither selected nor deleted. 9 Check track quality: Look the track over to judge its accuracy — does it cling to the surface? Flipping to Steady mode can make this easier to see. 10 Use the track: From here you will most often build a Planar Transform node out of the Inspector and use it to push the tracked perspective distortion onto masked images. When the image you are feeding the tracking data into is a full-frame, unmasked clip, the Steady, Corner Pin, and Stabilize operation modes of the Planar Tracker are available to you.

### Inspector

### The Planar Tracker Controls tab

### Controls tab

On the Controls tab you find the settings that decide how the Planar Tracker is put to use, fix the reference frame, and kick off the track. Operation Mode The Operation Mode menu picks what the Planar Tracker node is for. The Planar Tracker offers four operating modes:

- Track: Serves to single out a flat surface and follow how it moves through time. From there you can build a Planar Transform node that draws on this data to match move some other clip in a number of ways.
- Steady: Having studied a flat surface, this mode strips every bit of motion and distortion off it, usually as a setup for a paint or roto task, before the clip is later “unsteadied” to bring its motion back.
- Corner Pin: Once a flat surface has been analyzed, this mode works out a matching perspective distortion, applies it to a foreground image you feed into the Planar Tracker node’s foreground input, and lays that on top of the tracked footage.
- Stabilize: After examining a flat surface, this mode lets you smooth out a clip’s translation, rotation, and scale across time — handy for ridding a clip of unwanted shake while keeping the deliberate camera motion intact.

Those final three modes — Steady, Corner Pin, and Stabilize — all feed on the tracking data that Track mode generates. NOTE: You cannot run the operations together. Corner Pin and Stabilize, for one, cannot happen simultaneously, and you cannot track while corner pinning is active. Reference Time The Reference Time sets the frame on which the pattern gets outlined; it is likewise the moment from which tracking starts. You cannot revise the reference frame after it is set without wiping out every bit of existing tracking information, so scrub the footage you mean to track and decide with care. Picking the reference frame thoughtfully is what gives you the best-quality track. To set one, park the playhead on a fitting frame and click the Set button to lock it in. Pattern Polygon You mark which slice of the image to track by drawing a polygon on the reference frame. Normally the moment you drop in a Planar Tracker node you are set to begin drawing a polygon in the viewer, so it is best to get on with it straight away. As you decide where to draw, make sure the region you pick belongs to a genuinely flat surface in the shot. In a pinch a roughly flat region will serve, but the less flat the surface, the worse the track turns out. The general rule is that more pixels in the pattern mean a better track. Put concretely, the reference frame pattern ought to be:

- As large as possible.
- As much in frame as possible.
- As unoccluded as possible by any moving foreground objects.
- Captured as big as it gets (for instance, with a road sign coming toward camera, favor a later frame

where it measures 400 x 200 pixels over one where it is only 80 x 40 pixels).

- Fairly free of distortion (for example, as the camera circles a flat stop sign, lean toward a

frame in which the sign sits face-on and parallel to the camera, not one where it is sharply angled). Too few pixels in the pattern, or too few trackable features, can breed trouble in the track — jitter, wobble, and slippage among them. Stepping down to a simpler motion type sometimes eases that. Once your pattern is drawn, a group of Pattern parameters lets you transform and invert the polygon you made, if the need arises.
