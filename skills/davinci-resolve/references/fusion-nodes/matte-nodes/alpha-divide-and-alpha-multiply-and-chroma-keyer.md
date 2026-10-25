# Alpha divide and alpha multiply and chroma keyer

Version: DaVinci Resolve 20.3 Reference Manual. Context: Alpha divide, Alpha multiply, Chroma keyer.
[Chapter index](INDEX.md) / [Next section](chroma-keyer-chroma-key-tab.md)
<a id="source-alpha-divide-adv"></a> <a id="source-alpha-divide-node-introduction"></a> <a id="source-alpha-multiply-aml"></a> <a id="source-alpha-multiply-node-introduction"></a> <a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-basic-node-setup-2"></a> <a id="source-chroma-keyer-cky"></a> <a id="source-chroma-keyer-node-introduction"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-inputs-2"></a> <a id="source-inspector"></a> <a id="source-inspector-1"></a> <a id="source-matte-nodes"></a> <a id="source-matte-nodes-part-1"></a> <a id="source-the-alpha-divide-node"></a> <a id="source-the-alpha-multiply-node"></a> <a id="source-the-chroma-keyer-node"></a>

### Matte Nodes

Here the chapter walks through the Matte nodes that Fusion provides. You can type the abbreviation beside each node name into the Select Tool dialog while hunting for tools, and it works in scripting references too. Throughout this document, treat node trees that show MediaIn nodes in DaVinci Resolve as equivalent to Loader nodes in Fusion Studio, except where stated otherwise.

### Alpha Divide [ADv]

### The Alpha Divide node

### Alpha Divide Node Introduction

True to its name, the Alpha Divide exists for one job alone: dividing an incoming image's color channels by its alpha channel. To color correct an image carrying a premultiplied alpha channel, first place an Alpha Divide node ahead of any color correction node so you get a nonpremultiplied image. With that done, you can color correct. Once the correction is finished, tack on an Alpha Multiply node to put the image back into its premultiplied state.

### Inputs

Inside the Node Editor the Alpha Divide node has two inputs. Input: The orange input takes a 2D image carrying a premultiplied Alpha. Effect Mask: The optional blue input looks for a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wiring a mask here confines the Alpha divide to certain pixels. An effects mask gets applied to the tool once the tool has been processed.

### Basic Node Setup

You insert the Alpha Divide node ahead of any color correction performed on an image with a premultiplied Alpha channel. Assume here the MediaIn node carries a premultiplied Alpha channel. With the Alpha Divide node inserted, the color correction nodes then work on the “straight” Alpha. At the chain's tail, an Alpha Multiply node restores the premultiplied Alpha channel. Should you be using just one color correction node, the Pre-Divide/Post-Multiply checkbox on the Options tab can stand in for the Alpha Divide/Alpha Multiple nodes.

Ahead of color correcting an image that has premultiplied alpha, an Alpha Divide node goes in.

### Inspector

This node has no controls.

### Alpha Multiply [AML]

### The Alpha Multiply node

### Alpha Multiply Node Introduction

True to its name, the Alpha Multiply exists for one job alone: multiplying an image's color channels by its alpha channel. To color correct an image carrying a premultiplied alpha channel, first place an Alpha Divide node ahead of any color correction node so you get a non-premultiplied image. With that done, you can color correct. Once the correction is finished, tack on an Alpha Multiply node to put the image back into its premultiplied state.

### Inputs

Inside the Node Editor the Alpha Multiply node has two inputs. Input: The orange input takes a 2D image carrying a “straight” or non-premultiplied alpha. Effect Mask: The optional blue input looks for a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wiring a mask here confines the Alpha multiply to certain pixels. An effects mask gets applied to the tool once the tool has been processed.

### Basic Node Setup

You place the Alpha Multiply node after color correction is done on an image with a premultiplied Alpha channel. Assume here the MediaIn node carries a premultiplied Alpha channel. With the Alpha Divide node inserted, the color correction nodes then work on the “straight” Alpha. At the chain's tail, an Alpha Multiply node restores the premultiplied Alpha channel. Should you be using just one color correction node, the Pre-Divide/Post-Multiply checkbox on the Options tab can stand in for the Alpha Divide/Alpha Multiple nodes.

Following color correction of an image that has premultiplied alpha, an Alpha Multiply node goes in.

### Inspector

This node has no controls.

### Chroma Keyer [CKy]

### The Chroma Keyer node

### Chroma Keyer Node Introduction

By stripping chosen colors out of the scene, the Chroma Keyer node builds an alpha channel (matte) for an image. While the Delta Keyer and Primatte carry particular optimizations for keying off blue and green, the Chroma Keyer handles any color just as well. NOTE: For blue- or green-screen shots, the Delta Keyer or Primatte node is the better choice over the more general-purpose Chroma Keyer node.

### Inputs

Inside the Node Editor the Chroma Keyer node carries four inputs. Input: The orange input takes a 2D image holding the color you want keyed for transparency. Garbage Matte: The gray garbage matte input takes a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wire a mask here and any image areas inside the matte turn transparent. The garbage matte goes straight onto the image's alpha channel. Solid Matte: The white solid matte input takes a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wire a mask here and any image areas inside the matte become fully opaque. Effect Mask: The optional blue input looks for a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wiring a mask here confines the alpha multiply to certain pixels. An effects mask gets applied to the tool once the tool has been processed.

### Basic Node Setup

The Chroma Keyer node accepts a 2D image such as the MediaIn node below, then strips out a color you specify by dragging across it in the viewer. As a result, the chosen color becomes transparency, letting you composite the image as the foreground inside a Merge node.
