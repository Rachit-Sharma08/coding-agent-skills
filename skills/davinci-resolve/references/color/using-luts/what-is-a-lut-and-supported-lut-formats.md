# What is a LUT and supported LUT formats

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using luts.
[Chapter index](INDEX.md) / [Next section](lut-browser-and-applying-a-lut-within-a-node.md)
<a id="source-adding-lookup-tables-of-your-own"></a> <a id="source-applying-luts-to-source-clips"></a> <a id="source-custom-lut-paths"></a> <a id="source-lut-controls-in-the-project-settings"></a> <a id="source-lut-paths-for-the-macos-app-store-version-of-davinci-resolve"></a> <a id="source-luts-and-aces"></a> <a id="source-supported-lut-formats"></a> <a id="source-using-luts"></a> <a id="source-using-luts-1"></a> <a id="source-using-the-color-page-lut-browser"></a> <a id="source-what-is-a-lut"></a>

### Using LUTs

Lookup Tables, otherwise called LUTs, rank among the most widespread ways out there to create, trade, and apply image processing operations — serving color management, display calibration, look management, and general-purpose work on an image's color and contrast. Throughout its image processing pipeline, DaVinci Resolve offers solid LUT support.

### What is a LUT?

LUTs amount to nothing more than files, akin to plugins yet far narrower in focus and lacking any user interface, that spell out image processing operations. Those operations get carried out through several different means. The classic approach relies on a 1D table or a 3D "cube" of pre-computed values to run an image color transform. Newer LUT formats such as CLF and DCTL, by contrast, let you process an image with mathematical scripts. Regardless of which type of LUT you reach for, these files load into DaVinci Resolve and apply at various stages of the image processing pipeline to deliver image processing operations for assorted ends. Several well-recognized uses of LUTs exist, but the key point to grasp is that LUTs are merely color transform operations applicable to many tasks, with no single use of a LUT carrying any more or less weight than another. Below are a few common uses for LUTs:

- Though Resolve Color Management (RCM) can optionally take their place, lookup tables (LUTs) have long served to build a starting-point adjustment for footage shot with some logarithmic encoding. Consider DPX log film scans, or digital media carrying the ARRI ALEXA's Log-C encoding, or footage on Sony's S-Log exposure setting, or RED R3D media debayered through the REDFilmLog setting: each one rides a logarithmic exposure curve, shaped to preserve every bit of highlight and shadow detail a digitally encoded image can hold. Even though log-encoded media holds plenty of image data, the picture starts out flat and unusable until graded. You have to tune the exposure and color to "normalize" the media, nudging it toward how it should look, before grading can begin. While doing this by hand is an option, it tends to be quicker to apply a LUT matched to your media type and the exposures you are working with. Failing that, Resolve Color Management can handle it too.
- LUTs see frequent use in onset workflows, where dailies for separate scenes are paired with matching LUTs. These LUTs served to monitor the media as it was recorded, setting a baseline reference for the intended look of each scene, at least where field monitoring is concerned. In more elaborate workflows, LUTs act as a baseline look — set before the shoot and used throughout it — which then becomes the creative starting point for separate scenes once grading kicks off after the shoot.
- LUTs are often deployed as a stylistic ingredient of a grade, or "look," giving users a fast jump-start when they want some kind of creative adjustment. Across the years, companies and individuals have grown an ecosystem of such looks that get circulated and sold in the various LUT formats DaVinci Resolve supports.

Across every one of these cases, LUTs are simply image processing adjustments laid over a clip to affect its color and contrast, much as you would by reaching for any of the contrast or color controls on the Color page.

### Supported LUT Formats

DaVinci Resolve works with both 1D and 3D LUTs and supports LUTs across a range of formats.

- .cube: In the .cube format, DaVinci Resolve handles both 1D and 3D LUTs. You can export 3D LUTs as 17x17x17, 33x33x33, or 65x65x65 cubes carrying 32-bit floating point processing. DaVinci Resolve also reads and uses Shaper LUTs in the .cube format, although these too have to be authored outside of DaVinci Resolve. Bear in mind that while 17-point LUTs are discouraged for grading, they come in handy when exporting LUTs for on-set monitoring, to suit various display, calibration, and signal conversion devices.
- Panasonic VLUT format: This LUT format, built for the Panasonic VariCam camera ecosystem, is one DaVinci Resolve can both read and generate.
- Video Range LUTs: Starting with DaVinci Resolve 17, the ability arrived to import LUTs carrying extra metadata that tags them as processing image data in Video Range instead of Full Range. Guidance on how to format LUTs as Video Range lives in the Developer Documentation reachable from the Help menu. Being able to declare whether a LUT targets Video or Full Range lets LUT processing automatically fall in line with DaVinci Resolve's data range setting pipeline across clip attributes, project settings, and output settings.
- CLF (common LUT format): CLFs rely on an XML format able to wrap a limited set of mathematical transforms alongside traditional lookup-tables for image processing. The academy promotes it as the best-suited LUT format when working with ACES, and because the CLF format brings extra precision and flexibility, LMTs for ACES are recommended to take that form.
- DCTL: DCTL files are in fact color transformation scripts that DaVinci Resolve reads and applies exactly like any other LUT. Where other LUTs are 1D or 3D lookup tables of values approximating image transformations through interpolation, DCTL files instead consist of computer code that transforms images directly via combinations of math functions you devise. On top of that, DCTL files execute natively on your workstation's GPU, so they can run fast.

For more information on DCTL, see Chapter 201, "Creating DCTL LUTs."

