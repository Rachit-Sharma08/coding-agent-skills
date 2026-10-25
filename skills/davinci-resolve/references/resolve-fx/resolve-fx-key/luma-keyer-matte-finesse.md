# Luma keyer matte finesse

Version: DaVinci Resolve 20.3 Reference Manual. Context: Luma keyer.
[Chapter index](INDEX.md) / [Previous section](hsl-keyer-keyer-options.md)
<a id="source-garbage-matte"></a> <a id="source-luma-keyer"></a> <a id="source-luma-keyer-selection-range-controls"></a> <a id="source-matte-finesse"></a> <a id="source-output"></a> <a id="source-selection-range-controls"></a>

### Luma Keyer

Built on the Luma Qualifier from the Color page, the Luma Keyer derives a key from the luma channel. It behaves just like the HSL Keyer with H and S switched off. It's rarely employed on its own, but the Luma Keyer can deliver handy results when paired with Composite modes.

### Selection Range Controls

Using the Selection Range buttons in the Inspector, you define a key by sampling pixels inside the Viewer with the mouse pointer.

### Luma Keyer Selection Range controls

- Sample Eyedropper: The very first control you reach for any time you sample the image. It establishes the keyer's starting range; this tool has to be used ahead of all the others. On the Edit page, the Timeline Viewer Overlay needs to be set to Open FX. A single click with it grabs one pixel value, whereas clicking and dragging grabs a span of image values that accumulate.
- Add/Subtract Luma Range: This pair of controls lets you bring image regions into, or take them out of, the luma range currently selected as the core of the key. Just like the eyedropper, you can click individual pixels or drag across a span of color.
- Add/Subtract Softness: This pair of controls lets you reshape the softness transitioning from the key's inner range and tapering toward its outer edge. As with the other keying controls, you can click individual pixels or drag across a span of color.
- Invert: Flips the sampled luma range so it becomes opaque, and the regions that weren't sampled become transparent.
- Reset: Clears the sampled luma range while keeping the Output control settings intact.

### Matte Finesse

Sampling the screen color alone may turn out to be insufficient for certain problems. Trouble such as chattery edges, holes, or noise can often be addressed with the Matte Finesse controls. They filter what the Keyer outputs and act on the matte itself, reshaping the key according to the content of the frame.

- Pre Filter: This slider tries to tidy up the image ahead of color sampling. It can come in handy when your footage carries MPEG blocking artifacts.
- Clean Black: Clean Black is a dedicated operation that removes noise appearing as white speckling across the black region of a key. Pushing Clean Black up lets you "fill holes" in the background part of a key and erode translucent edges.
- Clean White: Clean White is a second dedicated operation that removes noise (appearing as black speckling when you view a high-contrast highlight) within the white region of a key that covers the parts of the image you're isolating, and it grows the key by brightening light areas of a key the higher you push this parameter, driving light gray portions of the key toward white. In practice, raising Clean White lets you "fill holes" in the foreground part of a key and grow translucent edges.
- Black Clip: Pushing Black Clip up applies a "lift" adjustment so that translucent regions of the matte (the gray areas when you view a high-contrast highlight) get driven black-ward. Its range runs 0 to 100, where 0 is the default.
- White Clip: Pulling White Clip down applies a "gain" adjustment so that translucent regions of the matte (the gray areas when you view a high-contrast highlight) get driven white-ward. Its range runs 0 to 100, where 100 is the default.
- Blur Radius: At small settings, blurring a key works nicely to soften problem edges. That said, blurring a key can also spread the key's edges beyond the outline of the subject you're keying, producing a visible "halo" around your subject depending on how far you push it. The range is 0 to 2000, with 0 being the default. Given how high that maximum blur radius goes, together with what the In/Out Ratio offers for shaping the direction of the spread, you can convert some rather sketchy mattes into surprisingly smooth, usable results.
- In/Out Ratio: Reaching for In/Out Ratio can help get rid of fringing. Raising In/Out Ratio fills in tiny black holes within the matte, while dropping In/Out Ratio below 0 clears speckling by driving small white specks of the matte toward black.
- Morph Operation: Pick Shrink or Grow to dilate or erode the matte's edges, or pick Opening or Closing to plug or open up holes in order to tidy a ragged matte.
- Morph Radius: Sets how far to shrink, grow, open, or close the key.
- Denoise: Offers a separate approach to post-processing pulled keys to selectively cut the noise in

a key, clearing away stray pockets of qualification and gently filling holes in a matte.

- Shadow: Tunes key strength according to the darker portions of the original image.
- Midtone: Tunes key strength according to the midtones of the original image.
- Highlight: Tunes key strength according to the brighter portions of the original image.
- Post Filter: Carries out a last clean-up of the key, referencing the original image; handy for

restoring some fine detail along sharp edges or in hair.

### Garbage Matte

These controls let you mask off other unwanted elements in the frame, like lighting fixtures, boom microphones, tracking patches, and so on.

- Matte Shape: Pick either a Rectangle or Ellipse to crop around the subject you're keying. Picking None switches off Garbage Matte. With a garbage matte active, the Open FX Overlay mode of the Viewer presents an on-screen control for setting the shape and position of the garbage matte.
- Edge Softness: Lets you feather the borders. Its default sits at 50 and it spans 0 (no softening) up to 100 (maximum softening).
- Invert: Flips the garbage matte.
- Center X and Y: Lets you set and keyframe a garbage matte's position.
- Bounding Width and Height: Lets you set the garbage matte's width and height.
- Rotation: Lets you set the garbage matte's angle.

### Output

With the Output controls you decide how the image is output, composited, and shown in the Viewer.

- Output: This menu gives three choices for which channels the effect outputs. Alpha Highlight: Renders the see-through portion of an Alpha channel in gray while showing the opaque portion of that alpha channel at full color. Alpha Highlight B/W: Renders the black and white Alpha channel, which often helps when you're sampling extra regions to key. Final Composite: The keyed image appears composited over whatever video track lies below it.
- Use Alpha: A control found across many Resolve FX and 3rd party Open FX plugins; this checkbox sets whether the Alpha channel is used when compositing over another video track. You can use it in place of selecting RGB Only (Blank Alpha) from the Output menu.

Keying a subject with the Luma Keyer on the Edit page goes like this: 1. Add the Luma Keyer onto a clip sitting on video track 2 or higher. 2. Within the Timeline Viewer, open the Viewer Overlay menu (down in its lower-left corner) and pick Open FX Overlays. 3. Either click on a pixel within a light or shadowed area of the picture you'd like keyed out, or click and drag over a stretch of pixels inside that subject. 4. Transparency kicks in right away, presenting the keyed subject over whichever clip sits on the video track below it in the Timeline as a composite. To inspect and keep refining the matte you built, pick either Alpha Highlight or Alpha Highlight B/W under the Output drop-down menu. 5. To grow or shrink the matte, click the plus or minus Luma Range buttons, then click or drag across that part of the keyed image. 6. To soften the outer boundary of the key you're building, click the plus Softness button and then click or drag over the region of the image you want treated as a soft edge.
