# Dust frame replacement and temporal denoising

Version: DaVinci Resolve 20.3 Reference Manual. Context: Dust buster studio version only, Frame replacer studio version only, Noise reduction studio version only.
[Chapter index](INDEX.md) / [Previous section](dust-buster-patch-type.md) / [Next section](denoising-object-removal-and-patch-replacement.md) / [Dust Buster (Studio Version Only)](deflicker-and-dust-buster.md)
<a id="source-advanced-controls"></a> <a id="source-frame-replacer-studio-version-only"></a> <a id="source-noise-reduction-studio-version-only"></a> <a id="source-spatial-nr-controls"></a> <a id="source-spatial-threshold-controls"></a> <a id="source-temporal-nr-controls"></a> <a id="source-temporal-threshold-controls"></a>

### Advanced Controls

These controls let you tailor this effect's UI.

- Clone Sticks to Mouse: With this on, drawing or dropping a Rect, Ellipse, or Patch while in Clone or Blend Clone mode jumps straight to placing the sample region, which speeds up the workflow.
- New Patches Stay Selected: With this on, a patch stays selected once you've drawn it, ready for you to refine it further.
- UI Line Thickness: Lets you set how thick the on-screen outlines appear.
- Output Mode: This shows you various views of the patched effect you're building.

It carries four options. Patched Result: The finished image, each patch mending the blemish beneath it. Patch Locations: Presents a key in which every placed patch reads white against black. Differences: Presents how each patch differs from the original image. Difference Magnitude: Presents a stronger version of that Differences view.

### Frame Replacer (Studio Version Only)

The Frame Replacer lets you recycle or merge neighboring frames to help eliminate corrupt frames or artifacts that appear for the span of a lone frame. It comes in handy for repairing issues such as a damaged film frame or a video frame marred by pixelated digital breakup.

- Replace This Frame: Ticking this box picks out the particular frame in the clip you wish to replace. It also drops a keyframe at the right spot in the clip automatically.
- Replacement Method: Lets you pick how the new frame gets made.

From Previous: Swaps in the frame right before the selected one, in effect cloning that frame. From Next: Swaps in the frame right after the selected one, in effect cloning that frame. Blend Prev/Next: Swaps in a merge of the frames sitting just before and just after the selected one. Optical Flow: Swaps in a merge of the surrounding frames built with DaVinci Resolve's optical flow technology.

### Noise Reduction (Studio Version Only)

Drawing on the Color page's Noise Reduction controls, the Resolve FX Noise Reduction splits into a pair of GPU-accelerated noise reduction types built to tame noise in troublesome clips. You can apply either method on its own or both at once, in differing amounts according to what the specific material in front of you calls for.

### Temporal NR Controls

The Temporal NR controls study the picture across several frames so as to tell noise apart from detail. Motion estimation settings let you keep moving subjects out of this process to head off unwanted motion artifacts.

- Frames Either Side: How many frames flanking the current one you want averaged in order to part detail from noise. The choice runs from 0 to 5 frames. 0 does no frame averaging; larger values do more, though at a steep rise in compute cost. A larger frame count can sharpen the analysis, yet it can also breed unwanted artifacts where the frame holds fast-moving imagery. For fast-moving imagery, a value of 1 may serve better. Should you need larger frame values but encounter artifacts, you might also tune the Motion Threshold to clear the problem.
- Motion Est. Type: Selects which method DaVinci Resolve relies on to spot motion in the picture. Faster, the default, is lighter on the processor but less precise. Picking Better can fence off motion more precisely, though it taxes the processor harder. None switches motion estimation off entirely, which applies Temporal NR across the whole picture.
- Motion Range: Three options, Small, Medium, and Large, let you state the motion speed that Motion Estimation should anticipate excluding. The Small option presumes slow subjects with little or no motion blur, letting Temporal NR reach more of the picture at a given Motion Threshold setting. The Large option presumes brisk motion whose blur covers a wider swath of the picture, which fences more of it off from Temporal NR at that same Motion Threshold setting. Pick whichever option strikes the best balance between cutting noise and inviting motion artifacts as you tune the Motion Threshold parameter.

### Temporal Threshold Controls

Through the Temporal Threshold parameters you steer which image traits receive more or less noise reduction.

