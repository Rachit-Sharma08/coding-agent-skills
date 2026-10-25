# Difference keyer and luma keyer

Version: DaVinci Resolve 20.3 Reference Manual. Context: Difference keyer, Luma keyer.
[Chapter index](INDEX.md) / [Previous section](depth-map-and-difference-keyer.md) / [Next section](luma-keyer-controls-tab.md) / [Continue Luma Keyer LKy / Controls Tab](luma-keyer-controls-tab.md) / [Difference Keyer DFK](depth-map-and-difference-keyer.md)
<a id="source-basic-node-setup-2"></a> <a id="source-common-controls-2"></a> <a id="source-controls-tab-1"></a> <a id="source-inputs-2"></a> <a id="source-luma-keyer-lky"></a> <a id="source-luma-keyer-node-introduction"></a> <a id="source-the-difference-keyer-controls-tab"></a> <a id="source-the-luma-keyer-node"></a>

### The Difference Keyer Controls tab

### Controls Tab

Every parameter for tuning the matte's quality sits on the Difference Keyer's Controls tab. Threshold This range slider pins the lower threshold with the left handle and the upper threshold with the right. Moving them carves out a span of difference values between the two images from which the matte is built. A difference under the lower threshold goes black or transparent in the matte. A difference over the upper threshold goes white or opaque. The difference values that fall between yield a grayscale matte.

Filter This picks which filtering algorithm runs when a blur is laid onto the matte.

- Box: The quickest approach, though quality drops. Box fits best where blur is kept small.
- Bartlett: Also called a Pyramid filter, Bartlett strikes a sound balance of speed against quality.
- Multi-box: Choosing this brings up the Num Passes slider so you can steer the quality. With 1 and 2 passes you match Box and Bartlett in turn. From 4 passes upward, the output usually rivals Gaussian, faster and free of edge "ringing."
- Gaussian: Built on a genuine Gaussian approximation, the Gaussian filter yields superb output, albeit a touch slower than the rest. Now and then it leaves an exceedingly faint edge "ringing" on floating-point pixels.

Blur This softens the matte's edge with whatever method the Filter menu has chosen. Set it to zero and you get a crisp, cutout-style hard edge. Push it higher for more blur. Clipping Mode This setting governs how edges behave during domain of definition rendering. It matters greatly when you blur the matte, since that may pull samples from parts of the image beyond the current domain.

- Frame: Frame, the default, automatically hands the node's domain of definition the image's whole frame, in effect disregarding the current domain of definition. Should the upstream DoD fall short of the frame, the leftover frame area counts as black/transparent.
- Domain: Switch to Domain and the node honors the upstream domain of definition as its effect runs. That can clip badly wherever the node reaches for a large filter.
- None: Choose None and no source image clipping happens whatsoever. Consequently, any data the node's effect needs that would normally lie beyond the upstream DoD counts as black/transparent.

Contract/Expand This slider trims or swells the matte's semitransparent zones. Above 0.0 it expands the matte; below 0.0 it pulls it in. You'll usually pair it with the blur to soften a matte's hard edge and cut fringing. Because it touches only semitransparent zones, it leaves a matte's hard edge alone. Gamma Matte Gamma pushes the matte's values up or down across the semitransparent zones. Larger values make the gray areas more opaque; smaller ones make them more transparent. Fully black or white parts of the matte stay put. Invert Tick this checkbox to flip the matte, turning every transparent area opaque and every opaque area transparent.

Solid Matte A Solid Matte is any mask node or image fed to the node's solid matte input. It lands directly on the image's alpha channel. Typically a solid matte shields keying wherever you need things kept opaque, say a blue-eyed person standing against a blue screen. Turn on Invert and the solid matte is flipped ahead of its merge with the source alpha. Garbage Matte A Garbage Matte is any mask node or image fed to the node's garbage matte input. It too lands directly on the image's alpha channel. Typically a garbage matte clears away stray elements no key can handle, microphones and booms among them. It can likewise fill spots that carry the keyed color but which you mean to hold onto. Within a single tool, garbage mattes of unlike modes won't mix. A frequent move is placing a Matte Control node downstream of a Keyer node so it adds a garbage matte that counters the matte handed to the keyer. Turn on Invert and the garbage matte is flipped ahead of its merge with the source alpha. Post-Multiply Image Pick this so the keyer multiplies the image's color channels by the alpha channel it makes for that image. It tends to be enabled and ships on by default. Uncheck it and, for merging with other images, the image no longer reads as premultiplied. There, lean on the Merge node's Subtractive option in place of the Additive one. To dig into these Merge node settings, consult the DaVinci Resolve Reference Manual at Chapter 95, "Composite Nodes," or, equivalently, the Fusion Reference Manual at Chapter 35.

### Common Controls

Settings Tab The same Settings tab in the Inspector appears on the remaining Matte nodes as well. Detailed coverage of these common controls lives at the tail end of this chapter, within "The Common Controls."

### Luma Keyer [LKy]

### The Luma Keyer node

### Luma Keyer Node Introduction

The Luma Keyer node forges an Alpha channel out of an image's overall luminance. Its name can mislead a bit, given that it can pull mattes from nearly any channel. By one measure it's truer to think of this node as a general-purpose channel keyer, yet its chief role remains extracting alpha channels from luminance

### Inputs

Inside the Node Editor, the Luma Keyer node carries four inputs. Input: This orange input takes a 2D image holding the luminance values you want keyed for transparency. Garbage Matte: The gray garbage matte input takes a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wire a mask here and the image regions inside that matte turn transparent. That garbage matte goes straight onto the image's alpha channel. Solid Matte: The white solid matte input takes a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wire a mask here and the image regions inside that matte turn fully opaque. Effect Mask: The optional blue input looks for a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wire a mask here to confine which pixels the luminance key touches. That effects mask reaches the tool only after the tool has finished processing.

### Basic Node Setup

The Luma Keyer pulls a key from an image whose luminance varies markedly. From there, the Luma Keyer's output can route into any mask input you like.

A Luma Keyer output wired into a Merge node's effect mask Inspector
