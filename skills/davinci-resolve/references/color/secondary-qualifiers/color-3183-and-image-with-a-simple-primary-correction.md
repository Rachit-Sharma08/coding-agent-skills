# Color 3183 and image with a simple primary correction

Version: DaVinci Resolve 20.3 Reference Manual. Context: Secondary qualifiers.
[Chapter index](INDEX.md) / [Next section](hsl-qualification-and-color-picker.md)
<a id="source-a-sampled-key-thats-ready-for-further-refinement"></a> <a id="source-adding-a-secondary-operation-to-the-node-editor"></a> <a id="source-basic-qualification-using-the-3d-qualifier"></a> <a id="source-color-3183"></a> <a id="source-qualifier-palette-with-hsl-controls-selected"></a> <a id="source-secondary-qualifiers"></a> <a id="source-secondary-qualifiers-part-1"></a> <a id="source-set-the-default-qualifier-mode"></a> <a id="source-the-3d-qualifier"></a> <a id="source-the-final-adjusted-image"></a> <a id="source-the-image-with-a-simple-primary-correction"></a> <a id="source-the-qualifier-interfaces"></a> <a id="source-which-qualifier-do-i-use"></a>

### Secondary Qualifiers

Secondary correction means singling out a particular region of the image, or a particular subject, by means of a key. In DaVinci Resolve, keys are grayscale images marking which parts of the picture you intend to change (in white) and which parts you intend to leave untouched (in black). You can produce keys with the Qualifier palette's controls, with a Power Window, or by importing an external matte. For more on putting external mattes to use, see Chapter 146, "Combining Keys and Using Mattes." The focus of this chapter is using qualifiers to key a range of color values (much as you'd pull a green screen key) so as to build a matte for this sort of isolated adjustment.

### COLOR 3183

This section deals with the Qualifier palette. From it you can pull a key, be it 3D, HSL, RGB, or Luma, for isolating the correction you require. When you have to single out an irregularly shaped subject carrying a distinct range of color or lightness, the Qualifier controls are quick and adaptable. Because you generate a key by sampling the image, no tracking or keyframing is called for, so in the right circumstances qualifiers can be your speediest answer. In the example that follows, the client is happy with the somewhat cool overall treatment but wishes the skin tones had a bit more life. This is precisely where qualifiers prove helpful. Adding a second node and using the 3D or HSL Qualifier to single out the face makes it fairly easy to put color exactly where you want.

A second node added, with HSL Qualification singling out the skin tones

### The image with a simple primary correction

### The final adjusted image

Nearly every control on the Color page can be confined using one of the Qualifier modes DaVinci Resolve provides. That turns the Qualifier palette into a jack-of-all-trades tool boasting 101 uses. A handful of practical cases: keying a red element too hot for broadcast in order to darken or desaturate it; keying a span of green foliage so its hue shifts to something prettier; keying an actor's skin tone in a commercial to apply selective softening; or keying a stretch of sky into which you add blue. While you're using Resolve Color Management (RCM) or ACES, the Qualifier palette is color-space-aware. That lets Qualifiers build high-quality keys just as you'd expect, whatever the original media's color space happens to be, and whatever Timeline Color Space you're on, across both SDR and HDR mastering. The upshot is easier Qualifier isolations and a steadier experience no matter what your workflow is.

### Adding a Secondary Operation to the Node Editor

Any node can be flipped between acting as a primary correction, where your adjustments hit the whole image, and a secondary correction, where you're tuning one specific element in the scene. The sole distinction is that nodes serving as secondary corrections are confined using a qualifier, Power Windows, or an external matte.

When you plan to add a secondary operation to the current grade, you first need to add another node in the Node Editor. As you pull a key to qualify part of the image, it helps to grasp that you'll be sampling the YRGB values fed into that node by any earlier nodes in the tree. That is, the state of the image arriving at a node you're qualifying shapes the key you pull. If, say, the image leaving Node 1 is well saturated with a neutral color balance and a wide spread of colors, while the image leaving Node 2 lays on a low-saturation, monochromatically orange color wash, you may find pulling a detailed key off Node 2 harder than off Node 1.

