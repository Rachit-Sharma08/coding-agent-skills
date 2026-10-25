# Tracking a paint stroke and tracking a group of paint strokes

Version: DaVinci Resolve 20.3 Reference Manual. Context: Paint.
[Chapter index](INDEX.md) / [Previous section](setting-the-brush-size-and-choosing-an-apply-mode.md) / [Next section](planartracker-steady-mode-and-paint-connection.md)
<a id="source-paint-part-2"></a> <a id="source-setting-up-the-planar-tracker-for-stabilization"></a> <a id="source-tracking-a-group-of-paint-strokes"></a> <a id="source-tracking-a-paint-stroke"></a> <a id="source-using-the-planar-tracker-with-the-paint-tool"></a>

### Tracking a Paint Stroke

Any of Fusion’s trackers can animate where a paint stroke sits. Say you cloned a flag pole out of a clip but the camera pans — you can track the flag pole and bind the resulting path to the paint stroke.

A right-click over the Stroke’s Center control in the view lets you apply a tracker modifier To bind a tracker to a paint stroke: 1 Using the Paint node, pick the Stroke brush type and clone an object off a frame. 2 On the Paint toolbar above the viewer, click the Select tool. 3 Draw a selection box around the stroke to grab it. 4 Right-click the stroke’s center control, then pick Stroke1:Center > Modify With > Tracker Position. 5 Click the Modifiers tab to bring up the Tracker controls. 6 Out of the Node Editor, drag the MediaIn for the image you painted on into the Tracker Source field in the Inspector.

Drag the MediaIn you mean to track into the Inspector’s Tracker Source field 7 Click the Track Forward button. 8 Once the track is done, down at the bottom of the Inspector, reach for the Tracker 1 X Offset/Y Offset controls to nudge the paint stroke back into place if needed.

### Tracking a Group of Paint Strokes

You can hand a single tracker to several strokes by folding them into a group and wiring the tracker to that group. Rather than tying in each stroke separately, the group’s center serves all of the strokes. Provided every object moves consistently in the same direction — as things “nailed to the set” would — applying the tracker to the group makes cloning out a batch of objects with one paint node a breeze. To group paint strokes, proceed like so: 1 Draw a bounding box, Shift-click, or Command-click to grab every stroke you want grouped. 2 Click the Paint Group button on the Paint toolbar.

Grabbing all the strokes and then clicking the Paint Group button gathers them into one group The group’s onscreen controls stand in for each paint stroke’s controls, and the Inspector’s Modifiers tab now displays the group’s parameters. You can still edit the individual strokes by picking Show Subgroup Controls in the Inspector’s Modifiers tab. The group, in turn, brings a Center, Angle, and Size control for wiring to a tracker.

Either use the onscreen controls, or, within the Modifiers tab, right-click the Paint Group’s Center X label to wire up the tracker

### Using the Planar Tracker with the Paint Tool

What follows is an example digging further into a workflow that pairs the Paint tool with the Planar Tracker to retouch a clip. By teaming the Paint node with the PlanarTracker node, we’ll wipe a few facial scars off an actor’s forehead in a commercial, showing a typical way these two powerful tools join forces.

The actor carries a few forehead scars the director wants painted out Since this clip is in motion, we can’t simply paint the scars off the man’s forehead; we have to account for the motion so our paint work clings to his face. The usual workflow here analyzes the image’s motion and uses it to run a “steady” operation, locking the area we intend to paint in place so we’re painting on a surface that doesn’t move.

### Setting Up the Planar Tracker for Stabilization

The Planar Tracker is the best route for this, so we’ll drop the PlanarTracker node in after the MediaIn1 node, wiring the image into the PlanarTracker node’s background input. As ever, take care which input you connect so the effect works as intended.

Dropping in a PlanarTracker node to analyze and steady the portion of the image we plan to paint on With the PlanarTracker node selected and loaded into the viewer, a viewer toolbar shows up bearing an assortment of tools for drawing shapes and handling tracking data. The Planar Tracker operates by tracking flat surfaces that you mark out by drawing a shape around the feature you want followed. The moment you create a PlanarTracker node, you can start drawing a shape, so here we trace a plain polygon over the man’s forehead, that being the feature we want steadied ahead of painting. We make a plain box by clicking once on each corner of the man’s forehead to set control points, then clicking back on the first one to seal the shape.

Tracing a shape across the man’s forehead to get ready for Planar Tracking Inside the Inspector, the PlanarTracker node carries tracking transport controls akin to the Tracker’s. There are, however, two buttons — Set and Go — sitting beneath the Operation Mode menu, which starts on Track, that being our first order of business. The Set button picks which frame serves as the “reference frame” for tracking, so you click Set first, then the Track Forward button below it.

Placing a reference frame at the start of the frame range we intend to track TIP: The Set button lets you watch over a Planar Track as it runs and halt it the moment it starts slipping, tweaking things as needed before clicking Set on the new frame to establish a fresh reference, then carrying on tracking forward toward the clip’s end.

Use the Pattern controls to configure the way the analysis behaves. Among them, the Motion Type menu arguably carries the most weight. For the scenario shown here, Perspective is the tracking style we're after. That said, depending on your footage you might get cleaner output from the Translation, Translation/ Rotation, or Translation/Rotation/Scale options instead. As soon as the track begins, dots scatter across the track region shape you drew to flag the pixels it considers trackable. Down along the Timeline ruler, a green progress bar reports how much of the clip still needs to be processed.

Press the Track from First Frame button to launch the Planar Track; the green dots over the picture plus that green progress bar confirm tracking is underway. NOTE: Should the track refuse to move, or begin and then stall, take that as a signal that the shape you drew lacks enough trackable detail for the Planar Tracker, and your smartest move is to pick a different region of the picture to track. With the track done, head to the PlanarTracker node's controls in the Inspector and switch the Operation Mode to Steady.
