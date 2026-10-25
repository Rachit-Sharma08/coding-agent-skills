# Introduction to masks and polylines and mask nodes

Version: DaVinci Resolve 20.3 Reference Manual. Context: Rotoscoping with masks.
[Chapter index](INDEX.md) / [Next section](rotoscoping-mask-attachment-and-mattecontrol.md)
<a id="source-a-polygon-nodes-mask-seen-in-the-viewer"></a> <a id="source-b-spline-masks"></a> <a id="source-b-spline-polylines"></a> <a id="source-b-splines-excel-at-creating-smooth-curves"></a> <a id="source-bitmap-masks"></a> <a id="source-bézier-polylines"></a> <a id="source-converting-polylines-from-one-type-to-another"></a> <a id="source-ellipse-rectangle-and-triangle-masks"></a> <a id="source-how-to-use-masks-with-other-nodes"></a> <a id="source-introduction-to-masks-and-polylines"></a> <a id="source-mask-nodes"></a> <a id="source-mask-paint"></a> <a id="source-polyline-types"></a> <a id="source-ranges-mask"></a> <a id="source-rotoscoping-with-masks"></a> <a id="source-rotoscoping-with-masks-part-1"></a> <a id="source-wand-mask"></a>

### Rotoscoping with Masks

This chapter explains using masks to rotoscope, which ranks among compositing's most frequent jobs.

### Introduction to Masks and Polylines

A polyline is the spline that comes into play any time a control gets animated along a motion path or a node's effect is masked by a drawn shape. The Paint and Grid Warp nodes rely on them as well. At a more elementary level, polylines steer the animation within the Spline Editor. Because these splines turn up in nearly every context, they carry enormous flexibility, packing a sizable set of controls, modes, and options. The pages here give a broad look at polylines and how they work, with targeted notes on putting them to use for masks.

### Mask Nodes

A mask node produces an image whose job is to define transparency within some other image. Where most image-creation nodes in Fusion build a full RGBA image, mask nodes instead build a single channel image. The Polygon mask tool, the one you'll reach for most, sits in the toolbar. To dig deeper into these mask tools, consult Chapter 108, "Mask Nodes" (DaVinci Resolve Reference Manual), or, within the Fusion Reference Manual, Chapter 48.

The nodes on offer within the Effects Library's Mask bin Polygon Mask The masks Polygon produces are Bézier shapes the user draws. It is the polyline type you'll meet most often and the everyday backbone of rotoscoping. The moment you drop a Polygon mask tool into the Node Editor, it is set to animate automatically.

### B-Spline Masks

B-Spline masks are shapes the user builds from polylines drawn with the B-Splines. While linear, they act exactly like polyline shapes, but once smoothed the control points sway the shape via tension and weight. The upshot is generally cleaner shapes that need fewer control points. The moment you drop a B-Spline mask tool into the Node Editor, it is set to animate automatically.

### Bitmap Masks

With the Bitmap mask, images coming from the Node Editor can serve as masks for nodes and effects. A Bitmap mask can draw its values from any of the image's color, alpha, hue, saturation, luminance, or auxiliary coverage channels. You can also build the mask out of the Object or Material ID channels found inside certain 3D-rendered image formats.

### Mask Paint

Mask Paint lets a mask be painted with Fusion's built-in vector paint nodes.

### Wand Mask

A Wand mask gives you a crosshair you can place over the image. Whatever color the pixel beneath the crosshair holds is used to build a mask, and every neighboring pixel of a comparable color joins the mask too. A mask of this sort works perfectly for confining color adjustments.

### Ellipse, Rectangle, and Triangle Masks

These count as primitive shape masks. To dig deeper into these mask tools, consult Chapter 108, "Mask Nodes" (DaVinci Resolve Reference Manual), or, within the Fusion Reference Manual, Chapter 48.

### Ranges Mask

Much like the Bitmap mask, the Ranges mask lets images from the Node Editor stand in as masks for nodes and effects. Rather than pulling a plain luminance-based mask from one channel, Ranges supports spline-based picking of low, mid, and high ranges, much as the Color Corrector node does.

### Polyline Types

Polylines can be drawn with either the B-Spline or the Bézier spline type. Your pick hinges on the shape you're after and how at ease you are with each spline style.

### Bézier Polylines

A Bézier polyline is a shape built from control points and handles. Multiple points working together define a polyline's overall form.

Bézier control point with direction handles extended to create a smooth curve

Every control point carries a pair of handles that pin down the precise form of the polyline segments running through that control point. Changing the angle or the length of the direction handles dictates whether that polyline segment turns out smooth or linear.

Bézier control point with direction handles aligned to create a linear segment Anyone who has worked in programs like Adobe Photoshop or Illustrator will already grasp most of the fundamentals behind editing Bézier polylines.

### B-Spline Polylines

A B-Spline polyline resembles a Bézier spline, yet these polylines really shine at producing smooth shapes. Rather than relying on a control point plus direction handles for smoothness, the B-Spline polyline lays out points without direction handles to set a bounding box around the shape. How smooth the polyline reads comes down to the tension of the point, which you can dial in as needed.

### B-Splines excel at creating smooth curves

### Converting Polylines from One Type to Another

Building a shape with a B-Spline or polyline doesn't lock you into the controls you began with. Whenever you need to, you can turn any shape from B-Spline into Bézier, or Bézier into B-Spline. To swap a shape across the Polyline and B-Spline controls: right-click the shape inside the viewer, then off the spline's contextual menu pick either Convert Bézier Spline to B-Spline or Convert B-Spline to Bézier (whichever one fits is the only choice shown).

Converting between the two types keeps the original shape intact. As a rule the new polyline ends up with roughly double the control points of the original shape so the shape changes as little as possible. Animation carries over as well, though this conversion won't always come out flawless. Reviewing the animation once you've converted spline types is a smart move.

### How to Use Masks with Other Nodes

As a rule, a node applies its effect across every pixel of an image. Many nodes, though, carry mask inputs you can use to confine the effect that node has on the image.

A Blur node with a Polygon node masking its effect A mask is a single-channel image that pins down which regions of an image you intend to affect. You can build masks from primitive shapes (think circles and rectangles), from intricate polyline shapes handy for rotoscoping, or by pulling channels out of another image.

### A Polygon node's mask seen in the viewer

Any single mask node can produce just one shape. Mask nodes, however, are meant to be chained one after another, so you can blend several masks of various kinds into intricate shapes. As an example, a pair of masks can be subtracted from a third mask to punch holes through the resulting mask channel. Fusion gives you a handful of ways to put masks to work on various tasks. You can hang Mask nodes after other nodes where you want to introduce transparency, or you can wire Mask nodes straight into the dedicated inputs of other nodes to confine or generate various kinds of effects.
