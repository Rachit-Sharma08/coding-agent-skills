# Primatte replace tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Primatte.
[Chapter index](INDEX.md) / [Previous section](primatte-fine-tuning-tab-selected-color.md) / [Next section](primatte-and-relight.md) / [Primatte Pri](matte-control-and-primatte.md)
<a id="source-clean-background-noise"></a> <a id="source-clean-foreground-noise"></a> <a id="source-common-controls"></a> <a id="source-degrain-tab"></a> <a id="source-how-to-key-with-primatte"></a> <a id="source-matte-tab"></a> <a id="source-primatte-viewer-buttons"></a> <a id="source-primatte-viewer-options-menu"></a> <a id="source-replace-mode"></a> <a id="source-replace-tab"></a> <a id="source-the-primatte-degrain-tab"></a> <a id="source-the-primatte-matte-tab"></a> <a id="source-the-primatte-replace-tab"></a>

### The Primatte Replace tab

### Replace Tab

From the Replace tab you can pick among the three color spill replacement methods detailed earlier in the Spill Sponge section. Three choices govern the replacement color as spill is removed, and you set them through the Replace mode menu.

### Replace Mode

- Complement: Swaps the spill color out for the complement of the screen color. This mode preserves delicate foreground detail and yields the finest results. Where foreground spill isn’t much of an issue, this is the mode to reach for. When the spill on the foreground image runs fairly heavy, though, this mode will frequently push noticeable noise into the finished composite.
- Image: Swaps the spill color for hues drawn from a defocused version of the background image, or from the Replace image when one is wired into the node’s Replace input (magenta ). This mode lands a pleasing color tone on the foreground subject even against a high-contrast background. The downside is that Image mode now and then forfeits the fine edge detail of the foreground subjects. Trouble can also arise if you afterward resize the foreground image relative to the background: because the background/foreground alignment shifts, the color tone borrowed from the defocused image may no longer line up.
- Color: Swaps the spill color for a single solid color. Pick this option and a color swatch alongside R,G,B sliders appears for choosing that color. By adjusting the palette color of the solid replacement, you can land on a good spill replacement that harmonizes with the composite background. Its merit is that it copes well even under severe spill. The drawback is that, in Solid Color Replacement mode, fine detail along the foreground edge is apt to vanish. A lone palette color sometimes can’t produce a pleasing tone when the background image contains some high‑contrast color areas.

### The Primatte Degrain tab

### Degrain Tab

Turn to the Degrain tab when a foreground image is badly marred by film grain. Because of that grain, once backing screen noise has been wiped out entirely, the foreground object’s edges often turn harsh and jagged, producing a poor key. Grain Size The Grain Size selector offers a span of grain removal running from Small to Large. When the foreground image carries a heavy load of film grain-induced pixel noise, you risk losing a clean edge on the foreground object while attempting, via the Clean Background Noise Operation Mode, to scrub every bit of grain noise away. These tools tidy up the grain noise while leaving the key’s quality intact.

- None: Degraining doesn’t happen at all.
- Small: The averaged color taken from a small patch surrounding the sampled pixel. Reach for this

when the grain is very dense.

- Medium: The averaged color taken from a medium-sized patch surrounding the sampled pixel. Reach

for this when the grain is less dense.

- Large: The averaged color taken from a wider patch surrounding the sampled pixel. Reach for this

when the grain is very loose. Grain Tolerance Moving this slider boosts how strongly the Clean Background Noise tool works while leaving the foreground object’s edge untouched.

### The Primatte Matte tab

### Matte Tab

The Matte tab polishes the key’s alpha, folding in whatever solid and garbage masks are wired to the node. While you work the Matte tab, set the viewer to show the alpha channel of Primatte’s final output. Filter This control picks the filtering algorithm that gets applied when blur is added to the matte.

- Box: The quickest option, though at lower quality. Box fits best where only a little blur is needed.
- Bartlett: Also called a Pyramid filter, Bartlett strikes a sound balance between speed and quality.
- Multi-Box: Choose this filter and the Num Passes slider shows up so you can dial in the quality. At 1 and 2 passes the output matches Box and Bartlett respectively. From 4 passes upward, output tends to rival Gaussian, in less time and free of edge “ringing.”
- Gaussian: The Gaussian filter applies a genuine Gaussian approximation and produces excellent output, though it runs a touch slower than the rest. On occasion it can leave an extremely faint edge “ringing” on floating-point pixels.

Blur Matte Blur softens the matte’s edge according to whatever the Filter menu is set to. Set it to zero and you get a crisp, cutout-style hard edge; raise the value and more blur spreads across the matte. Blur Inward Switch on the Blur Inward checkbox and the blur is cast toward the foreground subject’s center. Ordinary blurring or defocus works on the matte edges in both directions (inward and outward) and at times leaves a halo artifact ringing the edge in the composite view. Blur Inward, by contrast, acts solely toward the inside of the foreground subject (in toward the center of the white area). The end result clears small dark noise from the screen area without it being grabbed again in the Clean Background Noise mode. Now and then it yields softer, cleaner edges on the foreground objects.

