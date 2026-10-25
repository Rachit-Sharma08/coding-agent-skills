# Duplicate angle adjustment with centered pivot

Version: DaVinci Resolve 20.3 Reference Manual. Context: Duplicate.
[Chapter index](INDEX.md) / [Previous section](duplicate-controls.md) / [Next section](highlight-and-hot-spot.md) / [Duplicate Dup](duplicate-controls.md)
<a id="source-angle-adjustment-with-centered-pivot"></a> <a id="source-angle-adjustment-with-offset-pivot"></a> <a id="source-common-controls"></a> <a id="source-jitter-tab"></a>

### Angle adjustment with centered pivot

### Angle adjustment with offset pivot

Apply Mode The Apply Mode choice sets the arithmetic used to blend or merge overlapping cloned objects.

- Normal: This default treats the foreground object’s Alpha channel as a mask that says which pixels stay transparent and which do not. With it active, a second menu surfaces the available operations: Over, In, Held Out, Atop, and XOr.
- Screen: Screen merges objects by multiplying their color values together. Here the Alpha channel plays no part and stacking order stops mattering. The output color always trends brighter. A black screen value leaves the color as-is, while a white screen value yields pure white. The look resembles several film frames projected together onto one surface. With it active, a second menu surfaces the available operations: Over, In, Held Out, Atop, and XOr.
- Dissolve: Dissolve blends overlapping objects together, deriving the blend from a computed average of those objects.
- Multiply: This multiplies the values within a color channel. The object appears to darken as the values run from 0 to 1. Since White equals 1, the outcome stays unchanged; since Gray equals 0.5, the outcome becomes a darker object, that is, one half as bright.
- Overlay: Depending on the values of the object underneath, Overlay either multiplies or screens the foreground object’s color values. Colors and patterns lay over the present pixels yet keep intact the highlights and shadows belonging to the underlying objects. Rather than being swapped out, the lower objects blend with the front ones so the original brightness or darkness shows through.
- Soft Light: Based on the color values of the objects underneath, Soft Light either dims or brightens the foreground object. The result is much like aiming a diffused spotlight at the picture.
- Hard Light: Based on the color values of the objects underneath, Hard Light either multiplies or screens the foreground object’s color values. The result is much like aiming a harsh spotlight at the picture.
- Color Dodge: Drawing on the foreground object’s color values, Color Dodge lightens the objects beneath it. It parallels the darkroom technique of dodging, which cuts an area’s exposure on a print.
- Color Burn: Drawing on the foreground object’s color values, Color Burn darkens the objects beneath it. It parallels the darkroom technique of burning, which raises an area’s exposure on a print.
- Darken: Per channel, Darken inspects the color data and picks whichever of the foreground or background color value is darker as the outcome. Pixels brighter than the blended colors get swapped out, while pixels darker than the blend stay put.
- Lighten: Per channel, Lighten inspects the color data and picks whichever of the foreground or background color values is lighter as the outcome value. Pixels darker than the blend get swapped out, while pixels brighter than the blend stay put.
- Difference: Per channel, Difference inspects the color data and, according to which side carries the greater brightness, subtracts the foreground object’s color values from the background’s, or vice versa. A white blend inverts the color; a black blend leaves it alone.
- Exclusion: Exclusion yields a result akin to the Difference mode but with reduced contrast. A white blend inverts the base color values; a black blend leaves them alone.
- Hue: Hue forms a result color that takes its luminance and saturation from the background objects’ color values and its hue from the foreground object’s color values.
- Saturation: Saturation forms a result color from the luminance and hue of the base color combined with the saturation of the blend color.
- Color: Color forms a result color carrying the luminance of the background object’s color value plus the hue and saturation of the foreground objects. Because it holds the image’s gray levels intact, it works well for tinting monochrome objects.
- Luminosity: Luminosity builds a color from the background object’s hue and saturation together with the foreground object’s luminance. The result is the reverse of what the Color mode produces.

Operator Through this menu you pick the Operation mode applied where duplicate objects overlap. Switching the Operation mode alters how those overlapping objects merge. The drop-down shows up only while the Apply mode sits at Normal. Within the Duplicate node, pixels are always combined by the formula (fg object _ x) + (bg object _ y). Each operation defines what x and y stand for, per the explanation given for every mode. Here are the Operator Modes:

- Over: Wherever the foreground object’s Alpha channel exceeds 1, the Over mode stacks the foreground onto the background by swapping the background pixels for the pixels coming from the Z.

x = 1, y = 1 - [foreground object Alpha]

- In: The In mode takes the background object’s Alpha channel and multiplies it against the foreground object’s pixels. It disregards the foreground object’s color channels. The output retains only

foreground object pixels. In effect this trims the foreground object by the background object’s mask. x = [background Alpha], y = 0

- Held Out: Held Out behaves as the inverse of the In operation. Here the foreground object’s pixels get multiplied by the background object’s inverted Alpha channel.

