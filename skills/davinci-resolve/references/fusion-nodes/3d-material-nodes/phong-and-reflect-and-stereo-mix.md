# Phong and reflect and stereo mix

Version: DaVinci Resolve 20.3 Reference Manual. Context: Phong, Reflect, Stereo mix.
[Chapter index](INDEX.md) / [Previous section](material-merge-3d-and-phong.md) / [Next section](ward-controls.md) / [Phong 3Ph](material-merge-3d-and-phong.md)
<a id="source-basic-node-setup-2"></a> <a id="source-basic-node-setup-3"></a> <a id="source-common-controls-1"></a> <a id="source-common-controls-2"></a> <a id="source-common-controls-3"></a> <a id="source-controls-tab-2"></a> <a id="source-controls-tab-3"></a> <a id="source-inputs-2"></a> <a id="source-inputs-3"></a> <a id="source-reflect-3rr"></a> <a id="source-reflect-controls"></a> <a id="source-reflect-node-introduction"></a> <a id="source-reflection"></a> <a id="source-refraction"></a> <a id="source-stereo-mix-3smm"></a> <a id="source-stereo-mix-controls"></a> <a id="source-stereo-mix-node-overview"></a> <a id="source-the-reflect-node"></a> <a id="source-the-stereo-mix-node"></a> <a id="source-transmittance"></a>

### Transmittance

Transmittance dictates how light travels through a material. Take a solid blue sphere, which throws a black shadow; the same form in translucent blue plastic would throw a far thinner blue shadow instead. A distinct Opacity option exists too. Opacity decides how transparent the actual surface appears once rendered. Fusion lets opacity and transmittance be tuned independently. For anyone new to 3D software this can feel odd at first. You can indeed build a surface that stays fully opaque yet passes 100% of the light striking it, in effect a luminous or emissive surface. Attenuation Attenuation fixes how much color travels through the object. To give an object transmissive shadows, set the attenuation to (1, 1, 1), so that 100% of green, blue, and red light passes through it. Dialing this color to RGB (1, 0, 0) lets the material transmit 100% of incoming red while blocking all green and blue, handy for “stained glass”-styled shadows. Alpha Detail With the Alpha Detail slider at 0, the object’s Alpha channel is disregarded and the whole object throws a shadow. At 1, the Alpha channel decides which parts of the object cast a shadow. Color Detail The Color Detail slider tints light crossing the surface by the diffuse color plus texture colors. Reach for it to cast a shadow holding the color detail of the texture on the object. Raising the slider from 0 to 1 feeds progressively more diffuse and texture color into the shadow. Keep in mind that the object’s Alpha and opacity are bypassed while color is transmitted, so an object with a solid Alpha can still pass its color into the shadow.

Saturation The Saturation slider sets how saturated the color portion handed to the shadow is. Drop it to 0.0 and the shadows turn monochrome. Receives Lighting/Shadows These checkboxes decide whether scene lighting and shadows touch the material at all. Switch them off and the object stays fully lit and unshadowed throughout. Two-Sided Lighting This in practice renders the surface two sided by appending a second batch of normals that point the other way on its backside. It usually sits off to speed up rendering, yet you can enable it for 2D surfaces or for objects that aren’t fully sealed, making their reverse or inner faces visible too. By convention a 3D application shows only a surface’s front face and culls the back, so a camera orbiting a plane would see it vanish on reaching the rear. Turning a plane two sided in a 3D application amounts to stacking a duplicate plane on the first, spun 180 degrees so its normals point the other way at the back. Hence, orbiting to the rear reveals that second image plane, whose normals face opposite. When you make a surface two sided, Fusion behaves precisely as those 3D applications do. The muddle over two-sided lighting stems from Fusion not culling back-facing polygons out of the box. Orbit a one-sided plane in Fusion and the backside still shows (though what you see is the frontside carried through to the back as if transparent). Rendering the plane two sided in effect tacks a second set of normals onto its backside. NOTE: Once the surface goes transparent this gets genuinely confusing, because the same rules hold and the outcome runs against intuition. Viewing a transparent two-sided surface from the front while it’s lit from behind makes it look unlit. Material ID Use this slider to set the numeric identifier given to this material. When the matching option is active in the renderer, that value writes into the MatID auxiliary channel.

### Common Controls

Settings Tab The Inspector’s Settings tab is mirrored across the other 3D nodes. Its shared controls receive their detailed coverage at the chapter’s end inside “The Common Controls.”

### Reflect [3RR]

### The Reflect node

### Reflect Node Introduction

Environment map reflections and refractions are layered onto materials by the Reflect node. You get a say over face on and glancing strength, falloff, per channel refraction indexes, and tinting, with several texture map inputs available to reshape how each parameter behaves. Environment mapping is itself an approximation, treating an object’s surroundings as though they sit infinitely far away. Picture a cube or sphere wrapped around the object at its center. Because of that infinite-distance premise, objects can’t reflect themselves — the reflections on a teapot’s handle show the surrounding environment map rather than the teapot’s own body. By the same token, applying one cube map to several scene objects leaves them unable to mirror one another, so two adjacent objects won’t reflect each other. Getting objects to reflect one another calls for rendering a separate cube map per object. Fuller coverage sits in Chapter 85, “3D Compositing Basics,” of the DaVinci Resolve Reference Manual, as well as Chapter 25 of the Fusion Reference Manual.

