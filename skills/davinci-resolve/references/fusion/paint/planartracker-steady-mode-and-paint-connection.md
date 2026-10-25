# Setting the planartracker node to steady and connecting the paint node

Version: DaVinci Resolve 20.3 Reference Manual. Context: Paint.
[Chapter index](INDEX.md) / [Previous section](tracking-a-paint-stroke-and-tracking-a-group-of-paint-strokes.md) / [Next section](inverting-the-garbage-input-overview.md)
<a id="source-choosing-the-clone-mode-in-the-inspector"></a> <a id="source-connecting-the-paint-node"></a> <a id="source-creating-a-freeze-frame-and-clean-plate"></a> <a id="source-drawing-a-polygon-mask"></a> <a id="source-isolating-the-painted-forehead"></a> <a id="source-painting-a-clean-plate"></a> <a id="source-setting-a-clone-source"></a> <a id="source-setting-the-planartracker-node-to-steady"></a>

### Setting the PlanarTracker node to Steady

The picture will warp on the spot, by however much it takes to lock the tracked region into position for whatever task you have planned. Scrubbing along the clip should reveal the image cornerpin-warping on the fly, by just enough to hold the forehead region pinned inside the shape you outlined. Here, that turns the man's head into a surface ready to be painted.

When the image is steadied, the warp keeps the forehead pinned so it can be painted. You're now set to paint over those scars.

### Connecting the Paint Node

You could simply paint straight onto the picture by hooking the Paint node up after the Planar Tracker, but you'll have a firmer grip on the workflow if you composite the Paint node above the steadied image. To pull that off, drop a Merge in after the Planar Tracker and then feed a Background node into the Merge's foreground. Place a Paint node after the background and you're set to begin.

The Paint node is merged above a steadied Planar Tracker. Making the Background Node Transparent The Background node has to be completely transparent, or you'll end up painting onto the solid color rather than onto the Merge background image. Render the background transparent by sliding the Alpha channel sidebar all the way to the top inside the Color Picker.

Here the Color Picker in the Background node is configured as transparent. Selecting the Stroke and Clone Mode Once the Paint node is chosen and configured, our next move is to grab the Stroke tool. You'll reach for the Stroke tool whenever you need to remove features or paint corrections onto subjects in the frame that should stay locked for the whole shot. Pick the Stroke tool from the Paint node's tools over in the viewer toolbar. After that, select the Clone mode under the Apply Controls. For this walkthrough, we'll borrow a portion of the man's face and clone it across the scars to erase them. Switching to Clone mode swaps the Paint node's controls over to the ones meant for cloning.

### Choosing the Clone mode in the Inspector

### Setting a Clone Source

By default the Paint node clones out of whatever Input image is wired in, unless you tell it to behave differently. If all you're doing is laying color over the background image, you're already set. But if your plan is to clone from the merge's steadied background image using the Paint tool, you have to assign that image as the source for the Paint node. Assign the clone source by dragging the PlanarTracker node onto the Source Tool field in the Inspector.

While cloning with the Paint tool, you can drop any node into the Source Tool field. With the Stroke tool active in the Paint toolbar, Clone mode chosen in the Inspector controls, and the cloning source dropped into the Source Tool field, painting can begin. Hover the pointer above the viewer and a circle marks the paint tool, primed for action. Working the clone brush starts by holding the Option key and clicking on the picture to mark the clone's source region. Here we'll grab our sample from a spot right beneath the first scar we intend to fix. Once you've Option-clicked to grab the sample, clicking anywhere in the frame starts painting.

On the left, an offset is set for the clone sample; on the right, a clone stroke is dragged out. Unhappy with a stroke you laid down? Reverse it with Command-Z and have another go. Doing the same with the second scar on the man's forehead, and perhaps tossing in a couple more tiny strokes so no visible seams remain, we resolve the whole thing within seconds.

