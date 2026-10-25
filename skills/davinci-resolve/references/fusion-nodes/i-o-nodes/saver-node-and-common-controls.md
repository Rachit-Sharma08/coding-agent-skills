# Saver node and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Saver node, Common controls.
[Chapter index](INDEX.md) / [Previous section](saver-node-saver-export-tab.md) / [Saver Node SV](mediaout-node-and-saver-node.md)
<a id="source-common-controls"></a> <a id="source-common-saver-settings-inspector"></a> <a id="source-inspector-2"></a> <a id="source-settings-tab"></a> <a id="source-the-common-controls"></a>

### Common Controls

Settings Tab Because the Settings tab controls are shared between the Loader and Saver nodes alike, you’ll find them described in the “The Common Controls” section at this chapter’s end. Clipping Mode This menu — sometimes thought of as source image clipping — lays out how the image’s edges ought to be handled.

- Frame: By default, the Frame setting clips to whichever parts of the image fall inside its visible dimensions. Any infinite-workspace behavior gets broken. Where the upstream DoD is smaller than the frame, whatever areas are left in the frame count as black/transparent.
- None: No source image clipping at all happens with this setting. So any data ordinarily called for beyond the upstream DoD counts as black/transparent. Mind that this may spawn humongous images which can eat up a considerable amount of disk space. So reach for this option only where it’s truly needed.

To learn more about ROI, DoD, and Infinite Workspace, turn to Chapter 69, "Using Viewers." within the DaVinci Resolve Reference Manual, or to Chapter 7 within the Fusion Reference Manual. Save Alpha to Color Switch this control on and the Alpha channel gets written into the color channels as a grayscale image. Doing so wipes out any color information already there. Color Space Type Setting the output file’s Color Space is what this menu does, so that you could, say, color space convert images from linear to Rec709, and the like, thereby putting out linear EXRs, 709 Quicktimes, and so on from one source. Nothing gets converted within the Comp; only the images written to disk get converted.

- Auto: Carries along whatever metadata might sit in the rendered image.
- Space: Lets the user fix the color space according to the output format.

Curve Type Picking a Gamma curve for the rendered file is the job of this menu. Having set the gamma curve type, you may opt to apply the curve for output.

- Auto: Carries along whatever metadata might sit in the incoming image.
- Space: Lets the user fix the gamma curve according to the chosen file format.
- Log: Brings up the Log/Lin settings, much like the Cineon Log node.

For fuller detail on the Log settings, turn to Chapter 99, “Film Nodes,” within the DaVinci Resolve Reference Manual, or to Chapter 39 within the Fusion Reference Manual. Apply Curve Depending on which Curve Type you chose, or on the Gamma Space turned up in Auto mode, the matching Gamma Curve gets applied, which in effect converts away from a linear working space.

### The Common Controls

Across the Inspector, I/O nodes have a number of identical controls in common. The controls shared among I/O nodes are what this section lays out.

### Inspector

### Common Saver settings inspector

### Settings Tab

You’ll find the Inspector’s Settings tab on the Loader, Saver, MediaIn, and MediaOut nodes. Its controls stay consistent and behave the same on each tool, though a handful of parameters live on only certain nodes — they’re still covered here. Blend What the Blend control does is mix the tool’s original image input together with whatever modified output image the tool finally produces. Set the blend value to 0.0 and the outgoing image matches the incoming one exactly. Ordinarily this has the tool bypass processing altogether, copying the input straight across to the output. Process When Blend Is 0.0 The tool runs even where the input value is zero. That can come in handy if this node’s processing is scripted to set off another task while the node’s value sits at 0.0. Red/Green/Blue/Alpha Channel Selector These four buttons serve to confine the tool’s effect to certain color channels. The filter usually goes on once the tool has finished processing. As an example, deselect the red button on a Blur tool and the blur first goes onto the image, after which the red channel from the original input gets copied back over the result’s red channel. There are a few exceptions — tools where deselecting these channels has the tool skip processing that channel outright. Tools that behave this way generally carry a matching set of RGBA buttons on their Controls tab. In that case, the buttons on the Settings and the Controls tabs are one and the same. Apply Mask Inverted Switch the Apply Mask Inverted option on and the tool’s entire mask channel gets inverted. That mask channel is the combined product of every mask connected to or generated within a node. Multiply by Mask Pick this option and the masked image’s RGB values get multiplied by the mask channel’s values. As a result, every pixel of the image left out of the mask (that is, set to 0) turns black/transparent. Use Object/Use Material (Checkboxes) Certain 3D applications are able to render into file formats that carry extra channels. The EXR file format notably supports Object and Material ID channels, usable as a mask for the effect. Whether those channels get used, when present, is what these checkboxes decide. Which particular Material ID or Object ID is affected gets picked with the next set of controls. Correct Edges This checkbox turns up only once the Use Object or Use Material checkboxes are on. It flips the method used to handle overlapping edges of objects within a multi-object image. With it on, the Coverage and Background Color channels serve to separate and sharpen the effect around the object’s edge. Leave this option off (or have no Coverage or Background Color channels available) and aliasing may show up on the mask’s edge. For more on Coverage and Background Color channels, turn to Chapter 78, "Understanding Image Channels," within the DaVinci Resolve Reference Manual, or to Chapter 18 within the Fusion Reference Manual.

Object ID/Material ID (Sliders) Reach for these sliders to pick which ID builds a mask out of an image’s object or material channels. Put the Sample button to use just as you would the Color Picker: to grab IDs off the image shown in the view. That image or sequence has to have been rendered from a 3D software package with those channels folded in. Hide Incoming Connections Switch this checkbox on to tuck away connection lines coming from incoming nodes, which makes a node tree look tidier and read more easily. With it on, the Inspector shows an empty field for each input on a node. Drag a connected node out of the node tree into the field and that incoming connection line hides, so long as the node stays unselected in the node tree. Select the node in the node tree and the line comes back. Comments Adding notes to a tool is what the Comments field is for. Click in the empty field and type your text. Add a note to a tool and a small red square turns up in the node’s lower-left corner when the full tile is shown, or a small text bubble icon turns up on the right when nodes are collapsed. To read the note in the Node Editor, rest the mouse pointer over the node to bring up the tooltip. Scripts From the Settings tab, every tool in Fusion offers three Scripting fields. Each holds edit boxes for adding scripts that run as the tool renders. For fuller detail on scripting nodes, please refer to the Fusion scripting documentation.
