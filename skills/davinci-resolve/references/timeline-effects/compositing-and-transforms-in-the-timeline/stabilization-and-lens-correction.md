# Stabilization and lens correction

Version: DaVinci Resolve 20.3 Reference Manual. Context: Compositing and transforms in the timeline.
[Chapter index](INDEX.md) / [Previous section](dynamic-zoom.md)
<a id="source-lens-correction"></a> <a id="source-object-snapping-in-the-viewer"></a> <a id="source-onscreen-controls-for-transform-crop-and-dynamic-zoom"></a> <a id="source-retime-and-scaling"></a> <a id="source-stabilization"></a> <a id="source-transform-controls-in-the-timeline-viewer"></a> <a id="source-using-onscreen-controls"></a>

### Stabilization

Image Stabilization is on offer for clips directly in the Timeline. These controls let you iron out, or even fully steady, unwanted camera movement inside a clip. The analysis runs in a way that holds onto the motion of individual subjects in the frame, along with the overall path of intended camera movement, while ironing out the shakiness. They're the very same stabilizer controls that live in the Color page's Tracker palette (without the tracker graph), and the stabilization analysis that results is echoed over on the Color page, where the data can be seen plotted on the graph if you need it. A pop-up menu hands you three different options governing how the chosen clip gets analyzed and transformed during stabilization. You have to pick an option first, ahead of clicking the Stabilize button above, because the option you settle on alters how the image analysis runs. Switch to a different option and you'll have to click the Stabilize button once more to reanalyze the clip.

- Perspective: Enables perspective, pan, tilt, zoom, and rotation analysis and stabilization.
- Similarity: Switches on pan, tilt, zoom, and rotation analysis along with stabilization, useful when

perspective analysis throws off unwanted motion artifacts.

- Translation: Switches on pan and tilt analysis plus stabilization alone, useful when stabilizing on the X and Y

axes by themselves gives you results you can live with.

Stabilization controls found in the Edit page Inspector for each clip

The remaining controls let you fine-tune how hard the chosen clip is stabilized.

- Stabilization Toggle: The toggle for the Stabilization controls lets you flip stabilization off and on so you can hold the stabilized image up against the unstabilized one.
- Camera Lock: Switching this checkbox on disables Cropping Ratio and Smooth, and lets the stabilizer concentrate on wiping out every bit of camera movement from the shot in a bid to deliver a locked shot.
- Zoom: With this checkbox switched on, the image is enlarged by a big enough percentage to wipe out the blanking (black edges) left behind by warping and transforming the image to remove unwanted camera movement. The lower you set Cropping Ratio, the harder DaVinci Resolve has to zoom into an image to wipe out these blanked edges. Switch this off and the image isn't zoomed whatsoever, and whatever blanking creeps into the image is sent out alongside it, on the premise that you'll have dedicated compositing artists handle removing that blanking by filling in the absent image data more elaborately. You might equally leave this checkbox switched off if your plan is to keyframe the Input Sizing Zoom parameter for a dynamic zoom in and out across a stabilized shot, clearing blanking only at the spots it surfaces, with no more zoom than any given region of the shot calls for.
- Cropping Ratio: This value caps how hard the stabilizer pushes to stabilize, by spelling out how much blanking or zooming you'll tolerate in trade for wiping out unwanted motion. A value of 1.0 means no stabilization gets applied. Steadily lower values turn on more aggressive stabilization. Altering this value forces you to click the Stabilize button once more to reanalyze the clip.
- Smooth: Lets you run mathematical smoothing across the analyzed data used to stabilize the clip, permitting camera motion in the shot while wiping out unwanted jitter. Lower values smooth less, letting more of the original camera motion's character come through, while higher values smooth the shot more aggressively. Altering this value forces you to click the Stabilize button once more to reanalyze the clip.
- Strength: This value acts as a multiplier letting you choose how tightly you want to lean on the stabilization track to wipe motion out of a shot using the current analysis. At a value of 1, stabilization runs at maximum. Since certain clips can read as more natural with looser stabilization, picking a number under 1 lets a slice of the original camera motion come through. Zero (0) switches stabilization off entirely. As a further tip, you can flip the stabilization by picking –1 when pasting a stabilization analysis from another clip to pull off a match move grounded in the scene's overall motion, and you can use a negative value either under 0 or above –1 to under- or overcompensate while inverting the stabilization, faking the effects of parallax where foreground and background planes travel together but at different rates.

### Lens Correction

The Lens Correction group (offered only in Resolve Studio) carries two controls that let you fix lens distortion in the image, or introduce lens distortion of your own.

- Analyze: Automatically examines the frame in the Timeline sitting at the playhead for edges bent by a wide angle lens. Clicking the Analyze button nudges the Distortion slider to deliver an automatic fix. If the clip you're examining is an especially tough one, a progress bar will turn up to tell you how long it'll take.
- Distortion: Sliding this to the right lets you manually lay a warp onto the image that straightens the bent regions of the picture that wide angle lenses can produce. If you clicked the Analyze button and the upshot was an overcorrection, then sliding this to the left lets you ease off the automatic adjustment until the image reads correctly.

### Retime and Scaling

The Retime and Scaling group carries four parameters touching retiming quality and clip scale:

