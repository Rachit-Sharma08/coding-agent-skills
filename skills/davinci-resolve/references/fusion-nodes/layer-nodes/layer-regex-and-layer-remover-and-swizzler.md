# Layer regex and layer remover and swizzler

Version: DaVinci Resolve 20.3 Reference Manual. Context: Layer regex, Layer remover, Swizzler.
[Chapter index](INDEX.md) / [Previous section](layer-muxer-and-layer-regex.md) / [Next section](swizzler-and-common-controls.md) / [Layer Regex LRx](layer-muxer-and-layer-regex.md)
<a id="source-basic-node-setup-2"></a> <a id="source-basic-node-setup-3"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab-2"></a> <a id="source-controls-tab-3"></a> <a id="source-examples"></a> <a id="source-inputs-2"></a> <a id="source-inputs-3"></a> <a id="source-inspector-2"></a> <a id="source-inspector-3"></a> <a id="source-layer-remover-controls"></a> <a id="source-layer-remover-lrm"></a> <a id="source-layer-remover-node-introduction"></a> <a id="source-swizzler-controls"></a> <a id="source-swizzler-node-introduction"></a> <a id="source-swizzler-swz"></a> <a id="source-the-layer-remover-node"></a> <a id="source-the-swizzler-node"></a>

### Examples

Add a prefix to existing layer names Expression: (.\*) Name Template: Right.$1 Doing this prepends Right. onto every one of the layer names, so you end up with Right.Layer1 , Right.Layer2 NOTE: For a suffix instead, flip the order within the Name Template, $1.Right. That yields Layer1.Right , Layer2.Right

Locate certain characters or words within the current layer names, then prepend a prefix Expression: (Right._) Name Template Stereo-$1 Here the operation finds whichever layers hold the word Right, then tacks the word Stereo- onto the front of each of those layer names, producing Stereo-Right.Layer1 Swapping text out Expression: right(._) Name Template: Left$1 With this, layer names that include right get found and that layer name is exchanged for Left. As a result, layers labeled right.1 , right.2 , right.3 become renamed to Left.1 , Left.2 , Left.3 . Bear in mind that with this approach, any layer name carrying the letters right (for instance, copyright) gets caught by the expression and is renamed too. If you want to pin down a specific run of characters, reach for the expression ^right(.\*) NOTE: The ^ stands for matching the very start of the text. That makes it screen right yet leave copyright alone, since copyright opens with a copy.

Match one word or the other, then strip them out (or retain them) Expression: (copy|right) Mode: Remove (copy|right) picks out copy and right , and with the mode at Remove, any layers holding copy or right get stripped from the layer list. An expression like this comes in handy for catching variants of a word, such as (copy|Copy|COPY) NOTE: Switching the mode to Keep instead preserves the layers that satisfy the Expression. Taking the example above, if the Mode reads Keep, the layers holding copy or right are the ones left behind while everything else is removed.

Find characters, ignoring case Expression: (?i)(right) This grabs every character in the word right, regardless of upper case. In practice that means any capitalized form of the word right: Right, RIGHT or riGth gets grabbed. RegEx Cheat Sheet To read more about working with RegEx https://www.debuggex.com/cheatsheet/regex/pcre Common Controls Settings Tab The Inspector’s Settings tab likewise shows up on the other Layer nodes. A thorough rundown of these shared controls sits at the chapter’s end within the “The Common Controls” section.

### Layer Remover [LRm]

### The Layer Remover node

### Layer Remover Node Introduction

Using this tool, you get an easy means of disabling or stripping layers out of a source that's connected to it.

### Inputs

A single input feeds the Layer Remover tool. Image 1: Connect this orange input to a node holding the multilayer data from which you intend to strip a layer.

### Basic Node Setup

Fed by a node that carries Multilayer data, the Layer Remover node lets you pull out particular layers ahead of handing the image downstream.

Layer Remover lets you disable specific layers of a multilayer file.

### Inspector

### Layer Remover controls

### Controls Tab

On the Controls tab you'll find a plain checklist covering every layer in the multilayer clip. Ticking a box disables or removes the corresponding layer(s) from the layer list.

### Common Controls

Settings Tab Like the others, the Inspector's Settings tab is shared with the rest of the Layer nodes. You'll find these common controls explained thoroughly at the close of this chapter under the “The Common Controls” section.

### Swizzler [Swz]

### The Swizzler node

### Swizzler Node Introduction

With this tool you can fold one or more image layers and/or channels into a custom-built layer or set of layers. Much like Channel Booleans, Swizzler is able to take channels from a source and route them into a destination channel; the key distinction, though, is that Swizzler works with layers, whether it draws on layers as a source or spins up new ones. Put plainly, the tool can manufacture new layers, drive source layers or channels into a layer, or pull channels out of a source.

### Inputs

The Swizzler tool takes several inputs. Input 1: Wire this orange input to a node holding the image data you'd like folded into a new layer. Input X: The white inputs get wired to further nodes whose image data you'd like folded into a new layer.

### Basic Node Setup

Fed by several nodes that each carry image data, the Swizzler node merges them to form new layers.

### Inspector

Swizzler combines multiple images into new layers.

### Swizzler controls

### Controls Tab

The Controls tab carries the parameters used to pick which layers are applied.

- Layer List: Through the layer list you can browse and pick custom layers. The button beneath it lets you append a fresh layer to the list, bringing in a new custom layer. For whichever layer you've highlighted in this list, the

options underneath let you decide which channels belong in the layer. On top of that, you're able to rename layers right inside this list. Add Layer: Generates a new layer and tacks it onto the layer list. Keep Main Input Layers: Ticking this box holds onto the layers already present in the source clip wired to Input1. With it switched on, the Input1 layers carry through to the Swizzler output, leaving you free to stack further layers atop an existing multilayer source.

- Channels: With this control you decide which channels get added to whichever layer is selected in the layer list. All Channels: Moves every channel into the selected layer. Color/Aux: Surfaces extra "Color" and "Aux" options that split RGBA apart from AUX channels. That split lets you name a source for the RGBA and a separate source for the AUX channels, so in the end RGBA comes from one input while AUX comes from another. Two further options, “RGB/A“ and “R/G/B/A,” hand you even finer control over channels and widen the source choices for individual channels.
- Source: Pick an input from this drop-down to feed layers or channels into your chosen layer. The chosen layer here is whatever you've highlighted in the layer list above.
- Source Layer: With a multi-layer file wired to one of the inputs, this control lets you target a particular layer. Every layer offered by the Source Input control is shown.
- Source Channels (Color/Aux mode): Pick which channels of the chosen layer should feed the Aux channel. Should the chosen layer lack Aux channels and have been rendered as RGB only, fall back instead on the color values — that is, RG for UV Texture or RGB for XYZ Normal.
