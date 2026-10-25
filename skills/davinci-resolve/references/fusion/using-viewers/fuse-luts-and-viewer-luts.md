# Fuse luts and viewer luts

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using viewers.
[Chapter index](INDEX.md) / [Previous section](enabling-roi-controls-and-while-the-roi-is-active.md) / [Next section](viewer-settings-and-lut-curves.md)
<a id="source-applying-multiple-luts"></a> <a id="source-checker-underlay-dithering"></a> <a id="source-editing-the-fusion-view-lookup-table"></a> <a id="source-editing-the-log-lin-view-lut"></a> <a id="source-editing-viewer-luts"></a> <a id="source-fuse-luts"></a> <a id="source-image-luts-1"></a> <a id="source-image-output"></a> <a id="source-lut-processing-order"></a> <a id="source-lut-settings"></a> <a id="source-macro-luts-fusion-view-lut"></a> <a id="source-post-processing"></a> <a id="source-saving-custom-luts"></a> <a id="source-the-gamut-view-lut-editor"></a> <a id="source-the-log-lin-lut-editor"></a> <a id="source-using-viewer-luts"></a> <a id="source-viewer-output"></a>

### Fuse LUTs

Fuses are scriptable plugins that come bundled with the application or that you build inside Fusion. A fuse called CT_ViewLUTPlugin is applicable as a LUT on a viewer. You can additionally script fuses that draw on graphics hardware shaders baked into the LUT for real-time processing. Since fuse LUTs call for shader-capable graphics hardware, they can't run in software. To learn more about Fuses, consult the Fusion Scripting Guide found on the Blackmagic Design website.

### Using Viewer LUTs

Viewer LUTs can be switched on, edited, and switched off via the viewer LUT button and menu, plus through the viewer contextual menu. That menu lists every LUT on hand to Fusion, custom LUTs you've added yourself included.

The viewer LUT button alongside its menu, shown on the Fusion page inside DaVinci Resolve

To turn the current viewer LUT on and off:

- In the viewer toolbar, click the LUT button so the viewer LUT flips on and off.
- The LUT menu can additionally be reached as a submenu inside the viewer's contextual menu.

To choose another viewer LUT:

- Open the menu sitting to the right of the viewer LUT button and pick an option out of the viewer LUT menu.

To apply a Buffer LUT: 1 Somewhere inside the viewer, right-click and pick Global Options > Buffer LUT > Enable. 2 For a particular Buffer LUT, right-click yet again and select a LUT out of the Global Options > Buffer LUT submenu. Buffer LUTs frequently come in handy for applying monitor corrections, which tend not to shift between projects. To remove a Buffer LUT:

- Somewhere inside a viewer, right-click and pick Global Options > Buffer LUT > Enable so it gets unchecked.

### Editing Viewer LUTs

The viewers form the main spot where composites get judged, so it matters greatly that they give a faithful picture of how the content will appear once it's shown to an audience. The LUT Editor lets you tailor your viewer's output to fit the gamma and color traits of the playback device you'll eventually use, or to test how the present image looks within a wholly different color space, or how well it bears up across a span of differing color spaces. To bring up the Editor for any editable viewer LUT option: 1 In the viewer toolbar, click the LUT button so it's switched on. 2 Do one of the following:

- Choose Edit from the top of the viewer LUT menu.
- Inside the viewer, right-click and then pick LUT > Edit off the contextual menu.

### Editing the Fusion View Lookup Table

Much like the Color Curves node, the Fusion View LUT Editor relies on spline-based color correction. On top of letting you alter the separate color channels, the LUT carries Gain and Gamma sliders. The Gain slider helps with momentarily brightening or darkening the viewed image so shadow or highlight detail is easier to inspect. The Color Gamma and Alpha Gamma sliders serve to mirror the gamma values of the output device you'll eventually use. Video monitors, for instance, usually carry a gamma of 1.7, whereas computer monitors may span anywhere from 1.6 to 2.2. Alpha Gamma kicks in solely while you view an image's alpha channel, or while you view masks.

