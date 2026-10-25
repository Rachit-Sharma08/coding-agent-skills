# Face refinement and relight

Version: DaVinci Resolve 20.3 Reference Manual. Context: Face refinement studio version only, Relight studio version only.
[Chapter index](INDEX.md) / [Previous section](face-refinement-side-lighting.md) / [Next section](relight-relight-settings.md) / [Continue Relight (Studio Version Only) / Example](relight-relight-settings.md) / [Face Refinement (Studio Version Only)](depth-map-and-face-refinement.md)
<a id="source-cheeks"></a> <a id="source-chin"></a> <a id="source-forehead"></a> <a id="source-grain"></a> <a id="source-relight-studio-version-only"></a> <a id="source-setting-up-relight"></a> <a id="source-using-relight"></a>

### Forehead

True to its name, this adjusts color and texture across the forehead.

- Hue and Saturation: These sliders let you tweak the forehead's color.
- Gamma: This drives a gamma curve so you can set how bright the forehead reads.
- Smooth: This slider lets you apply a dedicated smoothing pass to the forehead to soften wrinkles and worry lines.

### Cheeks

Plain color-adjustment controls covering the whole cheek area, not merely the blush area.

- Hue and Saturation: These sliders let you tweak the color of the cheek, eye, and nose area.

### Chin

Plain color-adjustment controls covering the face's chin.

- Hue and Saturation: These sliders let you tweak the color of the chin, extending up along the sides of the face (the beard area).

### Grain

At times the Skin Smoothing controls leave the skin pleasingly smooth, yet they also strip out the video clip's natural grain by accident, giving it an artificial look. The Grain toolset lets you reintroduce that grain pattern to match the shot's original overall grain. Grain touches only the smoothed regions inside the Face Refinement plugin, so it's already prequalified on your behalf.

- Add Grain to Skin Areas: Tick this box to switch the Grain effect on or off.
- Strength: Sets how much grain gets added.
- Size: Sets the grain's size.
- Softness: Sets how crisp or blurred the grain pattern is.
- Saturation: Sets how colorful the grains are.

TIP: Every parameter above can be keyframed by hand should the automatic tracking fail to lock on, by clicking their keyframe icons in the Inspector. As an example, if you locate a face at frame 10 and once more at 50, Face refinement will interpolate across those moments. Should you manually shift the mouth down at frame 50, then frames 11-49 will adjust to suit.

### Relight (Studio Version Only)

Relight lets you introduce light sources into your scene, lighting up the objects inside it realistically. Whereas a Power Window keeps a fixed on-screen shape, Relight studies the forms of people and objects to build a Surface Map, then uses that map to bounce light appropriately. Tuned well, the effect can sell the illusion of light tracing an object's contours, glinting off highlights, and fading into shadow. Relight comes in handy when you wish there'd been an extra light on set, want to play up an existing light to match another shot, or want to make day-for-night grading more believable. NOTE: The Relight effect manufactures the illusion of depth through its analysis of a scene's surfaces, but it does not work out the 3D relationships among the scene's objects. Shapes can't be set to cast shadows, and depth data can't be produced.

### Setting up Relight

Studying the image to build a Surface Map is extremely demanding on the processor. Working out how light sources affect an existing analysis is, by comparison, very quick. By default, dropping Relight onto a node both builds the map and adds a light in a single step. That's handy, but moving the light position re-runs the effect, and so re-runs the analysis. That can make it sluggish to work with unless you've got an

extremely powerful computer. Happily, the work can be divided across two nodes — caching the analysis in the first node while you tweak light positions in the second. The full procedure follows below. Bear in mind you can add several light sources off the same analysis. With, say, three distinct lights in one scene reusing a single analysis, this runs three times faster than redoing the analysis for every light. And as an advanced option, the split method lets you draw on a Surface Map saved to disk, or one coming from a different application. Such packages can often output the “surface normals” of 3D models next to the images they generate, and these can be made compatible with Relight. Here a “normal” is a geometric term that describes the orientation of a surface. No single universal format exists for surface normals; check the External Map settings for some options that can assist with using these as Surface Maps in the plugin. Here's a sample node graph dividing the Relight across two stages: how to build a dual Relight Node Tree using two distinct Relight nodes, set up as shown. They've been named Surface Map and Lighting to keep things clear. In that example you've got the source video together with two Relight nodes. This is how they're connected:

- Feed the source video into the first RGB input (top green triangle) on both nodes.
- The first Relight Node ((RLT) Surface Map) builds the image's Surface Map when you

tick the “Output Surface Map” checkbox in the Relight effect's settings. Once ticked, the plugin shifts into analysis-only mode and the other options vanish. You can switch on Node Caching to build the Surface Map automatically in the background whenever you aren't using DaVinci Resolve. Route this node's RGB output into the second RGB input (bottom green triangle) on the second Relight Node.

- Over on the second Relight Node ((RLT) Lighting), switch the top option “Surface Map” away from its default of “Use Internal” over to “Use Input 2.” Every other setting stays on screen; this is the node where you'll dial in the light properties.

You can attach Power Windows, Qualifiers, or masks to either node, or to separate nodes joined via the first Alpha channel (top blue triangle) of either node. For instance, you could pick out a person with the magic mask and use it to confine the lighting to that person alone rather than the background.

The Relight Surface Map's output, which then feeds the input of the Relight Lighting node.

### Using Relight

The moment you first drop Relight onto a node and turn the lighting preview off, the image shows no visible change. That's because the map of what the light illuminates lives in the Alpha channel, primed for every one of DaVinci Resolve's color grading tools to act on. The easiest starting move is to raise Gain (boost it directly or add color); changes to gamma and saturation are often fitting too. For a day-for-night look you can invert the Alpha so a scene darkens everywhere except the lit areas, landing a day-for-night effect while the “light source” remains the original scene lighting.
