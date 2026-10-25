# Vector transform and vector warp and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Vector transform, Vector warp, Common controls.
[Chapter index](INDEX.md) / [Previous section](vector-transform-controls.md) / [Vector Transform VXf](tween-and-vector-denoise-and-vector-transform.md)
<a id="source-a-vector-warp-node"></a> <a id="source-basic-node-setup"></a> <a id="source-common-controls"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab"></a> <a id="source-inspector"></a> <a id="source-inspector-1"></a> <a id="source-settings-tab"></a> <a id="source-the-common-controls"></a> <a id="source-the-common-optical-flow-settings-tab"></a> <a id="source-the-vector-warp-controls-tab"></a> <a id="source-the-vector-warp-node"></a> <a id="source-vector-warp-node-introduction"></a> <a id="source-vector-warp-vwp"></a>

### Common Controls

Settings Tab The Inspector’s Settings tab is repeated across the rest of the Optical Flow nodes too. A full breakdown of these shared controls sits at this chapter’s conclusion within the “The Common Controls” section.

### Vector Warp [VWp]

### The Vector Warp node

### Vector Warp Node Introduction

A Vector Warp node carries a primary image input stream (serving as the background) plus the map input picture (a still that gets warped). What comes out is an RGBA picture that can carry additional motion vector channels (Vx, Vy. BVx, BVy) holding forward and backward tracking data so later tools downstream can use it. The node bends a chosen reference frame or picture to match how the source clip moves. Two inputs feed the node: the Input Layer, which takes your source clip together with its motion vectors (produced by an Optical Flow tool), and the Texture Layer. Whatever clip or picture you attach to the Texture Layer gets warped according to how the vectors arriving from the Input Layer move. Before any warping happens, the source clip first needs motion vectors generated for it. Typically you would place Vector Warp right after an Optical Flow tool, since that tool produces the vectors it needs. Since Vector Warp rides the motion vectors to track movement throughout a clip, it shines when you want to put elements onto or take them off pliable surfaces such as cloth or skin. You might lean on this node to stick or strip logos on garments, drop a scar onto a person’s face, or lay texture across skin Inputs The Vector Warp node relies on a pair of inputs. Input: The orange image input takes a 2D image stream. That picture has to carry pre-generated Vector and Back Vector channels, whether produced by an Optical Flow node or stored in EXR format carrying vector channels. Texture: The green input takes a 2D still picture that serves as the texture for warping.

### Basic Node Setup

A Vector Warp node grabs the result of a clip plus a 2D still picture and bends the two together.

### A Vector Warp node

### Inspector

### The Vector Warp Controls tab

### Controls Tab

Through the Controls tab you can tune how the Vector Warp behaves.

- Set Frame: Treats whatever frame is showing as the reference frame. Hitting this button writes the Reference Frame value shown beneath it.
- Reference Frame: Pick the reference frame belonging to the Main sequence that the Map overlay was built against.
- Operation: Pick which operation you’d like to run. Generate Warp: Builds a warp map running from the reference frame out to the current frame, stored within the UV channels. Generate Warp + Map: Builds a warp map from the reference frame to the current frame and bends the map frame too. Apply Warp Map: Bends the map frame using a texture map produced earlier and fed in. UnWarp: Locks the map onto the reference frame and warps the main current frame backward so it matches the reference frame.
- Smooth UV: Averages each result against the surrounding UV values nearby. Handy for ironing out glitches and stray fluctuations that appear in the UV channels.
- Grid Overlay: Shows the warping as an overlay in the viewer.
- Merge Warp over BG: Shows the combined map picture sitting on top of the main image sequence.

### Common Controls

Settings Tab The Inspector’s Settings tab is repeated across the rest of the Optical Flow nodes too. A full breakdown of these shared controls sits at this chapter’s conclusion within the “The Common Controls” section.

### The Common Controls

Every node performing optical flow work carries a set of matching controls within the Inspector. What follows covers the controls that recur across the Optical Flow nodes.

### Inspector

### The Common Optical Flow Settings tab

### Settings Tab

You’ll find the Inspector’s Settings tab on each and every tool sitting in the Optical Flow category. Its controls stay uniform and behave the same way from one tool to the next. Blend The Blend control mixes between the picture the tool first received and the picture it ultimately produced after modification. With the blend set to 0.0, what leaves the tool matches what arrived exactly. Usually that makes the tool bypass processing altogether and pass the input directly through to the output. Process When Blend Is 0.0 Here the tool still runs even with the input value at zero. That comes in handy whenever this node’s processing is scripted to kick off some other task while the node’s own value sits at 0.0.

Red/Green/Blue/Alpha Channel Selector This quartet of buttons confines the tool’s effect to the color channels you pick. Such filtering usually kicks in once the tool has already done its processing. Say you turn off the Red button on a Blur tool: the blur first hits the picture, after which the red channel taken from the original input is laid back over the result’s red channel. Certain exceptions exist, like tools where switching off these channels makes the tool bypass that channel’s processing entirely. Tools behaving that way normally carry a matching set of RGBA buttons over on the tool’s Controls tab. Then the buttons sitting in the Settings and the Controls tabs match one another. Apply Mask Inverted Switching on the Apply Mask Inverted option flips the tool’s entire mask channel around. That mask channel is the merged outcome of every mask attached to or built inside a node. Multiply by Mask Picking this option multiplies the masked picture’s RGB values by the figures held in the mask channel. As a result every pixel left out of the mask (that is, set to 0) turns black/transparent. Use Object/Use Material (Checkboxes) Certain 3D applications can write to file formats carrying extra channels. The EXR file format in particular handles Object ID and Material ID channels, and those can serve as a mask driving the effect. These checkboxes decide whether such channels get used when they exist. Which specific Material ID or Object ID is targeted gets picked through the next batch of controls. Correct Edges You’ll only see this checkbox once the Use Object or Use Material checkboxes are switched on. It flips between the approaches used for handling object edges that overlap inside a multi-object picture. Switched on, the Coverage and Background Color channels come into play to isolate and refine the effect along the object’s edge. Leave this option off (or lack any Coverage or Background Color channels), and aliasing can show up along the mask’s edge. For deeper coverage, see Chapter 78, "Understanding Image Channels," found within the DaVinci Resolve Reference Manual; alternatively, turn to Chapter 18 which lives inside the Fusion Reference Manual. Object ID/Material ID (Sliders) With these controls you choose which ID builds a mask out of a picture’s object or material channels. Treat the Sample button just like the Color Picker: it pulls IDs straight from the picture shown in the view. That picture or stream needs to have come out of a 3D software package that bundled in those channels. Hide Incoming Connections Turning on this checkbox can tuck away the connection lines running in from upstream nodes, leaving the node tree looking tidier and simpler to follow. Switch it on and the Inspector shows blank fields for every input belonging to a node. Drop a connected node out of the node tree onto the blank field and that incoming connection line disappears, provided the node stays unselected within the node tree. Select that node in the node tree and the line shows up again.

Comments You use the Comments field to attach notes onto a tool. Click into the blank field and enter your text. Once a note exists on a tool, a tiny red square shows in the node’s lower-left corner while the full tile is on display, or a small text bubble icon turns up at the right whenever the nodes sit collapsed. To read the note inside the Node Editor, rest the mouse pointer over the node so the tooltip pops up. Scripts Each tool in Fusion offers three Scripting fields from the Settings tab. Every one holds edit boxes where you enter scripts that run while the tool renders. For fuller details on scripting nodes, refer to the Fusion scripting documentation.
