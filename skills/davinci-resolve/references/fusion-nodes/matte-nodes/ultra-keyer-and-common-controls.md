# Ultra keyer and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Ultra keyer, Common controls.
[Chapter index](INDEX.md) / [Previous section](ultra-keyer-inputs.md) / [Next section](common-controls-controls.md) / [Ultra Keyer UKY](relight-and-ultra-keyer.md)
<a id="source-basic-node-setup"></a> <a id="source-common-controls"></a> <a id="source-image-tab"></a> <a id="source-inspector"></a> <a id="source-matte-tab"></a> <a id="source-pre-matte-tab"></a> <a id="source-subtract-background"></a> <a id="source-the-common-controls"></a> <a id="source-the-ultra-keyer-image-tab"></a> <a id="source-the-ultra-keyer-matte-tab"></a> <a id="source-the-ultra-keyer-pre-matte-tab"></a>

### Basic Node Setup

Most green- or blue-screen footage carries issues the keyer was never built to address, so one lone keyer seldom produces flawless output. To cope, keyers frequently lean on garbage mattes or solid mattes drawn with a Polygon or B-Spline node. Some shots demand more than a single keyer before the result is clean. In the example below, the blue-screen footage feeds into the orange input of the Ultra Keyer node. What comes out is an image carrying alpha, ready to be routed into the foreground of a Merge node.

A polygon matte feeding the garbage matte of an Ultra Keyer node, whose output wires into a Merge node's foreground

### Inspector

### The Ultra Keyer Pre-Matte tab

### Pre-Matte Tab

Keying typically gets underway in the Pre-Matte tab. Its job is to pick the screen color and even out the screen's coloration. Background Color The Background Color picks out the hue of the blue or green screen in the imagery. As a rule, sample the screen color near the subject you're trying to lift away from its screen background. Red Level, Green Level, Blue Level These color sliders dial in the level of the difference channels so the color can be pulled apart more cleanly. With a green background color, Red and Blue level options show up. With a blue background color, Red and Green level options show up instead. Background Correction Based on whichever background color you picked above, the keyer repeatedly composites the pre-keyed image over a blue or green background before carrying processing further. This sometimes yields cleaner, more refined edges. Matte Separation Matte Separation runs a pre-process across the image to assist in pulling foreground from background ahead of color selection. As a general approach, raise this control while watching the alpha to clear away most of the background, but halt right before it begins punching holes in the subject or chewing up fine detail along the matte's edges. Pre-Matte Range These R,G,B, and Luminance range controls refresh on their own to mirror the current color selection. You select colors by clicking the Ultra Keyer node's tile within the node tree and dragging the Eyedropper across the viewer to grab the colors that will build the matte. While these range controls let you nudge the selection a bit, picking colors in the viewer is really all you have to do.

Lock Color Picking Ticking this checkbox guards against picking up extra colors from the view by accident. Switching it on once you've settled the color selection for the matte is a wise move. The node's remaining controls stay fully editable. Pre Matte Size You can apply the Pre Matte Size control to soften the broad region surrounding the keyed image. It serves to seal holes in the matte that spill in semitransparent parts of the subject often produces. A faint halo may appear around the subject as a result, and that can be cleared away with the Matte Contract tools provided further along in the tool. Reset Pre Matte Ranges This throws out every color selection by resetting the ranges, yet leaves all the other slider and control values untouched.

### The Ultra Keyer Image tab

### Image Tab

Most of the spill suppression in the Ultra Keyer is dealt with on the Image tab. A type of color correction, spill suppression works to strip the screen color away from the matte's fringe. Spill refers to the screen color bleeding through the semitransparent regions of the alpha channel. For blue- or green-screen keying, the upshot is usually that the backdrop's color shows up along the edges of the foreground subject. Spill Suppression With this slider at 0, the image receives no spill suppression whatsoever. Pushing the slider up strengthens the spill method. Spill Method This picks how aggressive the algorithm is when applying spill suppression to the image.

- None: Pick None whenever spill suppression isn't needed.
- Rare: Stripping only a sliver of the spill color, this is the gentlest of every method.
- Medium: This works best for green screens.
- Well Done: This works best for blue screens.
- Burnt: Best for blue screens as well; reserve this mode for only the most stubborn shots.

Fringe Gamma You can apply this control to alter how bright the fringe or halo encircling the keyed image is. Fringe Size This grows and shrinks how big the fringe or halo around the keyed image is. Fringe Shape Fringe Shape either pushes the fringe out toward the image's outer edge or draws it inward toward the fringe's inner edge. Its effect is most visible while a large value sits in Fringe Size. Cyan/Red, Magenta/Green, and Yellow/Blue Reach for these three controls to color correct the image's fringe. They help when semitransparent pixels still hold color from the original backdrop and need to be matched to the new one.

.

### The Ultra Keyer Matte tab

### Matte Tab

