# Dirt chromatic aberration and dead pixel removal

Version: DaVinci Resolve 20.3 Reference Manual. Context: Automatic dirt removal studio version only, Chromatic aberration removal studio version only, Dead pixel fixer studio version only.
[Chapter index](INDEX.md) / [Next section](dead-pixel-fixer-and-deband.md)
<a id="source-aberration-correction"></a> <a id="source-advanced-options"></a> <a id="source-automatic-dirt-removal-studio-version-only"></a> <a id="source-chromatic-aberration-removal-studio-version-only"></a> <a id="source-dead-pixel-fixer-studio-version-only"></a> <a id="source-estimation-options"></a> <a id="source-fine-controls"></a> <a id="source-main-controls"></a> <a id="source-multiple-dead-pixel-removal-patches"></a> <a id="source-resolve-fx-revival"></a> <a id="source-resolve-fx-revival-part-1"></a>

### Resolve FX Revival

Gathered in this category are plugins for sorting out the everyday technical, damage, and quality troubles that plague programs in the midst of finishing, remastering, or restoration.

### Automatic Dirt Removal (Studio Version Only)

Optical flow technology drives the Automatic Dirt Removal plugin, which pinpoints and mends temporally unstable specks of dust, dirt, hair, tape hits, and similar unwanted artifacts that flash by for a frame or two before vanishing. Every repair preserves structurally consistent detail in the frame underneath, so the image comes out restored at high quality. Happily, for all its sophistication the plugin is fairly easy to operate; you simply drop it onto a shot, tune the parameters for the best outcome, and let it run.

(Left) Original image, (Right) Using Automatic Dirt Removal. NOTE: The plugin fares worse against vertical scratches that stay fixed in one position across multiple frames, and it does nothing at all for lens dirt that lingers for the whole shot.

### Main Controls

The main controls govern how much dirt the filter strips from the image.

- Motion Estimation Type: Offers a pick among None, Faster, Normal, and Better. This sets where you land on the performance-versus-quality tradeoff.
- Neighbor Frames: Sets how many frames get compared while dirt is being detected. Comparing more frames lengthens processing, yet generally turns up more dirt and artifacts.
- Repair Strength: A slider that sets how aggressively found dirt and artifacts get repaired. Lower settings can let small specks slip by that may or may not really be dirt, whereas higher settings wipe out everything turned up.
- Dirt Size Threshold: A slider that sets how big a detected speck of dirt has to be before it’s removed. Pushing this parameter up keeps things like film grain out of the operation, though it may let smaller specks of dirt through.
- Show Repair Mask: A checkbox that displays the detected dirt and artifacts on their own, letting you judge how effective the results are while you fine tune this filter.

### Fine Controls

These controls let you fine tune the effect as you chase the ideal balance between clearing dirt successfully and holding onto genuine image detail.

- Motion Threshold: A slider that sets the point above which moving pixels get treated as dirt and artifacts. Lower values let more dirt escape correction but leave you with fewer motion artifacts. Higher values clear more dirt, though footage with camera or subject motion may show more motion artifacts as a result.
- Edge Ignore: A slider for shielding the picture’s hard edges from being touched by the dirt or artifacts being removed. The higher the value, the more edges get left untouched.

### Chromatic Aberration Removal (Studio Version Only)

A Revival category plugin for correcting by hand the faint color fringing that a lens’s chromatic aberration leaves behind. The Show Estimated Fringes checkboxes for the RGB channels bring up an “alignment guide” that sets each fringing type apart visually against gray. (Left) The original image in close up, with chromatic aberration on show; (Right) the same image once Estimated Red Fringes is on, which surfaces the precise problems as differences between red and cyan stripes.

### Advanced Options

Advanced Options supply extra parameters for troublesome shots.

- Lens Center: The Center X and Y parameters shift the lens center when you’re working on a reframed and re-rendered shot. You can also reposition by dragging the lens center on-screen control inside the Viewer.
- Stronger Correction: Points out where image features that look like fringing sit.

### Estimation Options

The Estimation options exist only to highlight and pinpoint regions of fringing. They leave the image’s final output untouched. They turn available solely once one of the Show Estimated Fringes boxes is ticked in the Aberration Correction section.

- R/C, G/P, B/Y Balance: These tools shift the incoming balance between their respective colors to make hard-to-spot fringing easier to identify.
- Brightness: Amplifies the fringe indicators shown whenever you switch on either of the Estimated Fringes checkboxes.

### Aberration Correction

These tools let you correct aberration troubles by hand.

- R/C, G/P, B/Y Scale: Work these sliders to clear the fringing out of their respective colors.
- R/C, G/P, B/Y Edge: Work these to offset the fringing difference brought on by the curvature of the

lens’ edges.

- Show Estimated Fringes: Tick this box to display nothing but the estimated fringes over a gray

background. Ticking it also switches on the Estimation Options sliders, which help you highlight and pin down fringing regions further. From there it’s simple to correct the problem by hand, leaning on the Scale and Edge controls to treat Red/Cyan, Green/Purple, and Blue/Yellow fringing one at a time.

(Left) The original image in close up, with chromatic aberration appearing as a cyan fringe down the right of the smokestack and a red fringe along the building’s nearest corner; (Right) the corrected image in close up, the fringe now gone.

### Dead Pixel Fixer (Studio Version Only)

When you have clips shot on a camera whose sensor carries one or more “dead” or “stuck” pixels, the image may show black or white spots locked in one place. This filter is built to let you lay patches over each dead or stuck pixel, marking them out so you can apply various fix methods. The Dead Pixel Fixer resembles the Dust Buster in many ways, but the Dust Buster effect targets fleeting bits of dust and dirt that survive only a frame or two, while the Dead Pixel Fixer is meant for blemishes pinned in place across a clip’s whole length. To mend dead or stuck pixels, apply the Dead Pixel Fixer filter, confirm the OFX onscreen controls are switched on in the viewer, then click each pixel you need fixed with the mouse to drop a patch on it. Click anywhere on the image to lay down as many patches as you want — there’s no cap. An Option-click removes patches you no longer need. To relocate a patch, just drag it elsewhere.

### Multiple dead pixel removal patches

Once several patches are down, a click selects whichever patches you’d like to set the controls for. The control settings can differ from one patch to the next.
