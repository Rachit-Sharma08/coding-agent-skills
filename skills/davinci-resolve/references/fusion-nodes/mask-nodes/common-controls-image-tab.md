# Common controls image tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Common controls.
[Chapter index](INDEX.md) / [Previous section](wand-mask-and-common-controls.md) / [Next section](common-controls-settings-tab.md) / [The Common Controls](wand-mask-and-common-controls.md)
<a id="source-image-tab"></a> <a id="source-inspector-3"></a> <a id="source-mask-node-image-tab"></a> <a id="source-mask-nodes-part-4"></a>

### Inspector

### Mask node Image tab

### Image Tab


This tab’s controls govern both the resolution and the clipping approach applied to the mask that gets generated. Output Size The Output size menu determines the resolution at which the mask node renders. Its three choices are the comp’s default resolution, the resolution coming from the source input on nodes that accept an input, or a resolution you define yourself. Custom Picking Custom from the Output Size menu ties the new mask’s width, height, and pixel aspect to whatever the composition’s Frame Format preferences specify. Should those Frame Format preferences be altered, the mask’s resolution shifts to follow. Turning this option off comes in handy when you want to assemble a composition at a resolution that differs from the final render’s intended target.

- Width and Height: Together these two controls define the Width and Height that the mask being created will have.
- Pixel Aspect: With this control you state the Pixel Aspect ratio for the mask you are making. Choosing 1:1 yields a square pixel measuring the same on each side (as on a computer monitor), whereas 0.91 produces a mildly rectangular pixel (as on an NTSC monitor).
- Depth: Use the Depth drop-down menu to choose the pixel color depth of the mask’s output image. Although 32-bit pixels consume four times as much memory as 8-bit pixels, they deliver considerably more precision. Float pixels permit high dynamic range numbers beyond the usual 0..1 range, letting you describe colors lighter than white or deeper than black.

NOTE: A right-click on the Width, Height, or Pixel Aspect controls brings up a menu of the file formats configured under the preferences Frame Format tab. Choosing one of those entries applies that format’s width, height, and pixel aspect values.

Clipping Mode This setting controls the way edges are treated during domain of definition rendering. The Clipping mode matters most once blur or softness enters the picture, since those may need to sample regions of the image that lie beyond the current domain.

- Frame: Frame is the default, and it makes the node’s domain of definition span the entire frame of the image, in effect disregarding the current domain of definition. Where the upstream DoD falls short of the frame, whatever frame area is left over is rendered as black/transparent.
- None: Choosing None skips clipping of the source image altogether. Whatever data the node’s effect needs that would normally sit beyond the upstream DoD is rendered as black/transparent.
