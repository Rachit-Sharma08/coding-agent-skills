# Planar transform a planar transform creating a match move

Version: DaVinci Resolve 20.3 Reference Manual. Context: Planar transform.
[Chapter index](INDEX.md) / [Previous section](letterbox-and-planar-transform.md) / [Next section](resize.md) / [Planar Transform PXF](letterbox-and-planar-transform.md)
<a id="source-a-planar-transform-creating-a-match-move"></a> <a id="source-common-controls-4"></a> <a id="source-controls-tab-4"></a> <a id="source-inspector-4"></a> <a id="source-the-planar-transform-controls-tab"></a>

### A Planar Transform creating a match move

### Inspector

### The Planar Transform Controls tab

### Controls Tab

There are only a handful of controls on the Planar Transform node, and all of them sit on the Controls tab. It exists to take the analyzed Planar Tracking data and lay it down as a match move. Reference Time This refers to the moment in time from which the pattern was sampled in the Planar Tracker node that generated the Planar Transform. Right-Click Here for Track Spline The Track spline holds the perspective-distortion data, kept as 4 x 4 matrices. When a Planar Transform node is exported out of a Planar Tracker node, the Track spline the Planar Tracker produced is shared by linking it to the Planar Transform node. One upshot of sharing the Track spline this way is that altering the track inside the Planar Tracker node automatically refreshes the Planar Transform. Keep in mind that you can inspect this spline in the Spline Editor, which helps reveal how many frames were tracked.

### Common Controls

Settings Tab Other Tracking nodes carry a copy of the same Settings tab found here in the Inspector. You will find a full account of these shared controls under the “The Common Controls” section at this chapter's close.
