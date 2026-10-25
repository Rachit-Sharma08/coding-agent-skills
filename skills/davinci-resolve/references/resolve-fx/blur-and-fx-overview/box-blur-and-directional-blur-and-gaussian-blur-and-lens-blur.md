# Box blur and directional blur and gaussian blur and lens blur

Version: DaVinci Resolve 20.3 Reference Manual. Context: Box blur, Directional blur, Gaussian blur, Lens blur studio version only.
[Chapter index](INDEX.md) / [Previous section](resolve-fx-overview-and-resolve-fx.md) / [Next section](lens-blur-and-mosaic-blur-and-radial-blur.md)
<a id="source-box-blur"></a> <a id="source-directional-blur"></a> <a id="source-gaussian-blur"></a> <a id="source-lens-blur-studio-version-only"></a> <a id="source-resolve-fx-blur"></a> <a id="source-resolve-fx-blur-1"></a> <a id="source-shape"></a> <a id="source-speed"></a>

## Resolve FX Blur

### Resolve FX Blur

Compared with what the Blur palette gives you, the plugins gathered here supply a broader assortment of distinct blurring techniques.

### Box Blur

An adjustable-quality blur spanning the range from extremely coarse to extremely soft.

- Horizontal and Vertical Strength: Use these sliders to set how wide and how tall the blur spreads.
- Same Horizontal/Vertical: Tick this checkbox to either link these parameters or control them on their own.
- Horizontal and Vertical Channel Adjustment: With these sliders you can tune the blur

separately for each color channel. Red: Sets how much the Red channel is blurred compared with the blur applied across the whole image. Green: Sets how much the Green channel is blurred compared with the blur applied across the whole image. Blue: Sets how much the Blue channel is blurred compared with the blur applied across the whole image. Alpha: Sets how much the Alpha channel is blurred compared with the blur applied across the whole image.

- Number of Iterations: Governs how smooth the final blur turns out — a setting of 1 gives the coarsest, most “boxy” result and 6 gives the finest, most fluid one. When the iteration count is low, the output of a box blur can look a fair bit like a lens blur.
- Border Type: Determines the way the blur treats the picture's edges; the choices are Black, Replicate, Reflect, and Wrap Around.
- Blur Alpha: Tick this box so the Alpha channel is blurred together with the picture's contents.

### Directional Blur

A blur locked to one single angle.

- Blur Strength: The quantity of blur you'd like.
- Blur Angle: Which way the blur points.
- Blur Type: With Blur Type set to Realistic, the blur reproduces the look of a photographic motion blur.

Set to Stylized instead, the blur becomes a clean, uncomplicated digital smear.

- Symmetric Blur: With the Symmetric checkbox enabled, the blur looks as though it's built

from both directions, yielding more of a double-image streaking along the blur angle, which mimics camera motion blur. With it disabled, the blur instead reads as travelling one way only, outward from the starting position along the blur angle.

- Channel Adjustment: Lets you set how strong the blur is within one particular channel, measured against the strength of the blur as a whole. Red: Sets the Red channel's blur amount as a proportion of the blur applied overall. Green: Sets the Green channel's blur amount as a proportion of the blur applied overall. Blue: Sets the Blue channel's blur amount as a proportion of the blur applied overall. Alpha: Sets the Alpha channel's blur amount as a proportion of the blur applied overall.
- Border Type: Determines the way the blur treats the picture's edges; the choices are Black, Replicate, Reflect, and Wrap Around.
- Blur Alpha: Tick this box so the alpha channel is blurred together with the picture's contents.

### Gaussian Blur

Delivers a gentle blur that's like viewing the picture through frosted glass, softening fine detail and noise.

- Horizontal and Vertical Strength: A pair of sliders lets you control the Horizontal and Vertical Strength on their own.
- Same Horizontal/Vertical: This checkbox keeps the Horizontal and Vertical Strength figures locked to one another.
- Horizontal and Vertical Channel Adjustment: Use these sliders to fine-tune the blur on a per channel basis. Red: Sets the Red channel's blur amount as a proportion of the blur applied overall. Green: Sets the Green channel's blur amount as a proportion of the blur applied overall. Blue: Sets the Blue channel's blur amount as a proportion of the blur applied overall. Alpha: Sets the Alpha channel's blur amount as a proportion of the blur applied overall.
- Border Type: Determines the way the blur treats the picture's edges; the choices are Black, Replicate, Reflect, and Wrap Around.
- Blur Alpha: Tick this box so the Alpha channel is blurred together with the picture's contents.

### Lens Blur (Studio Version Only)

A premium recreation of how an optical lens defocuses. Its adjustable parameters let you reach assorted “bokeh” looks, comparable to those that arise from various pairings of aperture geometry and lens spherical-aberration correction, both of which shape the “circle of confusion” responsible for the visible forms that appear in picture regions holding tiny pinpoint highlights.

### Shape

Within the Shape group you pick which aperture shape gets simulated, and that choice governs the shape the bokeh takes in this effect.

A user-supplied shape feeding a color node tree to build bespoke bokeh within the Lens Blur plugin

- Shape Type: Determines which kind of aperture is used. Three choices exist: Real Apertures: Pick a true-to-life option from the Aperture Shape pop-up menu beneath, to shape the resulting bokeh. The Aperture Shape choices here are Triangle, Square, Pentagon, Hexagon, Heptagon, or Octagon shaped aperture.

Creative: Pick a more whimsical option from the Aperture Shape pop-up menu beneath, to shape the resulting bokeh. Such choices mimic the bokeh you might genuinely capture by mounting a blackout filter with a custom-cut hole at its center in front of the lens. The Aperture Shape choices here are Heart, Star, Starfish, Starburst, Petals, Lip, Eye, Droplet, and Leaf. External Input: Takes any graphic of your choosing — ideally with a small white form set on a black field — and uses it to shape the bokeh. That form has to be supplied as a graphic or matte clip placed into the Node Editor, after which you connect the image into the second RGB input of the Lens Blur node.

- Aperture Shape: Offers a selection of aperture forms that govern the look of this plugin's simulated bokeh blur.
- Preview Shape: Tick this checkbox to view the exact shape you've chosen to apply.

### Speed

Use the Speed Options group to dial in the balance between quality and speed for this plugin.

- Quality: Three settings — Full, Half (Faster), and Quarter (Fast) — let you strike the right compromise between picture quality and how fast the plugin runs.
- Blur Alpha: Tick this box so the Alpha channel is blurred together with the picture's contents.
- Horizontal and Vertical Crop: Trims down the External Input shape image driving the

bokeh, which is handy when an oversized graphic is bogging things down and you'd like to cut away surplus black around its edges. The result won't visibly shift until you begin trimming into the white portion of the shape.
