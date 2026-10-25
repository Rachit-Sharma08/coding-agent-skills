# Color gain gain tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Color gain.
[Chapter index](INDEX.md) / [Previous section](color-curves-and-color-gain.md) / [Next section](color-gain-and-color-matrix.md) / [Color Gain Clr](color-curves-and-color-gain.md)
<a id="source-color-gain-controls"></a> <a id="source-color-nodes-part-4"></a> <a id="source-gain-tab"></a> <a id="source-inspector-1"></a>

### Inspector

### Color Gain controls

### Gain Tab


Through the Gain tab you govern the separate RGBA Lift/Gamma/Gain parameters. Such controls let you swiftly correct uneven color casts confined to particular channels. Lock R/G/B Switch this on and the Red, Green, and Blue channel controls for each effect collapse into a single slider. Effects on the Alpha channel stay independent. Gain RGBA What the Gain RGBA controls do is scale the image channel's values linearly. Every pixel gets the same multiplier, yet the result shows up more on bright pixels and less on dark ones. A black pixel won't budge, since any number times 0 always yields 0. Lift RGBA Whereas Gain pivots the color values around black, Lift pivots them around white. This control's value is multiplied into the pixel values. Set Lift to 0.5 and a pixel reading R0.0 G0.0 B0.0 becomes R0.5 G0.5, B0.5, while white pixels stay completely untouched. Lift bears down on the lower values more than the higher ones, so its grip is firmest across an image's low and middle tones. Gamma RGBA The Gamma RGBA controls steer the brightness of the image's midrange. This node behaves nonlinearly. Adjusting gamma leaves the image's white and black pixels alone, while the pure grays feel the most from changes to this parameter. Push this control hard and midrange pixels tend to get driven toward black or white, depending on the value you choose.

Pre-Divide/Post-Multiply Tick this checkbox and the image's pixel values are divided by the Alpha values ahead of the color correction, then multiplied by the Alpha value again once the correction is done. It comes in handy when you're trying to color correct images carrying premultiplied Alpha channels.
