# Srectangle and srender and sstar

Version: DaVinci Resolve 20.3 Reference Manual. Context: Srectangle, Srender, Sstar.
[Chapter index](INDEX.md) / [Previous section](spolygon-and-srectangle.md) / [Next section](sstar-basic-node-setup.md) / [Continue sStar / Basic Node Setup](sstar-basic-node-setup.md) / [sRectangle](spolygon-and-srectangle.md)
<a id="source-basic-node-setup-3"></a> <a id="source-basic-node-setup-4"></a> <a id="source-common-controls-2"></a> <a id="source-controls-3"></a> <a id="source-image-tab"></a> <a id="source-inputs-1"></a> <a id="source-inspector-2"></a> <a id="source-srender"></a> <a id="source-sstar"></a> <a id="source-style-2"></a> <a id="source-style-tab-2"></a> <a id="source-the-srectangle-controls-tab"></a> <a id="source-the-srectangle-style-tab"></a> <a id="source-the-srender-image-tab"></a> <a id="source-the-srender-node"></a> <a id="source-the-sstar-node"></a>

### Basic Node Setup

Being a shape generator, the sRectangle node produces a shape and so carries no inputs. The sRectangle's output can feed a sRender for viewing and further compositing, or—more commonly—hook into another Shape node such as sGrid or sDuplicate.

An sRectangle node routed to an sDuplicate node, then displayed via an sRender node

### Inspector

### The sRectangle Controls tab

### Controls

You use the Controls tab to set the rectangle's traits—fill, border, size, and placement. Solid With the Solid checkbox on, the rectangle shape fills with whatever color you defined in the Style tab. With it off, only an outline drawn by the Border Width control shows, and the middle turns transparent. Border Width This parameter grows or shrinks the border running around the shape. Though usable while the Solid checkbox is on, its main job is governing outline thickness once the checkbox is off. Border Style The Border Style parameter dictates the way the rectangle's sides meet at the corners. Three corner-treatment styles are on offer. Bevel flattens each corner to a square. Round gives corners a curved finish. Miter keeps corners sharp and pointed. Cap style With the Solid checkbox off, three Cap Style options appear. Those cap styles let lines end flat, rounded or squared off. Flat caps finish with flat, squared ends, whereas rounded caps finish with semi-circular ends. Squared caps carry projecting ends reaching half the line width past the line's end. None of the caps show up unless the length sits below 1.0. Position Only when the Solid checkbox is off does the Position parameter appear. It lets you set the shape's starting point. Paired with the Length parameter, it places the gap in the outline. Length Only when the Solid checkbox is off does the Length parameter appear. A length of 1.0 yields a closed shape. Dropping the length under 1.0 opens a gap in the outline. Keyframing the Length parameters lets you build write-on style animations.

X and Y Offset You use these parameters to shift the shape left, right, up, and down across the frame. The shape begins at the frame's center, and the parameters offset that placement. The offset coordinates are normalized to the frame's width. So an X offset of 0.0 sits centered, and a value of 0.5 drops the shape's center right onto the frame's right edge. Width/Height The Width and Height parameters fix the vertical and horizontal size of the rectangle. When the values match, you've got a square. Corner Radius This parameter decides whether the rectangle's corners come out sharp or rounded. A value of 0.0 yields sharp corners, while a value of 1.0 turns a starting square shape into a circle or a rectangle into a pill shape. Angle The Angle parameter spins the shape around its center axis.

### Style Tab

### The sRectangle Style tab

### Style

The Style tab handles assigning color to the shape and managing its transparency. Color The Color parameter controls fix the color of both fill and border coming from the sRectangle node. To pick a shape color, click the color disclosure arrow and work the color swatch, or drag the eye dropper into the viewer to lift a color out of an image. With the RGBA sliders or number fields you can key in the value of each color channel or the Alpha channel's strength. Allow Combining With this checkbox on, the Alpha channel value holds steady even while passing through downstream nodes that might overlap the shape with copies of itself. With it off,

