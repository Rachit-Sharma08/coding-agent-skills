# Dolby vision mapping analysis and licensing

Version: DaVinci Resolve 20.3 Reference Manual. Context: HDR setup and grading.
[Chapter index](INDEX.md) / [Previous section](hdmi-tunneling-using-decklink-8k-pro-g2.md) / [Next section](dolby-vision-cm-v4-controls-preview-and-trim.md)
<a id="source-analyzed-clips-have-hdr-badges-to-identify-them"></a> <a id="source-auto-analysis-is-available-to-all-studio-users"></a> <a id="source-dolby-vision-cm-v29-controls"></a> <a id="source-dolby-vision-trim-controls-in-davinci-resolve"></a> <a id="source-external-content-mapping-unit-ecmu-for-dolby-vision"></a> <a id="source-licensing-davinci-resolve-to-expose-dolby-vision-trim-controls"></a> <a id="source-the-metadata-fields-for-each-clip"></a>

### External Content Mapping Unit (eCMU) for Dolby Vision

For studios tackling heavier HDR mastering, DaVinci Resolve accommodates a Dolby External Content Mapping Unit (eCMU), which drives an HDR display alongside an SDR display so you can trim side by side at high resolutions in hardware. On top of that, the eCMU can show Dolby Vision live on a consumer display through HDMI tunneling, giving you a direct look at what home viewers will get.

### Auto Analysis is Available to All Studio Users

Whether or not they hold a license, Resolve Studio users can have the image analyzed automatically and Dolby Vision analysis metadata produced. That metadata serves both to deliver Dolby Vision content and to render the other HDR and SDR deliverables out of the HDR grade you built. As a result, any DaVinci Resolve Studio user is able to turn out Dolby Vision deliverables carrying Level 1 metadata. Trimming that analysis metadata by hand, though, calls for a license from Dolby.

HDR Setup and Grading — within Setup and Workflows, under HDR Viewers

Every Resolve Studio user can reach the commands that drive Dolby Vision auto-analysis; they sit both under the Color > Dolby Vision™ submenu and inside the Dolby Vision palette, and the list runs:

- Analyze All Shots: Runs analysis on every Timeline clip on its own and saves each result separately.
- Analyze Selected Shot(s): Confines the analysis to whichever shots are selected on the Timeline.
- Analyze Selected And Blend: Treats several selected shots as though they formed one continuous sequence. Each clip then receives the identical analysis result. Handy for cutting down time when the clips you analyze share the same content.
- Analyze Current Frame: A quick approach for clips where one frame stands in for the whole shot.

After a clip is analyzed, the Min, Max, and Average fields fill in on their own with the produced L1 data; you cannot edit those fields.

### The metadata fields for each clip

On top of that, an analyzed clip displays an HDR badge in the Thumbnail timeline, which helps you track at a glance which clips are done and which still await analysis.

### Analyzed clips have HDR badges to identify them

### Licensing DaVinci Resolve to Expose Dolby Vision Trim Controls

Surfacing the DaVinci Resolve Studio Dolby Vision controls that allow manual trims atop the automatic analysis every DaVinci Resolve Studio copy performs starts with emailing dolbyvisionmastering@dolby.com for details on securing a license. After Dolby hands you a license file, bring it in via File > Dolby Vision > Load License; once it installs cleanly the Dolby Vision controls become available on the Color page. You ought to receive a display configuration file as well, loadable through the File > Dolby Vision > Load Configuration command, which fills the Dolby Vision drop-down menus with the freshest options.

HDR Setup and Grading — within Setup and Workflows, under HDR Viewers

### Dolby Vision® Trim Controls in DaVinci Resolve

With a clip analyzed, you can go ahead and trim the outcome. The current Dolby Vision palette puts forward four groups of controls. First come the main controls:

