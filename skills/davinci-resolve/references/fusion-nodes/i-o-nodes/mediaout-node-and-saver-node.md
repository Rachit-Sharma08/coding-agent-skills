# Mediaout node and saver node

Version: DaVinci Resolve 20.3 Reference Manual. Context: Mediaout node, Saver node.
[Chapter index](INDEX.md) / [Previous section](mediain-node-and-mediaout-node.md) / [Next section](saver-node-saver-export-tab.md) / [MediaOut Node MO](mediain-node-and-mediaout-node.md)
<a id="source-basic-node-setup-1"></a> <a id="source-file-tab"></a> <a id="source-inputs-1"></a> <a id="source-inspector"></a> <a id="source-inspector-1"></a> <a id="source-saver-file-tab"></a> <a id="source-saver-node-introduction"></a> <a id="source-saver-node-sv"></a> <a id="source-the-color-grade-tab-set-to-color"></a> <a id="source-the-color-grade-tab-set-to-mix"></a> <a id="source-the-color-grade-tab-set-to-none"></a> <a id="source-the-mediaout-controls"></a> <a id="source-the-saver-node"></a>

### Inspector

### The MediaOut controls

For viewing on the Fusion page, the MediaOut node offers a range of Color Grade options.

- None: The default view, this one shows nothing but the output of the Fusion composition.
- Color: This one shows the Fusion composition’s output, Color page adjustments included, at timeline resolution.
- Mix: This one shows the Fusion composition’s output together with Cut and Edit page effects plus Color page adjustments, at timeline resolution.

NOTE: These options serve only as previews, putting your current comp in the context of whatever other effects may have been added beyond Fusion. The MediaOut node’s own actual output stays as it was.

### The Color Grade tab set to None

None shows nothing but the output of the Fusion composition. Notice that the display sits at the source media/composition resolution.

### The Color Grade tab set to Color

Color shows the Fusion composition, taking in whatever adjustments got applied on the Color page. Notice that once the MediaOut view is on Color, the display moves to the timeline resolution.

### The Color Grade tab set to Mix

Mix shows the Fusion composition, taking in whatever effects got applied on the Cut or Edit page along with whatever adjustments are on the Color page. Notice that once the MediaOut view is on Mix, the display moves to the timeline resolution.

### Saver Node [SV]

### The Saver node

NOTE: Within DaVinci Resolve, the Saver node serves only to export EXR files.

### Saver Node Introduction

The final composition output coming out of Fusion Studio is what the Saver node stands for. Its job is rendering out movie files or sequential images, though you can drop it into a composition at any point to render out a composition’s intermediate stages. Any number of Saver nodes can live inside one composition, for rendering a comp’s different branches as well as different formats. The Saver node can additionally tack scratch track audio onto your composition, audible during interactive playback.

### Inputs

The lone input on the Saver node is meant for the finished composition you’re after rendering. Image Input: Use that orange input to wire up the resulting image you want rendered.

### Basic Node Setup

You position the Saver node at the composition’s end. Several Savers can sit in one comp to render different formats or to render a composition’s different parts.

A Saver node placed at a node tree’s end so as to render the composition

### Inspector

### Saver File tab

### File Tab

What the Saver File tab does is set where the rendered file lands and what format it takes. Filename The Filename dialog is where you settle on the name and path for the rendered image output. Click the Browse button to bring up a file browser and pick a spot for the output. When you render a sequential image file format, sequence numbering gets tacked onto the filename for you. As an example, enter c\renders\image.exr as the filename and render 30 frames of output, and the files get numbered automatically as image0000.tga, image0001.exr, image0003.exr... and onward. Numbers below 10000 automatically get four-digit padding. By typing the digits straight into the filename you can dictate how many digits the padding uses. For instance, image000000.exr would put 6-digit padding on the numbering; meanwhile image.001.exr gives you 3-digit padding, whereas image1.exr gives none whatsoever. Output Format Picking which image format to save is the job of this menu. Keep in mind that picking a fresh format off this menu won’t change the filename’s extension to match. Edit the filename by hand to line up with that format’s expected extension, so name and image format don’t end up mismatched. Save Frames This control picks between two rendering modes: Full Renders Only or High Quality Interactive.

- Full Renders Only: For most situations this is the usual setting. Images land on disk once a final render kicks off with the Start Render button in the Time Ruler.
- High Quality Interactive: Built for real-time rendering during painting and rotoscoping, this render mode has Fusion write each frame to disk as it’s processed interactively. Put to use properly, the feature can do away with the need for a final render once rotoscoping is done.

NOTE: Paired with a node tree carrying spline-animated parameters, the High Quality Interactive setting can readily breed confusion. Should those splines get altered such that frames already saved interactively change, the frames already on disk won’t re-render on their own. Either walk through each frame once more or run a final render to be sure the result is right Frame Offset With this thumbwheel control you can set an explicit start frame for the number sequence put on the rendered filenames. As an example, set Global Start to 1 and render frames 1-30 so that files normally get numbered 0001-0030. With the Sequence Start Frame set to 100, the rendered output would instead carry numbers from 100-131.
