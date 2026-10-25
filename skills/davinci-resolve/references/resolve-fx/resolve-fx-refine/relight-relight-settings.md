# Relight relight settings

Version: DaVinci Resolve 20.3 Reference Manual. Context: Relight studio version only.
[Chapter index](INDEX.md) / [Previous section](face-refinement-and-relight.md) / [Relight (Studio Version Only)](face-refinement-and-relight.md)
<a id="source-example"></a> <a id="source-resolve-fx-refine-part-3"></a> <a id="source-the-relight-on-screen-controls"></a> <a id="source-the-relight-settings"></a>

### The Relight Settings

These controls let you set the strength, type, and direction of the light bouncing off the surface map. Most can be keyframed, and positions can be tied to the FX Tracker, enabling things like sliding a light source as though it were fixed to an object, or sweeping a spotlight to trail a person as they cross the scene. The controls and their groupings are:

- Surface Map: This picks the mode used to build the Surface Map. Use Internal: builds the Surface Map and applies it right away within this same node. Use Input 2: takes in the Surface Map handed over from a different Relight Node. Apply this on the second node when you've set up a dual Relight Node arrangement.
- Output Surface Map: Ticking this box makes this instance of the effect output a multi-colored map of the input frame. That Surface Map can next be routed into a second Relight effect (with “Use Input 2” chosen, per above), and there the light sources get placed and tuned.
- Directional/Point Source/Spotlight: Directional: makes a light source casting from one fixed direction at an infinite distance away. Point Source: makes a light source casting outward from a single central point. Spotlight: is likewise a point source, only focused down into a cone shape.
- Relighting Map Preview: Ticking this box exposes the Alpha channel of this light's effect. Unticking it shows the current image but with the light mask held in the Alpha channel.
- Diffuse Reflection Properties: These controls set the character of the emitted light. Brightness: This governs the strength of whatever grading is applied to the scene. On its own it adds no brightness changes; it amplifies the changes you make with the grading tools. Softness: This governs the size of the light emitter, in effect setting how harsh or gentle the gradient runs between light and dark. Distance Falloff: This governs how much reflections dim as distance from the light source grows.
- Light Properties: Brightness: This governs the strength of whatever grading is applied to the scene. On its own it adds no brightness changes; it amplifies the changes you make with the grading tools. Reach: This governs how much reflections dim with distance from the light source. Contrast: This sets how harsh or gentle the gradient runs between light and dark.
- Surface Properties: Glossiness: Lends reflective surfaces the illusion of a metallic sheen. Specularity: Whenever any glossiness is added, this governs how metallic and shiny that glossiness reads. Shadow Softness: Governs how far the light reaches into shadows from ambient reflections, past where it would otherwise land.
- Spotlight :(shown only with Spotlight option enabled) Beam Angle: Sets how wide the cone of light spreads. This control is also offered graphically in the Viewer. Edge Softness: Sets the softness along the edges of the light cone/beam.
- Light Position: These controls handle the position of the light emitter for every light type. They can be set directly, but more conveniently they can be set graphically in the Main Viewer. Make sure the Main Viewer's mode is set to Open FX Overlay using the icon at the lower left.

In Directional mode: Azimuth/Elevation XY : sets which direction the light arrives from. In Point and Spotlight modes: Source Follows FX Tracker: tick this box so the light source rides along with the FX tracker. Light Source XYZ: these controls fix where the light emitter sits in 3D space. In Spotlight mode: Spot Follows FX Tracker: tick this box so the light source trails the FX tracker. Spot Target XY: these controls fix where the base of the spotlight cone lands.

While in Use Input 2 mode, options appear for working with an externally generated Surface Map.

- Rescale Oversaturated: Various applications scale the Surface Map differently. One common format resembles the Relight plugin's own internal maps but with the colors heavily saturated, and it can run dark or black across some regions. If your imported surface map looks like that, tick this box to reinterpret it.
- Reinterpret Left/Right: Tick this box to flip the direction of your external surface map when its surfaces look concave rather than convex.
- Reinterpret Up/Down: Tick this box to flip the direction of your external surface map when its surfaces look lit from beneath while the light sits above them.

While you're producing an analysis internally with Use Internal, or using Output Surface Map, an Advanced Options group also appears holding an option tied to Blanking Regions. These won't matter in most cases; they exist only to fix certain particular situations. They serve to force different edge-of-frame behavior in these special cases:

