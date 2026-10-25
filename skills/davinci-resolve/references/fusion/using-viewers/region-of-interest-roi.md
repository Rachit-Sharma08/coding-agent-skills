# Region of interest roi

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using viewers.
[Chapter index](INDEX.md) / [Previous section](viewer-guides-and-frame-format.md) / [Next section](enabling-roi-controls-and-while-the-roi-is-active.md)
<a id="source-region-of-interest-roi"></a> <a id="source-using-viewers-part-3"></a>

### Region of Interest (RoI)


A rectangular region akin to the Domain of Definition, the Region of Interest is often shortened to RoI. Yet whereas the DoD informs the node which pixels truly exist within the picture, the RoI informs the node which pixels genuinely have to be rendered. As a node renders, it overlaps the present RoI against the present DoD so as to work out which pixels ought to be touched.
