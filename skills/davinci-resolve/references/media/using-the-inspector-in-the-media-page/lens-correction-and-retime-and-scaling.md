# Lens correction and retime and scaling

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the inspector in the media page.
[Chapter index](INDEX.md) / [Previous section](the-inspector-and-adjusting-media-pool-clips-in-the-inspector.md) / [Next section](bands-1-and-6-and-bands-2-through-5.md)
<a id="source-audio"></a> <a id="source-clip-eq-graph"></a> <a id="source-clip-eq-in-the-audio-inspector"></a> <a id="source-equalizer"></a> <a id="source-lens-correction"></a> <a id="source-master-eq-controls"></a> <a id="source-retime-and-scaling"></a> <a id="source-super-scale"></a> <a id="source-the-audio-inspector-parameters"></a> <a id="source-the-clip-eq-graph-with-user-draggable-handles"></a> <a id="source-the-super-scale-parameters"></a>

### Lens Correction

The Lens Correction section sitting within the Video Inspector panel The Lens Correction group (offered only in Resolve Studio) holds two controls with which you correct lens distortion in the image, or introduce lens distortion of your own.

- Analyze: Automatically inspects the frame in the Timeline at the playhead’s spot for edges bent by a wide angle lens. A click on the Analyze button drives the Distortion slider to deliver an automatic correction. While you analyze an especially tough clip, a progress bar appears to indicate how long it’ll take.
- Distortion: Dragging this slider rightward lets you apply a warp to the image by hand so you can straighten the bent regions of the picture that wide angle lenses can introduce. If you clicked the Analyze button and got an overcorrection, dragging this slider leftward lets you ease off the automatic adjustment until the image looks right.

### Retime and Scaling

The Retime and Scaling section sitting within the Video Inspector panel The Retime and Scaling group holds four parameters bearing on retiming quality and clip scale:

- Retime Process: Lets you pick a default way of processing clips in mixed frame rate timelines and those carrying speed effects (fast forward or slow motion), on a clip-by-clip basis. The default is “Project Settings,” so every speed-effected clip gets handled identically.

Three options exist: Nearest, Frame Blend, and Optical Flow, laid out in fuller detail in the Speed Effect Processing section, refer to Chapter 51, “Speed Effects.”

- Motion estimation mode: While using Optical Flow to process speed change effects or clips whose frame rate differs from the Timeline’s, the Motion Estimation pop-up lets you pick the best-looking rendering option for a given clip. Each method brings its own artifacts, and the top-quality option isn’t always the right pick for a particular clip. The default is “Project Settings,” so every speed-effected clip gets handled identically. Several options exist. The “Standard Faster” and “Standard Better” settings are the very ones carried over from earlier versions of DaVinci Resolve. They lean lighter on the processor and turn out good quality fit for most situations. That said, “Enhanced Faster” and “Enhanced Better” ought to produce better results in just about every case where the standard options show artifacts, though they cost more computationally and so run slower on most systems.
- The “Standard Faster” and “Standard Better” options are the same ones that earlier DaVinci Resolve releases offered. Being easier on the processor, they deliver solid quality suitable for the majority of cases. Even so, “Enhanced Faster” and “Enhanced Better” should give superior output nearly everywhere the standard options reveal artifacts, the trade-off being heavier computation and therefore slower performance on most systems.
- “Speed Warp Faster and “Speed Warp Better” are on hand for even higher-quality slow motion effects by way of the DaVinci Neural Engine. How well this setting performs depends on a clip’s content, but under ideal conditions it’ll deliver greater visual quality with fewer artifacts than even the Enhanced Better setting.
- Scaling: Lets you set how clips that don’t match the current project resolution get handled on a clip-by-clip basis. The default is “Project Settings,” so all mismatched clips share the same method of being resized automatically.

That said, a clip-specific method of automatic scaling can be chosen for any clip too. Your options here are Crop, Fit, Fill, and Stretch; for more, refer to the 2D Transforms sectionm, see Chapter 152, “Sizing and Image Stabilization.”

