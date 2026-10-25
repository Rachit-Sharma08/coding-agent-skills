# Channels in Fusion and types of channels supported by Fusion

Version: DaVinci Resolve 20.3 Reference Manual. Context: Understanding image channels.
[Chapter index](INDEX.md) / [Next section](node-color-groups-and-channel-propagation.md)
<a id="source-alpha-channels"></a> <a id="source-always-connect-the-background-input-first"></a> <a id="source-auxiliary-channels"></a> <a id="source-channels-in-fusion"></a> <a id="source-fusion-node-connections-carry-multiple-channels"></a> <a id="source-inputs-require-specific-channels"></a> <a id="source-node-inputs-and-outputs"></a> <a id="source-rgb-color-channels"></a> <a id="source-single-channel-masks"></a> <a id="source-types-of-channels-supported-by-fusion"></a> <a id="source-understanding-image-channels"></a> <a id="source-understanding-image-channels-part-1"></a> <a id="source-using-multiple-inputs"></a>

### Understanding Image Channels

The aim of this chapter is to clear up the way Fusion treats image channels and, along the way, demonstrate how various nodes must be wired together to land the outcomes you’re after. On top of that, it unravels the puzzle of premultiplication and lays out a thorough account of how Fusion can both consume and even produce auxiliary data.

### Channels in Fusion

Fusion brings some inventive approaches to handling the assorted channels of image data that today’s compositing workflows involve. The opening look this chapter gives at color and data channels, and the way various nodes and operations act on them, is a worthwhile starting point for learning to perform paint, compositing, and effects inside Fusion. Should you be a newcomer to compositing, or fresh to how Fusion works, skipping this chapter is risky, since it lays down a firm grounding for grasping how to control image data dependably while you operate inside this capable environment.

### Types of Channels Supported by Fusion

A digital image can be split into individual streams of image data named Channels, with each one holding a particular sort of image data. The nodes that carry out various image processing tasks usually rely on certain channels in order to deliver dependable outcomes. The three usual color channels of red, green, and blue are likely already known to you, yet plenty more exist. What follows describes the assorted channel kinds that Fusion handles.

### RGB Color channels

For any still photo or movie clip, the red, green, and blue channels add together additively to portray all that visible light lets us perceive. Viewed on its own, each one of these three channels reads as a grayscale image. Brought together additively, they make up a full-color image.

### Alpha Channels

A fourth channel baked in to set varying degrees of transparency across an RGB image is what an alpha channel is. Such alpha channels usually come embedded inside RGB images produced by computer graphics software. Within Fusion, solid regions are shown as white, whereas transparent regions show as black. Across the grayscale range, lighter values read as more opaque and darker ones as more transparent. Should you bring in an alpha channel from some other application where this scheme runs the opposite way, don’t worry. Any node able to make use of an alpha channel can equally well invert it.

### Single-Channel Masks

Though they resemble alpha channels, mask channels are single channel images that sit outside any RGB image and are usually built by Fusion inside one of the Mask nodes on offer. What sets Mask nodes apart is that they carry forward single-channel image data marking which regions of a picture ought to be solid and which ought to be see-through. That said, masks can equally specify which portions of an image a given operation should touch and which it should leave alone. The intended purpose of mask channels is connecting them to particular mask inputs on nodes such as the Effect Mask, Garbage Mask, and Solid Mask inputs.

### Auxiliary Channels

Auxiliary channels (treated more fully further along in this chapter) name a class of special-purpose image data that generally surfaces 3D data in a form usable within 2D composites. As an illustration, Z-Depth channels record how deep each pixel of an image sits along a Z axis, whereas an XYZ Normals channel records the facing (pointing up, pointing down, or pointing left or right) of every pixel in an image. Because auxiliary channel data comes out of rendering 3D images, it commonly travels alongside, or sits embedded within, RGB images that 3D modeling and animation packages produce. Such channels may equally be produced inside Fusion through the Renderer 3D node, which takes a 3D scene you have built and lit and emits it as 2D RGBA channels, optionally bundled with auxiliary channels.

What makes auxiliary data worthwhile is that 3D rendering eats up computation and runs slowly, so emitting descriptive details about a 3D image already rendered lets compositing artists apply elaborate changes in 2D. Motion blur can be added, relighting can be carried out, and depth-based compositing can be done far quicker than rendering the 3D source over and over again. TIP: Any single channel of a node can be inspected on its own through the Color drop-down menu within the viewer. Opening that Color drop-down menu surfaces a roster of every channel inside the node currently selected, covering red, green, blue, or auxiliary channels.

### Fusion Node Connections Carry Multiple Channels

In Fusion’s Node Editor, the links that hand image data from one node along to the next can convey several channels of image data at once. What that means is one link might carry RGB, or RGBA, or RGBAZ-Depth, or perhaps Z-Depth on its own, hinging on which Input you wire into and what the node does. Take the following example, where the pair of MediaIn nodes put out RGB data. The Delta Keyer, though, builds an alpha channel and joins it with MediaIn2’s RGB image. The RGB-A from the Delta Keyer turns into the foreground image the Merge node can draw on to assemble a two-layer composite.

