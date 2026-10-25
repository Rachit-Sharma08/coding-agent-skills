# Hue saturation chroma luma mode and color warper interface

Version: DaVinci Resolve 20.3 Reference Manual. Context: Color warper.
[Chapter index](INDEX.md) / [Previous section](introduction-to-the-color-warper-and-chroma-warp.md) / [Next section](color-warper-color-space-selection.md)
<a id="source-grid-resolution-affects-the-specificity-and-quality-of-adjustments"></a> <a id="source-hue-saturation--chroma-luma-mode"></a> <a id="source-previewing-which-colors-are-warped-by-each-control-point"></a> <a id="source-resetting-grid-points"></a> <a id="source-sampling-to-warp-colors"></a> <a id="source-the-color-warper-interface"></a> <a id="source-using-the-grid-controls-to-manipulate-color"></a>

### Hue-Saturation / Chroma-Luma Mode

The Color Warper Hue-Saturation / Chroma-Luma palettes form a mesh-based warping tool that bends one group of colors into another rather than displacing pixels in space. What's more, in contrast to the HSL curves, they allow you to tune two color parameters together at once, confined to userselectable zones of chosen hues. Carried out through a grid of draggable control points, these adjustments naturally taper off smoothly from the colors you are warping toward the other colors that have been locked in place. How smooth that taper turns out hinges on the gap between the warp points you are moving and the nearby warp points held fixed against change.

The Color Warper, sitting in the center palette area This tool offers two avenues of use. One is to drag the grid's control points directly, giving you very targeted image adjustments. The more instinctive route is to click and sample the image, which grabs the nearest grid point governing that color, and then drag to adjust using that control point.

Clicking and dragging to sample skin tone in the Viewer so that color's control point on the Hue-Saturation warping grid can be adjusted This tool can carry out extremely precise color tweaks in an image, comparable to what a Qualifier key or the HSL curves would let you do. Yet because the points warp through a grid, you can work two color characteristics together, moving both hue and saturation, or chroma and luma. The example that follows fine-tunes the woman's shirt, corrects her skin tone, and reworks the greens of the foliage in the shot. Each of these three lifelike adjustments stays smooth and free of artifacts thanks to the clean way the Color Warper remaps color.

(Top) The original image, (Bottom) Reworking the grass's hue and saturation by way of the Chroma-Luma controls Beyond that, this tool can build sweeping stylistic looks across the whole image, twisting the color in inventive directions other controls cannot reach. In the next image, every neutral and lower-saturation color gets warped toward a bluish-cyan, while the more saturated oranges are warped toward a saturated orange-red, producing a quick stylistic treatment of the image.

(Top) The original image, (Bottom) Giving the whole image a stylized treatment with the Hue-Saturation controls

### The Color Warper Interface

You may work with the Color Warper right where it docks in the middle palette area, or hit the Expand button to pop it out into a floating window you can stretch to any size, which gives you finer command over crowded grids of control points. For clarity, this chapter's examples present the Color Warper alongside the Viewer in a floating window. Once the Color Warper is open in its own window, pressing the Close button returns the palette to the palette area underneath.

Pressing the Expand button floats the Color Warper into its own window, and pressing the Close button inside that window docks the palette again. The Color Warper palette breaks into two broad regions. On the left, the grid area holds the warping grid itself, whose points you move to make adjustments, with controls below it for setting the grid's resolution and the color space it operates in. On the right, the control area supplies every tool, range control, and feathering control you can use to work the warping grid in all sorts of highly specific ways.

### Using the Grid Controls to Manipulate Color

Two modes live in this palette, each giving you its own way to work the image's colors and each carrying a distinct grid style for warping whichever color channels come into play. Getting comfortable with how you move the color-warping points on each of these grids is key to grasping how the palette behaves.

(Left) Hue-Saturation mode's radial grid, (Right) Chroma-Luma mode's pair of rectangular grids Dragging to Warp Colors Their shapes differ, yet all of these grids respond to handling in much the same fashion. When you drag a control point, the color tied to that point changes, and the colors ringing the dragged point shift proportionally too, based on where they fall between the point you are moving and neighboring points that either (a) go untouched or (b) are pinned in place. Pinned points hold the colors at those spots steady. Locking certain stretches of a grid while dragging others lets you build refined, hue-targeted adjustments.

Here the orange control point has been chosen and dragged to apply an adjustment. Those control points wearing black outlines are pinned and serve to keep the control points across from them from shifting. Every other control point lying between the selected and locked ones gets stretched or compressed according to how the selected point was moved.

The picture above illustrates the three states a control point can hold in the grid:

- Orange: A selected point shows in orange. You can pick several at once by Command-clicking each point, by dragging a bounding box across multiple points, or by reaching for the draw selection tool to click and sketch over whichever points you want. After you have selected a control point and moved it, it locks itself so the adjustment stays put.

A selected point shows in orange; here four points are selected so they can all be moved together.

- Outlined: White control points carrying a black outline are locked. Such points do not budge on their own when points nearby are dragged, which makes them valuable for protecting particular colors you would rather leave alone, and for preserving edits to points you have already moved. Any adjusted point becomes locked. The Chroma-Luma grid locks its outer corners, just as the Hue-Saturation web locks its outer ring and center point.

