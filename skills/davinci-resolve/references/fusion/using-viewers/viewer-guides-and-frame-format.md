# Guides submenu in the viewers contextual menu and frame format settings

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using viewers.
[Chapter index](INDEX.md) / [Previous section](3d-viewer-lighting-shadows-and-transparency.md) / [Next section](region-of-interest-roi.md)
<a id="source-domain-of-definition-and-region-of-interest"></a> <a id="source-domain-of-definition-dod"></a> <a id="source-frame-format-settings"></a> <a id="source-setting-the-dod-manually-in-the-node-editor"></a> <a id="source-showing-the-dod"></a> <a id="source-the-frame-format-guides-settings"></a> <a id="source-the-guides-submenu-in-the-viewers-contextual-menu-1"></a>

### The Guides submenu in the viewer’s contextual menu

### Frame Format Settings

The Frame Format panel of the Fusion Settings window (found in the Fusion menu) offers two film guide settings you can use to tailor these guides.

- Guide 1 holds four fields specifying, in order, the offset from the image edges for the left, top, right, and bottom guides. Like every offset in Fusion, this is a resolution-independent figure where 1 equals the full image width and 0.5 equals half of it.
- The aspect ratio of the projection area is entered in Guide 2’s text box.

### The Frame Format Guides settings

### Domain of Definition and Region of Interest

As a compositing environment, the Fusion page leans on the familiar compositing conventions — Region of Interest (RoI) and Domain of Definition (DoD) — to lift performance dramatically.

### Domain of Definition (DoD)

In compositing, the Domain of Definition — usually shortened to DoD — denotes a rectangular region marking which part of an image truly holds data. DoD loosens the notion of an image’s actual frame, since rendering is no longer confined to the image’s literal width and height. This affects how Fusion renders images in two ways. First, nodes no longer have to render parts of the image the node won’t touch, which lets the renderer run more efficiently. Second, Fusion can now track and apply a node’s effect to pixels lying beyond the visible portion of the image. Take, for instance, the output of a Text+ node rendered over a transparent background: the text fills only some of the image’s pixels. Without Domain of Definition you’d be forced to process every pixel needlessly; with a DoD you can streamline the effects applied to the image, yielding faster results while using less memory. The image below shows an image with its DoD outlined.

The DoD appears as a pair of XY coordinates marking the corners of an axis-aligned bounding box (in pixels) Generally the DoD is worked out automatically with no need for you to step in. Every node in the Generator category, for example, generates the correct DoD on its own. For nodes such as Fast Noise, Mandelbrot, and Background, that usually means the full image dimensions, while for Text+ and nearly every Mask node the DoD is often much smaller or larger. The OpenEXR format can store an image’s data window, and Fusion applies that as the DoD when it loads such an image through a Loader node, then writes the DoD back out through the Saver node. When you work in the Fusion page within DaVinci Resolve, clips drawn from the Edit page timeline or Media Pool typically default the DoD to the full image width of the source media — media stored in OpenEXR format being the exception.

The DoD comes into being the moment the image is created or loaded into the composition. From there it flows downstream, where viewers fold it together with their Region of Interest to pin down precisely which pixels the node should affect. As you work, the various nodes automatically shrink, grow, or reposition the DoD as they apply their effect to an image, so the DoD shifts from node to node.

### Showing the DoD

When a node’s current DoD differs from that image’s frame size, it appears in the tooltip that pops up as the pointer hovers over a node in the Node Editor. The DoD can also be made visible in the viewer: right-click in a viewer and pick Region > Show DoD off the contextual menu.

### Setting the DoD Manually in the Node Editor

You can likewise set an image’s DoD by hand using the Tools > Miscellaneous > Auto Domain node found in the Effects Library. This node proves handy when you’re dealing with pre-created media that doesn’t fill the whole image. A rendering of a 3D character walking toward the camera, for instance, will often occupy only part of the image. The Auto Domain node can animate a DoD that wraps the character and disregards the rest of the image, which makes image processing more efficient.