What's the Difference Between a LUT and a Shaper LUT? Inside its 32-bit floating point image processing pipeline, DaVinci Resolve is able to import and use LUTs. You can put the .cube format to work either as a plain 33x33x33 3D LUT, or as a shaper LUT — really a technique that pairs two LUTs, a 1D LUT together with a 3D LUT, to tackle signal processing problems that 3D LUTs cannot solve on their own. For the sake of processor efficiency, 3D LUTs come with sensible lower and upper bounds on the data they are built to take. It is widely understood that feeding a 3D LUT values outside the range it is designed for causes the out-of-range data to clip. Because many LUTs assume digital cinema workflows, the practical result is that handing a video signal containing super-white to a 3D LUT built for full-range data (0–1) will clip the signal's super-white portion. Shaper LUTs sidestep this by first running a 1D LUT over video signals carrying out-of-range data, squeezing the signal into a range the 3D LUT will not clamp. The 3D LUT's output carries the reverse transformation, effectively canceling out the 1D LUT's transform while keeping whatever processing the 3D LUT was supposed to apply.

Shaper LUTs also help when handling extremely large data sets, such as OpenEXR files that could in theory span an image data range from –infinity to +infinity. A Shaper LUT lets you remap the incoming data to pack more precision into the 0–1 range, leaving the less important data outside that range.

### LUTs and ACES

The academy that champions the proper use of ACES firmly recommends processing LUTs in the ACES color space. To that end, two project settings let you decide how this gets done:

- ACEScc AP1 Timeline Space: This setting suits either the ACEScc or ACEScct Color Science settings, depending on what you picked in the Color Science pop-up atop the Color Management panel of the Project Settings. It lets you use LUTs authored for ACES workflows that resemble (yet differ from) LUTs you would build and use in a traditional log-encoded workflow. LUTs meant for this setting should span a range of –0.358 to 1.468 so that grading operations clipping an image from 0 to 1 will not wreck the look being applied. The "ACEScc AP1 Timeline Space" setting also works well for workflows where you want to apply conventional LUTs designed for Rec. 709 workflows by way of the ResolveFX "ACES Transform" plugin, which across a chain of three nodes lets you move the image from ACES to 709, apply a Rec. 709-designed LUT, then return the image from 709 back to ACES.
- ACES AP0 Linear: This setting demands that you apply an LMT LUT created specifically for ACES image data. Only turn to this setting when you are working with CLFs built for ACES using a range of –65504 to 65504, as laid out by SMPTE 2065.

### Adding Lookup Tables of Your Own

Within the Color Management panel of the Project settings, the menus carry a set of factory preset LUTs that shipped with DaVinci Resolve, plus any LUTs that DaVinci Resolve has generated or that you have placed into the correct directory for your operating system for your own use. Out of the box, the destinations where LUTs get stored break down per platform as follows.

- On OS X: Library/Application Support/Blackmagic Design/DaVinci Resolve/LUT/
- On Windows: C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\LUT
- On Linux: /home/resolve/LUT

### Custom LUT Paths

Over in the General panel of the DaVinci Resolve System Preferences, a list lets you register several file paths from which LUTs you want to use in DaVinci Resolve get loaded. This serves network volumes at facilities where multiple workstations tap a central pool of LUTs shared among multiple artists. Click the Add button to enter a file path into this table from a dialog. Highlight a location in this list and click Remove to drop that location.

Within the General panel of the System Preferences, a list permits registering several spots that hold the LUTs you intend to draw on inside DaVinci Resolve.

### LUT Paths for the macOS App Store Version of DaVinci Resolve

Should you have downloaded the non-studio version of DaVinci Resolve off the Apple App Store, LUTs land in a different spot so that DaVinci Resolve stays fully self-contained. Here, the Open LUT Folder button — found within the Project Settings under its Lookup Tables panel — opens, when clicked, a Finder window pointed at wherever these LUTs reside. Through that window you can copy in LUTs you want DaVinci Resolve to reach, or delete LUTs you no longer want. If you drop a LUT into one of these directories after DaVinci Resolve is already open, click the Update Lists button to refresh what the pop-up menus contain.

### LUT Controls in the Project Settings

While a whole cluster of LUT controls lives in the Color Management panel of the Project Settings, those are built to apply LUTs, at various points of the image processing pipeline, across the entire Timeline. That is useful when you want a single color and contrast transformation laid over the whole program at once, but it helps less when your aim is per clip variation in which LUT applies. To read up on putting the Lookup Table settings to work, turn to Chapter 4, "System and User Preferences."

### Applying LUTs to Source Clips

You can also hand a clip a LUT by dropping it straight onto the source clip — an option open for whatever clip sits in the Media Pool, or for a clip in the Color page's Thumbnail Timeline. Handy as that is, remember that ColorTrace will not carry source clip LUTs across from one timeline into another, so leaning on source clip LUTs narrows your possible workflows. Most workflows are better served by laying LUTs down within the Node Editor itself, where they become part of every clip's grade.

For one or more selected clips sitting in the Media Pool: right-click any clip among those you selected, then pick a LUT out of the 1D LUT or 3D LUT submenus. For one or more selected clips sitting in the Color page's Thumbnail Timeline: right-click any thumbnail among those you selected, then pick a LUT out of the 1D LUT or 3D LUT submenus. TIP: When your goal is an image transformation that normalizes log-encoded source clips, Resolve Color Management (RCM) is worth weighing too. Given your source media, it may prove the simpler, more hands-off route.

For more information, see Chapter 9, "Data Levels, Color Management, and ACES."

### Using the Color Page LUT Browser

On the Color page, the LUT Browser gives you one central place for browsing and previewing every LUT installed on your workstation. Every LUT shows in the sidebar, grouped by category. Out of the box, every LUT carries a test thumbnail hinting at that LUT's effect, but a live preview of the current clip under a given LUT is also yours by hover scrubbing the pointer across that LUT's thumbnail (more on this further down).
