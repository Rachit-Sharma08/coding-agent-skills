# Attaching masks to an image for rotoscoping and a mattecontrol node

Version: DaVinci Resolve 20.3 Reference Manual. Context: Rotoscoping with masks.
[Chapter index](INDEX.md) / [Previous section](introduction-to-masks-and-polylines-and-mask-nodes.md) / [Next section](polyline-creation-modes-and-click-append.md)
<a id="source-attaching-masks-to-an-image-for-rotoscoping"></a> <a id="source-combining-multiple-masks"></a> <a id="source-creating-and-editing-polylines-indepth"></a> <a id="source-effects-mask-inputs"></a> <a id="source-garbage-matte-inputs"></a> <a id="source-mask-inputs-on-other-nodes"></a> <a id="source-pre-masking-inputs"></a> <a id="source-selecting-a-specific-polyline"></a> <a id="source-solid-matte"></a> <a id="source-the-invert-and-solid-options"></a> <a id="source-the-polyline-toolbar"></a> <a id="source-the-polyline-toolbar-1"></a> <a id="source-using-a-mattecontrol-node"></a>

### Attaching Masks to an Image for Rotoscoping

You'll usually wire up a Mask node, such as a Polygon node, in one of two ways so that it tacks an alpha channel onto an image for compositing further down the node tree.

### Using a MatteControl Node

The chief node for blending masks in assorted ways and dropping the outcome into an image stream is the MatteControl node. You hang the MatteControl node downstream of whichever node outputs the image you mean to rotoscope. Typically you'll wire a Polygon or B-Spline node into the Garbage Matte input of the MatteControl node so the spline serves as an alpha channel.

Feeding a Polygon node to a MatteControl node to perform rotoscoping With this arrangement, you load the MatteControl node into the viewer and pick the Polygon node to reveal its controls, letting you draw and reshape a spline while watching the image you're rotoscoping. Which portion of the image turns transparent is set through the MatteControl node's Garbage Matte > Invert checkbox. Connecting a Mask to a MediaIn or Loader Node's Input Slightly simpler, this route hinges on your awareness that one node can be viewed while a different node is being tweaked, even with that other node disconnected. Add a free-standing Mask node like a Polygon or B-Spline node, then, with the Mask node selected, drop a MediaIn or Loader node straight into the viewer, and you can draw a spline to rotoscope the image. Once rotoscoping is done, simply route the output of the Polygon node into the input of the Loader node, and that node gains an alpha channel automatically.

Rotoscoping a MediaIn node using a disconnected Polygon node

Wiring a Polygon node into a MediaIn node so its spline serves as the alpha channel

TIP: Wire a Mask node into a MediaIn or Loader node's effect input with no shapes drawn yet, and that mask puts out full transparency, so right away the image the MediaIn or Loader node outputs goes entirely blank. That's the reason that, to rotoscope by wiring a mask into the input of a MediaIn or Loader node, you must first work inside a disconnected Mask node. The instant your drawn shape is closed, connect that Mask node into the MediaIn or Loader's input, and you're good to go.

### Combining Multiple Masks

Masks are built to be stacked one after another, with each Mask node serving as one more layer of masking. As soon as a Mask node's input attaches to another mask, a Paint Mode drop-down menu shows up, letting you pick how the two masks should be blended.

Combining multiple Polygon nodes one after the other in the node tree

The Paint Mode parameter in the Polygon node Inspector parameters

Merge is the default choice, but you can also pick Subtract, Minimum, Maximum, Multiply, or whatever other operation delivers the mask boolean interaction you're after. On top of that, a pair of Invert and Solid checkboxes let you fine-tune how the current mask blends with the one preceding it.

### The Invert and Solid options

### Mask Inputs on Other Nodes

Because masks serve so many purposes, different nodes offer several categories of mask input to cover those varied uses. As it happens, you can usually wire either masks or mattes into a mask input to make use of that input's capability. TIP: Pick a node that has an empty effect mask input, then add a Mask node, and it hooks straight into the open effect mask input on its own.

### Effects Mask Inputs

