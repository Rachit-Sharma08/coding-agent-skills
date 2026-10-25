# Transform advanced options

Version: DaVinci Resolve 20.3 Reference Manual. Context: Transform.
[Chapter index](INDEX.md) / [Previous section](surface-tracker-and-transform.md) / [Next section](video-collage.md) / [Transform](surface-tracker-and-transform.md)
<a id="source-advanced-options"></a> <a id="source-global-blend"></a>

### Advanced Options

- Edge Behavior: This menu decides how the frame's edges behave once the transforms shrink below the Timeline Resolution. Transparent: Whatever lies beyond the transformed image turns transparent, letting the video on the tracks below show through behind it. Reflect: The image is flipped and flopped into a mirrored image that reaches out to the Timeline Resolution frame boundary. Wrap-Around: Copies the image into a video-wall effect that fills the gap out to the Timeline Resolution frame boundary. Replicate: Copies the outermost pixels along the image edge. Those pixels are drawn out from every side to meet the Timeline Resolution boundary.
- Composite Type: Sets the Composite type used to blend several video layers as one.

For more on what each Composite type does, refer to Chapter 50, “Compositing and Transforms in the Timeline.”

### Global Blend

- Blend: Lets you dissolve between the image with no Transform on it and one with the Transform applied in full.
