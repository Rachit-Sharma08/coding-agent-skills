# Color match palette and tips for properly shooting a color chart

Version: DaVinci Resolve 20.3 Reference Manual. Context: Automated grading commands and imported grades.
[Chapter index](INDEX.md) / [Next section](primaries-auto-adjustment-and-white-balance.md)
<a id="source-a-clip-before-and-after-automatic-color-matching"></a> <a id="source-automated-grading-commands-and-imported-grades"></a> <a id="source-automated-grading-commands-and-imported-grades-part-1"></a> <a id="source-color-match-palette"></a> <a id="source-configuration-controls"></a> <a id="source-how-to-use-color-match"></a> <a id="source-poorly-lit-chart-with-irregularly-topped-waveforms"></a> <a id="source-reset-controls"></a> <a id="source-the-color-match-palette"></a> <a id="source-tips-for-properly-shooting-a-color-chart"></a> <a id="source-well-lit-chart-with-flat-topped-waveforms"></a>

### Automated Grading Commands and Imported Grades

DaVinci Resolve offers an enormous range of hands-on grading controls that let you steer nearly every aspect of a digital image, yet DaVinci has also poured significant effort into research aimed at making colorists more productive by building automated grading features. On top of that, now that integrated editing has welcomed professional editors into a single environment for cutting, grading, and finishing inside DaVinci Resolve, those same automation features designed to send colorists home sooner can equally help editors who aren't colorists handle the more straightforward grading chores.

### Color Match Palette

When the camera crew and lighting team are thoughtful enough to capture a color test chart at each of the principal lighting configurations across the project you're working on, DaVinci Resolve can overlay a grid of sample points onto a chart within a clip and run a mathematical analysis of those sampled values to build an automatic correction. The Color Match palette gives you controls for setting the Source Gamma, Target Gamma, and Target Color Space, ensuring the correction it produces suits both the camera that recorded the footage and the project configuration you've established. These standardized color charts are recognized by the Color Match palette:

- Datacolor SpyderCheckr 24
- DSC Labs ChromaDumonde 24+4
- DSC Labs SMPTE OneShot
- X-Rite ColorChecker Classic
- X-Rite ColorChecker Classic - Legacy
- X-Rite ColorChecker Video
- X-Rite ColorChecker Passport Video

A side-by-side comparison of the X-Rite ColorChecker, Datacolor SpyderCheckr, plus DSC Labs SMPTE OneShot charts, every one of them recognized within the Color Match palette The analysis yields an automatic color correction that establishes a neutral grade for the shot, giving you a base from which to build the remainder of your grade.

### Tips for Properly Shooting a Color Chart

How well Color Match performs hinges entirely on the way the charts were captured on location. Shoot the charts correctly and the outcome will be excellent; capture them badly and the outcome becomes erratic. Follow these recommendations to coax the strongest possible results out of Color Match:

- Light the chart uniformly so that each patch receives identical intensity (level) and color. Wherever shadows fall or the lighting color shifts across the chart, Color Match will attempt to correct for those variations and an imprecise match is the outcome. If you preview a chart on a waveform monitor while it's being lit ahead of the shoot, each patch as displayed on the scope ought to look like a rectangle with a "flat top."

### Poorly lit chart with irregularly topped waveforms

### Well lit chart with flat-topped waveforms

