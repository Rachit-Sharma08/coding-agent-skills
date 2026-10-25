# Hdr10 monitoring and grading

Version: DaVinci Resolve 20.3 Reference Manual. Context: HDR setup and grading.
[Chapter index](INDEX.md) / [Previous section](delivering-dolby-vision-and-rendering-a-dolby-vision-master.md) / [Next section](hdr-vivid-st2084-monitoring-and-grading.md)
<a id="source-connecting-to-hdr-capable-displays-using-hdmi-20a"></a> <a id="source-delivering-hdr10"></a> <a id="source-enabling-simultaneous-monitoring"></a> <a id="source-hdr-vivid"></a> <a id="source-hdr10"></a> <a id="source-hdr10-auto-analysis-commands"></a> <a id="source-hdr10-grading-workflow"></a> <a id="source-monitoring-and-grading-to-st2084-for-hdr10"></a> <a id="source-monitoring-and-grading-to-st2084-in-davinci-resolve"></a> <a id="source-necessary-hardware"></a> <a id="source-rendering-an-hdr10-master"></a> <a id="source-simultaneous-master-and-target-display-output-for-hdr10"></a>

### Monitoring and Grading to ST.2084 in DaVinci Resolve

To monitor an ST.2084 image you need nothing more than a ST.2084-compatible HDR display wired into whichever device drives your signal — DeckLink 8K, DeckLink 4K Extreme 12G, or UltraStudio 4K Extreme. Configuring Resolve Color Management to grade for ST.2084 mirrors the configuration for Dolby Vision. The video scopes get watched the same way and a master is output the same way too, since both standards lean on the identical PQ curve. TIP: When monitoring through the built-in video scopes in DaVInci Resolve, switch on “HDR (ST.2084/HLG)” within the Waveform Scale Style settings of the Scopes option menu to swap the scopes’ 10-bit scale for one keyed to nit values (cd/m2).

### Connecting to HDR-Capable Displays using HDMI 2.0a

With a DeckLink 4K Extreme 12G or an UltraStudio 4K Extreme video interface on hand, DaVinci Resolve 12.5 and later can emit the metadata that display devices need to render HDR video signals correctly over HDMI 2.0a — just tick the “Enable HDR metadata over HDMI” checkbox inside the Master Settings panel of the Project Settings.

Found in the Project Settings’ Master Settings panel, the Enable HDR metadata over HDMI option opens the door to HDR over HDMI 2.0a Once it’s on, a control over in the Project Settings’ Color Management panel — “HDR mastering is for X” — lets you state the output in nits to embed as metadata within the outgoing HDMI stream, so the display you’re wiring to reads it correctly. The figure you enter ought to line up with what your display anticipates.

By way of the “HDR mastering is for” setting you embed metadata for HDR sent out over HDMI 2.0a

Setup and Workflows | HDR Viewers HDR Setup and Grading

### HDR10+™

Samsung’s new HDR10+ HDR format is supported in DaVinci Resolve. Bear in mind the support remains a work in progress, the standard itself being new. Once active, an HDR10+ palette surfaces the trimming-analysis results that drive an automatic HDR-to-SDR downconversion, minting metadata that dictates how HDR-strength highlights read across a range of supported televisions and displays. You switch it on and configure it via the Enable HDR10+ checkbox in the Project Settings’ Color Management panel. Flipping HDR10+ on brings the HDR 10+ palette to life on the Color page.

HDR 10+ settings in the Color Management panel of the Project Settings

### Monitoring and Grading to ST.2084 for HDR10+

