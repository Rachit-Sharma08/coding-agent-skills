# Gamut stabilization contrast DCTL and dehaze

Version: DaVinci Resolve 20.3 Reference Manual. Context: Color space transform, Color stabilizer studio version only, Contrast pop studio version only, DCTL studio version only, Dehaze studio version only.
[Chapter index](INDEX.md) / [Previous section](aces-chromatic-adaptation-and-color-transforms.md) / [Next section](despill-and-false-color.md) / [Color Space Transform](aces-chromatic-adaptation-and-color-transforms.md)
<a id="source-advanced"></a> <a id="source-analysis-region"></a> <a id="source-captured-analysis-values"></a> <a id="source-channels-to-stabilize"></a> <a id="source-color-stabilizer-studio-version-only"></a> <a id="source-contrast-pop-studio-version-only"></a> <a id="source-dctl-studio-version-only"></a> <a id="source-dehaze-studio-version-only"></a> <a id="source-gamut-mapping"></a>

### Gamut Mapping

Choosing a Gamut Mapping Method serves pipelines where one color space must become another with a vastly larger or smaller gamut, helping to automate a stretch or squeeze of image saturation so the result reads as pleasing and naturalistic without clipping.

- Choosing None results in no Gamut mapping at all.
- Picking Saturation Mapping out of this menu switches on saturation mapping so it can squeeze the span of

saturation values coming from the Input Color Space and Gamma down into the Output Color Space and Gamma. Doing so switches on the Saturation Knee and Saturation Max. controls. Where saturation mapping kicks in is set by the Saturation Knee slider, marking an image level beneath which nothing gets remapped. From that level upward, every saturation value gets remapped per the Saturation Max. slider. Here, 1.0 stands for the fullest saturation possible within whatever output color space is active. As for the Saturation Max slider, it fixes the fresh ceiling you'd like every saturation value above the Saturation Knee setting raised or lowered to. Once again, a reading of 1.0 marks peak saturation inside the output color space you've currently got selected.

- Choosing "Clip" hard clips all out-of-gamut values.

NOTE: Even though this plugin carries ACES settings, the way it converts into the ACES color space is colormetric, which isn't truly correct for ACES pipelines. When you're on a genuine ACES pipeline, reach instead for the ACES Transform plugin, which draws on the transforms the Academy specifies.

### Advanced

This drop-down opens up the advanced capabilities of the Color Space Transform effect.

- Apply Forward OOTF: Tick this box to take the image from scene-referred over to display-referred color management.
- Apply Inverse OOTF: Tick this box to take the image from display-referred over to scene-referred color management.
- Use white point adaptation: Runs a chromatic adaptation transform to reconcile differing white points across color spaces. Leave this box unticked if you'd simply like to see the input color space's white point carried into the output color space untouched. As an example, you might want a P3-D60 mastered clip inside a P3-D65 timeline strictly for reference. Tick the box to run the chromatic adaptation transform, converting the input white point so it lines up with the output color space's white point. As an example, you might want a P3-D60 mastered clip to intercut cleanly with other clips mastered in a P3-D65 timeline.

### Color Stabilizer (Studio Version Only)

Built to handle clips suffering from inconsistent exposure and color—brought on by hand-twisting a lens's aperture, or by a camera's auto exposure and white balance shifting color and brightness partway through a shot in unwanted ways. The Color Stabilizer plugin examines one frame of the clip that embodies the exposure and color you want, then automatically brings every other frame of the current clip into line with those analyzed levels. IMPORTANT: You'll get the strongest results out of the Color Stabilizer on clips whose highlights aren't clipped. Within the Color page, the advice is to first grade the image so all the highlights you care about land at or below a value of 1023, then drop the Color Stabilizer onto a node downstream of that adjustment. The Color Stabilizer is best run before you grade the image. Grade ahead of running the Color Stabilizer and the outcome can turn unpredictable. The Color Stabilizer can be put to work in two ways:

- The simplest route is to pick Entire Frame from the Region of Analysis pop-up menu. Next, slide the playhead in the Viewer onto the frame holding the contrast and color you want spread across the whole clip, and hit the Analyze Now button. Now play back through the clip and the shifts in contrast and color ought to be gone. This route works best on clips where the inconsistency you're out to remove affects the whole picture.
- An alternative is to pick Selected Area from the Region of Analysis pop-up menu. Doing so brings up an onscreen rectangle you can resize and drag over a particular region you'd like to sample across the clip's length. If the feature you've selected to analyze happens to be moving, you can lean on the FX Tracker to follow the subject so the selection box trails it (which matters for a steady result). With that arranged, slide the playhead in the Viewer onto the frame holding the contrast and color you want the whole clip to carry, and hit the Analyze Now button. Now play through the clip and the contrast and color shifts should be gone. This lets you steady the shot's color even as dark objects pass through the frame or the highlights change level. The selection box lets you zero in on analyzing the part of the frame carrying the unwanted exposure change while leaving the desirable exposure change alone.