- None of the chart's patches should clip in any of the RGB color channels. Whenever a channel clips, Color Match is fed wrong RGB values, and that throws off the resulting match.
- Aim to record the chart's white patch somewhere in the 70–95 IRE/percent window. Nailing exposure matters a great deal here, and although Color Match offers a measure of leeway through the White Level option, you'll only get reliable output when the original chart was captured with its white patch landing inside the 70–95 IRE/percent band on a waveform monitor. Avoid recording a white patch above 95 IRE/ percent, because at those levels one of the RGB channels is typically near clipping or already clipping, which produces an imprecise match.
- Set the Source Gamma option so it corresponds to the encoded OETF (opto-electrical transfer function, or gamma) carried by the recorded image. Producing a faithful adjustment requires Color Match to work with image data that is scene linear (linear to light). The majority of captured or recorded footage carries a tone curve (gamma curve) applied to make the most of the available bit depth, and various cameras apply distinct gamma curves to draw the most out of their particular sensors. Because the Color Match algorithm first transforms the image data into a scene linear space prior to building an adjustment, it has to reverse the gamma curve introduced by the camera or the debayer stage. Choose the wrong Source Gamma value in the Match Color palette and the data won't linearize properly, leaving you with an imprecise match.
- A scene whose lighting has an odd spectral response or a pronounced color tint can produce an imprecise match. When a scene is illuminated by sources with an unusual spectral response (cheap fluorescent tubes, low-grade LED fixtures, or mercury vapor lamps whose spectral power distribution is extremely narrow or spiky), metameric errors can appear both in how the camera responds and in how the Color Match function behaves, yielding an imprecise adjustment. You'll get the cleanest results when the scene's lighting has a chromaticity sitting near the black body locus (with a tightly correlated color temperature) together with a reasonably smooth spectral power distribution. Put simply, rely on high-quality lighting free of spikes in particular regions of the spectrum.
- A wide gap between the color temperature of the light falling directly onto the chart and the ambient light filling the rest of the scene can produce perceptual errors. Frequently the issue stems from perception rather than a genuinely wrong color adjustment. Take an exterior scene lit artificially with fixtures throwing extremely warm light (color temperatures down around 3200K or below) while cooler ambient light fills the surroundings: matched to a Target Color Temp of 6500K, it can read as excessively blue. The reason is that the chart sitting under the direct fixtures is lit at the warmer (yellower) color temperature, whereas shadowed regions of the scene run far cooler thanks to the ambient "blue" skylight; the upshot is an automatic color adjustment that suits the chart yet looks overdone across the rest of the frame.

### How to Use Color Match

The procedure below demonstrates building a color correction with the Color Match palette and its overlay.

### The Color Match palette

To sample a color chart to make an automatic correction: 1 Pick the clip containing the chart you intend to sample. When needed, the View > Show Current Clip With Handles option reveals extra frames ahead of the present clip so a color chart sitting in the media's leader becomes visible. 2 When needed, pick the entry from the Source Gamma drop-down menu that matches the gamma used while the footage was recorded. 3 Next, select a target gamma and color space matching the format you intend this clip to be matched against. 4 Open the Viewer tool drop-down, select the Color Chart overlay, and work its corner-pinning controls to align the sampling boxes against the color patches on the chart.

Aligning the Color Match target with the chart in the video 5 Once you're done, press the Match button and the clip receives its automatic correction.

### A clip before and after automatic color matching

TIP: Bear in mind that a chart isn't required for every shot. Where a location's lighting holds steady throughout a scene, a single chart analysis is enough to build a correction you then copy onto all the remaining clips of that same scene. Naturally, when several cameras are at work in one scene, you'll want a separate chart analysis per camera if your goal is to bring them into closer agreement. And for a scene stretched across an entire day, consider capturing charts whenever the time shifts enough to track the lighting changes underway.

### Configuration Controls

What follows breaks down in greater depth each parameter you'll find in the Color Match palette.

- Source Gamma: Sets the source gamma that the footage was captured with. Picking the right gamma is mandatory or the output loses accuracy.
- Target Gamma: Lets you pick the target gamma you want the corrected clip to adopt. Although this is usually the gamma at which you'll deliver the finished program, alternative target gamma values are available for specialized workflows.
- Target Color Space: The color space in which you'll deliver the finished program.
- Color Temp: A tunable color temperature control letting you hand-adjust the target

color balance of the resulting correction toward warmer (lower values) or cooler (higher values). The default is 6500K.

- White Level: A checkbox, off by default, that lets you hand-pick the target white point the automatic correction will rely on. Pushing this value up or down expands or tightens the contrast of the finished correction.
- Match button: After you've dialed in the right settings and lined the color match target up with the chart that was captured, click to run the match.
- Chart type drop-down menu: This drop-down lets you pick from the chart types that are supported. As of this writing, the roster includes Datacolor SpyderCheckr24, then theChromaDuMonde 24+4, followed by DSC Labs SMPTE OneShot, alongside X-Rite ColorChecker Classic, plus X-Rite ColorChecker Classic - Legacy, as well as X-Rite ColorChecker Video, and finally X-Rite ColorChecker Passport Video.
- Reset All button: Clears every control and adjustment within this palette.

### Reset Controls

Within the Color Match option menu sit several commands letting you undo work you've done in the Color Match palette.

- Reset Match Configuration: Restores the Configuration parameters covered above.
- Reset Applied Match: Clears the matching operation while leaving the Configuration controls untouched.