- Luma Threshold: Lets you set how strongly or how lightly Temporal NR hits the image's luma component. Its scale spans 0–100, with 0 doing no noise reduction whatsoever and 100 the full amount. Push it too far and you can wipe fine detail out of the image.
- Chroma Threshold: Sets how strongly Temporal NR hits the image's chroma component. Its scale spans 0–100, with 0 doing no noise reduction whatsoever and 100 the full amount. Push it too far and you can wipe fine color detail out of the image. That said, you'll often find the Chroma Threshold can climb above the Luma Threshold while leaving artifacting less obvious.
- Luma Chroma Same Threshold: By default the Luma and Chroma Threshold parameters move as a pair, so a change to one changes both. Switch this checkbox off, though, and the two come apart, letting you apply distinct noise reduction amounts to each component of the image, keyed to wherever the noise is worst.
- Motion: Sets the threshold dividing which moving pixels count as in motion (over this threshold) from which count as static (under this threshold). With Motion Estimation in play, Temporal NR steers clear of image regions sitting above this threshold, warding off motion artifacts by withholding frame-averaging from parts of the image that are moving. Lower values hold more of the image back from Temporal NR by catching subtler movement. Higher values let Temporal NR cover more of the image by demanding quicker motion before excluding it. The choice spans 0 to 100, with 0 putting Temporal NR on no pixels and 100 on every pixel. Its default is 50, a fitting middle ground for plenty of clips. Bear in mind that pushing the Motion Threshold too high can surface artifacts in the moving portions of the image.
- Blend: Lets you fade between the image as the Temporal NR parameters shape it (at 0.0) and the image untouched by noise reduction (100.0). This parameter makes it easy to meet halfway when you're leaning on heavy temporal noise reduction.

### Spatial NR Controls

The Spatial NR controls let you even out pockets of high-frequency noise across the image while trying to hold onto detail rather than soften it. It works well at knocking down noise that Temporal NR cannot.

- Mode: The Mode drop-down menu swaps Spatial NR among three separate algorithms. Since all three share identical controls, you can flip between them on the same settings to weigh the results side by side.

Faster: Leans on a compute-light noise reduction method that holds up at lower settings but can throw artifacts once pushed to higher values. Better: Hands the Spatial NR controls a higher-quality algorithm whose output far outclasses Faster, at the cost of heavier rendering load and of barring you from splitting the Luma and Chroma Threshold sliders for separate tweaks per color component. Enhanced: Does a markedly finer job of holding image sharpness and detail as you raise the Spatial Threshold sliders to clear noise. The gain stands out most once the Spatial Threshold sliders climb to high values (where “high” lands depends on the image at hand). At lower values, the gain can read as subtler against the “Better” mode, which is lighter on the processor than the compute-hungry “Enhanced” setting. On top of that, “Enhanced” lets you split the Luma and Chroma threshold sliders so you can dial different noise reduction amounts into each color component as the image demands.

- Radius: The choices are Large, Medium, and Small. A smaller radius buys you better real-time performance and can hold up well at low Luma and Chroma Threshold values. You may, however, spot more aliasing across detailed regions when NR Threshold values stay low. Stepping the Radius up progressively yields higher quality across more visually detailed areas at high Luma and Chroma Threshold values, the trade being slower performance. For most images at medium NR Threshold settings, an NR Radius of Medium should deliver fitting quality. As with so many operations here, the quality-versus-speed balance is yours to adjust.

### Spatial Threshold Controls

Through the Spatial Threshold parameters you steer which image traits receive more or less noise reduction.

- Luma: Lets you set how strongly or how lightly noise reduction hits the image's luma component. Its scale spans 0–100, with 0 doing no noise reduction whatsoever and 100 the full amount. Push it too far and you can wipe fine detail out of the image.
- Chroma: Lets you set how strongly or how lightly noise reduction hits the image's chroma component, smoothing pockets of high-frequency noise while trying to keep significant edge detail crisp. Its scale spans 0–100, with 0 doing no noise reduction whatsoever and 100 the full amount. Push it too far and you can wipe fine color detail out of the image. That said, you'll often find the Chroma Threshold can climb above the Luma Threshold while leaving artifacting less obvious.
- Luma Chroma Same Threshold: By default the Luma and Chroma Threshold parameters move as a pair, so a change to one changes both. You can, however, split these parameters to feed different noise reduction amounts into each component of the image. Say an image goes too soft at a particular noise reduction level yet shows more color speckling than luma noise: you'd pull the Luma Threshold down to hold detail while pushing the Chroma Threshold up to clear the color noise.
- Blend: Lets you fade between the image as the Spatial NR parameters shape it (at 0.0) and the image untouched by noise reduction (100.0). This parameter makes it easy to meet halfway when you're leaning on heavy spatial noise reduction.
