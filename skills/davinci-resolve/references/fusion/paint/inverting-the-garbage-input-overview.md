# Inverting the garbage input overview

Version: DaVinci Resolve 20.3 Reference Manual. Context: Paint.
[Chapter index](INDEX.md) / [Previous section](planartracker-steady-mode-and-paint-connection.md)
<a id="source-inverting-the-garbage-input"></a>

### Inverting the Garbage Input

With the MatteControl1 node selected, we open the Garbage Matte controls and tick the Invert checkbox, which instantly delivers what we were after—the forehead on its own, set for compositing.

On the left, the Garbage Matte input is inverted; on the right, the resulting inverted mask flips the forehead. Compositing the Painted Forehead Against the Original Image We're nearly there. Up next, we'll bring in a Merge node to stack the repaired forehead over the original picture coming out of the MediaIn node. We make a Merge node wired to the PlanarTracker node's output, then wire the MatteControl's output into the Merge node's green foreground input. That drops the cropped, repaired forehead on top of the original picture.

The painted forehead is composited against the original picture. Match Moving the Mask to the Shot We've now got the best of both: a repaired forehead and a good-looking shot background. Yet if we pick the Polygon node and scrub ahead in the clip, the repaired forehead mask slips out of step with the shot's motion, leaving us one last problem. Happily, match moving the mask so it travels with the shot couldn't be easier.

Since the Polygon isn't animated to track the shot's motion, it falls out of step. Picking the first PlanarTracker node sitting right after the MediaIn node, and selecting Track from the Operation Mode menu, surfaces a Create Planar Transform button down at the foot of the listed controls. Pressing that button spawns a fresh, unconnected Planar Transform node in the Node Editor, with the Planar Tracker's transforms already baked into it. In contrast to the Planar Tracker, the Planar Transform is built to work with masks. Once the Planar Transform exists, the Planar Tracker has no further purpose and can be unhooked or removed from the Node Editor.

We slot this new node into the node tree by holding the Shift key and dragging it across the link between the Polygon node and the MatteControl node, releasing once that link lights up.

On the left, a PlanarTransform node is inserted by holding Shift while dropping over a connection; on the right, the result after the PlanarTransform node is inserted. With the new Planar Transform node in place, the Polygon shifts on its own to follow the forehead motion that the original PlanarTracker node captured, animating right along with the shot's movement. And with that, we're done!

The final painted image, along with the final node tree
