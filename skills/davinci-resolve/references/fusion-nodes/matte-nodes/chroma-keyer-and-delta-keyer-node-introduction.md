# Chroma keyer and delta keyer node introduction

Version: DaVinci Resolve 20.3 Reference Manual. Context: Chroma keyer, Delta keyer node introduction.
[Chapter index](INDEX.md) / [Previous section](chroma-keyer-chroma-key-tab.md) / [Next section](delta-keyer-initial-setup.md) / [Continue Delta Keyer Node Introduction / Key Tab View Mode](delta-keyer-initial-setup.md) / [Chroma Keyer CKy](alpha-divide-and-alpha-multiply-and-chroma-keyer.md)
<a id="source-a-clean-plate-connected-to-a-delta-keyer"></a> <a id="source-basic-node-setup-3"></a> <a id="source-basic-node-setup-4"></a> <a id="source-common-controls-1"></a> <a id="source-common-controls-2"></a> <a id="source-cryptomatte-cry-studio-version-only"></a> <a id="source-cryptomatte-node-introduction"></a> <a id="source-delta-keyer"></a> <a id="source-delta-keyer-node-introduction"></a> <a id="source-inputs-4"></a> <a id="source-inspector-3"></a> <a id="source-inspector-4"></a> <a id="source-mask-tab"></a> <a id="source-plate-tab"></a> <a id="source-the-clean-plate-mask-tab"></a> <a id="source-the-clean-plate-tab"></a> <a id="source-the-cryptomatte-controls"></a> <a id="source-the-cryptomatte-node"></a> <a id="source-the-delta-keyer-node"></a> <a id="source-time-mode"></a>

### Basic Node Setup

The Clean Plate node and the Delta Keyer form two distinct branches springing from the main image you mean to key. The green-screen or blue-screen clip is branched off so it feeds the orange image input on the Clean Plate as well as the matching orange image input over on the Delta Keyer. From there the clean plate's output wires into the magenta clean plate input on the Delta Keyer. The Delta Keyer's output then serves as the foreground into a Merge.

### Inspector

### A Clean Plate connected to a Delta Keyer

### The Clean Plate tab

### Plate Tab

The Plate tab holds the main tools for making a clean plate. From this tab you drag over the areas in the viewer, then use the Erode and Grow Edges sliders to build the clean plate. Method The Method menu picks which kind of color selection you use while sampling colors in the viewer.

- Color: Color leans on a difference method to split off the background color. It works well where the screen colors are even.
- Ranges: Ranges leans on a chroma range method to split off the background color. It's the stronger pick for a shadowed screen or screens carrying different colors.

Matte Threshold This range slider fixes the lower threshold with the left handle and the upper threshold with the right handle. Anything below the lower threshold goes black or transparent in the matte. Anything above the upper threshold goes white or opaque in the matte. Everything inside the range keeps its relative transparency. This control frequently serves to throw out salt and pepper noise from the matte. Erode Use the Erode slider to shrink the screen area. It's there to nibble away small non-screen color pixels that might get in the way of a smooth green- or blue-screen clean plate. Crop Crop pulls in from the image's edges. Grow Edges The Grow Edges slider spreads the edge color outward to plug holes until a full green or blue screen forms. Fill The Fill checkbox plugs leftover holes using color drawn from the nearby screen color.

### Time Mode

- Sequence: Builds a fresh clean plate on every frame.
- Hold Frame: Holds the clean plate on one single frame.

### The Clean Plate Mask tab

### Mask Tab

Use the Mask tab to invert the mask wired into the node's garbage mask input. You can apply the garbage mask to clear areas ahead of growing edges or filling leftover holes.

Invert Invert draws on the mask's transparent parts to clear the image.

### Common Controls

Settings Tab Other matte nodes carry a copy of the Inspector's Settings tab too. The closing “The Common Controls” section of this chapter explains these shared controls in detail.

### Cryptomatte [Cry] (Studio Version Only)

### The Cryptomatte node

### Cryptomatte Node Introduction

Fusion's Cryptomatte tool lets you read embedded mattes rendered into an EXR. Instead of leaning on manually-assigned masks or color keying, Cryptomatte reads the encoded IDs and pulls each one out so that selecting it becomes easy. With this tool you can build mattes for particular objects or materials within a 3D-rendered scene.

### Inputs

The Cryptomatte node has just one input in the Node Editor. Input: The orange input takes a 2D EXR image carrying embedded mattes.

### Basic Node Setup

The Cryptomatte node accepts an EXR image holding embedded mattes, then lets you pick which mattes carry on to the rest of the comp.

Cryptomatte accepting an EXR, picking out its mattes, and then handing them off to the Color Corrector and Bitmap tools

### Inspector

### The Cryptomatte Controls

With these parameters you steer the matte selection of an EXR file.

- View Layer: Swap the layer and matte type to pick (Object, Material etc). This shapes which matte type the Pick control lets you choose.
- View Mode: Alters the Cryptomatte tool's output. Colors: Renders the layer IDs as distinct colors. Edges: Renders the source EXR with the mattes outlined over the image. Beauty: Renders the source EXR. Matte: Puts out a black and white image of the chosen matte.
- Select Matte: Pick mattes from the viewer or off a list. Pick: Click to bring up a pick window holding a matte list selection. Click-drag, or use Cmd/Control-clicks, to grab several mattes from the list. Mode: Click and drag the control to summon an eye dropper cursor for picking or dropping mattes in the viewer.
- Selected Matte List: The Selected Matte List shows your chosen mattes in a list view. The selection lights up yellow in the viewer. Clear: Click the bin icon to drop the chosen mattes. Clear All: Click this button to drop every matte from the Selected Matte List. Clear Selected Layer: Click to drop all mattes off the layer. Expression: Into this field you can add regular expressions to pick layers within the tool. Matte Layers: Cycle among only the Selected layers, View, and All.

### Common Controls

Settings Tab Other matte nodes carry a copy of the Inspector's Settings tab as well. The closing “The Common Controls” section of this chapter covers these shared controls in detail.

### Delta Keyer

### The Delta Keyer node

### Delta Keyer Node Introduction

A sophisticated color difference keyer, the Delta Keyer packs plenty of features and controls for tuning the matte and pulling the subject off a blue or green screen. Several keying systems live inside it: as the master difference keyer you've got the Key tab, while Pre-Matte serves as a built-in clean plate for evening out screen color. Tuning, Fringe, and Matte round out the keying process. The tabs sit roughly in the order you'd normally work through them.