- Resize Filter: For clips being resized in any fashion, this setting lets you pick the filter method used to interpolate image pixels while resizing clips. Different settings suit different kinds of resizing. Four options exist: Sharper: As a rule the top-quality pick on projects whose clips have to be enlarged to fill a bigger frame size, or shrunk down to HD resolutions. Smoother: May deliver higher quality on projects whose clips have to be shrunk to fit an SD resolution frame size. Bicubic: Although the Sharper and Smoother options edge ahead in quality, Bicubic stays an exceptionally fine resizing filter and asks less of the processor than either of those. Bilinear: A lower quality setting that asks less of the processor. Useful when you preview your work ahead of rendering on an underpowered computer, after which you can switch over to one of the higher quality options. Other Resize Methods: A set of specific resize algorithms is on offer should you need them to line up with other VFX workflows.

### Super Scale

### The Super Scale parameters

For times when you need upscaling of higher quality than the standard Resize Filters provide, you can now switch on one of the “Super Scale” options in the Inspector. Unlike reaching for one of the many scaling options across the Edit, Fusion, or Color pages, Super Scale genuinely raises the source resolution of the clip being processed; that clip thus ends up holding more pixels than it had and becomes heavier on the processor to work with than it was, short of optimizing the clip (which bakes the Super Scale effect into the optimized media) or caching the clip somehow.

For fuller detail on Super Scale, refer to Chapter 11, “Image Sizing and Resolution Independence.”

Working Super Scale in the Inspector is, functionally, the same as configuring those identical controls on the media clip via the Clip Attributes. That means changing this setting affects every additional edit referencing the selected media as well. The Super Scale group carries these parameters touching quality and clip scale:

- Super Scale: Lets you pick how much scaling you need. The options are 2-3-4x and 2-3-4x Enhanced.
- Sharpness: Lets you pick how much detail the scaling carries. This is capped at Low, Medium, or High, unless the Super Scale mode sits on Enhanced, which lets you apply variable sharpness. You’ll want to weigh this setting against Noise Reduction.
- Noise Reduction: Lets you pick how much noise reduction the scaling carries. This is capped at Low, Medium, or High, unless the Super Scale mode sits on Enhanced, which lets you apply variable noise reduction. You’ll want to weigh this setting against Sharpness.

### Audio

The Audio tab holds four audio controls commonly used for video editing, namely Clip Volume, Clip Pan, Clip Pitch, and Clip Equalizer.

- Clip Volume: Each clip carries a single volume control matching the volume overlay across each audio clip.
- Clip Pan: (Surfaced only for clips) A plain Pan slider that governs stereo panning.
- Clip Pitch: Lets you shift a clip’s pitch while leaving the speed alone. A pair of sliders set clip pitch by semi tones (coarse moves, a twelfth of an octave) and by cents (fine moves, 100th of a semi tone).

### Equalizer

This six-band parametric equalizer offers both graphical and numeric controls for boosting or cutting various ranges of frequencies inside that clip, before it even reaches the EQ built into the Mixer. Every band provides its own controls — filter type (Bell, Lo-Shelf, Hi-Shelf, Notch), Frequency, Gain, plus Q-factor (how sharp the band is) — and which of those controls appear on a given EQ band depends on the filter type in use.

### The Audio Inspector parameters

TIP: You may copy Clip EQ settings and paste them across from one Clip EQ onto another, as well as back and forth between Clip EQ and Track EQ instances.

### Clip EQ in the Audio Inspector

### The Clip EQ graph with user-draggable handles

### Master EQ Controls

The Equalizer window carries these overall controls in its upper right and left corners:

- Enable button: Switches the overall EQ effect off and on, leaving the controls unreset.
- Reset button: Returns all controls of the EQ window to their defaults.

### Clip EQ Graph

This graph shows the current EQ curve with handles matching each enabled EQ band listed below. Drag any numbered handle to boost or cut the band’s frequency range, applying whichever equalization type that band is set to.. As you drag the numbered handles on this graph, the matching band’s parameters change accordingly, and changing each band’s parameters in turn redraws the EQ graph, which doubles as a graphical depiction of the equalization being applied to that track.
