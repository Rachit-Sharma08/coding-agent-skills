# Fast noise and jpeg damage and texture pop

Version: DaVinci Resolve 20.3 Reference Manual. Context: Fast noise, Jpeg damage, Texture pop studio version only.
[Chapter index](INDEX.md) / [Previous section](analog-damage-and-detail-recovery-and-fast-noise.md) / [Next section](texture-pop-understanding-advanced-mode.md) / [Fast Noise](analog-damage-and-detail-recovery-and-fast-noise.md)
<a id="source-adjustment"></a> <a id="source-auto-animation"></a> <a id="source-jpeg-damage"></a> <a id="source-output"></a> <a id="source-position"></a> <a id="source-texture-pop-studio-version-only"></a>

### Adjustment

Controls for tuning the noise pattern's parameters after it has been produced. They come in especially handy for reworking the noise pattern's Alpha channel ahead of compositing. Every parameter can be keyframed to vary the noise pattern across time.

- Brightness: Raises or lowers the noise pattern's gain.
- Contrast: Pushing this slider rightward brightens the light zones and deepens the dark zones within the

noise pattern, lifting the contrast. Pulling it leftward flattens the contrast.

- Saturation: This slider sets where the noise pattern falls between grayscale and full color.

A value of 0.000 is wholly grayscale, whereas 1.000 is fully saturated color.

- Color Tint: Establishes the effect's overall hue.
- Invert Dark Regions: Tick this box to flip the dark regions to white and deepen the edges within

the noise pattern.

- Invert Pattern: Tick this box to flip the noise's color.
- Allow Negative Values: Tick this box to feed negative values into the Output section further down.

### Position

Controls that set the noise pattern's center point and orientation.

- Position X/Y: Where the noise pattern's center sits.
- Rotation: Spins the noise pattern about its center.
- Position Reference: Dictates how the effect is placed when a clip gets resized or

repositioned within the Timeline. Sizing and FX Tracker: Here the noise pattern tracks along with Sizing and FX Tracker moves made on the Color page. Suppose you used the FX Tracker to follow a camera pan: the noise pattern would travel with that pan instead of holding still as the shot slid beneath it. Keyframed Positions: You adjust the noise pattern's placement the usual way, through keyframes. The position and rotation controls are also adjustable right in the Viewer once you choose Open FX Overlay mode from the drop-down at the Viewer's lower left. Drag the star inside the Viewer to set the X/Y position; drag the circle either clockwise or counterclockwise to set the rotation.

### Auto-Animation

This set of controls lets you shape how the noise pattern animates.

- Velocity X/Y: How far each frame is advanced automatically away from the starting position. Keyframing these controls steers the noise pattern's direction without touching its real X/Y position, which lets you imitate behavior like smoke shifting course in a breeze.
- Seethe: Dictates how far each frame is automatically evolved beyond the starting Evolution value.
- Randomize Start Frame: Pins the skipping cycle to the present frame, so you can reuse a

favorite effect across several clips without every copy turning out identical.

- Start Frame: Lets you name the reference frame for the skip pattern, giving you a handle on the

run of noise produced should you ever need to line it up with the same noise pattern on a different clip. That frame is the one that repeats.

### Output

This set of controls lets you decide how the noise pattern's output is handled.

- Preview Noise: Tick this box to view the noise pattern on its own.
- Output: Decide how the noise pattern is put to use.

Composite Onto Clip: The noise pattern gets laid over or blended into the video clip. Composite Type: Picks the composite mode for the noise pattern. Put Into Alpha Channel: The noise drops into the node's Alpha channel, letting you press the noise pattern into service for compositing. Bear in mind you'll also have to right click the node and pick “Use OFX Alpha” for this setting to take effect. As an alternative, drag the Fast Noise effect straight into the Node Graph as an FX Node rather than onto a corrector node, and the Alpha becomes available with no extra setup. Use to Warp Image: The noise pattern serves to distort the image. Input Alpha: Governs how the incoming Alpha channel is treated.

- Limits Warping Effect: Pens the warp into specific zones spelled out by the Alpha channel, for instance when you want a water ripple or heat shimmer confined to just part of the clip.
- Gets Warped as Well: The warp acts on the Alpha channel alongside the RGB channels, for instance when warping a logo that has a transparent backdrop.

### JPEG Damage

Recreates the slight or severe artifacts that crop up under JPEG compression; handy for faking compression damage.

- Quality: Lets you drop the image's bit depth.
- Resolution: Lets you enlarge the macroblocking artifacts that show up.
- Block Aspect Ratio: Lets you push the macroblocks toward squarer or more rectangular shapes.
- Frequency Scale: Crisps up the effect.
- Scale Component: Lets you anchor this effect on All Frequencies, the X-Frequency, or the

Y-Frequency.

### Texture Pop (Studio Version Only)

Texture Pop is a richer, more adaptable take on the Midtone Detail control that lives in the Primaries and HDR palette. With this effect's controls you can strip texture away or push it harder. It offers two operating modes that set how fine-grained a result is within reach.

- Within Simple mode, you get to dial in stronger doses of the Midtone Detail effect from the Primaries and HDR palette. One Details slider softens or sharpens the image's midtone detail across a wider range, and a Strength slider then pushes the effect further or eases it back.
- Within Advanced mode, you can finely shape the softness or sharpness of high-, medium-, and low-frequency image detail through seven separate “details” sliders, named Rough, Coarse, Medium, Small, Fine, and Tiny. That lets you treat several frequencies of image detail distinctly, softening Fine detail, say, while boosting Medium detail. The Strength slider raises or lowers the combined effect of all the sliders together.

Whichever mode you're in, the Details/Range sliders sit at a default of 0.000, leaving the image untouched. That's the setting to keep when you want the image's original detail quality preserved. Their span runs from -1.000 (the most softening) to +1.000 (the most sharpening). Beyond that, a group of Tonal Range controls (covered further on) lets you decide how strongly this effect lands on the image's Shadows, Midtones, and Highlights, handing you even tighter say over which areas of the picture get softened and/or sharpened.
