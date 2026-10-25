# Aperture diffraction and cinematic haze

Version: DaVinci Resolve 20.3 Reference Manual. Context: Aperture diffraction studio version only, Cinematic haze.
[Chapter index](INDEX.md) / [Next section](cinematic-haze-color-space-overrides.md)
<a id="source-aperture-controls"></a> <a id="source-aperture-diffraction-studio-version-only"></a> <a id="source-cinematic-haze"></a> <a id="source-compositing-controls"></a> <a id="source-diffraction-controls"></a> <a id="source-output"></a> <a id="source-resolve-fx-light"></a> <a id="source-resolve-fx-light-part-1"></a> <a id="source-source-regions"></a>

### Resolve FX Light

Every plugin grouped here recreates some distinct optical or lighting phenomenon. Although the majority were built to hand you believable output quickly, each one can be driven further to deliver a wide range of stylized looks.

### Aperture Diffraction (Studio Version Only)

Located within the ResolveFX Light category, Aperture Diffraction reproduces the starburst look that typically appears when bright sources are filmed at small apertures; physically, it stems from light bending around a lens's aperture blades. The plugin recreates that behavior, automatically targeting scene highlights you can isolate and tune through adjustable virtual apertures. Tiny bright patches take on a star-shaped glow, illustrated in the picture below.

(Left) Original image, (Right) Applying Aperture Diffraction Broader bright areas instead produce a smoother glow whose shaping and texture resemble a genuine optical artifact. You can lean on it for a glow variant that, in certain shots, reads more believably than the Glow plugin, at the cost of heavier processing. Elsewhere, the tool unlocks a broad palette of stylistic glow treatments.

(Left) Original image, (Right) Applying Aperture Diffraction

### Output

This group of controls determines which image the plugin sends downstream.

- View Output Buttons: Lets you inspect the picture at various stages of the Aperture Diffraction process, viewing the Source Regions, Diffraction Alone or Final Result.
- Input Alpha: Determines the role played by the incoming alpha channel. Masks the Source Regions: Employ the input alpha channel to keep sources in those zones from emitting light rays. Is Used for Compositing: Treats the input alpha channel as a compositing matte. Is the Source of the Glow: Treats the input alpha channel as the origin of the glow. This proves useful on VFX-heavy shots where hand-drawn mattes or Fusion alpha outputs mark out bespoke glow regions.
- Quality: Lets you pick a quality level balancing fidelity against rendering speed. Choices are Full, Half (Faster), Quarter (Fast). The high setting yields diffraction with finer detail but is otherwise identical in behavior. When the shot contains no tiny point lights, half or quarter settings are perfectly safe and cost you nothing in image quality.

### Source Regions

With the Source Region controls you decide which of the scene's highlights produce visible glow and patterning. You can watch their impact directly by switching Select Output to Isolated Source..

- Color Mode: A pop-up menu through which you either retain the hues of the various glow-producing highlight zones, or render them all as grayscale luminance alone (downstream color controls can still alter the look). Processing grayscale is quicker, yet Color can yield some striking results.
- Brightness: Establishes the cutoff above which highlights become isolated.
- Gamma: Lets you reshape the isolated highlights.
- Smooth: Lets you soften highlight detail that you would rather not see emphasized.
- Color Filter: Lets you target a specific highlight hue for isolation (an eyedropper lets you

select a value from the Viewer).

- Operation: Lets you refine the resulting Isolation matte (options include Shrink, Grow, Opening,

Closing) with a slider to define how much.

### Aperture Controls

The Aperture controls govern the form and texture of the glow this plugin produces.

- Iris Shape: Lets you pick a shape that sets how many arms appear in the star pattern. Options are Triangle, Square, Pentagon, Hexagon, Heptagon, and Octagon.
- Aperture Size: Lets you reshape the diffraction pattern, shifting toward a star form at higher values and a stippled wave look as values drop.
- Blade Curvature and Rotation: Lets you change the softness and the angle of each star's arms.
- H/V Ratio: Adjusts the aperture's horizontal-to-vertical proportion, letting you mimic an

anamorphic glow.

- Angle: Sets the angle of the aperture.
- Chroma Shift: Lets you push a bit of RGB “bleed” into the glow.

### Diffraction Controls

- Result Gamma: Lets you control how strongly the glow reads in the gaps between the arms of the star patterns.
- Result Scale: Lets you shift between sharply defined star patterns at high values and softer, more spread-out glows at low ones.

### Compositing Controls

These controls govern how the glow gets blended back over the source image.

- Normalize Brightness: This checkbox rescales the glow's brightness on a per-frame basis. As a result, the Aperture Diffraction effect holds a steady overall brightness even as the scene evolves.
- Brightness: Lets you set how intense the glow appears.
- Colorize: Lets you tint the glow using the Color control shown below.

### Cinematic Haze

A haze (or smoke/fog) machine is a common cinematographer's tool for adding a sense of depth and nuance to a shot. Its effect is to reduce contrast and to strengthen that impression the farther a subject sits from the camera. The Cinematic Haze Resolve FX reproduces both that behavior and the look of genuine outdoor smoke/fog conditions, leaning on DaVinci Resolve's powerful AI Depth Map (V2) tool to gauge depth and the objects within a shot. Because of this, Cinematic Haze feels more authentic than merely layering a 2D haze plate on top of the picture, since the haze now behaves as though it occupies a true 3D space, with density that varies by depth, atmospheric scattering, and wind disturbance.

The original image. Your budget might not stretch to actually flooding the whole of Paris with smoke. The depth map preview of the shot, building a matte from each pixel's apparent distance to the camera.

The final image. With the haze settings driven by the depth map, observe how the Eiffel Tower stays clearer than the buildings behind it.
