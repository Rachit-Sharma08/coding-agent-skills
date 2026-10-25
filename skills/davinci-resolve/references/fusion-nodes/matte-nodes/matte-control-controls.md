# Matte control controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Matte control.
[Chapter index](INDEX.md) / [Previous section](magic-mask-and-matte-control.md) / [Matte Control MAT](magic-mask-and-matte-control.md) / [Next section](matte-control-and-primatte.md)
<a id="source-matte-nodes-part-4"></a> <a id="source-matte-tab-1"></a> <a id="source-the-matte-control-matte-tab"></a>

### The Matte Control Matte tab

### Matte Tab

The Matte tab merges and reshapes alpha or color channels drawn from an image on the foreground input together with the background image. Combine Reach for this menu to choose which operation runs. It defaults to None, meaning no operation.

- None: This makes the foreground image be disregarded.
- Combine Red: This merges the foreground red channel into the background alpha channel.
- Combine Green: This merges the foreground green channel into the background alpha channel.
- Combine Blue: This merges the foreground blue channel with the background alpha channel.
- Combine Alpha: This merges the foreground alpha channel with the background alpha channel.
- Solid: This drives the background alpha channel to become fully opaque.
- Clear: This drives the background alpha channel to become fully transparent.

Combine Operation Reach for this menu to choose the method that merges the foreground channel with the background.

- Copy: This copies the foreground source over the background alpha, overwriting whatever alpha already exists in the background.
- Add: This adds the foreground source to the background alpha.
- Subtract: This subtracts the foreground source from the background alpha.
- Inverse Subtract: This subtracts the background alpha from the foreground source.
- Maximum: This weighs the foreground source against the background alpha and keeps the value

from whichever pixel is highest.

- Minimum: This weighs the foreground source against the background alpha and keeps the value

from whichever pixel is lowest.

- And: This runs a logical AND across the two values.
- Or: This runs a logical OR across the values.
- Merge Over: This lays the foreground source channel atop the background’s alpha channel and blends the two.
- Merge Under: This tucks the foreground source channel beneath the background’s alpha channel and blends the two.

Filter Picks the Filter used to blur the matte.

- Box Blur: This option lays a Box Blur effect over the whole image. It’s quicker than the Gaussian blur but yields lower quality.
- Bartlett: Bartlett lays down a gentler, anti-aliased blur filter.
- Multi-Box: Multi-Box stacks a box filter across several passes to mimic a Gaussian shape.

Running a modest count of passes (four, say) yields a high-quality blur, frequently quicker than the Gaussian filter and free of ringing.

- Gaussian: Gaussian lays down a smooth, symmetrical blur filter by way of a refined constant-time Gaussian approximation algorithm. Under extreme conditions that algorithm can show ringing, which is covered below. This serves as the default filter method.

Blur Softens the matte's edge with an ordinary, constant-speed Gaussian blur. Set it to zero and you get a crisp, cutout-style hard edge. Raise the value and progressively more blur gets applied to the matte.

Clipping Mode This setting governs the treatment of edges while domain of definition rendering takes place. It matters enormously when you blur the matte, since that can demand samples drawn from parts of the image beyond the present domain.

- Frame: Frame is the default, automatically configuring the node’s domain of definition to span the image's full frame and thereby disregarding the current domain of definition. When the upstream DoD comes in smaller than the frame, the leftover frame area counts as black/transparent.
- Domain: Switching this to Domain honors the upstream domain of definition as the node’s effect is applied. With a large filter in play, that can produce undesirable clipping.
- None: Picking None skips source image clipping entirely. Consequently, whatever data the node’s effect needs that ordinarily lies beyond the upstream DoD is taken as black/transparent.

Contract/Expand Shrinks or grows the matte much like an Erode Dilate node does. Pulling the matte in exposes more of the foreground input, whereas pushing it out exposes more of the background input. A value over 0.0 expands the matte; a value under 0.0 contracts it. Gamma Lifts or drops the matte's values throughout the semitransparent regions. Larger values render the gray areas more opaque, smaller values render them more transparent, while fully black or white parts of the matte stay untouched. Threshold Anything beneath the lower threshold turns black or transparent in the matte; anything above the upper threshold turns white or opaque. Everything in between holds onto its relative transparency. Restore Fringe Brings back the matte's edge surrounding the keyed subject. Keying frequently clips away the subject's edge wherever hair appears; Restore Fringe recovers that edge yet keeps the matte solid. Invert Matte Ticking this checkbox flips the image's alpha channel, so every transparent area turns opaque and every opaque area turns transparent. Solid Matte A solid matte is a mask node or image wired into the node's solid matte input. It feeds straight onto the image's alpha channel. Typically a solid matte holds out regions you want kept opaque, like someone with blue eyes shot against a blue screen. Turning on Invert flips the solid matte ahead of merging it with the source alpha. Garbage Matte A garbage matte is a mask node or image wired into the node's garbage matte input. It too feeds straight onto the image's alpha channel. Typically a garbage matte strips out unwanted items that resist keying, such as microphones and booms. It also fills in regions holding the keyed color that you nonetheless want to keep.

You can't blend garbage mattes of differing modes inside one tool. A Matte Control node frequently sits after a Keyer node to introduce a garbage matte whose effect opposes the matte fed to the keyer. Turning on Invert flips the garbage matte ahead of merging it with the source alpha. Post-Multiply Image Choosing this multiplies the image's color channels against the alpha channel it builds for the image. It's normally enabled and on by default. Clear this checkbox and the image stops counting as premultiplied for the sake of merging it with others. Reach for the Subtractive option of the Merge node rather than the Additive one. For fuller detail on these Merge node settings, turn to Chapter 95, "Composite Nodes," within the DaVinci Resolve Reference Manual, or else to Chapter 35 of the Fusion Reference Manual.
