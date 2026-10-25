# Introduction to manipulating and combining keys and outside nodes

Version: DaVinci Resolve 20.3 Reference Manual. Context: Combining keys and using mattes.
[Chapter index](INDEX.md) / [Next section](external-mattes-and-openexr-layer-extraction.md)
<a id="source-combining-keys-and-using-mattes"></a> <a id="source-combining-keys-and-using-mattes-part-1"></a> <a id="source-connecting-key-outputs-to-rgb-inputs-and-vice-versa"></a> <a id="source-feeding-keys-from-one-node-to-another"></a> <a id="source-introduction-to-manipulating-and-combining-keys"></a> <a id="source-outside-nodes"></a> <a id="source-using-a-high-contrast-color-correction-as-a-key"></a> <a id="source-using-external-mattes"></a>

### Combining Keys and Using Mattes

A key is the literal image channel that assorted secondary operations build to single out particular regions of images for you to work on. These pages walk through the various ways to reshape and merge keys drawn from several nodes, or to pass keys along between nodes. They also lay out the various ways to put mattes imported from other applications to use, plus how the Key palette lets you reshape keys further in different ways.

### Introduction to Manipulating and Combining Keys

The key input and key output on each node let you steer key channel data from one node into another so that isolated corrections can be applied. On top of that, the Key Mixer lets you blend an assortment of keys from different nodes into richer keys for taking on intricate operations. This section walks through every way of recombining key data, plus how keys can pair with the Alpha output to carve out regions of transparency in a clip for compositing right inside DaVinci Resolve.

### Outside Nodes

Any time you reach for a Power Window or HSL Qualifier to confine a correction inside one node, a special node structure builds a second node for you automatically, the Outside node, which applies further adjustments to the inverse of the region you singled out in the prior node. An Outside node is really nothing more than a Corrector node with the Key Palette's Key Input Invert control switched on, making it simple to apply separate corrections to a separated subject and to its surroundings.

The Key palette's Key Input Invert button, which flips whatever key arrives at that node's Key Input Below, a Power Window has singled out the sky, and an Outside node has been tacked on to correct everything else in the shot.

The Outside node automatically has its key input inverted. To tack an Outside node onto a node, building a secondary correction: 1 Pick a node already confined by a Power Window or HSL Qualifier. 2 Do one of the following:

- Choose Nodes > Add Outside (Option-O).
- Right-click a node choose Add Outside Node.

A fresh node appears right after the one you selected, the first node's RGB and key outputs hooking up to the new node's automatically. Pick the new node and open the Key palette, and you'll spot the Key Input's Invert control switched on by default, which is what inverts the key coming from the prior node.

The Key Input Invert control is on by default for each node. Should you want, rather than letting the Outside node invert the incoming key, to copy the existing key so you can run another operation on that same separated region, you can switch the key input's Invert control off.

### Feeding Keys From One Node to Another

Among the Node Editor's most potent traits is the knack for generating keys off a specific spot in the node tree and piping the outcome into a wholly different correction elsewhere in that tree. That is part of why every Corrector node carries a separate key input and output. Whatever key arises when you reach for the HSL Qualifier, draw one or more windows, or apply an external matte can leave one node's key output and feed the key input of any other node in a tree. There are plenty of reasons to do so, but the example below illustrates a frequent problem this technique solves. Leaning on a key from one node to drive an adjustment over in a different node: 1 Have Node 1 lay down a basic primary correction, raising contrast and balancing the color toward a pleasing ambient color temperature. 2 Add a Serial node (Node 2), then a Layer Mixer node, which brings in Node 4 too (as the screenshots below show). After that, drain all saturation from Node 4 and pile on contrast for super-high-contrast black and white, knock back Node 2's saturation just slightly, and right-click the Layer Mixer node to pick the Overlay blend mode for combining the two layers.

A group of nodes to create a stylized image

What comes out is a strongly stylized image, yet the skin tone across the actor's face and hands in that result is too flat, and you want to bring some variation back to it. Just dropping in another node past the Layer Mixer and keying the skin tone may fall short, since the meager saturation makes a key tough to pull.

The resulting stylized image may be difficult to key accurately. 3 Drop in another node after the Layer Mixer (Node 5 in the screenshot), then right-click the gray background area of the Node Editor and pick Add Node > Corrector to spawn an unattached node, (Node 6). 4 Wire the RGB output of Node 1 into the RGB input of Node 6, then wire the key output of Node 6 into the key input of Node 5. Now you're set to pull a high-quality key off the very first correction in Node 1, sidestepping all the tangle that follows. 5 Reach for the HSL Qualifier in Node 6 to pull a solid, strong skin tone key off the primary image. With the node tree arranged this way, that key feeds Node 5 and will confine whatever adjustments you make there.

Pulling a key with Node 6 off the image Node 1 outputs, then routing that key into Node 5 6 Now you can adjust Node 5's grade, dropping the contrast, brightening, and boosting the saturation of the actor's skin tone.Thanks to this operation, the background stays desaturated and contrasty while the actor's skin tone takes on the brighter quality the shot calls for.

