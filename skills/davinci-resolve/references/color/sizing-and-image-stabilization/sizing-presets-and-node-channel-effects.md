# Input and output sizing presets and node sizing for channel and paint effects

Version: DaVinci Resolve 20.3 Reference Manual. Context: Sizing and image stabilization.
[Chapter index](INDEX.md) / [Previous section](color-sizing-modes-and-processing-order.md) / [Next section](analyze-controls-and-interactive-mode-controls.md)
<a id="source-before-and-after-panning-the-green-channel"></a> <a id="source-example-1"></a> <a id="source-example-2"></a> <a id="source-image-stabilization-in-the-tracker-palette"></a> <a id="source-input-and-output-sizing-presets"></a> <a id="source-stabilizer-parameters-and-controls"></a> <a id="source-the-classic-stabilizer-mode-of-the-tracker-palette"></a> <a id="source-the-default-stabilizer-controls"></a> <a id="source-using-node-sizing-for-channel-and-paint-effects"></a> <a id="source-using-the-classic-stabilizer"></a> <a id="source-using-the-stabilizer"></a>

### Input and Output Sizing Presets

When you keep reaching for the same Input or Output Sizing settings, you can stash them as presets so they’re easy to call back. As an example, if there’s a batch of input settings you use to resize a clip of a certain format so it fits the current project, you can store it as a preset to pull up whenever you like.

- Preset drop-down menu: Opens up every preset presently stored within the current project library.
- Delete Preset: To remove a preset, pick it out of the drop-down menu, press the trash can button, then press OK.
- Save As New Preset: To stash a preset, dial in whatever settings tweaks you need, then press the plus button. Once the Format Preset dialog shows up, type a name, confirm the settings are right, then press Save in the Format Preset window.
- Update Preset: To revise a preset, load the one you want to revise, make whatever changes you need, then press Update in the Format Preset window.

The Input and Output Sizing modes hold separate presets. You can reach either preset set through the “Override input scaling” and “Override output scaling” drop-down menus sitting in the Image Scaling project setting menu.

### Using Node Sizing for Channel and Paint Effects

Node Sizing lets you lay down separate sizing tweaks on a per-node basis. Every Node Sizing tweak inside a grade stacks up, and any keyframing applied to Node Sizing parameters is held in that node’s Node Format keyframe track within the Keyframe Editor. Two solid examples of Node Sizing are realigning color channels one at a time together with the Splitter/Combiner nodes, or copying windowed regions of an image by shifting them around the frame.

### Example 1

Putting node sizing to work on separate color channels: 1 Choose Color > Nodes > Add Splitter/Combiner Node to drop this node structure into the current grade. 2 Pick whichever of the three Corrector nodes wired between the Splitter and Combiner nodes maps to the color channel you mean to transform. 3 Open the Sizing palette, pick Node Sizing from the mode drop-down, and reach for the Sizing parameters to transform that channel however you need. As an example, with an old video clip whose color components are misaligned, you could pan a misaligned channel left or right to try to tighten up its alignment.

Dropping in the Splitter/Combiner nodes so Node Sizing can act on separate color channels

### Before and after panning the green channel

### Example 2

Putting Node Sizing to work copying a windowed patch of an image to hide a blemish: 1 Make a new node. 2 Open the Window palette, build a Circular window, then shrink it and move it so it wraps around a feature you want gone. 3 Open the Tracking palette and track the window so it follows the feature being removed. 4 Once the track is finished, shift the window over to a neighboring patch of clean detail right beside the feature you want gone. This is the part of the image you’ll copy and lay over the unwanted feature. 5 Now open the Sizing palette, pick Node Sizing from the mode drop-down, tick Key Lock, and reach for the Sizing parameters to slide a copy of the windowed area on top of the unwanted feature.

Before/after where Node Sizing clones a patch of the image so a plant hides the actor and yields a clean background Once you’re finished, running through the clip should reveal that the copied patch of the image keeps tracking the feature you want gone.

### Image Stabilization in the Tracker Palette

The Tracker palette’s Image Stabilization mode lets you smooth out, or even fully steady, unwanted camera motion inside a clip. Its analysis runs in a way that holds onto the motion of separate subjects within the frame, along with the overall heading of any wanted camera move, all while ironing out the unsteadiness.

### Using the Stabilizer

DaVinci Resolve runs an advanced stabilizer that can both warp and translate to cut unwanted shaking in a clip, taking over from the classic stabilization tools that used to be on hand (those tools remain available should you need particular capabilities of the older toolset, and a later section covers them). One press of the Stabilize button analyzes the currently selected clip and stabilizes it automatically using a blend of warping and image translations.

