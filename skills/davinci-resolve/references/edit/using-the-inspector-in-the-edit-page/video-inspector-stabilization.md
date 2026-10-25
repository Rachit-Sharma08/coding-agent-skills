# Stabilization and stabilization section of the video inspector panel

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the inspector in the edit page.
[Chapter index](INDEX.md) / [Previous section](cropping-and-cropping-section-of-the-video-inspector-panel.md) / [Next section](audio.md)
<a id="source-lens-correction"></a> <a id="source-retime-and-scaling"></a> <a id="source-stabilization"></a> <a id="source-super-scale"></a> <a id="source-the-stabilization-section-of-the-video-inspector-panel"></a> <a id="source-the-super-scale-parameters"></a>

### Stabilization

### The Stabilization section of the Video Inspector panel

These controls let you smooth away — or fully steady — unwanted camera motion inside a clip. The analysis runs in a way that keeps the movement of individual subjects in the frame intact, along with the overall direction of the camera motion you want, while ironing out the shakiness. They’re the very same stabilizer controls in the Color page’s Tracker palette (the tracker graph aside), and the resulting stabilization analysis carries over to the Color page, where you can view the data plotted on the graph should the need arise. A pop-up menu offers three options that set how the selected clip is analyzed and reshaped during stabilization. Pick an option before you click the Stabilize button above, since your choice alters how the image analysis runs. Switch to a different option and you’ll have to click the Stabilize button once more to reanalyze the clip.

- Perspective: Turns on perspective, pan, tilt, zoom, and rotation analysis and stabilization.
- Similarity: Turns on pan, tilt, zoom, and rotation analysis and stabilization, for cases where

perspective analysis produces unwanted motion artifacts.

- Translation: Turns on pan and tilt analysis and stabilization only, for cases where X and Y stabilization alone gives acceptable results.

The remaining controls let you tailor how forcefully the selected clip gets stabilized.

- Stabilization Toggle: The toggle that governs the Stabilization controls lets you flip stabilization off and on so you can compare the stabilized image against the unstabilized one.
- Camera Lock: Switching on this checkbox shuts off Cropping Ratio and Smooth and lets the stabilizer concentrate on stripping every bit of camera motion out of the shot in pursuit of a locked-off result.
- Zoom: With this checkbox on, the image is scaled up by enough of a percentage to erase the blanking (black edges) left behind when warping and transforming the image removes unwanted camera motion. The lower you set Cropping Ratio, the harder DaVinci Resolve must zoom into an image to clear those blanked edges. Leave it off and the image isn’t zoomed at all; whatever blanking creeps into the frame is output right along with the image, on the premise that dedicated compositing artists will handle the blanking by filling in the missing image data more elaborately. You might also keep this checkbox off when you intend to animate the Input Sizing Zoom parameter, dynamically zooming a stabilized shot in and out to clear blanking only where it crops up, applying no more zoom than each region of the shot needs.
- Cropping Ratio: This value caps how hard the stabilizer pushes, by dictating how much blanking or zooming you’ll tolerate in trade for removing unwanted motion. At 1.0, no stabilization is applied. Steadily lower values open up more aggressive stabilization. Altering this value means clicking the Stabilize button once more to reanalyze the clip.
- Smooth: Lets you run mathematical smoothing over the analyzed data driving the clip’s stabilization, permitting camera motion in the shot while wiping out unwanted jitter. Lower values smooth less,

letting more of the original camera motion’s character come through, while higher values smooth the shot more aggressively. Altering this value means clicking the Stabilize button once more to reanalyze the clip.

- Strength: This value acts as a multiplier letting you decide how tightly the stabilization track is used to remove motion from a shot under the current analysis. At a value of 1, stabilization runs at its fullest. Because some clips read more naturally with looser stabilization, a number below 1 lets a share of the original camera motion remain visible. Zero (0) shuts stabilization off entirely. As one more tip, you can invert the stabilization by choosing –1 when you paste a stabilization analysis from another clip to do a match move based on the scene’s overall motion, and you can use a negative value either below 0 or above –1 to under- or overcompensate while inverting, mimicking parallax where foreground and background planes drift together yet at different rates.

### Lens Correction

The Video Inspector panel’s Lens Correction section Available solely in Resolve Studio, the Lens Correction group provides two controls for either fixing lens distortion in the image or introducing distortion of your own.

- Analyze: Automatically inspects the Timeline frame sitting under the playhead for edges being bent by a wide angle lens. Clicking the Analyze button shifts the Distortion slider to deliver an automatic fix. On an especially tough clip, a progress bar shows up to tell you how long it’ll take.
- Distortion: Pulling this slider rightward lets you hand-apply a warp that straightens the curved regions a wide angle lens can introduce. Should clicking the Analyze button leave you with an overcorrection, pulling this slider leftward eases off the automatic adjustment until the image looks right.

### Retime and Scaling

The Retime and Scaling section of the Video Inspector panel Four parameters in the Retime and Scaling group bear on retiming quality and clip scale:

- Retime Process: Lets you set, clip by clip, a default way of handling clips in mixed frame rate timelines

