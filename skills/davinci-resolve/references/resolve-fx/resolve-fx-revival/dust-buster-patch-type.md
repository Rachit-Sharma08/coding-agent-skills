# Dust buster patch type

Version: DaVinci Resolve 20.3 Reference Manual. Context: Dust buster studio version only.
[Chapter index](INDEX.md) / [Previous section](deflicker-and-dust-buster.md) / [Dust Buster (Studio Version Only)](deflicker-and-dust-buster.md) / [Next section](dust-frame-replacement-and-temporal-denoising.md)
<a id="source-patch-options-1"></a> <a id="source-patch-type-1"></a> <a id="source-resolve-fx-revival-part-2"></a>

### Patch Type

Six methods stand ready for fixing the contents of a selected patch. As you draw new patches, whichever Patch Type is selected at the time dictates what the next patch becomes. Once you’ve selected a patch that already exists, switching the Patch Type alters how that patch operates.

- Auto: The default method. After you draw a bounding box, the two frames ahead of and the two frames behind the current clip get analyzed and weighed against the current image. Whichever of these 5 frames fits best is sampled to lift the imperfection out of the current frame. Frames two away get priority because that staves off frozen grain, but only when they suitably match the current frame’s content.
- +/- 1 Frame: Under this mode, drawing a bounding box left to right pulls from the next frame to lift the imperfection. Drawing one right to left pulls from the previous frame instead.
- +/- 2 Frames: Drawing a bounding box left to right pulls from the image two frames ahead to lift the imperfection. Drawing one right to left pulls from the image two frames back instead.
- Spatial: Fills the inside of the selected patch automatically with pixels pulled from around the patch, by way of the Fill Method. It serves small blemishes well, but on large blemishes a pattern may become noticeable, which betrays the effect.
- Clone: Clone mode copies a portion of the image to fill a shape or patch laid over whatever you want gone. Here, clicking and dragging to lay a Rect or Ellipse over an imperfection

is followed by a second click that sets the sample region you mean to clone. A single click to lay a Patch is followed by a second click that sets the sample region. Selecting an existing shape or patch and picking Clone lets you click on the shape to position the clone region. A dotted shape tied to the original shape marks where the sample region is.

- Blend Clone: Works much like Clone mode, except that the copied portion of the image filling the Rect, Ellipse, or Patch is blended into the image so it merges more softly.
- Fill Method: With the Spatial Patch Type in use, the fill method decides how the image blemish gets mended. Grid: Reads the pixels ringing the Rect, Ellipse, or Patch, blurring them inward along both axes at once. Hugely effective on tiny blemishes. On larger ones, a grid-like pattern can surface. Horizontal: Reads the pixels flanking either side of the Rect, Ellipse, or Patch, then blurs them inward. Vertical: Reads the pixels above and beneath the Rect, Ellipse, or Patch, then blurs them inward. Patchy: Gathers pixels from every direction around the Rect, Ellipse, or Patch, then spreads and blurs them together into a soft, non-uniform region for mending the blemish. It sidesteps the patterning of the grid fill methods while delivering an exceptionally smooth result. Smooth: Just applies a gaussian blur to mend the blemish.

### Patch Options

Through these options you shape how a patch fills in over a blemish.

- Variability: (Spatial patches only) Turning this parameter up makes the Fill Method less even.
- Soft Edges: Lets you ease off the patch's edges.
- Size Adjust: Lets you resize a patch once it has been made.
- Mute: Lets you switch a given patch on or off through keyframing. Handy for blemishes that surface

across only a few pixels of a shot.

- Delete Patch: Removes whichever patch is currently selected; Option-Clicking any patch

works to delete it too.
