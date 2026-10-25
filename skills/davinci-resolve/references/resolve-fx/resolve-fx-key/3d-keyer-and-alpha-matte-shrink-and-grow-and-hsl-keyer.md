# 3D keyer and alpha matte shrink and grow and hsl keyer

Version: DaVinci Resolve 20.3 Reference Manual. Context: 3D keyer, Alpha matte shrink and grow studio version only, Hsl keyer.
[Chapter index](INDEX.md) / [Previous section](3d-keyer-behavior-options.md) / [Next section](hsl-keyer-keyer-options.md) / [Continue HSL Keyer](hsl-keyer-keyer-options.md) / [3D Keyer](3d-keyer-behavior-options.md)
<a id="source-alpha-matte-shrink-and-grow-studio-version-only"></a> <a id="source-garbage-matte"></a> <a id="source-hsl-keyer"></a> <a id="source-hsl-keyer-color-range-controls"></a> <a id="source-matte-finesse"></a> <a id="source-output"></a> <a id="source-selection-range-controls-1"></a>

### Matte Finesse

It may turn out that sampling the screen color alone won’t clear up certain problems. Trouble such as chattery edges, holes, or noise can at times be remedied through the Matte Finesse controls. These controls filter what the Keyer puts out and amount to adjustments made on the matte itself, reshaping the key by drawing on the frame’s content.

- Pre Filter: This slider gives the image a cleanup pass prior to any color sampling. The adjustment proves handy where your footage carries MPEG blocking artifacts.
- Clean Black: Clean Black names a focused operation that wipes out noise appearing as white speckling within a key’s black area. Pushing Clean Black up lets you “fill holes” throughout a key’s background portion and chew away translucent edges.
- Clean White: Clean White names yet another focused operation that wipes out noise (appearing as black speckling while you view a high-contrast highlight) within the white portion of a key that covers areas of the image you’re isolating, and it stretches the key by brightening a key’s light parts the further you push this parameter up, easing a key’s light gray areas toward white. The upshot is that pushing Clean White up lets you “fill holes” throughout a key’s foreground portion and stretch translucent edges.
- Black Clip: Pushing Black Clip up lays on a “lift” adjustment such that the matte’s translucent areas (its gray areas while viewing a high-contrast highlight) ease toward black. Values run 0 to 100, where 0 serves as the default setting.
- White Clip: Easing White Clip down lays on a “gain” adjustment such that the matte’s translucent areas (its gray areas while viewing a high-contrast highlight) ease toward white. Values run 0 to 100, where 100 serves as the default setting.
- Blur Radius: In modest doses, blurring a key does a good job of taking the bite off troublesome edges. That said, blurring a key may also feather a key’s edges out past the border of whatever subject you’re keying, the upshot being a visible “halo” ringing your subject, hinging on the adjustment you make. Values run 0 to 2000, where 0 serves as the default. With a maximum blur radius this generous, joined by what the In/Out Ratio brings for tailoring the direction of spread, you can convert some quite precarious mattes into surprisingly smooth, useful results.
- In/Out Ratio: Putting In/Out Ratio to work can help do away with fringing. Pushing In/Out Ratio up will pack small black holes within the matte, whereas easing In/Out Ratio under 0 will do away with speckling by easing small white bits of the matte toward black.
- Morph Operation: Settle on Shrink or Grow to dilate or erode the matte’s edges, or settle on Opening or Closing to plug or open up holes so a ragged matte gets cleaned up.
- Morph Radius: Sets how far to shrink, grow, open, or close the key.
- Denoise: Affords a separate means of post-processing pulled keys to selectively trim a key’s noise, doing away with stray patches of qualification and softly packing holes within a matte.
- Shadow: Tunes key strength off the darker portions of the original image.
- Midtone: Tunes key strength off the midtones of the original image.
- Highlight: Tunes key strength off the brighter portions of the original image.
- Post Filter: Carries out a closing cleanup on the key, putting the original image to use as reference; handy for coaxing back some fine detail across sharp edges or hair.

### Garbage Matte

Through these controls you can crop away other unwanted items present in the frame, such as lighting fixtures, boom microphones, tracking patches, and so forth.

- Matte Shape: Settle on either a Rectangle or Ellipse to crop around whatever subject you’re keying. Settling on None switches Garbage Matte off. With a garbage matte switched on, the Viewer’s Open FX Overlay mode surfaces an on-screen control for tuning the garbage matte’s shape and placement.
- Edge Softness: Lets you soften the edges. It defaults to 50; values run 0 (no softening) to 100 (maximum softening).
- Invert: Flips the garbage matte.
- Center X and Y: Lets you tune and keyframe where a garbage matte sits.
- Bounding Width and Height: Lets you tune the garbage matte’s width and height.
- Rotation: Lets you tune the garbage matte’s angle.

### Output

