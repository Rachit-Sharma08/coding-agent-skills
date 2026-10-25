# Paint overview and types of paint nodes

Version: DaVinci Resolve 20.3 Reference Manual. Context: Paint.
[Chapter index](INDEX.md) / [Next section](setting-the-brush-size-and-choosing-an-apply-mode.md)
<a id="source-editable-stroke-types"></a> <a id="source-paint"></a> <a id="source-paint-node-workflow"></a> <a id="source-paint-overview"></a> <a id="source-paint-part-1"></a> <a id="source-painting-directly-on-an-image"></a> <a id="source-select-the-correct-paint-stroke-type"></a> <a id="source-setting-the-paint-nodes-resolution"></a> <a id="source-setting-up-the-paint-node"></a> <a id="source-shape-drawing-tools"></a> <a id="source-single-frame-stroke-types"></a> <a id="source-the-polyline-stroke-shape-animation-label"></a> <a id="source-types-of-paint-nodes"></a>

### Paint

This chapter walks through wielding Fusion’s non-destructive Paint tool to mend images, take out objects, and layer in creative elements.

### Paint Overview

As a procedural paint tool, the Paint node treats every paint stroke as a live, editable object drawn from properties you can combine freely to tackle a broad range of painting work. Put it to use painting masks, retouching images, doing beauty work, cloning objects away, or even building motion graphics. Every part of a paint stroke stays open to change well after you lay it down. Because the strokes remain editable, you’re free to apply, adjust, bypass, delete, and even reorder them within a node tree.

### Types of Paint Nodes

Fusion offers two kinds of paint nodes. The Paint node is a fully featured, vector-based paint tool for creative work and retouching that needs an input to paint onto. The Mask Paint node, by contrast, lets you paint an alpha channel specifically so you can confine an effect’s area. With it you draw paint strokes on an alpha channel without any input being required.

- You’ll find the Paint node under the Paint category of the Effects Library.
- You’ll find the Mask Paint node under the Mask category of the Effects Library.

What chiefly separates these two Paint tools is that the Mask Paint tool only ever paints the Alpha channel, hence it has no channel selector buttons. The Paint tool, meanwhile, can paint on any channel or all of them. Most of this chapter deals with the Paint node, given that its parameters and settings match the Mask Paint node’s exactly.

The Paint node, found within the Effects Library’s Paint category

### Setting Up the Paint Node

Two inputs sit on the Paint node. As with most Fusion nodes, the orange background input is the main one, where you hook up the “canvas” or image you’ll paint on, and the second blue input takes an Effect Mask. The Paint node, unlike the Mask Paint node, needs a background input before any painting can start.

### Setting the Paint Node’s Resolution

However you place the Paint node in your node tree, it takes on the background input image’s resolution as the working resolution for that task. The Paint tool is genuinely resolution independent and you can revise this assigned resolution whenever you wish, yet getting the resolution of your media right matters, since it bears on operations like motion tracking that you’ll fold into your paint workflow. For that reason, the Paint node needs a background input to fix the resolution of the “canvas” you’re about to paint on. There are two ways to wire up a Paint node in the node tree for this: painting straight onto an image, or running Paint as the foreground.

### Painting Directly on an Image

The image you intend to paint on can plug straight into the Paint node’s background input. That’s the simplest, tidiest way to build the node tree, though it offers little compositing flexibility.

The Paint node is dropped right after the node it paints on Using Paint as the Foreground in a Merge Composite Another arrangement has a Background node set the resolution for the Paint node, with the result composited over the real background through a Merge node. Going this route lets you lean on the Merge node’s Apply Mode setting (sometimes called composite modes) to dictate how your paint strokes blend against the image, but it does call for a little more setup.

The merge composites the Paint node over the image you mean to paint on

Putting this together takes a bit of node configuration. The Background node has to be wholly transparent, and unless you’re doing something basic such as painting over an image with the Stroke tool set to Color, you have to drag the image you’ll clone or smudge into the Source Tool field of the Paint node’s inspector. Fuller coverage of these steps comes later in the chapter.

### Paint Node Workflow

