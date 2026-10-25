# Enabling roi controls and while the roi is active

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using viewers.
[Chapter index](INDEX.md) / [Previous section](region-of-interest-roi.md) / [Next section](fuse-luts-and-viewer-luts.md)
<a id="source-buffer-luts"></a> <a id="source-enabling-roi-controls"></a> <a id="source-fusion-view-lut"></a> <a id="source-gamut-view-lut"></a> <a id="source-how-lookup-tables-work-in-fusion"></a> <a id="source-image-luts"></a> <a id="source-log-lin-view-lut"></a> <a id="source-lut-presets"></a> <a id="source-macro-luts"></a> <a id="source-managing-viewer-lookup-tables-luts"></a> <a id="source-types-of-viewer-luts"></a> <a id="source-while-the-roi-is-active"></a>

### Enabling RoI Controls

Switching on the RoI controls lets you confine rendering to a small region of the picture and markedly boost performance whenever you're focused on just a small portion of a high-resolution or intricate composition. As an example, when you're applying paint to patch a few holes in a matte across the floor of a composition holding many, many high-resolution layers, 3D, and Lighting operations, the RoI controls let you single out the patch of floor you're tackling, which speeds up caching of that part of the composition considerably. So as to switch on the RoI controls, do one of the following:

- Click the RoI button in the 2D Viewer toolbar.
- In a viewer, right-click and pick Region > Show Region off the contextual menu. Once RoI is switched on and Show Region has been picked from the menu, a rectangular RoI control shows up within the viewer. Should this mark the first occasion RoI has been switched on, it gets sized to the whole width and height of the picture. If not, the RoI's most recent position for that view applies. That said, should you wish to assign the RoI to a custom area inside the frame, you can do one of the following.

To adjust the RoI controls, do one of the following:

- Drag whichever edge of the RoI rectangle to shift one side of the RoI.
- Drag a corner so the RoI rectangle is resized starting from that corner.
- Drag the little circle sitting at the upper-left corner of the RoI rectangle to reposition the RoI while leaving its dimensions alone. Now and then it's quicker to just draw a rectangle wherever you'd like the RoI to land.

To quickly draw the RoI at the desired size: 1 Pick Set out of the viewer menu beside the RoI button, or right-click somewhere inside the viewer and choose Region > Set Region. 2 Once the pointer becomes an RoI drawing cursor, drag inside the viewer to lay out a RoI rectangle. As another route, an Auto command sizes the RoI to cover whatever pixels are on view at the present zoom/pan level inside the viewer. That lets you swiftly cap the RoI to whichever part of the composition you've zoomed in on. To automatically draw the RoI:

- Choose Auto from the viewer menu next to the RoI button.
- Right-click anywhere within the viewer and choose Region > Auto Region.
- Once you've no further need for the RoI, you can reset it.

So as to restore the RoI back to the whole width and height of the present picture, do one of the following:

- Choose Reset from the viewer menu next to the RoI button.
- Somewhere inside the viewer, right-click and pick Region > Reset Region, whether off the contextual menu or via the toolbar button menu.
- Disable the ROI control, which will also reset it.

### While the RoI Is Active

The RoI serves solely for previewing your composition as you work, not for output out of Fusion. As long as the RoI stays active, Fusion only asks for rendering of the pixels within the region whenever it puts an image up in that viewer. Flipbook Previews you make inside that viewer likewise honor the present RoI. MediaOut and Saver nodes invariably draw on the whole image dimensions while writing the image to disk, paying no mind to whatever RoI you've assigned within the viewers. The RoI lifts not only rendering speed and memory use but can additionally trim file I/O, given that Loaders and MediaIn nodes pull in pixels only from inside the RoI when one has been set. Doing so does demand that the file format in use permits direct pixel access. Cineon, DPX, and numerous uncompressed file formats accommodate this capability, along with OpenEXR and TIFF in restricted situations. Do keep in mind that shifts to the viewed image size or color depth will make the pixels beyond the RoI reset to the picture's canvas color. The same occurs while toggling in and out of Proxy mode, and likewise over Proxy mode switching whenever Auto Proxy is switched on. So long as the image size holds steady, so do the most recently rendered pixel values beyond the RoI. That can prove handy when contrasting changes made within the RoI against an earlier node state. TIP: Right-clicking in a viewer and selecting Options > Show Controls to bring up onscreen controls will trump the RoI, compelling renders of pixels across the whole image.

### Managing Viewer Lookup Tables (LUTs)

Lookup Tables, also called LUTs, serve to help line up a viewer's look with where it will eventually be output. In essence they're image-processing operations touching only the image previewed inside the viewer, leaving the image data itself untouched. LUTs can work out color transformations in two fundamental ways: the first being a plain 1D LUT, and the second a more advanced 3D LUT.

