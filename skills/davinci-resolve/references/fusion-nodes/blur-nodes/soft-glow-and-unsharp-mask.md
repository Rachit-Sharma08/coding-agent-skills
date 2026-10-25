# Soft glow and unsharp mask

Version: DaVinci Resolve 20.3 Reference Manual. Context: Soft glow, Unsharp mask.
[Chapter index](INDEX.md) / [Previous section](soft-glow-inputs.md) / [Next section](vari-blur-and-vector-motion-blur-and-common-controls.md) / [Soft Glow SGlo](sharpen-and-soft-glow.md)
<a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-common-controls"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab"></a> <a id="source-controls-tab-1"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-inspector-1"></a> <a id="source-soft-glow-controls"></a> <a id="source-the-unsharp-mask-node"></a> <a id="source-unsharp-mask-controls"></a> <a id="source-unsharp-mask-introduction"></a> <a id="source-unsharp-mask-usm"></a>

### Basic Node Setup

A 2D image such as the MediaIn1 pictured here feeds the Soft Glow node. From its output, the node tree carries on into a further 2D image-processing node or into a Merge node.

### Inspector

A Soft Glow node applied to a MediaIn1 node

### Soft Glow controls

### Controls Tab

Every primary control you need to tailor the soft glow operation lives on the Controls tab. Down at the foot of the Inspector, a color scale region lets you tint the soft glow. Filter Pick the Blur method for the filter from this menu. What follows describes the available choices.

- Box: A simple but very fast Box filter.
- Bartlett: Bartlett produces a gentler, more understated glow whose drop-off is smoother, though rendering can run

slower than Box.

- Multi-box: Multi-box stacks a Box filter across several passes to mimic a Gaussian shape.

A modest pass count (say, four) yields a high-quality blur that frequently beats the Gaussian filter on speed and avoids ringing entirely.

- Gaussian: Gaussian lays down a soft glow blurred via the Gaussian algorithm. It serves as the default method.

Color Channels (RGBA) By default the filter works across the R, G, B, and A channels. You can filter channels selectively by toggling the channel buttons on or off. NOTE: Do not confuse this with the RGBA checkboxes under the common controls. Because the node honors these picks ahead of processing the image, turning a channel off makes the node bypass it during processing, which speeds up how fast the effect renders. By contrast, the channel controls on the Common Controls tab take effect once the node finishes processing. Threshold Use this control to cap how much the soft glow does. A higher threshold means a pixel has to be brighter before the glow touches it. Gain The Gain control sets how bright the glow is. Lock X/Y With Lock X/Y enabled, the horizontal and vertical glow amounts are tied together. Otherwise you can dial in distinct glow amounts on each axis of the image. Glow Size This figure governs how large the glow effect grows. Bigger values widen the glowing highlights across the image. Num Passes Offered only when in Multi-box mode. Higher values yield a smoother spread of the effect while also pushing render times up. Finding the balance between the quality you want and render times you can live with is worthwhile. Clipping Mode This choice governs how edges get handled during domain-of-definition rendering. It matters enormously for nodes such as Blur, since those can demand samples from regions of the image beyond the current domain.

- Frame: Frame, the default choice, makes the node's domain of definition span the image's whole frame, so the current domain of definition is effectively disregarded. Should the upstream DoD be smaller than the frame, whatever frame area is left over reads as black/transparent.
- Domain: Choosing Domain here honors the upstream domain of definition as the node's effect is applied. In cases where the node uses a large filter, this can produce unwanted clipping.
- None: Picking None skips any clipping of the source image whatsoever. So any data the node's effect needs that would ordinarily sit beyond the upstream DoD reads as black/transparent.

Blend How much of the affected image gets blended with the original image is set by the Blend slider. The closer the value drops toward 0, the more of the original image is mixed back in. This control mirrors the Blend slider over on the Common Controls tab. Adjusting one updates the other in the common controls at the same time. Color Scale (RGBA) These Scale sliders let you tune, channel by channel, how much glow lands on each color channel, tinting the glow. Click and hold the Pick button, then drag the pointer across the viewer to sample a particular color out of the image.

### Common Controls

Settings Tab Other Blur nodes share the same Settings tab found in the Inspector. Full coverage of these common controls sits at this chapter's close, in the "The Common Controls" section.

### Unsharp Mask [USM]

### The Unsharp Mask node

### Unsharp Mask Introduction

Unsharp masking is a method for sharpening solely the edges inside an image. Most commonly this node fixes blurring and lost detail in low-contrast pictures; one example is pulling usable detail from long exposure frames of distant galaxies. The filter pulls a band of frequencies out of the image and blurs that band to cut detail. That blurred output then gets weighed against the original images. Where a pixel differs markedly between the original and the blurred version, it is probably edge detail. Then that pixel is brightened so it stands out.

### Inputs

The Unsharp Mask node's two inputs serve to hook up a 2D image plus an effect mask that confines the effect. Input: The orange input takes the primary 2D image for the Unsharp Mask. Effect Mask: A mask shape from polylines, simple primitive shapes, paint strokes, or bitmaps from other tools goes into the blue input. Hooking a mask up here restricts the Unsharp Mask to just the pixels inside the mask. That effect mask kicks in on the tool after processing wraps up.

### Basic Node Setup

A 2D image like the MediaIn1 shown here feeds the Unsharp Mask node. Its output keeps the node tree going by linking to another 2D image-processing node or a Merge node.

### Inspector

An Unsharp mask node applied to a MediaIn1 node

### Unsharp Mask controls

### Controls Tab

All the primary controls you need to tailor the Unsharp Mask operation reside on the Controls tab. Color Channels (RGBA) Out of the box the filter operates over the R, G, B, and A channels. Selective channel filtering happens when you click the channel buttons to switch them active or inactive. NOTE: Do not mistake this for the RGBA checkboxes living under the common controls. Since the node weighs these picks before it processes the image, switching a channel off has the node skip it while processing, which makes the effect render faster. By contrast, the channel controls on the Common Controls tab apply once the node has finished processing.

Lock X/Y Once Lock X/Y is enabled, the horizontal and vertical sharpen amounts get locked together. Otherwise, distinct glow amounts can land on each axis of the image. Size This control sets how large the blur filter applied to the extracted image is. The larger this value goes, the greater the chance pixels register as detail. Gain The Gain control governs how much gain hits pixels the mask flags as detail. Bigger values yield a sharper image. Threshold Which frequencies get pulled from the source image is decided by this control. Pushing the value up drops lower-contrast regions out of having the effect applied.

### Common Controls

Settings Tab Other Blur nodes share the same Settings tab found in the Inspector. Full coverage of these common controls sits at this chapter's close, in the "The Common Controls" section.
