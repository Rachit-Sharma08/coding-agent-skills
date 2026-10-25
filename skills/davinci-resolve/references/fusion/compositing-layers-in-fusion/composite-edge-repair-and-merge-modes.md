# Fixing problem edges in a composite and composite modes in the merge node

Version: DaVinci Resolve 20.3 Reference Manual. Context: Compositing layers in Fusion.
[Chapter index](INDEX.md) / [Previous section](applying-effects-and-adding-a-node-to-the-tree.md) / [Next section](transform-controls-in-the-merge-node-and-final-composite.md)
<a id="source-creating-and-using-text"></a> <a id="source-creating-text-using-the-text-node"></a> <a id="source-disconnecting-and-reconnecting-nodes"></a> <a id="source-fixing-problem-edges-in-a-composite"></a> <a id="source-styling-and-adjusting-text"></a> <a id="source-the-manual-kerning-tool-in-the-viewer-toolbar"></a> <a id="source-the-restyled-text"></a> <a id="source-using-composite-modes-in-the-merge-node"></a> <a id="source-using-matte-control-nodes"></a> <a id="source-using-text-as-a-mask"></a>

### Fixing Problem Edges in a Composite

In the majority of cases the Merge node handles things flawlessly when fed a foreground image with premultiplied alpha transparency to lay over a solid background. Every now and then, though, you might spot a thin band of fringing right along the border between a foreground element and the transparent region, like what you see in the close-up below. That faint brightening along the edge is a giveaway that the clip most likely wasn't premultiplied. Every foreground image carrying an alpha channel is assumed by the Merge node to be premultiplied. Happily, this is a simple thing to remedy.

A touch of fringing along the border of a foreground element ringed by transparency Click on the Merge node belonging to that specific composite to select it, then hunt down the Subtractive/ Additive slider.

The Subtractive/Additive slider, handy for correcting or reducing fringing within composites Pull the slider fully leftward into the Subtractive position, and the fringing goes away.

An alpha-carrying clip showing fringing (left), and that fringing resolved after pulling the Subtractive/Additive slider leftward (right) That Subtractive/Additive slider—available only while the Apply mode sits on Normal—governs whether Normal mode runs an Additive merge, a Subtractive merge, or some mixture of the two. By default the slider sits on Additive merging, which presumes every input image with alpha transparency is premultiplied (true most of the time). In case the distinction between Additive and Subtractive merging isn't clear to you, here's a brief rundown:

- An Additive merge—slider pushed fully right—is what you want when the foreground image is premultiplied, that is, when the color-channel pixels have already been multiplied against the alpha-channel pixels. Because of that, transparent pixels come out black every time, given that anything times 0 equals 0. The background gets hidden (through multiplication by the inverse of the foreground alpha), and then the foreground's pixels are simply added on top.
- A Subtractive merge—slider pushed fully left—is what you need whenever the foreground image isn't premultiplied. The approach resembles an Additive merge, except the foreground image first gets multiplied against its own alpha to strip away any background pixels lying beyond the alpha region.

The Additive/Subtractive slider gives you a way to mix between the two flavors of the merge—one Additive, the other Subtractive—so you can hit the right balance for your specific composite. Mixing the two now and then helps with troublesome composites whose edges draw the eye by being either too bright or too dark. As an example, applying Subtractive merging to a premultiplied image can darken the edges, while applying Additive merging to a non-premultiplied image causes any non-black region beyond the foreground's alpha to be summed into the output, which brightens the edges. Sliding between Additive and Subtractive lets you dial the edge brightness in until it looks just right for your case.

### Using Composite Modes in the Merge Node

In layer-based programs, you frequently reach for Blend modes to make a composite more believable. Those Blend modes live inside the Merge node, since the Merge node is the place where one layer is laid over another. Imagine a case where you'd like the Screen mode to give a foreground image more of a reflection-like quality. Built into the Merge node is a whole assortment of controls for producing nearly any compositing effect you might want. The things you'd recognize as Blend modes sit in the Apply Mode pop-up menu. These mathematical compositing modes let you fuse the foreground and background layers together. A Blend slider is on hand for dissolving the foreground input into the background. Tweaking the Merge node's Apply Mode together with its Blend slider over in the Inspector NOTE: Pick any Apply Mode setting apart from Normal and the Subtractive/Additive slider vanishes, since the underlying math wouldn't hold up. That's nothing out of the ordinary; the Inspector hosts plenty of controls that tuck themselves away when they aren't needed or when some input is left unconnected. The Screen node works beautifully for faking reflections, and dropping Blend down a touch lets you even out the foreground against the background. The effect is gentle, yet it does help sell the shot. TIP: It may not have escaped you that the Merge node likewise carries a group of Flip, Center, Size, and Angle controls, which let you transform the foreground image without bringing in a separate Transform node. That's a tidy shortcut for streamlining node trees of any size.

### Creating and Using Text

For the next exercise, we'll look at building a basic text object by means of the Text+ node. After that, we'll see how the text generator's alpha channel can be pushed into a second image to assemble a richer composite.

### Creating Text Using the Text+ Node

For making 2D text on the Fusion page, the Text+ node is the go-to tool. When you're in DaVinci Resolve, this is the very same Text+ generator you'll find on the Edit page. You can grab it conveniently right from the toolbar. As a text-effects tool the Text+ node runs incredibly deep, packing six tabs of controls that cover everything from styling the text, to various ways of laying it out, to an array of shading options—fills, outlines, shadows, and borders among them. Powerful as it is, this exercise will only graze its surface. We'll begin with a MediaIn node acting as our background, selected within the Node Editor. Click the Text+ button and a new Text+ node is created automatically, wired in as the foreground input of a Merge node. You'll get the very same behavior in Fusion Studio, only with a Loader node.

