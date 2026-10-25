# Lens reflections and light rays

Version: DaVinci Resolve 20.3 Reference Manual. Context: Lens reflections studio version only, Light rays.
[Chapter index](INDEX.md) / [Previous section](lens-flare-element-types.md) / [Next section](light-rays-position.md)
<a id="source-global-controls"></a> <a id="source-lens-reflections-studio-version-only"></a> <a id="source-light-rays"></a> <a id="source-main-controls"></a> <a id="source-presets"></a> <a id="source-reflecting-elements"></a> <a id="source-source-regions"></a>

### Lens Reflections (Studio Version Only)

Sitting under the ResolveFX Light category, Lens Reflections recreates bright highlights bouncing off the assorted optical pieces inside a lens to produce flaring and scattering tied to the shape and movement of highlights you single out in the shot. It's a convincing simulation that performs best when the scene holds light sources or specular reflections—think headlights on a car, the sun, light fixtures, fire and flame, or any other lighting elements credibly bright enough to throw off such flaring. What's more, this plugin truly comes alive when those light sources travel, since each layer of simulated reflection moves in line with that element's spot inside the virtual lens being modeled, yielding organic motion you never have to keyframe. Lacking strong highlights, this filter's output works well for more abstract light-leak looks.

On the left, the original picture; on the right, Lens Reflections applied. Output The Output controls give you a preview of the picture at various stages of the Lens Reflections effect.

- View Output Buttons: Lets you preview the picture at various stages of the Lens reflection effect, viewing the Source Regions, Reflections Alone or Final Result.
- Input Alpha: Decides how the input alpha channel gets used. Masks the Source Regions: Leans on the input alpha channel to keep sources in those areas from throwing off light rays.

Is Used for Compositing: Puts the input alpha channel to work for compositing. Is the Source of the Glow: Treats the input alpha channel as where the glow originates, This can come in handy on VFX heavy shots where custom mattes or Fusion alpha outputs mark out custom glow areas.

- Quality: This pop-up lets you decide how the effect renders. Choices are Full, Half (Faster), and Quarter (Fast). You're trading sharpness against speed. The reflection process itself stays identical at every quality level. Smoother, lower-resolution material won't gain anything from the Full Quality setting.

### Source Regions

The Source Region controls let you pick which scene highlights will spawn lens reflections. You can watch what these controls do directly by switching Select Output to Isolated Source. It's strongly advised to tailor the Isolation controls to the picture in front of you when running this plugin, since, even more than with other plugins, the specific highlights involved sway the final effect dramatically.

- Color Mode: A pop-up menu that lets you either hold onto the colors of the various highlight regions feeding the lens reflections, or render them all as grayscale brightness alone (color controls downstream can still alter the effect). Grayscale processes faster, but Color can yield some dazzling results.
- Brightness: Sets the threshold at which highlights are isolated.
- Gamma: Lets you shape the isolated highlights.
- Smooth: Lets you blur details in the highlights you'd rather not have stand out.
- Color Filter: Lets you single out one particular highlight color to isolate (an eyedropper lets you

select a value from the Viewer).

- Morph Operation: A pop-up lets you tweak the resulting Isolation matte (choices include Shrink,

Grow, Opening, Closing), with a slider to set the amount. Morph Amount: Tunes the edges of the light source per the Morph Operation you picked.

### Global Controls

The Global controls let you swiftly and simply tune the overall quality of the Lens Reflections effect through one centralized cluster of parameters.

- Global Brightness: Lets you push the level of every reflection up or down. Lowering brightness is a handy way to soften a big lens reflection effect, though pictures carrying small lens reflection effects might gain from a touch more brightness.
- Global Blur: Lets you defocus every reflection. This is another solid route to softening lens reflection effects of all sorts.
- Anamorphism: Lets you warp the reflection elements to mimic the stretch of an anamorphic lens.
- Global Colorize: Lets you tune the color intensity of the reflections, whether by deepening the color of all reflections or draining it.

### Presets

A Presets pop-up offers a range of different settings to start from. Choosing a preset fills in the Reflecting Elements parameters below, from where you can tailor the effect to suit the picture in front of you. It's strongly advised to tailor these effects to match the kind of highlights in your picture so you get the best outcome.

### Reflecting Elements

There are four clusters of Reflecting elements, each carrying identical controls. That lets you build interactions blending as many as four sets of reflections. The controls inside each cluster are these.

- Brightness: Lets you tune the intensity of that reflection.
- Position in Optical Path: Lets you slide the reflection along an element's position in the

lens. In practice, that means positive values grow an inverted reflection drawn from the highlights, while pulling values toward 0 shrinks the reflection, and pushing into negative values flips the reflection and drags it the other way as it starts growing once more. A value of –1 places the reflection squarely over the highlight that produced it.

- Defocus type: Lets you pick the kind of blur to apply, options being Box blur, Triangular blur, Lens blur (the heaviest on the processor), and Gaussian blur (the default).
- Defocus: Lets you decide how much to blur that element.
- Stretch: Lets you hand the flare an anamorphic widescreen feel.
- Stretch Falloff: Lets you taper the edges for a less even stretch.
- Lens Coating: A pop-up lets you pick common colors like purple, green, and yellow matching different anti-reflective lens coatings, plus an assortment of other vivid colors. Defaults to none. Choosing any other option surfaces a color control and eyedropper so you can manually set a color or sample one from the picture. A Colorize slider lets you vary how strongly to tint the reflection with the chosen color, though dropping Colorize to 0 lets the flare draw its color from the source highlights of the picture, which can occasionally give you the most striking look.

### Light Rays

A "rays of light" effect that recreates volumetric lighting streaming out of light sources marked by a threshold you set. The effect echoes what people sometimes call "god rays" across the sky, or other strongly directional glow effects.

### Main Controls

The Main controls include:

- View Output Buttons: Lets you preview the picture at various stages of the Lightray effect, viewing the Source Regions, Rays Alone or Final Result.
- Input Alpha: Decides how the input alpha channel gets used. Masks the Source Regions: Leans on the input alpha channel to keep sources in those areas from throwing off light rays. Is Used for Compositing: Puts the input alpha channel to work for compositing. Is the Source of the Glow: Treats the input alpha channel as where the glow originates. This can come in handy on VFX-heavy shots where custom mattes or Fusion alpha outputs mark out custom glow areas.
- Source of Rays: Lets you set what emits the rays, using Bright Regions or Edges.
- Source Threshold: A slider that lets you set the cutoff at which bright parts of the picture

emit rays.
