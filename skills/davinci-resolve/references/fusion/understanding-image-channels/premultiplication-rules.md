# Understanding premultiplication and rules of premultiplication

Version: DaVinci Resolve 20.3 Reference Manual. Context: Understanding image channels.
[Chapter index](INDEX.md) / [Previous section](node-color-groups-and-channel-propagation.md) / [Next section](alpha-divide-multiply-and-multichannel-compositing.md)
<a id="source-alpha-channel-status-in-mediain-and-loader-nodes"></a> <a id="source-color-correcting-premultiplied-rgba-images"></a> <a id="source-controlling-premultiplication-in-color-correction-nodes"></a> <a id="source-double-premultiplied-rgba-means-double-trouble"></a> <a id="source-premultiplication-and-the-merge-node"></a> <a id="source-premultiplied-alpha-channels-and-filtering"></a> <a id="source-the-rules-of-premultiplication"></a> <a id="source-understanding-premultiplication"></a>

### Understanding Premultiplication

Having grasped how to steer and recombine RGB images and alpha channels within Fusion, it is now worth digging further into alpha channels so that you always pair RGB and alpha channels properly for every operation you carry out in your composite. It may look straightforward, yet tiny slip-ups happen easily and can leave behind ugly artifacts. This ranks among the most baffling corners of visual effects compositing, so don't bypass this section. Whenever a media file holds both alpha channel and RGB pixels — say a 3D rendered animation that carries RGB along with transparency, or a motion graphics movie file in which transparency is baked in — the pair can be joined in two distinct ways, and knowing which one applies matters.

- Unpremultipled (Straight): An RGB image left untouched by the semi-transparency data held in a fourth channel (alpha channel)
- Premultiplied: An RGB image whose every channel is multiplied by its alpha channel ahead of compositing.

Premultiplied alpha is a label editors, visual effects artists, and motion graphics designers have leaned on over the years, though it is loose. It is not the alpha channel that gets multiplied. Rather, the R, G, and B channels are multiplied by the alpha. Ultimately the alpha channel is unchanged, while the values held in the R, G, and B channels shift.

A RGB image (left) and its alpha channel (right)

Non-premultiplied images — at times referred to as “straight” alpha channels — carry RGB channels that the alpha channel has left untouched (not multiplied). As a consequence, the RGB image shows no anti-aliased edges and no semi-transparency. Typically you can plainly tell where the RGB image stops and the alpha matte starts. Below is an illustration of the ragged edges you get in the RGB channels with a non-premultiplied alpha channel. Note, though, the smooth semi-transparent edges present in the alpha.

A close-up showing, on the left, a non-premultiplied RGB image, with its alpha channel on the right With a premultiplied alpha channel, the RGB pixels have been multiplied by the alpha channel. That approach ensures the RGB image pixels carry semi-transparency where it is called for, such as anti-aliased edges. For the sake of convenience most computer-generated images come premultiplied, since that makes them simpler to review smoothly without ever dropping them into a composite.

A close-up showing, on the left, a premultiplied image, with its alpha channel on the right What is the upshot for compositing? A premultiplied image's edges look far smoother, which is what makes them preferable when you composite foreground over background in a merge. As a result, every alpha channel is rendered premultiplied within compositing operations if it was not already. Conversely, color correcting a non-premultiplied RGBA image is always the better course, because you would rather not disturb an image's pixel values once the RGB channels have been multiplied by the alpha channel. Looking at it through a mathematical lens:

- RGB pixel value x 0 = 0: The black transparent regions of an alpha channel hold a pixel value of 0. Take an RGB pixel's value, multiply it by 0 (n x 0 = 0), and by the rules of multiplication the RGB value drops to 0, or fully transparent.
- RGB Pixel value x 1 = RGB Pixel: The solid, opaque white regions carry a value of 1.0. Take an RGB pixel's value, multiply it by 1 (n x 1 = n), and the RGB value is unchanged, fully opaque.
- RGB Pixel value x 0.3 = A different color: Running along an alpha channel's edges are gray pixels that mark semi-transparency. Such semi-transparent pixels hold a value somewhere between 1.0 and 0.0. To carry the alpha channel's anti-aliased edges over to the RGB channels, you multiply the pixel values. That multiplication blends a certain proportion of the transparent pixels (black) into the RGB pixels. While this is what you want for clean anti-aliased edges, you cannot color correct the image afterward, since doing so disturbs the smooth semi-transparency you built once it is finished.

