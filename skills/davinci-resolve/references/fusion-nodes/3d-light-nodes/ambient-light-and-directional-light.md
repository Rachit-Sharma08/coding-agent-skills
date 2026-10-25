# Ambient light and directional light

Version: DaVinci Resolve 20.3 Reference Manual. Context: Ambient light, Directional light.
[Chapter index](INDEX.md) / [Next section](directional-light-and-domelight-and-point-light.md)
<a id="source-3d-light-nodes"></a> <a id="source-3d-light-nodes-part-1"></a> <a id="source-ambient-light-3al"></a> <a id="source-ambient-light-controls"></a> <a id="source-ambient-light-node-introduction"></a> <a id="source-ambient-light-node-structure"></a> <a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-common-controls"></a> <a id="source-controls-tab"></a> <a id="source-controls-tab-1"></a> <a id="source-directional-light-3dl"></a> <a id="source-directional-light-controls"></a> <a id="source-directional-light-node-introduction"></a> <a id="source-directional-light-node-structure"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-inspector"></a> <a id="source-inspector-1"></a> <a id="source-the-ambient-light-node"></a> <a id="source-the-directional-light-node"></a>

### 3D Light Nodes

This section walks through the 3D Light nodes you can reach while building 3D composites inside Fusion. Each node name carries a short abbreviation beside it; type that code into the Select Tool dialog to find a tool, and the same code surfaces in scripting references.

Throughout this write-up, any node tree that pictures MediaIn nodes in DaVinci Resolve behaves the same as one using Loader nodes in Fusion Studio, except where a note says otherwise.

### Ambient Light [3AL]

### The Ambient Light node

### Ambient Light Node Introduction

An Ambient Light casts illumination across the whole scene with no particular direction. It carries no meaningful position or rotation, though the viewer still draws an onscreen control so you know a light exists. The viewer also offers position controls so you can slide that widget aside when it overlaps other geometry. As with a Camera 3D, lights are wired into a Merge 3D and become visible only when you view the Merge 3D node; choosing a light node on its own and sending it to the viewer displays nothing.

### Inputs

There is just one optional orange input on the Ambient Light node, meant for a 3D scene or 3D geometry. SceneInput: This optional orange input takes a 3D scene. When you feed it a scene, the node's Transform controls then act on that whole scene.

### Basic Node Setup

Think of the Ambient Light node as one piece of a broader 3D scene. The light wires straight into a Merge 3D, and by routing lights through separate Merge 3D nodes you decide which objects each light reaches.

### Ambient Light node structure

### Inspector

### Ambient Light controls

### Controls Tab

Use the Controls tab to dial in the hue and brightness of the ambient light. Enabled With the Enabled checkbox ticked, the ambient light contributes to the scene; clearing it switches the light off. That checkbox mirrors the red switch sitting to the left of the node’s name in the Inspector. Color This standard Color control picks the light’s color. Intensity Drag this slider to dial the ambient light's Intensity, where 0.2 corresponds to light at 20% percent. As an illustration, a pure-white texture lit by nothing but a 0.2 ambient light renders out as 20% gray (.2, .2, .2).

### Common Controls

Transform and Settings Tabs The parameters shown on the Transform and Settings tabs recur across the other lighting nodes as well. For a fuller description of what each of these tabs offers, turn to the “The Common Controls” section at the end of this chapter.

### Directional Light [3DL]

### The Directional Light node

### Directional Light Node Introduction

A directional light has a definite direction yet no defined origin point or distance, much like sunlight. It does display an onscreen control, but where that control sits carries no significance. Instead, the control's rotation determines the apparent direction the light streams from within the scene. As with a Camera 3D, you wire lights into a Merge 3D and see them by viewing that Merge 3D node; picking a light node alone and loading it into the viewer reveals nothing.

### Inputs

The Directional Light node carries one optional orange input for a 3D scene or 3D geometry. SceneInput: This optional orange input takes a 3D scene, and once a scene is connected the node's Transform controls govern that entire scene.

### Basic Node Setup

The Directional Light node belongs within a larger 3D scene. Run the light straight into a Merge 3D, and split lights across separate Merge 3D nodes when you want to govern which objects each light touches.

### Directional Light node structure

### Inspector

### Directional Light controls

### Controls Tab

Use the Controls tab to choose the hue and brightness of the directional light, while the rotation controls over in the Transform tab steer which way the source points. Enabled Ticking the Enabled checkbox lets the directional light act on the scene; clearing it turns the light off. This checkbox does the same job as the red switch beside the node’s name in the Inspector. Color This standard Color control sets the light’s color. Intensity This slider governs the directional light's Intensity, with 0.2 mapping to light at 20% percent.
