# Clean black and before after raising black clip

Version: DaVinci Resolve 20.3 Reference Manual. Context: Secondary qualifiers.
[Chapter index](INDEX.md) / [Previous section](draggable-qualifier-controls-and-hsl-qualification-controls.md)
<a id="source-adding-multiple-keys-together-using-a-key-mixer"></a> <a id="source-beforeafter-lowering-white-clip"></a> <a id="source-beforeafter-raising-black-clip"></a> <a id="source-blur-radius"></a> <a id="source-clean-black"></a> <a id="source-clean-white"></a> <a id="source-combining-qualifiers-and-windows"></a> <a id="source-denoise"></a> <a id="source-highlight"></a> <a id="source-manipulating-keys-using-additional-nodes"></a> <a id="source-midtone"></a> <a id="source-post-filter"></a> <a id="source-shadow"></a> <a id="source-the-many-ways-to-invert-a-key"></a> <a id="source-white-clip"></a>

### Clean Black

Clean Black is a dedicated operation that removes noise (which reads as white speckling against a high-contrast highlight) in the black region of a key — the part that drops the areas you don't want isolated — and tightens the key by darkening its dark portions further as you push this

parameter up, driving dark gray key areas toward black. In practice, turning Clean Black up lets you "fill holes" in a key's background portion and chew back translucent edges.

Before/after raising Clean Black, viewing the high contrast matte Black Clip Pushing Black Clip up applies a "lift" so that translucent matte regions (the gray areas under a high-contrast highlight) get driven toward black. Its scale spans 0 to 100, where the default sits at 0.

### Before/after raising Black Clip

### Clean White

Clean White is a second dedicated operation that removes noise (which reads as black speckling against a high-contrast highlight) in the white portion of a key — the part covering the areas you are isolating — and stretches the key by brightening its light portions further as you push this parameter up, driving light gray key areas toward white. In practice, turning Clean White up lets you "fill holes" in a key's foreground portion and extend translucent edges.

Before/after raising Clean White, viewing the high contrast matte

### White Clip

Pulling White Clip down applies a "gain" so that translucent matte regions (the gray areas under a high-contrast highlight) get driven toward white. Its scale spans 0 to 100, where the default sits at 100.

### Before/after lowering White Clip

### Blur Radius

A touch of blur on a key works nicely to soften troublesome edges. That said, blurring can also spread a key's edges past the outline of whatever you're keying, leaving a noticeable "halo" around the subject according to how far you push it. The range is 0 to 2000, with 0 being the default. Given how large that top blur radius is, together with the control the In/Out Ratio gives you over the spread's direction, you can rescue some fairly dicey mattes into surprisingly clean, usable ones. TIP: When haloing crops up, one fix is to tweak the In/Out Ratio parameter; alternatively, reach for the Qualifier Softness parameters to soften the key's edges.

Reaching for the Blur parameters to ease a key's edges In/Out Ratio Sets whether the "Blur Radius" lands evenly on the inside and outside of the matte edge (zero), inside the matte only (negative values), or outside the matte only (positive values). Reaching for In/Out Ratio can help knock out fringing when you use the Blur Radius parameter.

(Left) In/Out Ratio dropped, so the blur stops at the matte edge and tapers inward; (Right) In/Out Ratio raised, so the blur begins at the matte edge and tapers outward

You can also put In/Out Ratio to work even when no Blur Radius is in play at all. Pushing In/Out Ratio up packs small black holes in the matte shut, while dropping In/Out Ratio under 0 clears speckling by driving tiny white matte bits toward black. (Left) In/Out Ratio controls turned down to widen matte holes; (Right) In/Out Ratio controls turned up to pack the matte's small black holes shut Morph Operation Lets you pick how to reshape the alpha channel/key. Pick Shrink or Grow to erode or dilate the matte edges very precisely. Or pick Opening or Closing to seal or open holes to tidy a rough matte. (Left) A matte showing small face holes; (Right) with Mode at Shrink and Morph Radius at 3, applied to seal a matte's holes Morph Radius Working together with Morph Operation, this slider tunes how far to shrink, grow, open, or close the edge's key.

### Denoise

Denoise offers a separate route for cleaning extracted keys after the fact, cutting back key noise selectively, clearing out stray pockets of qualification, and gently packing matte holes.

Before/after raising Denoise, viewing the high contrast matte

### Shadow

Tunes the key's strength according to the darker regions of the source picture.

### Midtone

Tunes the key's strength according to the midtones of the source picture.

### Highlight

Tunes the key's strength according to the brighter regions of the source picture.

### Post-Filter

Runs one last pass over the key, drawing on the source picture, to help restore fine detail along crisp edges or in hair.

### The Many Ways to Invert a Key

There are times you'll want to isolate a subject or value range in a frame and then alter everything else. One approach is placing an Outside node downstream of the node where you built the key. That setup lets you grade one way on what you keyed and another way on whatever lies outside the key. For a quick change, you can simply flip the key inside the Qualifier palette. There are, however, three more routes to inverting a key. The Qualifier Invert button: Clicking it just flips the key that all the Qualifier palette's controls produce. Key Palette Qualifier Invert: The Qualifier Invert control over in the Key palette gives you a second way to flip the key the Qualifier palette generates. Key Palette Output Invert: What makes the Output Invert control in the Key palette stand out is that it flips the total of every key applied inside that node. Say you pair a Qualifier with a Window — the two invert controls just described flip only the Qualifier key and leave the Window key untouched. The Output Invert control, by contrast, flips the combined sum of the Qualifier key and the Window all at once.

### Combining Qualifiers and Windows

A later section digs into this further, but when you build a key with one of the Qualifier modes and then add a Window, the node's final key output is held to where the Qualifier key and the Window overlap. That makes it simple to "garbage matte" away unwanted bits of a key with a Window when further Qualifier control adjustments can't remove them.

Her skin tone sits too near the other elements present in the shot.

A Circular Power Window serves to narrow the isolation down to her alone.

### Manipulating Keys Using Additional Nodes

When a qualified key needs more work than the Matte Finesse controls permit, the Node Editor lets you route one node's key output into another node's RGB input; from there every color tool on the second node is yours to massage the grayscale image that forms that key and refine it.

Wiring a key output into an RGB input, then routing the RGB output back into the following node's KEY input The Key Mixer node is another option for blending several keys in various ways — summing keys, or taking one away from another — so you can build precisely the key you're after.

### Adding multiple keys together using a Key Mixer

To dig deeper into these methods, refer to Chapter 146, “Combining Keys and Using Mattes.”
