# Node color groups and channel propagation

Version: DaVinci Resolve 20.3 Reference Manual. Context: Understanding image channels.
[Chapter index](INDEX.md) / [Previous section](channels-in-fusion-and-types-of-channels-supported-by-fusion.md) / [Next section](premultiplication-rules.md)
<a id="source-2d-processing-nodes-color-coded-by-type"></a> <a id="source-a-simple-merge-node-composite"></a> <a id="source-adding-alpha-channels"></a> <a id="source-brown-mask-nodes"></a> <a id="source-channel-limiting"></a> <a id="source-dark-blue-3d-nodes"></a> <a id="source-how-channels-propagate-during-compositing"></a> <a id="source-node-colors-tell-you-which-nodes-go-together"></a> <a id="source-purple-particle-system-nodes"></a> <a id="source-rearranging-or-combining-channels"></a> <a id="source-skipping-channel-processing"></a> <a id="source-understanding-image-channels-part-2"></a> <a id="source-using-channels-in-a-composition"></a>

### Node Colors Tell You Which Nodes Go Together

Every node within Fusion carries out one kind of effect or operation. Such single-purpose nodes make decoding an intricate composition simpler when you study its node tree. Single-purpose nodes likewise make it simpler to concentrate on tuning particular adjustments, one by one, as you build an ever-growing tree. Since each Fusion node serves a specific function, they’re sorted by type to make tracking which nodes need what kinds of image channels coming in, and what image data each node is expected to put out, easier. The broad types get described below.

A node tree illustrating the principal groupings of node colors Blue MediaIn and Loader Nodes, and Green Generator Nodes The blue MediaIn nodes plus blue Loader nodes pull clips into a composite, whereas green Generator nodes build images. Each kind of node puts out RGBA channels (subject to the source and generator), and may optionally put out auxiliary channels for handling advanced compositing tasks.

Because they serve as image sources, both sorts of node can hook into a broad range of other nodes for crafting effects beyond merely 2D nodes. As an example, MediaIn nodes can just as well feed Image Plane 3D nodes when you’re doing 3D compositing, or feed pEmitter nodes switched to “Bitmap” for building various particle systems. Green Generator nodes can likewise be attached to many differing kinds of node, such as attaching a FastNoise node to a Displace 3D node to lay rippling effects onto 3D shapes. Shape nodes are green as well, though they have to attach to a dedicated set of gray modifier and render nodes (each of which starts with the letter “s” and shows up in the Shape category of the Effects Library).

### 2D Processing Nodes, Color Coded by Type

These take in the bulk of 2D processing and compositing tasks within Fusion, each of which works RGBA channels and forwards auxiliary channels. They include:

- Orange Blur nodes
- Olive Color Adjustment nodes (color adjustment nodes additionally concatenate with one another)
- Pink Paint nodes
- Dark orange Tracking nodes
- Tan Transform node (transform nodes additionally concatenate with one another)
- Teal VR nodes
- Dark brown Warp nodes
- Gray, which includes Compositing nodes as well as many other types.

On top of that, certain 2D nodes such as Fog and Depth Blur (sitting in the Deep Pixel category) take in and apply auxiliary channels like Z-Depth to build various perspective effects in 2D. TIP: Two 2D nodes that intentionally steer clear of touching alpha channel data are the Color Corrector node and the Gamut node. With the Color Correction node you can grade a foreground layer so it matches a background layer, all while sparing an alpha channel. The Gamut node lets you carry out color space conversions on RGB data from one gamut into another while sparing the alpha channel.

### Purple Particle System Nodes

These are the nodes that link up to build various particle systems, and they stay incompatible with other sorts of node until you bring in a pRender node that emits 2D RGBA and auxiliary data able to be composited with other 2D nodes and operations.

### Dark Blue 3D Nodes

These are 3D operations, producing and reshaping 3D data (auxiliary channels included) that stays incompatible with other sorts of node until run through a Renderer 3D node, which then emits RGBA and auxiliary data.

### Brown Mask Nodes

Masks emit single-channel images that may only be wired to one another (to combine masks) or to designated Mask inputs. Masks come in handy for marking transparency (Alpha masks), for marking which portions of a picture should be cropped away (Garbage masks), or for marking which portions of a picture a given node operation should touch (Effects masks).

### Using Channels in a Composition

Wire one node’s Output into another node’s Input and you pass every channel coming out of the upstream node into the downstream node. 2D nodes, which make up most of the simple image processing tasks within Fusion, carry all channel data along from node to node, RGB, alpha, and auxiliary channels included, no matter whether that node actually touches or uses a given channel. 2D nodes additionally tend to act on all channel data routed through them. As an example, wire a node’s output carrying RGBA and XYZ Normals channels into the input of a Vortex node, and every channel gets equally transformed by this operation’s Size, Center, and Angle parameters, the alpha and XYZ normals channels included, as the following screenshot shows.

(Top) The Normal Z channel as emitted from a rendered torus, (Bottom) That same Normal Z channel once its output gets wired into a Vortex node; observe the way this auxiliary channel distorts together with the RGB and A channels

This is fitting because, in most situations, you want assurance that every channel is transformed, warped, or adjusted as one. Shrinking the image without shrinking the alpha channel right alongside it is something you wouldn’t want, and the same holds for the bulk of other operations. On the flip side, certain nodes deliberately pass over particular channels where that makes sense. As an example, the Color Corrector and Gamut nodes, both built to alter RGB data specifically, leave auxiliary channels untouched. That makes them handy for color-matching foreground and background layers you’re compositing, with no worry that you’re changing the depth information traveling with that layer. TIP: Should you be doing something exotic and you genuinely want to act on a channel a given node usually leaves alone, you can always reach for the Channel Booleans node to reassign the channel. When applying this to a single image, wiring that image into the background input of the Channel Booleans node matters, so the alpha and auxiliary channels get handled properly.