- Target Display Output: This drop-down names what Dolby calls the Target Display, the one used to show the tone mapped image. Through the menu you pick particular display characteristics so you can preview how the trimmed image will read on assorted displays with differing gamuts and peak luminance ceilings. Clicking the small chain icon just left of the options links the Target Display Output and Trim Controls For fields together. Doing so makes the Trim Controls For field track whatever value you assigned in the Target Display Output, keeping your trim controls correct for the display in question.
- Trim Controls for: The particular Target Display you are trimming for right now. Its default state (100-nit, BT.709, BT.1886, Full) lets you watch an SDR rendition of the HDR image, revealing how the trim metadata tone maps it on televisions that are not HDR.
- Analyze controls: The commands behind Dolby Vision auto-analysis appear here as buttons that do exactly what their like-named entries in the Color > Dolby Vision submenu do. Note that the bulk of trim controls stay greyed out until an analysis has run, which is a required first step.

All: Runs analysis on every clip in the present Timeline and keeps each result separate. Selected: Restricts analysis to the shots picked on the Timeline. Blend: Handles several selected shots as though they were one unbroken sequence. Every clip ends up with the same analysis result. Reach for the blend option when two clips meet at a through edit that splits frames which are otherwise continuous. Blend is likewise the usual pick for a scene of clips shot at the same place and time, so that ordinary lighting shifts do not introduce unwanted differences between the analyses of clips meant to already match each other. Blend additionally trims time when the clips you analyze hold identical content. Frame: Comes in handy when a portion of a clip carries an extreme color or brightness atypical of the rest, throwing off the analysis and yielding a poor result. Parking the playhead on a frame that fairly represents the clip’s intended look and selecting the Frame option grounds the analysis in that frame alone. It is also a quick way to analyze clips where one frame stands in for the whole shot.

- Enable Tone Mapping Preview: Surfaces the target display output in the Color page Viewer and on the video output, letting you judge how the tone mapped version reads on your HDR display. The control switches off once you turn on “Use dual-outputs on SDI,” a toggle living in the Project Settings’ Master Settings, because the second SDI output then shows the target display output for you.
- Mid Tone Offset (CM v4.0 only): Use this control to line up overall exposure between the tone mapped SDR signal and the HDR master. The offset lands on the L1 Mid values, so you can nudge the mid tones while leaving blacks and highlights alone. It can shift the overall L1 analysis to best protect the artistic intent. Because the setting is shared across every trim pass at every nit level, if you ran two passes — say one at 100 nits and one at 1000 nits — changing it always moves both passes together. Whatever you do to this control gets logged into each clip’s L3 metadata.

Second come the Min, Mid, and Max metadata fields, filled in from the current clip’s analyzed values. Although you cannot edit these fields, analysis metadata may be copied and pasted between clips. The figures stand for the L1 analysis and feed the calculation of how the HDR image gets trimmed to fit the video standard the Target Display calls for. Third are the Primary Trims, editable only after an analysis has run and only when you hold a Dolby license. Exactly which controls appear comes down to the Dolby Vision version you chose in the Color Management panel of the Project Settings.

HDR Setup and Grading — within Setup and Workflows, under HDR Viewers

### Dolby Vision CM v2.9 Controls

Choose Dolby Vision 2.9 from the Project Settings’ Color Management panel and you switch on the 2.9 build of Dolby’s content mapping algorithm, which brings up the original Dolby Vision trim controls. Relying on these is no longer advised, given that you can analyze and trim with Dolby Vision 4.0 yet still export converted 2.9 metadata for legacy workflows.

- Lift/Gamma/Gain: These behave much like the Y-only Lift, Gamma, and Gain master wheels in the Color Wheels palette, giving you a way to trim the image’s overall contrast levels. According to the Dolby Best Practices Guide, you should cap positive Lift at 0.025 and lean chiefly on Gamma and Gain when the image needs brightening.
- Saturation Gain: Trims the saturation of a scene’s most heavily saturated regions. Areas with weaker saturation feel less of the change.
- Chroma Weight: Deepens the saturated portions of the image to keep color richness in spots that smaller gamuts clip because they lack the headroom for saturation up in the highlights.
- Tone Detail: Helps you hold onto contrast detail in the highlights that could otherwise disappear as highlights are mapped into lower dynamic ranges, generally from clipping. Raising Tone Detail Weight keeps more highlight detail intact. In use, it can sharpen highlight detail.
