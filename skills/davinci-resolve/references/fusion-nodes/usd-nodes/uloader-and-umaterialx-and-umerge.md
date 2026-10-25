# Uloader and umaterialx and umerge

Version: DaVinci Resolve 20.3 Reference Manual. Context: Uloader, Umaterialx, Umerge.
[Chapter index](INDEX.md) / [Previous section](uexport-and-uimage-plane-and-uloader.md) / [Next section](urenderer.md) / [uLoader uLd](uexport-and-uimage-plane-and-uloader.md)
<a id="source-basic-node-setup-4"></a> <a id="source-basic-node-setup-5"></a> <a id="source-common-controls-3"></a> <a id="source-common-controls-4"></a> <a id="source-controls"></a> <a id="source-inputs-5"></a> <a id="source-inputs-6"></a> <a id="source-inspector-4"></a> <a id="source-the-umaterialx-controls"></a> <a id="source-umaterialx-umx"></a> <a id="source-umerge-umg"></a>

### Common Controls

Settings Tab You’ll also see the Inspector’s Settings tab on the other USD nodes. A detailed write-up of these shared controls sits in the “The Common Controls” section at this chapter’s end.

### uMaterialX [uMX]

The uMaterialX node uMaterialX Node Introduction All the uMaterialX node does is read in a MaterialX (.mtlx) definition file and produce a USD scene file holding nothing but those materials.

### Inputs

The uMaterialX node has no inputs at all—just a file requester for loading the .mtlx file.

### Basic Node Setup

Wire the material output into the remaining USD tools.

Here a node tree depicts a MaterialX definition (.mtlx) file named Material4 being read into a uMaterialX node, which hands the material on to a uReplaceMaterial node so the material gets swapped within a USD scene named JogBackwards.

### Inspector

### The uMaterialX controls

### Controls

There’s only one control here: a a Material File selector paired with a browse button for loading the .mtlx file off your computer. Settings Tab The Inspector’s Settings tab turns up on the other USD nodes as well. These shared controls get a thorough explanation in the “The Common Controls” section near the end of this chapter.

### uMerge [uMg]

The USD Merge node uMerge Node Introduction The uMerge node is Fusion’s main node for bringing distinct 3D elements together into one shared 3D environment. Take a scene built from an image plane, a camera, and a light: the camera couldn’t see the image plane and the light couldn’t touch it until all three objects are gathered into the same environment by way of the uMerge node. The uMerge carries the same standard transformation controls that most nodes in Fusion’s USD suite have. What sets it apart is that adjusting the uMerge’s translation, rotation, or scale alters every object wired into the uMerge. That behavior is what underpins all parenting throughout Fusion’s 3D environment.

### Inputs

At first the uMerge node shows three inputs, yet every time you fill one, another input pops up on the node, so there’s always a spare for adding a fresh element to the scene. SceneInput[#]: You use these inputs to attach USD image planes, 3D cameras, lights, whole USD scenes, and other uMerge nodes too. The node places no cap on how many inputs it will take. It keeps adding inputs on the fly as required, guaranteeing that at least one input is always open for a connection.

### Basic Node Setup

The uMerge node pulls together the 3D USD scene coming from the uLoader, two light sources, and the camera, then hands that view off to the uRenderer node, which flattens it down into a 2D image.

### Common Controls

Transform and Settings Tab Here too the Inspector’s Transform and Settings tab is shared with the other USD nodes. You can read a full description of these common controls in the “The Common Controls” section at the close of this chapter.