### The default Stabilizer controls

### Stabilizer Parameters and Controls

The default settings give good results in most cases, yet there are ways to tailor stabilization when unusual problems crop up. A drop-down menu offers three different choices that govern how the chosen clip is analyzed and reshaped as it’s stabilized. You have to pick a choice first, ahead of pressing the Stabilize button, because the choice you make alters how the image analysis runs. Switch to another choice and you have to press the Stabilize button once more to reanalyze the clip.

- Perspective: Enables perspective, pan, tilt, zoom, and rotation analysis and stabilization.
- Similarity: Turns on pan, tilt, zoom, and rotation analysis plus stabilization, for cases where

perspective analysis brings about unwanted motion artifacts.

- Translation: Turns on pan and tilt analysis plus stabilization alone, for cases where X and Y

stabilization on its own gives you results you can accept.

- Camera Gyro: When your footage comes off a Blackmagic Cinema Camera fitted with a gyroscope, this

choice turns up in the drop-down menu. You can steady the footage using the movement logged by the internal gyro baked into the clip. How forcefully the chosen clip gets stabilized is set by the remaining controls.

- Bypass Stabilization: This checkbox lets you flip stabilization off and on so you can weigh the stabilized image against the unstabilized one.
- Cropping Ratio: By spelling out how much blanking or zooming you’ll put up with in trade for clearing unwanted motion, this value caps how hard the stabilizer pushes. Set it to 1.0 and no stabilization is applied. Stepping it progressively lower switches on more aggressive stabilization. After changing this value you have to press the Stabilize button once more to re-analyze the clip.
- Smooth: Applies mathematical smoothing to the analyzed data the clip is stabilized with, leaving camera motion in the shot in place while clearing out unwanted jitter. Lower values smooth less, letting more of the original camera move’s character come through, whereas higher values smooth the shot more aggressively. After changing this value you have to press the Stabilize button once more to reanalyze the clip.
- Strength: Acting as a multiplier, this value lets you set how tightly the stabilization track is used to clear motion from a shot under the current analysis. At a value of 1.00, stabilization peaks. Because certain clips can feel more natural with looser stabilization, picking a figure under 100 leaves a slice of the original camera motion visible. Zero (0) shuts stabilization off entirely. As a further tip, you can flip the stabilization around by

picking –1.00 when pasting a stabilization analysis from a different clip to run a match move keyed to the scene’s overall motion, and you can apply a negative value either below or above –1.00 to under- or overcompensate while inverting the stabilization, faking the parallax effect where foreground and background planes travel together yet at differing rates.

- Camera Lock: Switching this checkbox on shuts off Cropping Ratio and Smooth and lets the stabilizer concentrate on wiping out every bit of camera motion in the shot, aiming to produce a locked shot.
- Zoom: With this checkbox switched on, the image is enlarged by enough of a percentage to clear the blanking (black edges) left behind by warping and transforming the image to cancel unwanted camera motion. The lower Cropping Ratio is set, the more DaVinci Resolve has to zoom into an image to clear those blanked edges. Switch this off and the image isn’t zoomed at all, so whatever blanking creeps into the frame goes out alongside the image, on the premise that you’ll have dedicated compositing artists handle clearing that blanking by painting in the missing image data through more elaborate means. You can also keep this checkbox off if you mean to animate the Input Sizing Zoom parameter to push into and out of a stabilized shot, clearing blanking only at the spots it shows up, using no more zoom than each part of the shot demands.

### Using the Classic Stabilizer

The “classic” image stabilizer controls found in DaVinci Resolve version 12.5 and earlier are still on hand; just pick “Classic Stabilizer” from the Tracker palette’s option menu. Classic image stabilization in DaVinci Resolve runs in three steps. First you analyze the clip. Second you settle on the Stabilization settings you’d like to use. Third you press Stabilize to work out the result. As you analyze the clip, you can go with the default Cloud Tracker, which on its own rounds up as many trackable points as it can across the image and figures stabilization from all of them, or you can switch to the Point Tracker, which lets you set one or more individual crosshairs by hand on image features you pick. To learn more about putting the Point Tracker to work for window tracking, turn to Chapter 140, “Motion Tracking Windows.”

### The Classic Stabilizer mode of the Tracker palette

Much as with object tracking, you can pick which facets of motion to stabilize, but that has to happen before you run the initial image analysis.
