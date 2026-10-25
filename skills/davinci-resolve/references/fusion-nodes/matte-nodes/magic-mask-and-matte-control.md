# Magic mask and matte control

Version: DaVinci Resolve 20.3 Reference Manual. Context: Magic mask, Matte control.
[Chapter index](INDEX.md) / [Previous section](luma-keyer-and-magic-mask.md) / [Next section](matte-control-controls.md) / [Continue Matte Control MAT / Matte Tab](matte-control-controls.md) / [Magic Mask MagM](luma-keyer-and-magic-mask.md)
<a id="source-basic-node-setup-1"></a> <a id="source-common-controls-1"></a> <a id="source-inputs-1"></a> <a id="source-inspector"></a> <a id="source-matte-control-mat"></a> <a id="source-matte-control-node-introduction"></a> <a id="source-matte-tab"></a> <a id="source-the-matte-control-node"></a> <a id="source-tracking-tab"></a>

### Tracking Tab

Picture each point you’ve set as a sticky eyedropper that samples whatever image overlaps it. The mask produced by every point’s combined reading of the image is generated live across each frame of the clip. So if the camera or the subject shifts, you’ll need to motion track or otherwise reposition each point so it travels with the motion, keeping the subject correctly recognized. You’ll also want to confirm that each point can analyze what it’s meant to, and switch off any points that, for whatever reason, can’t.

- Mode: A pair of options lets you weigh quality against performance. Faster generates a lower-quality mask more quickly, well suited to garbage matting. Better generates a higher-quality, more detailed mask that demands more from the processor.
- Point Mode: The primary controls for adding and removing points that define the mask:

Add Point: With the positive eyedropper icon you set a point (blue) in the Viewer flagging an area for inclusion in the mask. Subtract Point: With the negative eyedropper icon you set a point (red) in the Viewer flagging an area to leave out of the mask. Select Points: Lets you grab points that already exist in the viewer by drawing a bounding box around one or several. Selected points turn green. Delete Point: Removes whichever points are selected.

- Tracking Controls: These buttons govern the tracking direction, listed left to right:

Track Reverse: Tracks without stopping from the current frame all the way back to the clip’s start. Track Reverse One Frame: Tracks a single frame backward, then halts. Handy when you’re tracking frame-by-frame to watch how a particularly tricky bit of motion progresses. If something breaks, you can step back to the last frame where the point tracked the subject cleanly, then drag the point to a better spot with the pointer so it follows the subject correctly. If you must, work one frame at a time, nudging the point into a better position each time it fails to follow the feature you’re isolating with it. Track Forward Then Reverse: Starting at the current frame, this tracks right through to the clip’s end, then returns to the original tracking point and runs backward to the clip’s start. Stop Tracking: Halts tracking, for those moments when the track has a problem and you want to make a change. Track Forward: Tracks without stopping from the current frame all the way to the clip’s end. Track Forward One Frame: Tracks a single frame forward, then halts. Handy when you’re tracking frameby-frame to watch how a particularly tricky bit of motion progresses. If you must, work one frame at a time, nudging the point into a better position each time it fails to follow the feature you’re isolating with it.

- Clear Points: These buttons strip every point from the chosen range:

Current: Strips points from the frame under the playhead. Range: Strips points from the chosen render range. All: Strips every point from the whole clip.

- Go To Frame: These buttons jump the playhead to the chosen frame, listed left to right:

First Frame of Tracked Area: Sends the playhead to the first tracked frame in a range of tracked frames, getting ready to track backward when untracked frames sit at the clip’s start. Reference Frame: Sends the playhead to the frame where you first drew the points. Last Frame of Tracked Area: Sends the playhead to the last tracked frame in a range of tracked frames, getting ready to track forward when untracked frames sit at the clip’s end.

- Disk Cache: These buttons let you manage what gets held in the disk cache: Regenerate All: Rebuilds the disk cache. Clear: Wipes the frames in the current cache.
- Reference Time: The Reference Time fixes the frame where the initial points get drawn. It’s likewise the moment from which tracking starts. Once set, the reference frame can’t be moved without wiping out all the tracking information that already exists.
- Processed Frames: Shows the range of frames already tracked. Start is the earliest tracked frame and end is the latest tracked frame. You can’t edit these fields.

Post-Multiply Image Pick this option and the keyer multiplies the image’s color channels by the Alpha channel it generates for that image. This option is normally on and is enabled by default. Clear this checkbox and the image can no longer be treated as premultiplied when you merge it with other images. On the Merge node, reach for the Subtractive option in place of the Additive one. To read up on these Merge node settings, turn to Chapter 95, "Composite Nodes," found within DaVinci Resolve Reference Manual; its counterpart is Chapter 35 over in the Fusion Reference Manual.