- Retime Process: Sets a clip-by-clip default for how clips get processed in mixed frame rate timelines and those carrying speed effects (fast forward or slow motion). Out of the box this reads "Project Settings," meaning every speed-effected clip receives identical treatment. Three options exist: Nearest, Frame Blend, and Optical Flow, laid out at greater length within the Speed Effect Processing section see Chapter 51, "Speed Effects."
- Motion estimation mode: While Optical Flow handles speed change effects or clips with a frame rate unlike the Timeline's, the Motion Estimation pop-up lets you settle on the best-looking rendering option per clip. Every method brings its own artifacts, and the top quality option won't always be the wisest pick for a particular clip. Out of the box this reads "Project Settings," meaning every speed-effected clip receives identical treatment. A number of options exist. Two of them, "Standard Faster" and "Standard Better," carry over unchanged from prior DaVinci Resolve releases. They go lighter on the processor and turn out good quality suited to most situations. Even so, "Enhanced Faster" and "Enhanced Better" should produce stronger results in nearly any case where the standard options betray artifacts, though they demand more computation and thus run slower on the majority of machines. For even better slow motion quality, the Speed Warp setting harnesses the DaVinci Neural Engine. How this setting fares hinges on the clip's content, yet under perfect conditions it'll turn out finer visual quality with fewer artifacts than even the Enhanced Better setting manages.
- Scaling: Sets, clip by clip, how clips out of step with the current project resolution get dealt with. Out of the box this reads "Project Settings," so each mismatched clip relies on one shared automatic resizing method. Alternatively, any clip can take its own automatic scaling method. Your picks are Crop, Fit, Fill, and Stretch; for further detail consult the 2D Transforms section of Chapter 149, "Sizing and Image Stabilization."
- Resize Filter: Where clips are being resized, this setting governs which filter interpolates the image pixels as clips resize. One setting suits one style of resizing better than another. Four options exist:

Sharper: As a rule delivers the finest quality across projects whose clips must scale up to fill a larger frame size, or scale down to HD resolutions. Smoother: May offer better quality across projects whose clips must scale down into an SD resolution frame size. Bicubic: Although Sharper and Smoother edge it out slightly on quality, Bicubic stays a remarkably capable resizing filter that taxes the processor less than either of them. Bilinear: A lower quality choice that's gentler on the processor. Useful for previewing your work on an underpowered computer before you render, at which point you can swap over to one of the higher quality options. Other Resize Methods: A range of specific resize algorithms stands ready should you need to align them with other VFX workflows.

### Onscreen Controls for Transform, Crop, and Dynamic Zoom

You also have the choice of transforming, cropping, or layering on dynamic zoom effects to clips through the Transform/Crop/Dynamic Zoom button down at the lower left of the Timeline Viewer. These on-screen controls can equally be picked by choosing an option from the View > Viewer Overlay submenu; these commands carry no keyboard shortcuts by default, but you can set up a manual mapping if there's a mode you keep reaching for. Whichever overlay is currently selected toggles between on and off when you press Shift-` (Tilde), or alternatively through View > Viewer Overlay > Toggle On/Off.

### Transform controls in the Timeline Viewer

### Object Snapping in the Viewer

As you drag objects or dynamic zoom outlines around to reposition them, snapping kicks in at the X and Y center of the frame, plus around the outer third of the frame. Holding the Shift key while dragging a text object pins movement to just the X or Y axis.

### Using Onscreen Controls

Many find the onscreen controls a more intuitive route to working with your clips. Transforming a clip via graphical controls inside the Timeline Viewer goes like this: 1 Switch on the Transform/Crop button down at the lower left of the Timeline Viewer; white signals enabled, gray signals disabled. Once enabled, with nothing selected in the Timeline, the clip riding the highest auto-select-enabled track that the playhead crosses shows its onscreen transform controls. With a clip selected, that single clip becomes the one you transform. 2 Take one of these paths: a) If a mode change is needed, pick the Transform mode out of the pop-up menu. Up come the matching onscreen controls so the clip responds to your mouse. Inside Transform mode, dragging anywhere within the clip's bounding box adjusts pan and tilt, dragging a diagonal corner resizes proportionally, dragging a side squeezes or stretches width or height on its own, and dragging the center handle spins it.

Onscreen controls for transforming in the Timeline Viewer b) From the same pop-up menu, pick the Cropping mode. Now every side gains a cropping handle.

Onscreen controls for cropping in the Timeline Viewer

c) From the same pop-up menu, pick the Dynamic Zoom mode. Now the green box flags where the animated transform begins in size and position, and the red box flags where it ends in size and position. Dragging anywhere inside either bounding box adjusts the pan and tilt at whichever end—start or finish—of the animated effect, and dragging any corner adjusts the size. A motion path appears that lays out the movement being shaped. Once you touch the Dynamic Zoom controls, dynamic zoom switches itself on within the Inspector. In the Timeline Viewer, onscreen controls handle both transforming and cropping. 3 Where it helps, drop to a smaller viewing percentage via the Timeline Viewer scale pop-up so the onscreen controls read better as you rescale the picture, or rely on the scroll input from your mouse, trackpad, or tablet to pull back from the image. 4 When you've wrapped up, switch the Transform/Crop/Dynamic Zoom button off.
