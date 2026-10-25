# Attenuation and alpha detail

Version: DaVinci Resolve 20.3 Reference Manual. Context: 3D compositing basics.
[Chapter index](INDEX.md) / [Previous section](lighting-hierarchies-and-shadow-maps.md) / [Next section](refraction-and-bump-maps.md)
<a id="source-alpha-detail"></a> <a id="source-attenuation"></a> <a id="source-blinn"></a> <a id="source-cook-torrance"></a> <a id="source-illumination-models"></a> <a id="source-phong"></a> <a id="source-reflection"></a> <a id="source-reflections-and-refractions"></a> <a id="source-sphere-map-example"></a> <a id="source-textures"></a> <a id="source-ward"></a>

### Attenuation

How much color travels through the object is set by the transmittance color. For an object to throw fully transmissive shadows, the transmittance color has to be set to RGB = (1, 1, 1), meaning 100% of the green, blue, and red light passes through the object. Set this color to RGB = (1, 0, 0) and the material then passes 100% of the red landing on the surface but none of the green or blue light.

### Alpha Detail

With the Alpha Detail slider at 0, the non-zero regions of the diffuse color’s alpha channel get disregarded and the object’s opaque regions throw a shadow. Set it to 1 and the alpha channel then sets how dense a shadow the object throws. NOTE: The OpenGL renderer disregards alpha channels while rendering shadows, so a shadow always ends up thrown from the whole object. Alpha in the shadow maps is backed by the software renderer alone. The examples below for Alpha Detail and Color Detail throw a shadow built from this image. It runs as a green-red gradient from left to right. Its outer edges are transparent, and inside sits a small semi‑transparent circle.

Alpha Detail set to 1; shadow density is driven by the alpha channel

Alpha Detail set to 0; the upshot is a dense-colored shadow Color Detail Color Detail serves to tint the shadow with the object’s diffuse color. With the Color Detail slider lifted from 0 toward 1, additional diffuse color plus texture enters the shadow. TIP: The OpenGL renderer will forever throw a black shadow from the whole object, paying no heed to the color. Color in the shadow maps is backed by the software renderer alone.

Color Detail set to 0; no color is visible in the shadow.

Saturation Saturation lets the diffuse color texture set the shadow’s density without touching the color. This slider lets you mix between the full color and luminance only. Transmittance and Shadows A material’s transmittance plays a major part in setting how the shadow it throws looks. As a rule, that transmittance behavior gets defined within each object’s Materials tab as covered above. Ticking Force All Materials Non-Transmissive in the Spotlight Inspector overrides this, though, making the shadow map the spotlight produces disregard transmittance altogether.

### Illumination Models

With the various components that build up a material or shader now clear to you, we’ll examine them in more detail. Illumination models are sophisticated materials for crafting lifelike surfaces such as plastic, wood, or metal. Every illumination model carries upsides and downsides that suit it to particular looks. Since an illumination model sets how a surface answers light, these nodes need at least one light source for the object’s look to change. The Nodes > 3D > Material menu holds four different illumination models. Illumination models, in left-to-right order: Standard, Blinn, Phong, Cook-Torrance, and Ward Standard What the Standard material gives is a default Blinn material with basic command over the diffuse, specular, and transmittance components. For the diffuse component it accepts only a single texture map, with the alpha serving as opacity. The Standard Material controls sit within the Material tab on every node that loads or builds geometry. Wire any node that puts out a material into that node’s Material Input and the Standard material gets overridden, with the controls in the Material tab going hidden.

### Blinn

The Blinn material is an all-purpose material pliable enough to stand in for both metallic and dielectric surfaces. While it draws on the same illumination model as the Standard material, the Blinn material opens up a finer degree of command by offering extra texture inputs for the specular color, intensity, and exponent (falloff), plus bump map textures.

### Phong

The Phong material gives the same diffuse outcome as Blinn but with broader specular highlights at grazing incidence. Phong can equally make sharper specular highlights at high exponent levels.

### Cook-Torrance

