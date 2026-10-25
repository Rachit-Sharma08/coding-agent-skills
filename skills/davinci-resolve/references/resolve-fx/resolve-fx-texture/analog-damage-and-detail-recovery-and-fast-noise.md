# Analog damage and detail recovery and fast noise

Version: DaVinci Resolve 20.3 Reference Manual. Context: Analog damage studio version only, Detail recovery studio version only, Fast noise.
[Chapter index](INDEX.md) / [Next section](fast-noise-and-jpeg-damage-and-texture-pop.md)
<a id="source-analog-damage-studio-version-only"></a> <a id="source-appearance"></a> <a id="source-detail-recovery"></a> <a id="source-detail-recovery-studio-version-only"></a> <a id="source-details-extraction"></a> <a id="source-fast-noise"></a> <a id="source-resolve-fx-texture"></a> <a id="source-resolve-fx-texture-1"></a>

### Resolve FX Texture

This family of plugins exists to layer texture onto images, recreating both true-to-life and more stylized looks.

### Analog Damage (Studio Version Only)

Sitting in the Texture category, this plugin mimics the assorted ways a signal breaks down through analog broadcast and tape recording, so Analog Damage is your tool for conjuring all sorts of “old TV” or “junky videotape” treatments. Its Preset pop-up menu offers a selection of ready-made looks, and a Custom option opens the door to rolling your own.

(Left) The original image, (Right) The image with Analog Damage applied

- Preset: Lets you layer onto your footage the very video damage types DaVinci Resolve was originally built to clean up.
- It has the following categories of parameters:
- Telecine Source: Settings covering lens vignetting plus automatic leftward and rightward shutter weave.

Vignetting: Dims the frame toward its edges, mimicking a weak telecine lamp. Vignette Aspect: Tunes how wide the vignette spreads. Shutter Weave: Mimics the faint drift of the picture as a film reel feeds through a telecine.

- Broadcast Signal: Options governing adjustable noise, loss of detail, signal ghosting, and chroma misalignment. Noise Scale: Sets how fine-grained the noise becomes. Signal Noise: Sets how much static rides on the Luma signal. Chroma Noise: Sets how much static rides on the Chroma signal. Detail Loss: Sets how much detail drops out during “transmission.” Chroma Detail Loss: Sets how much chroma detail drops out during “transmission.” Ghosting: Recreates the ghost image a reflected signal produces. Ghost Offset: Lets you shift the ghost image's placement. Chroma Misalignment: Sets how far the color signal sits out of register with the brightness.
- Color Dials: Color tweaks specific to a television signal. Brightness: Stands in for a consumer set's brightness knob. Contrast: Stands in for a consumer set's contrast knob. Color: Stands in for a consumer set's color (saturation) knob. Tint: Stands in for a consumer set's tint knob.
- Scan: Controls that recreate faults in television scanning. Image Aspect: Reshapes the frame, padding or trimming it where required. H-Shift: Lets you roll the image horizontally.

V-Shift: Lets you scroll the picture up and down. V-Hold/Latch: V-Hold works together with the V-Hold Latch parameter so that a little keyframing can trigger animated vertical rolls that “bounce” convincingly over time the way a broadcast would. Overscan: Lets you set how much of the frame gets trimmed for on-screen display. V-Scale: Lets you tune the image's vertical scaling. Vertical Blanking: Lets you dictate the Vertical Blanking Interval size.

