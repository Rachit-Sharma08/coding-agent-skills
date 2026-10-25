# Deep to image and deep to points

Version: DaVinci Resolve 20.3 Reference Manual. Context: Deep to image, Deep to points.
[Chapter index](INDEX.md) / [Previous section](dcrop-and-deep-to-image.md) / [Next section](deep-to-points-and-dholdout-and-dmerge.md) / [Deep to Image DTI](dcrop-and-deep-to-image.md)
<a id="source-basic-node-setup-2"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab-1"></a> <a id="source-deep-to-points-controls"></a> <a id="source-deep-to-points-dtp"></a> <a id="source-deep-to-points-node-introduction"></a> <a id="source-image-tab"></a> <a id="source-inputs-2"></a> <a id="source-inspector-1"></a> <a id="source-the-deep-to-image-image-tab"></a> <a id="source-the-deep-to-points-node"></a> <a id="source-transform-tab"></a>

### Image Tab

What this tab’s controls do is set the resolution, color depth, and pixel aspect of the rendered image the node turns out.

### The Deep to Image Image tab

Process Mode Reach for this menu control to pick which Fields Processing mode Fusion uses while rendering changes to the image. Which option starts out as the default hinges on the Has Fields checkbox control in the Frame Format preferences.

Depth Setting the pixel color depth of the particles is the job of the Depth menu. Where an 8-bit pixel sits, a 32-bit pixel needs 4X the memory but delivers far finer color accuracy. With Float pixels you get high dynamic range values reaching past the usual 0…1 range, so colors brighter than white or darker than black can be represented. Source Color Space To set the Color Space of the footage and steer a linear workflow, you can turn to the Source Color Space menu. This carries out no real color space conversion the way the Gamut tool does; instead it writes the source space data into the metadata, where that metadata is missing. Downstream, that metadata can then feed a Gamut tool set to the From Image option, or a Saver where explicit output spaces have been defined. You get two options to pick from:

- Auto: Reads whatever metadata the image may hold and passes it along automatically.
- Space: Brings up a Color Space Type menu where you can pick the image’s correct color space.

the image. Source Gamma Space The footage’s Gamma Space is something you set through the Curve type menu, and while working in a linear workflow you can choose to strip it out via the Remove Curve checkbox. Three choices fill the Curve type menu:

- Auto: Reads whatever metadata the image may hold and passes it along automatically.
- Space: Brings up a Gamma Space Type menu where you can pick the image’s correct gamma curve.

the image.

- Log: Calls up the Log/Lin settings, much like the Cineon tool does.

To learn more, turn to Chapter 99, “Film Nodes,” within the DaVinci Resolve Reference Manual, or to Chapter 39 within the Fusion Reference Manual. Remove Curve Depending on which Gamma Space you chose, or on the Gamma Space turned up by Auto mode, the Gamma Curve gets stripped from the material — or a log-lin conversion gets run on it — which in effect converts it to a linear output space. Pre-Divide/Post-Multiply When you need it, this lets you turn “straight” Alpha channels into pre-multiplied Alpha channels.

### Common Controls

Settings Tab A copy of the Inspector’s Settings tab also lives on other Deep Image nodes. These common controls get their detailed treatment at the end of this chapter, in the “The Common Controls” section.

### Deep to Points [DTP]

### The Deep to Points node

### Deep to Points Node Introduction

Deep images get turned into a 3D point cloud by this tool. Handy for picturing depth samples, it gives you a way to see elements in Z as you bring them in.

### Inputs

A single input is what the Deep to Points tool relies on. Input: The lone required connection is this orange input. A node carrying deep image data feeds it. Camera: Wire a scene’s camera into the green camera input and the point cloud lands precisely relative to the original 3D scene. The camera’s perspective gets factored in, so points end up accurately placed inside the 3D Viewer.

### Basic Node Setup

Into the Deep to Points node comes the media in that holds the deep image data. From there it builds a 3D point cloud out of the image to make picturing elements in Z space easier.

Taking in deep image data, Deep to Points builds a Point Cloud out of it and then hands that visualization along to the node tree beyond.

### Inspector

### Deep to Points controls

### Controls Tab

Inside the Controls tab sit parameters that govern the point cloud.

- Style: Style lets you render the points in the viewer either as cross hairs or as points.
- Size: Use this slider to enlarge the onscreen crosshairs or points
- Antialiasing: Switch it on and points turn rounded and smooth, giving softer edges.
- Density: This slider lets you steer how concentrated the points are overall in the viewer.

Raise the value and the intensity of points builds up; lower it and the reverse happens.

- Default Color: Clear the Use Per-Point Colors checkbox and every point takes on the color you set in this control.
- Use Per-Point Colors: Switch it on and every point takes its color from the connected source clip.
- Make Renderable: Sets whether the point cloud you see in the 3D viewer will render in a Renderer3D node. Tick this checkbox and the point cloud can be rendered out to a flat 2D image.
- Unseen by Camera: This checkbox control shows up once the Make Renderable option is on. Tick the Unseen by Cameras checkbox and the point cloud stays visible in the viewers yet isn’t rendered into the output image by the Renderer 3D node.
- Scale: This slider lets you grow or shrink the point cloud’s overall size.
- Depth Scale: With the slider you can stretch or squeeze the point cloud’s overall depth. Raise the depth scale and the overall depth distance grows; the points spread apart, giving you a fuller picture of the point cloud.
- Flip Depth: Reach for this checkbox to invert the depth data, swapping the points’ position from negative to positive

### Transform Tab

What this tab’s controls do is set the position and scaling parameters of the point cloud.