Which extra options surface will vary according to the choice you make in the Region for Analysis pop-up menu.

### Analysis Region

Pick "Selected Area" from the Region of Analysis pop-up and a rectangle shows up in the Viewer, whose position, scale, and size you govern by clicking and dragging its corners in the Viewer. These on-screen controls let you reshape the selection box that marks which slice of the image gets analyzed.

### Channels to Stabilize

Once the frame holding that clip's ideal contrast and color has been analyzed, you'll decide how the correction happens by way of the Channels to Stabilize controls. Through the What to Stabilize pop-up menu you pick between stabilizing White Balance and Brightness, or R, G, B Channels Separately.

- Pick White Balance and Brightness, and two checkboxes let you decide independently whether to bring in Stabilize White Balance and Stabilize Brightness.
- Pick R, G, B channels separately, and three checkboxes turn up for Stabilize Red, Green, and Blue Channel, so you get to single out exactly which channels to correct.

Through the Stabilize drop-down menu you pick how the correction gets applied, its choices being Levels and Contrast, Offset, and Gain. Each one tackles the needed correction by a separate method, so should one fall short on whatever specific trouble your clip is showing, you're free to fall back on the others in pursuit of a better outcome.

### Captured Analysis Values

With the frame analyzed, a further set of parameters surfaces showing the captured analysis values that the automated correction rests on, so you can tweak things by hand where needed to sharpen the outcome. Which parameters appear hinges on the option you settled on in the What to Stabilize pop-up menu.

- Had you chosen White Balance and Brightness, you'll get a Normalized White Balance color control plus Low Level and High Level sliders.
- Had you chosen R, G, B Channels Separately, you'll get Red, Green, and Blue High and Low Level sliders.

### Contrast Pop (Studio Version Only)

A harsher, more targeted take on the Midtone Detail control over in the Color Wheels palette, crafted to drop either crisp high-contrast looks or gentle low-contrast looks onto a chosen slice of the image's tonal range.

- Detail Amount: Lets you set how heavily this effect lands. At 0, nothing is applied. Push into positive values and progressively crisper contrast builds, while negative values bring on progressively softer low-contrast.
- Detail size: Lets you pick which image structures this local contrast tweak touches, ranging from smaller ones to larger ones.
- Low and High Threshold: With these values you mark out which slice of image tonality the filter acts on, so you can leave either shadows or highlights out of the operation.
- Softness: Lets you ease the transition between the image's affected and untouched regions.

### DCTL (Studio Version Only)

Gives you a way to drop in a DCTL anywhere ResolveFX plugins are allowed. To dig deeper into DCTLs along with their install locations, consult Chapter 201, "Creating DCTL LUTs."

- DCTL List: A pop-up through which you select among the DCTLs that are already present at the location on your machine. Under Mac OS X, that path reads Library/Application Support/Blackmagic Design/DaVinci Resolve/LUT/ whereas on a Windows box it becomes C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\LUT and for Linux users the folder is /home/resolve/LUT
- Reload DCTL: Lets users refresh the content of the currently loaded DCTL file. With it, you can edit the DCTL in a text editor and then reload to view the outcome. It won't refresh the DCTL list, though; for that you have to relaunch the DaVinci Resolve application.

### Dehaze (Studio Version Only)

Crafted to let you tweak color and contrast so the visible signs of Aerial Perspective (that is, smog, airlight, and haze) in an image are toned down. The filter builds a simulated depth map on its own, drawn upon to lay more of this corrective color tweak onto distant parts of the image—those a haze would hit hardest—and less onto the nearby parts. It gauges haze and provides options for steering that estimate and shaping the processing.

- Dehaze Strength: This slider lays down a color and contrast tweak at once. Pushing Dehaze Strength up gently lifts contrast (the shadows most of all) while rebalancing color toward the complement of the chosen Haze Color and selectively boosting saturation. Pulling Dehaze Strength down lowers contrast and rebalances color back toward the chosen Haze Color itself while selectively trimming saturation.
- Haze Color: A color control letting you pick or sample the color of the smog, airlight, or haze in an image that you'd like to cut down.
- Display Depth: Lets you look at the simulated depth matte being built. Switch this on before you touch the Shadow and Highlight controls below.
- Shadow: This slider lifts or lowers the darkest stretches of the simulated depth map that mark which parts of the image are reckoned to be farthest away.
- Highlight: This slider lets you lift or lower the lightest stretches of the simulated depth map that mark which parts of the image are reckoned to sit closest to us.