(Left) A whole clip carrying a high-contrast grade, (Right) The skin tone, by way of a key, graded apart from that high-contrast grade This example might have been tackled any number of ways, but the takeaway is that you can drop in nodes wired to the image's state at any spot in a node tree and lean on them to make keys for feeding any other node, no matter what's befalling the picture in between.

### Connecting Key Outputs to RGB Inputs, and Vice Versa

There is yet another route for reshaping a key from one node by means of another inside the Node Editor, and that is wiring the key output of one node into the RGB input of another node. Do that and you can lean on any of the second node's controls to reshape the key, then put the result to use by wiring the RGB output of that second node into the key input of a third node.

Wiring a key output into an RGB input so a second node's controls can tune the key In the node tree pictured above, Node 2 pulls a key, Node 4 reshapes the key, and Node 3 leans on the key to make a color adjustment. Remember that a key is nothing more than a grayscale image. Building a node structure like this opens up any of the second node's controls to you. Among the candidates are Custom Curves; the Noise Reduction or Motion Blur controls; Sharpen and Midtone Contrast; Lift/Gamma/Gain alongside Contrast; or the Log controls. Each can reshape the key in ways no Matte Finesse control could manage on its own.

This technique may be needless for run-of-the-mill color isolations, yet it proves quite handy when crafting tricky isolations on hard-to-key subjects, or when leaning on one of the Qualifier modes to pull a key for compositing transparency through the Node Editor's Alpha output. In that case, you can wire the RGB output of a node used for key manipulation straight into the Alpha output. Here, a key is pulled by Node 1, with the RGB feeding Node 3, which color corrects the foreground image. The key off Node 1 feeds the RGB of Node 2, which reshapes the key to tidy it up before it connects to the Alpha output block at the lower right of the Node Editor.

Wiring a key output into an RGB input so as to tune a key that builds transparency through the Alpha output What's more, this capability lets you generate keys by routes other than the Qualifier palette controls too. In the next example, the Contrast and Custom Curve controls in Node 3 build a high-contrast matte of the windows, which then gets blurred. The RGB output of Node 3 then feeds the KEY input of Node 2, where the resulting key can drive an assortment of adjustments; here, to tint the product in the image green. Alternately, this same technique could serve to create transparency through the Alpha output.

### Using a high-contrast color correction as a key

You can hook RGB inputs and outputs up to Key inputs and outputs by hand, dragging links across between them. Or you can drag a node and hover it over an RGB or Key link to splice it in. Cross-wiring key and RGB inputs and outputs is a potent capability that opens the door to all sorts of workarounds for unusual situations.

### Using External Mattes

The External Matte node has grown over the years. Where it once served purely to bring in matte channels for setting opacity and confining adjustments, it has broadened into a means of bringing in a media file's RGB channels for layering grain, texture, and stylized distress over an image, and even into a way to treat a clip's own channels as a matte. There are two ways to bring matte clips into your project:

- You can bring mattes in through the Media page, either attaching them to a clip so a given matte stays available only to that one clip as part of a Clip grade, or adding timeline mattes that stand on their own in the Media Pool and then become available to any Track grade.
- Alternatively you can attach a matte to a clip via the Media Pool on the Color page, dragging a clip out of the Media Pool into the Node Editor. Doing that turns the clip into an external matte within the current grade, usable as a matte for secondary adjustments or as a compositing layer (paired with the Layer mixer) for blending textures or images into your grade. That clip also gets tied automatically to the Media Pool clip matching the one you're grading, as a clip matte, helping you track which clips draw on other clips as mattes.

To dig deeper into bringing matte clips into the Media page, consult "Adding and Removing External Mattes," located within Chapter 18, titled "Adding and Organizing Media with the Media Pool."" Attached or not, mattes work inside a grade by way of EXT MATTE (external matte) nodes. The outputs an EXT MATTE node carries are:

An external matte connected to the first node of a grade

- EXT MATTE Outputs: Through four blue square key outputs you can output the channels held inside the EXT MATTE node, though which channels exist governs what comes out. Where the EXT MATTE node's source clip holds RGBA channels, they show up as Alpha, Red, Green, and Blue key outputs you can wire into any other node's key input. Where, instead, the EXT MATTE node's source clip holds only RGB channels, the key outputs on offer become Red, Green, Blue, plus Y (luma); a "Use Lum for Alpha Output" setting on the Node Editor contextual menu then lets you press the Y channel into service as a matte.

One intriguing thing about these four outputs is that each is given over to a single A, R, G, and B color channel. As a rule, External Matte clips get written with their matte data laid down at once

to all three RGB channels. You could, though, render distinct pure primary-colored mattes onto each color channel (a so-called "disco" matte), giving the Red channel one matte, the Green channel another, and the Blue channels yet another, thereby packing three separate mattes inside a single media file for convenience. Add one more matte onto the Alpha channel and you can even pack four mattes into a single file. You then draw on each of these mattes individually by hooking up the correct EXT MATTE node output. (Note: To stay backward compatible, any project from a DaVinci Resolve release older than 12.5 keeps putting out RGBY from the square outputs rather than YRGB.)

- RGB Output: A square green RGB output lets you route a matte clip's RGB image data into any other clip's RGB input. That earns its keep especially when you're blending a matte clip with the current clip through a Layer Mixer node to build a textured composite of some sort.
