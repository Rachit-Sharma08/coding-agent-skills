# Uvolume and ucylinder light and udisk light and udistant light and udome light

Version: DaVinci Resolve 20.3 Reference Manual. Context: Uvolume, Ucylinder light, Udisk light, Udistant light, Udome light.
[Chapter index](INDEX.md) / [Previous section](uvolume-controls.md) / [Next section](usd-lights-normalmap-and-shader-nodes.md) / [uVolume uVo](utransform-and-uvariant-and-uvisibility-and-uvolume.md)
<a id="source-controls-tab"></a> <a id="source-controls-tab-1"></a> <a id="source-controls-tab-2"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-inputs-2"></a> <a id="source-inspector"></a> <a id="source-inspector-1"></a> <a id="source-inspector-2"></a> <a id="source-the-usd-cylinder-light-controls"></a> <a id="source-the-usd-disk-light-controls"></a> <a id="source-the-usd-distant-light-controls"></a> <a id="source-ucylinder-light-ucl"></a> <a id="source-udisk-light-udi"></a> <a id="source-udistant-light-udl"></a> <a id="source-udome-light-udo"></a> <a id="source-usd-lights"></a>

### USD Lights

The USD light tools mark a strong expansion of Fusion's USD toolset, handing you finer control and more freedom as you build and shape the lighting across your USD scenes. Six lights ship in the USD toolset; they are:

### uCylinder Light [uCL]

The USD Cylinder light uCylinder Light Node Introduction A uCylinder light is a geometric light carrying both length and diameter, much like a fluorescent tube. It comes with an onscreen control, and translating and rotating that control positions the light within the scene.

### Inputs

A single yellow Scene Input is provided for hooking up a USD scene, after which you can tweak whatever lights already live inside it.

### Inspector

### The USD Cylinder Light controls

### Controls Tab

Color and brightness for the uCylinder light are dialed in from the Controls tab, while the Transform tab governs where the light source sits, its direction, and its scale.

Override Selection Clicking the Pick button lets you grab a light that already exists in an attached USD file, so you can adjust the lights of an imported scene. Color Reach for this standard Color control to tint the light. Intensity This slider governs the light's intensity; a setting of 0.2 stands for 20% percent light. Exposure Much like Intensity, this alters how strongly the light exposes a scene. Color Temperature/Enable This fixes a light source's color temperature, defaulting to 6500K, the temperature of daylight. Diffuse Response Governs how much the light feeds into a material's Diffuse color. Specular Response Governs how much the light feeds into a material's Specular color. Normalize This evens out the light's contribution across the scene. Treat As Line This turns the light into a plainer line light source. Length Sets how long the light is. Radius Sets the light's diameter.

### uDisk Light [uDi]

The USD Disk light uDisk Light Node Introduction This light, the uDisk, takes the form of a flat circular emitter, akin to an umbrella or softlight. You set its color and brightness from the Controls tab, whereas the Transform tab handles the light source's position, direction, and scale.

### Inputs

You get a lone Scene Input, shown in yellow, for connecting a USD scene; once attached, its existing lights become yours to modify.

### Inspector

### The USD Disk Light controls

### Controls Tab

Through the Controls tab you set the uDisk light's color and brightness, leaving the Transform tab in charge of the light source's position, direction, and scale. Override Selection Hitting the Pick button lets you select a light already present in an attached USD file, which is how you adjust the lights of an imported scene. Color This standard Color control sets the light's color. Intensity Drive the light's intensity from this slider; 0.2 corresponds to 20% percent light. Exposure Comparable to Intensity, this shifts how strongly a scene gets exposed by the light. Color Temperature / Enable This establishes a light source's color temperature, with 6500K — daylight temperature — as the default. Diffuse Response Sets how strongly the light adds to a material's Diffuse color. Specular Response Sets how strongly the light adds to a material's Specular color.

Normalize This balances out the light's contribution throughout the scene. Shaping Focus This pins down the focus point for this light's lens effect. Shaping Cone Angle Sets how broadly the light spreads. Radius Sets the light's diameter.

### uDistant Light [uDL]

The USD Distant light uDistant Light Node Introduction A uDistant light behaves like a directional light, mimicking a faraway source the way sunlight does. It carries an onscreen control whose rotation decides the direction the light points from within the scene.

### Inputs

A single Scene Input, marked yellow, attaches a USD scene and from there opens up any lights already in it for adjustment.

### Inspector

### The USD Distant Light controls

### Controls Tab

Color and brightness for the uDistant light come from the Controls tab, with the Transform tab taking care of the light source's position, direction, and scale. Override Selection Press the Pick button to pull in a light that already exists within an attached USD file, the route for adjusting an imported scene's lights. Color Use this standard Color control to choose the light's color. Intensity This slider drives the light's intensity, where 0.2 equals 20% percent light. Exposure Akin to Intensity, this changes the degree to which the light exposes a scene. Color Temperature/Enable This sets a light source's color temperature; the default, 6500K, matches daylight temperature. Diffuse Response Dictates how much the light adds toward a material's Diffuse color. Specular Response Dictates how much the light adds toward a material's Specular color. Normalize This levels the light's contribution within the scene. Angular Size Sets how broadly the light spreads.

### uDome Light [uDo]

The USD Dome light uDome Light Node Introduction A uDome light draws on SDR and HDR images, wrapping the whole scene inside a sphere light that's mapped with the image, in the manner of an environment light. Its onscreen control has a rotation that sets which direction the light points from across the scene.
