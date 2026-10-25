# Cut copy and paste in the node editor pasting node settings

Version: DaVinci Resolve 20.3 Reference Manual. Context: Cut copy and paste in the node editor.
[Chapter index](INDEX.md) / [Previous section](node-view-indicators-and-clipboard.md) / [Next section](cut-copy-and-paste-in-the-node-editor-instanced-nodes.md) / [Cut, Copy, and Paste in the Node Editor](node-view-indicators-and-clipboard.md)
<a id="source-copying-and-pasting-nodes-to-and-from-any-text-editor"></a> <a id="source-input-layer-controls"></a> <a id="source-instancing-nodes"></a> <a id="source-nodes-and-inspector"></a> <a id="source-pasting-node-settings"></a> <a id="source-using-multilayer-nodes-studio-version-only"></a> <a id="source-viewer"></a>

### Pasting Node Settings

Rather than pasting a whole node, you may opt to paste only the parameter settings copied off another node. That comes in handy whenever you have painstakingly dialed in or animated parameters on one node and wish to reuse them on a second. Bear in mind that settings can be pasted between two nodes of identical type, or between two wholly different node kinds that nonetheless share one or more of the same parameters in the Inspector. While copying settings across node types, only the settings shared by both nodes get carried over. One common scenario takes an animated Center parameter from a Transform node and drops it onto a Mask node’s Center parameter. Moving settings between two nodes goes like this: 1 Pick a node holding settings you wish to copy, then choose Copy from the Edit menu (Command-C). 2 Right-click whichever node should receive those settings, and choose Paste Settings from the contextual menu.

### Copying and Pasting Nodes to and from Any Text Editor

Nodes in the Node Editor are stored not as binary but rather in a straightforward text format. What that implies might not jump out at first, yet one handy benefit shows up plainly once you begin handling nodes. You can copy one or more nodes out of the Node Editor and paste them straight into a text editor or an email. Doing so drops in the selection as text, exactly the way Fusion keeps it internally. As an illustration, were you to copy the following set of three nodes:

Three nodes shown in the act of being copied. Paste them afterward into a fresh text editing document and what you end up with is this:

The same three nodes pasted into a text editor.

From here, you can edit that text (assuming you know what you are doing), email it to coworkers, or tuck it away in some digital notepad for later use. Putting this script back to work in Fusion takes nothing more than copying it and pasting it back into the Node Editor. TIP: It makes for an exceedingly simple way to trade particular node settings between artists who might be in different rooms, cities, or even countries.

### Using Multilayer Nodes (Studio Version Only)

Multilayer image workflows are handled smartly by Fusion, which supports EXR, Stereoscopic 3D, and PSD assets. The Fusion viewers let users view a list of layers, and within the Settings tab in the Inspector you can interact with the layers belonging to each node. Because this layer structure carries through the whole toolset, you are able to confine a tool to operate on a single layer while the remaining layers pass through untouched.

### Viewer

While loading a multilayer file, you can preview individual layers in the Viewer and pick a layer off the drop-down list. A file lacking layer support offers only a ‘default’ entry in the drop-down menu.

Employing the Viewer’s Layer drop-down to isolate, for viewing, only the Asteroids layer out of a multilayer file

### Nodes and Inspector

The Settings tab holds a Layer category that grants you a set of controls for affecting particular layers and for governing layers coming from each tool input.

- Process Layers: Picks which layer the effects draw from: Default Layer (default): Puts the effect on the base/unnamed layer and leaves the rest untouched. All Layers: Puts the effect across every layer on offer. Custom: Lets you pick among the other available layers to receive the effect, leaving the remaining ones untouched.
- Input Layer: The Input Layer enumerates every layer coming from the upstream node feeding the default input. The chosen layer can be put to use by the current tool, or in isolation further down the node tree.
- Effect Mask Layer: Should the tool carry an Effect Mask input, this control enumerates the available layers able to supply mattes for the tool.

Wiring the multilayer file straight into the BrightnessContrast Effect Mask (blue arrow) on top of its normal input lets you swiftly produce flawless masks of any layer within the file.

Where a tool carries additional named inputs (Image, for one), it may surface further layer controls bearing a matching name (Image Layer, for one).

### Input Layer Controls

To run at peak performance, Fusion tools ask each input only for the processed layers. The Input Layer, Effect Mask Layer, Image Layer and the other input layer controls let the user tailor that behavior. Within each input control, you may pick Auto or Match, or settle on an explicit layer value to map:

- Auto (Default): Asks for whichever layer the Process Layers control has chosen. Should that layer be absent, the tool drops back to the default layer.
- Match: Asks for whichever layer the Process Layers control has chosen. Should that layer be absent, the tool reports a failure instead.
- Explicit Layer Selection: Asks for one specific layer named among those listed. Doing so confines that single layer for use in the present tool, or onward down the node tree.

When dealing with Fusion plugins, the Process Layer and Input Layer controls get generated automatically inside the Inspector’s Settings tab. Plugin authors may elect to spell out and position the controls somewhere else, much as the MultiMerge sets its controls within the main controls section. A number of Fusion tools carry controls for handling extra layer-based decisions. For instance:

- With a stereoscopic camera in play, the Renderer3D surfaces a fresh Eye control > Layers option,

which lets the left and right eyes each be output as their own layer.

- While merging multilayered sources by way of composite nodes (MultiMerge, say),

Channel Booleans, or a MatteControl, the Settings tab carries extra controls offering Background or Foreground options that isolate the chosen layers and bring them together.

- The Combiner tool serves to build custom layers. Switch the Mode to Layer. That reveals layer name fields where you can title the new layers.

### Instancing Nodes

As a rule, when copy and paste produces a duplicate of a node, that fresh node stands fully apart from the source node, so edits to one never propagate to the other. Even so, occasions arise where two nodes have to carry matching settings at every moment. Take the example of applying identical color corrections to two or more images: you would rather not endlessly tweak one color correction node and then by hand match the second to it. That is tedious, and in a rush you might neglect to keep them aligned. There do exist ways to publish controls in one node and tie them to corresponding controls in another, but for nodes where you are adjusting several controls that approach grows unworkably intricate and slow. Under such circumstances, building “instanced” nodes saves genuine time, and also serves as a plain visual signal in your node tree of what is happening.
