# Monitoring and grading to st 2084 for HDR vivid and HDR vivid grading workflow

Version: DaVinci Resolve 20.3 Reference Manual. Context: HDR setup and grading.
[Chapter index](INDEX.md) / [Previous section](hdr10-monitoring-and-grading.md) / [Next section](hybrid-log-gamma-hlg.md)
<a id="source-delivering-hdr-vivid"></a> <a id="source-enabling-simultaneous-monitoring-1"></a> <a id="source-hdr-vivid-controls-in-the-color-page"></a> <a id="source-hdr-vivid-grading-workflow"></a> <a id="source-hdr-vivid-trim-controls-in-davinci-resolve"></a> <a id="source-monitoring-and-grading-to-st2084-for-hdr-vivid"></a> <a id="source-necessary-hardware-1"></a> <a id="source-rendering-an-hdr-vivid-master"></a> <a id="source-simultaneous-master-and-target-display-output-for-hdr-vivid"></a>

### Monitoring and Grading to ST.2084 for HDR Vivid

For grading a program toward HD Vivid output, you’ll monitor an ST.2084 image, and all that demands is a ST.2084-compatible HDR display joined onto your output hardware — a DeckLink 8K, DeckLink 4K Extreme 12G, or UltraStudio 4K Extreme. Readying Resolve Color Management to grade for ST.2084 unfolds exactly as it does for Dolby Vision or ordinary HDR10. The video scopes are likewise observed the same and a master output the same, because every one of these standards depends on the same PQ curve. TIP: While monitoring on the built-in video scopes in DaVinci Resolve, turning on “HDR (ST.2084/HLG)” in the Waveform Scale Style settings within the Scopes option menu replaces the scopes’ 10-bit scale with one based on nit values (cd/m2).

### HDR Vivid Grading Workflow

The HDR Vivid workflow rests on grading the HDR version of every clip in your program first, then leaning on the automatic analysis to build a metadata-governed, downconverted tone mapped rendition of each shot. After the HDR Vivid trim pass wraps, you deliver the rendered HDR output carrying embedded HDR Vivid metadata.

### Simultaneous Master and Target Display Output for HDR Vivid

While mastering HDR and trimming versions destined for more limited displays, the ability to judge your HDR grade alongside the tone mapped trim pass is tremendously useful. As of DaVinci Resolve 15, both the Master Display output and the Target Display output can be emitted together whenever you grade with HDR Vivid switched on.

### Necessary Hardware

Going about it this way calls for the equipment below:

- A DaVinci Resolve grading workstation feeding its output through some video interface — a DeckLink 8K, a DeckLink 4K Extreme 12G, an UltraStudio 4K Extreme — or a superior model.
- A Mastering Display able to hit the HDR nit levels your required deliverable demands.
- An HDR target display that can be tuned to the correct tone mapped output.

Setup and Workflows | HDR Viewers HDR Setup and Grading

### Enabling Simultaneous Monitoring

Setting up your display hardware, send the HDR Master Display to output A and the Target Display to output B on whichever BMD video output device you happen to use. Next, switch on the “Use dual outputs on SDI” checkbox within the Master Settings of the Project Settings. From there, so long as every connection is mutually compatible, you ought to get an HDR image driving your HDR display and a trimmed image driving your SDR display.

### HDR Vivid Trim Controls in DaVinci Resolve

The newest HDR Vivid palette lays out three groups of controls, the first being the main controls:

- Target Display Output: This drop-down sets which parameters drive how the tone mapped image is shown. Through the menu you pick particular display properties to preview how the trimmed image reads on assorted displays spanning different gamuts and peak luminance capabilities.
- Trim Mode: Picks the toolset behind the trims, whether the Curve or the Statistical mode.
- Analyze controls: The commands that drive HDR Vivid auto-analysis show up as buttons,

doing the same jobs as their like-named siblings over in the Color > HDR Vivid submenu. Keep in mind that most trim controls stay greyed out until an analysis is run, a mandatory first move. All: Runs an automatic analysis on each clip in the present Timeline and banks each result separately. Selected: Restricts the analysis to selected shots in the Timeline. Frame: Handy where one stretch of a clip holds an extreme level of color or lightness atypical of the rest, skewing the analysis into a poor result. Park the playhead on a frame that captures how the clip ought to look and choose the Frame option to base the analysis on that frame alone. It’s also a quick route for clips where a single frame speaks for the whole shot.

- Enable Tone Mapping Preview: Surfaces the target display output in the Color page Viewer and the video output, so you can gauge how the tone mapped version reads on your HDR display.

Which controls come next depends on the Trim Mode you’ve chosen. Curve: The Curve trim mode opens up an assortment of controls letting the colorist tweak the trim metadata by hand at the clip or frame level. Offset, Brightness, and Detail settings cover the Dark and Bright stretches of the curve, while Midtones carry a brightness control. Highlight Crop reins any highlights that overshot the display’s top brightness — and thus blew out — back into range. Separate Global and Highlight saturation settings are on offer too. Statistical: The Statistical trim mode opens controls for fine-tuning the automatic tone mapping algorithm applied during the Analyze step.

Setup and Workflows | HDR Viewers HDR Setup and Grading

### HDR Vivid controls in the Color page

### Delivering HDR Vivid

After your HDR grade is finished and the SDR downconversion trimmed, the program needs outputting correctly over on the Deliver page.

### Rendering an HDR Vivid Master

For an HDR Vivid master once grading concludes, ensure the Output Color Space in the Project Settings’ Color Management panel is parked on the right HDR ST.2084 setting for your intended peak output (whatever exceeds it clips). After that, set your render to export an H.265, Quicktime, or MP4 codec under the Video Settings, tick the Embed HDR Vivid Metadata box, and pick the matching HDR mode you graded the master in from the drop-down box beneath.

HDR Vivid settings in the Video section of the Deliver page
