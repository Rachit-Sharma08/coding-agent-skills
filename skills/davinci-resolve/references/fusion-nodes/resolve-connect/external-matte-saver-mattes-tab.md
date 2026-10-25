# External matte saver mattes tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: External matte saver.
[Chapter index](INDEX.md)
<a id="source-basic-node-setup"></a> <a id="source-controls-tab"></a> <a id="source-external-matte-saver-ems"></a> <a id="source-external-matte-saver-node-introduction"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-mattes-tab"></a> <a id="source-motion-blur"></a> <a id="source-resolve-connect"></a> <a id="source-resolve-connect-1"></a> <a id="source-settings-tab"></a> <a id="source-the-external-matte-saver-controls-tab"></a> <a id="source-the-external-matte-saver-mattes-tab"></a> <a id="source-the-external-matte-saver-node"></a> <a id="source-the-external-matte-saver-settings-tab"></a>

### Resolve Connect

This chapter covers the lone node sitting in the Resolve Connect category, which exists solely in standalone Fusion Studio.

The shorthand shown beside each node name is what you type into the Select Tool dialog while hunting for tools, and it also turns up in scripting references. Throughout this document, treat node trees that display MediaIn nodes in DaVinci Resolve as equivalent to Loader nodes in Fusion Studio, except where stated otherwise.

### External Matte Saver [EMS]

### The External Matte Saver node

NOTE: Only within Fusion Studio do you get the Resolve Connect category along with its External Matte Saver node.

### External Matte Saver Node Introduction

The External Matte Saver node writes several mattes out across multiple channels within an EXR file. The intent is to bring that file into DaVinci Resolve's Color page, giving you a tidy way to hand off multiple mattes for color grading. Achieving the same thing with an ordinary Saver node calls for a Channel Boolean to drop each matte into a channel, after which you name that channel inside the Saver, which takes a touch more setup. This node trims that workflow down by offering multiple inputs and deriving each channel's name from the node.

### Inputs

By default the node offers one input for the 2D image you'd like to store as a matte. Input: At the start there's just a lone orange input where a matte can attach, but the Inspector supplies an Add button so you can tack on more inputs. Every input takes on a fresh color, yet they all accept 2D RGBA images.

### Basic Node Setup

You can park the External Matte Saver node at the tail of any node tree branch to save mattes. In the example below it's wired to the Delta Keyer plus three additional mattes. To attach each matte past the first, you click the Add button in the Inspector beforehand, and a fresh input then appears on the node.

An External Matte Saver node placed on its own branch within a node tree so the mattes get rendered

### Inspector

### The External Matte Saver Controls tab

### Controls Tab

You use the Controls tab to give the saved file a name and to pick where on your hard drive it lands. Filename Type the name you'd like the EXR file to carry into the Filename field. Tack the .exr extension onto the end of the name so that the file gets written as an EXR file. Browse Hitting the Browse button brings up a standard file browser window in which you pick the spot to save the file.

### Mattes Tab

On the Mattes tab you configure how many mattes go into the file, what each channel is called, and which RGBA channels are stored from each input.

### The External Matte Saver Mattes tab

Channels menu With the Channels menu you pick which channels end up saved in the matte. The options are the alpha channel, the RGB channels, or the RGBA channels. Channels Name Through the Channels Name field you set your own name for the matte channel being saved. That name then shows up in DaVinci Resolve's Color page. Node Name The Node Name field reports where the matte came from. It fills in on its own once you wire a node into the input. Add Hitting the Add button puts another input on the node along with a further group of fields where you set up and name the new matte channel.

### The External Matte Saver Settings tab

### Settings Tab

