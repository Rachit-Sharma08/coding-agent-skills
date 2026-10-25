# Lighten and lighter color

Version: DaVinci Resolve 20.3 Reference Manual. Context: Compositing and transforms in the timeline.
[Chapter index](INDEX.md) / [Previous section](timeline-composite-modes-and-opacity.md) / [Next section](opacity-and-video-fader-handles.md)
<a id="source-foreground"></a> <a id="source-inverted-alpha"></a> <a id="source-inverted-lum"></a> <a id="source-lighten"></a> <a id="source-lighter-color"></a> <a id="source-linear-burn"></a> <a id="source-linear-dodge"></a> <a id="source-linear-light"></a> <a id="source-lum"></a> <a id="source-luminosity"></a> <a id="source-multiply"></a> <a id="source-overlay"></a> <a id="source-pin-light"></a> <a id="source-saturation"></a> <a id="source-screen"></a> <a id="source-softlight"></a> <a id="source-subtract"></a> <a id="source-unknown"></a> <a id="source-vivid-light"></a>

### Lighten

Each pairing of pixels in every color channel is compared, and the lighter of the two becomes the output. Layer order doesn't matter. Lighten serves you well when you want the lightest features of both layers to win out, though for any particular pixel the output might come out as a color found in neither source layer at that pixel.

### Lighter Color

For each pairing of pixels, all three color channels from the bottom layer are summed, and all three color channels from the top layer are summed. Those results are compared, and the lighter pixel of the two layers becomes the output. Layer order doesn't matter. Lighten Color serves you well when you want the lighter features of both layers to win out. Unlike the Lighten composite mode, the result is always a specific color drawn from either the bottom or top layer.

### Linear Burn

Each pairing of pixels is summed, then 1 is subtracted from the total. Layer order doesn't matter. White regions in one layer let the other layer through; meanwhile, the colors and darker tones drawn from both layers play off one another to tint or darken the result.

### Linear Dodge

Each pairing of pixels is summed. This composite mode is identical to Add.

### Linear Light

Every region where the bottom layer sits above 50% is Linear Dodged so as to lighten those parts of the final result, while every region where the bottom layer falls below 50% is Linear Burned so as to darken those parts of the final result. This composite mode heightens image contrast in the final result.

### Luminosity

Rebuilds two layers from HSL image components: the bottom layer's Hue and Saturation are joined to the top layer's Luma.

### Multiply

Each pairing of pixels is multiplied. Layer order doesn't matter. Generally this has the effect of stressing the darkest parts of both images in the resulting output; black areas of either image in particular are retained (0 _ n = 0), while white areas of either image leave the output image unchanged (1 _ n = n). Multiply is good for compositing darker elements set in a field of white into an image, and when you blend in a noise, grain, or damage layer it can emphasize that layer's darkest regions.

### Overlay

Overlay marries useful aspects of both the Screen and Multiply composite modes, keyed to the pixel values of the bottom-most image on the Timeline; every bottom layer pixel above 50% is Screened, while every bottom layer pixel at 50% and below is Multiplied. Overlay is an excellent composite mode for marrying a layer of noise, grain, or damage imagery with another clip, since it combines both images in visually useful ways across the tonal range from shadows through highlights.

### Pin Light

Wherever bottom layer pixels sit under 50% gray, the bottom layer's darker pixels take over the top layer's lighter ones, while in the top layer darker pixels stand in for the bottom layer's lighter pixels, so the final image's darker half draws darker pixels out of both layers. Wherever bottom layer pixels go over 50% gray, the bottom layer's lighter pixels take over the top layer's darker ones, while in the top layer lighter pixels stand in for the bottom layer's darker pixels, so the final image's brighter half draws lighter pixels out of both layers.

### Saturation

Rebuilds two layers from HSL image components: the bottom layer's Luma and Hue are joined to the top layer's Saturation.

### Screen

Each layer's pixel values are first inverted, multiplied together, and then that product is inverted once more. Layer order doesn't matter. Screen is Multiply's inverse, since it keeps the lightest parts of both images, and it's useful when compositing lighter elements set in a field of black into an image; blend in a noise, grain, or damage layer and it can emphasize that layer's lightest regions.

### Softlight

A gentler way of applying the Hardlight composite mode that lands on a more even blend between the two layers.

### Subtract

For every pixel pairing, the top layer's value has the bottom layer's value taken away from it. This can yield dark areas of the image that bottom out at flat black, but image data dropping below 0 is retained and can be recovered by later color correction operations.

### Vivid Light

Every region where the bottom layer sits above 50% is Color Dodged so as to lighten those parts of the final result, while every region where the bottom layer falls below 50% is Color Burned so as to darken those parts of the final result. For an extreme effect, this composite mode pushes the final result's image contrast and its saturation up dramatically.

### Foreground

When the Foreground composite mode is put on the top layer, the transparency of its pixels is governed by a bottom layer set to one of the composite modes below: Alpha The Alpha composite mode set on the bottom layer governs the transparency of the top layer in a Foreground mode. The layer's alpha is what's used.

### Inverted Alpha

Set the Inverted Alpha composite mode on the bottom layer and it governs how transparent the Foreground-mode top layer becomes. This time, though, it rests on the inverted alpha of the bottom layer.

### Lum

When the Lum mode is set on the bottom layer, it alters the transparency of the top layer in a Foreground mode. The pixels' luminosity value is what decides this.

### Inverted Lum

Set the Inverted Lum mode on the bottom layer and it alters how transparent the Foreground-mode top layer becomes. This rests on the inverted luminosity value of the pixels.

### Unknown

As you import XML or AAF project files carrying composite modes that DaVinci Resolve doesn't offer, the Composite Mode pop-up menu is set to Unknown; in practice, this matches Normal. TIP: For a fast preview of the various composite modes, rest your pointer on any mode within the Composite Mode drop-down list, and that mode previews right in the viewer.
