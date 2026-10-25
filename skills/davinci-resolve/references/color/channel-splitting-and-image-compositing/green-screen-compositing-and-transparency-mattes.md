# A green screen clip ready for compositing and a matte to create transparency

Version: DaVinci Resolve 20.3 Reference Manual. Context: Channel splitting and image compositing.
[Chapter index](INDEX.md) / [Previous section](channel-splitting-conversion-and-compositing.md)
<a id="source-a-green-screen-clip-ready-for-compositing"></a> <a id="source-choosing-a-composite-mode-for-the-corrector-node"></a> <a id="source-setting-the-composite-mode-in-a-corrector-node"></a> <a id="source-using-a-matte-to-create-transparency"></a> <a id="source-using-ofx-alpha-channels-legacy"></a>

### A green screen clip, ready for compositing

To set this composite up, the background plate lives on track V1 of the Timeline while the green screen clip rides above it on track V2.

A green screen clip layered onto the Timeline's track V2, sitting over a background plate down on track V1 and set for compositing

To build a chroma-key composite within the Color page: 1 Right-click any point in the Node Editor's gray area and pick Add Alpha Output, which places the Alpha Output along the right side of the node graph. The Alpha Output turns up beneath the Node Tree output at the Node Editor's right edge.

The image Node Tree output with Alpha Output below 2 Lean on Node 1 to color correct the picture and prime it for keying. Here the foreground plate is log-encoded, so a LUT goes onto Node 1 to normalize it. 3 Place a Serial node after Node 1 and run its key output into the Alpha Output. That's a quick path to this composite provided you trust that the work done in Node 1 won't harm the key (or you know it'll actually help by stretching the contrast of a flat-contrast source clip). As another option, you can spin up a second processing branch by dropping in a disconnected node (Node 2), feeding the Source node into its RGB input, and then routing its key output to the Alpha Output you just made. Setting up a second image processing branch as the source of your key lets you key straight off the source (granted the source is keyable as-is), sidestepping any trouble that grading the first node might inflict on the key.

Node 1 grades the clip, stretching contrast to better the picture as well as its keyability. Node 2 then employs Qualifier controls to extract the key. 4 Using Node 2 and its Qualifier controls, key out the green backdrop, then switch on the Invert checkbox so the composite comes together correctly. For this example we're working in 3D Qualifier mode to draw a high-quality key.

An HSL Qualification keying out the green and feeding the Alpha Output so transparency results 5 Should green spill linger in the composite (or blue when your key is on a bluescreen), switch on the Despill checkbox to clear it. 6 A Power Window also lets you garbage matte away anything you don't want creeping into the frame, calling on the Tracker palette where needed so the window rides along with the foreground subject's motion.

A PowerCurve used to garbage matte out unkeyable lighting fixtures

7 When it's warranted, hang another node off the output of Node 2 to make whatever fixes the background plate clip needs so the composite knits together more cleanly. With that extra node selected, for instance, you might right-click the background clip and pick “Shot Match to This Clip” so DaVinci Resolve's automatic shot matching brings the foreground into line with the background.

Adding more color adjustments to a node added after the qualifier Once everything is in place you're left with a tidy green screen composite that displays across both the Color and Edit pages.

The outcome, where a window garbage matte trims away the gear, awaiting any further polish

### Using a Matte to Create Transparency

When someone hands you a standalone Matte clip that spells out a clip's transparency, you can fold that Matte clip into the node tree of a superimposed clip to assemble a composite by way of the Alpha Output. To assemble a composite from an external matte: 1 To tie an external matte to a clip, open the Media page, pick the clip you'd like to attach a matte to in the Media Pool, browse to the matte file through the Library browser, then right‑click that matte file and pick Add as Matte. To read more about importing mattes, see Chapter 146, “Combining Keys and Using Mattes.” 2 Move over to the Color page and click the foreground clip up in the Thumbnail timeline; now right-click Node 1 inside the Node Editor and, from its Add Matte submenu, choose the matte you brought in. Below Node 1 an EXT MATTE node appears, with the first among its four key outputs running into the key input of Node 1. (Handling external mattes gets fuller treatment in an earlier portion of this chapter.) 3 At this point, right-click any spot in the node graph (anywhere but a node) and pick Add Alpha Output from the contextual menu. An Alpha output appears below the Node Tree output. 4 Pull a connection line out of the EXT MATTE node's second key output and into the Alpha output.

Using an external matte in the grade and to the Alpha output A working composite should now be visible, the external matte opening up a transparent region in the foreground clip that lets the background clip peek through.

The final composite shown before and after, produced by linking an EXT MATTE node into the node graph's Alpha output

### Setting the Composite Mode in a Corrector Node

Whenever you're compositing in the Color page through the Alpha output, every corrector node can be given its own composite mode. Right-click the node and choose Composite Mode from the contextual menu. From there you can switch that node's composite type to any of the composite modes built into DaVinci Resolve.

### Choosing a Composite mode for the Corrector node

### Using OFX Alpha Channels (Legacy)

With every effect now running on standard color corrector nodes, the OFX Alpha is on hand at all times and needs no manual menu toggling. From DaVinci Resolve 18.5 onward, reaching an OFX Alpha takes no further action on your part. That said, an OFX Alpha menu carrying two choices still exists for older projects. Enable: Switched on by default. Clear it and any Alpha the effect produces gets disregarded entirely. Quite why anyone would craft an effect that makes an Alpha channel only to throw it away outright is anyone's guess, yet the toggle is provided in case your work is unusually odd and convoluted. Honestly, just leave it on. Use For Mixing: Switched on by default. Uncheck it and the node performs no Alpha mixing whatsoever. Power Windows and Keys quit functioning, and the node acts like an old-style FX node. Whatever Alpha is produced still gets output; it merely no longer constrains where the effect takes hold.

Taking over from the old Use OFX Alpha option is the OFX Alpha menu. Barring a genuinely compelling reason to do otherwise, leave both Enable and Use for Mixing checked.