Within the Inspector, the Settings Tab resembles the settings you'd find on the Saver tool. Its controls stay consistent and behave just like the Settings on other tools. Blend You use the Blend control to mix between the tool's untouched image input and the tool's finished, altered output image. With the blend value at 0.0, the outgoing image matches the incoming image exactly. Ordinarily that makes the tool bypass processing altogether, passing the input straight through to the output. Process When Blend Is 0.0 The tool still processes even with the input value at zero. That can come in handy when this node's processing is scripted to kick off another task while the node's value sits at 0.0. Red/Green/Blue/Alpha Channel Selector These four buttons restrict the tool's effect to the color channels you specify. This filter usually runs after the tool has finished processing. As an example, deselecting the Red button on a Blur tool means the blur is applied to the image first, and then the red channel from the original input gets copied back over the result's red channel. A few exceptions exist, namely tools where deselecting these channels makes the tool skip processing that channel outright. Such tools typically carry a matching set of RGBA buttons on the Controls tab in the tool. When that's the case, the buttons on the Settings and the Controls tabs are one and the same. Apply Mask Inverted Switching on the Apply Mask Inverted option flips the whole mask channel for the tool. That mask channel is the merged outcome of every mask wired into or produced within a node. Multiply by Mask Choosing this option makes the RGB values of the masked image get multiplied against the mask channel's values. The upshot is that every pixel of the image left out of the mask (that is, set to 0) turns black/transparent.

Use Object/Use Material (Checkboxes) Certain 3D software can render into file formats carrying extra channels. The EXR file format in particular supports Object ID and Material ID channels, either of which can serve as a mask for the effect. These checkboxes decide whether those channels get used when present. Which specific Material ID or Object ID is acted on gets set with the next group of controls. Correct Edges This checkbox surfaces only while the Use Object or Use Material checkboxes are on. It switches the method used for handling the overlapping edges of objects within a multi-object image. With it on, the Coverage and Background Color channels serve to separate and refine the effect along the object's edge. Turn this option off (or lack any Coverage or Background Color channels) and aliasing can show up along the mask's edge. To read more about the Coverage and Background Color channels, turn to the DaVinci Resolve Reference Manual at Chapter 78, "Understanding Image Channels," or else the Fusion Reference Manual at Chapter 18. Object ID/Material ID (Sliders) These sliders let you choose which ID builds a mask out of an image's object or material channels. Use the Sample button just as you would the Color Picker: to pull IDs from the image shown in the viewer. The image or sequence has to have been rendered from a 3D software package that bundled those channels in.

### Motion Blur

- Motion Blur: This toggles the rendering of Motion Blur on the tool. While this control is on, the tool's anticipated motion drives the motion blur produced by the virtual camera's shutter. With the control off, no motion blur gets created.
- Quality: Quality sets how many samples build the blur. A quality setting of 2 has Fusion lay down two samples on each side of an object's true motion. Bigger values yield smoother output but push up the render time.
- Shutter Angle: Shutter Angle governs the angle of the virtual shutter that produces the motion blur effect. Wider angles add more blur but lengthen the render times. A value of 360 amounts to leaving the shutter open across one full frame exposure. You can go beyond that, and higher values can yield interesting effects.
- Center Bias: Center Bias shifts where the center of the motion blur sits. That opens the door to motion trail effects.
- Sample Spread: Tweaking this control changes the weighting applied to each sample. That alters how bright the samples are.

Hide Incoming Connections Turning on this checkbox can conceal the connection lines coming from upstream nodes, leaving a node tree that looks cleaner and reads more easily. With it on, the Inspector displays an empty field for each input on a node. Drag a connected node from the node tree onto the field and that incoming connection line stays hidden for as long as the node remains unselected in the node tree. Select the node in the node tree and the line returns.

Comments You use the Comments field to attach notes to a tool. Click the empty field and type your text in. Once a note is on a tool, a small red square shows up in the node's lower-left corner while the full tile is shown, or a tiny text bubble icon appears at the right once nodes are collapsed. To read the note in the Node Editor, hover the mouse pointer over the node to surface the tooltip. Scripts Every tool in Fusion offers three Scripting fields from the Settings tab. Each holds edit boxes for adding scripts that run while the tool renders. For more on scripting nodes, please refer to the Fusion scripting documentation.
