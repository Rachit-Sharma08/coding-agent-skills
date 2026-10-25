# Selecting and viewing nodes in the inspector and versioning nodes

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing parameters in the inspector.
[Chapter index](INDEX.md) / [Previous section](fusion-inspector-and-brightness-contrast-controls.md) / [Next section](inspector-comments-and-control-context-menu.md)
<a id="source-apply-mask-inverted"></a> <a id="source-blend"></a> <a id="source-motion-blur"></a> <a id="source-multiply-by-mask"></a> <a id="source-parameter-tabs"></a> <a id="source-process-when-blend-is-00"></a> <a id="source-redgreenbluealpha-channel-checkboxes"></a> <a id="source-scripting"></a> <a id="source-selecting-and-viewing-nodes-in-the-inspector"></a> <a id="source-skipping-channel-processing"></a> <a id="source-the-parameter-tabs-of-the-blur-node"></a> <a id="source-the-parameter-tabs-of-the-delta-keyer-node"></a> <a id="source-the-settings-tab"></a> <a id="source-the-settings-tab-in-the-inspector"></a> <a id="source-versioning-nodes"></a>

### Selecting and Viewing Nodes in the Inspector

You click Inspector headers to select nodes, to open and close node parameters, and for other purposes. Ways to work with headers:

- To select a node using the Inspector header: With several nodes selected, clicking a node's Inspector header in the Inspector promotes it to active node. Once it's the actively selected node, both its Inspector header and its counterpart in the Node Editor turn orange, and its parameters are revealed.
- To load a node into the viewer using the Inspector header: Drag a node's header onto one of the viewers to see it there.
- To view a node's splines with the control header: To bring a node's animated curves into the Spline Editor, drag its Inspector header onto the Spline Editor. Every animated spline tied to that node's parameters then appears automatically.
- Using Header Controls

Because of the controls sitting in each node's Inspector header, simple jobs go quickly. To turn nodes off and on: A toggle switch sits left of the name on every Inspector header and serves to enable or disable that node. A disabled node hands image data straight from its upstream neighbor to its downstream neighbor untouched. To change the Inspector header name: Next along is the name of the node that header belongs to. Rename it by right-clicking the Inspector header to bring up contextual menu commands much like the ones you get right-clicking a node in the Node Editor, then choosing Rename. As an alternative, select an Inspector header and hit F2 to rename it. A Rename dialog opens, where you key in a fresh name and click OK (or press Return). To color-code nodes: From a color pop-up menu you can apply any one of 16 colors as a code. Pick Clear Color to send that node back to its default color. To version nodes: Switch on the Versions button and a Version bar carrying six buttons shows up. The section after this one covers versioning. To pin Inspector controls: Click the Pin button and a node's parameters get "pinned" in the Inspector, holding their spot even once you've deselected the node. There's no limit on how many nodes you pin, yet a bigger count forces more scrolling through the Inspector to find every parameter. To lock nodes: Click the Lock button and that node is locked, barring any changes to it. To reset Inspector controls: At the far right end of the Inspector header lives a Reset button, which restores the whole node to its default settings.

### Versioning Nodes

Every button can hold its own distinct set of parameter values for that node, which makes saving and comparing as many as six settings versions per node simple. Each version is stored together with its node in the Node Editor so you can reuse it later.

The Version bar sitting below an Inspector header once versions are enabled An orange underline marks whichever version is selected at the moment, meaning the version your composition is actively drawing on. To discard a version you no longer want, right-click its number and choose Clear from the contextual menu.

### Parameter Tabs

Below the Inspector header runs a row of panel tabs shown as themed icons. Click any one of these icons to open its own tab of parameters, typically gathered by purpose. A basic node like the Blur node has just two tabs, the first holding every parameter to do with blurring the image, the second being the Settings tab.

### The parameter tabs of the Blur node

Nodes of greater complexity carry additional tabs holding more parameter groups. The Delta Keyer, as an example, has seven tabs that split apart its Key, Pre-Matte, Matte, Fringe, Tuning, and Mask parameters alongside the mandatory Settings tab. Those tabs stop the Delta Keyer from becoming one enormous scrolling list of settings and help you track which stage of keying you're refining as you go.

### The parameter tabs of the Delta Keyer node

### The Settings Tab

A Settings tab ships with every node in Fusion. It holds a collection of standard controls present on practically every node, though a handful of nodes carry special Settings tab controls the rest don't have.

### The Settings tab in the Inspector

While the controls below appear on most nodes, a few are particular to certain ones. Motion Blur settings, for one, serve no function on a Color Space node.

### Blend

