# Layer muxer and layer regex

Version: DaVinci Resolve 20.3 Reference Manual. Context: Layer muxer, Layer regex.
[Chapter index](INDEX.md) / [Next section](layer-regex-and-layer-remover-and-swizzler.md)
<a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-common-controls"></a> <a id="source-controls-tab"></a> <a id="source-controls-tab-1"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-inspector"></a> <a id="source-inspector-1"></a> <a id="source-layer-muxer-controls"></a> <a id="source-layer-muxer-lmx"></a> <a id="source-layer-muxer-node-introduction"></a> <a id="source-layer-nodes"></a> <a id="source-layer-nodes-1"></a> <a id="source-layer-regex-controls"></a> <a id="source-layer-regex-lrx"></a> <a id="source-layer-regex-node-introduction"></a> <a id="source-the-layer-muxer-node"></a> <a id="source-the-layer-regex-node"></a>

### Layer Nodes

Here we look at how multilayer images are worked with and altered inside your compositions. Each node name carries an abbreviation alongside it, and those short codes are handy in the Select Tool dialog when you hunt for a tool, as well as throughout scripting references.

### Layer Muxer [LMx]

### The Layer Muxer node

### Layer Muxer Node Introduction

With this tool you can merge the layers belonging to one source into those of a different source. It exposes a pair of inputs, and once two multilayer sources feed into them, the layers coming from one are folded together with the layers from the other.

### Inputs

Two inputs feed the Layer Muxer tool. Image 1: Wire this orange input to a node carrying the multilayer data you intend to merge. Image 2: Wire this green input to a node carrying the multilayer data you intend to merge.

### Basic Node Setup

Fed by two nodes that each hold multilayer data, the Layer Muxer node blends them through several possible methods, governed by your choices about which layers to retain and which to skip.

Layer Muxer combines two multi layer images.

### Inspector

### Layer Muxer controls

### Controls Tab

Parameters for picking which layers get used live on the Controls tab.

- Layer: Choose layers out of the clip wired to the Image 2 input so they merge with the clip wired to Image 1. Using the pulldown control, you state which layer(s) should be folded in. Whenever you pick anything besides All Layers, a tiny layer icon shows up on the Layer Muxer node as a reminder that only a subset of layers is making it through. Default Layer: Should the Input 2 multilayer media file carry a default layer, that layer gets merged. All Layers: Merges every layer of the Input 2 multilayer image as a group. Custom: Brings up a checklist covering all the layers in Input 2 so you can toggle the individual layers on or off.
- Conflicts: This control lets you flip between Image 1 or Image 2, the pair of inputs on the tool; whichever Image you pick becomes the tool’s Default/[Main] layer on output.

### Common Controls

Settings Tab The Inspector’s Settings tab also recurs across the rest of the Layer nodes. Full coverage of these shared controls appears later, in the “The Common Controls” section that closes out this chapter.

### Layer Regex [LRx]

### The Layer Regex node

### Layer Regex Node Introduction

By using elaborate expressions, this tool screens the layers of multilayer files according to how those layers are named. After you set up a filter, any layers that satisfy the "expression" may be renamed, retained, or stripped away.

### Inputs

A pair of inputs feed the Layer Regex tool. Image 1: Hook this orange input up to a node holding the multilayer data you mean to filter. Image 2: Hook this green input up to a node holding the multilayer data you mean to filter.

### Basic Node Setup

Wired to two nodes that each carry multilayer data, the Layer Regex node enables you to sift through them with Regex according to the names of the layers.

Layer Regex filters layers from two multi layer images.

### Inspector

### Layer Regex controls

### Controls Tab

The Controls tab holds the parameters you use to pick which layers come into play.

- Expression: The filter responsible for matching or locating characters.
- Mode: Governs the manner in which the expression gets applied. Transform: The operation of renaming or replacing characters. Keep: Retains whichever layers the Expression rule names. Remove: Strips out whichever layers the Expression rule names.
- Name Template: The rule tied to the “Expression," letting you swap characters or give layers new names.
- Unmatched: Sets how layers that fall outside the expression are handled. Keep: Layers that don't satisfy the Expression stay put; every layer is kept. Remove: Layers that don't satisfy the Expression are dropped. That leaves only the layers the expression actually touches.
- Tester: A lightweight utility that shows what your expression produces while you tweak the parameters.
- Conflicts: This control flips between Image 1 or Image 2, the two inputs on the tool; whichever Image you choose is sent out as the tool’s Default/[Main] layer.
