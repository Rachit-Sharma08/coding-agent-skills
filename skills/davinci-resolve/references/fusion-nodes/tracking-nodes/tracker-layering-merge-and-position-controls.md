# Tracker layering merge and position controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Tracker.
[Chapter index](INDEX.md) / [Previous section](tracker-operation-tab.md) / [Next section](tracker-and-common-controls.md) / [Tracker Tra](tracker-a-tracker-node-branched-from-the-node-tree.md)
<a id="source-additional-layering-controls"></a>

### Additional Layering Controls

Picking any operation besides None makes a set of extra controls appear. Merge What the Merge control settles is what happens (if anything at all) to the image fed into the green Foreground input of the Tracker. This menu surfaces once the operation is set to anything other than None.

- BG Only: The foreground input goes unused; only the background is touched. This serves chiefly when you're stabilizing the background image.
- FG Only: The foreground input gets transformed to track the movement in the background, and that transformed image passes out through the Tracker's output. This Merge approach comes into play when match moving the motion of one layer onto another layer's motion.
- FG Over BG: The foreground image lands over the background image, drawing on the Merge method spelled out by the Apply Mode control that appears.
- BG Over FG: The background lands over the foreground. People often reach for this approach when tracking a layer that carries an Alpha channel, so that a more static background can sit behind it.

Apply Mode and Operator Menus A range of options that decide how the two layers ought to combine is offered by this menu. The choices held in this menu match exactly the ones found in the Merge node.

- Apply Modes: What the Apply Mode setting fixes is the math that runs when the foreground and background pixels are blended or combined.

Normal: The Default merge mode treats the foreground's alpha channel as a mask that decides which pixels are transparent and which aren't. While it's active, a further menu surfaces the possible operations, among them Over, In, Held Out, Atop, and XOr. Screen: Screen merges the images by multiplying their color values together. The alpha channel goes ignored and layer order ceases to matter. The color you end up with always comes out lighter. Screening against black leaves the color as it was, whereas screening against white yields white every time. The effect resembles projecting several film frames onto one surface. While it's active, a further menu surfaces the possible operations, among them Over, In, Held Out, Atop, and XOr. Dissolve: Dissolve blends two image sequences into one. It draws on a computed average of the two images to carry out the mixture. Multiply: Multiplies a color channel's values. This lends the look of darkening the image as the values scale from 0 to 1. White carries a value of 1, so the outcome would stay the same. Gray carries a value of 0.5, so the outcome would be a darker image — put another way, an image half as bright. Overlay: Depending on the background image's color values, Overlay either multiplies or screens the foreground image's color values. Patterns or colors lie over the existing pixels while the background image's color-value highlights and shadows are kept intact. Rather than being replaced, the background image is mixed with the foreground image so that the background image's original lightness or darkness comes through. Soft Light: Depending on the background image's color values, Soft Light either darkens or lightens the foreground image. The result is akin to aiming a diffused spotlight at the image. Hard Light: Depending on the background image's color values, Hard Light either multiplies or screens the foreground image's color values. The result is akin to aiming a harsh spotlight at the image. Color Dodge: Color Dodge draws on the foreground's color values to brighten the background image. This parallels the photographic trick of dodging, where exposure across a region of a print is cut back. Color Burn: Color Burn draws on the foreground's color values to darken the background image. This parallels the photographic trick of burning, where exposure across a region of a print is increased. Darken: Darken examines the color information in each channel and picks whichever color value — the background's or the foreground's — runs darker as the result color. Pixels lighter than the merged colors get replaced, while pixels darker than the merged color hold steady.

Lighten: Lighten examines the color information in each channel and picks whichever color value — the background's or the foreground's — runs lighter as the result color value. Pixels darker than the merged color get replaced, while pixels lighter than the merged color hold steady. Difference: Difference looks at each channel's color information and, depending on whichever carries the greater brightness value, takes the foreground color values away from the background ones — or the background away from the foreground. Merging against white inverts the color. Merging against black leaves it unchanged. Exclusion: Exclusion yields an effect much like the Difference mode but lower in contrast. Merging against white inverts the base color values. Merging against black leaves it unchanged. Hue: Hue builds a result color out of the luminance and saturation of the background color values together with the hue of the foreground color values. Saturation: Saturation builds a result color out of the luminance and hue of the base color together with the saturation of the blend color. Color: Color builds a result color out of the luminance of the background color value together with the hue and saturation of the foreground. It keeps the image's gray levels and proves handy for coloring monochrome images. Luminosity: Luminosity builds a color out of the hue and saturation of the background color together with the luminance of the foreground color. This mode produces the inverse of what the Color mode does.

- Operator Modes: Selecting the merge's Operation Mode is what this menu is for. It settles how the foreground and background get combined to yield a result. You'll only see this drop-down menu while the Merge node's Apply Mode sits at either Normal or Screen.

NOTE: Should you want an outstanding account of the math that drives the Operation modes, the source to read is "Compositing Digital Images" — a paper credited to Porter, T., and T. Duff that ran in the SIGGRAPH 84 proceedings, across pages 253-259. In essence, the math runs as laid out below.

