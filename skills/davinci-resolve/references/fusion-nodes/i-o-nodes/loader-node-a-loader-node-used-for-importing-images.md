# Loader node a loader node used for importing images

Version: DaVinci Resolve 20.3 Reference Manual. Context: Loader node.
[Chapter index](INDEX.md) / [Next section](loader-node-loader-import-tab.md)
<a id="source-a-loader-node-used-for-importing-images"></a> <a id="source-basic-node-setup"></a> <a id="source-file-tab"></a> <a id="source-i-o-nodes-part-1"></a> <a id="source-import-tab"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-io-nodes"></a> <a id="source-loader-node-file-tab"></a> <a id="source-loader-node-introduction"></a> <a id="source-loader-node-ld"></a> <a id="source-the-loader-node"></a> <a id="source-the-magic-comp-variable"></a>

### I/O Nodes

The bringing of media in and out by way of Loader and Saver nodes inside Fusion Studio, plus the MediaIn and MediaOut nodes within DaVinci Resolve, is what this chapter covers. The abbreviation beside each node name can be typed into the Select Tool dialog while you hunt for tools, and it carries over into scripting references too.

### Loader Node [LD]

### The Loader node

### Loader Node Introduction

NOTE: Within DaVinci Resolve, the Loader node serves only for bringing in EXR files. Over in Fusion Studio, the Loader node is the one you turn to for picking and pulling footage off your hard drive into the Node Editor. Three routes exist for adding a Loader node, and along with it a clip, to the Node Editor.

- Add the Loader out of the Effects Library or toolbar (Fusion Studio only), then work Loader's file browser to pull a clip into the Node Editor
- Drag clips straight out of an OS window into the Node Editor, which spawns a Loader node in the Node Editor.
- Pick File > Import > Footage (Fusion Studio only), though this route spawns a fresh composition on top of adding the Loader node to the Node Editor.

Once a Loader gets added to the Node editor, a File dialog pops up on its own so you can pick a clip off your hard drives. NOTE: The file browser's automatic appearance can be switched off by turning off Auto Clip Browse under the Global > General Preferences. After clips have been pulled in through the Loader node, the Loader handles trimming, looping, and stretching the footage, plus assigning the field order, pixel aspect, and color depth. The Loader counts, arguably, as the single most important tool inside Fusion Studio.

### Inputs

The lone input on the Loader node is meant for an effect mask that crops the image the Loader pulls in. Effect Mask: The blue input takes a mask shape made by polylines, basic primitive shapes, paint strokes, or bitmaps coming from other tools. Wiring a mask here confines the loaded image so it surfaces solely within the mask. An effects mask gets applied to the tool once the tool has been processed.

### Basic Node Setup

The Loader node is a 2D image in whatever format Fusion Studio supports. Within DaVinci Resolve it's confined to an EXR format. Below, the LOADER pulls in an image, which then gets masked using an Ellipse matte. From the masked LOADER, the output carries onward to 2D image-processing nodes.

### A Loader node used for importing images

### Inspector

### Loader node File tab

### File Tab

The Loader's File tab carries controls for trimming, making a freeze frame, looping, and reversing the clip. You can additionally re-pick, from your hard drive, whichever clip the Loader points to. Global In and Out: this node's position within the project gets fixed through the Global In and Out handles. Reach for Global In to fix the frame on which the clip begins, and Global Out to fix the frame on which the clip wraps up inside the project's global range. The node yields no image on frames falling beyond this range. Should the Global In and Out values be lowered until the span between the In and Out values drops under the count of frames on hand in the clip, Fusion trims the clip on its own by nudging the Trim range control. Should the Global In/Out values be raised until the span between the In and Out values exceeds the count of frames on hand in the clip, Fusion stretches the clip on its own by nudging the Hold First/Last Frame controls. Stretched frames get shown within the range control by turning the color of the held frames green inside the control.

