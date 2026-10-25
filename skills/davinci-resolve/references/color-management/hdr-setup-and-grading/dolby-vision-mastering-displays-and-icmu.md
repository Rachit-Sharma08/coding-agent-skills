# Choosing mastering displays for dolby vision and the dolby vision internal content mapping unit icmu

Version: DaVinci Resolve 20.3 Reference Manual. Context: HDR setup and grading.
[Chapter index](INDEX.md) / [Previous section](dolby-cinema-and-sdr-peak-luminance.md) / [Next section](hdmi-tunneling-using-decklink-8k-pro-g2.md)
<a id="source-choosing-mastering-displays-for-dolby-vision"></a> <a id="source-enabling-simultaneous-monitoring"></a> <a id="source-necessary-hardware"></a> <a id="source-simultaneous-master-and-target-display-output-for-dolby-vision"></a> <a id="source-using-the-dolby-vision-internal-content-mapping-unit-icmu"></a>

### Choosing Mastering Displays for Dolby Vision

Performing HDR grading requires an appropriate HDR display. In principle, any monitor that supports SMPTE ST.2084 (aka PQ) will do the job. Fortunately, an expanding lineup of professional displays from Sony, Flanders Scientific, TV-Logic, Canon, and Eizo is well suited to HDR grading suites. EBU Tech 3320 lays out the requirements for a Grade 1 HDR mastering monitor. Dolby suggests these minimum specifications for HDR monitors:

- A minimum Peak Luminance of 1000 nits
- A 200,000:1 contrast ratio
- Minimum black at 0.005 nits
- Capable of at least 99% of P3 gamut To learn more about Dolby’s recommended practices for color grading Dolby Vision, head to: https://www.dolby.com/us/en/technologies/dolby-vision/dolby-vision-for-creativeprofessionals.html.

### Using the Dolby Vision Internal Content Mapping Unit (iCMU)

DaVinci Resolve includes a GPU-accelerated “internal” software implementation of the Dolby Vision CMU (Content Mapping Unit), letting you preview Dolby Vision mapping directly inside DaVinci Resolve. You enable and configure iCMU support in the Color Management panel of the Project Settings by switching on the Enable Dolby Vision checkbox. It’s available only in DaVinci Resolve Studio.

Setup and Workflows | HDR Viewers HDR Setup and Grading

Dolby Vision settings in the Color Management panel of the Project Settings Beyond that, the Dolby Vision group of settings surfaces menus for picking which version of Dolby Vision to run, the analysis type and the Master Display kind you’re working with, and whether to use an eCMU (provided you have that option). There are also options to turn on HDMI tunneling (covered below). Lastly, enabling Dolby Vision likewise activates the Dolby Vision palette and controls on the Color page, which this chapter explains more fully later on. Mastering with Dolby Vision in DaVinci Resolve through the built-in iCMU still demands a more particular hardware configuration than a typical grading and finishing workstation, made up of the equipment below:

- Your DaVinci Resolve grading workstation fitted with a DeckLink 8K Pro or DeckLink 4K Extreme

12G video interface.

- A mastering display that can output HDR nit levels appropriate to the deliverable you must

produce

### Simultaneous Master and Target Display Output for Dolby Vision

While mastering HDR and trimming versions for more constrained displays, being able to judge your HDR grade alongside your SDR trim pass is enormously helpful. You can send out the Master Display output and the Target Display output at the same time whenever you grade with either Dolby Vision or HDR10+ turned on.

### Necessary Hardware

To work in this manner, you must have the following equipment:

- Your DaVinci Resolve grading workstation has to output through a DeckLink 8K Pro by way of the attached HDMI card. That carries the Dolby Vision metadata onward to the SDR display, letting you see the SDR derived from the HDR grade.
- Your Mastering Display has to handle HDR nit levels appropriate to the deliverable you must produce.
- A display you can configure to output calibrated SDR, most likely using the BT.709 gamut

Setup and Workflows | HDR Viewers HDR Setup and Grading

### Enabling Simultaneous Monitoring

As you wire up your display hardware, attach the HDR Master Display to output A and the Target Display to output B of whatever BMD video output device you’re using. After that, within the Master Settings of the Project Settings, tick the “Use dual outputs on SDI” checkbox. From there, provided every connection is mutually compatible, you should get an HDR image sent to your HDR display and a trimmed image sent to your SDR display.