TIP: A handful of modes absent from the Operator drop-down menu (Under, In, Held In, Below) come easily by swapping the foreground and background inputs and selecting a matching mode. Combining pixels in the merge always follows the formula fg _ x + bg _ y. Which values x and y take is what the different operations decide, as the description for each mode lays out. The Operator modes run as follows:

- Over: The Over mode lays the foreground layer atop the background layer by swapping the

background pixels for the pixels from the Z wherever the foreground's alpha channel exceeds 1. x = 1, y = 1-[foreground Alpha]

- In: The In mode multiplies the background input's alpha channel against the foreground pixels. The foreground input's color channels go ignored. Only foreground pixels reach the final output. This in effect clips the foreground using the background's mask.

x = [background Alpha], y = 0

- Held Out: Held Out is in essence the reverse of the In operation. Here the pixels of the foreground image get multiplied by the background image's inverted alpha channel. The identical outcome is reachable through the In operation paired with a Matte Control node that inverts the matte channel of the background image.

x = 1-[background Alpha], y = 0

- ATop: ATop sets the foreground over the background only where the background carries a matte.

x = [background Alpha], y = 1-[foreground Alpha]

- XOr: XOr joins the foreground with the background wherever either the foreground or the background carries a matte, yet never where both carry one.

x = 1-[background Alpha], y = 1-[foreground Alpha]

- Subtractive/Additive: Whether Fusion runs an Additive merge, a Subtractive merge, or some blend of the pair is governed by this slider. For most operations the slider defaults to Additive merging, on the assumption that the input images are premultiplied (as they usually are). Should the gap between Additive and Subtractive merging be unclear to you, here's a brief rundown:
- An Additive merge is called for when the foreground image is premultiplied, meaning that within the color channels the pixels have already been multiplied by those of the alpha channel. The upshot is that transparent pixels stay black at all times, since anything multiplied by 0 always comes to 0. This hides the background (through multiplication with the inverse of the foreground alpha), then merely adds the foreground pixels on top.
- A Subtractive merge is called for if the foreground image isn't premultiplied. The compositing method mirrors an Additive merge, except the foreground image gets multiplied by its alpha first to wipe out any background pixels lying outside the alpha area. Across most software applications, you'll see the Additive/Subtractive option shown as a plain checkbox. Fusion lets you blend across the Additive and Subtractive variants of the merge operation, which now and then helps with troublesome composites whose edges draw the eye for reading too bright or too dark.

To take an example, applying a Subtractive setting to a premultiplied image can leave you with darker edges. Applying an Additive setting to a non-premultiplied image can lighten the edges. By blending across Additive and Subtractive, you can dial the edge brightness in until it's exactly right for your situation. Filter Method (Match Move) Settles which filter handles image transforms produced through the Tracker node. This menu shows up only while the Operation Mode is set to Match Move.

- Box: A plain interpolation-based resize of the picture.
- Linear: Relies on a bare-bones filter that turns out fairly clean, quick results.
- Quadratic: Yields a middling result from this filter. Between

speed and quality it strikes a fair balance.

- Cubic: Yields stronger results on continuous-tone pictures, though it runs slower than Bi‑Cubic.

Where the pictures hold fine detail, the outcome can come out blurrier than you'd want.

- Catmull-Rom: Yields solid results on continuous-tone pictures scaled down.

On finely detailed pictures it turns out sharp results.

- Gaussian: Sits very close to Bi-Cubic in both speed and quality.
- Mitchell: Resembles Catmull-Rom yet turns out stronger results on finely detailed pictures. Compared to Catmull-Rom it runs slower.
- Lanczos: Sits very close to Mitchell and Catmull-Rom, just a touch cleaner and a touch slower as well.
- Sinc: A high-end filter delivering exceptionally sharp, detailed results; that said, it can throw

visible "ringing" under certain conditions.

- Bessel: Resembles the Sinc filter though it may run a shade faster.

Edges Which way the revealed edges get treated, once the image has shifted to match position and scaling, is what this menu picks.

- Black Edges: Whatever out-of-frame edges Stabilization exposes are left black.
- Wrap: Whatever stretches of the image get pushed off frame on one side go toward filling the edges exposed

on the opposite side.

- Duplicate: The final valid pixel along an edge gets repeated outward to the frame's edge.
- Mirror: To fill out to the frame's edge, the image's pixels are mirrored.

Position, Rotation, and Scaling Checkboxes (Match Move) This trio of checkboxes surfaces only while the mode sits at Match Move. They settle which components of motion Stabilization will try to correct in the image. As one case, when nothing but the Position checkbox is ticked, no attempt is made at fixing the image's Rotation and Scaling. Flatten Transformation (Match Move) This particular checkbox surfaces only while the mode rests at Match Move. As with most transformations in Fusion, Stabilization concatenates with other sequential transformations by default. Ticking this checkbox flattens the transform, severing any concatenation under way and applying the transform right away. Mapping Type The Mapping Type control surfaces only within the Corner Positioning mode. Two options sit in the menu:
