# Copy metadata and set metadata

Version: DaVinci Resolve 20.3 Reference Manual. Context: Copy metadata, Set metadata.
[Chapter index](INDEX.md) / [Next section](set-timecode-and-common-controls.md)
<a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-common-controls"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab"></a> <a id="source-controls-tab-1"></a> <a id="source-copy-metadata-meta"></a> <a id="source-copy-metadata-node-introduction"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-inspector"></a> <a id="source-metadata-nodes"></a> <a id="source-metadata-nodes-1"></a> <a id="source-set-metadata-node-introduction"></a> <a id="source-set-metadata-smeta"></a> <a id="source-the-copy-metadata-controls-tab"></a> <a id="source-the-copy-metadata-node"></a> <a id="source-the-set-metadata-controls-tab"></a> <a id="source-the-set-metadata-node"></a>

### Metadata Nodes

This chapter walks through the Metadata nodes that Fusion provides.

Each node name carries an abbreviation beside it that you can type into the Select Tool dialog while hunting for tools, and that also serves in scripting references. Throughout this document, node trees depicting MediaIn nodes in DaVinci Resolve may be swapped for Loader nodes in Fusion Studio, except where stated otherwise.

### Copy Metadata [Meta]

### The Copy Metadata node

### Copy Metadata Node Introduction

Copy Metadata merges, swaps out, or wipes the metadata held in your image. You can inspect metadata through a subview of the viewer.

### Inputs

A pair of inputs sit on the Copy Metadata node, each meant for wiring up a 2D image. Background Input: The orange background input carries the main 2D image that the node sends on. Foreground Input: The green foreground input carries the secondary 2D image holding the metadata you intend to merge into or overwrite onto the background image.

### Basic Node Setup

The Copy Metadata node pulls metadata off the foreground input (green) and writes it onto the background input (orange). What emerges is the background input bearing its altered metadata.

Here a Copy Metadata node lifts metadata off the foreground and bakes it into the background clip Inspector

### The Copy Metadata Controls tab

### Controls Tab

The Controls tab governs the way metadata arriving from the foreground input image gets folded into the background input image. Operation The Operation menu sets how the metadata from the foreground and background inputs is handled.

- Merge (Replace Duplicates): Everything is merged, though where names collide the value is taken from the foreground input.
- Merge (Preserve Duplicates): Everything is merged, though where names collide the value is taken from the background input.
- Replace: The foreground's metadata stands in for the whole of the background's metadata.
- Clear: Every piece of metadata is thrown away.

### Common Controls

Settings Tab The Settings tab in the Inspector also recurs across the other Metadata nodes. A full account of these shared controls sits at the close of this chapter under the "The Common Controls" heading.

### Set Metadata [SMeta]

### The Set Metadata node

### Set Metadata Node Introduction

Set Metadata lets you add fresh Name = Value pairs into the metadata. You can inspect metadata through a subview of the viewer.

### Inputs

The lone input on the Set Metadata node is meant for wiring up a 2D image that will have metadata added to it. Background Input: The orange background input carries the main 2D image that the node sends on with its new metadata.

### Basic Node Setup

The Set Metadata node writes fresh metadata onto the background input (orange). What emerges is the background input carrying the new metadata. Here a Set Metadata node generates fresh metadata and bakes it into the background clip.

### Inspector

### The Set Metadata Controls tab

### Controls Tab

The Controls tab is where you enter the metadata field's name plus the value or information that accompanies the metadata. Field Name The name given to the metadata value. Steer clear of spaces. Field Value The value tied to the name above.

### Common Controls

Settings Tab The Settings tab in the Inspector also recurs across the other Metadata nodes. A full account of these shared controls sits at the close of this chapter under the "The Common Controls" heading.
