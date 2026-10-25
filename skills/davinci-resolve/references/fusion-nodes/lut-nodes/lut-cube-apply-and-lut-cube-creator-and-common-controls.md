# LUT cube apply and LUT cube creator and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: LUT cube apply, LUT cube creator, Common controls.
[Chapter index](INDEX.md) / [Previous section](file-lut-and-lut-cube-analyzer-and-lut-cube-apply.md) / [LUT Cube Apply LCP](file-lut-and-lut-cube-analyzer-and-lut-cube-apply.md)
<a id="source-a-cube-image-created-with-the-rect-type"></a> <a id="source-basic-node-setup-2"></a> <a id="source-basic-node-setup-3"></a> <a id="source-common-lut-settings-inspector"></a> <a id="source-controls-tab-2"></a> <a id="source-inputs-2"></a> <a id="source-inputs-3"></a> <a id="source-inspector-2"></a> <a id="source-inspector-3"></a> <a id="source-inspector-4"></a> <a id="source-lut-cube-creator-controls"></a> <a id="source-lut-cube-creator-lcc"></a> <a id="source-lut-cube-creator-node-introduction"></a> <a id="source-settings-tab-2"></a> <a id="source-settings-tab-3"></a> <a id="source-settings-tab-4"></a> <a id="source-the-common-controls"></a> <a id="source-the-lut-cube-creator-node"></a> <a id="source-the-resulting-color-cube"></a>

### Inputs

Three inputs live on the LUT Cube Apply: a green input that the LUT Cube Creator’s output plugs into, an orange input carrying the image you want the LUT laid onto, and a blue effect mask input Input: That orange input takes a 2D image, which then receives the LUT. Reference Image: Wire the green input to either the LUT Cube Creator’s output or to a node reworking the image that began at the LUT Cube Creator. Effect Mask: The optional effect mask input takes a mask shape built from polylines, simple primitive shapes, paint strokes, or bitmaps from other tools. Hook a mask here and the LUT Cube Apply confines itself to just the pixels inside that mask. This kind of effects mask hits the tool once the tool has wrapped up processing.

### Basic Node Setup

The example beneath opens with a LUT Cube Creator node and passes through a pair of color adjustments. That adjusted image then plugs into the green Reference input on the LUT Cube Apply, while the image you want carrying the LUT goes to the orange Input.

A LUT made by the LUT Cube Creator gets laid onto an image by means of the LUT Cube Apply node.

### Inspector

The LUT Cube Apply node carries no controls at all. Whatever LUT feeds the green foreground input gets laid onto the image feeding the orange background input, and no real 3D LUT need ever be written through the LUT Cube Analyzer.

### Settings Tab

You’ll see this same Settings tab in the Inspector echoed on the other LUT nodes. The “The Common Controls” section wrapping up this chapter covers these shared controls in full.

### LUT Cube Creator [LCC]

### The LUT Cube Creator node

### LUT Cube Creator Node Introduction

The LUT Cube Creator builds an image meant to be used downstream by the LUT Cube Analyzer or LUT Cube Apply nodes. Its output is fair game for grading, color correction, or reworking with any tool, whether inside Fusion or out. Should you work outside Fusion, hold the image at 32-bit floating point so color accuracy survives. Run the untouched LUT Cube Creator image into the LUT Cube Analyzer node and you end up with an unaltered, or 1:1, LUT file, the viewer left blank.

### Inputs

No inputs sit on the LUT Cube Creator. This node exists to build an image from which a LUT can be made.

### Basic Node Setup

Below, the example begins at a LUT Cube Creator node and threads through two color adjustments. That adjusted image then plugs into a LUT Cube Analyzer, which spits out the LUT file. The whole LUT-making path kicks off at the LUT Cube Creator and wraps up at a LUT Cube Analyzer.

### Inspector

### LUT Cube Creator controls

### Controls Tab

The Controls tab lays down a kind of test pattern that goes toward building a 3D LUT. What you set here governs how intricate the pattern is that ultimately feeds a LUT through the LUT Cube Analyzer. Type: Reach for the Type menu to build a pattern of color cubes.

- Horizontal: Builds a long, horizontal strip standing in for a color cube.
- Vertical: Builds a long, vertical strip standing in for a color cube.
- Rect: Builds a rectangular image, pictured beneath, standing in for a color cube.

### A Cube image created with the Rect type

### The resulting color cube

Size Sets how much resolution the color cube carries. Common Size choices for color cubes run to 33 (33 x 33 x 33) or 65 (65 x 65 x 65). Each figure counts the samples along one side of the cube. So a 33 x 33 x 33 cube works out to roughly 35,937 color samples. NOTE: Pushing resolution higher sharpens the result, yet it leans harder on memory and computation alike.

### Settings Tab

This Settings tab in the Inspector recurs on the other LUT nodes too. The “The Common Controls” section coming up next walks through these shared controls.

### The Common Controls

Across the Inspector, the LUT nodes hold a set of matching controls in common. What this section covers are the controls shared among LUT nodes.

### Inspector

### Common LUT Settings Inspector

### Settings Tab

Every tool in the LUT category carries this Settings tab in the Inspector. The controls stay uniform and behave identically from one tool to the next, though a tool here or there throws in an option or two of its own, which get covered here as well.

Use GPU There are three choices on the Use GPU menu. Pick Disable to shut off hardware-accelerated rendering on your computer’s graphics card. Enabled puts the hardware to work. Auto leans on a capable GPU whenever one’s around and falls back to software rendering when none is. Hide Incoming Connections Tick this checkbox to tuck away the connection lines arriving from upstream nodes, leaving a node tree that reads cleaner and easier. With it on, the Inspector shows a blank field for every input on a node. Drag a connected node out of the node tree onto that field and the incoming connection line stays hidden, so long as the node isn’t selected in the node tree. Select the node in the node tree and the line comes back. Comments Use the Comments field to jot notes onto a tool. Click into the blank field and type away. Once a tool carries a note, a small red square turns up in the node’s lower-left corner while its full tile shows, or a small text-bubble icon appears off to the right when the nodes are collapsed. To read that note inside the Node Editor, hover the mouse pointer over the node so the tooltip appears. Scripts From the Settings tab, every Fusion tool offers three Scripting fields. Each holds an edit box where you drop scripts that run as the tool renders. For fuller detail on scripting nodes, turn to the Fusion scripting documentation.
