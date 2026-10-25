# Media 326 and hardware requirements for working in stereo 3D

Version: DaVinci Resolve 20.3 Reference Manual. Context: Stereoscopic workflows.
[Chapter index](INDEX.md) / [Next section](stereo-clip-generation-and-optimized-media.md)
<a id="source-creating-stereo-3d-clips-from-separate-files"></a> <a id="source-hardware-requirements-for-working-in-stereo-3d"></a> <a id="source-media-326"></a> <a id="source-setting-up-to-display-stereo-3d-via-hdmi"></a> <a id="source-setting-up-to-display-stereo-3d-via-sdi"></a> <a id="source-step-1--import-and-organize-your-media"></a> <a id="source-stereoscopic-workflows"></a> <a id="source-stereoscopic-workflows-part-1"></a> <a id="source-supported-stereo-3d-media"></a> <a id="source-using-dual-sets-of-media-in-any-supported-format"></a> <a id="source-using-stereoscopic-cineform-media"></a> <a id="source-using-stereoscopic-mxf-media"></a> <a id="source-using-stereoscopic-openexr-media"></a>

### Stereoscopic Workflows

A broad range of stereoscopic workflows is solidly supported in DaVinci Resolve. With the tools built into the Studio version of DaVinci Resolve, you can cut with stereoscopic clips, grade the finished program, tweak each clip’s stereo‑specific properties — convergence and floating windows among them — and master a stereoscopic output, every bit of it inside DaVinci Resolve.

### MEDIA 326

Building a stereo 3D project takes several steps and goes much more smoothly with careful media organization. The pages ahead explain how to prepare for stereoscopic projects, how to bring them in, and how to send stereoscopic media back out. To begin, stereoscopic clip pairs — that is, the separate left- and right-eye media files — get imported into the Media Pool, arranged, and then joined with the “Stereo 3D Sync” command to produce a fresh set of linked stereo clips. From there, those stereo clips may be edited or conformed against imported project data within a single Timeline. In the Color page, DaVinci Resolve lets you handle left- and right-eye grades and sizing through the controls in the Thumbnail timeline’s shortcut menu and in the Stereo 3D palette. Working with stereoscopic CineForm media — which holds muxed left-eye and right-eye image data that DaVinci Resolve can decode — still requires you to follow this same process, except that you’ll rely on duplicate clips to fill the Left and Right folders with matching sets.

### Hardware Requirements for Working in Stereo 3D

On Mac systems running DaVinci Resolve, twin 4:2:2 Y’CbCr stereoscopic video streams come out over SDI from a compatible Blackmagic Design video interface. Depending on what your stereo 3D-capable display accepts, you can pick either Side-by-Side or Line Mesh output to send to it. As an alternative, head into the Project Settings, open its Master Settings panel, find the Video Monitoring group there, and tick “Enable Dual SDI 3D Monitoring”; that makes your compatible Blackmagic Design video interface deliver full resolution 4:2:2 Y’CbCr per eye to compatible displays. As you build a 3D-capable DaVinci Resolve workstation, bear in mind that a 3D project’s paired video streams place heavier loads on disk bandwidth, on media decoding handled by your workstation’s CPU, and on effects processing handled by the GPU cards your workstation has available.

### Setting Up to Display Stereo 3D via SDI

Every DaVinci Resolve system is able to send out a side-by-side frame-compatible signal viewable on a stereo 3D-capable display over a single SDI connection, driven by a DeckLink HD Extreme card or something better. To monitor at higher quality, you can route two SDI signals so the left-eye and right-eye images each go out separately at full resolution, using one of these Blackmagic Design video interfaces:

- DeckLink HD Extreme 3D+
- DeckLink 4K Extreme
- DeckLink 4K Extreme 12G
- DeckLink 8K Pro
- UltraStudio 4K
- UltraStudio 4K Extreme
- UltraStudio 4K Extreme 3

On very old legacy systems, this is handled through NVIDIA dual SDI monitoring outputs.

NOTE: When your stereo display can’t multiplex the two arriving SDI signals on its own, an external device can do the job, combining both SDI signals into one compatible stereo 3G signal. Ask your display manufacturer beforehand whether you’ll need that. The procedures that follow lay out two separate ways to configure stereo 3D monitoring. Monitoring via dual SDI to dual SDI: 1 Within the Project Settings, open the Master Settings panel, and then carry out these steps:

- Confirm that the Use 4:4:4 SDI checkbox is left unchecked.
- Switch on the “Use dual outputs on SDI” checkbox. 2 Over in the Color page, open the Stereo 3D palette, then carry out these steps:
- Set Vision to Stereo.
- Set the Out pop-up menu to None.

NOTE: While “Enable dual SDI 3D monitoring” is active, the grading monitor won’t show split-screen wipes or cursors, and image resizing won’t be visible there either.

### Setting Up to Display Stereo 3D via HDMI

When your stereo-capable display offers only an HDMI input, you’ll have to send stereo 3D signals from the HDMI output of a compatible Blackmagic Design video interface equipped with HDMI 1.4 or newer; consult the documentation that came with your video interface for further details.

### Supported Stereo 3D Media

If you’re bringing stereo 3D media in from other applications, two media types will work with DaVinci Resolve stereoscopic workflows.

