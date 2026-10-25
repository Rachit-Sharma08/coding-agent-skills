# Sky replacement and stylize and tilt shift blur

Version: DaVinci Resolve 20.3 Reference Manual. Context: Sky replacement, Stylize studio version only, Tilt shift blur studio version only.
[Chapter index](INDEX.md) / [Previous section](sky-replacement-artificial-sky.md) / [Next section](tilt-shift-blur-and-watercolor.md) / [Sky Replacement](scanlines-and-sky-replacement.md)
<a id="source-foreground-appearance"></a> <a id="source-main-controls"></a> <a id="source-sky-integration"></a> <a id="source-sky-replacement-workflow"></a> <a id="source-stylize-studio-version-only"></a> <a id="source-tilt-shift-blur-studio-version-only"></a>

### Sky Integration

These controls help you reconcile the qualities of the finished sky with the foreground footage.

- Preview Final Sky: Tick this box to see only the finished sky output, motion and any keyframed parameters included.
- Lens Distortion: Tune this to bend the sky so it matches the curve of the original camera lens.
- Lens Defocus: Tune this to soften the sky's focus so it mirrors the depth of field belonging to the

original lens.

- Exposure: Tunes the sky's overall brightness.
- Add Grain: A pared-down toolset for mimicking the grain patterns seen on

motion picture film. Tick this box to switch the grain pattern on or off. Grain: Sets how much grain goes into the sky. Size: Sets how large the sky's grain is. Softness: Sets how crisp each grain reads. Saturation: Lends color to the grain. 0 is monochromatic.

### Foreground Appearance

Switching these controls on makes an automatic effort to reshape the foreground's overall look, drawing on an analysis of the finished sky's parameters.

- Adjust Foreground: Tick this box to switch on the Foreground Appearance tools beneath it.
- Auto Adaptation: Chooses how the Foreground Appearance analysis is produced.

None: Nothing is set automatically. You're free to tune the parameters underneath by hand. Globally Applied: The color cast is derived from the visible sky and then laid across the foreground uniformly, with no brightness variation. Even so, that color cast refreshes on the fly should the sky shift over time. Match Horizon: The color cast is derived from the visible sky but leans toward the horizon, with its reach set by the Localization control. As a result, brighter or darker patches of sky push bright or dark shifts onto the foreground. As an instance, with a dark sky but a moon near the horizon, the foreground reads brighter around the moon than elsewhere. This too refreshes on the fly over time.

- Adaptation Amount: Lets you pick how much adaptive color adjustment is applied.
- Localization (Match Horizon only): Lets you set how far or near the color

cast extends out from the horizon.

- Brightness: Tunes the foreground's gain or brightness.
- Saturation: Tunes the foreground's saturation.
- Temperature: Tunes the foreground's color temperature.
- Tint: Tunes the foreground's tint.

### Sky Replacement Workflow

What follows is a sample run-through for swapping the sky with one the artificial sky tools build. We begin from the original clip, whose sky we mean to swap out. The first move is simply to add a new color node.

The original shot whose sky we intend to swap.

After that the sky needs qualifying. For this particular clip, applying the Magic Mask (object) tool to the node isolates just the sky we mean to swap. The HSL qualifier, 3D qualifier, or even a power window would accomplish the same.

The sky isolated by way of the Magic Mask tool.

With the sky now isolated, we can drag the Sky Replacement effect out of the Effects Library and drop it onto the very node our Magic Mask already occupies.

The black region marks where our new sky will be built.

With both toolsets now live on the same node, the Magic Mask and the Sky Replacement parameters can be tuned together. That turns the full sky replacement into a single-node task.

Both the Magic Mask (or any qualifier) and the Sky Replacement tools can share one node.

The finished replacement sky, tracking right along with the camera's movement.

Through the Artificial Sky Controls we build a fresh, more compelling sky. Next, by way of the Sky position tools, we lock that sky to the original clip's camera movement. Last, layering in the Foreground Appearance toolset lets us blend the foreground and the sky together without a seam.

### Stylize (Studio Version Only)

This plugin lets you cast one of several painterly styles over an image, derived from analyses of various paintings, in a manner that holds up temporally for moving footage: the style strokes seem to settle onto individual objects in the scene and travel and flow with them in a steady way. It offers two controls:

- Styles: A pop-up menu where you pick an artistic style to lay over the image.
- Style Scale: A slider with which you set how large or small the applied art strokes

should be applied.

(Left) The original image; (Right) that same image after Style Transfer, set to Dance at a Style Scale of 4 TIP: There's more range in this plugin than you'd expect, provided you layer Style Transfer against the original image. Pull this off with a duplicate layer on the Edit page, or with two nodes — one carrying the Style Transfer effect, the other the original image — joined by a Merge node on the Fusion page or a Layer node on the Color page. With that in place, just blend the Style Transfer output against the original image through composite modes and opacity tweaks for richer compositing. Notably, the Luminosity composite mode lets you pull texture from the Style Transfer while keeping the original image's color, whereas the Saturation composite mode lets you pull color from the Style Transfer while keeping the original clip's texture.

### Tilt-Shift Blur (Studio Version Only)

This mimics depth-of-field effects by way of a graduated blur driven by a generated Z-depth map. Out of the box its settings produce a “miniaturization” illusion, in which the image looks tiny thanks to the top and bottom depth-of-field settings in play.

### Main Controls

These controls pick and govern the effect as a whole.

- Blur Type: Your two options here are Fast Blur and Lens Blur, with Lens Blur selected by default.
- Blur Strength: A slider with which you set how much blur is added.
