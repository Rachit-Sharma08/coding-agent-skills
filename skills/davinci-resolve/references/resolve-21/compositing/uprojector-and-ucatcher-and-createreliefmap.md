# Uprojector and ucatcher and createreliefmap

Version: DaVinci Resolve 21 New Features Guide. Context: Uprojector, Ucatcher, Createreliefmap.
[Chapter index](INDEX.md) / [Previous section](uprojector-controls.md) / [Next section](createreliefmap-and-reliefmap.md) / [uProjector uPj](uprojector-controls.md)
<a id="source-3d-renderer-now-supports-creating-and-using-cryptomatte"></a> <a id="source-basic-node-setup"></a> <a id="source-common-controls"></a> <a id="source-common-controls-1"></a> <a id="source-createreliefmap-crm"></a> <a id="source-createreliefmap-node-introduction"></a> <a id="source-fusion-global-in-out-controls-for-usd-loader"></a> <a id="source-inputs"></a> <a id="source-projection-mode"></a> <a id="source-relief-map-tools"></a> <a id="source-the-createreliefmap-node"></a> <a id="source-ucatcher-uca"></a>

### Projection Mode

- Light: Casts the texture in the manner of a diffuse/specular light.
- Texture: Paired with the uCatcher node, this option enables texture projections you can re-light. Only surfaces whose material shaders include the catcher material are hit by the projection. A handy approach is wiring a uCatcher node into the Specular Texture input of a USD Material node (a Blinn, for instance). Then every object carrying that Blinn material picks up the projection within its specular highlight. You can apply this same idea to any material input that accepts texture maps, including the Specular and Reflection maps.

Shadows Because the projector derives from a spotlight, it can likewise cast shadows by means of shadow maps. The settings within this reveal govern the dimensions and characteristics of that shadow map.

- Enable Shadows: Turn on the Enable Shadows checkbox when the light should generate shadows. Its default state is selected.
- Shadow Color: This ordinary Color control sets the shadow's color. It defaults to black (0, 0, 0).
- Density: The Shadow Density governs how transparent the shadow appears. At a density of 1.0 the shadow becomes fully transparent, while smaller numbers reduce its opacity.
- Softness: Governs how soft the shadow's edges are.
- Softness Quality: Governs the quality level of that softness.
- Shadow Map Size: The Shadow Map Size control sets the dimensions of the bitmap used to build

the shadow map. Bigger numbers yield finer shadow maps but cost additional memory and performance.

- Shadow Map Bias: When shadows fail to appear, this control can be tuned so the shadow map shows up in the scene.
- Shadow Map Offset: Shifts the value of the Shadow Map Size.

### Common Controls

Transform and Settings Tabs The Transform and Settings tabs that remain are shared by many USD nodes. You will find their descriptions in the “The Common Controls” section that closes this chapter.

### uCatcher [uCa]

The uCatcher node uCatcher Node Overview The job of the uCatcher material is to “catch” texture-mode projections thrown by uProjector and uCamera nodes. Those captured projections become a texture map, which the uCatcher material then lays onto whatever geometry it is wired to. Grasping the uCatcher node is easier once you see how light-based and texture-based projections differ. Picking Light in the projection mode menu of a uProjector or uCamera node merely adds the RGB channel values from the projected picture onto the diffuse texture of whatever geometry falls inside the projection cone. That makes it impossible to trim away geometry using an image's Alpha channel under light mode projections. Picture a case where you want to throw an image of a building onto an image plane for a set extension shot. You begin by rotoscoping the picture to cut out the windows. Doing so lets you reveal the geometry of the rooms behind the wall in the finished composite. Once that image is cast as light, its Alpha channel goes unused, leaving the masked windows opaque. If instead you wire the uCatcher into the diffuse texture map of the material on the image plane, and then flip the projection mode menu on the uProjector or uCamera node from Light to Texture mode, the image gets laid down as a texture map. Following this method for the example above, the windows turn transparent and the geometry behind them becomes visible. The chief benefits of this route over light projection are that the uCatcher can throw Alpha onto an object and needs no lighting turned on. Another plus is that the uCatcher is not confined to a material's diffuse input, letting you cast specular intensity maps, or even maps for reflection and refraction. NOTE: The uCatcher material needs a uProjector or uCamera node present in the scene, configured to cast an image in Texture mode onto the object the uCatcher is wired to. With no projection present, or a projection not set to Texture mode, the uCatcher merely renders the object transparent and invisible.

### Inputs

USD geometry feeds the yellow Scene input — for instance a uShape, or a USD asset routed in via a uLoader.

### Basic Node Setup

What feeds the uCatcher node is the geometry of the USD asset meant to receive the projected texture. From there the uCatcher node sends its output to a uMerge where additional assets, lights, or cameras may be composited.

A uCatcher node draws its input from the geometry node (uShape1) that receives the texture projection, and then feeds a uMerge node. Inspector

uCatcher controls Controls Tab The Options under the Controls tab decide how the uCatcher manages stacking up several projections. Color Mode The Color mode menu governs the way the uCatcher blends light coming from multiple projectors. With a single projector present, it changes nothing. Alpha Mode The Alpha mode governs the way the uCatcher blends the Alpha channels coming from multiple projectors. With a single projector present, it changes nothing.

Threshold The Threshold lets you keep certain low values out of the accumulation math. As an example, in Median Accumulation mode a threshold of 0.01 would leave out any pixel whose value is under 0.01 from the median computation. Restrict by Projector ID Once enabled, the uCatcher takes in light solely from projectors whose ID matches. Projectors carrying a different ID get skipped.

### Common Controls

Transform and Settings Tabs The Transform and Settings tab in the Inspector also appears again across other USD nodes. You will find these common controls explained fully at the close of this chapter under “The Common Controls” section.

### Fusion Global in-out controls for USD Loader

Bringing a USD file into stand alone Fusion now offers a way to define a global in-out range.

### 3D Renderer now Supports Creating and Using Cryptomatte

When working with the Renderer3D’s hardware renderer, Cryptomatte layers and metadata can now be produced for objects as well as materials. This added capability lets you build several soft mattes targeting particular 3D objects or materials drawn from a rendered scene. Fusion’s Cryptomatte tool can read the new layers, natively pulling in the embedded mattes and making it easier to isolate rendered pieces for compositing. You can also store them in an OpenEXR file to use later.

### Relief Map Tools

The Relief Map tools are new to Fusion and can boost the realism of a 3D object. What sets Relief mapping apart from ordinary bump maps is that it can produce self-occlusion. This pair of additions, CreateReliefMap and ReliefMap, exist to assist in building detailed surface textures. CreateReliefMap is a fresh filter tool that produces the image the ReliefMap node requires. That generated depth map drives the creation of simulated texture and lighting effects. CreateReliefMap offers controls for depth scale and smoothing so you can dial how pronounced or gentle the relief looks. ReliefMap is a fresh 3D tool that adds height-driven surface detail onto 3D shapes. Working from an image, the ReliefMap carves away parts of a 3D shape, in effect building depth information for the surface. This sculpting approach modifies a material’s normal/displacement mapping directly, allowing rich textures to emerge without hand-modeling every detail. Detailed coverage of both tools follows below.

### CreateReliefMap [CRM]

### The CreateReliefMap node

### CreateReliefMap Node Introduction

Create Relief Map is a partner tool that produces the image the ReliefMap node needs. It builds a relief map by taking a height field and computing values that reshape the object’s surface normals. Once fed into a Relief Map, it yields simulated texture and lighting effects. CreateReliefMap offers controls for depth scale and smoothing so you can dial how pronounced or gentle the relief appears.