The Matte tab tunes the key's alpha together with whatever solid and garbage masks are wired to the node. As you work in the Matte tab, aim the viewer at the final output's alpha channel from the Delta Keyer. Filter This control picks which filtering algorithm gets used when blur is applied to the matte.

- Box: The quickest method, though quality drops. Box suits small amounts of blur best.
- Bartlett: Also called a Pyramid filter, Bartlett strikes a solid balance between speed

and quality.

- Multi-Box: Pick this filter and the Num Passes slider shows up, handing you control over quality. With 1 and 2 passes, output matches Box and Bartlett in turn. From 4 passes upward, output is generally on par with Gaussian, faster and free of edge “ringing.”
- Gaussian: Built on a true Gaussian approximation, the Gaussian filter delivers excellent output, albeit a touch slower than the rest. On occasion it can yield an extremely faint edge “ringing” on floating-point pixels.

Blur Matte Blur softens the matte's edge in line with whatever the Filter menu is set to. Set it to zero and you get a crisp, cutout-style hard edge. Raise the value and more blur lands on the matte. Clipping Mode This setting governs how edges get treated while domain of definition rendering is taking place. It matters enormously when you blur the matte, since that may pull samples from areas of the image lying beyond the current domain.

- Frame: Frame is the default, and it has the node's domain of definition span the image's full frame automatically, effectively disregarding the current domain of definition. Should the upstream DoD fall short of the frame, whatever's left in the frame counts as black/transparent.
- Domain: Choosing Domain honors the upstream domain of definition while the node's effect is applied. Adverse clipping can result wherever the node relies on a large filter.
- None: Choosing None skips any source image clipping entirely. So any data the node's effect needs to process that would ordinarily sit beyond the upstream DoD counts as black/transparent.

Contract/Expand This slider either contracts or enlarges the matte's semitransparent regions. Values over 0.0 expand the matte, whereas values under 0.0 contract it. You typically pair this control with the Matte Blur to soften a matte's hard edge and cut fringing. Because the control touches only semitransparent regions, it leaves a matte's hard edge alone. Gamma Matte Gamma pushes the matte's values in the semitransparent regions up or down. Higher settings make the gray zones more opaque, while lower ones make those gray zones more transparent. Fully black or white parts of the matte stay untouched. Since this control only reaches semitransparent regions, it has no bearing on a matte's hard edge. Threshold This range slider establishes the lower threshold with the left handle and the upper threshold with the right handle. Anything beneath the lower threshold setting turns black or transparent in the matte. Anything above the upper threshold setting turns white or opaque in the matte. Everything sitting inside the range keeps its relative transparency values intact. People often reach for this control to throw out salt and pepper noise in the matte.

Restore Fringe This brings the matte's edge back around the keyed subject. Frequently while keying, the subject's edge where hair sits gets cut away. Restore Fringe recovers that edge while leaving the matte solid. Invert Matte Tick this checkbox and the alpha channel the keyer built gets flipped, turning every transparent region opaque and every opaque region transparent. Solid Matte Solid mattes are mask nodes or images wired to the node's solid matte input. The solid matte lands straight on the image's alpha channel. Typically you use solid mattes to fence off keying in regions meant to stay opaque, like a person with blue eyes shot against a blue screen. Switch on Invert and the solid matte is flipped ahead of combining with the source alpha. Garbage Matte A garbage matte is a mask node or image wired to the node's garbage matte input. The garbage matte lands straight on the image's alpha channel. Typically garbage mattes serve to strip out unwanted items that resist keying, such as microphones and booms. They also fill in regions holding the keyed color that you nonetheless want to keep. You cannot blend garbage mattes of differing modes inside one tool. People frequently drop a Matte Control node after a Keyer node to introduce a garbage matte whose effect opposes the matte sitting on the keyer. Turning on Invert flips the garbage matte before it merges with the source alpha. Post-Multiply Image Pick this option and the keyer multiplies the image's color channels against the alpha channel it generates for that image. This option is usually enabled and is on by default. Untick this checkbox and the image can no longer count as premultiplied for the sake of merging it with other imagery. Turn instead to the Merge node's Subtractive option in place of its Additive one. Those Merge node settings are documented more fully in the DaVinci Resolve Reference Manual under Chapter 95, "Composite Nodes" — equivalently, the Fusion Reference Manual covers them at Chapter 35.

### Subtract Background

When the screen color gets stripped and anti-aliased against a black background, this option color corrects the resulting edges. Switching it on can leave those edges somewhat darker. Leaving it off lets you carry the screen's color forward for use in other downstream processes.

### Common Controls

Settings Tab Other matte nodes carry a duplicate of the Settings tab found in the Inspector. The “The Common Controls” section coming up next covers these shared controls thoroughly.

### The Common Controls

Across the nodes that perform matte operations, a set of identical controls shows up in the Inspector. The controls shared among matte nodes are laid out in this section.
