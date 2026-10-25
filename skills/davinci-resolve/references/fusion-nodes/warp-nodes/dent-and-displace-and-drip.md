# Dent and displace and drip

Version: DaVinci Resolve 20.3 Reference Manual. Context: Dent, Displace, Drip.
[Chapter index](INDEX.md) / [Previous section](coordinate-space-and-corner-positioner.md) / [Next section](drip-and-grid-warp.md)
<a id="source-basic-node-setup-2"></a> <a id="source-basic-node-setup-3"></a> <a id="source-common-controls-2"></a> <a id="source-common-controls-3"></a> <a id="source-controls-tab-2"></a> <a id="source-controls-tab-3"></a> <a id="source-dent-dnt"></a> <a id="source-dent-node-introduction"></a> <a id="source-displace-dsp"></a> <a id="source-displace-node-introduction"></a> <a id="source-drip-drp"></a> <a id="source-drip-node-introduction"></a> <a id="source-inputs-2"></a> <a id="source-inputs-3"></a> <a id="source-inputs-4"></a> <a id="source-inspector-2"></a> <a id="source-inspector-3"></a> <a id="source-the-dent-controls-tab"></a> <a id="source-the-dent-node"></a> <a id="source-the-displace-controls-tab"></a> <a id="source-the-displace-node"></a> <a id="source-the-drip-node"></a>

### Dent [Dnt]

### The Dent node

### Dent Node Introduction

The Dent node bends an image into a circular deformation akin to a Fish Eye Lens look, offering a pick of six distinct Dent filters.

### Inputs

There are two inputs on the Dent node, for attaching a 2D image plus an effect mask, with the mask serving to confine the warped region. Input: The orange input takes the main 2D image getting warped. Effect Mask: Into the blue input goes a mask shape built from polylines, simple primitive shapes, paint strokes, or bitmaps from other tools. Plugging a mask in here limits the Dent to only the pixels sitting inside the mask. The effects mask is applied to the tool after that tool has been processed.

### Basic Node Setup

Below, the Dent node shapes a circular pattern that's driven by a Fast Noise together with a Mosaic Blur (DaVinci Resolve Resolve FX only). Sitting at the tail end, the Crop node is what locks in whichever resolution you're after.

The Dent node lends a hand in producing lens-distortion looks or a backdrop for motion graphics.

### Inspector

### The Dent Controls tab

### Controls Tab

The settings on the Controls tab let you alter the Dent's style, position, size, and strength.

Type Choose from this menu which kind of Dent filter you'd like. Every Dent parameter can be keyframed. Dent 1 Produces a bulging dent. Kaleidoscope Forms a dent, then mirrors it and inverts it. Dent 2 Produces a displacement dent. Dent 3 Produces a deform dent. Cosine Dent Produces a fracture toward a central point. Sine Dent Produces a smooth, rounded dent. Center X and Y This places the Center of the Dent effect onto the image. By default the values are 0.5, 0.5, which sit the effect at the image's center. Size This alters how large an area the dent touches. Animate the slider to make the dent expand. Strength This adjusts the dent's overall strength.

### Common Controls

Settings Tab The Inspector's Settings tab here is mirrored across the other Warp nodes as well. A complete description of these shared controls waits at the end of this chapter in the "The Common Controls" section.

### Displace [Dsp]

### The Displace node

### Displace Node Introduction

By way of a map image, the Displace node shifts or refracts a second image. That's handy for producing a huge spread of effects, running from bevels and heat distortion through to glass and water looks.

### Inputs

Three inputs sit on the Displace node: the primary image, the foreground image serving as the displacement map, plus an effect mask. Input: A required connection, the orange image input, carries the primary image you mean to displace. Foreground Image: The green input is likewise mandatory, holding the image that drives the displacement of the background. With it connected, you can pick the red, green, blue, alpha, or luminance channel to build the displacement from. Effect Mask: The optional blue effect mask input wants a mask shape created out of polylines, simple primitive shapes, paint strokes, or bitmaps from other tools. Wiring a mask here keeps the displacement confined to the pixels within the mask. The effects mask is applied to the tool once it has been processed.

### Basic Node Setup

In the setup below, the Displace node draws on a Fast Noise to build the Displace map. Pushing up the seethe rate can yield heat-distortion looks or a waving-flag effect.

The Displace node using a Fast Noise node for the Displace map

### Inspector

### The Displace Controls tab

### Controls Tab

The Controls tab is where you adjust the displacement's style, position, size , strength, and lighting (embossing). Type The Type menu lets you select which mode the Displace node runs in. Radial mode leans on the map image to refract each pixel outward from the center, whereas X/Y mode hands you control over how much displacement happens along each axis on its own. NOTE: Radial mode gives you a single set of Refraction controls, while XY mode supplies two sets—one apiece for the X and Y channels. Center (Radial Only) Where pixels get pushed toward or pulled away from is marked by the Center control. Refraction Channel This drop-down governs which channel of the foreground image drives the image's displacement. Pick from the Red, Green, Blue, Alpha, or Luminance channels. Under XY mode this control shows up twice, once for X displacement and once for Y displacement. Refraction Strength (Radial) Sets how strong the refraction is. Bigger values bring on stronger, more pronounced refraction. X and Y Refraction (X/Y) A pair of separate sliders shows up so the Refraction strength can be set along the X- and Y-axis independently. Apart from that, it behaves just like Refraction Strength. Light Power This governs how intense, or strong, the simulated light is, making bright and dim regions appear that follow the contour of the refraction image. Larger values render those bright and dim regions more pronounced.

Light Angle This dictates the angle the simulated light source comes from. Spread This broadens the Displacement effect and softens the edge of the Refraction map. Larger values make the ridges or edges fan out. Light Channel Decide which channel of the refraction image stands in as the simulated light source. Your options are the Color, Red, Green, Blue, Alpha, or Luminance channels. NOTE: In Radial mode, pixels are driven inward or outward away from a central point according to the pixel values read off the Displacement map. XY mode draws on two separate channels of the map to shift pixels both horizontally and vertically, which buys you tighter precision. Working in XY mode, the Displace node is even capable of pulling off basic morphing effects. Meanwhile the Light controls bring directional highlighting to refracted pixels, faking a beveled appearance.

### Common Controls

Settings Tab This node's Settings tab in the Inspector recurs on the other Warp nodes too. The shared controls are laid out in full toward the end of this chapter, in the "The Common Controls" section.

### Drip [DRP]

### The Drip node

### Drip Node Introduction

Across the whole image, the Drip node lays down a ripple effect that can be made to animate outward from a central origin. A selection of differing Drip effects is on offer.

### Inputs

The Drip node provides two inputs, used to attach a 2D image and an effect mask, where the mask can confine the warped region. Input: Send the main 2D image getting warped into the orange input. Effect Mask: The blue input expects a mask shape formed from polylines, simple primitive shapes, paint strokes, or bitmaps from other tools. Hooking a mask in here keeps the warping bound to only the pixels inside the mask. That effects mask is applied to the tool once the tool has been processed.
