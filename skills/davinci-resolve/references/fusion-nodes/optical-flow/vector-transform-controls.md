# Vector transform controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Vector transform.
[Chapter index](INDEX.md) / [Previous section](tween-and-vector-denoise-and-vector-transform.md) / [Vector Transform VXf](tween-and-vector-denoise-and-vector-transform.md) / [Next section](vector-transform-and-vector-warp-and-common-controls.md)
<a id="source-controls-tab-4"></a> <a id="source-optical-flow-part-2"></a> <a id="source-the-vector-transform-controls-tab"></a>

### The Vector Transform Controls tab

### Controls Tab

The Controls tab is where you adjust the Vector Transform settings.

- Smooth UV: Averages each result against the surrounding UV values nearby. Handy for ironing out glitches and stray fluctuations that show up in the UV channels.
- Smooth Vector: Blends vectors together across frames that sit next to each other. Works well as a prep stage ahead of running a Vector Warp that uses a texture map.
- Attenuate UV: Boost, reduce, or null the warp map influence drawn from the vector magnitudes. The same control can also weaken how strong the UV channels are.
- Attenuate Vector: Shortens the motion vector length so you can dial the warping anywhere between its maximum and none at all.
- Center X/Y: Shifts the UV channels to a new position using this control.
- Size X/Y: Rescales the UVs with this control.
- Use Size and Aspect: Tick this box to switch on the parameters that follow. Size: Resizes the picture by the same factor on the X axis and the Y axis. Aspect: Lets you dictate the picture’s aspect ratio.
- Angle: Tweaks the angle applied to the UV.
