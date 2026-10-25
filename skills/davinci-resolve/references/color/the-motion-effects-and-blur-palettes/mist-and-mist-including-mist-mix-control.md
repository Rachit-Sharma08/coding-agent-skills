# Mist and mist including mist mix control

Version: DaVinci Resolve 20.3 Reference Manual. Context: The motion effects and blur palettes.
[Chapter index](INDEX.md) / [Previous section](spatial-noise-radius-and-reduction-limits.md)
<a id="source-mist"></a> <a id="source-mist-including-mist-mix-control"></a>

### Mist

Through the Mist mode you can fold blur and sharpen operations together to produce looks reminiscent of those you’d get from “Vaseline on the lens” or Pro-Mist optical filters.

### Mist including Mist Mix control

In contrast to the Blur or Sharpen modes, in which the Radius sliders deliver the wanted effect right away, the Mist mode asks you to bring the Radius and Mix sliders down jointly before you reach a pleasing result. Shifting the levels of Radius and Mix opens up countless takes on the mist effect.

- Radius: To build a Mist effect, your first move is to drop Radius so the image sharpens. That step then pairs with a reduction of the Mix parameter to deliver the blend of detail and blurring that yields a mist effect.
- H/V Ratio: Gives you a way to lend directionality to the operation underway. Held at its default of 0.50, the image is treated equally across the horizontal and vertical directions. Pushing H/V Ratio upward drives the effect more and more along the horizontal axis, whereas easing it down drives the effect more and more along the vertical axis.
- Scaling: Boosts the degree of scaling the Radius control applies, letting you push a mist effect past the Radius slider’s normal reach. For blur effects, the scaling parameter does nothing once Radius sits at 0.50 or higher.
- Mix: Having sharpened the image with the Radius slider, lowering the Mix parameter layers on a superimposed blur that merges with the picture’s high-detail areas to form the mist effect.
