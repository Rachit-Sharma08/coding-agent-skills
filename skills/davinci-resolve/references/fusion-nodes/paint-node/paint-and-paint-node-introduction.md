# Paint and paint node introduction

Version: DaVinci Resolve 20.3 Reference Manual. Context: Paint node.
[Chapter index](INDEX.md) / [Next section](editing-options-toolbar-and-paint-controls-tab.md)
<a id="source-basic-node-setup"></a> <a id="source-inputs"></a> <a id="source-paint"></a> <a id="source-paint-node"></a> <a id="source-paint-node-1"></a> <a id="source-paint-node-introduction"></a> <a id="source-the-paint-node"></a> <a id="source-types-of-paint-strokes"></a>

### Paint Node

The Paint node found in Fusion is the subject of this chapter.

When you're hunting for tools in the Select Tool dialog, or working with scripting references, the abbreviation beside each node name comes in handy. Throughout this document, treat node trees that display MediaIn nodes in DaVinci Resolve as interchangeable with Loader nodes in Fusion Studio, except where stated otherwise.

### Paint

### The Paint node

### Paint Node Introduction

Paint is a highly adaptable, stroke-based tool meant for wire and rig removal, image cloning, or quickly building custom masks and mattes. You can even lean on Fusion's paint to construct brand-new images and artistic elements from nothing. A series of brush strokes makes up each Paint node. Those strokes are vector shapes whose brush, size, and effect can all be edited. There's a broad selection of apply modes and brush types on offer. The majority of Brushstrokes styles are editable polylines that give you fine control. You can animate them so their shape, length, and size shift over time. With a supported tablet, a stroke's opacity and size can respond to velocity and pressure. Because paint offers unlimited undo and redo, you're free to experiment before locking changes into an image sequence. Paint strokes can be reordered, deleted, and modified with practically boundless flexibility.

### Inputs

The Paint node carries two inputs, used to attach a 2D image plus an effect mask that can confine the painted region. Input: The orange input has to be wired to a 2D image, which establishes the size of the “canvas” you paint onto. Effect Mask: The blue input takes a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps coming from other tools. Attaching a mask here keeps the Paint confined to just the pixels inside the mask.

### Basic Node Setup

A Paint node can never go without an input connection. The most basic arrangement is to paint straight onto the incoming MediaIn node.

A MediaIn node connected directly to the Paint input

A setup with more flexibility uses a Background node to define a size matching the image you'll paint on. Within the Inspector, you'd make that background completely transparent. The Paint tool can then be merged as the foreground above the actual image you intend to paint on.

For added flexibility, a Paint node merged above a MediaIn

### Types of Paint Strokes

Paint stroke types located in the viewer toolbar. When you start out with the Paint tool, first pick the paint stroke type from the Paint toolbar sitting above the viewer. There are ten stroke types available, alongside a pair of additional tools that select and group paint strokes. Coverage of the stroke types and tools follows below, matching the sequence they sit in along the toolbar.

- Multistroke: While this is the default pick and the first real brush type in the toolbar, Multistroke generally isn't the stroke type you'll reach for most. That said, it's ideal for those 100-strokes-per-frame retouching paint jobs such as removing tracking markers. Multistroke runs much quicker than the Stroke type but can't be edited once it's made. By default a Multistroke lasts a single frame and can't be altered after it's painted. Set the number of frames ahead of painting using the Duration setting in the Stroke controls. The Keyframes Editor shows a shaded area for the Multistroke duration, though it's not editable there. Even though Multistrokes can't be edited directly, they can be grouped using the PaintGroup modifier and then tracked, moved, and rotated by animating the PaintGroup instead.
- Clone Multistroke: Much like Multistroke but built specifically for cloning elements from one area or image onto another. Ideal for those 100-strokes-per-frame retouching paint jobs such as removing tracking markers. Clone Multistroke moves faster than the Stroke type yet can't be edited once it's made. By default a Clone Multistroke lasts a single frame and can't be altered after it's painted. Set the number of frames ahead of painting using the Duration setting in the Stroke controls. The Keyframes Editor shows a shaded area for the Clone Multistroke duration, though it's not editable there.
- Stroke: For the most part, the Stroke tool is what comes to mind when people picture paint, and it's the go-to choice for most jobs. It's a fully animatable, editable, vector-based paint stroke. It can bog down when hundreds of strokes fill an image; when you're laying down a great many paint strokes, Multistroke is the better option. The Stroke type spans the whole global range as its duration. You can, however, change its duration whenever you like in the Keyframes Editor. After you've finished painting, click the Select button in the Paint toolbar so you don't accidentally tack on new strokes.
- Polyline Stroke: This lets you build and reshape a stroke the same way you'd build a Bézier path or polygon mask. To add a Polyline Stroke, click the Polyline button and click in the viewer to drop the first point. Keep clicking to drop further points onto the polyline. This click append style is the default, though polyline strokes can also be drawn in draw append mode. Polylines can be tracked or hooked up to existing polylines such as masks or animation paths. By default the Polyline Stroke spans the whole global range as its duration. You can, however, change its duration whenever you like in the Keyframes Editor.
- Circle: Builds a circular shape with animatable control over radius and center. By default the Circle type spans the whole global range as its duration. You can, however, change its duration whenever you like in the Keyframes Editor.
- Rectangle: Builds a rectangular region. By default the Rectangle type spans the whole global range as its duration. You can, however, change its duration anytime in the Keyframes Editor.
- Copy Polyline: Lets you build a closed Polyline region with an animatable offset so you can clone elements from one area or image onto another. By default the Copy Polyline type spans the whole global range as its duration. You can, however, change its duration whenever you like in the Keyframes Editor.
- Copy Circle/Rectangle: A circular or rectangular shape region with an animatable offset for cloning elements from one image onto another. By default the Copy Circle/Rectangle type spans the whole global range as its duration. You can, however, change its duration whenever you like in the Keyframes Editor.
- Fill: Comparable to the Wand mask tool. It fills neighboring pixels of similar color using a fill color drawn from the chosen color channel. By default the tool spans the whole global range as its duration. You can, however, change its duration whenever you like in the Keyframes Editor
- Paint Group: Lets you bundle several paint strokes together with full command over center and size. Because the Multistroke and Clone Multistroke styles can't be tracked, bundling those paint stroke types and tracking the paint group is one common reason to use groups.
