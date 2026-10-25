# Lens blur and mosaic blur and radial blur

Version: DaVinci Resolve 20.3 Reference Manual. Context: Lens blur studio version only, Mosaic blur, Radial blur.
[Chapter index](INDEX.md) / [Previous section](box-blur-and-directional-blur-and-gaussian-blur-and-lens-blur.md) / [Next section](zoom-blur-controls.md) / [Lens Blur (Studio Version Only)](box-blur-and-directional-blur-and-gaussian-blur-and-lens-blur.md)
<a id="source-controls"></a> <a id="source-mosaic-blur"></a> <a id="source-radial-blur"></a>

### Controls

Which parameters show up in the Controls group depends on the Shape Type you currently have chosen.

- Blur Size/Scale: Sets how much blur there is overall. Push it higher and the bokeh's shape grows more distinct.
- Blade Curvature: (Only available with Real and Creative Apertures) Softens the corners of whichever Aperture Shape you picked.
- Rotation: Sets the angle at which the shape is oriented.
- Anamorphism: Adjusts this effect's aspect ratio so it can replicate the lens blur

that anamorphic lenses produce.

- Chroma Shift: Lets you reproduce chromatic aberration inside the blur.
- Highlights: Controls the degree to which the picture's highlights drive the blur, expanding or shrinking the

image to a greater or lesser extent according to how high Smooth Strength is set.

- Apodization: (Only available with Real and Creative Apertures) A slider for tuning the

simulated “Airy disk” pattern within the defocus being produced. Pulling the slider leftward into negative territory emphasizes the concentric rings circling the bokeh pattern, recreating optical diffraction and laying a pattern over the result; pushing it rightward into positive territory steadily softens the simulated bokeh pattern's edges, for an increasingly smooth outcome.

- Catadioptric: (Only available with Real and Creative Apertures) A slider that recreates how a shaped mirror element inside a Catadioptric telescope “improves” focus within the defocused bokeh this plugin generates. As the value climbs, the source image grows steadily sharper while still being warped by the bokeh shape in play, producing gentle image overlays and a markedly different flavor of simulated optical defocus.

### Mosaic Blur

A plain, blocky blur well suited to concealing the face of an anonymous witness.

- Pixel Frequency: Sets each pixel's size, which in turn dictates how dense and detailed the resulting grid of pixels becomes.
- Cell Shape: Sets the underlying form of the mosaic. The choices are Square, Hexagon, and Triangle.
- Aliasing: Sets how tightly each cell samples whatever sits beneath it.
- X Offset: Slides the grid horizontally.
- Y Offset: Slides the grid vertically.
- Aspect: Tunes the cells' aspect ratio.
- Antialias Result: When this box is ticked, the effect does additional work to produce cleaner edges

between the cells.

- Blur Alpha: Tick this box so the Alpha channel is blurred together with the picture's contents.
- Whole Cells Only: Restricts the cells shown to only those falling entirely inside a

window.

### Radial Blur

A blur that imitates the streaking you'd get if the picture were rotating about its central point.

- X and Y Position: Repositions the center of the blur.
- Smooth Strength: Sets how much blurring takes place.
- Blur Type: With Blur Type set to Realistic, the blur reproduces the look of a photographic motion blur.

Set to Stylized instead, the blur becomes a clean, uncomplicated digital smear.

- Blur Symmetry: There are three choices.

Symmetric: The blur reads as built in both directions, yielding more of a double-image arcing around the X/Y Position, mimicking camera motion blur. Clockwise: The blur reads as moving one way, clockwise. Anti-Clockwise: The blur reads as moving one way, counter-clockwise.

- Channel Adjustment: Lets you set how strong the blur is within one particular channel, measured against the strength of the blur as a whole. Red: Sets the Red channel's blur amount as a proportion of the blur applied overall. Green: Sets the Green channel's blur amount as a proportion of the blur applied overall. Blue: Sets the Blue channel's blur amount as a proportion of the blur applied overall. Alpha: Sets the Alpha channel's blur amount as a proportion of the blur applied overall.
- Border Type: Determines the way the blur treats the picture's edges; the choices are Black, Replicate, Reflect, and Wrap Around.
- Move with Sizing: Tick this box so the blur center holds its relative spot in the frame whenever the Input and Editing sizing get altered.
- Blur Alpha: Tick this box so the Alpha channel is blurred together with the picture's contents.
