# Createreliefmap and reliefmap

Version: DaVinci Resolve 21 New Features Guide. Context: Createreliefmap, Reliefmap.
[Chapter index](INDEX.md) / [Previous section](uprojector-and-ucatcher-and-createreliefmap.md) / [Next section](reliefmap-and-dcolorcorrector.md) / [CreateReliefMap CRM](uprojector-and-ucatcher-and-createreliefmap.md)
<a id="source-basic-node-setup-1"></a> <a id="source-basic-node-setup-2"></a> <a id="source-changing-common-inspector-properties"></a> <a id="source-common-controls-2"></a> <a id="source-common-controls-3"></a> <a id="source-controls-tab"></a> <a id="source-controls-tab-1"></a> <a id="source-createreliefmap-controls"></a> <a id="source-inputs-1"></a> <a id="source-inputs-2"></a> <a id="source-inspector"></a> <a id="source-inspector-1"></a> <a id="source-multi-inspector"></a> <a id="source-reliefmap-3rm"></a> <a id="source-reliefmap-controls"></a> <a id="source-reliefmap-node-introduction"></a> <a id="source-the-reliefmap-node"></a> <a id="source-the-source-shape-fed-into-the-createreliefmap-node"></a>

### Inputs

The lone yellow input takes a 2D image.

### Basic Node Setup

Here, a chain of shape nodes feeds the input of the CreateReliefMap node. That node’s output would next be routed into a ReliefMap node to set the depth of the 3D surface.

A 2D shape arrives from the sRender node into the CreateReliefMap node.

As an example, a plain Arrow Shape is built and routed into the CreateReliefMap node.

Once you have tweaked the CreateReliefMap node, you would then wire its output into a ReliefMap node.

You would then tweak settings in the ReliefMap Node to actually lay the shape onto the connected 3D image.

### The source shape fed into the CreateReliefMap node

What the CreateReliefMap produces here is the output you would then route into the ReliefMap node

The output the ReliefMap node yields once applied onto a 3D shape

### Inspector

### CreateReliefMap controls

### Controls Tab

Map Type There are 3 choices on offer: Relief, Relaxed Cone and Cone. Each of the three relies on a mix of RGB and Alpha to build the relief map. Relaxed Cone and Cone can give more accurate output at the cost of performance. Depth Source Pick from the dropdown menu which source supplies the depth data for the relief map. Depth Scale Raising the slider’s value deepens the relief map. Texture Depth Choices to keep or alter the bit depth of the relief map. Pre Blur Move the slider to apply more pre blur onto the source image ahead of building the Relief Map. Flip Depth Ticking this box reverses the depth mapping.

The same shape above, with the Flip Depth checkbox selected.

### Common Controls

Transform and Settings Tabs The Transform and Settings tabs that remain are shared by many nodes. You will find their descriptions in the “The Common Controls” section that closes this chapter.

### ReliefMap [3RM]

### The ReliefMap node

### ReliefMap Node Introduction

Relief Map is a 3D tool that adds height-driven surface detail onto 3D shapes. Drawing on an image routed through its partner Create Relief Map node, the Relief Map carves away parts of a 3D shape, in effect building depth information for the surface. This sculpting approach modifies a material’s normal/displacement mapping directly, allowing rich textures to emerge without the need to hand-model every detail. What distinguishes Relief mapping from bump maps is that Relief can occlude itself, producing natural lighting interactions. The Relief Map’s RGB channels hold normals values while the alpha carries the height/depth.

### Inputs

Background Input: A material connection feeds the yellow input — for example Blinn, Ward, CookTorrance or Phong. Relief Map Input: Into the white input you wire a 2D image, routed through the Create Relief Map node, that will serve as the Relief Map texture.

### Basic Node Setup

Here, a Text+ node runs through a Create Relief Map node to build the data the Relief Map needs before it is laid onto a Shape3D. For the Relief Map, the produced map goes into the white input while a material goes into the yellow input. The Relief Map’s output is wired to 3D geometry (Shape3D) and merged into a 3D scene.

The ReliefMap node merging data from both a Relief Map and a Blinn node before sending the completed relief data on to apply to a Shape3D node.

### Inspector

### ReliefMap controls

### Controls Tab

Depth Scale This slider lets you stretch or compress the relief map’s total depth. Pushing the depth scale up boosts the overall span of depth. Lock U/V With this on, the U/V channels scale together uniformly. With it off, each channel’s frequency can be tuned on its own. Map Type Two methods exist for applying a relief map, Relief and Cone. Both draw on RGBA values to build data, though Cone delivers higher quality and quicker shading at a performance cost. Quality Raising the quality slider’s value sharpens the result. The effect is most visible with the Relief map type.

### Common Controls

Transform and Settings Tabs The Transform and Settings tabs that remain are shared by many nodes. You will find their descriptions in the “The Common Controls” section that closes this chapter.

### Multi-Inspector

The Multi-Inspector is a strong new addition in Fusion v21 letting users tweak shared properties across several selected tools at the same time. It smooths out workflows by removing the need to set identical parameters on every tool one by one. With several tools chosen in the Flow, the Multi-Inspector shows controls shared among them all. Users then adjust these common parameters, and the edits land at once on every selected tool.

### Changing Common Inspector Properties

The Combine Selected Tools icon in the Inspector header With several tools selected, a fresh toggle icon in the Inspector header now lets them merge into one set, displaying only the controls every selected tool has in common. Dragging one such control, or entering a fresh value, adjusts all the selected tools together. This can speed up plenty of routine workflows, letting you tweak many different tools at once without needing full instancing or copy & paste.

Two uTransform nodes merged let you set parameters for both tools at once. When the chosen controls hold differing values across tools, the control knobs and values are hidden. Dragging on the value edit field adds or removes an offset from each tool’s control on its own, keeping the differences rather than forcing them to match. Size and Scale controls instead apply a scaling factor, holding the ratio between each tool. On top of that, holding the Opt/Alt key while dragging toggles between offset and scale mode, giving you even finer control.
