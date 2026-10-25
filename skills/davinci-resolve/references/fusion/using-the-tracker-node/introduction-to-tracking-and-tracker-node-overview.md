# Introduction to tracking and tracker node overview

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the tracker node.
[Chapter index](INDEX.md) / [Next section](tracker-inspector-controls-and-tracker-control-tab.md)
<a id="source-analyze-the-image-to-be-tracked"></a> <a id="source-apply-the-tracking-data"></a> <a id="source-basic-tracker-node-operation"></a> <a id="source-connect-to-a-trackers-background-input"></a> <a id="source-corner-positioning"></a> <a id="source-introduction-to-tracking"></a> <a id="source-match-moving"></a> <a id="source-modes-of-the-tracker-node"></a> <a id="source-perspective-positioning"></a> <a id="source-stabilizing"></a> <a id="source-tracker-node-overview"></a> <a id="source-using-the-tracker-node"></a> <a id="source-using-the-tracker-node-part-1"></a> <a id="source-viewing-tracking-data-in-the-spline-editor"></a>

### Using the Tracker Node

This chapter walks through everything the Tracker node in Fusion can do, opening with how trackers wire into your node trees and closing with the various jobs they can carry out.

### Introduction to Tracking

For any compositor, tracking ranks among the handiest and most indispensable techniques around. Loosely put, it's the building of a motion path by analyzing a particular region of a clip across time. Fusion ships several distinct tracking nodes so you can analyze different sorts of motion. Once a clip's motion is tracked, the resulting data feeds stabilization, motion smoothing, matching one object's movement to another's, and plenty of other vital jobs. Types of tracking nodes in Fusion: Tracker: Trails a comparatively small, recognizable feature or pattern within a clip to derive a 2D motion path. People sometimes call this point tracking. Planar Tracker: Trails a flat, unchanging surface region of a clip to derive a 2 ½D motion path that includes perspective. A planar tracker also copes better than a point tracker when some tracked pixels slip offscreen or get hidden. Camera Tracker: Trails several points or patterns across a clip and runs a more elaborate analysis by comparing how those patterns move. The payoff is a faithful rebuild of the live-action camera inside virtual 3D space. In this manual each tracker type is given a chapter of its own. The Tracker node and its tracking techniques are what the present chapter addresses.

### Tracker Node Overview

The Tracker node is a single node that actually handles tracking, stabilizing, match moving, and corner-pinning operations. Because the Tracker node can transform the foreground input, it can generate tracks and then stand in as a Merge within a match move or corner-pin setup. Alternatively, you can have it produce tracking data alone and then publish that data to other nodes in the Node Editor.

### Modes of the Tracker Node

The Tracker node is a remarkably versatile tool, often dropped into a composite several times to assist with dozens of jobs. Most of those jobs, though, distill down to a handful of operations. The Tracker node provides four operation modes that span the bulk of tracking situations.

### Stabilizing

One or more tracked patterns can serve to strip all motion out of a sequence, or to even out vibration and shakiness. Stabilizing from a single tracker pattern fixes only the X and Y position. Combine multiple patterns and you can stabilize position, rotation, and scaling.

### Match Moving

Stabilizing's opposite is match moving, which reads position, rotation, and scaling within a clip from one or more patterns. Rather than removing that motion, it lays the motion onto another image so the two images can be composited as one.

### Corner Positioning

Corner positioning tracks four patterns, which then map the four corners of a fresh foreground into the background. The technique is typically used to swap out signs or mobile phone screens. For tasks of this sort, the Planar Tracker node is frequently the better opening move.

### Perspective Positioning

Perspective positioning likewise tracks four patterns to pinpoint the four corners of a rectangle. Each corner then maps to a corner of the image, rescaling and warping it to strip away all apparent perspective. For removing perspective from a clip, the Planar Tracker node is frequently the better opening move.

### Basic Tracker Node Operation

Three fundamental steps underlie every tracking workflow. 1 Wire whatever image you wish to track into the yellow background input of the Tracker node. 2 Define the tracking pattern, then analyze the clip so a path is created. 3 Put the resulting tracking data toward stabilizing, match moving, corner pinning, or removing perspective.

### Connect to a Tracker's Background Input

The starting move is to wire the output of whatever image you want to track into a Tracker node's background input. The Tracker node analyzes the image attached to its background input. You can slot the Tracker node serially among other nodes if you mean to use the Tracker node itself for a simple stabilization, or to have it carry out a Merge node's role within a match move or corner-pin operation.