Picking the node onto which you intend to tack a further node (top) Pressing the Text+ button along the toolbar spawns a Merge composite on its own, with the text wired in as the foreground input connection (bottom) When you select a Text node, the Inspector opens to its default Text panel parameters, and a toolbar specific to that node also appears across the top of the viewer. Click the leftmost tool and you can type straight into the viewer, or alternatively type into the Styled Text field over in the Inspector.

The Text node's viewer toolbar, offering tools that handle text entry, kerning, plus outline controls

While the Merge is the thing on display, the text surfaces in the viewer sitting atop the background clip. Controls appear right onscreen for spinning the text (via the circle) and shifting its position (using the red center handle plus the two arrows), and a dim cursor is there as well, allowing us to edit and kern the text by means of the viewer toolbar's remaining tools.

Text entered directly into the viewer, accompanied by onscreen controls for transforming the text

### Styling and Adjusting Text

For styling the text, turn to the Inspector controls, adjusting text-style options such as Font, Size, and Tracking to alter how far apart the letters sit.

### The restyled text

TIP: Keep the Command key pressed as you drag any Inspector control and the change becomes "geared down," letting you fine-tune in smaller, more gradual steps.

Choosing the Manual Kerning tool over in the viewer toolbar (it's the second tool from the left) brings up small red dots beneath every letter of the text. Click the red dot below a given letter and a kerning highlight lands over that letter.

### The Manual Kerning tool in the viewer toolbar

To make manual kerning adjustments: 1 Option-drag the red dot beneath any letter to shift that character's kerning, with the letter's motion held to the left and right. Letters can also be dragged up and down to achieve other looks. On some systems the kerning of the letter being adjusted won't refresh until you release the red dot into position. 2 If the result isn't to your liking, you can open up the Advanced Controls in the Inspector and wipe out either the kerning on just the selected letters or every manual kerning adjustment, then start fresh.

Option-dragging the small red dot exposed by the Manual Kerning tool so kerning can be tuned by hand

### Using Text as a Mask

The text can be filled with a solid color or a gradient, or it can serve as a matte that cuts its letters out of a different image. To begin, we'll drag a second clip—a chalkboard covered in math—out of the Media Pool onto the Node Editor as a free-floating MediaIn2 node.

### Disconnecting and Reconnecting Nodes

Picking up from the earlier example, where a MediaIn served as the background and the Text+ as the foreground into a Merge, a bit of rearranging is in order. Click the latter half of the connection running from the Text1 node to the Merge foreground input and it detaches.

Clicking a connection's latter half to detach it (previous page), and how things look once the text node is detached (above) Once a MediaIn2 or Loader2 node is wired onto the Merge1 node's foreground input, the whole viewer fills with the MediaIn2 (granting that we're still looking at the Merge node). Now we have to feed the Text1 node's image in as an alpha channel into the connection for the MediaIn2 node, and a MatteControl node is how we pull that off.

The revised composite, where two video images are now wired in and the text node sits detached

### Using Matte Control Nodes

Pick the MediaIn2 node, then click the Matte Control button on the toolbar to drop it in between the MediaIn2 and Merge1 nodes. (For tidiness I've nudged the nodes around a little in the screenshot.) The MatteControl node serves all sorts of purposes. One of them is gathering up one or more alpha channels, mattes, or images fed into the Garbage Matte, Solid Matte, and/or foreground inputs, combining them, and then applying the result as an alpha channel onto whatever image is wired into the background input. It's essential to confirm that the image you intend to give an alpha channel is plugged into the background input of the MatteControl node, otherwise the MatteControl node simply won't do its job.

The second image properly connected to the MatteControl node's background input Once that's set, wiring the Text+ node's output (which carries the alpha channel) into the MatteControl node's Garbage Matte input is a shortcut for building a mask, matte, or alpha that knocks a transparent area out of an image. Bear in mind it's all too easy to plug into the wrong input by accident. Since the inputs shuffle around based on what's connected and where the node sits (and, honestly, the colors are tough to track while you're still learning), it's vital to keep an eye on the tooltips for whichever input you're dragging a connection toward, so you can be certain you've got the right one. If you don't, the effect falls flat, and whenever an effect isn't behaving, the very first thing to confirm is whether the correct inputs are connected.

Option-dragging a node connection and letting it fall onto a second node brings up a node input menu

There's another way to link nodes: hold the Option key as you drag a connection from one node's output and let it fall onto the body of a second node. Doing so brings up a popup menu where you can pick, by name, exactly which input you want. Keep in mind the menu only surfaces once you've dropped the connection on the node and let go of your pointing device's button. As soon as the Text1 node is correctly tied to the MatteControl node's Garbage Matte input, a text-shaped transparent region appears for the graphic when you load the MatteControl node into the viewer.

Wiring the Text node into the MatteControl node's Garbage Matte input (previous page), along with the hole that gets knocked through the image as a result (above) Customizing Matte Control Nodes The Inspector lets you tweak a few parameters until you land on the result you're after. Within the Inspector controls for the MatteControl node, opening up the Garbage Matte controls exposes parameters that govern how the Garbage Matte input gets applied to the image. For instance, you might decide to fill the text mask with the image rather than punching a hole through it.
