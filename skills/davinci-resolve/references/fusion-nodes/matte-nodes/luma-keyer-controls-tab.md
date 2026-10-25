# Luma keyer controls tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Luma keyer.
[Chapter index](INDEX.md) / [Previous section](difference-keyer-and-luma-keyer.md) / [Next section](luma-keyer-and-magic-mask.md) / [Luma Keyer LKy](difference-keyer-and-luma-keyer.md)
<a id="source-controls-tab-2"></a> <a id="source-matte-nodes-part-3"></a> <a id="source-the-luma-keyer-controls-tab"></a>

### The Luma Keyer Controls tab

### Controls Tab


Within the Luma Keyer, the Controls tab gathers every parameter you use to tune how good the matte looks. Channel This menu picks which color channel drives matte creation. Pick from Red, Green, Blue, Alpha, Hue, Luminance, Saturation, or Depth (Z-buffer). Threshold On this range slider, the left-hand handle establishes the lower threshold, while the right-hand handle establishes the upper threshold. Moving them marks out a span of luminance values from which the matte is built. Anything that falls under the lower threshold setting turns black, or transparent, in the matte. Anything that climbs past the upper threshold setting turns white, or opaque, in the matte. Whatever sits inside that span produces a grayscale matte. Filter This control picks which filtering algorithm runs when a blur is applied to the matte.

- Box: The quickest option, though quality drops. Box works best when only a small amount of blur is needed.
- Bartlett: Also called a Pyramid filter, Bartlett strikes a reasonable balance between

speed and quality.

- Multi-box: Choosing this filter brings up the Num Passes slider, which hands you control over

quality. With 1 and 2 passes you get output identical to Box and Bartlett, respectively. From 4 passes upward, the look is typically on par with Gaussian, achieved faster and free of edge “ringing.”

- Gaussian: Built on a genuine Gaussian approximation, the Gaussian filter delivers superb output, though it runs a touch slower than the rest. Occasionally it may introduce a barely perceptible edge “ringing” on floating-point pixels.

Blur This applies a blur to the matte’s edge by way of whichever method you chose in the Filter menu. Set it to zero and you get a crisp, cutout-style hard edge. Raise the value and the blur grows. Clipping Mode This setting governs the treatment of edges during domain of definition rendering. It matters enormously when you blur the matte, since doing so can pull samples from parts of the image that lie beyond the current domain.

- Frame: Frame is the default, and it automatically pins the node’s domain of definition to the image’s full frame, in effect disregarding the current domain of definition. Where the upstream DoD is smaller than the frame, whatever frame area is left over counts as black/transparent.
- Domain: Choosing Domain honors the upstream domain of definition as the node applies its effect. In cases where the node uses a large filter, this can introduce unwanted clipping.
- None: Choosing None skips source image clipping entirely. As a result, any data the node needs to render its effect that ordinarily sits beyond the upstream DoD counts as black/transparent.

Contract/Expand This slider grows or shrinks the matte’s semitransparent regions. A setting above 0.0 expands the matte; a setting below 0.0 contracts it. You typically pair this control with the blur so you can soften a matte’s hard edge and cut down on fringing. Because the control touches only semitransparent regions, a matte’s hard edge is left alone. Gamma Matte Gamma drives the matte’s values up or down across the semitransparent regions. Pushing the value up makes the gray regions more opaque; pulling it down makes them more transparent. Regions of the matte that are fully black or white stay as they are. Invert Tick this checkbox to invert the matte, so every transparent region turns opaque and every opaque region turns transparent. Solid Matte Solid mattes are mask nodes or images wired into the node’s solid matte input. That solid matte goes straight onto the image’s alpha channel. As a rule, solid mattes hold out keying wherever you need things to stay opaque — say, a person with blue eyes shot in front of a blue screen. Turning on Invert flips the solid matte before the source alpha takes it in. Garbage Matte A garbage matte, too, is a mask node or image wired into the node’s garbage matte input. That garbage matte goes straight onto the image’s alpha channel. As a rule, the garbage variety strips out stray elements that resist keying, such as microphones and booms. They also serve to patch in regions that hold the key color but that you want to keep. You can’t blend garbage mattes of differing modes inside one tool. It’s common to place a Matte Control node downstream of a Keyer node to introduce a garbage matte whose effect is the reverse of the matte on the keyer. Turning on Invert flips the garbage matte before it merges with the source alpha. Post-Multiply Image Pick this option and the keyer multiplies the image’s color channels by the alpha channel it generates for that image. This option is normally on and is enabled by default. Clear this checkbox and the image can no longer be treated as premultiplied when you merge it with other images. On the Merge node, reach for the Subtractive option in place of the Additive one. To read up on these Merge node settings, turn to Chapter 95, "Composite Nodes," in the DaVinci Resolve Reference Manual, or to Chapter 35 in the Fusion Reference Manual.
