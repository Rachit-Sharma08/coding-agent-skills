# Editing options toolbar and paint controls tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Paint node.
[Chapter index](INDEX.md) / [Previous section](paint-and-paint-node-introduction.md) / [Next section](stroke-controls-and-paint-node-modifiers.md)
<a id="source-apply-controls"></a> <a id="source-brush-controls"></a> <a id="source-controls-tab"></a> <a id="source-editing-options-toolbar"></a> <a id="source-inspector"></a> <a id="source-the-paint-controls-tab"></a>

### Editing Options Toolbar

Paint edit options show up in the viewer once a Polyline stroke has been made. Polyline-based paint strokes bring a second toolbar into the viewer for picking among different editing options. Polyline Stroke and Copy Polyline are the paint strokes that bring along this second toolbar. As for the Stroke style, it too surfaces this toolbar once you've selected the stroke and pressed the Make Editable button over in the Inspector.

- Click Append: This is the default behavior while you're making a polyline stroke. It acts more like a Bézier pen drawing tool than a paintbrush. A click sets a control point and adds the next control point when you click again somewhere else.
- Draw Append: A freehand drawing tool. It lays down a stroke much like sketching with a pencil on paper. With the Draw tool you can build a fresh Polyline Stroke or Copy Polyline Stroke, or lengthen a Stroke style once the Make Editable button over in the Inspector has been pressed.
- Insert: Insert drops a new control point onto the paint stroke spline.
- Modify: Modify lets you safely shift or smooth any existing point along a spline without

worrying that you'll accidentally tack on a new point.

- Done: Keeps every point along the spline from being moved or modified. New points can't be added either. You are, however, free to move and rotate the whole spline.
- Closed: Closes an open polyline.
- Smooth: Converts whichever stroke or control point is selected from a linear into a smooth curve.
- Linear: Converts whichever stroke or control point is selected from a smooth curve into linear.
- Select All: Selects every control point on the polyline.
- Keys: Reveals or hides the control points along the polyline.
- Handles: Reveals or hides the Bézier handles along the polyline.
- Shape: Wraps a reshape rectangle around the selected polyline control points. With that reshape

rectangle, you can deform clusters of polyline control points or whole shapes far more easily than tweaking each point.

- Delete: Deletes the selected control point(s).
- Reduce: Opens a Freehand precision window you can use to cut down the count of control

points on a polyline. That can make a paint stroke easier to modify, particularly one drawn with the Draw tool.

- Publish: The Publish menu lets you publish either control points or the path. Publishing is a kind of parameter linking. It makes the chosen item available for other controls to use, or lets you attach a control point to a tracker.
- Follow Points: Lets a chosen point trail the path of a published point. The point follows the published point at an offset position.
- Roto Assist: Switch on the Roto Assist button as you start painting with the Polyline Stroke tool. As you click to build up the shape's points, the polyline points snap onto whichever edge is closest. Points that have snapped onto an edge are marked by a cyan outline. Three principal Roto Assist options are available from the drop-down menu:

Multiple Points: With this on, a single click on a high-contrast edge drops several points to map the entire edge, rather than making you place each one by hand. It's a one-time-only click. The next click goes back to single point edge detection. Distance 8: Brings up a dialog where you set the pixel range within which the edge search happens. Reset: Used to clear the snap attribute from every snapped point. Once reset, those points can no longer be tracked.

### Inspector

### The Paint Controls tab

### Controls Tab

Not every control described here turns up in every mode. Certain controls matter only within a particular Paint mode and stay hidden when they don't apply. The Controls tab is where you set up your paint settings before painting. After a paint stroke has been made, apart from the Multistroke and Clone Multistroke, you can pick the stroke in the viewer and revise the controls.

### Brush Controls

- Brush Shape: Picking the brush tip shape is done with the brush shape buttons. Apart from the single pixel shape, the brush shape's size can be changed in the viewer if you hold the Command or Ctrl key as you drag with the mouse. Soft Brush: A circular brush tip with soft edges is what the Soft Brush type gives you. Circular Brush: With hard edges, a Circular Brush is a brush tip shape. Image Brush: Through the Image Brush, pictures pulled from any node in the node tree, or off a file system, can act as a brush tip. Single Pixel Brush: Well suited to fine detail work, the Single Pixel Brush yields a brush tip measuring precisely one pixel across. The single pixel brush receives no anti-aliasing. Square Brush: With hard edges, a Square Brush is a brush tip.
- Vary Size: Vary size settings alter the stroke size according to speed or a pressure-sensitive pen and tablet.

Constant: The brush tip holds a constant size across the stroke. With Pressure: The stroke size changes with the pressure actually applied. With Velocity: The stroke size changes with how fast you paint. A quicker stroke comes out thinner.

- Vary Opacity: Vary opacity settings alter the stroke opacity according to speed or a pressuresensitive pen and tablet.

Constant: The brush tip stays at a constant transparency setting across the whole stroke. With Pressure: The stroke transparency changes with the applied pressure. With Velocity: The stroke transparency changes with how fast you paint. A quicker stroke comes out more transparent.

- Softness: This control lets you raise or lower the Softness of a soft brush.
- Image Source: With the Image Source brush type, choose among three possible source

brush images. Node: Here the image source is taken from a node's output within the node tree. To assign the source, drop that node onto the Source node input field in the Inspector. Clip: Here the image source is taken from an image or sequence stored on disk. Any file format that Fusion's Loader or MediaIn node handles will work. Brush: From the menu, choose an image that will serve as a brush. Whatever images live in the Fusion > Brushes directory fill out that menu.

- Color Space: With the Fill tool active, a Color Space menu picks the color space used when sampling colors around the Fill tool center to decide what goes into the fill range.
- Channel: With the Fill tool active, a Channel menu picks which color channel drives the fill paint. As one example, with alpha chosen, the fill spreads over contiguous pixels of the alpha channel.

### Apply Controls

- Apply Mode: The Apply Modes are buttons that change how a brush paints. Color: The Color Apply Mode paints plain colored strokes. Paired with an image brush, it can also tint the image.

Clone: Drawing on adjustable positions plus time offsets, the Clone Apply Mode duplicates a region out of the same image. It's also capable of copying parts of one image into a second image. The source image can be any image taken from the node tree. Emboss: The Emboss Apply Mode embosses the parts of the image the brush stroke covers. Erase: Erase reveals the underlying image through every other stroke, effectively wiping away parts of the strokes below it without actually destroying those strokes. Merge: This Apply Mode effectively merges the brush onto the image. It works much like the Color Apply Mode but offers no color controls. It's best paired with the image brush type. Smear: Smears the image, taking the brushstroke's direction and strength as a guide. Stamp: Stamps the brush onto the image, disregarding any alpha channel or transparency information entirely. This mode suits applying decals to the target image best. Wire: By sampling the pixels nearby and dragging them inward toward the stroke, this Wire Removal Mode takes out wires, rigging, and similar small elements within the frame.
