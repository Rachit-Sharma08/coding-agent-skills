# Match moving text example and adding a layer to match move

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the tracker node.
[Chapter index](INDEX.md) / [Previous section](simple-match-moving-and-corner-positioning-operations.md) / [Next section](positioning-the-tracker-onscreen-control.md)
<a id="source-a-simple-tracking-workflow"></a> <a id="source-adding-a-layer-to-match-move"></a> <a id="source-match-moving-text-example"></a> <a id="source-setting-up-motion-tracking"></a>

### Match Moving Text Example

Walking you through an entire motion tracking job, this example demonstrates how to build a very basic match-moving effect with the Tracker node — Fusion’s Swiss army knife among trackers.

### Adding a Layer to Match Move

Our sample composition holds a Text1 node generating a “Switzerland” title laid over a drone shot that sweeps over and around a mountain bridge. When the Text1 node is selected, the viewer reveals the onscreen controls for placing the text it produces, and that text already sits at the starting spot we want. Keep in mind that, with the Text node selected, even the portion of the text running offscreen shows up as an outline that tells us where it is.

Text laid over a backdrop, prepared for tracking

What we’re after in this composition is to motion track the background picture so the text travels in step with the scene while the camera soars past.

### Setting Up Motion Tracking

To prepare the motion track, we’ll start by making a standalone Tracker node through a different route than the ones shown earlier. Right-click on any empty part of the Node Editor (ideally where you’d like the new node to land) and pick Add Tool > Tracking > Tracker from the contextual menu, which spawns a fresh Tracker1 node below the MediaIn node (or the Loader node, if you’re on Fusion Studio).

Creating a new node using the Node Editor contextual menu After that, we’ll pull a connection from the MediaIn1 node over to the Tracker1 node so the source clip wires itself into the Tracker1 background input automatically. Doing so branches the MediaIn1 node’s output into the Tracker node, letting the Tracker1 node work on the image apart from the rest of the node tree. It isn’t mandatory, but it’s a neat organizational touch that makes clear the Tracker node is running an analysis referred to by means other than a “physical” connection.

Branching off a Tracker node so it can analyze an image

### A Simple Tracking Workflow

Of all the tracking operations on the Fusion page, the Tracker node is the most basic, and though it can be used in several fashions, one extremely common workflow is to let the Tracker node controls analyze the motion of a subject in the frame whose movement you wish to follow, then put the resulting motion path data to work by “connecting” it to the Center parameter of some other node that can transform the image you want to match move.
