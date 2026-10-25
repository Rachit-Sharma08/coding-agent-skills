# Ambient occlusion and depth blur

Version: DaVinci Resolve 20.3 Reference Manual. Context: Ambient occlusion, Depth blur.
[Chapter index](INDEX.md) / [Next section](depth-blur-and-fog-and-shader.md)
<a id="source-ambient-occlusion-as-a-2d-post-process"></a> <a id="source-ambient-occlusion-controls"></a> <a id="source-ambient-occlusion-node-introduction"></a> <a id="source-ambient-occlusion-ssao"></a> <a id="source-ao-tips-and-limitations"></a> <a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-common-controls"></a> <a id="source-controls-tab"></a> <a id="source-deep-pixel-nodes"></a> <a id="source-deep-pixel-nodes-part-1"></a> <a id="source-depth-blur-dbl"></a> <a id="source-depth-blur-node-introduction"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-inspector"></a> <a id="source-output-mode"></a> <a id="source-the-ambient-occlusion-node"></a> <a id="source-the-depth-blur-node"></a> <a id="source-usage"></a>

### Deep Pixel Nodes

The Deep Pixel nodes within Fusion are what this chapter covers. What Deep Pixel nodes can do is process AOVs (Arbitrary Output Variables) coming from 3D-rendered files.

The abbreviation shown beside every node name serves both as a search term inside the Select Tool dialog when hunting for tools and within scripting references. Throughout this document, any node tree depicting MediaIn nodes in DaVinci Resolve stands in for Loader nodes in Fusion Studio, except where a note states otherwise.

### Ambient Occlusion [SSAO]

### The Ambient Occlusion node

### Ambient Occlusion Node Introduction

Ambient Occlusion (AO) refers to the illumination that arises when a uniform diffuse spherical light source wraps around a scene. Picture the scene enclosed by an enormous sphere whose surface gives off light evenly in every direction. What AO records is the low frequency lighting. Sharp shadows, along with Diffuse or Specular lighting, lie outside what it records. For that reason, AO is generally paired with Diffuse and Specular lighting to assemble a complete lighting solution. As a post effect, the Ambient Occlusion node produces global lighting results across 3D-rendered scenes. It offers a fast approximation of the computationally costly ray-traced global illumination. Since it runs as a post effect, it surfaces aliasing problems much like the Shader, Texture, and Volume Fog nodes do. Consequently, certain circumstances may bring out artifacts.

### Usage

Seldom does the AO node deliver correct results untouched; some adjustment is needed. Getting it set up means tuning the Kernel Radius along with the Number Of Samples until the look you want appears. How large the Kernel Radius should be hinges on the scene’s inherent “scale.” At the outset it can seem as though no AO shows up whatsoever. Most often the Kernel Radius sits too small or too large, and you have to hunt down values that work.

### Inputs

The AO node carries three inputs. To confine the AO effect, the standard effect mask comes into play. Both the Input and Camera connections are mandatory. Leave out either one and the node produces no image at its output. Input: This orange input takes a 2D RGBA image, Z-Depth, and Normals. Camera: That green camera input will accept either a 3D Scene or the 3D Camera that rendered the 2D image. Effect Mask: This optional blue effect mask input takes a mask shape built from polylines, simple primitive shapes, paint strokes, or bitmaps coming from other tools. Wiring a mask into this input confines the Ambient Occlusion to just the pixels falling inside the mask. An effects mask gets applied to the tool once the tool has finished processing.

### Basic Node Setup

You normally drop the Ambient Occlusion node in after a Renderer 3D node. That Renderer 3D node has to have Z-Depth and Normals switched on among its output channels. The Camera3D the Renderer3D node renders then gets wired into the camera input on the AO node.

### Ambient occlusion as a 2D post process

### Inspector

### Ambient Occlusion controls

### Controls Tab

Every primary control for compositing with AO lives on the controls tab. It governs how good and how the effect looks.

### Output Mode

- Color: Picking the Color menu option merges the arriving image together with Ambient Occlusion laid on top.
- AO: This choice puts out the raw Ambient Occlusion as a grayscale image. Bright areas of the picture map to white, whereas the areas meant to be darker map to black. That lets you build a lighting equation by joining separate ambient/diffuse/ specular passes. Keeping the AO as its own buffer grants you the creative latitude to blend the passes in all sorts of ways.

