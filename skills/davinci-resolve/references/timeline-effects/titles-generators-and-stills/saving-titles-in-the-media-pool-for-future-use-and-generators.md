# Saving titles in the media pool for future use and generators

Version: DaVinci Resolve 20.3 Reference Manual. Context: Titles generators and stills.
[Chapter index](INDEX.md) / [Previous section](title-generator-shared-settings.md) / [Next section](fusion-generators.md)
<a id="source-itu-r-bt2111-1-color-bar-generators"></a> <a id="source-saving-titles-in-the-media-pool-for-future-use"></a> <a id="source-using-generators"></a>

### Saving Titles in the Media Pool for Future Use

When you've built a title in a style you'd like to reuse later—say a distinctively formatted lower third meant to seed each lower-third across your program—dragging any title out of the Timeline into the Media Pool stores it there as its own clip. Title clips in the Media Pool show a thumbnail previewing the text they hold. If you've keyframed any animated text or video adjustments, those keyframes ride along with this clip too. Once stored in the Media Pool, text generators open in the Source Viewer and edit just like any other clip.

A text generator saved as a clip in the Media Pool

### Using Generators

Generators—Solid Color aside—offer no editable parameters beyond the Composite, Transform, Cropping, and Dynamic Zoom parameters standard on every clip. On top of that, generators carry a Display Name field in the Inspector letting you hand a given clip a custom name that surfaces in the Timeline. Gliding your pointer across any thumbnail in the Generators tab previews the various video generators bundled with DaVinci Resolve. To bring a generator into your timeline, simply seize the thumbnail of the one you want and drop it onto your Timeline on the Edit page, or onto either the upper or lower Timelines on the Cut page. These generators are on offer:

- 10 Step: A grayscale ramp broken into 10 steps running black to white.
- 100mV Steps: A grayscale ramp broken into segments of exactly 100mV apiece.
- BT.2111 Color Bar HLG Narrow: Reach for these bars when your HDR timeline runs a Hybrid Log Gamma

curve (HLG). This one turns up most in broadcast for its easy backward compatibility with SDR televisions.

- BT.2111 Color Bar PQ Full: Though PQ Full belongs to the Rec. 2100 (BT.2100) specification, it isn't widely used right now. Pick this setting only when you know you need it.
- BT.2111 Color Bar PQ Narrow: Reach for these bars when your HDR timeline runs a format carrying a PQ gamma curve (DolbyVision or HDR10, that is). This one turns up most for video streaming services and Blu-ray discs.
- EBU Color Bar: For PAL-using countries, a set of color bars at a 1.77:1 aspect ratio.
- Four Color Gradient: A gradient blending four different colors at each corner of the frame. You

can shift the Center X and Center Y parameters to move the point where all four colors blend together, and you can swap the four colors showing at each corner via the matching color parameters.

- Grey Scale: A plain grayscale ramp running black to white.
- SMPTE Color Bar: For NTSC-using countries, a refreshed set of color bars at a 1.77:1 aspect ratio.
- Solid Color: A plain fullscreen color generator. A Color parameter lets you pick what color this generator puts out.
- Window: A plain white-on-black shape generator, defaulting to a white rectangle over a black background.
- YCbCr Ramp: A gradient built to test the Y'CbCr signal.

### ITU-R BT.2111-1 Color Bar Generators

For HDR video, DaVinci Resolve now bundles a Color Bar Generator following the ITU-R BT.2111-1 specification. Reach for these color bars whenever you're calibrating, analyzing, or mastering a Rec. 2100 (BT.2100) HDR signal. Saturation on these new color bars is pinned at 100% up top, dropping to 75% through the middle section. Down in the lower corners they also carry Rec. 709 (BT.709) color bars, keeping things compatible with HD SDR signals. Levels people reference most often are flagged on the image below. You'll find the full color bar specification over on the ITU's web site: https://www.itu.int/rec/R-REC-BT.2111/en.

The BT.2111-1 color bars together with a handful of the levels referenced most

The BT.2111-1 color bars shown on the Vectorscope, landing on their targets at 100% levels around the outside and 75% levels toward the middle, the Rec. 709 bars meanwhile sitting in the interior
