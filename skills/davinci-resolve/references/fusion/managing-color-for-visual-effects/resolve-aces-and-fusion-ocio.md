# ACES color management in resolve and ocio for ACES color management in Fusion

Version: DaVinci Resolve 20.3 Reference Manual. Context: Managing color for visual effects.
[Chapter index](INDEX.md) / [Previous section](color-management-and-all-compositing-is-math.md)
<a id="source-applying-ocio-luts-in-the-viewer"></a> <a id="source-using-aces-color-management-in-resolve"></a> <a id="source-using-ocio-for-aces-color-management-in-fusion"></a>

### Using ACES Color Management in Resolve

The ACES (Academy Color Encoding Specification) color space is yet another standard for handling color across an entire production. It's built to make start-to-finish, scene-referred color management achievable for digital cinema workflows. Much like DaVinci's RCM, ACES makes it simpler to draw high-precision, wide-latitude image data out of raw camera formats, to safeguard high-quality image data from acquisition all the way through color grading, and to deliver data of high quality for broadcast viewing, for film printing, or for digital cinema encoding. The way ACES operates is by assigning an IDT (Input Device Transform) to each camera and to each acquisition device. That IDT lays out how media from the device gets converted into the ACES color space. At the tail of the pipeline, an ODT (Output Device Transform) does the work of moving image data out of ACES color space and into the gamut of your final output. As with setting up RCM, DaVinci Resolve's color management project settings can be set for ACES, which flows through the Edit, Fusion, and Color pages. NOTE: When you're on Fusion Studio, the OpenColorIO (OCIO) framework handles ACES color management. Setting up ACES color management in DaVinci Resolve happens through the Color Science drop-down menu, found in the Project Settings' Color Management panel.

With ACES switched on, input and output devices are pinned down by the IDT and the ODT.

- Color Science: Through this drop-down menu, you can pick either ACEScct or ACEScc color science. This comes down mostly to personal preference, since the two are largely identical, though the shadows react differently to grading operations. On the Fusion page, images get converted to linear automatically, so whoever handles the grading has more reason to favor one over the other.

ACEScc: Pick ACEScc color science to put a standard Cineon-style log encoding onto the ACES data before DaVinci Resolve processes it. ACEScct: This take on ACEScc tacks on a roll-off at the toe of the image so that color-correction lift operations “feel” closer to how they do with film scans and LogC encoded images.

- ACES Version: Once you've selected one of the ACES color science options, this menu opens up so you can pick which version of ACES to use.
- ACES Input Device Transform: This menu lets you pick which IDT (Input Device Transform) to use for the dominant media format you're working with.
- ACES Output Device Transform: This menu lets you pick an ODT (Output Device Transform) to transform the image data so it matches the deliverable you need.
- Process Node LUTs In: This menu lets you set how LUTs are processed on the Color page; it has no bearing on the Fusion page.
- Disable tone mapping for Fusion conversion: Ticking this box strips any tone mapping out of the ACES color management.

To dig deeper into ACES inside DaVinci Resolve, turn to Chapter 9, “Data Levels, Color Management, and ACES.”

### Using OCIO for ACES Color Management in Fusion

On Fusion Studio, or whenever color management isn't in play in DaVinci Resolve, you have the option of bringing OpenColorIO nodes into Fusion so you can composite inside an ACES color space. Built for visual effects and computer animation work, OpenColorIO (OCIO) is an open-source color management framework. It's compatible with the Academy Color Encoding Specification (ACES). A trio of OCIO nodes, sitting in the Color category of the Effects Library, let you apply OCIO color space transforms in Fusion.

- OCIO CDL Transform node lets you create, save, load, and apply a Color Decision List (CDL) grade.
- OCIO Color Space delivers refined color space conversions that draw on an OCIO config file.
- OCIO File Transform lets you load and apply an assortment of LookUp Tables (LUTs).

Using OCIO to convert MediaIn or Loader nodes to linear gamma relies on the OCIO Color Space node. Dropping the OCIO Color Space node right after a Loader (or a MediaIn in DaVinci Resolve) shows the OCIO Source and Output controls in the Inspector.

To operate within an ACES color managed environment, you can lean on OCIO Color Space nodes.

Inside the Inspector for the OCIO Color Space node, Fusion supplies default Source and Output transforms for standard color spaces. To tap the full OCIO standard, though, you'll have to download and install the OCIO config file. That config file is available from the OCIO website. https://opencolorio.org Clicking the Browse button in the Inspector lets you navigate to the config file you downloaded. From the download, find the ACES 1.0.3 or later folder and pick the file config.ocio.

Whatever fills the Source and Output menus comes from the config.ocio file you download. As for the Source menu, it picks the color profile that applies to your Loader or MediaIn node. With the default raw setting, an untouched image appears, which essentially leaves the clip with no color management at all. Whatever you pick from the menu hinges on the recording profile of your media. The Output menu is set according to your deliverables. While working in Fusion Studio, the Output picked is typically ACEScg, so you work in a scene linear space.

### Applying OCIO LUTs in the Viewer

The viewer also carries OCIO View LUTs for calibrating the viewers. Once the OCIO Color Space View LUT is picked from the LUT menu above the viewer, choosing Edit on that same menu opens a dialog where the OCIO config file can be loaded.

Within Fusion Studio, you'll find the OCIO Color Space View LUT sitting in the Viewer LUT menu.

By default, the View LUT offers the same standard options. Clicking the Browse button, though, lets you load the very config file you loaded into the OCIO Color Space node. After it's loaded, all the expanded OCIO options become available. Having set the OCIO Color Space node to output ACEScg, you'd then turn to the OCIO View LUT, taking a source setting of linear sRGB across to an output of either sRGB or Rec. 709 in the majority of situations.

When you're working with the OCIO Color Space node in the Node Editor, the OCIO Color Space View LUT dialog is what configures the viewer. TIP: When your monitor is calibrated differently, you'll have to pick a LUT that lines up with your calibration. Setting the LUT by way of OCIO: 1 Open the LUT menu, then pick the OCIO Color Space View LUT from it. 2 Off that same menu, choose Edit. 3 Within the View LUT editor that opens, point the source's color space at lin sRGB 4 Point the output space at sRGB or REC 709, assuming a standard computer monitor is what you're viewing on. A normalized image now appears in the viewer, even though every color operation stays on linear images. No matter whether you reach for the OCIO Color Space LUT or a LUT matched to your particular monitor calibration, you're able to store the viewer setup as the default. Saving this OCIO ColorSpace LUT arrangement as the default viewer setup:

- Right-click in the viewer, and then choose Settings > Save Defaults. From here on, for each comp, the viewer comes preconfigured from the saved defaults.