Locked points with black outlines stopping the selected point from adjusting other colors in the image

- White: A white control point is neither selected nor locked, and it will stretch or compress whenever adjacent control points are moved.

Unlocked control points caught between a selected point and locked points (here the grid's corners) will compress and stretch, warping a whole range of color as you drag.

Although control points behave largely alike whether you are in Hue-Saturation or Choma-Luma mode, a few meaningful distinctions exist. The radial “spokes” of the Hue-Saturation wheel leave their neighboring spokes alone, so any tweak you apply to a control point on one spoke reaches only the colors lying between it and the two spokes flanking it. As a result, there is no need to lock control points on adjacent spokes of this wheel-shaped grid to keep them steady.

Tweaks applied to control points on one “spoke” of the Hue-Saturation wheel grid leave the points on neighboring spokes untouched, which behave as though locked despite not being so. Both the Hue-Saturation and Chroma-Luma warper grids pin the grid's outer boundary. You may still drag those points to adjust them, but they cannot be unlocked and they won't shift on their own as you move other control points. The Hue-Saturation grid pins one extra point dead center, holding the neutral colors (black through gray and white) neutral. TIP: Dragging that locked center point of the Hue-Saturation grid lets you recolor the white point while every other color in the image warps proportionally to absorb the change smoothly. That move can serve as the seed for a wide variety of looks.

### Previewing Which Colors Are Warped By Each Control Point

Hold down the Option key as you click a control point in the warp grid, and the Viewer shows you a preview of exactly which colors that control point reaches. The affected pixels show up in color over a black field, where the black stands for all the pixels that point will leave alone.

Keeping the Option key held while clicking a Color Warper control point previews the affected pixels set against black.

### Sampling to Warp Colors

Although it pays to understand how the grid's control points are handled, the most natural way to work this control is to point inside the Viewer, click to sample a color you want to change, keep the button pressed, and drag to adjust it. As you move the pointer through the Viewer, a crosshairs travels around the warping grid to mark the exact color on the vectorscope graph, while a yellow box flags the control point nearest the color you are sampling, the one a click would grab. In the example below, parking the eyedropper over the sky reveals that a click would land on a control point near the grid's center.

Gliding the pointer across the Viewer previews on the warping grid the very control point a click would select. A click-and-drag first grabs and then relocates the control point that matches that color in the Viewer. While you drag, the chosen control point follows your mouse in lockstep as the image's colors refresh live to reflect the change you are making. At the same time, an arrow on the grid conveys the delta of the adjustment underway. Carrying a selected control point to a different hue in the grid warps the starting color into the new one.

A click-and-drag shifts the grid's control point for that color to apply your change and pins it in place. Control points can also be locked by sampling the image: hold Command and Shift together, then click whichever color or colors in the warp grid you want frozen against change. This lets you lock unwanted colors right in the Viewer before you go on to adjust the colors you actually mean to alter. In the example below, Command-Shift-clicking the woman's shoulder pins the yellowish highlights resting on her uniform. After that, click-dragging a highlight on her face pushes the highlights toward teal while the warmer highlights on her shoulder survive intact, all done by sampling straight in the Viewer.

(Top) Command-Shift-clicking to pin the warping grid's closest control point to a color you want left alone, (Bottom) Warping an adjacent color while that freshly locked control point holds its part of the image steady

### Resetting Grid Points

Whenever you have moved a point and decide you want it back to default, just right-click it to unlock and reset that point.

### Grid Resolution Affects The Specificity and Quality of Adjustments

In both Hue-Saturation and Chroma-Luma modes you can alter the grids' resolution through the controls along the foot of the Color Warper palette, just below the grid. Individual drop-down menus set the control-point resolution for hue and saturation, or for chroma and luma, on their own, though out of the box the two stay tied together.

The two resolution controls sitting beneath the grid controls Out of the box the Hue-Saturation grid runs at a resolution of 6x6, the coarsest setting on offer. The Chroma-Luma grid also starts at 6x6, yet it can drop further, down to 4x4. Coarse warping grids make it simple to apply broad color changes that span wide bands of analogous color while staying smooth. On top of that, weaker media that is 8-bit, uses 4:2:0 chroma subsampling, and/ or is heavily compressed gains from coarser warping grids, which fend off artifacts and keep the color changes smooth.

(Left) The Hue-Saturation grid at a resolution of 6x6, (Right) The Hue-Saturation grid at a resolution of 24x16 Finer grids, by contrast, let you target tighter color bands with more pinpoint adjustments. That route pays off best on projects shot with high-quality media (10- or 12-bit, 4:2:2 or 4:4:4 chroma subsampling, and lightly compressed) where artifacts can be kept at bay. Given high-quality media, you will be able to lean on the Color Warper for astonishingly precise adjustments. To fix the default Hue and Saturation grid resolutions, open the Color Warper's Option menu, pick Default Hue Resolution or Default Saturation Resolution, and choose the resolution you prefer from the drop-down menu.

The Chroma-Luma grid at a resolution of 6x6

The Chroma-Luma grid at a resolution of 24x24 NOTE: Should you adjust the grid at one resolution and then switch it coarser or finer, your adjustment is interpolated onto the new grid resolution, even though the end result may shift slightly.
