# Transform controls in the merge node and final composite

Version: DaVinci Resolve 20.3 Reference Manual. Context: Compositing layers in Fusion.
[Chapter index](INDEX.md) / [Previous section](composite-edge-repair-and-merge-modes.md) / [Next section](dealing-with-spill-and-masking-a-graphic.md)
<a id="source-building-a-simple-green-screen-composite"></a> <a id="source-compositing-layers-in-fusion-part-2"></a> <a id="source-mapping-timeline-layers-to-nodes-in-fusion"></a> <a id="source-pulling-a-green-screen-key-using-the-delta-keyer"></a> <a id="source-the-final-composite"></a> <a id="source-using-transform-controls-in-the-merge-node"></a>

### Using Transform Controls in the Merge Node

Living in the Inspector, the Merge node carries a group of transform parameters that act specifically on the foreground input's image. That makes it fast and simple to nudge a foreground image into alignment with the background without bringing in another node.

The Merge node's transform controls, which act upon the foreground input's image NOTE: Should you feed two differently sized images into a Merge node, it's the background image's resolution that sets the node's output resolution. Bear that in mind whenever resolution problems crop up. The Size slider is there to scale the foreground.

### The final composite

### Building a Simple Green-Screen Composite

Pushing compositing one notch further, the upcoming example demonstrates how a multilayered Timeline—like the kind found on DaVinci Resolve's Edit page—maps onto nodes within Fusion's node tree. We'll lean on DaVinci Resolve here, but grasping how layers translate into nodes can help anybody just getting comfortable with a node-based interface. For this example we'll put together a simple composite from a green-screen key plus two additional layers to build a news story.

### Mapping Timeline Layers to Nodes in Fusion

Three layers within a Timeline make up this composite. Within that Timeline sit a background graphic riding video track 1, a green-screen clip riding video track 2, plus a foreground graphic riding video track 3.

The background riding video track 1 (top left), the green-screen clip riding video track 2 (bottom), and the graphic file riding video track 3 (top right) Built into any timeline-based system is the idea that video tracks with higher numbers sit more toward the front—nearer the viewer. Video track 1 acts as the background beneath all the rest. Video track 3 lies ahead of video track 1 as well as video track 2. TIP: Working in DaVinci Resolve, you're able to carry all three layers off the Edit page and into Fusion by turning them into a Fusion clip. To read more about building Fusion Clips, consult Chapter 65, "Getting Clips into Fusion." within the DaVinci Resolve Reference Manual, or else Chapter 3 of the Fusion Reference Manual.

A pile of clips destined for a composite (previous page), and that pile being converted into a Fusion clip on DaVinci Resolve's Edit page (above) Over in Fusion, every video clip stands for a MediaIn on the Fusion page or a Loader in Fusion Studio. In the example down below, the MediaIn2 corresponds to video track 2, and MediaIn 1 corresponds to video track 1. Those two pieces get composited through a Merge node (foreground laid over background, in that order). The combined output of that pair becomes the first Merge node's output, which in turn feeds in as the background to a second Merge. Chaining Merges one after another costs you nothing in quality and involves no precomposing. MediaIn3 stands for video track 3 and serves as the ultimate foreground in the tree, being the layer on top.

The starting node tree formed from the three clips we converted into a Fusion clip Now that this node tree has been built to echo the video layers, we can spend the remainder of the example adding whatever nodes each branch of the tree requires to produce the green-screen composite.

### Pulling a Green-Screen Key Using the Delta Keyer

For this composite you have to generate transparency behind the newscaster. As you work inside a node tree, you'll grow used to shifting existing nodes aside to clear room for new ones. Frequently you'll slide nodes off to one side or up overhead to open up space for the extra nodes.

