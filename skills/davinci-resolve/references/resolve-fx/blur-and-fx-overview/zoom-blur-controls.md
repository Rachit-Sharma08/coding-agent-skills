# Zoom blur controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Zoom blur.
[Chapter index](INDEX.md) / [Previous section](lens-blur-and-mosaic-blur-and-radial-blur.md)
<a id="source-zoom-blur"></a>

### Zoom Blur

A blur that imitates the streaking you'd get if a camera were pushing in toward the picture.

- Zoom Amount: With Blur Type set to Realistic, this slider works in both directions. Its midpoint is 0, meaning no blur whatsoever. Pulling it rightward pushes the blur outward away from the position, while pulling it leftward draws the image inward toward the Position, blurring outward from that point.
- Blur Type: With Blur Type set to Realistic, the blur reproduces the look of a photographic motion blur. Set to Stylized instead, the blur becomes a clean, uncomplicated digital smear.
- Smooth Strength: With Blur Type set to Stylized, this slider governs how strong the effect is. Its left end is 0, meaning no blur whatsoever. Pulling it rightward pushes the blur outward away from the position, while pulling it leftward draws the image inward toward the Position, blurring outward from that point.
- Center Exclusion: Sets how far out from the XY position the Zoom Blur kicks in.
- Channel Adjustment: Lets you set how strong the blur is within one particular channel, measured against

the strength of the blur as a whole. Red: Sets the Red channel's blur amount as a proportion of the blur applied overall. Green: Sets the Green channel's blur amount as a proportion of the blur applied overall. Blue: Sets the Blue channel's blur amount as a proportion of the blur applied overall. Alpha: Sets the Alpha channel's blur amount as a proportion of the blur applied overall.

- Center Position: Repositions the center of the blur.
- Quality: Pick from Faster, Better, and Enhanced. The Better and Enhanced modes serve to

sharpen up crisp picture detail when blur values are low. Where that's not relevant to your footage, Faster does the job just fine.

- Border Type: Determines the way the blur treats the picture's edges; the choices are Black, Replicate, Reflect, and Wrap Around.
- Move with Sizing: Tick this box so the blur center holds its relative spot in the frame whenever the Input and Editing sizing get altered.
- Blur Alpha: Tick this box so the Alpha channel is blurred together with the picture's contents.
