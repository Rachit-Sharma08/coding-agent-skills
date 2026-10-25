# Colorslice vector based grading tool and vectorspace colorslice controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Colorslice.
[Chapter index](INDEX.md)
<a id="source-colorslice"></a> <a id="source-colorslice-1"></a> <a id="source-global-colorslice-controls"></a> <a id="source-the-colorslice-global-controls"></a> <a id="source-the-colorslice-vector-based-grading-tool"></a> <a id="source-the-original-balanced-shot-we-want-to-enhance"></a> <a id="source-the-red-colorslice-vectorspace-slice-controls"></a> <a id="source-using-color-slice"></a> <a id="source-using-the-numeric-parameters"></a> <a id="source-vectorspace-colorslice-controls"></a>

### ColorSlice

This chapter walks through working with the ColorSlice tool, which lets you apply focused adjustments to particular color ranges so that they blend naturally back into the surrounding image.

ColorSlice is a fixed vector grading tool that lets you isolate one or several color ranges, each of which transitions smoothly into the others, producing a cleaner result than the HSL qualifier can.

### The ColorSlice vector-based grading tool

With ColorSlice you can dial in overall density, saturation, and hue to mimic various CMY print processes, and you can tune brightness and saturation per vectorspace slice. For rich, film-like color and looks, brightness is handled subtractively as you push saturation, which keeps saturated tones from looking unnaturally bright and removes the need for separate luminance tweaks.

Raising the Saturation (left) produces a brighter red, whereas applying the ColorSlice tool (right) yields a deeper red.

### Vectorspace ColorSlice Controls

The ColorSlice tool consists of seven separate vectorspace slices. Every vectorspace slice governs a band of colors keyed to the standard vectors on the Vectorscope: Red, Green, Blue, Cyan, Magenta, and Yellow. A seventh vector is also included to handle skin tones.

### The Red ColorSlice vectorspace slice controls

Every vectorspace slice carries this set of controls: Highlight: Pressing and holding this icon turns on a highlight view for as long as you keep the button held, revealing which parts of the image the control will affect. You can also lock in a permanent highlight for any vectorspace by first switching on a highlight view in the Viewer, which makes it simpler to dial in the parameters listed below. Slice Color: A label denoting the color of the region being controlled (Red, Green, Blue, and so on). Reset: Returns every one of the vectorspace slice controls to their default values. Color Wheel: A graphical depiction of the vectorspace slice. Everything inside the brightened wedge is what the controls will affect. Center: The single qualifying control you can adjust. Dragging this bright line one way or the other shifts the middle of the color range, slightly altering which colors carry the most weight in the qualifier. The center cannot be pushed beyond its range. Pair this with the highlight view so you can confirm the exact colors you intend to change are being qualified. Hue: Shifts the hue of every color inside the vectorspace slice. Changing it leaves the qualification of the original color untouched. Density: Modifies the density of the colors within the vectorspace slice by altering the luminance of the more saturated colors to imitate a subtractive color film process. Saturation: Modifies the saturation of colors qualified by the slice through a subtractive color model that keeps very saturated colors from turning unnaturally bright.

### Global ColorSlice Controls

Beyond the per-slice vectorspace controls, a row of global controls runs across the top of the tool. Those affect the values of the whole image.

### The ColorSlice Global controls

Density: Alters the luminance of the more saturated colors to imitate a subtractive color film process. Den.Depth: Governs how strongly density changes act on the brighter regions of the image. Saturation: Alters saturation through a subtractive color model that keeps very saturated colors from turning unnaturally bright. Sat.Balance: Governs the way saturation changes affect the luminance balance for colors sitting at medium saturation. Sat.Depth: Governs how strongly saturation changes act on the brighter regions of the image. Hue: Shifts the hue across every color in the image. Reset: Returns all ColorSlice adjustments to default.

### Using the Numeric Parameters

Beyond the Global controls described above, each vectorspace slice carries four numeric fields showing the current values of the Center, Hue, Density, and Saturation controls. You can edit these fields the same way you would any other parameter on the Color page. To set values directly:

- You can double-click a field to type its value in numerically.
- You can place the text cursor beside a value in the field and tap the Up and Down Arrow keys to change the value one digit per press.
- You can cut, copy, and paste values between fields.
- You can click a field and drag to the left or right to set its value using a virtual slider.

### Using Color Slice

Each vectorspace slice carries a center line that marks the color where most of the adjustment weight is applied. Dragging the Center control from side to side lets you pick which color gets qualified the most. Center is the lone control that qualifies colors; every other tool simply tweaks that qualification.

A bright white line marks the center of the Cyan color slice, and white lines on the clockwise and counterclockwise sides bound the extent of its color range.

While you move the Center control, you will want to review which colors are being qualified, either by pressing and holding the highlight icon at the top left of the vectorspace slice or by enabling the highlight in the Viewer. After the color range is selected, you just tune the Hue, Density, and Saturation controls of that vectorspace slice until the look matches what you want. Keep in mind that you don't have to pull a perfectly clean matte; you only need most of the colors you intend to boost to be selected. In this walkthrough we will rapidly qualify and adjust the sky and ocean together with the cyclist's skin tone, all within a single node and all at once using just the ColorSlice tool. Starting from this balanced image, the goal is to make the sky and ocean more vibrant and to bring out the sunset light hitting the cyclist.

### The original balanced shot we want to enhance

To begin, we launch the ColorSlice tool and switch the Viewer to B/W Highlight. With the Cyan vectorspace slice, we first nudge the Center control until the largest possible area of sky and ocean is qualified (white). After that we disable the highlight and move the density and saturation sliders to land a nicely vibrant sky and ocean.

Tuning the Cyan center control so the qualified area of sky and ocean is at its maximum (white)

The center, density, and saturation adjustments for Cyan (sky and ocean)

Next we switch to the Skin vectorspace slice, once more enabling the highlight and tuning the center until the greatest amount of the cyclist is qualified. As it happens, this also qualifies a fair amount of the hills behind him, which we'd rather avoid. We then disable the highlight and move the density and saturation sliders until a rich, warm glow lands on him (and the hills).

Tuning the Skin center control so the qualified portion of the cyclist is at its maximum (white). Note that a fair amount of the hills behind him is qualified too.

The Center, Density, and Saturation tweaks applied to Skin, bringing out the late-day sun striking the cyclist

We now move on to the next vectorspace slice, Yellow. With the highlight enabled, we tune the center control to maximize the portion of the hills behind him that gets qualified. Notice his skin tones are not picked up by this vectorspace slice, only the hills. We then disable the highlight and pull back the density and saturation on the hills that we had previously qualified in the earlier slice.

Tuning the Yellow center control to isolate just the hills (white). Note his skin tones are not qualified.

The Center, Density, and Saturation tweaks applied to Yellow, pulling only the hills back to a normal level after they had been unintentionally caught earlier by the Skin vectorspace slice.

The final image and result from those three fast ColorSlice operations.

The finished ColorSlice frame; three separate operations done in a single node with one tool. You might have spotted that the qualification mattes these operations produced were riddled with tiny holes, and you might expect a great deal of tedious matte finesse work to clean them up. With ColorSlice, every qualifier blends seamlessly into the rest, so there's no matte flicker or distracting speckles flashing in and out during playback. Naturally, for trickier shots you can still confine the ColorSlice effect with Power Windows, and even additional qualifiers, to steer the effect onto only the regions of the frame where you want it applied.
