# Tilt shift blur and watercolor

Version: DaVinci Resolve 20.3 Reference Manual. Context: Tilt shift blur studio version only, Watercolor studio version only.
[Chapter index](INDEX.md) / [Previous section](sky-replacement-and-stylize-and-tilt-shift-blur.md) / [Tilt-Shift Blur (Studio Version Only)](sky-replacement-and-stylize-and-tilt-shift-blur.md)
<a id="source-depth-of-field"></a> <a id="source-lens-iris"></a> <a id="source-watercolor-studio-version-only"></a>

### Lens Iris

The Lens Iris controls only come into play with Blur Type set to Lens Blur. They're a trimmed-down version of the controls found on the Lens Blur filter.

- Iris Shape: Lets you pick which kind of aperture to use, shaping the look of the bokeh effect. Aperture Shape choices run to Triangle, Square, Pentagon, Hexagon, Heptagon, or Octagon shaped aperture.
- Blade Curvature: (Only available with Real and Creative Apertures) Lets you soften the corners of the Aperture Shape you picked.
- Rotation: Sets the angle at which the shape sits.
- Anamorphism: Tunes this effect's aspect ratio so it lines up with the lens blur

that anamorphic lenses produce.

- Highlights: Tunes how the image's highlights play into the blur, dilating or eroding the

image to a greater or lesser degree according to how high Smooth Strength runs.

### Depth of Field

Further Depth of Field settings let you tune the depth map driving the depth-of-field effect.

- Map Source: Picks where the depth map comes from. Custom (default) lets you build the depth map within the effect. From Alpha In and From Second Input let you bring in depth maps built in other nodes.
- Center X, Center Y, and Angle: With these parameters you transform the depth map.
- Focus Sweep: Lets you home in on a region by “distance” for isolation. The depth

map's white areas take the blur, while its black areas are skipped.

- In Focus Range: Lets you widen or narrow the depth map's black center that marks out the

blurred region.

- Near Blur Range and Far Blur Range: A pair of parameters for separately tuning the falloff of the

depth map's white bottom and top.

- Depth Map Preview: A checkbox that lets you view the grayscale depth map straight away as you make

these tweaks. The white region gets blurred, while the black region stays untouched. TIP: For Depth of Field adjustments that read more convincingly, pair the Depth Map effect with the Tilt-Shift Blur effect. The depth map's output can flow straight into the Tilt-Shift Blur effect as a blur map: wire the Depth Map node's key output into the Tilt-Shift Blur node's key input, then choose “From Alpha In” from the Map Source dropdown within the effect's Depth of Field section. From there work the Focus Sweep to zero in on the area you mean to isolate. Should the result fall short of what you expect, try inverting the depth map.

### Watercolor (Studio Version Only)

A spin on the Abstraction filter, this one boils images down to simplified washes of gently blended color, in a thoroughly painterly manner.

- Channels: This pop-up menu lets you decide whether Luminance or RGB supplies the source for the smoothed color.
- Show Gradient: This checkbox lets you view the boundaries marking out each region of smooth color, keyed to the value you set on the Smoothness slider below.
- Smoothness: Governs how much detail survives in the end result. Low smoothness values keep more detail in the smoothed output, while higher ones produce broader pools of lower-detail yet smoother color.