A serially connected Tracker node that can both track and transform the images coming in. However, when you're merely using a Tracker node to analyze data destined for several nodes elsewhere in the comp, you might branch it and leave its output unconnected to signal that the Tracker node is a data repository. Note that this isn't required; serially connected Tracker nodes can link to multiple other nodes as well.

A branched Tracker connection, signaling that it ties to other nodes rather than being used on its own

### Analyze the Image to be Tracked

With the node tree built and the Tracker inserted where you want it, you can set the tracker up in the viewer. You pick out one or more features in the image to track (these are called patterns) by adding trackers (one comes by default) and, using the viewer's onscreen controls, positioning them. Once the clip has been analyzed by the Tracker node, the tracking data that results lives inside that Tracker node. Keyframes, one for each frame, mark the Tracked Center X and Y data that's been saved, while a motion path traces the tracked data's route in the viewer.

A motion path marking the tracked motion, together with tic marks flagging keyframes of tracking data

### Apply the Tracking Data

Two routes let the tracking data held inside the Tracker node go toward stabilizing, match moving, corner pinning, or removing perspective. Method 1: Use the Tracker node to match move and merge A foreground image can be attached to the Tracker node, with the motion drawn from the analyzed background image then applied to it.

Using a Tracker node in line for a match move

Set the Operation parameter on the Operation tab of the Inspector to Match Move, Corner Position, or Perspective Position, and the motion always lands on the foreground input (where one is connected). For simple cases the workflow is straightforward. Here a Merge node's role can fall to the Tracker node, given that Tracker nodes carry all the same functionality a Merge does. Handling a match move and merge together in one Tracker node. Method 2: Connect specific parameters to the Tracker Node Another path is to feed the Tracker node's tracking data into the specific parameters of other nodes that handle the real work, useful where a match move setup amounts to more than merely transforming a foreground image. Without any direct wiring in the node tree, each Tracker node—and each pattern inside it—publishes its data for other nodes to draw on. To illustrate, the node tree below puts an Ellipse node to work isolating a glow effect on the ray gun prop.

A Tracker set up as a branch, wired through the Connect To menu. Because the ellipse has to track the ray gun's motion, a Tracker node analyzes how the gun tip moves, and that tracking data then drives the ellipse's animation. Rather than tying to the tracker directly through the foreground input, the ellipse connects indirectly, by way of the Connect To contextual menu.

Lighting a ray gun by wiring tracking data into the center position of an Ellipse node. Things go more smoothly after you rename the Tracker you built to something that describes whatever's being tracked.

Renaming trackers in the Tracker List—double-click one and type descriptive text. After the ray gun's tip is tracked, that tracking data feeds into the Center parameter of an Ellipse node confining a Glow effect; you do this by right-clicking the Center parameter's label over in the Inspector and picking Tracker1 > Ray Gun Glow: Offset position out of the Connect to submenu on the contextual menu. Within that submenu appear the data from every Tracker node across your node tree along with each tracking pattern, and since the Tracker was named, finding it is simple. Offset position is our pick because it drops the ellipse's center squarely onto the path. It still, though, leaves us free to offset the ellipse if needed, by way of the offset controls in the Inspector.

A right-click on a parameter's label is what lets tracking data hook into it for animation. A Tracker node's data can be routed into any other node's parameter, though most often you'll wire track data into center, pivot, or corner X/Y style parameters. Using tracking data in this fashion, you needn't connect the Tracker node's own output to anything else across your node tree; once you link it via the Connect To submenu, the data flows from the Tracker straight to the Center parameter.

### Viewing Tracking Data in the Spline Editor

Within the viewer, tracking data turns up either as a path or, over in the Spline Editor, as a displacement spline. Either place lets you shape that tracking data. The Tracker's default is a displacement spline, which tells you how far the tracking point has drifted from where it began. That suits velocity adjustments well, yet it says nothing about direction. When you need to nudge a handful of points one way or another, the displacement spline can be converted into an X and Y coordinate spline. A right-click on a parameter's label is what lets tracking data hook into it for animation. A right-click in the viewer brings up a contextual menu. Sitting at its very bottom is a reference to the path the Tracker created, named Tracker1Tracker1Path:Polyline. Pick it and a longer submenu opens where Convert to XY Path is available. To read more about Displacement Splines, turn either to the DaVinci Resolve Reference Manual, Chapter 72, "Animating in Fusion's Spline Editor," or else to the Fusion Reference Manual, Chapter 10.
