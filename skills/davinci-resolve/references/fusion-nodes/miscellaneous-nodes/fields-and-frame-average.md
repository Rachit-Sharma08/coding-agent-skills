# Fields and frame average

Version: DaVinci Resolve 20.3 Reference Manual. Context: Fields, Frame average.
[Chapter index](INDEX.md) / [Previous section](fields-fields-node-introduction.md) / [Next section](frame-average-and-keyframe-stretcher-and-run-command.md) / [Fields FLDs](fields-fields-node-introduction.md)
<a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-common-controls"></a> <a id="source-controls-tab"></a> <a id="source-frame-average-avg"></a> <a id="source-frame-average-node-introduction"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-inspector"></a> <a id="source-operatiion-controls"></a> <a id="source-operation-menu"></a> <a id="source-process-mode"></a> <a id="source-process-mode-menu"></a> <a id="source-the-fields-controls-tab"></a> <a id="source-the-frame-average-node"></a>

### Inputs

The lone input on the Fields node lets you hook up a 2D image plus an effect mask, the latter handy for confining the blurred area. Stream1 Input: This orange background input takes the primary 2D image to be interpolated or converted. Stream2 Input: This optional green foreground input comes into play solely when you’re combining a pair of interlaced images.

### Basic Node Setup

The Fields node shown below takes the background image and turns it from a PAL interlaced format into progressive frames.

You can shift the background image into a range of interlaced formats.

### Inspector

### The Fields Controls tab

### Controls Tab

Two menus sit within the Controls tab. You pick the kind of field conversion to carry out from the Operation menu. The Process Mode menu, meanwhile, sets the field’s format for the resulting output image.

### Operatiion Controls

### Operation Menu

- Do Nothing: Leaves the images to be governed by the Process Mode selection and nothing else.
- Strip Field 2: Drops field 2 out of the input image stream, cutting the image down to half its original height.
- Strip Field 1: Drops field 1 out of the input image stream, cutting the image down to half its original height.
- Strip Field 2 and Interpolate: Drops field 2 from the input image stream and swaps in a field interpolated from field 1, keeping image height intact. Feed it frames rather than fields.
- Strip Field 1 and Interpolate: Drops field 1 from the input image stream and swaps in a field interpolated from field 2, keeping image height intact. Feed it frames rather than fields.
- Interlace: Merges fields drawn from the input image stream(s). Given a single image stream, every pair of frames merges into half as many double-height frames. Given two image streams, one frame from each merges into double-height images.
- De-Interlace: Splits the fields out of one input image stream. The result is twice as many half-height frames.

Reverse Field Dominance Turning this on flips the image’s Field Order or Dominance.

### Process Mode

### Process Mode Menu

- Full Frames: Compels Frame Processing. Handy when you need to process frames within a node tree region that otherwise runs field processing.
- NTSC Fields: Compels NTSC Field Processing. Handy when you need to process fields within a node tree region that otherwise runs frame processing.
- PAL Fields: Compels PAL Field Processing. Handy when you need to process fields within a node tree region that otherwise runs frame processing.
- PAL Fields (Reversed): Compels PAL-swapped Field Processing.
- NTSC Fields (Reversed): Compels NTSC-swapped Field Processing.
- Auto: Tries to mirror the mode of whatever input images arrive. When the input types are a mix, it falls back to Fields.

### Common Controls

Settings Tab You’ll find the Settings tab in the Inspector echoed across the other miscellaneous nodes as well. Full descriptions of these common controls appear later, in this chapter’s closing “The Common Controls” section.

### Frame Average [Avg]

### The Frame Average node

### Frame Average Node Introduction

The Frame Average node blends a run of frames together to mimic footage captured at long shutter speeds. Beyond motion blur-style looks, it can come in handy for time warps or stripping out noise.

### Inputs

The sole input on the Frame Average node is where you attach the 2D image that the averaging gets applied to. Input: The orange input carries the primary 2D image destined for averaging.

### Basic Node Setup

Whatever image feeds the orange input gets frame averaged according to the Inspector settings.

A Frame Average node merges the frames of the input image.