Shown is the LUT Editor belonging to the default Fusion View LUT. Editing the Gamut View LUT: through the Gamut View LUT Editor you pick a Source and Output color space that steers the viewer transform. The Remove and Add Gamma checkboxes let you decide to run the gamut conversion using linear or nonlinear gamma, or they let you merely strip or apply the relevant gamma values while leaving the color space alone. Ticking the Pre-Divide/Post-Multiply checkbox makes the image's pixel values get divided by the alpha values ahead of this conversion, then re-multiplied by the alpha value once it's done. That helps stave off the making of illegally additive images, especially along the edges of a blue/green key or while you handle 3D rendered objects.

### The Gamut View LUT Editor

### The Log-Lin LUT Editor

### Editing the Log-Lin View LUT

The Log-Lin LUT lets you run a Log to Lin or Lin to Log operation by way of the Mode pop-up menu. From the Log Type drop-down you pick which kind of log-encoding to process, and you decide whether the R, G, and B channels get locked together. A level adjustment lets you reset the digital span of output values, whereas the sliders for Soft Clip (Knee), Film Stock Gamma, and Conversion Gamma give you further command over the color transform. Finally, a Conversion Table field plus Browse button let you fold an extra LUT into this operation.

### LUT Processing Order

Within involved workflows, facilities might apply several LUTs back to back ahead of the image being seen. Their order counts, since every LUT yields different outputs. As an instance, for a Cineon file sitting in Log color space you may often apply three LUTs. First comes a Log to Lin conversion, then a Fusion View LUT that lays down a color calibration, and a third that corrects it for showing on an sRGB monitor, or you swap that last one for a 3D DCP LUT when you're viewing on a projector. Once you pick a node to be shown, the image it yields gets processed before it appears in the viewers. That processing order differs a little across 2D images and 3D scenes. With 2D images the image LUT goes on first, and the outcome gets composited over the checker underlay. 3D scenes are instead rendered using OpenGL.

### Image Output

### Image LUTs

### Macro LUTs Fusion View LUT

### Post Processing

### Checker underlay Dithering

Buffer LUT (single)

### Viewer Output

Order of processing. How processing is ordered across 2D images alongside 3D scenes. Whether 2D or 3D, the outcome may be drawn into an offscreen buffer where a Buffer LUT can apply, accompanied by dithering, a full view checker underlay, and any stereo processing. That final outcome is then drawn into the viewer, and any onscreen controls get drawn on top of it.

### Applying Multiple LUTs

By way of the viewer contextual menu you can stack several image LUTs into a processing chain. So as to add a further LUT, proceed thus: 1 Somewhere inside the viewer, right-click. 2 Off the viewer's contextual menu, pick LUT > Add New. 3 From within the Add New submenu, pick a LUT to bring in. So as to drop a LUT besides the first LUT, proceed thus: 1 Somewhere inside the viewer, right-click. 2 Off the viewer's contextual menu, pick LUT > Delete. 3 From within the Delete submenu, pick a LUT to drop. An entire stacked LUT configuration can be stored to and loaded out of a .viewlut file, as the text below explains.

### Saving Custom LUTs

Fusion offers an assortment of ways to build and use various viewer LUTs. You can store LUTs as you store viewer settings, you can import LUTs that were exported out of Fusion or other applications, and you can open any one of the many supported LUT file types. On top of that, you can draw on the standard nodes inside Fusion to build macros, which can then be stored and used as a LUT.

### LUT Settings

The simplest route to store a LUT you've built with the Fusion View LUT Editor is to reach for the LUT > Save menu sitting in the viewer contextual menu. Those settings get stored as an ASCII file carrying the extension .viewlut inside the LUTs folder. Whatever files bearing this extension turn up in that folder will appear within the Image LUT menus for easy loading. You can additionally load settings absent from the menu by picking LUT > Load out of the viewer's contextual menu.