- A LUT in its plainest form is a 1D LUT. Handling one color channel at a time, it can produce broad tonality shifts though not highly precise color shifts.
- A 3D LUT examines every conceivable color value (red, green, and blue) on its own. A 3D LUT permits sweeping global shifts plus highly precise color shifts to land on images very rapidly.

### How Lookup Tables Work in Fusion

A Lookup Table (LUT) amounts to a table of values employed to transform an image's color and luminance. Whereas a 1D LUT relies on a two-column table pairing input color with output color, a 3D LUT works more like a matrix. A LUT chiefly serves to compensate for differences in the monitor or in the image's source color space. You may opt to apply a LUT across all the viewers, or apply distinct LUTs to each viewer.

### Image LUTs

Image LUTs are applicable per viewer. You can indeed even apply separate Image LUTs to the A and B buffers belonging to one viewer. Such LUTs apply only to 2D images, never to 3D scenes. Routinely, Image LUTs serve to travel from one scene-referred color space across to another. For instance, when you're handling log-encoded media yet want a look at how the image will appear in the final color space, you can pick a LUT that transforms the image as a preview.

### Buffer LUTs

The Buffer LUT applies across the viewers no matter their contents, 3D scenes, 3D materials, and subview types included. No more than one Buffer LUT may apply. When a 2D image is shown carrying an Image LUT, the Buffer LUT then applies atop the result of that image LUT. Commonly, Buffer LUTs serve to emulate a different output color space particular to the display you're on—say, getting a DCI-P3 projector to render the image the way it would appear on an sRGB monitor. To use a Buffer LUT: 1 Turn off the LUT button sitting above the viewer. 2 Inside the viewer, right-click and pick Global Options > Buffer LUT > Enable. 3 Once more inside the viewer, right-click and pick Global Options > Buffer LUT > Type of LUT you want to apply. While handling nonlinear files out of many of today's digital cinema cameras, a current workflow would convert it all to linear at the head of the node tree, then build your composite, and then apply an Image LUT or Buffer LUT matching whatever color space you intend it to sit in for either grading on the Color page or for final output. In more involved production pipelines, though, you might have to apply several LUTs one after another.

### Types of Viewer LUTs

Beyond the industry standard 1D and 3D LUTs, further kinds of LUTs are accommodated, among them scriptbased Fuse node LUTs, OCIO files, and macros put together from standard nodes. As a rule, LUT processing runs on the graphics card's GPU in real time, though how macrobased LUTs perform hinges on the nodes inside them.

### Fusion View LUT

Serving as the default, the Fusion View LUT is a heavily used LUT type. It supplies an RGBA curve usable for assigning IN/OUT value pairs. This control matches the one offered by the Color Curve node. Because the View LUT exists to deliver a fixed correction for the monitor or the file's color space, however, its splines can't be animated.

### Log-Lin View LUT

The Log-Lin LUT turns logarithmic data into linear, and the reverse as well. That can come in especially handy alongside supplied LUT files that anticipate logarithmic data. It resembles the Cineon Log node.

### Gamut View LUT

The Gamut LUT turns a source color space into an output color space, offering choices for handling gamma settings, alpha channels, and premultiplication. The Gamut LUT is a heavily used LUT type for correcting the viewer while you work with Linear Gamma in the Node editor.

### Macro LUTs

Any macro node may serve as a viewer LUT too, merely by storing the macro's .setting file into the right Fusion directory. Within DaVinci Resolve, the storage spots for LUTs are these. Under macOS: Macintosh HD/Users/username/Library/Application Support/Blackmagic Design/ Fusion/LUTs/ Under a Windows host: C:\Program Files\Blackmagic Design\Fusion\LUTs Under Linux: home/username/.local/share/DaVinciResolve/Fusion/LUTs Over in Fusion Studio, the storage spots instead become these. Under macOS: Macintosh HD/Users/username/Library/Application Support/Blackmagic Design/ Fusion/LUTs/ Under a Windows host: C:\Users\username\AppData\Roaming\Blackmagic Design\Fusion\LUTs Under Linux: home/username/.fusion/BlackmagicDesign/Fusion/LUTs So that this works, the macro is required to carry one image input plus one image output. Whatever controls the macro surfaces will be on hand once the Edit option has been chosen for the LUT. For deeper detail on building macros, turn to Chapter 68, “Node Groups, Macros, and Fusion Templates,” over in the DaVinci Resolve Reference Manual, or else Chapter 6 within the Fusion Reference Manual.

### LUT Presets

Every LUT on hand to DaVinci Resolve is reachable from the Fusion page as well, which takes in custom LUTs you've added along with preset LUTs that ship with DaVinci Resolve, like the highly handy VFX IO category carrying a broad assortment of miscellaneous to Linear and Linear to miscellaneous transforms. The whole set of these LUTs turns up by category within the viewer LUT menu.
