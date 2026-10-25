# Selecting and adjusting the high clip and RGB parade displays the clipped image

Version: DaVinci Resolve 20.3 Reference Manual. Context: Curves.
[Chapter index](INDEX.md) / [Previous section](hdr-curves-and-editable-splines.md) / [Next section](additional-controls-in-the-hue-and-sat-curves.md)
<a id="source-high-soft"></a> <a id="source-image-sampling-for-hue-and-sat-curves"></a> <a id="source-low"></a> <a id="source-low-soft"></a> <a id="source-rgb-parade-displays-the-clipped-image"></a> <a id="source-selecting-and-adjusting-the-high-clip"></a> <a id="source-the-hsl-curves"></a>

### Selecting and adjusting the high clip

### RGB Parade displays the clipped image

At its default spot no clipping happens, and image data you drive past 1023 on the internal scopes is held and carried through the image processing pipeline to the nodes that follow. As an example, across the next two screenshots, the highlights in the top one are blown out by lifting the gain sharply in Node 1. In the bottom screenshot, a later adjustment in Node 2 drops the gain and reclaims every one of those previously clipped values.

The image is clipped using the Gain control in Node 2

Whatever image data got clipped in Node 1 is reclaimed in Node 3 by dropping the Gain control. This shows how deliberately clipped data is preserved. That said, drag the High Clip slider leftward anywhere along a node tree — even by one single digit — and every bit of image data above the new clipping threshold is thrown away from that node onward. In the example below, the High Clip slider in Node 1 gets lowered. The result is that all the clipped image data is thrown away. So when Node 2 drops the gain, there’s no image detail left to reclaim, and all three channels show flattening.

Drop the High Clip slider on Node 1 and every bit of image data sitting above the fresh High Clip threshold is discarded for good. No node further along can bring that clipped data back.

### High Soft

What the High Soft slider sets is the threshold, beneath the clipping point, where highlights start compressing ahead of hard clipping. At unity, no soft clipping happens. Raise this value and more and more of the clipped highlight values get compressed rather than clipped, giving softer, more pleasant “glowing” highlights. IMPORTANT: Image data clipped “in camera” isn’t necessarily reclaimable with the Soft Clip controls, though there may be some held-back overhead in the super-white highlights of Y’CbCr-encoded video data.

### Low

What the Low Soft Clipping Point slider does is let you set the bottom signal level where the signal clips. Measured against the DaVinci Resolve internal video scopes, this defaults to a digital level of 0. Drag this slider rightward and the image’s shadows clip at a higher level — the result being lifted minimum levels, plus a lower-contrast image whose shadows turn lighter (milky, even).

### Low Soft

What the Low Soft slider sets is the threshold, above the minimum clipping point, where shadows start compressing ahead of hard clipping. At unity, no soft clipping happens. Drag this slider rightward and more and more of the clipped shadow values get compressed rather than clipped, giving a softer, more pleasant rolloff in the shadows.

### The HSL Curves

By way of three sets of Hue curves — along with further curves for Lum vs. Sat, Sat vs. Sat, and Sat vs Lum — you can make different kinds of curve-based changes to the image. Where the Custom curves let you adjust an image’s color channels by tonality (boosting the Red channel in the highlights while dropping it in the shadows, say), the Hue curves let you adjust the hue, saturation, or luma of elements in an image by their hue. Curves controls including six-vector selection and bezier handle button As an example, you might reach for the Hue vs. Sat curve to selectively drop the saturation of everything blue while raising the saturation of everything red. These curves let you make adjustments akin to those from HSL qualification, but with one crucial distinction. A curve adjustment is mathematically smoother than the matte-limited adjustment of an HSL qualifier, so it can sometimes be simpler to make specific changes that blend cleanly into the rest of the image, free of the edge artifacts on qualified keys that can sometimes wreck a seamless result. On the flip side, drawing more distinct boundaries between separate elements is often easier with HSL qualification. Only time and experience will tell you which tools suit which situations best.

Right–Original image, Left–how the Hue vs. Sat curve above has reworked that same image Where the Custom curves default to a diagonal position with lower left as the black point and upper right as the white point, Hue and Sat curves are instead flat. With the Hue vs. Hue/Sat/Lum curves, the curve’s horizontal span from left to right stands for the whole range of possible hues, from red through green through blue and then wrapping back around to red. Because the range of hues wraps smoothly from the left edge to the right, changes touching the curve near these curves’ left boundary loop seamlessly over to the right boundary, and the other way around, so the curve’s left and right sides always travel together (as the screenshot above shows). IMPORTANT: With Hue curves, whatever range of hue you isolate using control points is always relative to the RGB input wired into that node. So if you shift a shirt’s hue from blue to red with Hue vs. Hue and then want to lift that same shirt’s saturation with the Hue vs. Sat curve inside the same node, you’ll need to set control points on the very same range of blue for both curves.

### Image Sampling for Hue and Sat Curves

DaVinci Resolve gives you one more way to work the Hue curves. Open up whichever curve tab you like — be it Hue vs. Hue, or Hue vs. Sat, or Hue vs. Lum, or else Lum vs. Sat, or Sat vs. Sat — then click, or click and drag, across any range of pixels inside the Viewer area; doing so samples that region’s hues and/or image tonality and drops three control points onto the currently open curve matching the range of color and contrast you sampled.