To start painting, first pick the paint stroke type from the Paint toolbar above the viewer. Ten stroke types are on offer, along with two more tools for selecting and grouping paint strokes. For a full rundown of the stroke types and tools, turn to the DaVinci Resolve Reference Manual’s Chapter 113, “Paint Node,” or, in the Fusion Reference Manual, Chapter 53. The Stroke tool is the main one for painting and cloning. A fully animatable, editable vector-based paint stroke, the Stroke tool starts out spanning the whole global range in duration.

Cloning, beauty work, and creative paint are the Stroke tool’s most frequent uses

### Select the Correct Paint Stroke Type

Rather than juggling several dedicated Paint nodes for separate operations, you get a single tool carrying an assortment of stroke types, thanks to the procedural design of Fusion’s Paint tool. Every stroke type fills a distinct role. From the Paint toolbar above the viewer you choose among the various stroke types and drawing tools, which fall into a handful of categories.

### Single-Frame Stroke Types

The Multistroke and Clone Multistroke are built squarely for single-frame retouching jobs — clearing raindrops out of a shot that’s meant to look sunny, say, or wiping away scratch marks and dust while restoring vintage footage. For tasks of that sort, these two Multistroke options outrun the other stroke types, but they can’t be edited afterward. So you have to settle the brush’s size and function, plus the paint stroke’s duration, before you paint. Each of these stroke types runs one frame by default, a figure you can change with the Stroke Duration slider in the Inspector. Multistroke and Clone MultiStroke are essentially one and the same, save that Clone Multistroke sets the tool up for cloning automatically. The Multistroke, on the other hand, leaves you to configure cloning by hand.

The Multistroke and Clone Multistroke are single-frame stroke types you can’t edit later

### Editable Stroke Types

The Stroke and Polyline resemble each other in that both stay open to change and animation whenever you like. Each one also opens with a duration covering the whole comp, which the Keyframes Editor can likewise alter.

The Stroke and Polyline strokes can be edited and run the whole comp The Stroke Tool Among the most adaptable editable stroke types you’ll reach for across many jobs is the Stroke, since it’s fully animatable and editable. Every element of the Stroke can be animated, and the Write-on/ Write-off parameters let you dictate how the stroke shows up onscreen. You can also tie a tracker to the Stroke’s Center point when you want it to track a specific onscreen motion. Out of the box, the Stroke type keeps the path’s shape control points hidden. The Stroke’s center and rotation can be moved and tracked, yet the individual control points forming the spline stay out of sight. To surface those control points, head to the Stroke Controls down at the Inspector’s base and hit the Make Editable button.

The Make Editable button brings the Stroke’s control points into view The Stroke type may be the most adaptable, but that adaptability can cost performance once you’re laying hundreds of strokes on a frame. When you have a great many strokes that don’t require animation, Multistroke or Clone Multistroke is the wiser pick, since they’re easier on the processor. The Polyline Stroke Tool The Polyline Stroke behaves more like a drawing tool than a paintbrush. It carries the Stroke tool’s full functionality, with the difference that you create it not by dragging or “painting” as you would a brush, but by clicking to lay down a spline path, the way you do with masks and motion paths. Even before you make a stroke in the viewer, the Polyline Stroke can attach to existing polylines such as a mask or a motion path. With a motion path published, a right-click on the Shape Animation label — found at the base of the Polyline Stroke’s Stroke Controls — lets you call up the Connect To menu and take on the shape of a motion path or mask. The same trick works when you import SVG graphics and want to “paint-on” their outlines.

### The Polyline Stroke Shape Animation label

### Shape Drawing Tools

There are five shape-based drawing tools for drawing shapes and then either filling them with a color or cloning an area out of a source image. Each behaves much like the Stroke and Polyline stroke type, in that you can edit them whenever you like and their default duration covers the comp’s full global range. That duration, too, can be edited at any moment in the Keyframes Editor.

The Shape Strokes serve to build shapes or to clone areas defined by shapes Every Copy [Shape Name] stroke type asks that you wire the source node you’re cloning from into the Paint node and switch the Fill Type menu to Image.

The Copy Shapes need a Source wired straight into the Paint tool and set to Image
