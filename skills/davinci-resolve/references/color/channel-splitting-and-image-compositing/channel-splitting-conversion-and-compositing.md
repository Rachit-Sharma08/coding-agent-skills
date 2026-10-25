# Channel splitting conversion and compositing

Version: DaVinci Resolve 20.3 Reference Manual. Context: Channel splitting and image compositing.
[Chapter index](INDEX.md) / [Next section](green-screen-compositing-and-transparency-mattes.md)
<a id="source-a-note-about-red-hdrx-media-and-performance"></a> <a id="source-channel-splitting-and-image-compositing"></a> <a id="source-channel-splitting-and-image-compositing-1"></a> <a id="source-enabling-disabling-and-converting-node-channels"></a> <a id="source-final-node-display-with-isolations"></a> <a id="source-introduction-to-compositing-using-the-alpha-output"></a> <a id="source-isolating-splitting-and-converting-color-channels"></a> <a id="source-multi-channel-red-hdrx-support"></a> <a id="source-splitting-channels-with-the-splittercombiner-nodes"></a> <a id="source-the-resulting-channel-split-effect"></a> <a id="source-the-splitter-combiner-node-structure"></a> <a id="source-using-a-qualifier-key-to-create-transparency"></a>

### Channel Splitting and Image Compositing

This chapter opens with node arrangements that let you single out, break apart, convert, and reassemble a clip's image channels in a variety of ways, including how to put to use the extra image channels carried by certain media formats. The chapter's latter half turns to compositing performed directly within the Color page, covering how to bring in external mattes for a composite and how to lean on qualifier keys for green- and blue-screen work against other layers sitting in the Timeline.

### Isolating, Splitting, and Converting Color Channels

DaVinci Resolve offers a pair of approaches for adjustments that target specific channels, the right one hinging on whether you're tweaking only a single channel inside one node or applying distinct corrections to all three channels spread across multiple nodes.

### Enabling, Disabling, and Converting Node Channels

Each node in the Node Editor carries a contextual menu that holds a set of four options:

A widened set of options for picking a node's image-processing color space and gamma, plus for switching channels off Although shifting a given node's operations away from the RGB default into another color space has been possible for a great many releases, the roster of selectable color spaces grew considerably in DaVinci Resolve 15 (every earlier choice, Lab (CIE), HSL, and YUV among them, remains on offer). On top of that, you can pick the gamma a node operates in, drawing from an equally lengthy menu. Picking a per-node color space and gamma won't reshape the image on its own, unlike what the Color Space Transform ResolveFX plugin does. Rather, swapping a node's color space and gamma changes which kind of image channels its red, green, and blue controls touch, along with how that node's corrections get applied. As an instance, this means you can perform a temperature shift while a node's gamma is set to Linear, which now and then turns out to be mathematically advantageous. There are also three checked Enable Channel 1–3 options that switch individual channels on or off, narrowing down which channel a node's adjustments genuinely reach. The next example demonstrates these capabilities by sharpening only the Y' (luma) of a picture while sparing the chroma, an effect that tends to be gentler than sharpening the whole frame at once.

To rely on channel disabling plus color space conversion for luma-only sharpening: 1 Add a node where you'll apply the sharpening you want to the current clip. 2 Right-click that fresh node and pick YUV from the contextual menu's Color Space submenu. 3 Carry out the sharpening with either of these routes: From the node's contextual menu, clear Enable Channel 2 and Enable Channel 3, the ones matching the U (Cb) and V (Cr) channels, so that only Channel 1 (Y) stays active. After that, bring up the Blur palette and pull the ganged Radius sliders downward to sharpen the Y channel. As an alternative, open the Blur palette, ungang the Radius sliders, and drag just the red slider down to sharpen the Y channel, because any control sporting three gangable sliders automatically maps them onto whichever channels belong to the Color Space currently in force.

(Before) The unaltered frame, (After) Sharpening confined to the picture's Y’ channel alone Note here that even when the Blur palette normally hands you independent R, G, and B controls you can ungang from one another, the Color Space submenu makes it possible to sharpen according to the channel definitions of other colorspaces, opening up plenty more corrective and creative avenues from the very same controls.

### Splitting Channels with the Splitter/Combiner Nodes

A second way to correct individual color channels relies on the Splitter/Combiner nodes, which peel the Red, Green, and Blue channels into their own node tree branches, each branch able to host any number of serial and parallel image-adjustment nodes. You can put a Splitter/Combiner node structure together in two fashions. Methods of adding Splitter/Combiner nodes:

- For the ready-made route: from the menus pick Color > Nodes > Add Splitter/ Combiner Nodes (Option-Y). Up pop a Splitter node and a Combiner node, both already wired to three Corrector nodes, one per color channel.
- To manually construct a Splitter/Combiner node structure: Right-click any blank spot in the Node Editor and use the Add Node submenu to drop in a Splitter node, a Combiner node, and three Corrector nodes, then link them up however the effect you're after demands.

### The Splitter Combiner node structure

An incoming image enters the Splitter node, which then hands out a separate output per color channel (top/red, middle/green, bottom/blue). Hooking each of those outputs to a Corrector node causes that one color channel to feed all three of the node's internal channels, so the structure's default trio of nodes ends up internally crunching red/red/red, green/green/green, blue/blue/blue. The Combiner afterward extracts the Red, Green, and Blue channels from every node tied to its three inputs and stitches them back into one RGB image. Naturally, whatever you do between the Splitter and the Combiner is completely your call. Among the easiest ways to demonstrate what this structure can do is pairing it with Node Sizing from the Sizing palette. With Node Sizing you can fix channels that drifted out of register in old archived footage, or deliberately misalign channels for a stylistic look. The example that follows applies one modest Node Sizing tweak to a split Blue channel and yields a striking “prism vignette” result.

