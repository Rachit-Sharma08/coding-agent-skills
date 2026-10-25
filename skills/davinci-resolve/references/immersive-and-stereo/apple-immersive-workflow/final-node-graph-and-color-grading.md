# Final node graph and color grading

Version: DaVinci Resolve 20.3 Reference Manual. Context: Apple immersive workflow.
[Chapter index](INDEX.md) / [Previous section](apple-immersive-motion-data-and-select-the-axis-to-view.md) / [Next section](dragging-a-control-point-and-or-right-click-to-delete-a-point.md)
<a id="source-3d-palette"></a> <a id="source-3d-palette-1"></a> <a id="source-color-grading"></a> <a id="source-edge-blend-mode"></a> <a id="source-edge-blend-viewer-controls"></a> <a id="source-noise-reduction"></a> <a id="source-primary-grading"></a> <a id="source-secondaries"></a> <a id="source-sizing"></a> <a id="source-the-final-node-graph"></a>

### The final node graph

In a collaborative setup, you can leave the Fusion page and go on editing, mixing, and grading the immersive timeline within DaVinci Resolve. For immersive turnovers, render each eye out separately as EXRs in ACES AP0 so the fullest set of properties survives for immersive delivery.

### Color Grading

Here we walk through the optical, color, and 3D tools at your disposal while handling immersive media on DaVinci Resolve’s color page. Given how distinctive immersive content is, certain tools simply can’t be used during postproduction. Still others are off the table for now but are being reworked to handle immersive content.

### Noise Reduction

You can still reduce noise while working with immersive video. Inside the Motion Effects palette, Spatial NR studies the noise pattern in the source media so it can cut that noise as far as possible while holding on to the original image detail. 1 From the color page toolbar, open the Motion Effects palette. Within the Spatial NR column you get to pick which noise reduction mode to apply.

- The Faster, Better, and Enhanced modes each carry out their pattern analysis inside a chosen radius size

and shape their output according to the threshold you set. They appear here in ascending order of processing complexity.

- AI UltraNR is an AI-powered noise pattern detector that pulls the noise pattern out of the signal by finding and studying the “flattest’’ region of the frame for pure noise. 2 Switch the spatial noise reduction mode to AI UltraNR.

Spatial Noise Reduction settings

3 Click Analyze. The viewer shows a bounding box marking the “emptiest” patch of pixel data in that frame. Because it holds no real visual content, whatever sits inside the square is perfect for pulling out the digital noise the camera sensor generates.

The bounding box for AIUltraNR. The bounding box can be moved and resized in the viewer should you want, yet it usually isn’t a good idea—AI UltraNR spots the best analysis regions more reliably than our eyes do. You’re also free to tweak the Noise Profile Luma and Chroma Threshold settings by hand, but once more, AI UltraNR generally lands on the right blend of thresholds for clean noise reduction on its own.

### Primary Grading

Primary color grading behaves exactly as it would on ordinary video footage. Apply the same thinking around normalization, balancing, and matching as you work the primaries color and log wheels, the HDR palette, and the HSL Curves. Likewise, the Color Slice and Color Warper palettes behave as you’d expect.

### Secondaries

Selection approaches that work at the pixel level, such as the Qualifier, behave as expected on immersive media. Object- or window-based selection can stay accurate only inside a flat equirectangular (or viewport) environment, so most secondary techniques demanding a precise qualification shape are off the table for the moment. That covers Power Windows (and, by extension, the Tracker palette) along with the Magic Mask tool.

### Sizing

Immersive content offers no sizing controls at all (that is, zooming and panning).

### 3D Palette

On the color page, the 3D palette carries controls for handling an assortment of 3D camera and graphics formats. In contrast to other stereoscopic formats, there’s no need to tune the alignment of the eyes here, since the Blackmagic URSA Cine Immersive camera lenses, focal length, and irises are all fixed.

### 3D palette

Reserved solely for immersive content, the Edge Blend mode lets you reshape and soften the outer rim of the immersive video frame. You can put it to work hiding film gear that would otherwise show and reining in how far the observer can see. Past that edge, the observer takes in the backdrop.

- Open the 3D palette.
- Over in the upper right corner, switch the mode to Edge Blend.

### Edge Blend Mode

- Confirm the viewer’s onscreen controls are switched to Edge Blend.

### Edge Blend Viewer Controls

A ring of control points should appear around the edge of the video frame, with an anchor handle sitting at its center.

- Drag a control point to move it.
