# Set timecode and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Set timecode, Common controls.
[Chapter index](INDEX.md) / [Previous section](copy-metadata-and-set-metadata.md)
<a id="source-basic-node-setup-2"></a> <a id="source-controls-tab-2"></a> <a id="source-inputs-2"></a> <a id="source-inspector-1"></a> <a id="source-inspector-2"></a> <a id="source-set-timecode-node-introduction"></a> <a id="source-set-timecode-tcmeta"></a> <a id="source-the-common-controls"></a> <a id="source-the-common-metadata-settings-tab"></a> <a id="source-the-set-timecode-controls-tab"></a> <a id="source-the-set-timecode-node"></a>

### Set Timecode [TCMeta]

### The Set Timecode node

### Set Timecode Node Introduction

Set Timecode writes dynamic timecode values into the metadata table, derived from the FPS settings.

### Inputs

The lone input on the Set Timecode node is meant for wiring up a 2D image that will have timecode added to it. Background Input: The orange background input carries the main 2D image that the node sends on with its new timecode.

### Basic Node Setup

The Set Timecode node writes fresh timecode metadata onto the background input (orange). What emerges is the background input carrying the refreshed timecode.

A Set Timecode node inserts new timecode metadata into the background clip.

### Inspector

### The Set Timecode Controls tab

### Controls Tab

Working from FPS, hours, minutes, seconds, and frames, the Controls tab establishes the clip's starting timecode metadata.

FPS A range of frames-per-second settings is on offer for you to pick from. Because this is a Fuse, tailoring the settings to your own needs is straightforward — just edit the relevant chunk of code that drives the buttons: MBTNC_StretchToFit = true, { MBTNC_AddButton = "24" }, { MBTNC_AddButton = "25" }, { MBTNC_AddButton = "30" }, { MBTNC_AddButton = "48" }, { MBTNC_AddButton = "50" }, { MBTNC_AddButton = "60" }, }) and likewise the actual values themselves: local rates = { 24, 25, 30, 48, 50, 60 } Hours/Minutes/Seconds/Frames Sliders Set an offset measured from the current comp's starting frame. Print to Console Sends a wordy dump of the Timecode/Frame value out to the Console. How the Timecode/Frames conversion comes out depends on the FPS settings. A sample of what you might see: TimeCode: 00:00:08:15 Frames: 207 Common Controls Settings Tab Across the other Metadata nodes, the Inspector's Settings tab turns up once again. A full account of these shared controls follows below under the "The Common Controls" heading.

### The Common Controls

Several identical controls in the Inspector are shared by the nodes that carry out metadata operations. The controls common across the Metadata nodes are laid out in this section.

### Inspector

### The Common Metadata Settings tab

Settings Tab Every tool within the Metadata category carries the Settings tab in the Inspector. These controls behave the same way and stay consistent from one tool to the next. Use Object/Use Material (Checkboxes) Certain 3D applications can render into file formats that carry extra channels. The EXR file format in particular supports Object ID and material ID channels, which are usable as a mask for the effect. Whether those channels get used, when present, is decided by these checkboxes. Which specific Material ID or Object ID is affected gets set with the next group of controls. Correct Edges This checkbox shows up only once the Use Object or Use Material checkboxes are turned on. It switches the approach used for handling overlapping object edges in a multi-object image. With it on, the Coverage and Background Color channels serve to separate the effect and clean it up around an object's edge. Should this option be off (or no Coverage or Background Color channels exist), aliasing can show up along the mask's edge. For a deeper look at the Coverage and Background Color channels, consult either Chapter 78, "Understanding Image Channels," within the DaVinci Resolve Reference Manual, or else Chapter 18 of the Fusion Reference Manual.

Object ID/Material ID (Sliders) These sliders pick which ID drives the mask built from an image's object or material channels. The Sample button works just like the Color Picker, grabbing IDs off the image shown in the view. The picture or sequence must have been rendered out of a 3D software package that included those channels. Comments The Comments field exists for jotting notes onto a tool. Click within the blank field and enter your text. After a note goes onto a tool, a tiny red square shows up at the node's lower-left corner whenever the full tile is shown, or a tiny text-bubble icon shows up on the right when nodes are collapsed. To view the note inside the Node Editor, hover the mouse pointer over the node and its tooltip appears. Scripts Each tool in Fusion offers three Scripting fields on the Settings tab. Every one holds edit boxes where you can drop in scripts that run while the tool renders. For fuller detail on scripting nodes, turn to the Fusion scripting documentation.
