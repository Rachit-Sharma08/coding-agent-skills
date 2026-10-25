# Projector 3D controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Projector 3D.
[Chapter index](INDEX.md) / [Previous section](point-cloud-3d-and-projector-3d.md) / [Projector 3D 3Pj](point-cloud-3d-and-projector-3d.md) / [Next section](projector-3d-and-renderer3d.md)
<a id="source-3d-nodes-part-5"></a> <a id="source-projection-mode"></a>

### Projection Mode

- Light: Casts the texture as a diffuse/specular light.
- Ambient Light: Draws on an ambient light to drive the projection.
- Texture: Paired with the Catcher node, this mode enables re-lightable texture projections. The projection lands solely on objects that include the catcher material among their material shaders. A handy trick is to wire a Catcher node into the Specular Texture input on a 3D Material node (a Blinn, for example), which makes every object using the Blinn material take the projection as part of its specular highlight. You can apply this approach at any material input that accepts texture maps, including the Specular and Reflection maps.

Shadows Because the projector builds on a spotlight, it can likewise cast shadows by means of shadow maps. The controls revealed here set the shadow map's size and behavior.

- Enable Shadows: Tick the Enable Shadows checkbox when you want a light to cast shadows. Its default state is selected.
- Shadow Color: This ordinary Color control lets you choose the shadow’s color. Its default is black (0, 0, 0).
- Density: How see-through a shadow is comes down to the Shadow Density. At a density of 1.0 the shadow becomes fully transparent, while smaller figures render the shadow transparent.
- Shadow Map Size: The dimensions of the bitmap behind the shadow map are governed by the Shadow Map Size control. Bigger figures yield finer shadow maps, though they cost more memory and performance.
- Shadow Map Proxy: For proxy and auto proxy calculations, the Shadow Map Proxy sets how large the shadow map is. Setting it to 0.5, for instance, applies a 50% shadow map.
- Multiplicative/Additive Bias: Because shadows amount to textures laid over the scene’s objects, Z-fighting crops up now and then, in which the parts of an object meant to catch the shadows draw on top of the shadow rather than beneath it.
- Multiplicative and Additive Bias: Bias operates by introducing a slight depth offset that nudges the shadow off the surface it falls on, doing away with the Z-fighting. With too little bias, objects may cast shadows onto themselves. With too much, the shadow may detach from its surface. Tune the multiplicative bias first, then refine the outcome through the additive bias control.
- Force All Materials Non-Transmissive: As a rule, shadow rendering relies on an RGBAZ shadow map. Switching this option on compels the renderer to adopt a Z-only shadow map instead. The payoff can be markedly quicker shadow rendering at roughly a fifth of the memory. The trade-off is losing the ability to throw “stained-glass”-style shadows.
- Shadow Map Sampling: Determines the sampling quality applied to the shadow map.
- Softness: Filtering the shadow map during sampling is what gives shadows their soft edges. Fusion offers three distinct filtering approaches, each yielding a different look when shadows render. None: Shadows keep a hard edge. The shadow map gets no filtering whatsoever. Its upside is that just a single pixel of the shadow map needs sampling, which makes it quick.

Constant: Every shadow edge carries the same softness. Sampling the shadow map employs a filter of fixed width. The filter’s size is governed by the Constant Softness slider. Keep in mind that a wider filter lengthens how long the shadows take to render. Setting the Softness to constant brings up a Constant slider. You use it to dial in the shadow’s overall softness. Variable: Shadow edges turn softer the greater the gap between the shadow receiver and the shadow caster. This variable softness comes from resizing the filter according to the receiver-to-caster distance. Choosing this option reveals the Softness Falloff, Min Softness and Max Softness sliders. Softness Falloff: The Softness Falloff slider shows up once Softness is set to variable. It governs how quickly shadow-edge softness builds as distance increases. Put more exactly, it sets how rapidly the shadow map filter size expands relative to the caster-to-receiver distance. The Min and Max Softness slider values temper its impact. Min Softness: The Min Softness slider surfaces when Softness is variable. It dictates the shadow’s Minimum Softness. The nearer the shadow lies to the object that casts it, the crisper it stays, bounded by the limit this slider sets. Max Softness: The Max Softness slider surfaces when Softness is variable. It dictates the shadow’s Maximum Softness. The farther the shadow sits from the object that casts it, the softer it grows, bounded by the limit this slider sets.