### Channel Limiting

The bulk of nodes carry a row of Red, Green, Blue, and Alpha buttons within the Settings tab of that node’s Inspector. Those buttons let you keep any mix of these channels from being touched by that node.

A Transform node’s channel limiting buttons within its Settings panel, configured so that just the Green channel gets touched As an example, were you wanting the Transform node to touch only an image’s green channel, you can switch off the Red, Blue, and Alpha buttons. The upshot is that this operation works the green channel, while the red, blue, and alpha channels copy straight across from the node’s input to the node’s output, bypassing that node’s processing so they stay untouched.

Applying a Transform effect to just the image’s green color channel

### Skipping Channel Processing

Behind the scenes, most nodes work every channel first, then afterward copy the input image across to the output for whichever channels have been enabled. Today’s workstations run so fast that you don’t usually notice this, yet there are certain nodes where switching off a channel genuinely makes that node skip processing that channel altogether. The nodes that behave this way carry a linked row of Red, Green, Blue, and Alpha buttons on a separate tab within the node. In those cases, the Common Control channel buttons are instanced to the channel buttons sitting elsewhere in the node. Blur, Brightness/Contrast, Erode/Dilate, and Filter serve as examples of nodes that each carry RGBA buttons in the main Controls tab of the Inspector, on top of the Settings tab.

### Adding Alpha Channels

A great deal of visual effects compositing comes down to setting a foreground subject atop a background. Arguably the most basic approach is by way of an alpha or matte channel. Where a clip holds no alpha channel, you add one through keying or rotoscoping. Although more specific methods get covered thoroughly in later chapters, here’s an illustration of how Fusion handles this. To pull an alpha matte out of a green screen image, you typically wire the image’s RGB output into the “Input” input of a Keyer node such as the Delta Keyer, then lean on the keyer’s controls to pull the matte. The Keyer node drops in the generated alpha channel right beside the RGB channels on its own, so the output comes out as RGBA automatically. Then, once you wire the keyer’s output into a Merge node to composite it atop another image, the Merge node automatically knows to draw on the embedded alpha channel arriving at the foreground input to build the composite you want, as the following screenshot shows.

A basic keying node tree; observe that just a single connection joins the DeltaKeyer with the Merge node Rotoscoping, that is hand-drawing a mask shape with a Polygon or other Mask node, is a further technique used to make the matte channel. The node tree for this job can be arranged many ways, but the most straightforward setup is just wiring a Polygon or B-Spline mask node into the Effect Mask input of a MediaIn or Loader node. TIP: While rotoscoping, you’re best off leaving the Mask node unhooked from the image as you draw the shape. Doing so lets you watch the MediaIn node while drawing. Wire the Matte node up once the shape is drawn.

A basic rotoscoping arrangement where a Polygon node feeds straight into a MediaIn’s Effect Mask input.

Either way, you can observe how the node tree’s knack for moving one channel or several channels of image data across a single connection line eases the compositing process.

### How Channels Propagate During Compositing

Images get blended or composited together by way of the Merge node. The Merge node accepts two RGBA inputs marked “Foreground” (green) and “Background” (orange) and fuses them into one RGB output (or RGBA where both the foreground and background input images carry alpha), with the foreground image up front (or on top, depending on what you’re doing), and the background image, you guessed it, behind.

### A simple Merge node composite

Auxiliary channels, by contrast, get handled in a far more specific manner. Composite two image layers through the Merge node, and auxiliary channels travel through only the image wired to the background input. The reasoning is that across most CGI composites, the background tends to be the CG layer carrying auxiliary channels, while the foreground is a liveaction green screen plate. Since most compositions employ several Merge nodes, taking care over how you wire each Merge node’s background and foreground inputs pays off, so the right channels move along properly. TIP: Merge nodes can equally fuse the foreground and background inputs using Z-Depth channels through the “Perform Depth Merge” checkbox, where every pair of pixels gets compared. Which one comes out front rides on its Z-Depth rather than on the wired input.

### Rearranging or Combining Channels

Lastly, and far from least, you can also reshuffle and re-blend channels however you require, by way of one of four different node operations. As an example, you might want to pair the red channel from one image with a second image’s blue and green channels to mint an entirely different channel mix. Or you might want to grab the alpha channel from one image and fold it together with a second image’s alpha channel in assorted ways, adding, subtracting, or applying other intersection operations to craft a highly specific blend of the two.

The following nodes are used to re-combine channels in different ways:

- Channel Boolean: A 3D node whose purpose is remapping and reworking the channels of 3D materials through an assortment of straightforward pre-defined math operations.
- Channel Booleans: Serves to shuffle or reorder RGBA and auxiliary channels inside one input image, or across two input images, producing a single output image. Should you wire only one image into this node, that image has to feed the background input so that everything functions properly.
- Copy Aux: The Copy Aux node serves to remap channels between RGBA channels and auxiliary data channels inside one 2D image. For the most part the Copy Aux node is a convenience node, since the same copying is achievable, with extra effort (and flexibility), through a Channel Booleans node.
- Matte Control: Built to carry out any mix of the following: (a) reassembling mattes, masks, and alpha channels in assorted ways, (b) reworking alpha channels by way of dedicated matte controls, and (c) writing alpha channels into the RGB stream of the image feeding the background input ahead of compositing. Particular channels can be copied from the foreground input over to the background input for use as an alpha channel, or you can hook masks up to the garbage matte input to serve as alpha channels too.
