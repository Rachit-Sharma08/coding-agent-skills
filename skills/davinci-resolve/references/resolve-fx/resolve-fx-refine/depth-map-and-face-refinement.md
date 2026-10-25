# Depth map and face refinement

Version: DaVinci Resolve 20.3 Reference Manual. Context: Depth map studio version only, Face refinement studio version only.
[Chapter index](INDEX.md) / [Previous section](beauty-and-custom-mixer.md) / [Next section](face-refinement-detection.md) / [Continue Face Refinement (Studio Version Only) / Skin Isolation](face-refinement-detection.md)
<a id="source-advanced-options-1"></a> <a id="source-depth-map-studio-version-only"></a> <a id="source-face-refinement-studio-version-only"></a> <a id="source-isolate-specific-depth"></a> <a id="source-main-controls"></a> <a id="source-map-finesse"></a> <a id="source-resulting-map-adjustment"></a> <a id="source-the-original-footage-with-a-distracting-background"></a>

### Depth Map (Studio Version Only)

NOTE: The Depth Map Resolve FX has seen sizable behind-the-scenes improvement and an update from DaVinci Resolve 20 onward. Its interface and usage stay as they were, yet you should get markedly more precise results out of the tool. The fresh Depth Map v2 has taken the original's place and gets applied automatically whenever you use the Depth Map effect. Depth Map builds an Alpha channel from how far away the objects in your clip appear. Being able to single out a particular depth region greatly widens what you can do to the resulting image. As one example, teamed with a Fast-Noise plugin you could fake a fog effect kept solely to the far background of your shot. You could lift a foreground object such as a person by raising contrast, saturation, and sharpness, much as a qualifier would. A Depth Map can mend video troubles too — say, correcting a color temperature issue by isolating a distant window shot in daylight that tinted background actors blue, while sparing the foreground subject lit by studio lighting. Depth Map can additionally pair with DaVinci Resolve's other windows and keying tools to assemble more elaborate rotoscoping and keys with less work. The resulting Depth Map Alpha channel is shown as a black-and-white image, white marking the area the changes affect and black areas staying untouched.

(Top) The original image. (Bottom) The scene's Depth Map v2 analysis; white marking areas "closer" to the camera and black marking those farther off

### Main Controls

These controls establish the Depth Map's chief parameters.

- Quality: Depth Map is a heavily computational effect. The quality setting offers a Faster mode that quickens how responsively adjustments register, whereas the default Better mode yields the best results and ought to be on once the adjustments are done.
- Depth Map Preview: This box is ticked by default and presents the current Depth Map for your adjustments. Switch it off and the resulting alpha becomes usable for grading on other nodes. Should you have applied the effect to a corrector node, be sure to right-click the Depth Map's node and choose "Use OFX Alpha" so the node passes the effect's Alpha channel correctly.
- Invert: Ticking this box flips the Depth Map, swapping its transparent and opaque regions.

### Resulting Map Adjustment

These controls let you decide how the Depth Map's contrast gets adjusted.

- Adjust Map Levels: Left off (the default), DaVinci Resolve's grading tools (lift, gamma, gain, etc.) can work the Depth Map's whole range. Switched on, this option clips the Depth Map's levels to 0 and 1, serving as a preview of what becomes of the Depth Map once it's used as an Alpha channel, where DaVinci Resolve always clips the values to 0 and 1.
- Far Limit: This control tunes the Depth Map's black levels.
- Near Limit: This control tunes the Depth Map's white levels.
- Gamma: This control nudges the in-between depth values brighter or dimmer relative to

the fixed black and white levels.

### Isolate Specific Depth

These controls let you glide back and forth through the scene by depth, so you can isolate a particular depth range to adjust.

- Isolation: This checkbox switches the depth isolation tools on or off.
- Target Depth: This sets the exact depth you want isolated. 1 sits fully in the foreground,

whereas 0 sits fully in the background.

- Tolerance: Fixes how much range on each side of the Target Depth is folded into the Depth Map.
- Softness: This adds a gentle ramp-in and ramp-out to the chosen range, lending it a more

organic selection.

### Map Finesse

These controls reshape the resulting Depth Map's Alpha channel so it's ready for grading.

- Post Processing: This control switches the Map Finesse tools on or off.
- Post Filter: Smooths the depth map along the image contours.
- Contract/Expand: This control swells or shrinks the overall shape at its edges, handy for fine-

tuning the border between the map's affected and unaffected regions.

- Blur: This control softens the map's border so it blends more smoothly into the

resulting image.

### Advanced Options

These controls instruct the Depth Map on how to deal with assorted blanking issues.

- Blanking Regions: These controls instruct the Depth Map on handling letter and pillar boxing regions within the effect. Process Entire Frame: Has the AI disregard any data about the timeline shape and simply process every visible pixel. Handle Automatically (default): The AI processes only the area DaVinci Resolve recognizes as holding your media. Auto + Extra Crop: Advised for trimming away black bars; it leans on DaVinci Resolve's awareness of which pixels your media filled while letting you crop out the framing or letterboxing relative to its shape. It's advised because it holds steady as you tweak Timeline settings. Manual Cropping: Simply lets you override whatever the content's framing is, disregarding any of DaVinci Resolve's awareness of your media's shape.

As an example, suppose you have footage of a person filmed on a rainy day, but the background is overly distracting and contrasty. Building a depth map that isolates only the foreground person lets us then put a Fast Noise smoke effect on the background alone, giving it a foggy-mist look that's less of a distraction.

### The original footage with a distracting background

That same footage with a Fast Noise Smoke effect node faking a fine mist, except it blankets the whole frame, the main subject included. For realism, the mist belongs in the background alone.

Dropping a node carrying Depth Map between the original nodes lets you use the effect to pull a key based purely on "distance" from the camera. Here we've picked the background (white) and ruled out the woman with the umbrella (black). Notice the fine detail in the furry coat, which an HSL or window qualifier would struggle to capture.

The process's end result shows the main subject up front with the Fast Noise smoke effect held to the background only. TIP: For more convincing Depth of Field adjustments, run the Depth Map effect alongside the Tilt-Shift Blur effect. You can route the Depth Map's results straight into the Tilt-Shift Blur effect as a blur map by joining the Depth Map node's key output to the Tilt-Shift Blur node's key input and choosing "From Alpha In" from the Map Source drop-down within the effect's Depth of Field section. From there, tune the Focus Sweep to home in on the area you want isolated. If the results aren't what you expected, try inverting the Depth Map.

### Face Refinement (Studio Version Only)

The Face Refinement effect now boasts better tracking, profile handling, and smooth skin options. The freshly revised effect is laid out below. Face Refinement is a remarkably sophisticated yet approachable filter that lets you rapidly make highly targeted tweaks to people's complexions. To put the face refinement toolset to work, your first job is to identify the face (or faces) you intend to work on, then analyze and track that face across the clip. You identify a face by clicking the Detect Faces in Frame button. When faces sit in the frame at the playhead's position, the result is boxes drawn over each detectable face. Click any of those boxes to pick the face you want to refine, and that box highlights green to show which face you'll be refining.

With several faces detected, you can click a box to pick the one to work on. Having chosen the face to work on, you then use the tracking controls to track it across the clip, and an outline of the face's main features shows up so you can follow along.
