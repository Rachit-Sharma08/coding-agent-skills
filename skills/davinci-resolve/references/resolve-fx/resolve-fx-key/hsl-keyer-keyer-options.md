# Hsl keyer keyer options

Version: DaVinci Resolve 20.3 Reference Manual. Context: Hsl keyer.
[Chapter index](INDEX.md) / [Previous section](3d-keyer-and-alpha-matte-shrink-and-grow-and-hsl-keyer.md) / [HSL Keyer](3d-keyer-and-alpha-matte-shrink-and-grow-and-hsl-keyer.md) / [Next section](luma-keyer-matte-finesse.md)
<a id="source-garbage-matte-1"></a> <a id="source-hsl-keyer-options"></a> <a id="source-keyer-options"></a> <a id="source-matte-finesse-1"></a> <a id="source-output-1"></a> <a id="source-resolve-fx-key-part-2"></a>

### Keyer Options

A notable strength of the HSL Keyer is that each of the three HSL components can be switched on or off through the Hue, Sat, and Lum checkboxes. That lets you skip particular color components while zeroing in on others that might matter more. As an example, when you’re after keying the saturated portions of a picture, no matter the hue or brightness, you can switch off Hue and Lum so only Sat drives the sampling.

### HSL Keyer options

### Matte Finesse

Sampling the screen color on its own may prove insufficient for clearing certain problems. Trouble like chattery edges, holes, or noise can occasionally be sorted out by way of the Matte Finesse controls. These controls filter the Keyer’s output and stand as adjustments laid on the matte itself, reworking the key through the frame’s content.

- Pre Filter: With this slider the image gets a cleanup pass before any colors are sampled. The adjustment can pay off where your footage carries MPEG blocking artifacts.
- Clean Black: Clean Black is a dedicated operation that strips noise showing as white speckling across the black region of a key. Lifting Clean Black lets you “fill holes” throughout the background portion of a key and wear down translucent edges.
- Clean White: Clean White is a further dedicated operation that strips noise (showing as black speckling when you view a high-contrast highlight) across the white portion of a key that takes in areas of the image you’re isolating, and it grows the key by making bright parts of a key brighter the more you lift this parameter, nudging light gray regions of the key toward white. In practice, lifting Clean White lets you “fill holes” throughout the foreground portion of a key and grow translucent edges.
- Black Clip: Lifting Black Clip lays on a “lift” adjustment so that translucent regions of the matte (the gray regions when you view a high-contrast highlight) get nudged toward black. Its range runs 0 to 100, with 0 as the default setting.
- White Clip: Dropping White Clip lays on a “gain” adjustment so that translucent regions of the matte (the gray regions when you view a high-contrast highlight) get nudged toward white. Its range runs 0 to 100, with 100 as the default setting.
- Blur Radius: At modest amounts, blurring a key does a fine job of softening troublesome edges. Yet blurring a key can equally feather a key’s edges out past the boundary of the subject you’re keying, leaving a visible “halo” around your subject, according to the adjustment you make. Its range runs 0 to 2000, with 0 as the default. Given so large a maximum blur radius, together with what the In/Out Ratio offers for shaping the direction of spread, you can convert some rather dicey mattes into surprisingly smooth, usable results.
- In/Out Ratio: Reaching for In/Out Ratio can help wipe out fringing. Lifting In/Out Ratio will pack small black holes in the matte, whereas dropping In/Out Ratio below 0 will clear speckling by nudging small white bits of the matte toward black.
- Morph Operation: Pick Shrink or Grow to dilate or erode the matte’s edges, or pick Opening or Closing to plug or open holes so a ragged matte gets cleaned up.
- Morph Radius: Sets the degree to which the key is shrunk, grown, opened, or closed.
- Denoise: Offers a separate route to post-process pulled keys so a key’s noise gets selectively cut, clearing stray patches of qualification and gently packing holes in a matte.
- Shadow: Tunes key strength off the darker portions of the original image.
- Midtone: Tunes key strength off the midtones of the original image.
- Highlight: Tunes key strength off the brighter portions of the original image.
- Post Filter: Runs a closing cleanup of the key, leaning on the original image as reference; handy for restoring some fine detail across sharp edges or hair.

### Garbage Matte

Through these controls you can crop away other stray things in the frame, such as lighting fixtures, boom microphones, tracking patches, and so on.

- Matte Shape: Pick either a Rectangle or Ellipse to crop around whatever subject you’re keying. Picking None switches Garbage Matte off. With a garbage matte switched on, the Viewer’s Open FX Overlay mode surfaces an on-screen control for tuning the garbage matte’s shape and position.
- Edge Softness: Lets you soften the edges. The default is 50; its range runs 0 (no softening) to 100 (maximum softening).
- Invert: Flips the garbage matte.
- Center X and Y: Lets you tune and keyframe a garbage matte’s position.
- Bounding Width and Height: Lets you tune the garbage matte’s width and height.
- Rotation: Lets you tune the garbage matte’s angle.

### Output

Through the Output controls you pick how the image gets output, composited, and shown in the Viewer.

- Output: This menu hands you three options for which channels come out of the effect. Alpha Highlight: Shows an Alpha channel’s transparent part as gray and an alpha channel’s solid part in full color. Alpha Highlight B/W: Shows the black and white Alpha channel, frequently of help while sampling further areas to key. Final Composite: The keyed image gets shown composited over whatever video track sits beneath it.
- Use Alpha: A widespread control across many Resolve FX and 3rd party Open FX plugins; this checkbox sets whether the Alpha channel comes into play while compositing over another video track. It serves in place of picking RGB Only (Blank Alpha) off the Output menu.

Working with the HSL Keyer on the Edit page goes like this: 1. Add the HSL Keyer onto a clip sitting on video track 2 or higher. 2. Within the Timeline Viewer, open the Viewer Overlay menu (down in its lower-left corner) and pick Open FX Overlays. 3. Drag across the on-screen color that you want taken out. 4. Transparency kicks in right away, presenting the keyed subject over whichever clip sits on the video track below it in the Timeline as a composite. To inspect and keep refining the matte you built, pick either Alpha Highlight or Alpha Highlight B/W under the Output drop-down menu. 5. To grow or shrink the matte, click the plus or minus Color Range control, then click or drag across that part of the keyed image. 6. To soften the outer boundary of the key you're building, click the plus Softness control and then click or drag over the region of the image you want treated as a soft edge.