x = 1 - [background Alpha], y = 0

- Atop: Atop lays the foreground object on top of the background object solely where the background object carries a matte.

x = [background Alpha], y = 1 - [foreground Alpha]

- XOr: XOr joins the foreground and background objects anywhere one or the other holds a matte, yet never where the two overlap with a matte.

x = 1 - [background Alpha], y = 1-[foreground Alpha] Subtractive/Additive Use this slider to choose whether Fusion runs an Additive composite, a Subtractive composite, or some mixture of the two where the duplicate objects overlap. By default it sits at Additive, on the assumption that the incoming image’s Alpha channel is premultiplied, which it generally is. Here is a brief primer if the distinction between Additive and Subtractive compositing is unclear. You need an Additive blend when the foreground image is premultiplied, meaning each color-channel pixel has already been multiplied by the matching Alpha-channel pixel. Consequently transparent pixels end up black, because anything times 0 stays 0. The operation hides the background by multiplying it with the inverted foreground Alpha and then adds the foreground pixels on top. A Subtractive blend is what you want when the foreground image lacks premultiplication. The technique resembles an additive composite, except the foreground image is first multiplied by its own Alpha to wipe out any background pixels lying beyond the Alpha region. Whereas most other software treats Additive/Subtractive as a strict either/or toggle, the Duplicate node permits a blend between the Additive and Subtractive flavors of the compositing math. That comes in handy for troublesome composites showing bright or dark fringes. As an illustration, Subtractive merging on a premultiplied image can darken edges, while Additive merging on a non-premultiplied image adds any non-black region beyond the foreground’s Alpha into the result and so lightens the edges. Sliding between Additive and Subtractive lets you dial the edge brightness exactly right for the shot. Gain The Gain RGB fields scale the image channel values in a linear fashion. Each pixel gets multiplied by one shared factor, though bright pixels shift more than dark ones. Black pixels stay fixed, since anything multiplied by 0 stays 0. Alpha Gain scales the Alpha-channel values of the front objects linearly. Doing so cuts how much the background objects get hidden and thereby brightens the whole result. With the Subtractive/Additive slider at Additive and Alpha Gain at 0.0, the foreground pixels merely add onto the background. With the Subtractive/Additive slider at Subtractive, it instead governs the composite’s density, much as Blend does. Every Gain value compounds with each successive duplication.

Blur Introduces a blur onto the cloned layers.

- Lock Blur: Ties the X and Y Blur sliders together so blurring stays symmetrical. It comes on by default. Deselecting the Lock Blur control hands you separate command of each axis.
- Blur: Determines how much blur the tool puts on the cloned layers. This Blur amount does not compound with the count of duplications.
- Glow: Puts a glow onto the blur of the cloned layers.
- Blend: The Blend slider sets what percentage of the processed image gets mixed back with the

original image. The closer the value sits to 0, the more of the original image it folds in.

- RGBA Scale: Lets you tune the strength of the separate Red, Green, Blue, and Alpha channels

feeding the blur of the cloned layers. Burn In The Burn In field sets how much Alpha is used to darken objects sitting behind others, while leaving the quantity of added foreground objects alone. At 0.0 the blend acts as a plain Alpha blend, whereas at 1.0 the front objects are essentially added onto the rear objects (following Alpha multiplication when in Subtractive mode). The upshot is that foreground objects appear to brighten the ones behind, just as Alpha Gain does. Indeed, with Additive blends, raising the Burn In matches the outcome of lowering Alpha Gain. Blend This blend control differs from the Blend slider found on the Common Settings tab. Adjusting it applies the blend across objects. The Blend slider dissolves the last object’s result first, the second-to-last next, and onward. The blend spans from 0 to 1, where 1 keeps every object fully opaque and 0 leaves only the source object visible. Merge Under Ticking this checkbox flips the stacking order of the cloned elements, so the final copy becomes the lowest layer and the first copy becomes the topmost.

### Jitter Tab

Controls on the Jitter tab let you randomize position, rotation, size, and color across all the copies that the Controls tab produced.

r Duplicate Jitter tab

Random Seed Together, the Random Seed slider and the Reseed button create a random origin point for how much jitter is applied to the cloned objects. Pair two Duplicate nodes with matching settings but different random seeds and you get two entirely separate outcomes. Center X and Y These two fields tune how much the X and Y position of the cloned objects varies. Axis X and Y These two fields tune how much the rotational pivot center of the cloned objects varies. They touch only the extra jitter rotation, leaving the rotation from the Controls tab’s Rotation settings untouched. X Size This field tunes how much the Scale of the cloned objects varies. Angle This dial tunes how much the Z rotation of the cloned objects varies. Gain The Gain RGBA fields randomly scale the image channel values in a linear way. Blend Adjusting this control randomizes the blend across objects.

### Common Controls

Settings Tab Because the Settings tab controls apply across every Effect node, you will find them documented under the “The Common Controls” heading that closes this chapter.
