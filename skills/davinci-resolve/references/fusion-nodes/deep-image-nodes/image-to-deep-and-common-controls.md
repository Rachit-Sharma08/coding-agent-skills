# Image to deep and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Image to deep, Common controls.
[Chapter index](INDEX.md) / [Previous section](drecolor-and-dresize-and-dtransform.md)
<a id="source-basic-node-setup-8"></a> <a id="source-common-controls-8"></a> <a id="source-controls-tab-3"></a> <a id="source-image-to-deep-controls"></a> <a id="source-image-to-deep-itd"></a> <a id="source-image-to-deep-node-introduction"></a> <a id="source-inputs-6"></a> <a id="source-inspector-2"></a> <a id="source-settings-tab"></a> <a id="source-the-common-controls"></a> <a id="source-the-deep-image-settings-tab"></a> <a id="source-the-image-to-deep-node"></a>

### Image to Deep [ITD]

### The Image to Deep node

### Image to Deep Node Introduction

An input for a 2D image is what this tool carries. Once connected, the image gains deep image data and can be composited within a deep environment through the dMerge node.

### Inputs

A single input is what the Image to Deep tool relies on. Input: The lone required connection is this orange input. A node carrying 2D image data you mean to use with a Deep Image feeds it.

### Basic Node Setup

Into the Image to Deep node comes the media in that holds the 2D image data. From there it tacks Deep Image information onto it, so that it can be put to work in deep image compositing with a dMerge node.

Taking in a 2D image (MediaIn3), Image to Deep then tacks on Deep Image data so that, through a dMerge node, it can be composited together with Deep Image media (MediaIn1).

### Inspector

### Image to Deep controls

### Controls Tab

Inside the Controls tab sit parameters that govern the depth information.

- Specify Z: Tick this box to set the current Z depth. Leave it unticked and you can adjust it with the Z Scale control below.
- Z Scale: With the slider you can stretch or squeeze the source’s overall depth samples. Raise the scale and the overall depth distance grows. Lower it and the depth range gets compressed.
- Z Offset: Lets you slide an object forward or back along its depth channel. That gives you the control to move an object nearer to or farther from camera. Sample: Click and drag out of the sample button into the viewer to pick a value.
- Center X/Y: Reposition the 2D image along the X/Y axes.

### Common Controls

Settings Tab A copy of the Inspector’s Settings tab also appears on the other Deep Image nodes. These common controls are covered thoroughly at the end of this chapter, in the “The Common Controls” section.

### The Common Controls

### Settings Tab

On most tools in Fusion you’ll find the Common Settings tab. The controls below are settings specific to Deep Image nodes.

### The Deep Image Settings tab

Hide Incoming Connections Switch this checkbox on to tuck away connection lines coming from incoming nodes, which makes a node tree look tidier and read more easily. With it on, the Inspector shows an empty field for each input on a node. Drag a connected node out of the node tree into the field and that incoming connection line hides itself, so long as the node stays unselected in the node tree. Select the node in the node tree and the line returns. Comments Tab A single text control fills the Comments tab, used for adding comments and notes onto the tool. Add a note to a tool and a tiny red dot icon turns up beside the setting tab’s icon, while a text bubble shows on the node. To read the note in the Node Editor, rest the mouse pointer over the node briefly. Should you need it, the Comments tab’s contents can be animated over time. Scripting Tabs Every tool in Fusion carries the Scripting tab. It holds several edit boxes for adding scripts that run as the tool renders. For fuller detail on what this tab holds, please refer to the scripting documentation.
