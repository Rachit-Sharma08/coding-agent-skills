# Utransform and uvariant and uvisibility and uvolume

Version: DaVinci Resolve 20.3 Reference Manual. Context: Utransform, Uvariant, Uvisibility, Uvolume.
[Chapter index](INDEX.md) / [Previous section](ushape-and-uswitch-and-utransform.md) / [Next section](uvolume-controls.md) / [Continue uVolume uVo / Usage](uvolume-controls.md) / [uTransform uXF](ushape-and-uswitch-and-utransform.md)
<a id="source-basic-node-setup-4"></a> <a id="source-basic-node-setup-5"></a> <a id="source-basic-node-setup-6"></a> <a id="source-common-controls-4"></a> <a id="source-controls-tab-2"></a> <a id="source-controls-tab-3"></a> <a id="source-controls-tab-4"></a> <a id="source-inputs-5"></a> <a id="source-inputs-6"></a> <a id="source-inspector-4"></a> <a id="source-inspector-5"></a> <a id="source-inspector-6"></a> <a id="source-the-usd-transform-controls"></a> <a id="source-the-uvariant-controls"></a> <a id="source-the-uvisibility-controls"></a> <a id="source-the-uvisibility-node"></a> <a id="source-the-uvolume-tool"></a> <a id="source-uvariant-uva"></a> <a id="source-uvisibility-uvis"></a> <a id="source-uvolume-uvo"></a>

### Basic Node Setup

The uTransform node layers 3D position, rotation, and pivot control on top of whatever transforms already exist in the USD node ahead of it. Chaining several uTransform nodes together lets you construct parenting or hierarchical movement.

The uTransform node hands you a further set of 3D transform controls, usable for tweaking the ones in the uShape node's Transform tab.

### Inspector

### The USD Transform controls

### Controls Tab

Pick Pick brings up the Scene Tree window, where you single out particular materials or objects within a USD scene. For more on working with the USD Scene Tree, consult its section near this chapter's start. Translation Transform controls serve to place the USD shape within 3D space.

Rotation Order These buttons set the order in which rotation is applied along each axis of the object. XYZ, for instance, would rotate the X-axis first, then the Y-axis, and finally the Z-axis. Rotation Use these controls to spin the shape about its pivot point. With the Use Target checkbox ticked, rotation is relative to the target's position; otherwise the global axis governs it. Pivot An object's pivot point is the spot it rotates around. By default an object turns about its own center, treated as a pivot of 0,0,0. These controls let you shift the pivot off the center. Scale With the Lock X/Y/Z checkbox ticked, a single scale slider appears that resizes the object overall. Leave the Lock checkbox unticked and separate X, Y, and Z sliders show up so you can scale along any dimension. Scale Ticking the Use Target checkbox brings up a set of controls for positioning an XYZ target. With the target on, the object continually rotates to face it, and the object's rotation becomes relative to the target.

### Common Controls

Settings Tab The Settings tab found in the Inspector is mirrored on the other USD nodes as well. These common controls receive a full explanation in the "The Common Controls" section wrapping up this chapter.

### uVariant [uVa]

The uVariant node uVariant Node Introduction Hooking the uVariant node up to the USD loader lets you flip among the various alternatives, or "variants," that have been defined for assets within the USD scene.

### Inputs

One required input for a USD scene or USD object is all the uVariant node has.

### Basic Node Setup

The uVariant node lets you pick from whichever variants have been created inside a USD scene. It takes a USD scene as input.

The uVariant node accepts the input from the MonsterJumpDown USD scene.

### Inspector

### The uVariant controls

### Controls Tab

Pick Pick brings up the Scene Tree window for singling out particular materials or objects within a USD scene. For more on working with the USD Scene Tree, consult its section near this chapter's opening. Selected Prims Lists which prims have been picked. Invert Prim Selection Tick this box to trade the picked prims for the unpicked ones. Keyframes can animate this action.

Variant Set This drop-down menu reveals which of the scene elements carry variants to pick from. When no variants exist, it shows No Selection. Variant Having chosen a variant set above, the variant choices to pick between turn up in this dropdown.

### uVisibility [uVis]

The uVisibility node uVisibility Node Introduction Hooking the uVisibility node up to the USD loader lets you govern whether an object, or a whole branch of objects, in a scene is visible.

### Inputs

A lone required input for a USD scene or USD object is what the uVisibility node carries. Scene Input: Connect the orange scene input to a USD scene or USD object so a second set of transformation controls can be applied.

### Basic Node Setup

The uVisibility node takes a USD scene and then sends the visible elements onward to the rest of the node tree.

### The uVisibility node

The uVisibility tool lets you reveal or conceal individual 3D assets. Above, the cityscape model (left) has been set visible, while below it's concealed with its visible box cleared.

### Inspector

### The uVisibility controls

### Controls Tab

Pick Pick brings up the Scene Tree Dialog, where you single out particular materials or objects within a USD scene. The prims highlight in the viewer as you select them. Refer to this chapter's opening for details on working with the Scene Tree Dialog. Selected Prims Lists the prims that have been picked.

Invert Prim Selection Tick this box to swap the picked prims for the unpicked ones. Keyframes can animate this action. Visible Toggling this checkbox either adds the picked prims to the view or pulls them from it. Keyframes can animate this action.

### uVolume [uVo]

### The uVolume tool

Introduction uVolume is a flexible, capable tool that streamlines bringing volumetric VDB files into a USD environment. Through this node you can tweak VDB parameters like density, temperature, and color, handing you full command over how the imported VDB file looks and behaves.
