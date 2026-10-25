# Hot spot color tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Hot spot.
[Chapter index](INDEX.md) / [Previous section](highlight-and-hot-spot.md) / [Hot Spot Hot](highlight-and-hot-spot.md) / [Next section](hot-spot-and-object-removal.md)
<a id="source-color-tab"></a> <a id="source-effect-nodes-part-2"></a> <a id="source-hot-spot-color-controls"></a> <a id="source-hot-spot-controls"></a> <a id="source-hot-spot-node-applied-to-an-image"></a> <a id="source-hot-spot-tab"></a> <a id="source-inspector-2"></a>

### Hot Spot node applied to an image

### Inspector

### Hot Spot controls

### Hot Spot Tab

Through the Hotspot tab you command the primary and secondary hot spots, dialing in each one's placement, size, strength, angle, plus its apply mode. Primary Center X and Y This sets where the primary hot spot lands in the scene. The placement of secondary lens elements and reflections is referenced off the primary hot spot’s position. Primary Strength This field fixes how bright the primary hot spot is. Hot Spot Size This field fixes the primary hot spot’s diameter, where a value of 1.0 spans a circle as wide as the whole image. Aspect This governs the spot’s aspect. At 1.0 the hot spot stays perfectly round; above 1.0 the circle stretches sideways, and below 1.0 it stretches up and down. Aspect Angle This field rotates the primary hot spot. Secondary Strength This field fixes the strength, meaning the brightness, of the secondary hot spot, which is a mirror of the primary one and always sits on the image’s opposite side from the primary hot spot.

Secondary Size This sets how large the secondary hot spot is. Apply Mode This field fixes the way the hot spot acts upon the picture beneath it.

- Add (Burn): The created spots brighten the picture.
- Subtract (Dodge): The created spots dim the picture.
- Multiply (Spotlight): The created spots single out one region of the picture with light while

darkening everything else. Occlude This menu lets you pick which channel of the image fed to the Hot Spot node’s Occlusion input supplies the occlusion matte. You can drive occlusion from the Alpha or the R, G, or B channels of whatever image is wired into the Occlusion input on the node’s tile. Lens Aberration Aberration reshapes and re-behaves the primary and secondary hot spots.

- In and Out Modes: Stretches the hot spot’s shape into a flare. With In mode the hot spot reaches toward the center, while with Out mode it reaches toward the corners.
- Flare In and Flare Out Modes: This setting is a lens distortion effect driven by the lens effect’s motion. Flare In intensifies the effect as the hot spot nears the center, whereas Flare Out grows the effect as the hot spot approaches the image edges.
- Lens: This setting mimics a circular, ringed lens look.

Aberration The Aberration slider sets the overall intensity of the lens aberration effect.

### Color Tab

Color for the primary and secondary hot spots is adjusted on the Color tab.

### Hot Spot color controls

Color Mode From this menu you decide whether color changes are animated or static, working through the compact curves editor in the Inspector.

- None: With the default None choice, a single static curve adjustment applies across the whole range.
- Animated Points: This choice lets the color curves in the spline region animate over time.

After you pick it, jump to the frame you want and make an edit in the Spline Editor to drop a keyframe.

- Dissolve mode: Largely outdated, Dissolve mode remains only for backward compatibility.

Color Channel and Mix Ticking these checkboxes turns on editing of the selected splines in the small Inspector Spline Editor. Ticking the Mix checkbox turns on the Mix Spline, which gauges the sway that the Radial tab controls hold along the hot spot’s radius. Red, Green, Blue, and Alpha Splines The Spline Window plots the curves for each separate channel and acts as a tiny Spline Editor. You use the Red, Green, Blue, and Alpha splines to shape the spotlight’s color across the hot spot’s radius. Up the vertical axis runs the color channel’s intensity or strength. Across the horizontal axis runs the hot spot position along the radius, going from the outer left edge to the inner right edge. By default the curve gives the red, green, blue, and Alpha channels a linear falloff. Mix Spline The Mix spline gauges the sway the Radial controls hold along the hot spot’s radius. Across the horizontal axis runs the position around the circle’s circumference, where 0 marks 0 degrees and 1.0 marks 360 degrees. Up the vertical axis runs how much of the radial hot spot to mix with the color hot spot. At 0 it is entirely the radial hot spot, and at 1.0 it is entirely the color hot spot. NOTE: A right-click within the LUT brings up a contextual menu offering options for editing spline curves.

To read more about the LUT Editor, turn to Chapter 69, “Using Viewers.” in the DaVinci Resolve Reference Manual, or to Chapter 7 in the Fusion Reference Manual.
