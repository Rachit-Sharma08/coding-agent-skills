# Controlling premultiplication with alpha divide and alpha multiply and multi channel compositing

Version: DaVinci Resolve 20.3 Reference Manual. Context: Understanding image channels.
[Chapter index](INDEX.md) / [Previous section](premultiplication-rules.md) / [Next section](displaying-channels-in-the-viewer.md)
<a id="source-aux-channel-setup"></a> <a id="source-beauty-pass-setup"></a> <a id="source-commonly-used-beauty-passes-compared"></a> <a id="source-compositing-multiple-beauty-passes-in-the-node-editor"></a> <a id="source-compositing-with-beauty-passes"></a> <a id="source-controlling-premultiplication-with-alpha-divide-and-alpha-multiply"></a> <a id="source-embedding-alpha-into-beauty-passes"></a> <a id="source-multi-channel-compositing"></a> <a id="source-working-with-auxiliary-channels"></a>

### Controlling Premultiplication With Alpha Divide and Alpha Multiply

The Alpha Divide and Alpha Multiply nodes, sitting in the Matte category of the Effects Library, come into play when several operations in succession expect a “straight” alpha channel. Rather than repeating Pre-Divide/Post Multiply operations on every node, you can deploy these two nodes to bracket the rest. Just drop in the Alpha Divide node when you want the RGBA image data left non-premultiplied, and drop in the Alpha Multiply node when you want the image data premultiplied once more. As an example, when you rely on third-party OFX nodes that perform color adjustments, you might have to govern premultiplication by hand both before and after such an adjustment.

A node tree with explicit Alpha Divide and Alpha Multiply nodes

### Multi Channel Compositing

If you have headed to the cinema for any recent superhero movie, you will have witnessed the fruits of advanced 3D rendering paired with a great deal of compositing. 3D applications can produce strikingly realistic images, but the time needed to render each frame of those realistic images runs into hours rather than minutes. Any tweak to the 3D images — even fairly basic moves such as color adjustments, focus changes, filtering, or extra masking — forces a full re-render of those images, which leaves you waiting, frequently again and again. For the sake of efficiency, it is far quicker to make iterative changes achievable through 2D image processing operations in Fusion instead. So that you keep the freedom to make routine after-the-fact changes to 3D images, the assorted attributes making up the 3D scene get split apart and rendered as separate image sequences, commonly called render passes. As an example, render passes are routinely produced for attributes such as raw color, shadows, and reflections, which can then be reassembled as a 2D composite to deliver the finished result. Rendering different attributes into different image sequences hands you a great deal of flexibility, since each image attribute can now be color corrected, blurred, or otherwise processed apart from the image's other attributes, using fast-processing operations in Fusion. The render passes most commonly produced come out of the 3D scene's RGBA channels. Together these are called beauty passes and may take in attributes like color, shadows, lighting, reflections, environment, and more. Render passes can likewise hold non-RGB data. Across effects applications these passes carry assorted names — among them Data Channels, or AOVs (Arbitrary Output Variables). Within Fusion these channels are termed Auxiliary Channels, and the 3D data they hold runs to things like Depth, Normals, Motion Vectors, and UV Coordinates (these being just a handful). When you composite a 3D render made up of several render passes, the beauty passes get handled one way while the Auxiliary Channels get handled another. Because Fusion nodes carry RGBA channels by default, beauty passes come first here, with how to handle Auxiliary Channels explained later in this chapter.

### Compositing with Beauty Passes

Every attribute of a beauty pass can be rendered into its own image sequences, so you wind up with a numbered run of images: a diffuse pass here, a reflection pass there, a shadow pass alongside them, and so on. As an alternative, all the passes can live inside a multi-part EXR image sequence. Multi-part EXRs have the upside of demanding slightly less file management, though Fusion handles the passes much the same whichever method you choose.

One MediaIn or Loader node deals with only a single beauty pass, since just one set of RGBA channels comes out of each node. Building your composite in Fusion therefore calls for a separate MediaIn or Loader node per pass.

