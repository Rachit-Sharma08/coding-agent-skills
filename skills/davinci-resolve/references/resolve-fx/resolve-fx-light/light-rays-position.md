# Light rays position

Version: DaVinci Resolve 20.3 Reference Manual. Context: Light rays.
[Chapter index](INDEX.md) / [Previous section](lens-reflections-and-light-rays.md) / [Light Rays](lens-reflections-and-light-rays.md)
<a id="source-appearance"></a> <a id="source-atmosphere"></a> <a id="source-position"></a> <a id="source-shimmer"></a>

### Position

Position parameters let you set the direction the rays travel.

- Ray Directions: A pop-up menu offering a choice between "From A Location," which surfaces controls for picking an X or Y position to mark an origin point setting the angle of the light beams, or "At an Angle," which surfaces controls for picking an overall orientation for the rays.

### Shimmer

Adds gentle variation to the light pattern thrown by the rays.

- Add Shimmer: Tick this box to switch the Shimmer effect on or off.
- Strength: Governs how much the light patterns vary.
- Detail: Governs the relative detail of the variation, lower levels produce finer detail and higher

levels produce larger detail.

- Scale: Governs the size of the noise pattern.
- H vs. V Ratio: Governs the ratio between horizontal and vertical spread of the variations.
- Evolution: How much the noise pattern should shift.
- Seethe: How much to automatically evolve on each frame counting from the start.

### Appearance

Appearance parameters let you tailor the ray effect.

- Ray Dropoff: A pop-up carrying four options. Default (soft): Yields soft, indistinct rays of light that seem to dissolve as they stream outward. Keep Shape of Source: The edge of the light rays follows the shape that emitted them. CCD Bloom Harsh: Sharply lifts the brightness of the part of the picture emitting rays as Length climbs, producing harsh glow or bloom in the picture.

CCD Bloom Soft: Mildly lifts the brightness of the part of the picture emitting rays as Length climbs, producing a very gentle brightening of the picture.

- Length: Lets you make the rays longer or shorter.
- Relative Length Red: How far the red glow spreads compared with the other colors.
- Relative Length Green: How far the green glow spreads compared with the other colors.
- Relative Length Blue: How far the blue glow spreads compared with the other colors.
- Soften: Lets you blur the rays being emitted.
- Brightness: Lets you tune how bright the rays are.
- Gamma: Tunes the brightness of the ray effect through a gamma curve.
- Saturation: Tunes the intensity of the ray's color.
- Color: A color picker and eyedropper let you set a color with which to tint the rays.
- Composite Type: Lets you pick a composite mode for blending the glow effect into the

picture. Defaults to Add, which suits hotter, more intense rays. Screen lets you make gentler rays, while other composite modes let you produce other varied effects.

- Bright Region Recovery: Drag this slider to win back some picture detail in spots blown out by the rays.

### Atmosphere

- Add Atmosphere: Tick this box to switch the Atmosphere effect on or off.
- Strength: Governs how much the light patterns vary.
- Detail: Governs the relative detail of the variation, lower levels produce finer detail and higher

levels produce larger detail.

- Scale: Governs the size of the noise pattern.
- H vs. V Ratio: Governs the ratio between horizontal and vertical spread of the variations.
- Evolution: How much the noise pattern should shift.
- Seethe: How much to automatically evolve on each frame counting from the start
