# Color generator and color palette and grid

Version: DaVinci Resolve 20.3 Reference Manual. Context: Color generator, Color palette studio version only, Grid.
[Chapter index](INDEX.md)
<a id="source-color-generator"></a> <a id="source-color-palette-studio-version-only"></a> <a id="source-grid"></a> <a id="source-resolve-fx-generate"></a> <a id="source-resolve-fx-generate-1"></a>

### Resolve FX Generate

This set of plugins produces imagery you can then put to work in grades and composites in a variety of ways.

### Color Generator

Produces one flat color, picked through either a color picker or an eyedropper control. It pairs nicely with a layer node's knack for blending a color into an image across various composite modes.

- Color picker: Click the color picker and the color controls that open let you settle on the color you want generated.
- Eyedropper: Alternatively, click the eyedropper to lift a color straight off the image in the Viewer; the eyedropper draws its sample from whatever feeds the input of the current node, no matter how that node's image currently appears.

### Color Palette (Studio Version Only)

Leaning toward analysis rather than a creative look, this plugin surfaces the colors that dominate each frame.

- Display Mode: A pop-up offering four choices. Color Palette: Renders the image's leading colors as rectangular swatches across the bottom (the default is 8 colors), with the eight strongest colors from each of the three principal tonal zones (shadow, midtone, highlight) shown as smaller rectangular patches just above them. At a glance you get the color palette for whatever shot you're on, and it can be exported for adventurous art directors who like having it. Shadow Region, Midtone Region, or Highlight Region: Shows a visual preview marking which portions of the image belong to which regions (per how the Shadow and Highlight Threshold sliders are currently set). In these previews the active tonal region reads as saturated while everything else in the image reads as black.
- Number of Colors: Sets how many separate colors get isolated. You can dial it to show anywhere between 8 and 24 patches.
- Shadow and Highlight Threshold: The boundaries marking where shadows, midtones, and highlights stop and start are governed by the Shadow and Highlight Threshold sliders.

### Grid

True to its name, this plugin lays a grid overlay over your image. It isn't a creative look so much as a handy measuring aid for your images.

- General: With these controls you tune the grid's overall density and orientation. Row Cells and Column Cells: A pair of sliders that decide how many cells the grid splits into across the vertical and the horizontal. Major Line Spacing: Determines how many grid squares add up to one thicker major line on the grid. Set it to zero and the feature switches off.
- Line Properties: These govern the characteristics of the grid lines themselves. Line Color: This color picker control plus its companion eyedropper let you settle on the color used to draw the grid. Individual Hor. Line Width and Ver. Line Width: Sliders for setting the thickness of every horizontal or every vertical line. Major Line Width: Chooses how thick the major lines should be. Pan, Tilt, Zoom, Rotate, Width, Height, ShearX, ShearY, Pitch, and Yaw: A bank of controls for transforming the grid however your situation calls for.