The Cook-Torrance material fuses the Blinn material’s diffuse illumination model with a joint microfacet and Fresnel specular model. Those microfacets need not exist within the mesh or bump map; a statistical function, Roughness, stands in for them, and it can be mapped. According to the Refractive Index, which can be mapped, the Fresnel factor dampens the specular highlight.

### Ward

The Ward material carries the same diffuse model as the rest but layers on anisotropic highlights, perfect for mimicking brushed metal or woven surfaces, since the highlight can be stretched along the mapping coordinates’ U or V directions. Each of the U and V spread functions is mappable. This material does call for properly structured UV coordinates on whatever meshes it lands on.

### Textures

Texture maps reshape how a material looks on a per-pixel basis. That happens by wiring an image or another material into the inputs on the Material nodes within the Node Editor. Where a 2D image gets used, the geometry’s UV mapping coordinates serve to fit the image onto the geometry, and as each pixel of the 3D scene gets rendered, the material reshapes the material input per the value of the matching pixel in the map. TIP: UV Mapping is the technique used to wrap a 2D image texture onto 3D geometry. Much like X and Y coordinates within a frame, U and V are the coordinates for textures across 3D objects.

A range of material inputs gets reshaped by texture maps, among them diffuse color, specular color, specular exponent, specular intensity, bump map, and others. Where texture maps see the most use is the diffuse color/opacity component.

The Fast Noise texture put to work driving the roughness on a Cook-Torrance material

A node that puts out a material gets reached for often, in place of an image, to offer other shading options. The materials handed between nodes are RGBA samples; they hold no further information about the shading or textures that gave rise to them.

The Texture2D node serves to shift a texture within the object’s UV space, as well as set the filtering and wrap mode Composite Materials Building intricate materials comes down to wiring the output of one Material node into one of the Material inputs on another Material or Texture node. Where a Material input gets supplied, just as with a 2D image, its RGBA values serve per pixel as a texture. That allows for very direct compositing of shaders. As an instance, to pair an anisotropic highlight with a Blinn material, you can take the Blinn’s output, specular included, and use it as the diffuse color of the Ward material. Or, should you not want the Blinn’s output relit by the Ward material, you can reach for the Channel Boolean material so the Ward material’s anisotropic specular component gets laid onto the Blinn material with a finer degree of command.

Pairing an anisotropic highlight together with a Blinn material by way of the Channel Boolean material

### Reflections and Refractions

Environment maps can be laid on with the Reflect material under the 3D > Material category. This node can serve to mimic reflections and refractions across an object. Reflections are direct-bounce light striking an object, whereas refractions mimic how light distorts when seen through semi-translucent surfaces. The reflections and refractions lean on an environment mapping technique to yield an approximation that balances lifelike results against greater rendering performance. Environment maps treat whatever surrounds an object as infinitely far away and rendered down into a cubic or spherical texture enclosing it. To help build environment maps, you have the Nodes > 3D > Texture > Cube Map and Sphere Map nodes, which lay special processing and transforms on to mint the cubic or spherical coordinates required.

### Sphere map example

To yield reflections with real-time interactive feedback at a quality fit for production environment maps, you accept some trade-offs in functionality versus the slower but physically accurate raytraced rendering. Environment-mapped reflections and refractions offer no self-reflection nor any other sort of interaction across separate objects. This infinite distance assumption, in particular, means objects cannot interact with themselves (for instance, the reflections on a teapot’s handle will not show the teapot’s body). It equally means objects sharing the same cube map will not inter-reflect with one another. As an example, two adjacent objects would not reflect each other. A separate cube map has to be rendered per object. The Reflect node puts out a material that can land on an object directly, yet the material holds no illumination model. Consequently, objects textured straight by the Reflect node will not answer the scene’s lights. That is why the Reflect node usually gets paired with the Blinn, Cook-Torrance, Phong, or Ward nodes.

### Reflection

Reflection puts out a material that makes it possible to lay the reflection or refraction onto other materials either ahead of or after the lighting model for differing effects.

A Blinn material wired into a background material input on the Reflect; the result is the reflection getting added onto the Blinn output

Here a Reflect feeds the Diffuse Color component on the Blinn, so the reflection ends up multiplied against the diffuse color and shaped by the lighting