Contract/Expand This slider tightens or enlarges the semitransparent zones of the matte. Push it above 0.0 to expand the matte; drop it below 0.0 to contract it. You’ll typically pair this control with the Matte Blur to soften a matte’s hard edge and cut down fringing. Because it acts only on semitransparent zones, it leaves a matte’s hard edge alone. Gamma Matte Gamma pushes the matte’s values up or down within the semitransparent zones. Higher settings make the gray areas more opaque; lower settings make those gray areas more transparent. Fully black or fully white parts of the matte stay put. Acting only on semitransparent zones, it has no bearing on a matte’s hard edge. Threshold This range slider fixes the lower threshold with the left-hand handle and the upper threshold with the right-hand one. Anything under the lower threshold turns black or transparent in the matte, and anything over the upper threshold turns white or opaque. Everything in between keeps its relative transparency. The control sees frequent use for rejecting salt and pepper noise in the matte. Restore Fringe This brings back the matte’s edge around the keyed subject. Keying often clips out the subject’s edge wherever there’s hair; Restore Fringe returns that edge while keeping the matte solid. Invert Matte Tick this checkbox and the alpha channel the keyer made is flipped, so every transparent area turns opaque and every opaque area turns transparent. Solid Matte Solid mattes are mask nodes or images wired into the node’s solid matte input. A solid matte is laid straight onto the image’s alpha channel. As a rule, solid mattes hold out keying in regions meant to stay opaque — think of someone with blue eyes shot against a blue screen. Switching on Invert flips the solid matte ahead of its merge with the source alpha. Garbage Matte A garbage matte is itself a mask node or image wired into the node’s garbage matte input. A garbage matte too is laid straight onto the image’s alpha channel. As a rule, garbage mattes strip out unwanted things that can’t be keyed, such as microphones and booms. They also patch in regions that hold the keyed color yet need to be preserved. You can’t blend garbage mattes of differing modes inside one tool. A Matte Control node is frequently placed after a Keyer node to introduce a garbage matte that does the reverse of the matte fed to the keyer. Switching on Invert flips the garbage matte before it merges with the source alpha. Post-Multiply Image Pick this option and the keyer multiplies the image’s color channels against the alpha channel it builds for that image. It’s normally switched on and enabled by default.

Clear this checkbox and the image stops counting as premultiplied when you go to merge it with others. In that case reach for the Subtractive option of the Merge node rather than the Additive one. To read more about these Merge node settings, consult Chapter 95 ("Composite Nodes") of the DaVinci Resolve Reference Manual, or else Chapter 35 within the Fusion Reference Manual.

### Common Controls

Settings Tab The Inspector’s Settings tab is mirrored across the other Matte nodes as well. You’ll find these shared controls spelled out in full at this chapter’s close, under the “The Common Controls” section.

### How to Key with Primatte

To start keying with Primatte, wire the blue- or green-screen shot into the orange foreground input of the Primatte node and route the composite’s background shot into the green background input. With the connections set, working the Primatte breaks down into four core steps, in order: 1 Select Background Color, then 2 Clean the Background Noise, then 3 Clean the Foreground Noise, and finally 4 Remove Spill. Selecting Background Color 1 Within the Inspector, press the Select Background Color button. 2 Hover the mouse pointer over the blue/green-screen region in the viewer, somewhere close to the foreground subject. 3 Drag across the background color. Primatte averages the pixels down to one color. There are times when Primatte performs best on a single sampled pixel rather than a span of them. If your keying is giving you trouble, run Select Background Color again on one dark screen pixel or one light screen pixel. Alternatively, to make a rectangular selection, use the Box button up in the viewer’s top left-hand corner. The Median button behaves like Line selection, save that every sampled point comes from a 3 x 3 region centered on your click that then has a median filter applied. This can help trim down any noisy pixels.

### Primatte viewer buttons

When the foreground image holds a shadow you’d like preserved in the composite, steer clear of selecting any of the dark screen pixels inside that shadow. Doing so keeps the shadow bundled with the rest of the foreground image.

### Clean Background Noise

Any white or light gray patches sitting in the dark screen area get the name “noise.” In practice it’s assorted shades of the screen color that the first sample missed and that ought to come out. Background noise is cleared by way of the Clean Background Noise button. 1 Within the Inspector’s View Mode menu, pick Black. 2 Over the viewer, press the Alpha Channel/RGB button. The displayed picture switches to a black-and-white “matte” rendition. 3 Press the Clean Background Noise button. 4 Drag the mouse pointer across the white or light gray patches that should read as pure black. Primatte works through the selection and strips the noise away. 5 Run this procedure as many times as it takes to rid the background areas of noise. Choosing Gain/Gamma from the viewer’s Options menu to lift brightness or gamma reveals noise that would otherwise stay hidden.

### Primatte viewer Options menu

Good results don’t hinge on clearing out every last white pixel. In a key image, most pixels shown as a dark near-black color count as transparent and effectively let the background stand as the final output there. So there’s no call to wipe out all the noise across the screen portions of the image. Indeed, trying to scrub noise away too meticulously around the foreground subject often makes a smooth composite hard to achieve. TIP: While clearing noise from around loose, flying hair or any background/foreground transitional zone, take care not to grab any of the areas hugging the hair’s edge. Leave a touch of noise around the hair, since the Fine Tuning tools can deal with it later.

### Clean Foreground Noise

Dark patches sitting amid the largely white foreground subject mean the key isn’t 100% in those spots. Clean Foreground Noise can drive the matte as white as it will go. 1 Leave the View Mode menu on Black and the viewer on the Alpha Channel. 2 Press the Clean Foreground Noise button. 3 Drag the mouse pointer across the dark foreground pixels that ought to be pure white. Primatte works through the selection and strips the noise away. 4 Run this procedure as often as it takes to clear noise from the foreground areas. 5 If it’s on, switch off Gain/Gamma in the viewer’s Options menu to get back to a normal viewer.