Here the foreground input of the Merge node draws on the alpha channel the Delta key produced to do its compositing. NOTE: The node trees pictured throughout this chapter may show MediaIn nodes belonging to DaVinci Resolve’s Fusion page; nonetheless, Fusion Studio Loader nodes can be swapped in unless something says otherwise. Pushing several channels down a single connection line keeps Fusion node trees easy to read, yet it equally means you have to stay aware of which nodes handle which channels so you’re sure the right image data reaches the right operations.

### Node Inputs and Outputs

Out of the box, MediaIn nodes within the Fusion page and Loader nodes within Fusion Studio emit RGBA channels. Wire one node’s output into another node’s input and the live channels travel from the upstream node down to the downstream node, which then works the image per that node’s purpose. A node input accepts a connection from only one node output at any given moment. Take this plain example, where a MediaIn node’s output is wired to the input of a Highlight node to produce a sparkly highlight effect.

Within the Fusion page, a MediaIn node feeds a Highlight node, which in turn feeds a MediaOut node. As you link nodes, the channels a node’s output carries stay identical however many times that output gets “branched.” You cannot route one channel down one branch and a separate channel down another branch.

Though the MediaIn node’s output gets branched, both inputs still receive identical RGB channels.

### Using Multiple Inputs

The majority of nodes carry two inputs, one taking RGBA and a second taking an effect mask you can optionally apply to confine that node’s effect to a certain region of the image. Some nodes, though, carry three or even more inputs, and it matters that you feed the right image data into the right input to land the result you want. Wire one node’s output into another node’s input and see nothing change, and odds are you wired into the wrong input. As an example, the MatteControl node carries a background input plus a foreground input, each accepting RGBA channels. It additionally carries SolidMatte, GarbageMatte, and EffectsMask inputs that take alpha or mask channels to adjust how transparent the Node’s output is. To pull off the very common task of having a MatteControl node build an alpha channel through a Polygon node for rotoscoping an image, you have to be sure the Polygon node feeds into the GarbageMatte input to land the right result. That GarbageMatte input is set up by default to modify the foreground image’s alpha channel. Hook it into any other input and your Polygon mask might not behave as expected.

For rotoscoping, a Polygon node wired into a MatteControl node’s GarbageMatte input

For another case, the DeltaKeyer node carries a primary input (marked “Input”) that takes RGBA channels, but it additionally carries three Matte inputs. Those SolidMatte, GarbageMatte, and EffectsMask inputs on the Delta Keyer take alpha or mask channels to reshape the matte being pulled from the image in assorted ways.

The DeltaKeyer combines the multiple mask nodes in different ways. Hover your pointer over any node’s input or output, and a tooltip shows up in the Tooltip bar along the foot of the Fusion window, telling you what that input or output does, so you’re steered toward the right input for the task. Linger a moment more and a further tooltip surfaces right inside the Node Editor.

(Left) Within the Tooltip bar, the node input’s tooltip, (Right) Within the Node Editor, the node tooltip Connecting to the Correct Input While wiring nodes, dragging a connection line off one node’s output and letting it go squarely on the body of a second node forms a link to that node’s default input, which is typically the “Input” or “Background” input.

Shown side by side, letting a connection go onto a node’s body so it links to that node’s primary input

That said, let a connection line go directly atop a particular input, and you’ll wire into that input, so staying conscious of where you drop connection lines as you piece different node trees together is important.

Shown side by side, letting a connection land on one particular node input; observe how the inputs reshuffle themselves afterward so the node tree stays neat-looking TIP: Should you keep the Option key pressed while dragging a connection line off one node onto another, and hold that Option key down as you let the pointer’s button go to drop the link, a menu pops up letting you select by name which particular input to wire into.

### Inputs Require Specific Channels

Typically you’re blocked from wiring a node’s output into another node or node input that isn’t compatible with it. As an example, attempt to wire a Text3D node’s output straight into a plain Merge node’s input and it won’t go; 3D nodes don’t output RGB images, they output 3D geometry data, so you first have to wire into a Renderer3D node that builds the RGB output suited to 2D compositing tasks. Other times, feeding the wrong image data into the wrong node input throws no error at all, it simply doesn’t yield the result you anticipated, forcing you to troubleshoot the composition. Should that befall you, look over the Fusion Effects section of this manual to find out whether the node you’re trying to wire into carries any restrictions on how it has to be hooked up. TIP: This chapter aims to address many of the easily overlooked exceptions to node connection that matter for you to grasp, so resist skimming too quickly.

### Always Connect the Background Input First

Plenty of nodes blend images in assorted ways through “background” and “foreground” inputs. The Merge node, the Matte Control node, and the Channel Booleans node count among common examples of this. The coloring of a node’s inputs can steer you toward making the right hookups. As an instance, background inputs are forever orange and foreground inputs are forever green.

The first time you wire any node’s output into a multi-input node, you generally want the background input wired up first. That happens for you automatically the first time you drop a connection line onto the body of a fresh multi-input node. The orange-colored background input almost always gets wired first (the exception being Mask nodes, which always wire into the first open Mask input). That’s welcome, because building the habit of always wiring the background input first is what you want. Should you wire into just one input of a multi-input node and skip the background input, you may discover the results aren’t what you wanted. The reason is that every multi-input node assumes the background is wired before anything else, so the internal links and math the node uses can stay predictable. TIP: The sole node where you can safely wire the foreground input ahead of the background input is the Dissolve node, a special node usable either to dissolve between two inputs or to switch automatically between two inputs of differing duration.
