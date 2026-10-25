# Ultra keyer inputs

Version: DaVinci Resolve 20.3 Reference Manual. Context: Ultra keyer.
[Chapter index](INDEX.md) / [Previous section](relight-and-ultra-keyer.md) / [Next section](ultra-keyer-and-common-controls.md) / [Ultra Keyer UKY](relight-and-ultra-keyer.md)
<a id="source-inputs-1"></a> <a id="source-matte-nodes-part-6"></a>

### Inputs


Four separate inputs appear on the Ultra Keyer node within the Node Editor. Input: A 2D image carrying the color you intend to key for transparency is fed into the orange input. Garbage Matte: A mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks is taken by the gray garbage matte input. When you wire a mask here, any portion of the picture sitting inside that matte becomes transparent. That garbage matte goes straight onto the image's alpha channel. Solid Matte: A mask shape produced by polylines, basic primitive shapes, paint strokes, or bitmaps masks is accepted by the white solid matte input. Wiring a mask into it forces whatever region of the picture lies within the matte to render fully opaque. Effect Mask: This optional blue input looks for a mask shape generated from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Hooking a mask up here restricts the pixels in which keying takes place. An effects mask gets applied to the tool once that tool has finished processing.