Choosing your battles–keying the image leaving Node 1 is easier than keying the heavily stylized one leaving Node 2 This matters because you have the freedom to decide which image you'll try pulling a qualified key from. By wiring the node that puts out the best YRGB image for the key you're after to the node you're qualifying, you govern what you key. For more about which node to use when setting up a qualifier, see Chapter 146, "Combining Keys and Using Mattes."

### The Qualifier Interfaces

The DaVinci Resolve Qualifier palette interface is uncomplicated. On the left, graphical controls above numeric parameters let you manually set what ranges of each color component feed the key you're building. Over on the right, the Selection Range tools below let you set a key by using the pointer to sample image pixels, while a set of Matte Finesse parameters beneath those lets you reshape the key you've pulled.

### Qualifier palette with HSL controls selected

By default the qualification mode is the HSL Qualifier, which leans on three color components, hue, saturation, and luma, to define a key. You can, however, also reach for the RGB or LUM (Luma) qualification modes to pull keys from other color-component blends. The LUM qualifier mode especially lets you tune particular ranges of image lightness in a targeted way. Many colorists use this technique to shift color temperature inside a specific range of image highlights or shadows. Alternatively, the 3D qualifier lets you swiftly and easily pull well-refined keys by drawing lines that sample colors from the image corresponding to volumes of color within a three-dimensional gamut. Sophisticated as the underlying technology is, all that's asked of you is to draw blue lines sampling colors you want isolated, or red lines sampling colors you want subtracted from the isolation you're making, all of which automatically yield a high-quality key. Every line you draw puts a sample onto the selection list; you can switch each sample off and on to judge how much it adds to the resulting key, or remove samples that aren't pulling their weight.

### The 3D qualifier

Whichever qualifier mode you pick, the Matte Finesse controls make refining the resulting key into something cleaner and more usable straightforward. In some cases you can even rescue a marginal, otherwise-unusable key, coaxing it into something useful with the Clean Black, Clean White, and Blur Radius controls.

### Which Qualifier Do I Use?

The Qualifier palette's four modes give you the latitude to reach for whichever keyer best suits the task of isolating some range of color or brightness values. Sometimes keys hard to pull in one mode are easier in another. Here's a quick rundown: HSL: Often the HSL keyer isn't as instantly accurate as the 3D keyer and pulls in a wider slice of the image for any given sample. On the flip side, when the 3D keyer isn't getting you satisfactory results on a particular shot, the HSL keyer can sometimes do better. Because of its interface, the HSL keyer makes it simpler to "fine-tune" both the range and the softness of every sampled color component on its own to improve the result. The HSL keyer also lets you switch off color components you don't want feeding the final key, so a saturation-only key, or a hue-only key, becomes possible wherever that solves the problem at hand.

RGB: The RGB keyer carries much of the HSL keyer's limits and strengths, yet because what you sample and adjust are the red, green, and blue color components, the precision available for fine-tuning the resulting key works out quite differently. LUM: The LUM keyer works specifically to single out parts of the image by image tonality, lightness, or darkness. It's the ideal tool when you're after highlights or shadows in the image, which lets you address a host of creative and technical problems. The LUM keyer matches using the HSL keyer with the Hue and Saturation qualifier controls switched off. 3D: The 3D keyer makes a good starting point whenever your aim is to isolate some color range, say a blue shirt, a cyan sky, a performer's skin tone, or an autumn tree's orange leaves. Its way of drawing lines over the part of the image you want isolated, together with its high quality and extreme specificity, make it a fast, accurate tool across many situations. The 3D keyer always samples every color component of the image, though; it's no help when you want to isolate specific color components, like luma only, or hue and saturation without luma. The 3D keyer's biggest strength, the speed at which you sample picture areas to include (or exclude) from the final key, is also now and then a weakness on images where your first samples aren't giving you what you want, because few avenues exist to fine-tune the key as it's being built (the result is still yours to manipulate). On the other hand, across most images you'd want to qualify, two or three samples does the job, paired with the Matte Finesse controls for adjusting the resulting key. Should you need to do some compositing on the Color page, the 3D keyer also excels at blue and green screen keying to create transparency, and carries a built-in Despill control too.

