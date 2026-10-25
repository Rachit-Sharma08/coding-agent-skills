# Fields fields node introduction

Version: DaVinci Resolve 20.3 Reference Manual. Context: Fields.
[Chapter index](INDEX.md) / [Previous section](custom-tool-neighborhood-filter.md) / [Next section](fields-and-frame-average.md)
<a id="source-fields-flds"></a> <a id="source-fields-node-introduction"></a> <a id="source-miscellaneous-nodes-part-2"></a> <a id="source-the-fields-node"></a>

### Fields [FLDs]

### The Fields node

### Fields Node Introduction


The Fields node is a sturdy all-around tool that bundles a number of operations tied to interlaced video frames. It can interpolate video fields up into frames or break video frames down into fields. Even though the interlace preference and method type gets set in the MediaIn or Loader, and generators, you can lean on this node to help with PAL-to-NTSC standards conversion, and it lets you process fields and frames over particular stretches of a node tree. The node is likewise able to weave two distinct images into one interlace image. Here the background input acts as the dominate field 1 while the foreground stands in as field 2.
