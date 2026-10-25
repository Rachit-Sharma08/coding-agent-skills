# Sharpen and soft glow

Version: DaVinci Resolve 20.3 Reference Manual. Context: Sharpen, Soft glow.
[Chapter index](INDEX.md) / [Previous section](glow-and-sharpen.md) / [Next section](soft-glow-inputs.md) / [Continue Soft Glow SGlo / Inputs](soft-glow-inputs.md) / [Sharpen Shrp](glow-and-sharpen.md)
<a id="source-common-controls-3"></a> <a id="source-controls-tab-4"></a> <a id="source-sharpen-controls"></a> <a id="source-soft-glow-node-introduction"></a> <a id="source-soft-glow-sglo"></a> <a id="source-the-soft-glow-node"></a>

### Sharpen controls

### Controls Tab

Inside the Controls tab live all the main controls for shaping the sharpen. Color Channels (RGBA) Out of the box this filter works on the R, G, B, and A channels. You can filter channels selectively by clicking the channel buttons to turn them on or off. NOTE: This isn't the same thing as the RGBA checkboxes sitting under the common controls. These picks are honored before the node processes the image, so turning off a channel makes the node bypass it during processing, which speeds the effect's render. The channel controls on the Common Controls tab, by contrast, kick in after the node has processed. Lock X/Y This ties the X and Y Sharpen sliders together so the sharpening stays symmetrical. It's checked by default.

Amount This slider sets how much sharpening lands on the image. Deselect the Lock X/Y control and you get separate command over each axis. Clipping Mode This setting governs how edges get treated during domain-of-definition rendering. It carries real weight for nodes such as Blur, which may need to sample parts of the image lying beyond the current domain.

- Frame: Frame is the default, and it automatically forces the node's domain of definition to span the image's whole frame, in effect disregarding the present domain of definition. Where the upstream DoD falls short of the frame, the leftover frame area is taken as black/ transparent.
- Domain: Choosing Domain honors the upstream domain of definition as the node's effect is applied. This can lead to unwanted clipping wherever the node reaches for a large filter.
- None: Choosing None skips source image clipping altogether. So whatever data the node's effect needs that would normally fall outside the upstream DoD is taken as black/transparent.

Blend The Blend slider sets what share of the affected image is blended with original image. The nearer the value gets to 0, the more of the original image it folds back in. This control is a cloned copy of the Blend slider over on the Common Controls tab; adjusting one adjusts the other in lockstep.

### Common Controls

Settings Tab The Settings tab in the Inspector also recurs across the other Blur nodes. These shared controls get a full treatment at this chapter's close, under the “The Common Controls” section.

### Soft Glow [SGlo]

### The Soft Glow node

### Soft Glow Node Introduction

The Soft Glow node resembles the Glow node but puts the image through extra processing to land a far softer, more natural glow. It's a great fit for atmospheric haze around planets, skin tones, and conjuring dreamlike settings.