### Matte Tab

The Matte tab fine-tunes the key’s alpha, taking into account any solid and garbage masks wired into the node. While working in the Matte tab, set the viewer so it shows the Alpha channel of Magic Mask’s final output.

- Filter: Picks the Filter used to blur the matte. Box Blur: This option lays a Box Blur effect over the whole image. It’s quicker than the Gaussian blur but yields lower quality. Bartlett: Bartlett lays down a gentler, anti-aliased blur filter. Multi-Box: Multi-Box stacks a box filter across several passes to mimic a Gaussian shape. With a moderate pass count (say, four), you can land a high-quality blur, frequently quicker than the Gaussian filter and with no ringing. Gaussian: Gaussian lays down a smooth, symmetrical blur filter using a refined constant-time Gaussian approximation algorithm. Fast Gaussian: Gaussian lays down a smooth, symmetrical blur filter using a refined constanttime Gaussian approximation algorithm. This mode is the default filter method.
- Blur: This blurs the matte’s edge with a standard, constant-speed Gaussian blur. Set it to zero and you get a crisp, cutout-style hard edge. The higher the value, the heavier the blur laid onto the matte.
- Erode/Dilate: This grows or shrinks the matte. Eroding the matte exposes more of the foreground input, whereas dilating it exposes more of the background input. Settings above 0.0 dilate the matte and settings below 0.0 erode it.
- Gamma: This drives the matte’s values up or down across the semitransparent regions. Pushing the value up makes the gray regions more opaque, and pulling it down makes them more transparent. Regions of the matte that are wholly black or white stay as they are.
- Threshold: Anything under the lower threshold turns black, or transparent, in the matte. Anything over the upper threshold turns white, or opaque, in the matte. Everything inside the range keeps its relative transparency values.
- Restore Fringe: This brings back the matte’s edge around the keyed subject. Keying often clips out the subject’s edge wherever there’s hair. Restore Fringe recovers that edge while keeping the matte solid.
- Invert Matte: Tick this checkbox and the image’s Alpha channel is inverted, so every transparent region turns opaque and every opaque region turns transparent.

Solid Matte Solid mattes are mask nodes or images wired into the node’s solid matte input. That solid matte goes straight onto the image’s Alpha channel. As a rule, solid mattes hold out keying wherever you need things to stay opaque — say, a person with blue eyes shot in front of a blue screen. Turning on Invert flips the solid matte before the source alpha takes it in. Garbage Matte A garbage matte, too, is a mask node or image wired into the node’s garbage matte input. That garbage matte goes straight onto the image’s Alpha channel. As a rule, the garbage variety strips out stray elements that resist keying, such as microphones and booms. They also serve to patch in regions that hold the key color but that you want to keep. You can’t blend garbage mattes of differing modes inside one tool. It’s common to place a Matte Control node downstream of a Keyer node to introduce a garbage matte whose effect is the reverse of the matte on the keyer. Turning on Invert flips the garbage matte before it merges with the source alpha.

### Common Controls

Settings Tab The Inspector’s Settings tab also appears in the other Matte nodes. These shared controls get a full write-up at this chapter’s close, under the “The Common Controls” section.

### Matte Control [MAT]

### The Matte Control node

### Matte Control Node Introduction

Keyer nodes exist to build an alpha channel on an image that lacks one. The Matte Control node serves to combine and reshape the alpha channels carried inside images, as well as masks made by masking tools. You’ll commonly drop this node in to copy a color channel or alpha channel from the foreground input onto the background input, or to merge alpha channels from the two images.

### Inputs

In the Node Editor, the Matte Control node carries four inputs. Background: This orange background input takes a 2D image that receives the foreground image’s alpha channel (or whatever other channel you want copied to the background). Foreground: This green foreground input takes a 2D image carrying an alpha channel (or some other channel) you want applied to the background image. Garbage Matte: This gray garbage matte input takes a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wiring a mask here makes the regions of the foreground/background combination inside the matte transparent. Solid Matte: This white solid matte input takes a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wiring a mask here makes the regions of the foreground/background combination inside the matte fully opaque. Effect Mask: This optional blue input looks for a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wiring a mask here confines the matte control to certain pixels. An effects mask gets applied to the tool once the tool has finished processing.

### Basic Node Setup

In the example below, the Matte Control node is wired to copy the foreground (green) input’s alpha channel onto the background (orange) input. What the Matte Control then outputs is an alpha-bearing image that serves, within the Merge node, as the foreground composite.

### Inspector

A Matte Control routing an alpha out of the foreground input and into the background input
