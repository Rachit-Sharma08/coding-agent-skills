# Point light and spot light

Version: DaVinci Resolve 20.3 Reference Manual. Context: Point light, Spot light.
[Chapter index](INDEX.md) / [Previous section](directional-light-and-domelight-and-point-light.md) / [Next section](spot-light-common-controls.md) / [Continue Spot Light 3SL / Common Controls](spot-light-common-controls.md) / [Point Light 3PL](directional-light-and-domelight-and-point-light.md)
<a id="source-basic-node-setup-4"></a> <a id="source-common-controls-2"></a> <a id="source-controls-tab-4"></a> <a id="source-inputs-4"></a> <a id="source-inspector-4"></a> <a id="source-shadows-1"></a> <a id="source-shadows-2"></a> <a id="source-spot-light-3sl"></a> <a id="source-spot-light-control"></a> <a id="source-spot-light-node-introduction"></a> <a id="source-spot-light-node-structure"></a> <a id="source-the-spot-light-node"></a>

### Shadows

The controls here let you spell out the shadow map this light relies on when it produces shadows. For additional detail, look to “3D Compositing Basics” — Chapter 85 of the DaVinci Reference Manual — or else Chapter 23 found in the Fusion Reference Manual.

NOTE: For the Point light's shadows to register in the 3D viewer, set the Rendering Type on the Renderer3D node to Hardware Renderer. Enable Shadows Select the Enable Shadows checkbox whenever the light should cast shadows; it is enabled by default. Shadow Color This standard Color control chooses the shadow's color and defaults to black (0, 0, 0). Density A shadow's density decides how see-through it is: at 1.0 the shadow is fully opaque, and lower settings make it more transparent. Shadow Map Size The Shadow Map Size control sets how large the bitmap underlying the shadow map is, with larger values delivering richer shadow maps at a cost to memory and performance. Shadow Map Proxy Shadow Map Proxy sets the shadow map size used whenever the Proxy or Auto Proxy modes are turned on. Picking 0.5 here, for example, builds a shadow map at half whatever resolution the Shadow Map Size holds. Multiplicative/Additive Bias Since shadows amount to textures placed onto scene objects, Z-fighting sometimes appears, in which the object regions that should receive the shadow draw over the top of it instead. Adding a small depth offset through bias shifts the shadow off the surface it falls on and removes that Z-fighting. With too little bias the objects shadow themselves, and with too much the shadow separates from the surface. Tune the Multiplicative Bias first, then refine the outcome with the Additive Bias control. You will find more on this in the Multiplicative and Additive Bias portion of “3D Compositing Basics,” namely Chapter 85 of the DaVinci Resolve Reference Manual, or Chapter 25 inside the Fusion Reference Manual. Force All Materials Non-Transmissive An RGBAZ shadow map is the default for rendering shadows; enabling this option compels the renderer to fall back on a Z-only shadow map. That can render shadows markedly faster while drawing only a fifth of the memory, though the trade-off is that you lose “stained glass”-type colored shadows. Shadow Map Sampling Governs how finely the shadow map is sampled.

Softness Filtering the shadow map during sampling is what yields soft shadow edges, and Fusion supplies two distinct filtering methods for rendering shadows, each producing a different look. NOTE: With a hard-edged shadow, the shadow map receives no filtering whatsoever. The benefit is that only one pixel of the shadow map has to be sampled, which keeps it fast.

- Constant: Shadow edges hold a steady softness. A constant-width filter samples the shadow map, and the Constant Softness slider sizes that filter; keep in mind that a bigger filter draws out the shadow render time.
- Variable: Shadow-edge softness increases as the receiver moves farther from the caster. That variable softness comes from scaling the filter by the receiver-to-caster distance, and picking it brings up the Softness Falloff, Min Softness, and Max Softness sliders.

Constant Softness This slider surfaces when Softness is set to Constant and lets you dial in the shadow's overall softness. Softness Falloff Shown when Softness is set to variable, this slider drives how rapidly edge softness rises with distance — more precisely, how fast the shadow map filter grows based on the caster-to-receiver separation, with the Min and Max Softness values reining it in. Min Softness Appearing when Softness is Variable, this slider sets the shadow's Minimum Softness: the closer the shadow lies to the casting object, the sharper it remains, down to this slider's limit. Max Softness Likewise shown when Softness is Variable, this slider sets the shadow's Maximum Softness: the farther the shadow sits from the casting object, the softer it turns, up to this slider's limit.

### Common Controls

Transform and Settings Tabs The settings on the Transform and Settings tabs are ones you will meet on the rest of the lighting nodes. For more detail on what these tabs offer, see the “The Common Controls” section at the end of this chapter.

### Spot Light [3SL]

### The Spot Light node

### Spot Light Node Introduction

A spotlight originates from one fixed point and projects a sharply outlined cone whose light tapers off toward the edges. Stage and theatre lighting veterans will spot its resemblance to the practical fixtures used on live shoots. It is the sole light type that can throw shadows. As with a Camera 3D, you route lights into a Merge 3D and see them in the scene by viewing that Merge 3D node; picking a light node on its own and loading it into the viewer displays nothing.

