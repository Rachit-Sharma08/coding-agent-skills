# Simple match moving and corner positioning operations

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the tracker node.
[Chapter index](INDEX.md) / [Previous section](obscured-and-out-of-frame-tracking-patterns.md) / [Next section](match-moving-text-example-and-adding-a-layer-to-match-move.md)
<a id="source-applying-the-tracker-as-a-modifier"></a> <a id="source-connecting-to-trackers-operations"></a> <a id="source-corner-positioning-operations"></a> <a id="source-offset-position"></a> <a id="source-perspective-positioning-operations"></a> <a id="source-simple-match-moving"></a> <a id="source-steady-angle"></a> <a id="source-steady-position"></a> <a id="source-steady-size"></a> <a id="source-unsteady-position"></a> <a id="source-using-the-outputs-of-a-tracker"></a> <a id="source-using-the-tracker-as-a-modifier"></a>

### Simple Match Moving

At its core, match moving hands the movement of the tracked clip over to a second clip. You can carry it out in two ways. The first wires other nodes — Transform or Merge, say — to a Tracker’s outputs. The second stabilizes an image as though removing every trace of motion, except that you leave the Merge menu off BG Only and choose FG Over BG, FG Only, or, on rare occasions, BG Over FG instead.

Choose, for the Merge menu, one of BG Only, FG Over BG, or BG Over FG With this Merge menu in play, you attach a foreground image to the input connection of the Tracker node within the Node Editor.

Connect a foreground image to the Tracker’s foreground input Turning on FG Only mode transfers the background’s motion onto the foreground, and the Tracker then outputs nothing but the altered FG image. That output can afterward be merged over the original, so you can keep refining the foreground with other nodes before laying the result over the background clip.

### Corner Positioning Operations

Corner Positioning pins the four corners of a foreground image onto four patterns held by the Tracker. People most often turn to this operation, or technique, when swapping out signs. For the Tracker’s Corner Positioning operation to work, at least four patterns must exist. Should you choose this mode without already having four patterns in the Tracker, it quietly adds more until the count reaches four. Switching the mode on brings up a row of drop-down boxes for assigning which tracker maps to each corner of the rectangle. It does nothing while the Merge control option sits on BG Only.

### Perspective Positioning Operations

Perspective Positioning serves either to strip perspective out of a foreground image or to carry the perspective of one sequence over to another. It comes in handy when you have to paint out a region that perspective has distorted. Pulling the perspective off flattens the images for painting, after which a second tracker restores the perspective. The Tracker’s Perspective Positioning operation demands at least four patterns. Pick this mode when fewer than four patterns are already configured in the Tracker, and it will add the missing ones automatically until four are present. With the mode active, a set of drop-down boxes appears for choosing which tracker corresponds to each corner of the rectangle. It produces no result while the Merge control option is set to BG Only.

### Connecting to Trackers’ Operations

A very frequent use for a tracked pattern is to let its tracked position or path govern where another node’s parameters sit. Take, for instance, tracking an eye so you can color correct it to blue through an effect mask. You begin by tracking the eye, then build a color corrector configured the way you want. You draw a mask shaped like the eye and tie the Tracker’s position to that mask’s Center. Beyond the path (known as Offset Position), every pattern within a tracker exposes four more values that can act as connections for other nodes in the Node Editor.

To bind a node’s position parameters to a tracker, choose the connection type out of the control’s contextual menu (say, via Transform 1: Center > Connect To > Tracker 1 > Offset Position). The tracker automatically publishes five connection types for hooking up to a position parameter on another node.

### Steady Position

Steady Position lets you stabilize footage across X and/or Y so camera shake and other unwanted movement disappear. This connection flips the output of the tracked pattern’s motion. Wire a Center parameter to the Tracker’s Steady Position and, by default, it lands at 0.5/0.5 (the center of the screen) on frame 1. The Reference mode in the Tracker’s Operation tab lets you alter that.

### Steady Angle

Steady Angle mode also stabilizes footage along X and/or Y to clear away camera shake and other unwanted movement. Connect a control — the Angle of a Transform, for example — to the Tracker’s Steady Angle, and by default it begins at 0 degrees on frame 1. That can be reset through the Reference mode in the Tracker’s Operation tab. From that point onward, the motion Steady Angle yields spins counter to the direction of the original. Thus, if the angle reads 15 degrees at frame 10, Steady Angle returns -15 degrees. Steady Angle calls for a minimum of two tracked patterns in the tracker; with only one point on hand, your sole option is (Un)Steady Position.

### Offset Position

Fundamentally, an Offset Position is the path the tracker produces. It’s what you reach for when you need an object to ride along the path. Each individual tracker inside the Tracker node has its own, and it pertains to that one tracker alone. Tie the Center X and Y parameters to the Tracker’s offset position, and the node’s center will trace that tracker’s path precisely. Hooking up to individual trackers is always handy when you want elements to align with object motion in your footage. You might, say, track your actor’s hand and pin a ball to the Tracker’s offset position so the ball mirrors the hand’s exact movement. Or track something that needs rotoscoping and fasten the mask’s center to the Tracker’s offset position.

