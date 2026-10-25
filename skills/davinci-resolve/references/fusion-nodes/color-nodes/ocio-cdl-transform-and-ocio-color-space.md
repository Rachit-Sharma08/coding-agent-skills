# Ocio cdl transform and ocio color space

Version: DaVinci Resolve 20.3 Reference Manual. Context: Ocio cdl transform, Ocio color space.
[Chapter index](INDEX.md) / [Previous section](gamut-and-hue-curves.md) / [Next section](ocio-color-space-and-ocio-display-and-ocio-file-transform.md)
<a id="source-basic-node-setup-1"></a> <a id="source-basic-node-setup-2"></a> <a id="source-controls-tab-2"></a> <a id="source-controls-tab-3"></a> <a id="source-inputs-1"></a> <a id="source-inputs-2"></a> <a id="source-ocio-cdl-transform-node-introduction"></a> <a id="source-ocio-cdl-transform-oct"></a> <a id="source-ocio-color-space-controls"></a> <a id="source-ocio-color-space-node-introduction"></a> <a id="source-ocio-color-space-ocs"></a> <a id="source-ocio-transform-controls"></a> <a id="source-offset"></a> <a id="source-settings-tab-2"></a> <a id="source-slope"></a> <a id="source-the-ocio-cdl-transform-node"></a> <a id="source-the-ocio-color-space-node"></a>

### OCIO CDL Transform [OCT]

### The OCIO CDL Transform node

### OCIO CDL Transform Node Introduction

Three OCIO nodes are how Fusion plugs into the Open Color IO color management workflow.

- With the OCIO CDL Transform node you can build, store, retrieve, and lay down a Color Decision List (CDL) grade.
- The OCIO Color Space handles advanced color space conversions, driven by an OCIO config file.
- The OCIO File Transform lets you bring in and apply an assortment of Lookup tables (LUTs).

As a rule, the OCIO color pipeline is built up out of a collection of color transformations spelled out in OCIO-specific config files, which usually carry a “.ocio” extension. Such config files give you a way to pass color settings around inside a facility or across several. Which config file gets loaded is ordinarily pointed to by a user-created environment variable named “OCIO,” although certain tools let you override that. Should no other \*.ocio config files turn up, the system falls back on the DefaultConfig.ocio file in Fusion’s LUTs directory.

To dig into how the format works under the hood, consult the official pages over at opencolorio.org.

### Inputs

There are two inputs on the OCIO CDL Transform node: one for the primary image and one for an effect mask that bounds the region in which the CDL takes effect. Input: The orange input is the only connection you must make, feeding a 2D image output into the CDL grade. Effect Mask: This optional blue input accepts a mask shape made from polylines, simple primitive shapes, paint strokes, or bitmaps coming out of other tools. Hook a mask up here and the CDL grade is held to just the pixels inside the mask. That effect mask takes effect after the tool has run its processing.

### Basic Node Setup

You will commonly drop the OCIO CDL Transform node downstream of a Gamut node that has already taken the Loader into linear color inside Fusion Studio.

An OCIO CDL Transform node sitting on a Loader node, once a Gamut conversion has brought it to linear within Fusion Studio Inspector

### OCIO Transform controls

### Controls Tab

On the OCIO CDL Transform, the Controls tab holds primary grading color correction controls laid out in a CDL-friendly format. R, G, B tweaks are driven by Slope, Offset, and Power, and there is a global Saturation control as well. This same tab also lets you bring CDL-compatible adjustments in and send them back out. Operation The menu flips between File and Controls. Pick File mode to load standard ASC-CDL files; pick Controls mode to set Slope, Offset, Power, and Saturation by hand and to write out the CDL file. NOTE: In DaVinci Resolve terms, slope behaves much like gain, steering the mids-to-high contrast. Offset shifts the whole color balance and exposure, and Power resembles contrast pivoting on a raised point, handing you command over shadow contrast. Direction Flips between Forward and Reverse. Forward lays down the corrections set in the node; Reverse attempts to back them out. Bear in mind that some color corrections simply cannot be reversed — picture every slope value driven to 0.0, which yields a wholly black image. Undoing that is impossible, in math and on screen alike.

