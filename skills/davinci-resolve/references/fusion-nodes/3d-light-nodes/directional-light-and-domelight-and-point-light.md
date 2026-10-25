# Directional light and domelight and point light

Version: DaVinci Resolve 20.3 Reference Manual. Context: Directional light, Domelight, Point light.
[Chapter index](INDEX.md) / [Previous section](ambient-light-and-directional-light.md) / [Next section](point-light-and-spot-light.md) / [Directional Light 3DL](ambient-light-and-directional-light.md)
<a id="source-basic-node-setup-2"></a> <a id="source-basic-node-setup-3"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab-2"></a> <a id="source-controls-tab-3"></a> <a id="source-dome-light-node-introduction"></a> <a id="source-dome-light-node-structure"></a> <a id="source-domelight-3do"></a> <a id="source-inputs-2"></a> <a id="source-inputs-3"></a> <a id="source-inspector-2"></a> <a id="source-inspector-3"></a> <a id="source-point-light-3pl"></a> <a id="source-point-light-controls"></a> <a id="source-point-light-node-introduction"></a> <a id="source-point-light-node-structure"></a> <a id="source-shadows"></a> <a id="source-the-dome-light"></a> <a id="source-the-dome-light-controls"></a> <a id="source-the-point-light-node"></a>

### Shadows

The controls here let you define the shadow map this light draws on when casting shadows. For deeper coverage, turn to “3D Compositing Basics” — that is Chapter 85 in the DaVinci Reference Manual, or alternatively Chapter 23 over in the Fusion Reference Manual.

NOTE: For the Directional light to throw visible shadows in the 3D viewer, the Renderer3D node must have its Rendering Type set to Hardware Renderer.

Enable Shadows Tick the Enable Shadows checkbox when you want the light to throw shadows; it is on by default. Shadow Color This standard Color control chooses the shadow's hue, defaulting to black (0, 0, 0). Density How opaque the shadow is comes down to its density: a setting of 1.0 yields a fully solid shadow, and smaller values let more light through. Shadow Map Size The Shadow Map Size control fixes how big the bitmap behind the shadow map is. Bigger values give finer shadow maps but cost more memory and speed. Shadow Map Proxy Shadow Map Proxy governs the shadow map's size while the Proxy or Auto Proxy modes are active. Setting it to 0.5, for instance, yields a shadow map running at half whatever resolution the Shadow Map Size specifies. Multiplicative/Additive Bias Because shadows are really textures laid over scene objects, Z-fighting can crop up, where the parts of an object that ought to catch the shadow instead draw over it. Bias counters this by nudging the shadow a small depth offset away from the surface it falls on, clearing the Z-fighting. With too little bias the objects shadow themselves; with too much the shadow drifts off the surface. Set the Multiplicative Bias first, then refine using the Additive Bias control. Further detail lives in the Multiplicative and Additive Bias portion of “3D Compositing Basics,” which is Chapter 85 of the DaVinci Resolve Reference Manual, or else Chapter 25 within the Fusion Reference Manual. Force All Materials Non-Transmissive By default an RGBAZ shadow map handles the rendering; switch this on and you push the renderer toward a Z-only shadow map instead. That can speed shadow rendering up considerably while consuming only a fifth of the memory, at the cost of losing “stained glass”-style colored shadows. Shadow Map Sampling Sets how finely the shadow map gets sampled. Softness Filtering the shadow map as it is sampled is what gives shadow edges their softness, and Fusion offers two distinct filtering approaches that behave differently. NOTE: A hard-edged shadow skips filtering entirely. Its upside is that a single pixel of the shadow map needs sampling, which keeps it quick.

- Constant: Shadow edges carry a uniform softness. The shadow map is sampled with a fixed-width filter, and the Constant Softness slider scales that filter; bear in mind that a wider filter lengthens shadow render times.
- Variable: Shadow edges soften more the farther the receiver sits from the caster. This variable softness comes from resizing the filter according to the receiver-to-caster distance, and choosing it reveals the Softness Falloff, Min Softness, and Max Softness sliders.

Constant Softness This slider shows up when Softness is set to Constant, and it governs the shadow's overall softness. Softness Falloff Visible when Softness is set to variable, this slider sets how quickly edge softness climbs with distance — more exactly, how fast the shadow map filter widens as the gap between caster and receiver grows, bounded by the Min and Max Softness values. Min Softness Appearing when Softness is Variable, this slider sets the shadow's Minimum Softness: the nearer the shadow is to its casting object, the crisper it stays, down to this slider's floor. Max Softness Also shown when Softness is Variable, this slider sets the shadow's Maximum Softness: the farther the shadow lies from its casting object, the softer it grows, up to this slider's ceiling.

### Common Controls

Transform and Settings Tabs You will encounter the Transform and Settings tab parameters on the other lighting nodes too. For a closer look at what those tabs control, refer to the “The Common Controls” section at the end of this chapter.

### DomeLight [3Do]

### The Dome light

### Dome Light Node Introduction

A Dome Light draws on SDR and HDR images, wrapping the whole scene inside a sphere that is light-mapped with the image, much like an environment light. This light shows an onscreen control.

### Inputs

This node offers an optional orange input for a 3D scene or 3D geometry plus a white Dome Texture input where you attach an image. SceneInput: The optional orange input takes a 3D scene; once one is connected, this node's Transform controls act on the whole scene. DomeTexture: The white input is where an SDR or HDR image plugs in.

### Basic Node Setup

The Dome Light node is meant to sit inside a larger 3D scene. Connect the light straight into a Merge 3D, and keep lights in distinct Merge 3D nodes so you can dictate which objects each light influences.

### Dome Light node structure

### Inspector

### The Dome Light controls

### Controls Tab

Use the Controls tab to set the hue and brightness of the uDome light, while the Transform tab handles the source's position, direction, and scale. Color This standard Color control picks the light's color. Intensity Drag this slider to control the light's intensity, where 0.2 stands for 20% light.

### Point Light [3PL]

### The Point Light node

### Point Light Node Introduction

A point light occupies a definite spot in space and radiates light outward in every direction, much like a light bulb. It carries an onscreen control, though only that control's position and distance matter to the light. Because the source emits a full 360 degrees, its rotation is irrelevant. A point light can also dim with distance, which sets it apart from ambient or directional lights. As with a Camera 3D, lights feed into a Merge 3D and appear in the scene when you view that Merge 3D node; selecting a light node by itself and sending it to the viewer shows nothing.

### Inputs

The Point Light node provides one optional orange input for a 3D scene or 3D geometry. SceneInput: This optional orange input accepts a 3D scene, and supplying one makes the node's Transform controls apply across that entire scene.

### Basic Node Setup

The Point Light node is built to form part of a larger 3D scene. Feed the light directly into a Merge 3D, and by spreading lights over separate Merge 3D nodes you choose which objects feel each light.

### Point Light node structure

### Inspector

### Point Light controls

### Controls Tab

The Controls tab handles the hue and brightness of the point light, while its position and distance are managed over in the Transform tab. Enabled Ticking the Enabled checkbox lets the point light affect the scene, and clearing it switches the light off. This checkbox does the same thing as the red switch beside the node’s name in the Inspector. Color This standard Color control sets the light’s color. Intensity This slider governs the point light's Intensity, with 0.2 equating to light at 20% percent. Decay Type By default a point light uses No Decay, so its illumination stays equally strong everywhere in the scene. If you want the brightness to drop off over distance, switch the Decay Type to either Linear or Quadratic modes.
