# Mirrors and pencil sketch in DaVinci resolve and prism blur and scanlines

Version: DaVinci Resolve 20.3 Reference Manual. Context: Mirrors, Pencil sketch in DaVinci resolve studio version only, Prism blur, Scanlines.
[Chapter index](INDEX.md) / [Previous section](drop-shadow-and-edge-detect-and-emboss-and-mirrors.md) / [Next section](scanlines-and-sky-replacement.md) / [Mirrors](drop-shadow-and-edge-detect-and-emboss-and-mirrors.md)
<a id="source-individual-controls"></a> <a id="source-kaleidoscope-controls"></a> <a id="source-main-controls-1"></a> <a id="source-pencil-sketch-in-davinci-resolve-studio-version-only"></a> <a id="source-prism-blur"></a> <a id="source-rosette-controls"></a> <a id="source-scanlines"></a>

### Main Controls

These controls set what sort of effect this plugin produces.

- Mirror Placement: Lets you pick among mirror effect types such as Individual (a plain reflection), Rosette, and Kaleidoscope.
- Reflect at Borders: Adds a further reflection of the image any time your reflection's angle and position would otherwise let offscreen black creep into the frame.

### Individual Controls

With Mirror Placement on Individual, six sets of Mirror parameters in a row let you stack multiple mirrored edges in various combinations; only one is on by default, but switching on more edges builds more intricate mirror effects. Every group of Mirror parameters carries the following parameters:

- Enable Mirror: Switches that mirror reflection on.
- X and Y Position: Places the center of the mirror split reflection.
- Angle: Sets the angle of the seam the reflection runs along.
- Flip: Swaps which side of the image gets reflected.

### Rosette Controls

With Mirror Placement on Rosette, one set of parameters generates an assortment of circular patterns.

- X and Y Position: Places the center of the circular rosette reflection.
- Angle: Sets the rosette pattern's orientation about its center.
- Wedge Width: Sets the thickness of the wedges ringing the outside of the rosette

pattern, and with it the number of wedges. Thicker wedges mean fewer reflections around the rosette pattern, while thinner wedges mean more reflections around it.

### Kaleidoscope Controls

With Mirror Placement on Kaleidoscope, one set of parameters lets you generate an assortment of kaleidoscopic images:

- X and Y Position: Places the center of the mirror split reflection.
- Center Size: Shrinks or grows the cells that make up the kaleidoscopic image.
- Angle: Sets the angle of the seam the reflection runs along.
- Number of Sides: Three sides yield a triangular pattern, while four sides yield a rectalinear

pattern lined up with the angle currently chosen.

### Pencil Sketch in DaVinci Resolve (Studio Version Only)

A plugin whose deeply adjustable controls make an image look hand-drawn.

- Color Sketch: Tick this box to switch between a color and a grayscale sketch.
- Sketch Stroke Controls: Parameters governing how thick the outlines are, the threshold at which

they show up around objects in the frame, and how long they run.

- Sketch Tone Controls: Parameters governing how many tonal levels appear in the rendered

result, plus contrast controls that steer how much of the image lands in shadows, mid-tones, and highlights.

- Sketch Texture Controls: Parameters that lay an adjustable stippled texture over the image, with a checkbox to auto animate it.

(Left) The original image, (Right) The image with Pencil Sketch applied

### Prism Blur

Mimics flat chromatic aberration together with a vignetted lens.

- X and Y Position: Let you move the point within the frame around which the chromatic aberration forms.
- Blur Strength: Blurs the primary image.
- Aberration Distance: Sets how far the aberration effect sits from the source image.
- Aberration Strength: Ramps up the zoom blur behind the chromatic aberration

to make it more pronounced.

- Vignette Size: Adds edge vignetting to the image; a setting of 0 clears the vignette,

and 1 is the largest vignette this filter allows.

- Vignette Sharpness: Sets the feathering of the vignette effect; lowering it

softens the edge, while raising it sharpens that edge yet never wholly removes its softness. The Vignette effect is built to fall off in a way that mimics how a lens shows vignetting.

### Scanlines

Mimics the scanlines of a television set, or any effect in which you want alternating lines darkening the image. With its assortment of parameters, this is a very flexible effect you can apply in many ways.
