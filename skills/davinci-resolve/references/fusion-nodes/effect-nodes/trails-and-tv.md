# Trails and tv

Version: DaVinci Resolve 20.3 Reference Manual. Context: Trails, Tv.
[Chapter index](INDEX.md) / [Previous section](trails-accumulation-and-blending-controls.md) / [Next section](tv-and-common-controls.md) / [Trails TRLS](rays-and-shadow-and-trails.md)
<a id="source-basic-node-setup"></a> <a id="source-common-controls"></a> <a id="source-controls-tab"></a> <a id="source-input"></a> <a id="source-the-tv-node"></a> <a id="source-tv-node-controls"></a> <a id="source-tv-node-introduction"></a> <a id="source-tv-tv"></a>

### Common Controls

Settings Tab Since the Settings tab controls are shared by every Effect node, you'll find their write-ups in the “The Common Controls” section closing out this chapter.

### TV [TV]

### The TV node

### TV Node Introduction

The TV node is a basic node built to reproduce a few of the everyday defects you'd spot in analog television broadcasts and on their screens. Within DaVinci Resolve this Fusion-specific node is largely redundant now, thanks to the more capable Analog Damage ResolveFX.

### Input

The TV node's two inputs serve to attach a 2D image plus an effect mask, the latter handy for confining where the TV effect shows up. Input: The orange input takes the main 2D image that the TV distortion gets applied to. Effect Mask: The blue input accepts a mask shape built from polylines, simple primitive shapes, paint strokes, or bitmaps drawn from other tools. Wiring a mask into this input restricts the zone in which the TV effect to appears. Any effects mask gets applied to the tool once the tool itself has been processed.

### Basic Node Setup

An image's output gets wired into the TV node's input. From there you shape the flavor of TV interference through the controls over in the Inspector.

The TV node reproduces television-style defects across whatever image is wired into its orange input Inspector

### TV node controls

### Controls Tab

The Controls tab is the first among three tabs for tailoring the analog TV distortion. This one reworks the effect's scan lines and image distortion. Scan Lines This slider recreates the interlaced look by knocking lines out of the picture. Set it to black with a transparent Alpha and a line drops. A value of 1 (default) removes every other line. A value of 2 keeps one line, then drops the next two, and repeats that pattern. A value of zero switches the effect off. Horizontal Reach for this slider to nudge the picture with a plain Horizontal offset. Vertical Reach for this slider to nudge the picture with a plain Vertical offset. Skew This slider lays a diagonal offset on the picture. Positive values lean the image toward the top left, negative values toward the top right. Pixels shoved past the frame wrap around and resurface on the picture's far side. Amplitude The Amplitude slider lets you bring smooth sine-wave-style deformation to the picture's edges. Crank the value up and the deformation grows more intense. Lean on the Frequency control to govern how often the distortion repeats.

Frequency The Frequency slider fixes the frequency of the sine wave that warps the picture's edges once the amplitude control rises past 1. Offset Use Offset to shift the sine wave's position, which drives the deformation the Amplitude and Frequency controls apply to ripple across the picture.