### Using Dual Sets of Media in Any Supported Format

As originally captured, the media for stereo 3D workflows lives in two directories — one holding the left-eye media and the other the right-eye media. To get the most automated workflow you can, that media has to be kept tightly organized. Every left-eye and right-eye media file pair across both directories ought to carry matching timecode plus reel numbers that plainly mark which shots are left-eye and which are right-eye. Organized that way, it becomes fairly straightforward for DaVinci Resolve to turn each matching clip pair into the stereo 3D clips you’ll need to work with in DaVinci Resolve. A later section walks through this process in detail.

### Using Stereoscopic OpenEXR Media

For professional cinema and specialty workflows, DaVinci Resolve supports stereo OpenEXR files. A stereo OpenEXR clip keeps each eye’s media as a separate part, so one OpenEXR file can put out either a lone image or stereo 3D images whenever it’s opened in an application that handles it, DaVinci Resolve included. That lets you cut stereo OpenEXR media, grade it, and apply every stereoscopic adjustment the Stereo palette of the Color page offers. Bring stereo OpenEXR clips into the Media Pool and they’ll initially look like ordinary non-stereo clips outputting a single image. Even so, turning them into stereo 3D clips is simple via the steps below. To make stereo OpenEXR clips usable as stereo clips: 1 Bring the OpenEXR media into the Media Pool the same way you’d handle any clip. 2 Highlight one or more OpenEXR clips, right-click them, and from the contextual menu pick “Convert to Stereo.” From then on those clips carry a stereo 3D badge marking them as stereo.

### Using Stereoscopic CineForm Media

CineForm stereo QuickTime files are likewise supported by DaVinci Resolve. A CineForm clip encodes both eyes’ media and muxes (multiplexes) them together such that a CineForm file can hand back either a single frame of image data, when opened in an application without stereoscopic capability, or stereo 3D media, when opened in one that has it — DaVinci Resolve being an example. So you’re able to edit CineForm media in nearly any NLE, export the project through whatever workflow suits you, and finish with a stereoscopic project that DaVinci Resolve can grade. CineForm files can be produced in two ways. The first uses a camera or recorder that takes two synchronized video signals and builds a single set of CineForm media. The second runs dual sets of stereo 3D assets back through the CineForm conversion tools bundled with GoPro CineForm Studio to reprocess them into the CineForm format. As a codec, CineForm encodes full-frame image data with wavelet compression, at any resolution, up to 12-bits, choosing among RGB, Y’CbCr, or RAW color spaces. DaVinci Resolve handles CineForm inside a QuickTime wrapper in any supported color space, giving access to the two image-data streams it carries. When you reach the point of outputting your program, remember that although DaVinci Resolve can read CineForm files, CineForm files won’t render out of DaVinci Resolve unless you’ve bought a GoPro encoding license for OS X or Windows. On top of that, DaVinci Resolve is unable to render Stereoscopic CineForm files. Import stereo CineForm clips into the Media Pool and at first they’ll seem like normal non-stereo clips outputting a single image. They can, however, be converted into stereo 3D clips quite easily with the steps below. To make stereo CineForm clips usable as stereo clips: 1 Drop the CineForm media into the Media Pool exactly as you’d treat any clip. 2 Select the CineForm media slated for conversion, right-click it, and from the contextual menu pick “Convert to Stereo.” Those clips will then show a stereo 3D badge indicating they’re stereo.

### Using Stereoscopic MXF Media

To serve professional cinema and specialty workflows, DaVinci Resolve also supports stereo MXF files. A stereoscopic MXF clip stores each eye’s media as a separate part, letting one MXF file return either a single image or stereo 3D images when opened in an application that handles it, such as DaVinci Resolve. As a result you can cut stereo MXF media, grade it, and apply all the stereoscopic adjustments the Stereo palette of the Color page provides. Once stereo MXF clips land in the Media Pool, they’ll first look like plain non-stereo clips outputting a single image. They’re readily converted into stereo 3D clips, though, with this procedure: To make stereo MXF clips usable as stereo clips: 1 Load the MXF media into the Media Pool the same way you’d handle any clip. 2 Highlight one or more MXF clips, right-click them, and from the contextual menu pick “Clip Attributes.” 3 Inside Clip Attributes, choose the correct stereoscopic encoding mode — either side by side or over/under — from the Stereoscopic Mode dropdown. With multiple clips highlighted, remember to enable the checkbox sitting to the left of the Stereoscopic Mode dropdown so every selected clip takes the mode.

### Creating Stereo 3D Clips From Separate Files

When your stereo media was shot or generated as separate left- and right‑eye files, you’ll have to combine each matching clip pair into the stereo 3D clips DaVinci Resolve needs you to work with. That takes two steps.

### Step 1 – Import and Organize Your Media

Bring every left-eye and right-eye media file into its own bin. 1 Open the Media page and make three Media Pool bins called “Left,” “Right,” and “Stereo Clips.” The precise names don’t matter; how the media is organized does. 2 Place every left-eye file in the “Left” bin while every right-eye file goes in the “Right” bin. For stereoscopic Cineform media you must still build the same arrangement, which means putting a duplicate of each clip into each of the “Left” and “Right” bins.