### Inputs

Five inputs sit on the Reflect node, each one taking a 2D image or a 3D material. They drive the overall color and imagery of the 3D object together with the color and texture feeding the reflective highlights. Background Material: The orange Background material input takes a 2D image or a 3D material; a 2D image gets read as a diffuse texture map over a basic material. Reflection Color Material: The white Reflection Color material input takes a 2D image or a 3D material, whose RGB channels serve as the reflection texture while the Alpha goes unused. Reflection Intensity Material: The white Reflection Intensity material input takes a 2D image or a 3D material, and that texture’s Alpha channel scales the reflection’s intensity. Refraction Tint Material: The white Refraction Tint material input takes a 2D image or a 3D material; its RGB channels supply the refraction texture. Bump Map Texture: The white Bump Map texture input takes only a 3D material. As a rule, you wire the texture into a Bump Map node and then route that Bump Map node here. The RGB data at this input acts as texture-space normals. Once a node sports this many inputs — several sharing a color — landing connections precisely gets awkward. As you drag another node’s output across the node tile, hold the Option or Alt key down and keep it held while releasing the left mouse button. A compact drop-down then lists every input the node provides. Click the one you need to seal the connection.

### Basic Node Setup

As shown in the example beneath, the Reflection node can act as an object’s primary shader, or it can supply the diffuse material input of a Ward, Blinn, Phong, or some other material node. The Reflect node’s reflection color input is typically fed from a Sphere Map node.

A Reflect node producing a strongly mirror-like surface on a Shape 3D node Inspector

### Reflect controls

### Controls Tab

Parameters on the Controls tab let you tune reflective strength according to the object’s orientation, plus the tint color of the Reflect shader node.

### Reflection

Reflection Strength Variability This multi-button control toggles between Constant and By Angle, varying reflection intensity in line with how the surface is oriented relative to the viewer. The three controls below it surface only while this is set to By Angle. Glancing Strength [By Angle] Glancing Strength sets reflection intensity across the geometry where the reflection turns away from the camera. Face On Strength [By Angle] Face On Strength sets reflection intensity over the geometry that reflects straight back at the camera. Falloff [By Angle] Falloff governs how sharp the handoff is between the Glancing and Face On Strength zones — akin to gamma-correcting a gradient stretched between the Face On and Glancing values. Constant Strength [Constant Angle] This one appears only while reflection strength variability is set to Constant, where reflection intensity holds steady no matter the reflection’s incidence angle.

### Refraction

Whenever the incoming background material drops below an opacity of 1, an environment map can serve as the refraction texture, letting you fake refraction inside transparent objects. Separate RGB Refraction Indices Ticking this checkbox tucks away the Refraction Index slider and swaps in three sliders that tune the refraction index for the Red, Green, and Blue channels individually. That opens the door to mimicking the spectral refraction often visible in thick, flawed glass. Refraction Index This slider dictates how heavily the environment map warps when seen through a surface, with the overall warp keyed to the incidence angle. Being an approximation rather than a true simulation, its output isn’t built to model real refractions exactly. Refraction Tint Multiplying the refraction texture by the tint color simulates color-filtered refractions — useful for the kind of coloring found in tinted glass, like that of many beer bottles.

### Common Controls

Settings Tab Inside the Inspector this Settings tab turns up on the other 3D nodes as well. Full detail on its shared controls lives at the chapter’s close under “The Common Controls.”

### Stereo Mix [3SMM]

### The Stereo Mix node

### Stereo Mix Node Overview

Swapping the left and right material inputs is this node’s job. It frequently feeds the left and right eye of the 3D Render.

### Inputs

Two inputs sit on this node, and both must be wired for it to function; either a 3D material or a 2D image is accepted at each. LeftMaterial: The orange left material input takes a 2D image or a 3D material that becomes the material for left eye rendering. A 2D image gets turned into a diffuse texture map via the basic material type. RightMaterial: The green right material input takes a 2D image or a 3D material that becomes the material for right eye rendering. Here too a 2D image is converted into a diffuse texture map via the basic material type. Although either input may be a 2D image or a 3D material, the output is invariably a material.

### Basic Node Setup

Either stereo images or stereo materials work with the Stereo Mix node. In the example beneath, two images merge inside the Stereo Mix node so that its output becomes a stereo anaglyph material.

A Stereo Mix node merging left and right images down to one stereo material Inspector

### Stereo Mix controls

### Controls Tab

A lone switch on the Controls tab exchanges the left and right material inputs. Swap This option flips both of the node’s inputs. Material ID This slider assigns the numeric identifier given to this material. Should the corresponding renderer option be on, the value lands in the MatID auxiliary channel.

### Common Controls

Settings Tab The Settings tab carried in the Inspector shows up again on the rest of the 3D nodes. Its common controls are spelled out fully where this chapter finishes, in “The Common Controls.”