Kernal Type AO is worked out by shooting rays off a point on the shaded surface, outward toward a big enclosing sphere. Whichever rays reach the sphere unobstructed set the AO factor.

- Hemisphere: Rays head toward a hemisphere aligned with the surface’s normal. Being more lifelike than Sphere, this choice ought to be used barring a solid reason not to. Flat surfaces take on 100% ambient intensity, while the remaining parts get darkened.
- Sphere: Rays head toward a sphere centered on the point under shading. This choice exists to deliver a stylistic look. Flat surfaces take on 50% ambient intensity, while the remaining parts grow darker or brighter.

Number of Samples Push the samples upward until artifacts across the AO pass vanish. Larger values can yield finer results yet also lengthen render time. Kernel Radius What the Kernel Radius governs is how large the filter kernel is within 3D space. Per pixel, it governs how far the search for occluders reaches into 3D space. You should dial in the Filter Kernel by hand for every separate scene. Set it too small and nearby occluders may go unseen. Set it too large and the AO quality drops, forcing you to crank the samples way up to win that quality back. This value rides on the scene Z-depth. So with enormous Z values throughout the scene, the kernel size has to be large to match. With minuscule Z values, a modest kernel size around 0.1 ought to do. Lift/Gamma/Tint The lift, gamma, and tint controls are there for you to tweak the AO toward artistic ends.

### Common Controls

Settings Tab A copy of the Settings tab in the Inspector also turns up across the other Deep Pixel nodes. Those shared controls get covered thoroughly at this chapter’s close within the “The Common Controls” section. TIP: Blending several AO passes that use differing kernel radii can yield finer effects.

### AO Tips and Limitations

Transparency/Translucency: Opaque objects are what AO is built to handle. Known shortcomings exist with transparent receivers as well as transparent occluders. Some of those shortcomings can be sidestepped by pulling the transparent/translucent objects out into separate scenes and computing AO solely on the opaque objects. Particles: Owing to the transparency/translucency shortcomings, steer clear of using AO on particles unless those particles are solid opaque geometry. Anti-aliased edges count as yet another kind of transparency, so they too trip up AO. Supersampling: For rendering anti-aliasing alongside Ambient Occlusion, switch on HiQ for the Z and Normals pass within the Renderer 3D. Viewer Dependence: AO methods operate in viewer space, leaving the outcome viewer dependent. What this means is the degree of darkening can shift with the viewing position when it really ought to hold constant. Where the AO at a point on an object reads 0.5, shifting the camera might turn it into 0.4. Baking of AO: The OpenGL UV renderer can serve to bake AO down into the textures on models.

### Depth Blur [DBl]

### The Depth Blur node

### Depth Blur Node Introduction

What the Depth Blur node chiefly serves is producing focal length or depth-of-field looks. Drawing on the bundled Z-channel values, it blurs 3D-rendered images, and through the Blur Channel controls it can equally drive general per-pixel blurring effects.

### Inputs

Three inputs come with the Depth Blur node: one carrying the main image, one carrying a blur image, plus another carrying an effect mask to bound the region where the depth blur lands. Input: This orange input is the lone connection that’s required. It takes a 2D image carrying a Z channel. That Z channel sets how much blur applies across the differing regions of the picture. Blur Image: Wire up the Blur Image input and the image’s channels then steer the blur. That opens up general 2D per-pixel blurring effects. Effect Mask: This optional blue effect mask input takes a mask shape built from polylines, simple primitive shapes, paint strokes, or bitmaps coming from other tools. Wiring a mask into this input confines the depth blur to just the pixels falling inside the mask. An effects mask gets applied to the tool once the tool has finished processing.

### Basic Node Setup

The image holding the Z channel is what feeds the Depth Blur node. Down below, the Z depth channel arrives as a standalone image file and gets merged with the RGB (beauty) image by way of a Channels Booleans tool. Channel Booleans is set so the Z buffer channel copies into the luminance foreground.

Working from a Z depth channel, Depth Blur lands on the beauty image Inspector
