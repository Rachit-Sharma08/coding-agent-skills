# Loader node loader import tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Loader node.
[Chapter index](INDEX.md) / [Previous section](loader-node-a-loader-node-used-for-importing-images.md) / [Next section](mediain-node-image-tab.md) / [Loader Node LD](loader-node-a-loader-node-used-for-importing-images.md)
<a id="source-common-controls"></a> <a id="source-format-tab"></a> <a id="source-format-tab-1"></a> <a id="source-loader-import-tab"></a>

### Loader Import tab

Process Mode Reach for this menu to pick the Fields Processing mode that Fusion applies while loading the image. The Has Fields checkbox control inside the Frame Format preferences fixes the default option, plus the default height too. Options on offer take in:

- Full frames
- NTSC fields
- PAL/HD fields
- PAL/HD fields (reversed)
- NTSC fields (reversed).

The two reversed options bring fields in in the reverse order and thus leave the fields spatially swapped in time order and in vertical order alike. Reach for the Swap Field Dominance checkbox (covered below) to swap fields in time alone. Depth The Depth menu serves to pick the color depth applied to processing footage out of this Loader. The default option is Format.

- Format: The color depth follows the color depth that the loaded file format supports. As an example, JPEG files process at 8 bit on their own since the JPEG file format stores no color depths over 8. EXR files load at Float. Should the format's color depth be undetermined, the default depth named inside the Frame Format preferences applies. Formats supporting several color depths get set to the fitting color depth on their own.
- Default: The color depth follows the settings inside the composition's Frame Format Preferences panel.
- Int 8 Bit/Int 16 Bit/Float 16/Float 32: These options fix the color depth used to process the image.

Pixel Aspect This menu serves to fix the image's pixel aspect ratio.

- From File: The loader falls in line with the image aspect spotted inside the saved file. A handful of formats are able to store aspect information. TIFF, JPEG, and OpenEXR stand as examples of image formats that may carry the pixel aspect embedded inside the file's header. Where no aspect ratio information sits stored within the file, the default frame format method applies.
- Default: Whatever pixel aspect ratio information sits stored in the header of the image file gets ignored. The pixel aspect set inside the composition's frame format preferences applies instead.
- Custom: Pick this option to trump the preferences and assign a pixel aspect for the clip by hand. Picking this button makes the X/Y Pixel Aspect control surface.

Custom Pixel Aspect This control is on view solely once Custom has been picked from the Pixel Aspect menu. Key in the X and Y aspect you want, or right-click on the control to bring up a menu of common frame formats together with their aspects.

Import Mode This menu supplies options for stripping pull-up out of an image sequence. Pull-up is a reversible way of combining frames that serves to convert 24 fps footage into 30 fps. It's commonly relied on for broadcasting NTSC versions of films.

- Normal: This lets the image pass without laying on pull-up or pull-down 2:3.
- Pull Up: This strips existing 3:2 pull-down laid on the image sequence, converting from

30 fps to 24 fps 2:3.

- Pull Down: The footage carries pull-down, converting 24 fps footage to 30 fps by spawning

five frames for every four it starts with. Where a Loader sits at Pull Down, its process mode ought always to stay Full Frames. First Frame This menu turns up whenever the Import Mode sits at either Pull Up or Pull Down. Which frame of the 3:2 sequence becomes the loaded clip's first frame is what it fixes. Detect Pull-Down Sequence This button serves to spot and assign the footage's pull-up sequence on its own. It functions solely once Pull-Up or Pull-Down has first been picked from the Import Mode menu. Should it manage to spot the order, the First Frame control sets itself to the right value on its own. Make Alpha Solid Switched on, the clip's original Alpha channel gets wiped and set to solid white (fully opaque). Invert Alpha Switched on, the clip's original Alpha channel gets inverted. This may also pair with Make Alpha Solid to set the Alpha to pure black (fully transparent). Post-Multiply by Alpha Switching this option on makes each pixel's color value get multiplied by the Alpha channel for that pixel. This option can serve to convert subtractive (non-premultiplied) images into additive (premultiplied) images. Swap Field Dominance Switched on, the image's field order (dominance) gets swapped, so the order in time the fields show up gets reversed. Unlike the Process Mode control, this happens without spatially swapping the scanlines inside the image Color Space Type This menu serves to set the footage's Color Space so as to help reach a linear color space workflow. Unlike the Gamut tool, this carries out no actual color space conversion, but rather folds the source color space data into the metadata when that metadata isn't there yet. That metadata can then be drawn on downstream by a Gamut tool carrying the From Image option, or inside a Saver where explicit output spaces have been defined.

- Auto: Carries along whatever metadata might sit in the incoming image.
- Space: Lets the user set the color space according to the recording device used to capture

content or to the software settings used while the content was rendered inside another application.

Curve Type This menu serves to fix the footage's gamma curve. After the Gamma Curve Type has been set, you can opt to strip the curve so as to help reach a linear workflow.

- Auto: Carries along whatever metadata might sit in the incoming image.
- Space: Lets the user set the gamma curve according to the recording device used to capture

content or to the software settings used while the content was rendered inside another application.

- Log: Brings up the Log/Lin settings, akin to the Cineon Log node.

To learn more about the Log settings, refer to Chapter 99, “Film Nodes,” inside the DaVinci Resolve Reference Manual and Chapter 39, within the Fusion Reference Manual. Remove Curve Hinging on the chosen Curve Type or on the Gamma Space turned up under Auto mode, the matching Gamma Curve gets stripped from, or a log-lin conversion gets run on, the material, in effect converting it into a linear output space.

### Format Tab

The Format tab holds file format-specific controls that shift on the fly according to the chosen Loader and the file it points to. Some formats carry a lone control or none whatsoever. Others, such as Camera RAW formats, carry RAW-specific debayering controls. A partial format list appears below for reference.

### Format tab

- OpenEXR: EXR delivers a compact, flexible format for supporting high dynamic range images (float). The format additionally backs an assortment of extra channels and metadata.The Format tab for OpenEXR files supplies a means of mapping any non-RGBA channels onto the channels supported natively inside Fusion. By way of the Format tab, you can key the name of a channel held inside the OpenEXR file into any edit box that sits beside its Fusion channel name. To dump out the channels' names, a command line utility is available at https://www.openexr.com.
- QuickTime: QuickTime files may potentially hold several tracks. Reach for the format options to pick one of the tracks.
- Cinema DNG: CinemaDNG is an open format able to carry high-resolution raw image data with a wide dynamic range. It ranked among the formats Blackmagic Design cameras recorded before they shifted over to the BRAW format.
- Photoshop PSD Format: Fusion is able to load any one of the individual layers held inside the PSD file, or the finished image carrying all layers. Transformation and adjustment layers aren't supported. To load every layer in a PSD file with fitting blend modes, reach for File > Import > PSD.

### Common Controls

Settings Tab The Settings tab controls are shared across both Loader and Saver nodes, so you'll find their descriptions in the “The Common Controls” section toward the end of this chapter.