### Inputs

The Spot Light node has a lone optional orange input for a 3D scene or 3D geometry. SceneInput: This optional orange input takes a 3D scene, and when one is connected the node's Transform controls operate on that whole scene.

### Basic Node Setup

The Spot Light node is intended to be one element of a larger 3D scene. Wire the light directly into a Merge 3D, and keeping lights on separate Merge 3D nodes lets you decide which objects each light reaches.

### Spot Light node structure

### Inspector

### Spot Light control

### Controls Tab

The Controls tab handles the hue and brightness of the spotlight, while its position, rotation, and distance live on the Transform tab. Enabled With the Enabled checkbox ticked the spotlight acts on the scene, and clearing it turns the light off. This checkbox matches the red switch sitting to the left of the node’s name in the Inspector. Color This standard Color control sets the light’s color. Intensity This slider governs the spot light's Intensity, where 0.2 amounts to light at 20% percent. Decay Type Out of the box a spotlight uses No Falloff, so its illumination hits geometry at the same strength no matter the distance from light to surface. To make the brightness taper with distance, change the Decay type to either Linear or Quadratic modes. Cone Angle The light's Cone Angle is the width of the cone within which the light shines at full strength. A bigger value widens that cone, up to a ceiling of 90 degrees.

Penumbra Angle The Penumbra Angle marks the zone past the cone angle where the light’s strength tapers toward 0. A larger penumbra angle creates a broader falloff, whereas 0 yields a hard-edged light. Dropoff The Dropoff governs how fast the penumbra angle drops from full intensity down to 0.

### Shadows

The controls in this area let you pin down the shadow map this spotlight draws on when generating shadows. For additional reading, the “3D Compositing Basics” material sits at Chapter 85 of the DaVinci Resolve Reference Manual, or at Chapter 25 in the Fusion Reference Manual.

NOTE: For the Spotlight, either the Hardware or Software Renderer may be chosen as the Rendering Type in the Renderer3D node, and only then do shadows appear in the 3D viewer. Enable Shadows Tick the Enable Shadows checkbox when the light should create shadows; it starts out selected. Shadow Color This standard Color control sets the shadow's hue and defaults to black (0, 0, 0). Density The density of a shadow controls how transparent it is: 1.0 makes a fully solid shadow, and lower figures let more light through. Shadow Map Size The Shadow Map Size control decides how big the bitmap that builds the shadow map is, where higher values give sharper shadow maps but tax memory and performance. Shadow Map Proxy Shadow Map Proxy fixes the shadow map size in play once the Proxy or Auto Proxy modes are switched on. Choose 0.5, say, and you get a shadow map at half whatever resolution the Shadow Map Size carries. Multiplicative/Additive Bias Shadows are in effect textures draped over scene objects, so Z-fighting occasionally surfaces, with the object areas meant to take the shadow rendering on top of it instead. Bias resolves this by introducing a slight depth offset that pushes the shadow away from the surface it shadows, ending the Z-fighting. Too little bias lets objects shadow themselves; too much pulls the shadow off the surface. Dial in the Multiplicative Bias first, then refine using the Additive Bias control.

More on this appears in the Multiplicative and Additive Bias portion of “3D Compositing Basics,” which is Chapter 85 of the DaVinci Resolve Reference Manual, or Chapter 25 over in the Fusion Reference Manual. Force All Materials Non-Transmissive An RGBAZ shadow map is normally what renders the shadows; turn this option on and you force the renderer onto a Z-only shadow map. That option can speed shadow rendering up sharply while using just a fifth of the memory, but you give up the ability to cast “stained glass”-like shadows. Shadow Map Sampling Determines how finely the shadow map gets sampled. Softness Soft shadow edges come from filtering the shadow map as it is sampled, and Fusion gives you two separate filtering methods for rendering shadows, each with its own effect. NOTE: A hard-edged shadow involves no filtering of the shadow map at all. Its advantage is that just one pixel of the shadow map needs sampling, so it stays fast.

- Constant: Shadow edges keep a single, even softness. A fixed-width filter samples the shadow map, with the Constant Softness slider setting that filter's size; remember that enlarging the filter stretches out the shadow render time.
- Variable: Shadow-edge softness builds the further the receiver lies from the caster. This variable softness is produced by adjusting the filter size according to the receiver-caster distance, and selecting it makes the Softness Falloff, Min Softness, and Max Softness sliders appear.

Constant Softness This slider appears when Softness is set to Constant, and you use it to set the shadow's overall softness. Softness Falloff Present when Softness is set to variable, this slider controls how quickly edge softness builds with distance — specifically, how fast the shadow map filter expands based on the caster-to-receiver distance, kept in check by the Min and Max Softness values. Min Softness Shown when Softness is Variable, this slider sets the shadow's Minimum Softness: the nearer the shadow sits to its casting object, the crisper it is, down to this slider's limit. Max Softness Likewise shown when Softness is Variable, this slider sets the shadow's Maximum Softness: the further the shadow sits from its casting object, the softer it becomes, up to this slider's limit.
