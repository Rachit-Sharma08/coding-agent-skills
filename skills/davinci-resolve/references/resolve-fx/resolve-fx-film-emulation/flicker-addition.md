# Flicker Addition

Version: DaVinci Resolve 20.3 Reference Manual. 

[Film emulation effects](INDEX.md)

<a id="source-flicker-addition"></a> <a id="source-flicker-quality"></a> <a id="source-main-controls"></a>

### Flicker Addition

Rather than stripping flicker out with the Resolve FX Flicker Removal plugin, why not put some in? The Flicker Addition plugin introduces fast, animated exposure shifts that make the picture seem to flicker, producing animated results that would be tough to keyframe on your own. Applied to an image in various ways, this plugin can stand in for torchlight, firelight, fixtures running old ballasts or frayed wiring, or any light source that's unstable over time. As an example, you might key just the highlights in a night-time shot and let Flicker Addition act on those isolated highlights alone. Its flickering quality is governed by two sets of controls.
### Main Controls

With these controls you decide how the flicker gets applied along with its overall pace and strength.

- Flicker Type: This pop-up menu sets which kind of adjustment carries the flicker, your choices being Lift, Gamma, Gain, Vignette, or Alpha.
- Range slider: Use this to dictate how broadly the flickering ranges.
- Speed: Use this to set the rate at which the flickering animates.
- Smoothness: With this slider you tune the temporal character of the flickering, deciding whether it jumps

sharply from one value to the next (at lower settings) or eases through smoother transitions between values (at higher settings).

- Flicker R, G, B Channels: A trio of checkboxes lets you pick which color channels this flickering touches.
### Flicker Quality

These controls let you fine-tune the specifics of the flickering animation.

- Randomness Scale: With this slider you bring irregularity into the Horizontal, Vertical, and Rotational motion of the camera shake. A higher value brings in more irregularity.
- Pause Length: This slider governs how often the intermittent pauses occur that interrupt the random motion this filter adds.
- Pause Interval: This slider governs how long the intermittent pauses last that interrupt the random motion this filter adds.
- Pause Randomness: This adds some measure of randomness to the intervals that take place.
- Random Seed: This slider changes the value that determines which random values get

generated. Matching values yield matching randomness.
