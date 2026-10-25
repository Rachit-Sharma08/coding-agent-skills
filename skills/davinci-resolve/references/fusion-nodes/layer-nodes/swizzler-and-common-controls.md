# Swizzler and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Swizzler, Common controls.
[Chapter index](INDEX.md) / [Previous section](layer-regex-and-layer-remover-and-swizzler.md) / [Swizzler Swz](layer-regex-and-layer-remover-and-swizzler.md)
<a id="source-assigning-aux-channels"></a> <a id="source-common-controls-2"></a> <a id="source-connecting-multiple-rgb-sources-to-the-swizzler"></a> <a id="source-connecting-multiple-rgb-sources-to-the-swizzler-1"></a> <a id="source-creating-a-new-layer-in-the-swizzler"></a> <a id="source-creating-new-layers-in-the-swizzler"></a> <a id="source-examples-1"></a> <a id="source-previewing-the-new-channels-in-the-viewer"></a> <a id="source-selecting-the-new-layers-in-the-viewer"></a> <a id="source-settings-tab"></a> <a id="source-the-common-controls"></a> <a id="source-the-settings-tab"></a>

### Examples

### Assigning Aux channels

For the example below, several RGB sources are on hand. Every one of them is a pre-rendered pass that we'd like to route to an Aux channel.

### Connecting multiple RGB sources to the Swizzler

Every RGB pass gets wired into its own fresh input on the Swizzler.

### Creating a new layer in the Swizzler

A fresh layer has been appended to the layer list; since it's the only layer present, it takes on the role of the new ‘default layer’

Assigning sources in the channel controls for the new layer

Within the channel controls for the new layer, set the right source for each of the Aux channels.

### Previewing the new channels in the viewer

After every one of the Aux channels has had an input assigned to it, you can preview the channels in the viewer. Creating a multilayer clip For this example, several RGB sources are available. Each one is a pre-rendered pass that we'd like to route to a new layer, building a multilayer clip in the process.

### Connecting multiple RGB sources to the Swizzler

Each RGB pass feeds into a separate new input on the Swizzler.

### Creating new layers in the Swizzler

Inside the layer list, append a new layer for each pass and assign it a custom name. Highlight a layer in the layer list, then in the controls set the appropriate source input for that layer. As an illustration, the UV pass has been wired to Input 4; by selecting the custom layer named “UV-Texture” and picking Input 4 from the Input list, all of the channels from Input 4 are driven into the “UV-Texture” layer.

### Selecting the new layers in the viewer

After each of the inputs has had a custom layer assigned to it, you can preview them in the viewer and put them to work in the comp.

### Common Controls

Settings Tab As with the other nodes, the Inspector's Settings tab reappears throughout the Layer nodes. These shared controls get a detailed treatment near the chapter's end in the “The Common Controls” section.

### The Common Controls

### Settings Tab

### The Settings tab

You'll come across the Common Settings tab on the majority of tools in Fusion. The controls below are settings tied specifically to Deep Image nodes. Hide Incoming Connections Turning on this checkbox lets you conceal the connection lines arriving from upstream nodes, which keeps a node tree tidier and more legible. With it active, the Inspector shows an empty field for each of a node's inputs. If you drag a connected node out of the node tree and into that field, the incoming connection line is hidden for as long as the node stays unselected in the node tree. The moment the node becomes selected in the node tree, the line shows up again.

Comments Tab Just one text control sits on the Comments tab, and you use it to attach comments and notes to the tool. As soon as a note is attached to a tool, a small red dot icon shows up beside the setting's tab icon and a text bubble surfaces on the node. To read the note within the Node Editor, rest the mouse pointer over the node briefly. Should you need it, the material on the Comments tab can be animated across time. Scripting Tabs Every tool in Fusion carries the Scripting tab. Within it are several edit boxes where you can enter scripts that run while the tool renders. For fuller detail on what this tab offers, refer to the scripting documentation.
