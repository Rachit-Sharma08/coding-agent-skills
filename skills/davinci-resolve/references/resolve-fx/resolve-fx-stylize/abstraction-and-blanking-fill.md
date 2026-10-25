# Abstraction and blanking fill

Version: DaVinci Resolve 20.3 Reference Manual. Context: Abstraction studio version only, Blanking fill.
[Chapter index](INDEX.md) / [Next section](blanking-fill-and-defocus-background.md)
<a id="source-abstraction-studio-version-only"></a> <a id="source-blanking-fill"></a> <a id="source-draw-edge-controls"></a> <a id="source-fill-extent"></a> <a id="source-main-controls"></a> <a id="source-quantization-controls"></a> <a id="source-resolve-fx-stylize"></a> <a id="source-resolve-fx-stylize-part-1"></a> <a id="source-source"></a>

### Resolve FX Stylize

Every plugin gathered in this category opens up a different route to making artistic alterations to the image.

### Abstraction (Studio Version Only)

A filter more capable than it looks, letting you produce a broad spread of cartoon-style renders by reducing an image into adjustable pools of like color, with outlines as an option.

### Main Controls

This effect is built on these controls.

- Pre Blur: Eases the image by blurring away unwanted detail before this filter does its work.
- Abstraction Strength and Iterate Abstraction: Acting together, these parameters then smooth the image and form pools of simplified color amid its detail. Abstraction Strength: Has to sit above 0 before the Iteration No. parameter does anything. A higher Abstraction Strength flattens image detail further still by averaging neighboring regions of color into one another. Iterate Abstraction: Cuts the small detail in the image down even more by "broadening" adjacent areas of similar color so they merge into one.

### Quantization Controls

By quantizing the bit depth used to stylize the image, these controls thin out the pools of color even more forcefully. What you get is a still sharper flattening within every region of color.

- Quantization: A checkbox switches this function on.
- Steps: Pushing this parameter up divides each region of color into a larger number of

separate regions.

- Softness: Softens the boundary between each level of color.

### Draw Edge Controls

Puts an edge around the regions of color this effect produces.

- Draw Edge: Turns edge drawing on.
- Edge Strength: Higher values yield thicker, more sharply defined edges.
- Edge Detection Threshold: Higher values confine edges to only the strongest edge detail in the picture.

### Blanking Fill

This plugin is built specifically to fill black frame blanking quickly with a stylized image drawn from the clip itself, making blanking less of a distraction for viewers of documentaries and news segments. The example that follows uses the Blanking Fill plugin to put image on the left and right of "pillarboxed" standard definition 4:3 video sitting inside a High Definition or Ultra High Definition 16:9 aspect ratio.

(Left) The standard definition image as shot, (Right) The same image once default Blanking Fill is applied A range of controls makes it easy to tailor this effect to whatever you need.

### Source

These controls reshape the clip in various ways, which in turn affects how that clip gets used to fill the blanking area.

- Zoom: Zooms the clip while holding it inside the native domain of definition. Handy for quickly trimming unwanted edge pixels so they stay hidden and do not feed the blanking fill.
- Crop Left and Right: Trims the image's left and right edges alike and grows the side area given over to blanking fill.
- Same Left/Right Sliders: On by default, it ties both sliders together so that moving one mirrors the move on the other.
- Crop Top and Bottom: Trims the image's top and bottom edges alike and grows the vertical area given over to blanking fill.
- Same Top/Bottom Sliders: On by default, it ties both sliders together so that moving one mirrors the move on the other.
- Center: When checked, it re-centers the image area should a sizing operation have shifted it off.

### Fill Extent

These controls set how the current copy of the image is stretched to cover the blanking area.

- Zoom Mode: Three options are available: Stretch to Timeline: Warps the image automatically so it stretches to fill the full frame. Keeps features within the blanking fill area aligned with where they sit in the original image. Zoom to Timeline: Zooms into the image automatically to fill the full frame. Leaves the clip looking "inset" from the blanking fill image. Manual: Brings up Expand and Aspect sliders so you can set by hand how much the image zooms and stretches to cover the blanking fill area.

Warp Top Layer: lets you pick, with onscreen controls, a strip along an image edge to stretch out and fill the frame's blanking. This mode gives you two sets of onscreen controls for shaping the result: one set of outer handles decides how far out the image's edges warp to fill whatever blanking exists, defaulting to the project frame size. A set of inner handles decides how much of the image gets stretched out, defaulting to the current title safe boundary. When you adjust these, choosing too narrow an edge produces a harsher warp and stretch, whereas choosing a wider edge to stretch reads more naturally but touches more of the frame.

- Expand: (Appears only when Zoom Mode is Manual) Zooms the image.
- Aspect: (Appears only when Zoom Mode is Manual) Stretches the image.

(Left) A 4:3 image dropped into a 16:9 timeline, which leaves black pillar boxing down the left and right sides, (Right) That image once Blanking Fill is set to Warp Top Layer, where the left and right edges stretch out to cover the blanking area
