# Film Grain

Version: DaVinci Resolve 20.3 Reference Manual. Studio version only.

[Film emulation effects](INDEX.md)

<a id="source-advanced-controls"></a> <a id="source-color-3511"></a> <a id="source-film-grain-studio-version-only"></a> <a id="source-grain-params"></a> <a id="source-main-controls-1"></a>

### Film Grain (Studio Version Only)

Lays a procedurally built layer of simulated “film grain” over the image as a composite. Each simulated grain, complete with falloff, is generated to suit the project's resolution.
### Main Controls

These controls let you swiftly pick and lay down a film grain effect.

- Film Grain Presets: This pop-up lets you swiftly pick from a range of 8mm, 16mm, and 35mm film grain effects.
- Composite Type: Lets you settle on a composite mode for marrying the image to the grain this plugin simulates.
- Opacity: Lets you fade the Film Grain effect against the original image.
- Grain Only: With this checkbox you view the grain layer on its own as you build it, so you

can judge its look before it gets composited into the image.

- Freeze: Halts the grain animation's motion, so you can put the effect to use on a still image or

freeze frame.
### Grain Params

The Grain Params group lets you fine-tune the grain's quality.

- Texture: Bigger values spread the grains this plugin generates farther apart, whereas smaller ones pack them tighter for denser grain patterns.
- Grain Size: Bigger values zoom in on the individual simulated grains this plugin generates, whereas smaller ones zoom back out.
- Grain Aspect Ratio: Lets you tune the grains' aspect ratio.
- Grain Strength: Tunes the simulated grain layer's contrast. Higher values yield more

contrast, lower ones less.

- Offset: Brightens or darkens the whole simulated grain layer. In practice, lower

values play up the lighter grains while higher ones play up the darker grains.

- Symmetry: A lopsided contrast tweak. Lower values darken the lighter grains,

whereas higher values brighten the darker grains.

- Softness: Lets you blur the grain layer for even gentler transitions from one grain to the next.
- Saturation: Lets you dial the grain's color up or down. Set to 0, the grain turns monochrome.
### Advanced Controls

Within the Advanced Controls, the Red, Green, and Blue sliders steer the grain's color. The Shadow, Midtone, and Highlight Gain controls let you set how much grain is composited into each of those tonal zones of the image. Switch on the Optimized Mode checkbox (its default state) and performance ought to climb considerably. Switching on the Animate on Every Refresh checkbox animates the grain while you work the sliders, giving you a clearer sense of how the grain pattern reads in motion.
