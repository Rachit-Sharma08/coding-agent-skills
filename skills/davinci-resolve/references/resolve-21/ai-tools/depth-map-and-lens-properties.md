# Depth map and lens properties

Version: DaVinci Resolve 21 New Features Guide. Context: Ai tools.
[Chapter index](INDEX.md) / [Previous section](speech-generator-custom-voices-and-voice-convert.md) / [Next section](additional-grain-and-ai-face-age-transformer.md)
<a id="source-aperture"></a> <a id="source-depth-map"></a> <a id="source-foreground-edge-overlap"></a> <a id="source-lens-distortion"></a> <a id="source-lens-properties"></a> <a id="source-remove-and-replace-grain"></a>

### Depth Map

With this toolset you tweak the Depth Map, surfacing a simulated depth inside a 2D image. Reaching for the Depth mode view above can show you these tools’ results in finer detail.

- Source: Pick Internal to build a Depth Map within the CineFocus tool, or From Alpha Input if you’ve made a Depth Map in another node.
- Quality: Decide whether to favor speed (Faster) or quality (Better).
- Invert: Tick this box to flip the Depth Map, swapping what counts as near versus far in

the image.

- Adjust Map Levels: Tick this box to fine-tune the Depth Map and switch on the toolset below.

Far Limit: Tunes the Depth Map’s black levels, setting the cap on how “far away” the map reaches. Near Limit: Tunes the Depth Map’s white levels, setting the cap on how “close up” the map reaches. Gamma: Tunes the Depth Map’s gamma curve, letting you decide the relative “distances” between near and far objects.

- Post Processing: Tick this box to make tweaks to the black-and-white Depth Map and switch on the toolset below. Post Filter: Drag this slider to ease the Depth Map smooth following the contours of the image. Contract / Expand: Drag this slider to pull in or push out the Depth Map’s white foreground areas. Blur: Drag this slider to soften the Depth Map, a help where it carries jagged edges in need of smoothing, though it can throw off artifacts at the borders of image objects. Reach for this option only when repairing a troublesome depth map Separate Layers: Drag this slider to crisp up the depth edges wherever one object stands in front of another. This can help tease distances apart on depth maps that aren’t quite sharp. With an external Depth Map in play, be sure this stays at 0.0.

### Lens Properties

With this toolset you nudge the virtual lens toward being less than perfect. That yields a more realistic result and makes matching the traits of a real lens easier.

- Chromatic Aberration: Tick this box to mimic Chromatic Aberration, the fact that different frequencies of light come to focus at different depths. Strength: Tunes how strong the color separation is. Phase: Tunes the relative bending of the various frequencies, hinging on the lens optics.
- Spherical Aberration: Tick this box to mimic Spherical Aberration, the fact that large apertures can spread the focal point across a range of differing depths. Lens Model: Pick the lens construction type to mimic. Strength: Tunes the light dispersion.

### Aperture

With this toolset you tune the virtual lens’s Aperture traits. Reaching for the Aperture mode view above can show you these tools’ results in finer detail

- Shaped Bokeh: Tick this box to tune the virtual lens’s Bokeh and unlock the toolset below. Leaving this box unticked yields perfectly circular Bokeh. Number of Blades: Move the slider to set how many blades the virtual lens’s aperture has. Each blade reshapes the Bokeh accordingly. Rotation: Move it to spin the aperture shape left or right. Curvature: Tunes the curve of the aperture blades. Pinwheel: Tunes how much of the blade tips show. The Pinwheel name points to a ratchet-style shape inside the bokeh (those out-of-focus highlights) that some lenses show at wide-aperture, looking like a pinwheel fan.
- Anamorphic Lens: Tick this box to give the Bokeh an anamorphic shape. Anamorphism: Move this slider to set how much anamorphic stretch is applied.

### Lens Distortion

With this toolset you tune the virtual lens’s distortion traits. This recreates the fact that lenses build Bokeh at differing sizes depending on its distance from the lens center.

- Curved Lens: Tick this box to lay artificial curvature onto the lens and switch on the toolset below. Curvature: Tune the strength of the distortion around the frame’s edges. Lateral Aberration: Tunes the color distortions within the blurring at the frame’s edges. Phase: Tunes the relative spread of the various colors, hinging on the lens optics.

### Foreground Edge Overlap

With this toolset you set how the foreground edge overlap blends into the rest of the image. Where the foreground doesn’t overlap, these tools do nothing. In a real optical system, objects sitting close to the lens get “blurred-out” and turn transparent. As an example, hold the tip of a pen pointing up close to your eye and you can see straight through it. That physics doesn’t carry over to 2D video, so these tools offer a workaround that fakes the phenomenon.

- Overlap Preview: Tick this box to spot where the foreground edge overlaps the rest of the image.
- Overlap Boost: Move this slider to make the overlapping foreground denser so it better hides the transition edge. You can only reach this tool when Automatic Edge Handling is switched off.
- Automatic Edge Handling: Tick this box to build clean defocused overlaps on its own, at the price of some background detail in the overlapping regions. Using this tool switches off Overlap Boost.

### Remove and Replace Grain

In real footage, film grain and video noise stay independent of depth of field, scattered evenly throughout the frame. As the CineFocus tool blurs the background, the grain across those regions blurs out too, yet partially-blurred grain lingers through the slightly-blurred regions (hinging on the blur and the grain), which becomes awkward to handle afterward. With this toolset you can first strip grain out of the image to defocus the background more accurately, then drop it back in once the defocus is done, for the look of an image that had defocus by depth before it was ever captured to film

- Remove Grain: Ticking this box switches on the Remove and Replace toolset.
- Grain Detection: Pick the method that studies and strips the grain. Enhanced Spatial, or

AI Ultra Noise Reduction.

- Estimate Best Thresholds: With AI Ultra Noise Reduction picked above, this button is yours to press

so the AI can work out the grain vs detail threshold.

- Split Luma Chroma Thresholds: Tick this box to set separate grain thresholds for Luma and

Chroma signals.

- Threshold: Move this slider to set the dividing line between what counts as grain and what counts as edge detail.
- Preview Grain: Tick this box to see a preview of just the grain in the viewer, making it easier

to gauge what the parameters in this toolset are doing.

- Replace Grain After Defocus: Tick this box to drop all the grain you just stripped back into the

defocused areas once processing is done.

- Grain Replacement: Lets you decide just how much of the grain gets added back.