Every node except the Loader, MediaIn, and Generator nodes carries the Blend control. Its job is to mix the node's untouched input image against the node's fully processed result. At a blend value of 0.0, the output image matches the input image exactly. Normally that makes the node bypass processing altogether, passing the input directly through to the output. This node's default is 1.0, so the node sends out the modified image at 100%.

### Process When Blend is 0.0

Even when the input value sits at zero and the output image equals the input, this checkbox makes the node process anyway. That can help on certain nodes or third-party plugins that carry values across from one frame to the next. Leave this checkbox off on nodes that behave that way and the node skips processing whenever Blend is at 0, which yields wrong results on the frames that follow.

### Red/Green/Blue/Alpha Channel Checkboxes

A row of RGBA boxes sits in the Settings tab of most nodes. Ticking these boxes lets you keep any mix of those channels from being touched by the node.

A Transform node's channel-limiting boxes, in its Settings panel, configured to act on the green channel alone. Say you wanted the Transform node to act on an image's green channel alone; you'd switch off the Red, Blue, and Alpha checkboxes. The green channel then runs through this operation, while the red, blue, and alpha channels travel straight from the node's input to its output, bypassing that node's processing so they stay untouched.

Applying a Transform effect to nothing but the image's green color channel

### Skipping Channel Processing

Behind the scenes, most nodes really do process all of the channels first and only afterward copy the input image to the output for whichever channels you've unchecked. Today's workstations are quick enough that you rarely notice this, but a few nodes really will skip a channel's processing entirely when you deselect it. Such nodes carry a linked group of Red, Green, Blue, and Alpha boxes on a separate tab within the node.

On the Blur node's Controls tab, the channel boxes signal that any disabled channel is skipped outright so rendering time is saved.. When that's the case, the Common Control channel boxes are instanced to the channel boxes located elsewhere in the node. Blur, Brightness/Contrast, Erode/Dilate, and Filter are among the nodes that carry RGBY checkboxes on the Inspector's main Controls tab as well as on the Settings tab.

### Apply Mask Inverted

Enable the Apply Mask Inverted checkbox and any mask wired into that node's Effect Mask input is flipped. TIP: The Apply Mask Inverted checkbox acts on effects masks alone; garbage masks are left out.

### Multiply By Mask

Choosing this option multiplies the masked image's RGB values by the values of the Mask channel. The upshot is that every image pixel left out of the mask (the ones set to 0) turns black. The result is a premultiplied image. Use Object/Use Material (For Masking) Certain 3D animation and rendering packages can write to file formats carrying auxiliary channels. The OpenEXR file format, notably, holds Object ID and Material ID channels, and either one can serve as the mask for an effect. Whether those channels get used when present is decided by this checkbox. Exactly which Material ID or Object ID is targeted is set with the next group of controls.

- Sample Controls: The Sample Controls show up only after the Use Object or Use Material checkbox is turned on. With them you pick which ID builds a mask from the Object or Material channels stored in the image. The Sample button grabs IDs out of the image in the viewer the same way the Color Picker grabs a color: hold the left mouse button down on the Sample button, then drag across to the viewer onto the part of the image you mean to select. Whatever image or sequence you use must have been rendered out of a 3D software package with those channels baked in.
- Correct Edges: The Correct Edges checkbox shows up only after the Use Object or Use Material checkbox is turned on. With the Correct Edges checkbox enabled, the Coverage and Background Color channels go to work separating and refining the effect around an object's edge. With it disabled (or with no Coverage or Background Color channels on hand), the mask edge may show aliasing.

### Motion Blur

On nodes able to introduce motion, Transform nodes and Warp nodes among them, the Motion Blur checkbox switches that node's motion blur rendering on or off. With this checkbox on, the node's estimated motion drives the blur a virtual camera shutter would produce. Switch the control off and no motion blur is generated. While Motion Blur stays off, no extra controls show up. Switch Motion Blur on, though, and four more sliders appear for shaping the look of the motion blur you're applying to that node. Quality: Sets how many samples go into building the blur. At the default of 2, two samples are placed to either side of an object's real motion. Bigger numbers smooth the result but lengthen the render time. Shutter Angle: Governs the angle of the virtual shutter that yields the Motion Blur effect. Wider angles add blur but push up the render times. Setting 360 is the same as leaving the shutter open across one full frame's exposure. You can go higher, which opens the door to interesting effects. This slider defaults to 100. Center Bias: Shifts where the center of the motion blur sits. Tuning the value makes trail-type effects possible. Sample Spread: Tuning Sample Spread changes the weighting handed to each sample. That alters how bright the samples chosen with the Quality slider come out.

### Scripting

Every node carries Scripting fields holding one or more editable text fields where you can drop in scripts that run as that node renders. Turn to the Scripting documentation for more on what this tab contains.