A MediaIn or Loader node is needed for each beauty pass. TIP: Fusion's handling of the EXR format is optimized when several Loaders read the same EXR file. The file loads just once to reach all the channels.

### Beauty Pass Setup

Split-out components of 3D renders — diffusion, shadows, or reflections, for instance — can each be rendered on their own using RGB channels. When you are handed separate image sequences for every image component, they import and open in Fusion and can show in the viewer just like any other clip. When you work with multi-part EXR files, you essentially hold several RGB images bundled in one file. The MediaIn and Loader nodes, however, can only draw on one set of RGB channels at a time. To composite multiple RGB beauty passes with one another, you have to bring in several MediaIn or Loader nodes pointing at the same image sequence yet assigned to different passes held in the EXR file.

Several Loader or MediaIn nodes feeding off one multi-part EXR image sequence TIP: It pays to rename each Loader or MediaIn after the beauty pass it carries.

Mapping Each Set of Beauty Passes to a Particular Node Whether you sit on a MediaIn node or instead a Loader node, mapping beauty passes onto RGB channels happens through one of the Inspector's Image tab, Channels tab, or Format tab. On a Loader node, it is the Loader's Format tab that handles it.

Within a Loader node, beauty passes assigned across the red, green, and blue channels The MediaIn's Image tab carries a Layer menu. Any pass held in a multi-part EXR image sequence can be picked from this menu and assigned to the RGBA channels automatically.

Inside a MediaIn node, the Layer menu listing headings for the combined channel passes Most of the time the menu lists the combined channel passes, which means the separate red, green, blue, and alpha channels are not selectable. Since the alpha channel is missing from many beauty passes, now and then you must borrow the alpha channel from another beauty pass. That is why the Channels tab is frequently the better place for mapping a beauty pass's individual channels onto the MediaIn node's channels.

Reaching the individual channels is done through either the Channels tab on the MediaIn node or the Format tab on the Loader. That same channel mapping functionality lives in both the DaVinci Resolve MediaIn node and a Loader node's Format tab. Up at the tab's top, individual RGBA menus appear on the Channels tab as well as on the Format tab. These menus let you map the RGBA channels off any pass held in the multi-part EXR. To map the Ambient Occlusion pass onto the RGB channels, for instance, pick AO. R (Red) out of the Red channel menu; next set AO. G (Green) by way of the Green channel menu; then assign AO. B (Blue) using the Blue channel menu. Within the MediaIn node, a pass' individual channels assigned across the red, green, blue, and alpha channels TIP: Beauty passes get labeled differently from one 3D application to the next. For example, an Ambient Occlusion beauty pass might be named AO, AM_OCC, or some other abbreviation. No alpha channel comes with the Ambient Occlusion beauty pass. To composite it, the alpha channel pass from another beauty pass can be reused. In the image below, the alpha channel is drawn from the combined render pass' alpha channel.

An alpha channel borrowed from another beauty pass joined onto the Ambient Occlusion pass

TIP: With the Format tab in the Loader node, the checkbox beside each channel has to be switched on for that channel to surface in the node's output.

### Compositing Multiple Beauty Passes in the Node Editor

After all your passes are imported and mapped to RGBA channels, you will be left with a string of MediaIn or Loader nodes. Just how many MediaIn and Loader nodes really comes down to your workflow. No fixed count of passes is set in stone. Each studio settles on its own standard set. Even so, certain render passes turn up in the majority of composites. What follows is a roster of commonly used render passes alongside their generic names.

### Commonly used beauty passes, compared

Compositing several beauty passes down to one output image is fairly painless. 3D rendering applications generally put out linear gamma, so no Gamut or other color space conversion nodes are needed provided you keep the image in a linear color space for easy compositing. The core compositing gets done with either a Merge node or a Channels Booleans node. Both support additively combining render passes. There is no hard requirement to composite each pass any particular way, though in most cases a plain additive composite ought to do fine. To start compositing render passes by way of a Merge node: 1 Feed a Color pass into a Merge node's background input. 2 Feed a Direct Lighting pass into the foreground input. 3 Tune the Alpha gain and Blend parameters until the look suits you.