Grading a program for HDR10+ output means monitoring an ST.2084 image, and that takes only a ST.2084-compatible HDR display hooked into your output device — be it a DeckLink 8K, DeckLink 4K Extreme 12G, or UltraStudio 4K Extreme. Preparing Resolve Color Management to grade for ST.2084 plays out just as it would for Dolby Vision or plain HDR10. Likewise the video scopes are read the same and a master is output the same, all three standards resting on the one PQ curve. TIP: Should you monitor via the built-in video scopes in DaVinci Resolve, enabling “HDR (ST.2084/HLG)” under the Waveform Scale Style settings in the Scopes option menu trades the scopes’ 10-bit scale for one founded on nit values (cd/m2).

### HDR10+ Grading Workflow

The HDR10+ workflow runs on the premise that you first grade the HDR version of every clip in your program, then let the automatic analysis spin up a metadata-driven, downconverted tone mapped take on each shot. With the HDR10+ trim pass finished, you hand off the rendered HDR output together with HDR10+ JSON metadata files so a facility can perform the final mastering.

### Simultaneous Master and Target Display Output for HDR10+

As you master HDR and trim versions aimed at more constrained displays, being able to weigh your HDR grade against the tone mapped trim pass side by side is enormously helpful. From DaVinci Resolve 15 onward, the Master Display output and the Target Display output can be sent out at the same time whenever you grade with either Dolby Vision or HDR10+ turned on.

Setup and Workflows | HDR Viewers HDR Setup and Grading

### Necessary Hardware

Operating this way requires the following gear on hand:

- A DaVinci Resolve grading workstation whose output runs through one of these video interfaces — DeckLink 8K, DeckLink 4K Extreme 12G, UltraStudio 4K Extreme — or anything stronger.
- A Mastering Display reaching the HDR nit levels that your intended deliverable calls for.
- An HDR target display you can dial to the right tone mapped output.

### Enabling Simultaneous Monitoring

As you wire up your display hardware, route the HDR Master Display into output A and the Target Display into output B of whatever BMD video output device is in play. Then enable the “Use dual outputs on SDI” checkbox under the Master Settings of the Project Settings. From here, provided all your connections agree with one another, an HDR image should reach your HDR display while a trimmed image reaches your SDR display.

### HDR10+ Auto Analysis Commands

Once an HDR version of every clip in your program is graded, a batch of HDR10+ specific commands lets you auto-analyze each clip and mint custom HDR to SDR downconversion metadata, handing you a launch point for the SDR trim pass ahead. You’ll find these commands in the Color > HDR10+ submenu:

- Analyze All Shots: Runs an automatic analysis on every Timeline clip and banks each result on its own.
- Analyze Selected Shot(s): Confines the analysis to the shots you’ve selected in the Timeline.
- Analyze Selected and Blend: Looks at several selected shots and averages their result, which is

then written to every one of those clips. A time-saver when the clips you’re analyzing share identical content.

- Analyze Current Frame: A quick path for clips where one frame stands in

for the whole shot.

### Delivering HDR10+

With the HDR grade complete and the SDR downconversion trimmed, your program must be output the right way on the Deliver page.

### Rendering an HDR10+ Master

For an HDR10+ master once grading is done, verify the Output Color Space in the Project Settings’ Color Management panel rests on the proper HDR ST.2084 setting for your target peak output (anything over it clips). After that, build your render around the top-quality Format/Codec pairing that suits whoever handles the final mastering. The HDR10+ analysis plus the manual trim metadata you produced while trimming is stored per clip across a run of JSON sidecar files; export them by right-clicking the timeline in the Media Pool and selecting Timelines > Export > HDR10+JSON. Those two file sets then travel to a facility able to build an HDR10+ Mezzanine File (something DaVinci Resolve cannot do). NOTE: The HDR10+ mastering workflow remains a work in progress, and more information will follow as it surfaces.

Setup and Workflows | HDR Viewers HDR Setup and Grading

### HDR Vivid

HDR Vivid is the HDR video technology standard put out by the UHD World Association (UWA). Mastering to this format guarantees broad compatibility across HDR televisions, phones, computers, and other devices that conform to the standard.

HDR Vivid settings in the Color Management panel of the Project Settings