- The source video carries letterboxing or some framing border that's been “baked in,” meaning the incoming frames hold black pixels at the edges that DaVinci Resolve didn't add. Letterboxing that DaVinci Resolve itself adds (say, a 21:9 frame fit into a 16:9 timeline) needs no special handling. You'll spot the trouble because the Surface Map AI treats the scene as though the black areas are genuine objects or stuck to objects in frame. Objects touching the black bars may seem to merge into those regions.
- The source video carries pillarboxing, just like the letterboxing above. As an example, a 4:3 source video captured into a 16:9 clip with black borders before it reached DaVinci Resolve.
- A case where a wide clip was placed into a narrower timeline correctly, but once resizing or effects were applied you want the plugin to process the original blanking areas because content now sits there. This case is obvious, since the analysis halts at the original blanking edge, cropping off areas you mean to analyze.

When you hit any of these special cases your options are:

- Blanking Regions:

Process Entire Frame: Tell the AI to disregard any data about the timeline shape and simply process every visible pixel. Handle Automatically (default): The AI processes only the region DaVinci Resolve knows holds your media. Auto + Extra Crop: This is recommended for cropping away black bars; it draws on DaVinci Resolve's knowledge of which pixels your media occupied while letting you crop out the framing or letterboxing relative to its shape. It's recommended because it stays consistent as you change timeline settings. Manual Cropping: Simply lets you override whatever the content's framing is, ignoring any of DaVinci Resolve's knowledge of your media's shape.

### The Relight On-Screen Controls

Several of the light-source positioning controls are offered graphically in the Viewer; be sure Open FX Overlay is chosen at the Viewer's lower left to see them.

While in Directional mode, dragging the emitter (red rays) about the frame sets the Azimuth/Elevation controls.

In the Point Source and Spotlight modes you can shift the emitter (red rays) to change the XY coordinates, and the circle to adjust the emitter's Z coordinates. While in Spotlight mode you can drag the X to change the Spot Target's XY coordinates, and scale the large circle to adjust the Cone Angle.

### Example

For this example, we'll relight the scene shown below. Filmed on a cloudy overcast day, the director is happy with the flat look on the building. Sadly, the dull muted lighting also hit the model, which he'd like to make pop more out of the scene. We'll turn to the Relight tool to drop a phantom sunbeam onto the model alone and onto none of the surrounding fence or walls.

The model's lighting reads flat and dull. We want to alter it by adding an artificial sunbeam landing on her that the shot didn't have. We also want to leave the fence and background untouched. The first tool we'll reach for is the Magic Mask to separate the model from her surroundings.

Separating the model via a Magic Mask to confine the effect Next we'll bring in two distinct relight nodes — one that builds the surface map, the other that receives it and does the actual relighting of the shot. The node tree gets explained below.

The Relight node tree holds a pair of Relight nodes, the first named Surface Map and the second named Relight. The RGB output coming off the Magic Mask routes into the upper RGB inputs on each of those nodes. On top of that, the Magic Mask’s Alpha output runs into the Relight node. Wired this way, the Relight effect touches only the model we isolated with the Magic Mask while the backdrop stays untouched.

Within that first node (Surface Map), the Surface Map option is set to Use Internal. We also tick the Output Surface Map checkbox so the map it builds reaches the second node (Relight). To finish wiring it up, drag the Surface node’s RGB output into the lower RGB input on the Relight node. Over in the Relight node, switch the Surface Map option inside the Inspector to Use Input 2.

The surface map produced by the Surface Map node With the node tree wired up properly, the Surface Map gets built inside its own node; confirm that node cache is switched to On for it. From there you can operate right in the Relight node and pick a Directional light. The Relighting Map Preview checkbox together with the on-screen controls reveals precisely where the lighting lands and how it traces the contours of your subject. While the Relighting Map Preview box stays ticked, you get a clear read on where and how the Relight reshapes the subject. Clear that box and the finished color result comes into view instead. All that remains is to dial in the fresh light qualities themselves, so working the Primaries Wheels controls inside the Relight effect, we push the gain up, tint it toward a faint yellow/orange, and raise the saturation to fake a golden-hour shaft of light striking our subject in place of the flat, overcast scene we started with.

Working the Primaries gain and saturation wheels within the Relight node to lend the light its character, convincing the eye that the model is bent over the fence and caught in a sunbeam.