So as to slide the clip through time or shift it across the project while leaving its length intact, rest the mouse pointer at the center of the range control and pull it across to the new spot, or else key the value in by hand inside the Global In value box. Filename The Filename field surfaces the file path of the clip the Loader node pulled into the Node Editor. Clicking the Browse button brings up a standard file browser. The path to the footage may also be keyed straight in via the field on offer. The text box accommodates filename completion. As a directory or file name gets typed into the text box, Fusion brings up a pop-up listing likely matches. Reach for the arrow keys to pick the right match and round out the path. NOTE: Bringing in image sequences is routine practice for compositing, whether the image sequence arrives from a 3D renderer or a digital cinema camera. Should the tail end of a file's name be a number (the file extension aside), Fusion sweeps the directory on its own searching for files that fit the sequence. As an example, these filenames would form valid sequences: image.0001.braw , image.0002.braw, image.0003.braw … or image151.exr , image152.exr, image153.exr … These next ones, by contrast, wouldn't register as a sequence, given that their final characters aren't digits: shot.1.fg.jpg, shot.2.fg.jpg, shot.3.fg.jpg Picking the very first file in the sequence isn't required. Fusion combs the whole folder for files that fit the sequence in the chosen filename. As well, Fusion gauges the sequence's length off the first and last numeric value across the filenames. Any missing frames get skipped. As an example, should the folder hold two files carrying these names: image.0001.exr, image.0100.exr Fusion reads this as a file sequence spanning 100 frames, not an image sequence holding two frames. The Missing Frames drop-down menu serves to pick how Fusion deals with missing frames. The Trim In/Trim Out control's context menu can additionally serve to force a particular clip length or to re-sweep the folder. A fuller account of both controls sits below. Now and then you'll want to pull in just a lone frame out of a sequence—say, a photograph out of a folder that holds many other files too. By default Fusion reads those as a sequence, but holding Shift while you drag the file out of the OS window into the Node Editor makes Fusion take only that one file and ignore any sequencing. Proxy Filename The Proxy Filename control surfaces solely once the filename control points at a valid clip. The Proxy Filename can name a clip that loads whenever the Proxy mode is switched on. That lets smaller renditions of the image get loaded to quicken file I/O off disk, plus processing. As an example, build a 1/4-scale rendition of an 8K EXR sequence for use as EXR proxy files. Any time the Composition's Proxy mode is switched on, the lower resolution proxy clip loads off disk, and all processing runs at the reduced resolution, markedly cutting render times. That proves especially handy while you handle large RAW plates kept on a remote file server. Lower-resolution renditions of the plates can be kept locally, trimming network bandwidth, interactive render times, and memory usage.

The proxy clip is required to carry the same count of frames as the source clip, and the clip's sequence numbers have to begin and end on the same frame numbers. The strong suggestion is that the proxies share the same format as the main files. Where formats carry options, like Cineon, DPX, and OpenEXR, the proxies adopt the same format options as the primary. Trim The Trim range control serves to clip frames off the start or end of a clip. Nudge the Trim In to drop frames off the start, and nudge Trim Out to fix the clip's last frame. The values applied here act as offsets. A value of 5 in Trim In would take the fifth frame in the sequence as the start, passing over the first four frames. A value of 95 would halt frame loading past the 95th. Hold First Frame/Hold Last Frame: for the stated count of frames, the clip's first or last frame is kept held by the Hold First Frame and Hold Last Frame controls. Held frames join the loop whenever the footage gets looped. Reverse Tick this checkbox to flip the footage so the last frame plays first and the first frame plays last. Loop Tick this checkbox to loop the footage on through to the project's end. Whatever stretching of the clip via Hold First/Last Frame or shortening via Trim In/Out joins the looped clip. Missing Frames The Missing Frames menu sets how the Loader behaves whenever a frame is missing or can't load for whatever reason.

- Fail: The Loader yields no image until a frame turns available. Rendering is halted.
- Hold Previous Output: The last valid frame is held until a frame turns available once more. This fails when no valid frame has been encountered—say, when the first frame is missing.
- Output Black: Puts out a black frame until a valid frame turns available once more.
- Wait: Fusion holds out for the frame to turn available, checking every few seconds. This comes in handy

for rendering a composition at the same time as a 3D render. Every render halts until the frame shows up.

### The Magic Comp Variable

For the media's location, Loaders and Savers rely on the absolute file paths. That said, over in Fusion Studio, you can rely on a file path stated relative to where the composition was saved. The Comp variable functions for Loaders and Savers and helps you keep your work tidy. Keying Comp:\ in place of the entire file path name acts as a shortcut to the folder where your Fusion composition document sits saved. You may either key the Comp:\ in by hand inside a Loader's filename field, or switch on the Enable Reverse Mapping of Paths Preferences checkbox within the Path Map preferences. Switching on the Path Map preference check box will apply the Comp:\ on its own. So provided all your source footage sits in subfolders of your Comp folder, Fusion locates that footage no matter the actual hard drive or network share name.

You might, as an instance, copy a whole shot off the network onto your local drive, configure your Loaders and Savers to rely on the Comp variable, work all your magic locally (that is, configure your composition), and then copy only the composition back onto the server and kick off a net-render. Every render slave locates the source footage on its own. A few examples: Your composition sits saved in: X:\Project\Shot0815\Fusion\Shot0815.comp Your source footage lives in: X:\Project\Shot0815\Fusion\Greenscreen\0815Green_0000.dpx The relative path inside the Loader node would then read: Comp:\Greenscreen\0815Green_0000.dpx Should your source footage live in: X:\Project\Shot0815\Footage\Greenscreen\0815Green_0000.dpx The relative path inside the Loader node would then read: Comp:\..\Footage\ Greenscreen\0815Green_0000.dpx Notice how the two dots .. push the directory up one folder, rather like CD .. inside a Command Shell window.

### Import Tab

The Import tab carries settings for the frame format and for handling fields, pixel aspect, 3:2 pull down/pull up conversion, and stripping gamma curve types so as to reach a linear workflow.
