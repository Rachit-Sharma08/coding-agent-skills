# Rendering overview and rendering in the Fusion page

Version: DaVinci Resolve 20.3 Reference Manual. Context: Rendering using saver nodes.
[Chapter index](INDEX.md) / [Next section](fusion-studio-previews-and-network-rendering.md)
<a id="source-configurations"></a> <a id="source-frame-range"></a> <a id="source-network"></a> <a id="source-render-settings-dialog-options"></a> <a id="source-rendering-in-fusion-studio"></a> <a id="source-rendering-in-the-fusion-page"></a> <a id="source-rendering-overview"></a> <a id="source-rendering-using-saver-nodes"></a> <a id="source-rendering-using-saver-nodes-part-1"></a> <a id="source-rendering-with-the-saver-node"></a> <a id="source-saver-nodes-in-the-davinci-resolve-fusion-page"></a> <a id="source-setting-filenames-for-export"></a> <a id="source-settings"></a> <a id="source-shoot-on"></a> <a id="source-size"></a> <a id="source-the-render-settings-dialog-options"></a> <a id="source-the-savers-format-tab-with-controls-for-quicktime"></a> <a id="source-using-the-render-settings-dialog"></a>

### Rendering Using Saver Nodes

This section walks through rendering compositions by way of Saver nodes, both in Fusion Studio and on the Fusion page in DaVinci Resolve. It also explains how to spread rendering across several networked computers while working in Fusion Studio.

### Rendering Overview

Once a composition in Fusion is finished, you'll want to render its files out to disk so they can play back and slot into a larger timeline. The way you render differs sharply between Fusion Studio and the Fusion page in DaVinci Resolve. Wrapping up a composite on the Fusion Page means using a MediaOut node to cache the outcome into the Edit or Cut page Timeline, while the DaVinci Resolve Deliver page takes care of the final render of the whole Timeline. Pulling finished composites out of Fusion Studio, by contrast, starts with setting up and rendering from a Saver node in the Node Editor. Fusion Studio can also hand off an assortment of rendering tasks to other machines across a network.

### Rendering in the Fusion Page

On the Fusion page, you need a MediaOut node to carry your composite from the Fusion page back to the Edit or Cut page Timeline. Whatever appears at the MediaOut node when you view it is exactly what gets rendered back onto the Edit or Cut page. In DaVinci Resolve the process runs semi-automatically: the Smart Render Cache setting starts caching the MediaOut node almost as soon as you head back to the Edit or Cut page Timeline. The cache file format, along with any resolution scaling that fits the composition into the Timeline Resolution, is governed in the DaVinci Resolve Project Settings.

### Rendering in Fusion Studio

Within Fusion Studio, every render passes through Saver nodes. Much like MediaOut nodes on the Fusion page, Saver nodes usually hang off the end of a node tree to render the final composite. It is the Saver node that fixes the name, format, and location of the rendered files.

### Rendering with the Saver Node

Kicking off a render in Fusion Studio requires dropping at least one Saver node into the node tree. Typically you park one Saver node right at the tail of your tree to render the final image.

A lone Saver node sits at the end of a node tree to render the final composite. You're free to hook several Saver nodes anywhere along the node tree to render out separate parts of a composite. The example below places three Saver nodes at various spots in the node tree: the top pair render each half of the composite, while the bottom one renders the result of the whole composite.

Several Saver nodes can sit at different parts of a node tree. You may also branch several Saver nodes off the same node to produce a range of output formats. In the example beneath, the three Savers export differing formats of one shot.

Several Saver nodes can be added to produce different output formats. Dropping a Saver node into a node tree pops open a Save dialog automatically, where you name the file and browse to the spot the exported file lands. From there you turn to the Inspector to set up the output format. For fuller detail on the Saver node, the DaVinci Resolve Reference Manual covers it in Chapter 105, “I/O Nodes,” and the Fusion Reference Manual covers it in Chapter 45.

### Setting Filenames for Export

Tack a file extension onto the name and Fusion sets the output format to match. Name your file image_name.exr, for instance, and the Inspector is geared to output an EXR file; name one image_name.mov and the Inspector is geared for an H264 QuickTime movie. Should you want to switch or tweak the file type setting, the specific parameters for whichever format you pick live on the Saver's format tab in the Inspector.

