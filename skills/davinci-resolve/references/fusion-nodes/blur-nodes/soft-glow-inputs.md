# Soft glow inputs

Version: DaVinci Resolve 20.3 Reference Manual. Context: Soft glow.
[Chapter index](INDEX.md) / [Previous section](sharpen-and-soft-glow.md) / [Next section](soft-glow-and-unsharp-mask.md) / [Soft Glow SGlo](sharpen-and-soft-glow.md)
<a id="source-blur-nodes-part-2"></a> <a id="source-inputs-5"></a>

### Inputs


Much like the Glow node, Soft Glow carries three connections too: an orange one feeding the main image, a blue one for an effect mask, plus a white one dedicated to a Glow mask. Input: Feed the primary 2D image for the soft glow into the orange connection. Effect Mask: Into the blue connection goes a mask shape that polylines, simple primitive shapes, paint strokes, or bitmaps from other tools can produce. Attaching a mask here confines the soft glow to just the pixels inside the mask. Such an effect mask takes hold on the tool once processing has finished. Glow Mask: Pre-masking through the white glow mask input is supported by the Soft Glow node. A Glow pre-mask runs a filter over the image before the soft glow is laid down. After that, the soft glow gets composited back atop the original image. That behavior contrasts with an ordinary effect mask, which crops the finished render. With a Glow mask, the soft glow may spill past the mask edges, even though the soft glow's source stays confined to pixels inside the mask. In all other ways, Glow masks behave just like effect masks.