### Unsteady Position

Once Steady Position has done its work, Unsteady Position brings the original movement back onto an image after you’ve layered in an effect or a new element. The motion Unsteady Position produces amounts to an offset running the same way as the original motion did.

### Steady Size

What the Steady Size connection puts out is the inverse of the tracked pattern’s scale. Tie a parameter — the Size of a Transform, for instance — to the Tracker’s Steady Size and by default it starts at a Size of 1 (that is, the original size) on frame 1. You can revise that through the Reference mode in the Tracker’s Operation tab. The size Steady Size mode generates then works against the size shifts of the original motion. So when the true size at frame 10 comes to 1.15, Steady Size returns 1 - (1.15 - 1) = 0.85. Steady Size needs at least two tracked patterns in the tracker; with a single point only, you’re limited to (Un)Steady Position.

### Using the Outputs of a Tracker

Every tracker pattern you create in the Tracker node publishes the outputs covered above. On top of that, the Tracker node as a whole publishes a Steady Position, Angle, Size, and an Unsteady Position. These node-level outputs are worked out from all the patterns in that tracker, governed by the Match Move Settings controls in the Tracker’s Operation tab. Those Match Move settings fix the reference frame for stabilization and the point that stabilization pivots around Rather than leaning on the Tracker node to carry out the Merge operation, a common alternative is to build a match move by routing these published outputs to several nodes. A tracker tracks a pattern, and the resulting data can then be fed to multiple other nodes by way of the Connect To submenu. As an illustration, here is how to perform a match move through the Connect To menu: 1 Track the background clip with no fewer than two tracking patterns in the tracker. 2 On a separate branch, attach a Transform node to the background clip.

With the background branched off toward a Tracker and a Transform 3 Over the Transform’s Center, right-click and choose Connect to > Tracker1 > Steady Position.

Here the tracker exposes its output so other nodes can hook into it, used in this case to steady the clip 4 Wire the foreground into a corner-positioned node so you can line up the foreground’s corners suitably over the background. 5 Drop one more Transform node into the Node Editor following the Merge.

Following the Merge, a second Transform serves to reintroduce the original motion through Unsteady Poisition 6 Link the new Transform’s Center to the Tracker’s Unsteady Position. The picture returns to its initial state, now carrying the added effect. To get a clearer sense of the mechanism, picture a pattern chosen at frame 1 sitting at position 0.5, 0.5. It stays put on frame 2, so it remains at 0.5, 0.5. By the third frame it has shifted 10 percent of the image’s width rightward, putting it at 0.6, 0.5. With a transform center tied to the Tracker’s Steady Position output, the Transform node’s center reads 0.5, 0.5 across the first two frames since nothing changed. At frame 3 the center slides to 0.4, 0.5 — the mirror image of the horizontal motion the pattern tracked, nudging the picture a touch rightward by 10 percent of the image width to offset the movement and bring the pattern of pixels back to where it originally lay.

### Using the Tracker as a Modifier

One more way to attach a tracker straight to a control is to bring it in as a modifier. Picking the Tracker out of the Modify With contextual menu doesn’t employ a Tracker node at all; it instead places a modifier in the Inspector whose parameters are nearly the same as those in the Tracker node itself. The upside is that whatever object you want riding the tracked path gets wired to the tracker modifier automatically the moment you apply it.

### Applying the tracker as a modifier

Here is how a Tracker modifier diverges from a Tracker node:

- A Tracker modifier is limited to tracking just one pattern.
- You have to assign a source image to the Tracker modifier.

Because a Tracker modifier emits only a single value, it can’t handle elaborate stabilization jobs, yet it offers a tidy, fast way to drop a tracker onto a point you need to follow.

Over any Center Coordinate Control, right-click and pick Modify With > Tracker Position to bring in a Tracker modifier

For an example of applying the Tracker as a modifier, follow these steps: Suppose you had to track an actor’s eyes so an otherworldly, alien glow could be laid over them. 1 Place an ellipse mask node so it covers one of the actor’s eyes. 2 Within the Inspector, right-click the mask’s Center parameter and, from the contextual menu, pick Ellipse1 Center > Modify With > Tracker Position. 3 Open the Modifiers tab in the Inspector and drag the MediaIn1 node you intend to track into the Tracker Source field.

Holding the tracking controls plus a Tracker Source field that names which node does the tracking, the Modifiers tab 4 Press the Track Forward button to set the eye-tracking in motion. 5 Slot a Soft Glow node right after the MediaIn and route the Ellipse Mask into the white Glow Mask input.

A Tracker modifier put on the Ellipse so a green glow forms over an actor’s pupil

To give the Tracker modifier a different source image, type the node’s name or drag the node out of the Node Editor and drop it onto the Tracker Source field control. Where a node (call it node#1) is wired into the node that holds the modifier (call it node#2), the Tracker modifier’s source image becomes node #1 automatically To dig deeper into the Tracking parameters, consult Chapter 119 (“Tracking Nodes”) of the DaVinci Resolve Reference Manual, or alternatively Chapter 59 within the Fusion Reference Manual.
