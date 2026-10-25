# Ocio color space and ocio display and ocio file transform

Version: DaVinci Resolve 20.3 Reference Manual. Context: Ocio color space, Ocio display, Ocio file transform.
[Chapter index](INDEX.md) / [Previous section](ocio-cdl-transform-and-ocio-color-space.md) / [Next section](set-canvas-color-and-white-balance.md) / [OCIO Color Space OCS](ocio-cdl-transform-and-ocio-color-space.md)
<a id="source-basic-node-setup-3"></a> <a id="source-basic-node-setup-4"></a> <a id="source-controls"></a> <a id="source-controls-tab-4"></a> <a id="source-inputs-3"></a> <a id="source-inputs-4"></a> <a id="source-inspector-2"></a> <a id="source-ocd-display-node-introduction"></a> <a id="source-ocio-display-ocd"></a> <a id="source-ocio-file-transform-controls"></a> <a id="source-ocio-file-transform-node-introduction"></a> <a id="source-ocio-file-transform-ocf"></a> <a id="source-settings-tab-3"></a> <a id="source-settings-tab-4"></a> <a id="source-the-ocio-display-controls"></a> <a id="source-the-ocio-display-node"></a> <a id="source-the-ocio-file-transform-node"></a>

### Settings Tab

The Inspector’s Settings tab here is repeated throughout the remaining Color nodes. A complete description of these common controls waits at the bottom of the chapter, in the “The Common Controls” section.

### OCIO Display [OCD]

### The OCIO Display node

### OCD Display Node Introduction

Use the OCIO Display node to bring an OpenColorIO (OCIO) Display transform (.ocio) onto an input.

### Inputs

That one input on the OCD Display node serves to attach whichever node you mean to put the OCIO Display transform on, along with an effect mask for narrowing the display transform area.

### Basic Node Setup

Wire whatever media or tool you intend to carry the OCIO Display transform into the input. From there the node hands its output off to the rest of the node tree.

A basic node tree in which the OCIO Display node accepts the Media In Node, runs the Display Transform on it, and hands the result to Media Out

### Inspector

### The OCIO Display controls

### Controls

Through the OCIO Display controls you load an .ocio configuration file and push its color space and display transform onto whatever feeds the node’s input.

- OCIO Config File: Hit the Browse button to bring up a file system prompt where you point to the .ocio file.
- Source Space: From the list, pick the color space your source material is in.
- Display: Pick which monitor holds your viewer.
- View: Pick the color space you want to see.

### OCIO File Transform [OCF]

### The OCIO File Transform node

### OCIO File Transform Node Introduction

By means of three OCIO nodes, Fusion hooks into the Open Color IO color management workflow.

- Use the OCIO CDL Transform node to make, keep, reload, and put down a Color Decision List (CDL) grade.
- The OCIO Color Space carries out refined color space conversions according to an OCIO config file.
- Use the OCIO File Transform to import and put to work all sorts of Lookup tables (LUTs).

In broad terms, the OCIO color pipeline is assembled from a series of color transformations described by OCIO-specific config files that conventionally end in a “.ocio” extension. The purpose of these config files is to let color settings be shared inside a facility or between facilities. A user-created environment variable called “OCIO” usually designates the config file to load, though some tools will override it. If no further \*.ocio config files are present, Fusion turns to the DefaultConfig.ocio file in its LUTs directory.

For a deep dive into the internals of the format, head to the official pages on opencolorio.org. The same capability the OCIO File Transform node provides is also on offer via a View LUT node from the View LUT menu.

### Inputs

Two inputs live on the OCIO File Transform node: one for the primary image and one for an effect mask that fences off where the color space conversion gets applied. Input: This orange input is the single connection you cannot skip, routing a 2D image into the LUT. Effect Mask: The optional blue input accepts a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps from elsewhere. Plug a mask in here and the applied LUT reaches only the pixels the mask spans. That effect mask kicks in after the tool has been processed.

### Basic Node Setup

More often than not the OCIO File Transform node follows a Gamut node that has carried the Loader into linear color within Fusion Studio.

An OCIO File Transform node placed on a Loader node once a Gamut node has converted it into linear color space Inspector

### OCIO File Transform controls

### Controls Tab

On the OCIO File Transform node, the Controls tab gives you ways to bring in the LUT, flip the transform, and pick the color interpolation method. LUT File Pops a File > Open dialog so you can load whichever LUT you want.

CCC ID Serving as the ID key, this pinpoints the particular file transform held inside the ASC CDL color correction XML file. Direction Switches between Forward and Reverse. Choosing Forward lays in the corrections the node defines, whereas Reverse works to peel them away. Remember, though, that not all color corrections can be rolled back: imagine each slope value pushed to 0.0 so the picture goes completely black — there is no undoing that, mathematically or on screen. Interpolation Lets you choose the color interpolation that balances quality against render time best. Nearest runs quickest, while Best is the slowest of them.

### Settings Tab

Just like the other Color nodes, this node carries the same Settings tab in its Inspector. The chapter wraps up with the “The Common Controls” section, which documents these shared controls fully.
