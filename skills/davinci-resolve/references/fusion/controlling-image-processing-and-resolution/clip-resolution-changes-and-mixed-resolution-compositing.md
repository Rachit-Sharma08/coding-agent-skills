# Changing the resolution of a clip and compositing with different resolution clips

Version: DaVinci Resolve 20.3 Reference Manual. Context: Controlling image processing and resolution.
[Chapter index](INDEX.md) / [Previous section](fusion-image-pipeline-and-source-media.md) / [Next section](frame-format-and-mixed-color-depth.md)
<a id="source-changing-the-resolution-of-a-clip"></a> <a id="source-color-bit-depths"></a> <a id="source-compositing-with-different-resolution-clips"></a> <a id="source-configuring-default-color-depth-preferences"></a> <a id="source-downscale-clip-compositions-to-timeline-resolution"></a> <a id="source-editcut-page-lens-correction"></a> <a id="source-editcut-page-transforms"></a> <a id="source-fusion-clip-compound-clip"></a> <a id="source-fusion-page-timeline-resolution"></a> <a id="source-fusion-timeline-sizing-for-fusion-and-compound-clips"></a> <a id="source-fusion-transforms"></a> <a id="source-input-sizing"></a> <a id="source-output-sizing"></a> <a id="source-setting-color-depth-in-fusion-studio"></a> <a id="source-sizing-between-davinci-resolve-pages"></a> <a id="source-sizing-with-compound-and-fusion-clips"></a> <a id="source-super-scale"></a> <a id="source-the-loaders-inspector-color-bit-depth-settings"></a> <a id="source-timeline-hd-resolution"></a> <a id="source-uhd-source-media-1"></a> <a id="source-understanding-integer-vs-float"></a>

### Changing the Resolution of a Clip

Where your comp draws on a single image, the pixel output resolution can be altered through a few different routes. The Resize, Scale, and Crop nodes are three frequently used tools for changing a clip's pixel resolution. A fourth, Letterbox, sees less use but likewise shifts a clip's pixel resolution. All four of these nodes reside in the Transform category of the Effects library, and Resize additionally appears on the toolbar.

- Crop: Fixes the node's output resolution by pairing X and Y size with X and Y offset to trim the frame down to whatever dimensions you're after. Because Crop discards pixels from the image, reaching for a Transform node afterward to reposition the image leaves those pixels unavailable.
- Letterbox: Fixes the node's output resolution by laying horizontal or vertical black edges wherever they're needed to shape the frame size and aspect ratio.
- Resize: Fixes the node's output resolution in terms of absolute pixels.
- Scale: Fixes the node's output resolution as a relative percentage of the current input

image size.

TIP: When you want to rescale and reposition a frame yet leave a clip's pixel resolution untouched, turn to the Transform node.

### Compositing with Different-Resolution Clips

As you composite images of differing resolutions through the Merge node, it's the image feeding the orange background input that settles the Merge node's output resolution. Frequently the simplest way to govern comp resolution from the outset is to wire a node holding your intended output resolution into that orange background input on the Merge node. A Background node tends to be the pick here, since it draws very little from your system.

A Background node fixes the merge's output resolution The Background node establishes the output size, and a foreground image bigger than that gets cropped.

A Background node made at 1280 x 720 crops the larger foreground. Even so, the whole pixel content of that larger foreground stays on hand for repositioning.

### Downscale Clip Compositions to Timeline Resolution

Should your machine be laboring under your Fusion comps, switch on Project Settings > Fusion > Downscale Timeline Resolution for Timeline Clip Compositions. With it active, your clips are scaled down to the timeline resolution before any processing happens. That lets you, for one, handle 4K original footage in an HD timeline while carrying only HD-sized processing overhead. NOTE: EXR files stay un-downscaled no matter the Downscale Timeline Resolution for Timeline Clip Composition settings, on account of the potentially enormous number of information channels they may hold.

### Sizing Between DaVinci Resolve Pages

How sizing operations are ordered across DaVinci Resolve pages carries a touch more subtlety. Knowing which sizing operations land inside the Fusion page versus afterward matters, because it tells you which effects reshape the image fed into the Fusion page and which reshape what the page puts out. Lens correction, for instance, isn't strictly a sizing operation, but it still alters how the image enters your Fusion composition. The Edit or Cut page stabilization function, by contrast, is an effect occurring past the Fusion page, so it never shows up in the composition you're building. Across the various DaVinci Resolve pages, the sequence of sizing effects can be laid out this way:

### Super Scale

### Edit/Cut Page Lens Correction

### Fusion Transforms

### Edit/Cut Page Transforms

### Input Sizing

### Output Sizing

### Sizing with Compound and Fusion Clips