On the left is the original picture; on the right, both scars on the man's forehead have been removed using the Stroke tool in Clone mode. TIP: When you need to, the brush size can be tuned straight inside the viewer by holding the Command key and dragging the pointer side to side. As you do, the brush outline grows or shrinks to match. Inverting the Steady Effect to Put the Motion Back In By now, scrubbing the clip confirms the paint strokes really do cling to the man's forehead exactly the way we wanted. The only thing left is to reverse the transform the Planar Tracker laid down so the clip returns to its original state, only this time carrying the painted repair along with it. It works out to a two-stage job, though the opening stage is the easy one.

Scrubbing the steadied clip confirms the paint repair is "clinging" to the man's forehead. We grab and copy the PlanarTracker node sitting ahead of the Merge node, then paste a duplicate of it afterward. That duplicate carries every bit of the analysis and tracking data from the original PlanarTracker node.

Pasting a second copy of the PlanarTracker node after the Paint node

After the second PlanarTracker node is selected, we visit the Inspector and switch on the Invert Steady Transform checkbox, which flips the steady warp transform so the picture goes back to how it started.

Switching on Invert Steady Transform aims to bring the picture back to its starting state. This is merely one way to wire up a Planar Tracker alongside a Paint node. Certain shots may demand extra effort with masks and layering, but the walkthrough above hands you a solid foundation.

### Painting a Clean Plate

For straightforward clips, planar tracking your clone paint strokes can be perfectly adequate. Other times, steadying the clip just won't happen, or the strokes may seem to "bubble." A paint stroke is really one stroke played back across many frames. Every painted frame can look slightly off from its neighbors before and after. Frequently a steadier approach to painting is to build what's known as a "clean plate." Produce a single solid painted frame and lock it. After that, lean on the Planar Tracker to track the cleaned patch back over the original. The payoff: you have only one paint stroke rather than a series of repeated ones that can surface unwanted artifacts. For the upcoming walkthrough we stay with the same clip, only now the method is to freeze, mask, and composite one lone frame of the repaired forehead over the original clip.

### Creating a Freeze Frame and Clean Plate

Just like before, you still track the clip with the Planar Tracker. With tracking done, you can split off from the MediaIn (or the Loader node if you're in Fusion Studio) into a Time Stretcher to build the freeze frame.

Time Remap handles retiming or freezing a clip. Switch off the default Keyframe inside the Time Stretcher and type in the frame you'd like frozen. If you've already run a Planar Track, then typing in the frame you assigned as the Reference Frame is generally a sound choice to freeze.

Build the clean plate by wiring the paint node into the Time Stretcher's output. Clone across whatever regions you want hidden and you've got a lone clean frame. The next job is to composite that clean patch over the original.

### Isolating the Painted Forehead

To begin, we have to mask off only the man's painted forehead. We pull that off by wiring a MatteControl node onto the Paint node's output and then feeding a Polygon node into the garbage matte input. That lets us trace a shape with the Polygon node and apply it as a mask to crop the man's painted forehead out.

Adding a MatteControl node carrying a garbage mask crops the painted forehead out.

TIP: There are several ways to wire up masks for creating transparency—for instance, (a) feed the image into the background input of a Brightness/ Contrast node and feed a Polygon mask node into the effect mask input. Over on the Brightness/ Contrast node, switch on the Alpha channel and pull the Gain slider down to punch a dark hole, or (b) lean on Channel Booleans to copy channel data into the alpha from a Polygon node wired into the foreground input with the image wired into the background input.

### Drawing a Polygon Mask

With the playhead parked on the clip's first frame, we're set to trace a mask that isolates the "clean plate" forehead. Loading MatteControl1 into the viewer and choosing the Polygon1 node so its tools show up in the viewer toolbar gets us positioned to draw a polygon. Tracing shapes with the Polygon node mirrors how shapes are drawn in other spline-driven environments, the Color page included:

- A single click lays down a corner control point.
- Clicking while dragging produces a Bézier curve.
- Clicking the very first control point you placed seals the shape.

We click and drag to trace a shape around the man's forehead, and on sealing the shape we get the exact reverse of our goal—a hole punched in the center of the picture.

Tracing a shape to isolate the forehead yields a reversed result at first when the Garbage Matte input of the MatteControl node is used to wire the Polygon to the MatteControl node. Before correcting that, we slide the Soft Edge slider in the Inspector rightward to soften the edges a touch.
