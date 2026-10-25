# Dead pixel fixer and deband

Version: DaVinci Resolve 20.3 Reference Manual. Context: Dead pixel fixer studio version only, Deband studio version only.
[Chapter index](INDEX.md) / [Previous section](dirt-chromatic-aberration-and-dead-pixel-removal.md) / [Next section](deflicker-and-dust-buster.md) / [Dead Pixel Fixer (Studio Version Only)](dirt-chromatic-aberration-and-dead-pixel-removal.md)
<a id="source-advanced-controls"></a> <a id="source-deband-parameters"></a> <a id="source-deband-studio-version-only"></a> <a id="source-general"></a> <a id="source-minimizing-banding-using-the-deband-filter"></a> <a id="source-patch-options"></a> <a id="source-patch-type"></a>

### General

These top-level controls govern how you draw the patches used to mend frame blemishes, along with whether their on-screen controls appear and in what manner.

- Draw Rect: Click and drag to lay a rectangular patch of any size from one corner across to the opposite corner. After it’s drawn, click any edge of the overlay and drag to reposition it.
- Draw Ellipse: Click and drag to lay an elliptical patch of any size from one corner across to the opposite corner. After it’s drawn, click any edge of the overlay and drag to reposition it.
- Place Patch: For laying small patches aimed at tiny details such as dead pixels. Picking this option brings up a New Patch Size slider that sets the size of the patches you’re about to place before you place them. After one’s drawn, click the edge of any patch and drag to reposition it.
- New Patch Size: (active only while Place Patch is selected) Sets how big a patch the Place Patch tool lays down.
- Show Patches: A checkbox that reveals or conceals every patch’s onscreen outline in the Viewer.
- Hide During Interaction : Conceals every patch’s onscreen outline in the Viewer as you move a patch; this makes it easier to gauge the effect of moving the patch on the image, without the outline in the way.

### Patch Type

Three methods stand ready for fixing the contents of a selected patch. As you draw new patches, whichever Patch Type is selected at the time dictates what the next patch becomes. Once you’ve selected a patch that already exists, switching the Patch Type alters how that patch operates.

- Spatial: Fills the inside of the selected patch automatically with pixels pulled from around the patch, by way of the Fill Method. It serves small blemishes well, but on large blemishes a pattern may become noticeable, which betrays the effect.
- Clone: Clone mode copies a portion of the image to fill a shape or patch laid over whatever you want gone. Here, once you click and drag a Rect or Ellipse across an imperfection, a second click then sets the sample region you mean to clone. A single click to lay a Patch is followed by a second click that sets the sample region. Selecting an existing shape or patch and picking Clone lets you click on the shape to position the clone region. A dotted shape tied to the original shape marks where the sample region is.
- Blend Clone: Works much like Clone mode, except that the copied portion of the image filling the Rect, Ellipse, or Patch is blended into the image so it merges more softly.
- Fill Method: With the Spatial Patch Type in use, the fill method decides how the image blemish gets mended.

Grid: Reads the pixels ringing the Rect, Ellipse, or Patch, blurring them inward along both axes at once. Hugely effective on tiny blemishes. On larger ones, a grid-like pattern can surface. Horizontal: Reads the pixels flanking either side of the Rect, Ellipse, or Patch, then blurs them inward.

Vertical: Reads the pixels above and beneath the Rect, Ellipse, or Patch, then blurs them inward. Patchy: Gathers pixels from every direction around the Rect, Ellipse, or Patch, then spreads and blurs them together into a soft, non-uniform region for mending the blemish. It sidesteps the patterning of the grid fill methods while delivering an exceptionally smooth result. Smooth: Just applies a gaussian blur to mend the blemish.

### Patch Options

These options let you tailor how a patch fills over a blemish.

- Variability: (Spatial patches only) Pushing this parameter up makes the Fill Method less uniform.
- Soft Edges: Softens the patch’s edges.
- Size Adjust: Resizes a patch after you’ve made it.
- Mute: Switches a given patch on or off through keyframing. Handy for blemishes that crop

up across only a few pixels of a shot.

- Delete Patch: Removes the currently selected patch; an Option-Click on any

patch deletes it as well.

### Advanced Controls

These controls let you tailor this effect’s UI.

- Clone Sticks to Mouse: With this on, the moment you draw or place a Rect, Ellipse, or Patch while in Clone or Blend Clone mode, the tool jumps straight to positioning the sample region, which speeds things up.
- New Patches Stay Selected: With this on, patches remain selected after you draw them, ready for more customization.
- UI Line Thickness: Sets how thick the on-screen outlines come out.
- Patches Stick to: This parameter handles fixing dead pixels or blemishes on clips that

have undergone stabilization. Source: The patches you lay stay put, unless you apply motion stabilization to the shot, at which point they’re transformed along with the image so they stay “stuck” to the feature in the source clip they’re mending. Scene: When clearing a blemish off a moving subject, the FX Tracker can track whatever you’re fixing, so the patch travels along with it.

- Output Mode: This shows you various representations of the patched effect you’re building. Four options are on offer. Patched Result: The finished result, every patch mending the blemish beneath it. Patch Locations: Presents a key with each placed patch in white against black. Differences: Presents each patch’s difference against the original image. Difference Magnitude: Presents a more pronounced version of the Differences view.

### Deband (Studio Version Only)

Low bit-depth media carrying regions of shallow color gradient, such as a sky or a wall, often display color banding — visible stripes — since there simply aren’t enough color values to render the gradation from light blue to darker blue in the sky smoothly.

An example of banding in the sky of an image

### Minimizing banding using the Deband filter

This filter is built to single out the edges of color banding and tamp them down by dithering pixels on either side to ease the transition. It performs best on image regions you’ve isolated with a secondary qualifier or window; otherwise you run the risk of every edge in your image getting dithered and softened (though that can make for an interesting stylistic effect).

### Deband Parameters

Deband’s controls are these:

- Edge Threshold: Governs how sharply defined an edge must be before the filter acts on it; lowering it leaves out fainter edges, while raising it takes them in.
- Radius: Dials the strength of dithering up or down within the affected regions.
- Post Refine: Tightens (when lowered) or broadens (when raised) the regions touched by dithering.
- Display Edge: A checkbox that gives you a black-and-white high-contrast preview of which edges

are being picked up for dithering, which can help you fine-tune your results.
