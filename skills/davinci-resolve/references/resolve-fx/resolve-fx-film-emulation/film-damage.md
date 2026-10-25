# Film Damage

Version: DaVinci Resolve 20.3 Reference Manual. 

[Film emulation effects](INDEX.md)

<a id="source-add-dirt"></a> <a id="source-add-scratch"></a> <a id="source-add-vignetting"></a> <a id="source-blur-and-shift-controls"></a> <a id="source-color-3510"></a> <a id="source-film-damage"></a>

### Film Damage

You'll find it in the Resolve FX Texture category. Once you've leaned on the new Resolve FX Revival plugins to mend damage in archival footage, you can flip things around and apply the Film Damage plugin to give freshly shot digital clips a worn, grimy, scratched appearance instead. Pair it with the Film Grain and Flicker Addition plugins and you can persuasively rebuild the look of badly stored vintage archival footage.

Original image (Left), and result with Film Damage (Right)
### Blur and Shift Controls

The three parameters up top let you reshape the image's underpinnings as a first step toward an older-film look.

- Film Blur: Throws in a touch of targeted defocusing to take the digital crispness off the image.
- Temp Shift: By default it warms the image a little to echo the warmer bulb of a film projector,

though you can push it to cool or warm the image by varying degrees.

- Tint Shift: By default it yellows the image to suggest harm to the film dyes, yet sliding it the opposite way

adds a hint of magenta, evoking a different sort of dye failure.
### Add Vignetting

These parameters mimic lens vignetting that darkens the image's edges.

- Focal Factor: Tunes how deep the vignetting reaches into the image.
- Geometry Factor: Shapes how dark the vignetting runs and how sharply its edges read.
- Tilt Amount: Shapes how evenly the vignetting at the image's top weighs against the bottom.
- Tilt Angle: Shapes how evenly the vignetting on the image's left weighs against the right, though only while Tilt Amount sits at something besides 0.
### Add Dirt

These parameters let you mimic dirt particles (not dust) clinging to the film. They are the larger specks, and you have several ways to shape them.

- Dirt Color: With this control you decide the dirt particles' color (black mimics dirt on a print, while white mimics dirt on a negative).
- Changing Dirt: This checkbox lets you toggle between mimicking temporally unstable dirt on the film (ticked) and stationary dirt on the lens (unticked).
- Dirt Density: Lets you set how many dirt particles surface over time.
- Dirt Size: Lets you set the typical size of the dirt particles that appear.
- Dirt Blur: Lets you soften the dirt's focus so it reads less sharply.
- Dirt Seed: Shifting this value reshuffles the random spread of dirt, yet for any single

value the results hold steady across any given set of control tweaks.
### Add Scratch

Five sets of Add Scratch parameters let you place as many as five scratches on the image, mimicking something gouging the emulsion as the film ran.

- Scratch Color: Lets you set the scratch's color (scratches can take on a range of colors depending on the scratch's depth, the film type, and the printing method).
- Scratch Position: Lets you shift the scratch's horizontal placement across the image.
- Scratch Width and Scratch Strength: Let you tune how severe the scratch appears.
- Scratch Blur: Lets you soften the scratch's focus.
- Moving Scratch: With this checkbox you decide whether the scratch jitters around or holds still.
- Moving Amplitude: Sets how far the scratch travels.
- Moving Speed: Sets how quickly the scratch travels.
- Moving Randomness: Sets the way the scratch wanders about.
- Flickering Speed: Sets how much the scratch flickers lighter and darker in severity.
