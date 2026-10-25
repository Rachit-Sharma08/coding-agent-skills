# Cinematic haze and glow

Version: DaVinci Resolve 20.3 Reference Manual. Context: Cinematic haze, Glow.
[Chapter index](INDEX.md) / [Previous section](cinematic-haze-color-space-overrides.md) / [Next section](glow-and-lens-flare.md) / [Cinematic Haze](aperture-diffraction-and-cinematic-haze.md)
<a id="source-air-disturbance"></a> <a id="source-color-and-composite"></a> <a id="source-glow"></a> <a id="source-secondary-glow"></a> <a id="source-shape-and-spread"></a>

### Air Disturbance

These controls inject motion and stir the haze to mimic wind or similar atmospheric activity.

- Enable Disturbance: Tick this box to switch on the air disturbance toolset.
- Preview Influence: Renders a preview that displays the disturbance pattern

interacting with the haze depth map.

- Intensity: Controls how dense the air disturbance pattern is.
- Brightness: Controls how bright the air disturbance pattern is.
- Scale: Controls how large the air disturbance pattern is.
- Detail: Governs how much fine detail the disturbance pattern carries.
- Flow Direction: Sets the angle along which the disturbance pattern flows.
- Flow Speed: Governs how quickly the disturbance pattern flows.
- Seethe Rate: Controls how fast the disturbance pattern changes over time.
- Start Frame: Lets you nominate a particular frame where the seethe begins.
- Randomize Start Frame: Picks a random frame for the seethe to begin, which you can use

to avoid repeating the identical disturbance pattern across several shots.

### Glow

A refined, soft glow treatment that stays highly adjustable through just a handful of essential parameters.

- View Output Buttons: Lets you inspect the picture at various stages of the Lens reflection process, viewing the Source Regions, Glow Alone or Final Result.
- Input Alpha: Determines the role played by the incoming alpha channel. Masks the Source Regions: Employ the input alpha channel to keep sources in those zones from emitting light rays. Is Used for Compositing: Treats the input alpha channel as a compositing matte. Is the Source of the Glow: Treats the input alpha channel as the origin of the glow. This proves useful on VFX-heavy shots where hand-drawn mattes or Fusion alpha outputs mark out bespoke glow regions.
- Shine Threshold: Sets the luminance value above which glow begins to appear in the picture.

### Shape and Spread

- Spread: Sets how far the shine reaches out from the picture regions that set it off.
- H/V Ratio: Lets you change the balance of horizontal versus vertical spread, so you can fashion

“streaky” shine that travels farther along one axis.

- Relative Spread Red/Green/Blue: Lets you set a separate spread amount per color channel,

mimicking a form of chromatic aberration within the glow.

### Color and Composite

- Gain: Sets how bright the glow is.
- Gamma: Tunes the glow's spread and the way it falls off with distance.
- Saturation: Sets how strong the glow's color is.
- Color Filter: A color picker and eyedropper let you select a hue to tint the glow with.
- Glow framing: Lets you decide what occurs when shine reaches the frame's edge, whether it gets

boosted by “Reflect in Camera” or tempered by a “Vignette” effect.

- Composite Type: Lets you select which composite mode blends the glow over the

picture. The default is Screen, well suited to soft glows. Add produces hotter, more intense glows, and the remaining composite modes open up other varied looks.

- Opacity: Lets you set how transparent the glow is, giving a quick way to “ease off” a glow you like overall but that runs too strong for the shot in hand.
- Invert Effect: Ticking this box reverses the Glow parameters, so now the darker regions drive the brighter ones rather than the reverse.
- Bright Region Recovery: Move this slider to win back some image detail in spots the glow has blown out.

### Secondary Glow

In effect, this is a glow layered onto your glow. It lets the inner and outer glows carry distinct colors within a single glow effect. Take a red neon sign on a blue wall: you could give it a vivid red inner glow paired with a blue-tinted secondary outer glow. That outer glow picks up more of the surroundings, as if a brighter blue wall were lit by the sign, while the inner glow stays vivid red, echoing the neon tube's own color.

- Add Secondary Glow: Tick this box to switch the Secondary Glow effect on or off.
- Gain: How bright the secondary glow appears.
- Spread: How far the secondary glow reaches outward.
- Color Filter: The color of the Glow Halo.
