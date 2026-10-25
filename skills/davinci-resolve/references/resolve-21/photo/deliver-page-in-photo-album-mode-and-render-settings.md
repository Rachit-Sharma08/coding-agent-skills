# Deliver page in photo album mode and render settings

Version: DaVinci Resolve 21 New Features Guide. Context: Photo.
[Chapter index](INDEX.md) / [Previous section](looks-and-adjustments.md) / [Next section](photo-editing-example-and-original-camera-phone-image.md)
<a id="source-file-1"></a> <a id="source-photo-part-3"></a> <a id="source-render-settings"></a> <a id="source-the-deliver-page-in-photo-album-mode"></a>

### The Deliver page in Photo Album mode

To export photos from the Deliver page:

- Select your File Naming, Location and Image Format in the Render Settings.
- Choose whether to send out the Entire Album, or just the Selected Photos drawn from the Album.
- Hit the Add to Render Queue button. Should you wish, tweak any of the export settings, then

press Add to Render Queue again to export multiple output formats.

- In the Render Queue press Render All to start processing your images.

### Render Settings

- File Name: Enter the base name for the rendered photo or photos. Pressing the + icon lets you add common metadata types to the file name, which fill in automatically per photo. By default the exported file takes this name plus a numbered suffix so every shot gets a unique file name.
- Location: The spot on disk where your photos should be written. Hit the Browse button to bring up a file system requestor and pick it.
- Export: Pick either Entire Album to export every photo in the album, or Selected Photos to export only the photos you have selected in the Album at the bottom of the Deliver page.

These settings let you set parameters for the exported photo format. Not every format carries all of these parameters.

- Format: Pick which photo format the export targets. The options on offer are: HEIF, JPEG, PNG and TIFF.
- Bit Depth: Choose the bit depth for the exported photo.
- Include Alpha Channel: When your format supports an alpha channel, tick this box to switch it on and

carry transparency information.

- Size: Choose the method by which you want to size your photo.

Original: With this approach the photo goes out at exactly it’s original dimensions. Width and Height: Here you type a precise width plus a precise height, both in pixels, for the export. Short Side: Here you give a precise pixel figure for the image’s short side (usually its height), and the long side is sized to match the aspect ratio on its own. Long Side: Here you give a precise pixel figure for the image’s long side (usually its length), and the short side is sized to match the aspect ratio on its own. Percentage: Here you set a percentage by which the image shrinks. The figures available go from 25% to 100%. Megapixels: Here you scale the image by a Megapixels figure instead. Enlarge: Tick this box whenever the resolution you are after exceeds the original resolution.

- Resolution: Type the image resolution you want right here, expressed either as Pixels per Inch (ppi) or as Pixels per Centimeter (ppcm).
- Compression: If your format supports image compression, enter your desired values here.
- Include Metadata: Tick this box to carry metadata such as location data, lens values, and the like into the

exported photo.

### File

These settings let you decide how the file naming of the exported photos is handled.

- File Name Uses: Pick either Custom Name to build your own naming structure, or Timeline name to take the timeline’s name plus a numerical suffix instead.
- Custom Name: Type text here to set the custom name; you can also fold in metadata variables that update per photo by first typing “%” and then picking the metadata field from the dropdown list.
- File Suffix: Type text here to tack on as a suffix following the custom name you set above.
- Use X Digits in the File Name: This number governs how many decimal places the file

numbering scheme applies within the file name. To illustrate, picking 3 digits draws on numbers running 1-999, whereas 8 digits draws on numbers running 1-99,999,999.
