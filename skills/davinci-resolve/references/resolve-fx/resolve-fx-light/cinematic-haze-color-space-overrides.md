# Cinematic haze color space overrides

Version: DaVinci Resolve 20.3 Reference Manual. Context: Cinematic haze.
[Chapter index](INDEX.md) / [Previous section](aperture-diffraction-and-cinematic-haze.md) / [Next section](cinematic-haze-and-glow.md) / [Cinematic Haze](aperture-diffraction-and-cinematic-haze.md)
<a id="source-atmospheric-scattering"></a> <a id="source-color-space-overrides"></a> <a id="source-depth-map"></a> <a id="source-light-halos"></a> <a id="source-light-rays"></a>

### Color Space Overrides

Here you can override the effect's input gammas and color spaces should you need to set them by hand for a display-referred pipeline. The default, “Use timeline,” mirrors whatever color spaces you picked in the Color Management section of the Project Settings.

- Input Color Space: Establishes the input color space, picked from the menu provided.
- Input Gamma: Establishes the input gamma, picked from the menu provided.

### Depth Map

This group configures the depth map's parameters.

- Depth Map Preview: Switches on the depth map preview so you can review what the depth map has measured. Brighter zones lie farther off, while darker ones sit closer.
- Depth Map Source: Lets you select where the depth map comes from, either generated internally by the plugin or pulled from the node's alpha input when you've supplied an external depth map.
- Invert: Flips the depth map so the near and far ranges trade places.
- Advanced Depth Controls: Tick this box to enable the Advanced Depth Controls.

Quality: Lets you pick between a Better quality or Faster rendering depth map. Stay in Faster mode while you rough in the effect, then flip to Better once you're ready to finish. Adjust Map Levels: Brings the Far Limit, Near Limit, and Gamma controls online as covered below. Isolation: Ticking this box enables the tools that confine the isolation to one chosen depth on the map. Target Depth: Pick the depth you wish to isolate. Tolerance: Pick how broad a depth band you wish to isolate. Softness: Controls whether the boundary between isolated and non-isolated depths is gradual or abrupt. Post Processing: Ticking this box enables the tools that help the effect hug objects more closely. Post Filter: Smooths the depth map to follow image contours. Contract / Expand: Pulls the foreground in or pushes it out. Blur: Softens the picture so colors average together at the edges. Blanking Regions: These controls instruct the Depth Map on how to deal with letter and pillar boxing zones within the effect.

- Process Entire Frame: Instructs the AI to disregard any data about the timeline's shape and simply work on every visible pixel.
- Handle Automatically (default): The AI restricts itself to the region that DaVinci Resolve identifies as holding your media.
- Auto + Extra Crop: This is recommended for cropping away black bars. It draws on DaVinci Resolve's awareness of which pixels your media filled, while still letting you trim away the framing or letterboxing relative to its shape. It comes recommended because it remains consistent as you change Timeline settings.
- Manual Cropping: Simply lets you set the content's framing yourself, disregarding any of DaVinci Resolve's knowledge about your media's shape.
- Deflicker: This dials in how much deflickering occurs. Keep values low for top quality, and raise them if moving objects begin to show extra edges.
- Far Limit: Tunes the depth map's black levels, governing how far out the effect reaches.
- Near Limit: Tunes the depth map's white levels, governing how near the effect reaches.
- Gamma: Lays a gamma curve over the depth map to make it more or less contrasty.

### Atmospheric Scattering

These tools reproduce the way the atmosphere alters light passing through fog and haze.

- Airlight: Controls how much ambient haze there is, akin to an off-screen source such as the moon or a big streetlight.
- Density: Controls how thick the haze is.
- Resolution Loss: Introduces blur to the picture as the haze obscures it.
- Halation Threshold: Defines the brightness ceiling a source light must cross to trigger the

halation effect.

- Halation: Controls how much halation the source lights produce.
- Saturation: Controls the saturation of the halation.
- Colorize: Choose a color to tint the haze.

### Light Halos

You use these controls to fine-tune the light halos.

- Halo Threshold: The cutoff governing source light motivation.
- Size: Controls how large the halo around source lights is
- Brightness: How bright the halo around the source lights appears.
- Saturation: The color saturation that arises from the source lights' own color.
- Colorize: Applies a color cast to the halo.

### Light Rays

These controls recreate volumetric light streaming out from sources within the picture.

- Enable Light Rays: Tick this box to switch on the light rays toolset.
- Preview Threshold: Renders a preview that isolates only those lights in the picture set to

cast rays.

- Source Threshold: Defines how bright an object must be before it casts rays.
- Ray Directions: A pop-up menu offering either “From A Location,” which surfaces

controls for picking an X or Y position as the origin point that fixes the beams' angle, or “At an Angle,” which surfaces controls for setting one overall orientation for the rays.

- Angle: Sets the angle of the light rays.
- Length: Lets you stretch or shorten the rays.
- Soften: Lets you blur the rays as they're emitted.
- Brightness: Lets you set how bright the rays appear.
- Saturation: Tunes how strong the rays' color is.