- Scan lines: Recreate adjustable television scan lines able to reproduce moire and color artifacts. Line Sharpness: Lets you dial in how crisp the scan lines look. Line Frequency: Lets you set how many scan lines fill the image. Colored Lines: Tick this box to give the scan lines colored outlines.
- TV Construction: Controls that recreate CRT troubles with phosphor brightness, tint, and defocus, plus the means to apply an adjustable curved border and warped screen curvature. Phosphor Brightness: Lets you tune the front screen's brightness even while the tv is supposedly “off.” Phosphor Tint: Lets you tune the front screen's color even while the tv is supposedly “off.” Defocus: Lets you tune how much detail the screen swallows. Screen Curvature: Lets you tune how rounded the picture tube appears. Edge Mask: Tick this box to wrap a black mask around the screen's edge. Edges Transparent: Tick this box to render the screen edges transparent for compositing. Mask Curvature: Lets you tune the black mask's shape. Mask Aspect: Lets you tune the aspect ratio of the black mask.
- VHS: Lets you bring in an adjustable “Restless Foot” that recreates recorded-tape artifacts. Restless Foot Height: Lets you decide how far the restless foot creeps up from the screen's bottom. Restless Foot Offset: Lets you pick the direction and degree of the restless foot's distortion. Restless Foot Jitter: Lets you tune how much the restless foot shakes from frame to frame.

TIP: Running the Analog Damage plugin over on the Fusion page means you can hook up Modifiers that drive automatic animation (Perturb among them) on the various parameters, a fast and simple way to generate self-animating video damage effects.

### Detail Recovery (Studio Version Only)

Detail Recovery is a no-frills, practical effect: it pulls image detail off the second input and grafts it onto the picture arriving at the first input. That way you can put detail back, piece by piece, into an image that had it stripped away. Owing to its mechanics, this effect is meant for the Color page. Putting Detail Recovery to work requires that you drop it into the node tree as a Resolve FX node, dragging it straight out of the Open FX library so it stands as its own node, which is what surfaces both of the RGB inputs that then appear on it. Out of the box, the first RGB input takes the picture you intend to enrich, while the second RGB input takes the picture you're harvesting detail from. For the walkthrough below, Node 1 holds the base grade and Node 2 holds a grade whose highlights are deliberately blown out for a stylistic look. The Detail Recovery node is then introduced to feed targeted image detail from Node 1 back into the output of Node 2.

Configuring Detail Recovery so that image detail off Node 1 feeds into the picture arriving from Node 2 Set against the picture in Node 2, the outcome remains severely exposed yet now carries hints of fine image detail, so it reads as less clipped.

(Left) The frame whose highlights are crushed hard, (Right) The frame after high-frequency detail is restored The parameters Detail Recovery exposes are as follows.

### Detail Recovery

- Transfer Direction: A drop-down where you pick which input supplies the detail and which input that detail gets merged into.

### Details Extraction

- Frequency Cutoff: A slider for setting how much detail to pull out for recovery. Lower settings single out the finest details, while higher ones progressively take in larger ones.
- Detail/Edge Balance: This lets you decide whether to recover every detail or only the more pronounced edges.
- Strength: A slider that boosts or dampens whatever detail gets pulled for recovery.
- Detail Mix: Set to 1.000, this slider mixes the harvested detail into the picture you're adding

it to so the two layers fuse. Set to 0.000, the harvested detail overwrites whatever overlapping pixels live in the picture you're adding it to. The slider lets you land on whichever blend suits your needs.

- Preview Detail checkbox: Switch this checkbox on and you can watch the detail being harvested via the Frequency Cutoff and Strength sliders.

### Fast Noise

Fast Noise generates noise patterns by computer that you can composite over a clip, or use to warp it, for an assortment of effects like smoke, haze, or rippling water.

(Top) The unaltered frame; (Bottom) that same frame after Fast Noise’s Smoke preset, with the position and rotation onscreen controls on display.

### Appearance

Controls that govern which noise pattern gets produced. Every parameter can be keyframed to vary the noise pattern across time.

- Preset: Pick from several typical noise-pattern scenarios: Mist, Smoke, Water Surface, River, and Heat Haze. Default gives the baseline noise pattern, and Custom switches itself on the moment you alter any parameter below.
- Scale: How large the noise pattern is.
- H/V Ratio: Governs the horizontal-to-vertical spread ratio.
- Detail Level: How many tiers of fine detail get produced.
- Detail Balance: Weights the various detail scales against each other. The slider lets you favor

either bolder large detail or bolder fine detail. A value of 0.000 strips out fine detail completely.

- Evolution: Shifts the noise pattern by degrees. This slider drives the noise pattern's “progress”

through time instead of merely tweaking its present form.
