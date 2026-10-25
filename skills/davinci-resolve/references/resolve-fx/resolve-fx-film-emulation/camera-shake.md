# Camera Shake

Version: DaVinci Resolve 20.3 Reference Manual. Studio version only.

[Film emulation effects](INDEX.md)

<a id="source-blanking-handling"></a> <a id="source-camera-shake-studio-version-only"></a> <a id="source-main-controls"></a> <a id="source-shake-levels"></a> <a id="source-shake-quality"></a>

### Camera Shake (Studio Version Only)

This effect mimics random camera movement across Horizontal and Vertical position, Rotation, and Zoom. You get an assortment of parameters for shaping the motion's character, ranging from a slow wandering drift through to sharp, jagged jerks and pops.
### Main Controls

The chief controls deciding how much camera shake gets applied.

- Motion Scale and Speed Scale: With these sliders you tune the overall amplitude and pace of the camera shake added to the image.
- Motion Blur: Lets you layer simulated motion blur onto the shaken image, lending the motion a more lifelike feel. Such blur shows up more on fast movement, since DaVinci Resolve is mimicking how a motion picture camera's shutter speed treats subjects exposed while in motion.
### Shake Levels

These controls let you dial in how intense the camera shake is.

- Pan Amplitude: Lets you decide how much horizontal motion to apply.
- Tilt Amplitude: With this slider you pick how much vertical motion to apply. The two sliders stay

wholly independent of each other.

- Rotation Amplitude: Lets you fold rotational motion into the camera shake too.
- PTR Speed: Through this slider you set how quickly the Pan, Tilt, and Rotation camera shake runs.
- Zoom Amplitude: Through this slider you add zooming to the camera motion you're building.
- Zoom Speed: Through this slider you pick how quickly this random zooming plays out.
- Zoom Type: From this pop-up menu you decide how zooming is added; the choices are

Outward Only, Inward Only, or Outward and Inward. Pick Inward Only and blanking never creeps in around the frame's edges.
### Shake Quality

These controls let you tailor the kind of shaking you're after.

- Motion Method: From this pop-up menu you select among several ways of generating the motion this plugin brings in. Your options are SINE, Rectified SINE, Rectified SINE (Invert), and Square Wave (handy for popping or flickering motion).
- Phase: With this slider you fix where the camera shake you're building begins, drawing on the Motion Method and Amplitude settings you've picked.
- Randomness Scale: With this slider you work irregularity into the camera shake's Horizontal, Vertical, and Rotational motion. A higher value brings in more irregularity.
- Randomness Speed: With this slider you swing between smoothly erratic motion (toward the low end) and more jagged motion (toward the high end).
- Pause Length: With this slider you tune how often the intermittent pauses arrive that interrupt the random motion this filter adds.
- Pause Interval: With this slider you tune how long the intermittent pauses last that interrupt the random motion this filter adds.
- Pause Randomness: This lets you sprinkle some randomness into the intervals that occur.
- Random Seed: With this slider you change the value driving which random values get

produced. Matching values yield matching randomness.
### Blanking Handling

These controls let you settle what happens when camera shake pushes blanking beyond the image's edge.

- Border Type: From this pop-up menu you pick how to fill the empty edge spaces that show up when the camera shake you create shoves the image past your project's current frame size. Four options let you Replicate, Reflect, or Wrap-Around the image to plug the gap.
- Zoom to Crop: With this slider you zoom into the image to trim away unwanted blanking that the Camera Shake effect brings in.
