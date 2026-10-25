# Sky replacement artificial sky

Version: DaVinci Resolve 20.3 Reference Manual. Context: Sky replacement.
[Chapter index](INDEX.md) / [Previous section](scanlines-and-sky-replacement.md) / [Next section](sky-replacement-and-stylize-and-tilt-shift-blur.md) / [Sky Replacement](scanlines-and-sky-replacement.md)
<a id="source-artificial-sky"></a> <a id="source-sky-position"></a>

### Artificial Sky

With these options you can build artificial sky elements that look believable. They fall under three headings: Sky, Cloud, and Hotspot (a stand-in for the sun or moon). Out of the box, each element's opacity sits at zero (off). To reveal any of them, raise the opacity for that category above zero.

- Preview Artificial Sky: Ticking this box displays the Artificial Sky categories on their own, with no compositing against the foreground plate.
- Sky Opacity: Tunes the sky's opacity. At zero it's fully off; at one it's wholly opaque. Anything between mixes the artificial sky with the source sky.
- Sky Color: Picks the sky's color.
- Horizon Color: Picks the color of the horizon haze that fades into the sky color.
- Horizon Softness: Sets how gently the horizon dissolves into the sky.
- Horizon Height: Sets how far up the frame the horizon climbs.
- Horizon Angle: Sets the angle of the horizon.
- Cloud Opacity: Tunes how opaque the clouds are against the sky. Lower settings fold

the clouds in further; higher ones make them pop.

- Cloud Color: Picks the clouds' color.
- Cloud Scale: Sets the scale of the noise pattern that builds the clouds, which governs

how near the clouds sit to the foreground.

- Cloud Shape: Tunes the horizontal/vertical ratio of the clouds. Lower settings yield puffier

(cumulus) clouds, while higher ones stretch them out (cirrus).

- Cloud Tilt: Tunes the sky's angle against the ground, so it lines up with the

foreground angle.

- Cloud Detail: Sets the balance of coarse versus fine detail across the clouds.
- Cloud Fill: Tunes how much of the sky the clouds cover.
- Cloud Contrast: Tunes how much contrast the cloud cover holds against the sky.
- Cloud Time: Shifts the clouds' noise pattern. Pairing this control with keyframes

lets the cloud pattern evolve across time.

- Hotspot Brightness: Tunes how intense the hotspot is. At zero there's no hotspot. An on-screen control for this sits in the Viewer.
- Hotspot Color: Tunes the hotspot's color.
- Hotspot Position: Tunes where the hotspot sits. An on-screen control for this

resides in the Viewer.

- Hotspot Size: Tunes the hotspot's size.
- Hotspot Sharpness: Tunes how sharp the hotspot's edges read.

### Sky Position

With these tools you track the foreground clip's motion so the sky shifts convincingly along with whatever the camera does.

- Match Motion: Picks which tracking approach to apply. Keyframing Only: Lets you drive the sky's movement by hand, keyframing the position controls. Track Foreground: Runs a track automatically off the foreground elements within the composite. Track Original Sky: Runs a track automatically off the sky in the original clip. It works only where the sky already holds detail such as clouds. When your footage permits, this is the soundest, most dependable tracking approach. Use FX tracker: Ties into the track the FX tracker produced in the tracker controls.
- Adjust Size: Resizes the sky so it can span the range of motion the tracker laid out.
- Adjust Position: Lets you set the sky's X and Y positions by hand.
- Auto-Size for Motion: Examines the track and sets the sky's size and position on its own to

span the track's full reach.

- Flip Horizontal: Mirrors the sky across its horizontal axis.