### The Saver’s Format tab with controls for QuickTime

Choose to output an image sequence and a four-digit frame number gets slotted in automatically ahead of the filename extension. Name your file image*name.exr, say, and you wind up with files called image_name0000.exr, image_name0001.exr, and onward. To dictate the frame padding, append a run of zeroes that signals how many digits you want. Enter a filename as image* name*000.exr, for example, and you get an image sequence named Image_name_000.exr, Image* name_001.exr, Image_name_002.exr, and so forth. NOTE: The opening frame number always takes the Time Ruler start frame number.

### Using the Render Settings Dialog

Within Fusion Studio, you launch a render by clicking the Render button, which brings up the Render Settings dialog. That dialog sets the render's quality, frame range, and network usage. To Render a comp in Fusion Studio: 1 Wire a Saver node onto the end of your composition. 2 Type a name and a location for the saved file(s) into the Save window. 3 Where needed, set the format via the Format tab in the Inspector. 4 Click the Render button over in the transport controls area, or pick File > Render All Savers. Up comes the Render Settings dialog, offering options for the rendered output.

### The Render Settings dialog options

Double-check that the frame range and the other parameters are right, then click Start Render.

### Saver nodes in the DaVinci Resolve Fusion page

A Saver node lives on the Fusion page as well, though it serves a different end than its Fusion Studio counterpart. On the Fusion page, the MediaOut node carries the bulk of rendering duties. No Render Settings dialog appears here, because DaVinci Resolve's cache settings already fix the rendering location and format. Saver nodes on the Fusion page are a special case, reserved for rendering OpenEXR files alone. After dropping in a Saver node, you type the filename followed by the extension. exr. Click the Browse button to choose where the EXR sequence goes, then pick Fusion > Render All Savers. The Saver node proves handy for streamlining wildly complex, processor-hungry compositions. You might, for example, use a Saver node to render specific branches of a node tree that no longer need regular tweaking out to OpenEXR, then reimport that result in place of the original branch of nodes to lift your composition's performance. Or you can render out multi-channel mattes or EXR images holding Arbitrary Output Variables (AOVs) for use in other applications.

### Render Settings Dialog Options

A lot of what the Fusion Studio Render Settings dialog offers comes into play when you want a quick preview or a test render. The dialog's options let you boost performance by switching off some of the image-processing operations that eat time yet yield higher-quality results. More often than not, the Configurations section is where you set things first. That section decides whether you're after a final high-quality render or a speedier preview render. Pick Final and you're locked out of the options that would cap the quality.

### Settings

With the Configuration section on Preview, the Render dialog's Settings section carries three options that shape the overall quality and look of your final output. These buttons weigh heavily on render times too. With the Configurations setting on Final, you can't switch these options off HiQ: Switched on, this setting renders at full image quality. When you need to preview how a node's final output would look, you'd enable the HiQ setting. When you're knocking out a rough preview to test animation, switching it off saves you time. MB: The MB here is short for Motion Blur. Switched on, this setting renders with motion blur in place wherever a node is set to generate it. When you're putting together a rough preview and aren't worried about motion blur on animated elements, switching it off saves you time. Some: With Some switched on, only the nodes strictly required to build the image of the node you're previewing get rendered.

### Size

With the Configurations section on Preview, the Size options let you render frame sizes below full resolution. That comes in handy when you're using the Render dialog to build proxies or simply to keep the file size down.

### Network

How rendering gets spread across multiple computers is governed by the Network setting. For fuller detail, turn to this chapter's network rendering section.

### Shoot On

Once more, this option surfaces only while Configurations is on Preview. The Shoot On setting lets you skip frames during a render. You might render every second, third, or fourth frame to trim render time and get quicker feedback. The Step parameter is what you use to set the interval at which frames render.

### Frame Range

Whether Configurations rests on Final or on Preview, this option starts out at whatever current Render In/Out Range the Time Ruler holds, and from that it derives the render's start and end frames. You're free to change the range to render more frames or fewer.

### Configurations

On Final, the Render Settings are geared to turn out the highest-quality results, and most of the dialog's options are off-limits to you. On Preview, you can dial the options for quicker rendering performance. Once you've built a preview configuration worth keeping, save it for later by clicking the Add button, naming it, and clicking OK.