Nearly every node in Fusion carries an Effect mask input (colored blue) that lets you decide which parts of the image that node does or doesn't affect.

A Blur node with a Polygon node masking its effect When a mask (or matte) is wired in through an input, it is really applied "post effect," meaning the node first runs its effect over the whole image and then the mask trims the result by copying unaffected image data back over from the input. Plenty of nodes accept effects masking, but on a few it does not apply—namely Savers, Time nodes, and the Resize, Scale, and Crop nodes. TIP: Effects masks set the domain of definition (DoD) for that effect, boosting its efficiency.

A Polygon node serving as the mask that confines what the Blur node affects

### Pre-Masking Inputs

A pre-mask input (whose name is generally particular to each node that uses one) differs from an effect mask in that the node consults it before running the effect. That usually lets the node render faster and turn out a more lifelike result. With the Highlight and the Glow nodes, a pre-mask pens the effect into certain image areas yet lets the effect's result spill out past the mask's edges. Pre-masking's upside is that it lets glows and highlights behave more like they do in the real world. Picture an actor shot in front of a bright light: the light triggers a glow inside the camera lens. Since the glow occurs in the lens, the actor's luminance gets affected even though the glow originates only from the light. On the DVE node, a pre-mask serves to transform only a selected slice of the picture, sparing the parts that fall beyond the mask. That proves useful when you mean to transform just a single region of the picture.

### Garbage Matte Inputs

A Garbage Matte input (usually colored gray) exists to shut out light stands, rigging, and boom microphones that creep into masks being pulled through blue-screen and green-screen keys. In the example that follows, a lighting stand on the left is wiped from the image by a B-Spline node's mask wired into the Garbage Matte input of the DeltaKeyer node.

Here a B-Spline node feeds the Garbage Matte input on a DeltaKeyer node, wiping out a light stand sitting at frame left TIP: You can drop a mask node onto the Effect/Solid/Garbage Matte inputs of a keyer node in a hurry by right-clicking that node's header bar in the Inspector and picking whichever mask node you want from the Effect Mask, SolidMatte, and GarbageMatte submenus. Whether a garbage matte hits a keying node as opaque or transparent is your call in the Inspector for the node it's wired to.

### Solid Matte

A Solid Matte input (colored white) is meant to plug unwanted gaps in a matte, often via a more loosely pulled key that yields a dense matte with eroded edges, although a polygon or mask paint could fill that role too. In the example below, a soft key meant to keep the gentle edges of the talent's hair leaves gaps in the mask of the woman's face, but bringing in another

DeltaKeyer to build a solid matte for the key's interior, one that can be eroded smaller than the original matte, lets you plug the gaps while keeping the soft edges undisturbed. People sometimes call this a hold-out matte.

Plugging gaps in the mask the DeltaKeyer1 node pulled (left) by way of a harder, eroded key from DeltaKeyer2 wired into the SolidMatte input on DeltaKeyer1 (right)

### Creating and Editing Polylines In‑Depth

This section digs into the Polygon node's capabilities thoroughly.

### The Polyline Toolbar

Any time a node holding one or more polylines is selected, the polyline appears on every viewer and the Polyline toolbar lines up along the side of each viewer. The toolbar holds a handful of buttons that put switching polyline modes and options within easy reach.

### The Polyline toolbar

Hover the pointer over any button on the Polyline toolbar and a tooltip spelling out that button's job pops up. Clicking a button acts on the currently active polyline or on the selected polyline points, depending which button it is. You can resize the toolbar icons, attach labels to the buttons, or otherwise tweak how the toolbar looks to make polylines simpler to work with. Every one of these options turns up when you right-click the toolbar and pick from the choices shown in the contextual menu.

### Selecting a Specific Polyline

Selecting several Mask nodes in the Node Editor can leave more than one polyline in the viewer at the same time, so being able to flip between polylines with ease matters. To make a polyline active, do one of the following:

- Click one of the polyline's control points or segments.
- Press Tab and Shift-Tab to cycle between available polylines.
- Right-click inside the viewer and, from the Controls > Select menu, pick the polyline you want by its name.
