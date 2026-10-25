# Dynamic zoom and composite

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the inspector in the cut page.
[Chapter index](INDEX.md) / [Previous section](the-inspector-and-video.md) / [Next section](retime-and-scaling-and-super-scale.md)
<a id="source-composite"></a> <a id="source-dynamic-zoom"></a> <a id="source-lens-correction"></a> <a id="source-speed-change"></a> <a id="source-stabilization"></a> <a id="source-the-composite-section-of-the-video-inspector-panel"></a> <a id="source-the-speed-change-controls-in-the-video-inspector"></a> <a id="source-the-stabilization-section-of-the-video-inspector-panel"></a>

### Dynamic Zoom

Within the Video Inspector panel, the Dynamic Zoom area's controls, which start off turned off, give you a fast, easy way to do pan and scan moves that ease into or back out of a clip. Toggling the Dynamic Zoom group on brings up two Inspector controls that operate in tandem with the Dynamic Zoom onscreen adjustment controls. To read more about working with the Dynamic Zoom controls, refer to Chapter 50, “Compositing and Transforms in the Timeline.”

- Dynamic Zoom Ease: Sets the way the movement these controls produce ramps up. The choices are Linear, Ease In, Ease Out, and Ease In and Out.
- Swap: Pressing this button flips the opening and closing transforms behind the dynamic zoom effect.

### Composite

### The Composite section of the Video Inspector panel

When clips are layered above other clips on the Timeline, Composite modes let you blend them together.

- Composite Mode: Picks which kind of composite mode blends the layered clips together. The default of “Normal” signifies that no compositing mode is in effect.

To read more about Composite Modes, refer to Chapter 50, “Compositing and Transforms in the Timeline.” CUT

- Opacity: On top of whatever compositing is already happening, this slider raises or lowers

a clip’s transparency.

### Speed Change

Right inside the Video Inspector’s Speed Change controls you can retime your clip. One advantage of doing it here is that the controls show up on both the Cut and Edit pages.

### The Speed Change controls in the Video Inspector

- Direction: Picks the clip’s intended playback, whether forward, backward, or freeze frame.
- Speed %: Adjusting this slider changes the clips motion on a percentage basis.

This value can be keyframed.

- Frames Per Second: Moving this slider alters the clip’s motion by raising or lowering the number of frames per second at which the clip plays back. You can keyframe this value.
- Duration: Right here you can pick exactly how long the clip should run by entering a precise duration in HH:MM:SS:FF format. The clip’s speed then adjusts on its own so that every frame plays within that precise span of time.
- Ripple Sequence checkbox: Turn this checkbox on if you want the upcoming speed change to ripple the Timeline, shoving or dragging every clip after the current one to make room for that clip’s altered length.
- Pitch Correction checkbox: Ticking this box applies pitch correction to the clip’s audio, so that as the audio length stretches or compresses to track the picture speed, it still sounds natural. Keep in mind that pitch correction over big speed shifts may not hold up as well as pitch corrections done on small speed shifts.

### Stabilization

### The Stabilization section of the Video Inspector panel

Unwanted camera shake inside a clip can be smoothed or even fully steadied with these controls.

The analysis runs in a manner that keeps the motion of separate subjects in the

frame intact, along with the intended path of any wanted camera movement, all while ironing out the jitter.

These controls are the very same stabilizer controls found in the Color page’s Tracker palette (without the tracker graph), and the stabilization analysis that results is mirrored over to the Color page, where the data can be viewed on the graph whenever needed.

Three choices in a pop-up menu set how the chosen clip gets analyzed and reshaped while it is stabilized. Pick one before you press the Stabilize button above, because your pick alters the way the image analysis runs. Should you switch to a different choice, you have to click the Stabilize button once more to reanalyze the clip.

- Perspective: Enables perspective, pan, tilt, zoom, and rotation analysis and stabilization.
- Similarity: Turns on pan, tilt, zoom, and rotation analysis plus stabilization, for cases where perspective analysis brings about unwanted motion artifacts.
- Translation: Turns on pan and tilt analysis plus stabilization alone, for cases where X and Y stabilization on its own delivers results you can accept.

How forcefully the chosen clip is stabilized can be tuned with the remaining controls.

- Stabilization Toggle: Acting as the on/off switch for the Stabilization controls, this lets you flip stabilization off and on so you can weigh the stabilized image against the unstabilized one.
- Camera Lock: Switching this checkbox on shuts off Cropping Ratio and Smooth and lets the stabilizer concentrate on wiping out every bit of camera motion in the shot, aiming to produce a locked shot.
- Zoom: With this checkbox on, the image is enlarged by just enough of a percentage to wipe out the blanking (black edges) left behind by warping and transforming the image to cancel unwanted camera movement. The lower you set Cropping Ratio, the harder DaVinci Resolve has to zoom into an image to clear those blanked edges. Turn this off and the image stays at its original size, so whatever blanking creeps into the frame is sent out with the image, on the premise that you’ll have dedicated compositing artists handle the blanking by painting in the missing image data through more elaborate means. You can also keep this checkbox off if you intend to animate the Input Sizing Zoom parameter to push into and out of a stabilized shot, clearing blanking only at the spots it shows up and using no more zoom than each part of the shot demands.
- Cropping Ratio: By deciding how much blanking or zooming you’ll tolerate in trade for canceling unwanted motion, this value caps how aggressively the stabilizer works. At a setting of 1.0 no stabilization is applied at all. Stepping the value progressively lower turns on more aggressive stabilization. After changing this value you must click the Stabilize button again to reanalyze the clip.
- Smooth: Applies mathematical smoothing to the analyzed data the clip is stabilized with, permitting camera movement in the shot while clearing out unwanted jitter. Lower settings smooth less, letting more of the original camera move’s personality come through, whereas higher settings smooth the shot more aggressively. After changing this value you must click the Stabilize button again to reanalyze the clip.
- Strength: Acting as a multiplier, this value sets how tightly the stabilization track is used to remove motion from a shot under the current analysis. At a value of 1, stabilization is at its peak. Because certain clips can feel more natural with looser stabilization, picking a figure below 1 allows a slice of the original camera movement to remain visible. Zero (0) shuts stabilization off entirely. As a further tip, you can flip the stabilization by selecting –1 when pasting a stabilization analysis from a different clip to run a match move keyed to the scene’s overall motion, and you can apply a negative value either under 0 or above –1 to under- or overcompensate while inverting the stabilization, faking the parallax effect where foreground and background planes travel together but at differing rates.

### Lens Correction

Within the Video Inspector panel, the Lens Correction area (offered only in Resolve Studio) provides two controls that let you fix lens distortion in the picture, or introduce lens distortion of your own.

- Analyze: Automatically scans the frame currently under the Timeline playhead for edges bent by a wide angle lens. Pressing the Analyze button shifts the Distortion slider to apply a correction for you. If the clip you’re analyzing is an especially tough one, a progress bar shows up to tell you how long it will run.
- Distortion: Dragging this slider rightward lets you manually warp the picture to straighten out the bent regions that wide angle lenses tend to cause. If pressing the Analyze button left you with an overcorrection, dragging the slider leftward lets you ease off the automatic adjustment until the image looks right.
