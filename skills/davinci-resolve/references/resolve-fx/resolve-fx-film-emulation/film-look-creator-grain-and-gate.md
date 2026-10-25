# Film Look Creator grain and gate

Version: DaVinci Resolve 20.3 Reference Manual. Studio version only.

[Film emulation effects](INDEX.md)

<a id="source-film-gate"></a> <a id="source-flicker"></a> <a id="source-gate-weave"></a> <a id="source-grain"></a> <a id="source-resolve-fx-film-emulation-part-2"></a>

### Grain

These controls form a pared-down toolset for reproducing the grain patterns you find on motion picture film. When you want finer command, switch this setting off and turn to the Film Grain effect instead.

- Enable Grain: Switches the grain pattern on or off.
- Preset: Hands you a few jumping-off points for grain, grounded in film stock standards.
- Amount: Sets how much grain appears in the image.
- Size: Sets how large the grain in the image is.
- Softness: Sets how crisp each individual grain reads.
- Saturation: Tints the grain. At 0 it stays monochromatic.
- Image Defocus: Bears on the image's overall resolution, softening focus further as you pull the

control toward 0. At 1.000 the resolution stays untouched. This control leaves the grain alone.
### Flicker

These controls lend the image exposure a soft pulse, echoing the flicker of motion picture projection. For finer controls, switch this setting off and turn to the Flicker Addition effect instead.

- Enable Flicker: Switches the Flicker effect on or off.
- Amount: Sets how much flicker reaches the image. Low settings barely register,

while high ones lend themselves to more extreme looks such as the Nostalgic preset.

- Rate: The pace at which the flicker pulses.
### Gate Weave

These controls reproduce the faint horizontal and vertical drift of the image as the film is mechanically dragged through the camera's gate.

- Enable Gate Weave: Switches the Gate Weave on or off.
- Amount: Sets how much motion the weave carries.
- Rate: The pace at which the weave moves.
### Film Gate

These controls lay blanking along the image's edges that echoes film projection or telecine alignment controls.

- Enable Film Gate: Switches the Film Gate on or off.
- Preset: Pick an aspect ratio drawn from various common film standards.
- Ratio H/V: Here you can set a custom ratio for the image.
- Enable Curvature: Switching this on gently rounds the image's corners to echo the way an actual

film frame's shape is exposed.

- Padding: This zooms the image into and out of the blanking, letting you take in the entire

exposed “frame” of film where you want it. It behaves much like a telecine control. NOTE: Film Gate can produce surprising outcomes when the video hasn't been scaled to cover the whole frame. Should that be the situation, first reach for the sizing controls to make your image fill the frame.

Read [Film Look Creator setup and color spaces](film-look-creator-overview.md) for the shared prerequisites.