The first move in compositing beauty passes is wiring a background and a foreground into a Merge node Should you rather, the same composite can be built with a Channels Booleans node. In that case nothing technical separates the two nodes. To composite render passes via a Channels Booleans node: 1 Feed a Color pass into a Channels Booleans node's background input. 2 Send a Direct Light pass to the foreground input. 3 Out of the Operations menu, pick Add 4 Out of the Alpha To menu, pick Do Nothing.

Here Channel Booleans sits on Add, blending the foreground input with the background input. Shadow passes — Ambient Occlusion among them — count as exceptions to the steps above. For those, a multiply Apply mode is the customary pick. To composite an Ambient Occlusion render pass via a Merge node: 1 Wire the last in a chain of Merge node render passes into a Merge node's background input. 2 Send an Ambient Occlusion pass to the foreground input. 3 Out of the Apply Mode menu, pick Multiply. 4 Tune the Gain and Blend parameters until the look suits you. Simple as that may sound, compositing by a fixed recipe does not pan out for every shot. With different images, you may have to try out various compositing techniques to land the best results.

### Embedding Alpha into Beauty Passes

Not every beauty pass carries an alpha channel. When a shot calls for laying your assembled beauty passes over live-action or some other backdrop, supplying the alpha channel from a pass that does carry one may fall to you. To work an alpha channel into your assembled beauty pass composite, proceed as follows: 1 Wire the final Merge or Channel Booleans output into a Matte Control node's background input. 2 Wire the render pass holding the alpha into the green Foreground input on the Matte Control node. 3 Over in the Matte Control's Inspector, pick Combine Alpha from the Combine menu. 4 Out of the Combine Op menu, pick Copy.

The color pass' alpha channel restored into the finished beauty pass node tree TIP: Alpha channels off 3D renderings tend to be premultiplied. With that in mind, make sure the Pre Divide/Post Multiply checkbox is switched on for any node doing color correction. If more than one node in a row handles color correction, reach for the Alpha Divide and Alpha Mult nodes instead.

### Working with Auxiliary Channels

Auxiliary channels are not RGB images; rather they form a family of special-purpose 3D image data that generally conveys position, orientation, and object information for use in 2D composites. As an example, Z-Depth channels record how deep each pixel of an image sits along a Z-axis, while an XYZ Normals channel records the orientation (facing up, facing down, facing left or right) of every pixel in an image. As with the use of multiple beauty passes, one of the chief motives for using auxiliary data is to do away with re-rendering computationally costly 3D imagery, by letting still more facets of rendered images be manipulated after-the-fact. Since 3D rendering is computationally costly and slow, putting out descriptive information about a 3D image permits refined alterations to take place in 2D compositing, which is quicker to do and to adjust. Auxiliary channel data can be obtained in two ways:

- First, auxiliary data can be embedded inside a clip rendered out of a 3D application, most often through the EXR file format. In that case, your best bet is to check your 3D application's documentation to learn which auxiliary channels it can produce and output.
- Auxiliary channel data can also be had by producing it inside Fusion through 3D operations — those put out by the Renderer 3D node, those from the Optical Flow node, or those from the Disparity node.

An RGBA 3D rendered scene that also contains auxiliary channels TIP: While hunting for information on auxiliary channels in other software, bear in mind that some 3D applications call auxiliary channels Arbitrary Output Variables (AOVs), render elements, or secondaries.

### Aux Channel Setup

With a MediaIn or Loader node tied to a multi-part EXR file holding auxiliary channel data, the Inspector's Channels or Format tab carries a pre-defined set of auxiliary channels meant for mapping. Each pre-defined channel comes with a menu listing every attribute held in a multi-part EXR. From that menu you pick the render pass to assign to the matching channel. As covered earlier, RGB beauty passes such as diffuse, shadow, and reflection get mapped onto the red, green, and blue channels. Auxiliary passes arrive with preset mappings.

Inside a MediaIn node, a multi-part EXR file whose embedded render passes are assigned to their aux channels