Through the Output controls you settle on how the image gets output, composited, and shown within the Viewer.

- Output: This menu lays out three options for which channels come out of the effect. Alpha Highlight: Renders an Alpha channel’s transparent part as gray with an alpha channel’s solid part in full color.

Alpha Highlight B/W: Renders the black and white Alpha channel, frequently of use while sampling further areas to key. Final Composite: The keyed image gets rendered composited over whatever video track lies below it.

- Use Alpha: A widespread control found in many Resolve FX and 3rd party Open FX plugins; this checkbox decides whether the Alpha channel applies while compositing over another video track. It can stand in for picking RGB Only (Blank Alpha) off the Output menu.

To put the 3D Keyer to work on the Edit page: 1. Lay the 3D Keyer onto a green screen or blue screen clip sitting on a track above the background. 2. Within the Inspector, tick the Show Paths checkbox so the sampled areas come into view once you begin. 3. Off the Viewer Overlay menu at the lower-left of the Timeline Viewer, pick Open FX Overlays. 4. Within the Viewer, click and drag to draw a sampling stroke over the screen color you wish to strip out. 5. Transparency kicks in right away, showing the keyed subject against whatever clip sits on the video track below it in the Timeline as a composite. To view the matte you built for further tuning, pick Alpha Highlight or Alpha Highlight B/W off the Output drop-down menu. 6. As needed, you can add areas to or trim areas from the screen color selection through the add/ subtract Color range controls. Alternatively, with the default Sample eyedropper active, you can hold Shift to add onto the screen color selection or hold the Option key to pull from the screen color selection.

### Alpha Matte Shrink and Grow (Studio Version Only)

This filter gives you assorted ways to refine the edges of alpha and key mattes, both shrinking and growing those edges and opening or closing holes that surface within a matte. On the Color page, you can apply this filter to Qualifier or Window keys that have been routed into the RGB input of a corrector node, for tuning and refinement, before the result gets wired into a downstream node’s key input to isolate an adjustment.

Putting the Alpha Matte Shrink and Grow filter onto a key matte fed into the RGB input of a separate node

- Morph Operation: Through a drop-down menu you settle on how to reshape the Alpha channel/key. Settle on Shrink or Grow to dilate or erode the matte’s edges with great precision. Or settle on Opening or Closing to plug or open up holes inside the key so a ragged matte gets cleaned up.
- Shape: Through a drop-down menu you settle on how corners and angles along the key’s edges get treated as you grow or shrink it. Circle stands as the default and yields even expansion about the key’s surface that, at extreme Radius settings, eventually averages every angle into a circular form. Square averages every angle into a more rectangular form at extreme Radius settings. Diamond averages every angle into a diamond form at extreme Radius settings.
- Radius: A slider sets how far to Shrink, Grow, Open, or Close the key.
- Process: Lets you pick particular channels for the Morph Operation to act on. The options are RGB

(Blank Alpha), Alpha (RGB Unaffected), and RGB + Alpha. Preview Alpha: Ticking this box lets you quickly preview the Alpha channel the node will put out.

- Manual Iteration Control: Ticking this box hands you direct say over how the operators get applied.

Operator Radius: A slider governing the operator’s size. Repeat Operation: A slider reshapes what the Operator Radius setting does so you can push more extreme adjustments.

### HSL Keyer

Built on the Color page’s HSL Qualifier, the HSL Keyer Resolve FX is an all-purpose keyer drawing on a trio of color components, hue, saturation, and luma, in order to set up a key. On top of that, the HSL Keyer lets you switch off whichever color components you’d sooner keep from feeding the resulting key. A saturation-only key, or a hue-only key, is within reach for cases where leaning on individual components alone yields a finer result. The simplest route to working any keyer is sampling the picture in the Viewer with the settings untouched. Once you sample one or more pixels, the hue, saturation, and luma values get analyzed and assigned differing ranges. A number of eyedropper controls are on hand to sample color and soften the selection.

### Selection Range Controls

The Inspector’s Selection Range buttons let you set up a key by sampling and softening Viewer pixels with the mouse pointer.

### HSL Keyer Color Range controls

- Sample Eyedropper: This tool picks the colors that serve as the qualification range by way of clicking and dragging over the Viewer image. Click it once more to wipe the prior selection. As a rule, long drags yield finer results than short ones.
- Add/Subtract Color Range: This pair of controls lets you fold image areas into, or pull them out of, the presently chosen inner band of values forming the key’s core. As with the other sampling controls, dragging over a band of color works.
- Add/Subtract Softness: This pair of controls lets you reshape the softness that eases out of the key’s inner band, tapering toward the key’s outer edge. As with the other sampling controls, dragging over a band of color works.
- Invert: Flips the sampled color so it turns opaque, while regions left unsampled turn transparent.
- Reset: Clears every sampled color yet holds onto the general control settings.