To apply Node Sizing to individually split channels: 1 Choose Nodes > Add Splitter/Combiner Node (or hit Option-Y) so a premade Splitter/ Combiner node structure drops into the Node Editor. 2 Pick the middle Corrector node of the three that sit between the Splitter and the Combiner (Node 5 in the screenshot below). 3 Bring up the Sizing palette, set the Mode drop-down to Node Sizing, then nudge the zoom parameter upward by a touch; here the figure is 1.014.

Zooming just one color channel using the Splitter/Combiner nodes The screenshot shows that only the Green channel got zoomed in over the whole frame, something achievable solely through Node Sizing. It looks neat, yet it isn't quite the result you're after. 4 Open the Window palette, drop in a Circular window, switch on its Invert control, and reshape it into a very soft vignette aligned along the horizontal. Doing so confines the per-channel scaling of the Green channel to nothing but the image's outer rim, much as an overly aberrant lens would.

### The resulting channel split effect

Nothing stops you from pressing further, dialing in different zoom amounts and window shapes on each of the remaining color channels, maybe layering in a bit of blur to push the look, but even this single example conveys the creative range this technique opens up.

### Multi-Channel RED HDRx Support

The RED EPIC, SCARLET, DRAGON, and WEAPON cameras can all record in an HDR mode that essentially “brackets” a pair of separate exposures for every frame. What you get back holds two channels of picture data: the standard exposure plus a “highlight exposure” that's pulled down by an amount you choose (+3, +4, +5, or +6 ƒ-stops difference). Out of the box, the node graph's Input bar routes the standard exposure into your grade's node tree. If you want to draw on that extra “highlight” exposure, you can attach one more Source input to the node graph so it supplies a second image-data stream you're free to combine with the standard exposure however you like. NOTE: Another route to the highlight exposure of RED HDRx media is to switch on and tune the Magic Motion controls over in the Camera Raw palette. To build a node tree that blends the normal and highlight HDR versions: 1 Working on the very first default node (Node 1), grade the image to judge whether the alternate exposure is even something you'll need. For this walkthrough we'll suppose it is. Here the default exposure's sky is rather blown out, yet the highlight exposure may hold detail you can recover.

Using HDRx images with the Layer Mixer 2 Make a Layer Mixer node by picking Nodes > Add Layer (Option-L). That spawns two nodes: a Layer Mixer node placed after Node 1, plus a third node (Node 3) wired to a second RGB input of the Layer Mixer node running parallel to Node 1.

For the moment the Source delivers two inputs, yet you're able to attach a second source, namely the short exposure held in the HDR image

3 Right-click any spot inside the node graph (just not on a node) and pick Add Source from the contextual menu. A second Source input shows up beneath the first one, and it emits the image's highlight exposure as its own separate stream.

A node tree where a Layer Mixer node blends a pair of Corrector nodes, each wired to its own output for the standard and highlight exposures 4 Remove the link running from the top Source input to Node 3, then wire the bottom Source input into Node 3's RGB input. Right away the node thumbnail and the Viewer refresh to display the darker, underexposed take on the HDR image, simply because the Layer Mixer defaults to laying 100% of Node 3 on top of Node 1. 5 Pick Node 3 and follow either of the two procedures below to build a worthwhile blend of the two exposures: For a blend of both exposures, open the Key tab and slide the Key Output Gain slider down to trim how much Node 3 feeds the final image. Paired with dynamics (keyframing), this works nicely for animating a dissolve from the standard exposure into the highlight exposure when a single take moves from a dim setting into a bright one and you'd like a seamless handoff between the two exposures.

Cross-dissolving the standard and highlight exposures of RED HDRx footage by way of the Key Output Gain slider on a Corrector node tied into a Layer Mixer node TIP: The Blend Type and Blend Bias parameters in the Camera Raw palette offer another way to merge the two exposures without assembling a purpose-built node tree. When you want the highlight exposure to selectively restore detail (recovering blown-out windows, say), reach for a Power Window, HSL Qualification, or both together to fence off the region you mean to recover in Node 3. (Take care when blending both exposures via HSL Qualification, since keyed edges can be awkward to feather together.)

Fencing off an image region to swap in using the highlight exposure frame of a RED HDRx clip

### Final node display with isolations

### A Note About RED HDRx Media and Performance

Because RED HDRx media holds two full streams of picture data, DaVinci Resolve has to decode a pair of distinct tracks at once any time you tack on a second Source input. (Skip that second Source input and only the first stream gets decoded.) As a result, no matter whether your machine's CPU or GPU is handling the RED media, you'll see roughly half the throughput while the highlight stream of an HDR clip is in play. One remedy is to switch on the Smart Cache via Playback > Render Cache > Smart, which on its own caches every raw source clip into whatever codec is presently chosen under the Render Cache Format parameter of the Master Settings panel within the Project Settings. You could instead turn on the User Cache and cache each HDRx clip by hand, right-clicking it and selecting Render Cache Fusion Output > On. DaVinci Resolve does its cache rendering while you sit paused, so the next playback of a cached clip runs at full speed. Anyone working with RED HDRx media on a regular basis is well advised to fit several high-end GPU cards for the best decoding throughput.

### Introduction to Compositing Using the Alpha Output

DaVinci Resolve is happy to use the alpha channel that ships with imported media for compositing, but the Alpha Output in the Node Editor is a separate, optional output you can switch on to generate clip transparency through operations performed inside DaVinci Resolve, letting you composite over other clips that sit on lower video tracks. The Alpha Output lends itself to many uses, though this section narrows in on three examples.

### Using a Qualifier Key to Create Transparency

For this opening example, the Alpha Output serves to composite a green screen clip on top of a background plate.