the Alpha channel value can climb wherever the shape overlaps itself. For example, if a rectangle Alpha channel reads .5, turning on the Allow Combining checkbox preserves that value even when the shape moves through a duplicate or grid node that overlaps the shape and Alpha channel. Leaving the checkbox off lets the Alpha channel values compound at each spot of overlap.

Allow Combining turned on (left) and turned off (right) Common Controls Settings Tab Across all Shape nodes the Inspector's Settings tab is identical. Those common controls get a full treatment at this chapter's close in the “The Common Controls” section.

### sRender

### The sRender node

The sRender node turns the vector shapes into an image. Through the sRender's output, the vector shapes can blend with other elements inside a composite.

### Inputs

The Background node carries a single input, meant for an Effect Mask input. Input1: [orange, required] Here you wire in the output of your last shape node. The sRender node hands back a rendered bitmap image to composite into the remainder of your comp. Effect Mask: This optional blue effect mask input accepts a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps originating in other tools. A mask wired here restricts the shown area to just the pixels sitting within the mask.

### Basic Node Setup

The sRender node always sits at the tail of a chain of Shape nodes. Its output ties into other 2D nodes such as a Soft Glow node.

Several Shape nodes feeding the sRender node, which then processes and composites them alongside a title Inspector

### The sRender Image tab

### Image Tab

The controls within this tab set the resolution, color depth, and pixel aspect of the image the sRender node produces. Process Mode Use this menu control to pick the Fields Processing mode Fusion applies when rendering the resulting image. The default Full Frames option fits progressive formats. Width/Height This pair of controls set the Width and Height dimensions of the image the sRender node will create. Pixel Aspect This control specifies the Pixel Aspect ratio of the created images. A 1:1 aspect ratio would yield a square pixel sharing the same dimensions on both sides (like a computer display monitor), while a 0.9:1 aspect would yield a faintly rectangular pixel (like an NTSC monitor).

NOTE: Right-click on the Width, Height, or Pixel Aspect controls to bring up a menu listing the file formats set in the preferences Frame Format tab. Picking any of the listed options sets the width, height, and pixel aspect to that format's values accordingly. Auto Resolution With this checkbox selected, the width, height, and pixel aspect of the node's image lock to the values set in the composition's Frame Format preferences. Should the Frame Format preferences shift, the resolution of the node's image shifts to match. Switching this option off can help you build a composition at a resolution different from the eventual target resolution of the final render. Depth The Depth button array sets the pixel color depth of the image the Creator node produces. While 32-bit pixels demand 4X the memory of 8-bit pixels, they deliver far greater color accuracy. Float pixels permit high dynamic range values beyond the usual 0..1 range, representing colors brighter than white or darker than black. Source Color Space The Source Color Space menu is where you declare the footage's Color Space to support a linear workflow. This carries out no actual color space conversion the way the Gamut tool would; rather, it tucks the source space data into the metadata wherever that metadata is absent. Further down the chain, the metadata can feed a Gamut tool through the From Image option, or a Saver, provided explicit output spaces are set there. Two options stand available:

- Auto: On its own, reads and forwards whatever metadata the image might carry.
- Space: Brings up a Color Space Type menu for picking the image's

correct color space. Source Gamma Space By way of the Curve Type menu, you declare the footage's Gamma Space and may decide to remove it through the Remove Curve check box during a linear workflow. Three choices sit in the Curve Type menu

- Auto: By itself, reads and forwards any metadata the image holds.
- Space: Brings up a Gamma Space Type menu for picking the image's

correct gamma curve.

- Log: Brings up the Log/Lin settings, similar to the Cineon tool.

To dig deeper, consult Chapter 99, “Film Nodes,” within the DaVinci Resolve Reference Manual, or Chapter 39 of the Fusion Reference Manual. Remove Curve Based on the chosen Gamma Space, or the one detected under Auto mode, the Gamma Curve gets pulled off the material, or a log-lin conversion is applied, in effect rendering it a linear output space.

### Common Controls

Settings Tab The Settings tab in the Inspector is shared across every Shape node. Those common controls get a full treatment at this chapter's close in the “The Common Controls” section.

### sStar

### The sStar node

The sStar node serves to build multi-point star shapes. As with nearly every Shape node, the sStar node's output is only viewable through a sRender node.