Opening up room past the MediaIn nodes and picking the second of them, getting ready to drop in a node Green-screen keying's primary tool is the DeltaKeyer node. It hooks onto the output of whichever node stands in for the green screen—here that's the MediaIn2 node. With MediaIn2 selected, hit Shift-Space to bring up the Select Tool dialog, where any node can be searched for and inserted. Down below we've placed the DeltaKeyer right after the MediaIn2 node but ahead of the merge with the background.

Adding a DeltaKeyer node inline after the MediaIn2 node As a keyer the DeltaKeyer node is quite advanced, able to deliver striking results by blending various sorts of mattes alongside a clean-plate layer, yet it can also be driven very simply provided the background needing the key is well lit. And once the DeltaKeyer has pulled a key, it bakes the resulting alpha channel right into its output, so for this simple scenario it's the lone node we have to add. It's also worth pointing out that even though we're using the DeltaKeyer on a green screen, it isn't confined to keying only green or blue; the DeltaKeyer can pull striking keys off any color in your image.

Dragging the Eyedropper to the viewer samples the screen color

Having selected the DeltaKeyer, we'll turn to the Inspector controls and extract our key by briefly sampling the green tone out of the image's background. Pull a key from the green-screen color by dragging the Eyedropper out of the Inspector and over the screen color shown in the viewer. While you drag across the viewer, a read-out of whatever color the Eyedropper is currently sitting on shows up in a floating tooltip, hinting at the actual hue you are about to grab. At the same time, with the Merge displayed in a second viewer, we see an instant preview of both the transparency and the image we wired into the background.

At left, the untouched image; at right, the result once the green screen has been sampled with the Eyedropper from the Inspector. Once the preview looks right, letting go of the pointer button locks in the sample, and the Inspector controls refresh to show the value we picked.

At left, the DeltaKeyer Inspector refreshing to show the sampled color; at right, the DeltaKeyer loaded into the viewer with the Color button clicked so the alpha channel it generates is visible. However strong the composite appears, after you have chosen the screen color for the key you still have to load the DeltaKeyer node directly into the viewer. Doing so lets you judge how clean or dense the alpha channel produced by the key actually is. At the top of the viewer, hit the Color button on the viewer toolbar, or click inside the viewer and tap C, to flip the viewer back and forth between the image's RGB color channels and the alpha channel. In a matte, black stands for the see-through regions and white for the solid ones. The gray zones stand for partial transparency. Apart from cases involving glass, smoke, or fog, the majority of mattes ought to be solid white and solid black with no gray gray areas at all. Should a careful look at the alpha channel turn up some fringing around the white foreground of the mask, the DeltaKeyer comes with built-in controls for cleaning up the key afterward and tightening the matte. Here is a short rundown of the main tweaks worth making.

Once you have made the screen pick with the Eyedropper, work through the adjustments below to refine the key.

- Push the Gain slider up to intensify the screen color so it turns more transparent. Because this can also eat into the foreground's transparency, use a light touch.
- Use the Balance slider to bias the foreground toward one of the two colors that aren't the screen. With a green screen, that leans the foreground more to red or blue and alters how transparency falls across it.

Selecting the third tab among the seven control tabs in the DeltaKeyer Inspector reveals an assortment of controls for working the matte. Your first tweaks in the matte tab might cover these parameters:

- Move the lower and upper thresholds to build up density across the black and the white regions.
- With a very light hand, work the Clean Foreground and Clean Background sliders to plug tiny gaps in the

black and white matte. Pushing these parameters higher makes the edges of your matte progressively harsher. Tweaking the Clean Foreground slider within the DeltaKeyer's Matte panel: here, nudging the Clean Foreground slider up slightly clears out the inner fringing we want gone, while leaving the key's edges essentially intact.

At left, the key as it started; at right, the same key once the Clean Foreground slider has been applied

That done, the key satisfies us, so we drop the Merge1 node back into the viewer and tap C to return the viewer's Color control to RGB. The background graphic is now visible, though at the moment it is too small to fill the entire frame, which calls for one more adjustment.

The key itself is now solid; the background is what still needs attention