One more route for reshaping resolution before clips pass from the Edit page over to the Fusion page is to build a compound clip or a Fusion clip. Either kind shifts the working resolution of the constituent clips to align with the Timeline resolution. Stack two 4K clips one atop the other in an HD timeline, say, and forming a compound or Fusion clip rescales them to HD. The individual 4K clips' full resolution then isn't on offer in Fusion and is consequently passed to the Color page at the reduced size. To hold onto source clips' full resolution, carry just a single clip into the Fusion page from the Edit or Cut page Timeline, then draw the rest into the Fusion composition by way of the Media Pool. Naturally, when your clips are full HD and your timeline is full HD too, making a Fusion clip or compound clip leaves the resolution alone.

### UHD Source Media

### Timeline HD Resolution

### Fusion Clip Compound Clip

### Fusion timeline sizing for Fusion and Compound clips

### Fusion Page Timeline Resolution

### Color Bit Depths

Bit depth refers to the count of colors on offer in the palette from which an image is built. A larger bit depth means finer color precision in the image and, with it, richer color reproduction. That extra precision reveals itself most in gradients carrying delicate transitions. Gradients of lower bit depth pick up visible banding artifacts, while images of higher bit depth can render more colors, so banding artifacts grow scarce or vanish entirely. Inside DaVinci Resolve the Fusion page invariably processes images at 32-bit float bits per channel precision. In Fusion Studio, though, you may opt to process images at 8-bit integer, 16-bit integer, 16-bit float, or 32-bit float bits per channel. Staying at 16-bit float or 32-bit float always yields the finest quality, yet leaning on a lower bit depth can prove more efficient when your images start out in 8-bit or 16-bit integer formats.

### Understanding Integer vs. Float

As a rule, 8-bit integer color processing marks the lowest bit depth you'll meet among video formats. Images at 8-bit originate from older or consumer-grade gear such as mobile phones and camcorders. Push any sizable gamma or color correction onto 8-bit images and banding often grows more apparent. Stepping up to 16-bit integer color depth doubles the precision and clears away banding troubles. You can apply 16-bit integer processing to an 8-bit clip, but doing so won't lessen banding already baked into the original file, though it does help once you start piling further effects onto the clip. This seems like the ideal answer right up until you notice that plenty of digital cameras — the Blackmagic Design URSA Mini Pro among them — record in formats able to capture over-range values, with shadow regions under 0.0 and super highlights over 1.0, all of which get cut off at 16-bit integer. The 16-bit float color depth gives up a sliver of the precision found in ordinary 16-bit integer color depth in exchange for storing color values below 0 and above 1.0. Often termed half-float, 16-bit float turns up most commonly in the OpenEXR format and packs ample dynamic range for the bulk of film and HDR television work, all while demanding far less memory and processing time than full float, 32-bit images call for.

Holding onto over-range values lets you shift exposure without sacrificing highlights Working at 32-bit float copes with shadow regions under 0.0 and highlights over 1.0 much as 16-bit float does, only with a far wider span of precision and, alongside it, far heavier memory and processing demands.

### Setting Color Depth in Fusion Studio

As noted before, DaVinci Resolve always processes at 32-bit float bits per channel; even so, the Performance Mode setting in the User > Playback Preferences panel lets you spend less memory and still land more-than-acceptable results. Fusion Studio picks, on its own, whichever color depth best suits each file format. Pull in a JPEG file from disk, for instance, and the Loader's color depth is fixed at 8 bits per channel. Given that JPEG is an 8-bit format, loading it at a deeper color depth would mostly be a waste. Bring in a 16-bit TIFF and the color depth lands at 16 bits. A DPX file defaults to 32-bit float, whereas OpenEXR typically defaults to 16-bit float. That automatic per-format color depth can be overridden, however, through the settings in the Import tab of the Loader node's Inspector. Both the Loader's Inspector and the Inspector for images Fusion generates (text, gradients, fast noise, and so on) carry a Depth menu offering 8-bit, 16-bit integer, 16-bit float, and 32‑bit float.

### The Loader’s Inspector Color Bit Depth settings

### Configuring Default Color Depth Preferences

When set to default, the color depth pushes the tool to process according to whatever the Node Editor's Frame Format preferences hold. Those preferences establish a default color depth value that kicks in as a Generator tool joins the Node Editor. The preferences carry three drop-down menus for configuring color depth, each naming a separate color depth for the interactive session, for final renders, and for preview renders. For better performance while you build your comp, you might pin the Interactive and Preview depth at 8-bits per channel and leave final renders at 16-bit integer. That said, when the output of your final render is 16-bit float or 32-bit float, steer clear of the integer options for the interactive setting, since the finished results can diverge markedly from interactive previews left on integer options.