### Set the Default Qualifier Mode

You can have your favorite qualifier open as the default whenever you apply a qualifier to a fresh clip on the timeline. That can save plenty of clicks over a project's life. As you'd expect, if a qualifier other than the default has already been applied to the clip, that one opens instead. To change the Default Qualifier, click the Qualifiers (3-dot) Option menu, select Default Qualifier, and pick an option from the list.

Switching the Default Qualifier over to 3D, so new clips now open the 3D qualifier rather than the HSL qualifier

### Basic Qualification Using the 3D Qualifier

The 3D Qualifier mode hands you a quick, simple route to pulling a key that isolates a color range in the picture, by drawing lines over the parts you want keyed. Every line drawn across the picture either grows or shrinks the value cloud being sculpted out of a three-dimensional representation that holds every available color; you never lay eyes on that representation, but this "under the hood" behavior is what gives the 3D keyer its name. As a general-purpose keyer, the 3D keyer lets you isolate whatever color you like. The 3D keyer is poor at pulling luma-only keys, though. When you want to isolate a range of luma values in the image, turn to the LUM mode instead. To single out a subject in the Viewer via the 3D mode: 1 Open the Qualifier palette, pick the 3D icon at the upper right, and click the eyedropper. 2 To draw a line, click and drag over whichever part of the image you mean to isolate. Blue is the color of lines that add to the key.

Drawing a line that builds a key with the 3D qualifier 3 To watch the key take shape as you go, click the Highlight button in the Viewer Options toolbar atop the Viewer. While you draw the line, the viewer updates to display your current key in real time.

Viewing the key using the Highlight button

4 If needed, draw more lines to bring additional parts of the image into the key you're building. Generally it's smart to keep to two or three lines at most when sampling whatever part of the image you're out to isolate. A handful of long strokes works better than many short ones. What you ideally want is a key with a fairly soft edge, since that makes fine-tuning your result with the Matte Finesse controls easier afterward. Draw too many lines to sample the image and the result can be a key with hard, jagged edges that's sometimes harder to adjust later.

A hard-edged key created with three samples 5 Or, if there are parts of the image included in the key that you'd rather drop, hold the Option key and draw a line over those areas. Notice that Option-drawn lines are red, and these subtract regions from the key you're building. Again, don't go overboard drawing subtractive red lines, or you can wind up with an overly hard-edged key that's tough to adjust with other controls in the next few steps. Beyond that, you can still use power windows together with the 3D qualifier to leave out specific parts of the image.

Blue lines build up the key while a red line removes the grass from it, shown here with the highlight switched off 6 Should you ever wonder whether some sample in the list at left is helping at all, click the color patch at the left of any list entry to toggle that sample off and on. Decide you don't need a particular sample and you can click the trash can button at the right to delete it.

Controls that toggle samples off and on, plus remove them from the list 7 As soon as you're sure the key is solid enough to start fine-tuning, quit drawing lines. A bit of noise, speckling, or a few small holes in the key you're building is all right, because the Matte Finesse controls can take care of those.

### A sampled key that's ready for further refinement

Nearly every key you pull will gain from a little further "post-key" refinement. What that comes down to is this: once you've built the best key you can procedurally through image sampling, the resulting key itself, nothing more than a gray-scale image, is now open to adjustment so as to better the isolated result. That's the job of the Matte Finesse controls.

Matte Finesse controls 8 The three most common ways to refine a key with the Matte Finesse controls are raising Clean Black to fill "holes" in the parts of the image you're dropping (the background), raising Clean White to close holes in the part you're isolating (the foreground), and then using Blur Radius and In/Out Ratio controls to soften the key's edge and push it in and out. With these controls, you can hugely improve nearly any key without endlessly readjusting the Qualifier controls. There's more on the Matte Finesse controls later in this chapter. 9 Once finished, click the Highlight control so the highlight turns off, then apply whatever adjustment is called for. Here, the Hue control is used to swing the helicopter's orange around to blue.

Adjusting the orange color of the helicopter to be blue instead
