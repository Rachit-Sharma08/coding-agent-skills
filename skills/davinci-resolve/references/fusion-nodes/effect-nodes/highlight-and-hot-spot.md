# Highlight and hot spot

Version: DaVinci Resolve 20.3 Reference Manual. Context: Highlight, Hot spot.
[Chapter index](INDEX.md) / [Previous section](duplicate-angle-adjustment-with-centered-pivot.md) / [Next section](hot-spot-color-tab.md) / [Continue Hot Spot Hot / Color Tab](hot-spot-color-tab.md)
<a id="source-basic-node-setup-1"></a> <a id="source-basic-node-setup-2"></a> <a id="source-color-scale-tab"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab-1"></a> <a id="source-highlight-color-scale-controls"></a> <a id="source-highlight-controls"></a> <a id="source-highlight-hil"></a> <a id="source-highlight-node-introduction"></a> <a id="source-hot-spot-hot"></a> <a id="source-hot-spot-node-introduction"></a> <a id="source-inputs-1"></a> <a id="source-inputs-2"></a> <a id="source-inspector-1"></a> <a id="source-the-highlight-node"></a> <a id="source-the-hot-spot-node"></a>

### Highlight [HIL]

### The Highlight node

### Highlight Node Introduction

In bright areas of the picture, the Highlight filter produces star-shaped highlights or glints, akin to what a lens star filter does.

### Inputs

The Highlight node carries three Inputs: one for the image, one for the effects mask, and a third for a highlight mask.

Input: The orange input handles the principal 2D image onto which the highlight goes. Effect Mask: The blue input accepts a mask shape made from polylines, simple primitive shapes, paint strokes, or bitmaps from other tools. Wiring a mask here keeps the highlight confined to the masked pixels. Such a mask is processed after the tool runs. Highlight Mask: Through the white highlight mask input, the Highlight node permits pre-masking. The picture is filtered first, then the highlight goes on. After that the highlight merges back atop the source image. Differing from standard effect masks, it will not clip highlights off source pixels where the highlight reaches past the mask edges. In every other way highlight masks behave just like effects masks.

### Basic Node Setup

In the example below, the Highlight node produces glint-style highlights over an incoming picture, with the highlight mask keeping the effect within a chosen region.

### Inspector

A Highlight node placed on a picture, where a highlight mask confines the region of the effect

### Highlight controls

### Controls Tab

Every parameter for the highlight’s style lives on the Controls tab apart from color, which the Color Scale tab takes care of. Low and High This range control sets which span of Luminance values in the picture spawns highlights. Anything beneath the Low value gets no highlight. Anything past the High value gets the highlight at full strength.

Curve The Curve value adjusts the falloff across the highlight’s span. Raise it and the flare brightness fades nearer the highlight’s center; lower it and the fade happens farther out. Length This sets how long the flares reach from the highlight. Number of Points This fixes how many flares radiate out of the highlight. Angle This control spins the highlights. Merge Over Turn it on and the effect lays over the source image; turn it off and you get just the highlights as output. That is handy for color-correcting the highlights later down the chain.

### Highlight Color Scale controls

### Color Scale Tab

Color for the highlight is governed by the Color Scale tab. Click and hold the Pick button, then drag the pointer across the viewer, to grab a particular color out of the picture. Red, Green, and Blue Scale Lowering one or all of these channel sliders alters the highlight’s falloff color. Alpha Scale Lowering the Alpha slider renders the highlight falloff more see-through.

### Common Controls

Setting Tab Since the Settings tab controls are shared by all Effect nodes, look for their descriptions within the “The Common Controls” heading at this chapter’s close.

### Hot Spot [Hot]

### The Hot Spot node

### Hot Spot Node Introduction

With the Hot Spot node you build assorted lens flare, spotlight, and burn/dodge effects. Physically, lens flares arise when very bright light sources in a scene bounce off pieces of glass inside the camera’s lens. You will notice flares in a shot when a powerful light source, such as the sun or another brilliant star, is seen through a camera lens.

### Inputs

The Hot Spot node offers three inputs: one for the image, one for the effects mask, and one more for an Occlusion image. Input: The mandatory orange input handles the principal 2D image that receives the hot spot. Effect Mask: The blue input takes a mask shape drawn from polylines, simple primitive shapes, paint strokes, or bitmaps from other tools. Wiring a mask here keeps the hot spot inside the masked pixels. Such a mask is processed once the tool has run. Occlusion: The green Occlusion input takes an image that supplies the occlusion matte. That matte serves to block the hot spot so it appears to “wink.” White pixels in the image occlude the hot spot, while gray pixels partly suppress it.

### Basic Node Setup

Because the Hot Spot node cannot generate on its own, you must feed it an image input onto which the hot spot is placed.