### Slope

### Offset

Multiplying the color values, Slope does the very thing that Gain does over in the Brightness Contrast node.

Offset adds onto the color values, matching what Brightness does within the Brightness Contrast node. Power Lays a Gamma Curve over the image, working as the inverse of the Gamma function found in the Brightness Contrast node.

Saturation Raises or lowers the color saturation, operating exactly as Saturation does in the Brightness Contrast node. Export File Lets you write the current settings out to a CDL file.

### Settings Tab

Other Color nodes share the very same Settings tab within the Inspector. For a detailed breakdown of these shared controls, turn to the chapter’s final “The Common Controls” section.

### OCIO Color Space [OCS]

### The OCIO Color Space node

### OCIO Color Space Node Introduction

Fusion taps the Open Color IO color management workflow through a trio of OCIO nodes.

- The OCIO CDL Transform node lets you author, save off, bring back, and apply a Color Decision List (CDL) grade.
- Sophisticated conversions between color spaces, governed by an OCIO config file, come from the OCIO Color Space.
- Loading and applying a range of Lookup tables (LUTs) is the job of the OCIO File Transform.

For the most part, the OCIO color pipeline takes shape from a group of color transformations laid out in OCIO-specific config files, typically bearing a “.ocio” extension. These config files exist so color settings can travel within one facility or among many. Normally a user-created environment variable named “OCIO” points at whichever config file should load, though a handful of tools permit overriding that. When no other \*.ocio config files can be found, the DefaultConfig.ocio file in Fusion’s LUTs directory steps in. Anyone wanting a thorough account of the format’s inner workings should look to the official opencolorio.org pages. You can grab example configs at https://opencolorio.readthedocs.io/en/latest/ configurations/\_index.html#configurations What the OCIO Color Space node does can equally be had through a View LUT node reached from the View LUT menu.

### Inputs

The OCIO Color Space node carries two inputs: one for the primary image and another for an effect mask that pins down where the color space conversion happens. Input: Colored orange, this is the lone required hookup, supplying a 2D image to the color space conversion. Effect Mask: This optional blue input takes a mask shape drawn from polylines, basic primitive shapes, paint strokes, or bitmaps produced elsewhere. Attach a mask here and the color space conversion is limited to the pixels under that mask. The effect mask is applied once the tool has done its work.

### Basic Node Setup

As a rule the OCIO Color Space node goes right behind a MediaIn node in DaVinci Resolve, or behind a Loader node in Fusion Studio. A companion OCIO Color Space node then sits immediately ahead of a Media Out node in DaVinci Resolve, or ahead of a Saver node in Fusion Studio.

An OCIO Color Space node wired across both a Loader node and a Saver node inside Fusion Studio Inspector

### OCIO Color Space controls

### Controls Tab

For the OCIO Color Space node, the Controls tab moves an image out of one color space and into another according to an OCIO config file. Out of the box it draws on the config file that ships with Fusion, but the Controls tab will just as readily let you load a config file of your own. OCIO Config Brings up a File > Open dialog so you can load whichever config file you want. Source Space The source color spaces on offer here come straight from the config file. Since this list reflects nothing but the loaded profile, its contents can differ enormously. With no other OCIO config file loaded, the DefaultConfig.ocio file in Fusion’s LUTs directory fills this menu.

Output Space The output color spaces you can pick from here likewise derive from the config file. Because the listing depends purely on the loaded profile, it too can range widely. When no other OCIO config file has been loaded, this menu is populated from the DefaultConfig.ocio file in Fusion’s LUTs directory. Look Whatever OCIO Color Transform Looks you have installed turn up in this menu; if none are installed, the menu shows only None.