Multiplying RGB pixels against differing levels of transparency yields a changed RGB value.

### The Rules of Premultiplication

Building on what was laid out above, whenever you composite several images together and at least one carries a built-in alpha channel, you will want to stick to these broad rules so problems stay away:

- Always use premultiplied images with a Merge node.
- Only color-correct images that are not premultiplied.
- Always filter and transform images that are premultiplied.
- Never double premultiply an image.

### Premultiplication and the Merge Node

A Merge node's foreground input looks for a premultiplied RGBA image. Being an additive merge, it lays the foreground's semi-transparent regions over the background. Yet when the image is not premultiplied, the pixels meant to be transparent still get added in, which usually produces an unwanted bright fringe ringing your foreground subject's edges. Should you be compositing with a non-premultiplied alpha, you can cure these bright edges by switching the Merge over to a Subtractive merge in the Inspector.

On the left, nonpremultiplied edges within an additive Merge; on the right, premultiplied edges within an additive Merge

TIP: Suppose an RGB image and a Mask node are joined through, say, a Matte Control node; if the RGB image goes unmultiplied by the mask within the Matte control, the checkerboard background pattern in the viewer will look merely semi-transparent when it ought to be fully transparent.

### Color Correcting Premultiplied RGBA Images

Premultiplying an image binds any edits to the RGB pixels' brightness to the alpha channel pixels too. Raise the foreground image's brightness in any fashion, for instance, and you will lift the alpha channel's brightness as well, which is rarely what you want since it shifts the transparency the alpha channel produces. Viewed at the Merge node, the visible upshot is that the whole background grows brighter (or darker, had you dropped the RGB brightness) according to your color tweak. For that reason, the rule is to always divide the semi-transparent pixels before doing any color correction on an image bearing an alpha channel. You can pull this off by switching on the Pre-Divide/Post Multiply checkbox in any node that does color correction. Or you can lean on the Alpha Divide and Alpha Multiply nodes for the same effect. These approaches get fuller treatment later in this chapter.

On the left, color correcting a premultiplied foreground wrongly shifts the background; on the right, color correcting a nonpremultiplied foreground behaves correctly.

### Double Premultiplied RGBA Means Double Trouble

One frequent error many artists fall into is overcompensating for premultiplication. Premultiplying the alpha ahead of compositing within a Merge node is vital, yet just as vital is not premultiplying the alpha twice. Running a premultiply operation twice back to back can throw a darkened halo around your images. In effect you are multiplying by the gray semi-transparent pixels a second time; that is not ideal.

On the left, a double premultiplied image showing dark edges; on the right, a premultiplied image whose edges are correct

### Premultiplied Alpha Channels and Filtering

Where filtering is concerned, the RGBA channels' state ought to be irrelevant for the bulk of composites. An exception could crop up, though, when the filter algorithm you pick involves color modification. As an example, if a filter tries to mimic a defocus by blooming highlights the way a genuine light source would, that filter might over-brighten pixels close to a transparent edge, leaving some kind of artifact once that image is composited.

### Alpha Channel Status in MediaIn and Loader Nodes

Bringing a clip into the composite with a Loader node, you will find that the Import tab in the Inspector holds a set of checkboxes for deciding how an embedded alpha channel gets treated. These include a checkbox that makes the alpha channel solid (disregard transparency), one to Invert the alpha channel, and one to Post-Multiply the RGB channels against the alpha channel, where that proves necessary. With a MediaIn node, you can change how an embedded alpha channel is read by way of the Clip attributes window. The Clips Attributes window carries an Alpha Mode menu setting for picking whether the alpha channel is disregarded, taken as premultiplied, inverted, or taken as nonpremultiplied (straight).

### Controlling Premultiplication in Color Correction Nodes

The majority of nodes that make you explicitly handle an RGBA image's premultiplication state carry a “Pre-Divide, Post-Multiply” checkbox. That covers basic color correction nodes like Brightness Contrast and Color Curves, plus the Color Correct node, which keeps the “Pre-Divide/ Post-Multiply” checkbox inside the Options panel of its Inspector settings.

Shown in the Inspector, the Color Curves node's Pre-Divide/Post-Multiply checkbox This checkbox lets you wire an RGBA premultiplied image into the node and run a color correction operation. It takes in the RGBA image, runs a divide operation to strip out the semi-transparency, and then runs a multiplication operation before sending out the color corrected image. That way, the color correction happens on a nonpremultiplied image while the output that comes back is a Merge-friendly premultiplied image.