as well as those carrying speed effects (fast forward or slow motion). Its default is “Project Settings,” which treats every speed-effected clip alike. Three choices exist — Nearest, Frame Blend, and Optical Flow — and the Speed Effect Processing section covers them more fully; see Chapter 51, “Speed Effects.”

- Motion estimation mode: When Optical Flow is processing speed change effects or clips whose frame rate differs from the Timeline’s, the Motion Estimation pop-up lets you select the best-looking rendering option for a given clip. Every method leaves its own artifacts, and the top-quality option isn’t invariably the right pick for a particular clip. Its default is “Project Settings,” which treats every speed-effected clip alike. A handful of choices are offered. The “Standard Faster” and “Standard Better” settings match those carried over from earlier versions of DaVinci Resolve. They lean lighter on the processor and give good quality fit for most situations. By contrast, “Enhanced Faster” and “Enhanced Better” ought to deliver better outcomes in almost every case where the standard options show artifacts, though at the cost of heavier computation and therefore slower speeds on most systems.
- The “Standard Faster” and “Standard Better” settings match those carried over from earlier versions of DaVinci Resolve. They lean lighter on the processor and give good quality fit for most situations. By contrast, “Enhanced Faster” and “Enhanced Better” ought to deliver better outcomes in almost every case where the standard options show artifacts, though at the cost of heavier computation and therefore slower speeds on most systems.
- “Speed Warp Faster and “Speed Warp Better” exist for even higher-quality slow motion effects powered by the DaVinci Neural Engine. How well this setting performs depends on the clip’s content, but under ideal conditions it yields finer visual quality with fewer artifacts than even the Enhanced Better setting.
- Scaling: Lets you decide, clip by clip, how clips that don’t match the current project resolution get handled. Its default is “Project Settings,” so every mismatched clip is automatically resized the same way.

That said, you can also assign an individual automatic-scaling method to any clip. The choices are Crop, Fit, Fill, and Stretch; for more, see the 2D Transforms section and Chapter 152, “Sizing and Image Stabilization.”

- Resize Filter: Whenever a clip is resized in any fashion, this setting lets you pick the filter method that interpolates image pixels during the resize. Some settings suit certain kinds of resizing better than others. Four choices are on offer:

Sharper: Generally gives the best quality on projects whose clips must be scaled up to fill a bigger frame size, or scaled down to HD resolutions. Smoother: Can give higher quality on projects whose clips must be scaled down into an SD resolution frame size. Bicubic: Though the Sharper and Smoother options edge it out on quality, Bicubic is still an excellent resizing filter and asks less of the processor than either of them. Bilinear: A lower-quality, lighter-on-the-processor setting. It’s handy for previewing your work on an underpowered computer before rendering, when you can swap in one of the higher-quality options. Other Resize Methods: A set of particular resize algorithms is available when you need to align with other VFX workflows.

- Deinterlace Quality (Interlaced Clips Only): Permits per clip deinterlace-quality tweaks for how DaVinci Resolve fuses the two fields of interlaced media into progressive frames.

Normal: A high-quality deinterlacing method fit for most clips. On many clips, Normal can’t be told apart from High. Normal is what DaVinci Resolve always applies automatically during playback. High: A more processor-hungry method that, depending on the footage, can occasionally produce better results at the cost of slower rendering. DaVinci Neural Engine: This choice taps the advanced machine learning algorithms of the DaVinci Neural Engine to study motion between the fields of interlaced material and rebuild them into one frame. It’s very heavy on computation but, at its best, should yield an even more pleasing result than the “high” setting.

### Super Scale

### The Super Scale parameters

When you require higher-quality upscaling than the standard Resize Filters can manage, you can now switch on one of the “Super Scale” options in the Inspector. Unlike the many scaling options across the Edit, Fusion, or Color pages, Super Scale genuinely raises the source resolution of the clip it processes, meaning the clip ends up with more pixels than before and grows more processor-hungry to handle — unless you optimize it (which bakes the Super Scale effect into the optimized media) or cache it somehow. For deeper coverage of Super Scale, see Chapter 11, “Image Sizing and Resolution Independence.” Applying Super Scale in the Inspector amounts to the same thing as setting those controls for the media clip in the Clip Attributes. Consequently, changing this setting also touches every additional edit that references the selected media. These are the Super Scale group’s parameters bearing on quality and clip scale:

- Super Scale: Lets you choose how much scaling is needed. The choices are 2-3-4x and 2-3-4x Enhanced.
- Sharpness: Lets you choose how much detail the scaling carries. Your picks are confined to Low, Medium, or High except when Enhanced is the chosen Super Scale mode, where variable sharpness becomes available. You’ll want to weigh this setting against Noise Reduction.
- Noise Reduction: Lets you choose how much noise reduction the scaling applies. Again, the picks stay confined to Low, Medium, or High except when Enhanced is the chosen Super Scale mode, where variable noise reduction becomes available. You’ll want to weigh this setting against Sharpness.

Cinematic (Apple iPhone Footage and MacOS Only) The Cinematic parameters With Apple iPhone footage shot in Cinematic mode, on MacOS builds of DaVinci Resolve, you can tune that footage’s parameters by choosing the Cinematic overlay from the Viewer Overlays drop-down. F-Stop: Moving this slider lets you mimic the depth of field behavior of a lens iris.
