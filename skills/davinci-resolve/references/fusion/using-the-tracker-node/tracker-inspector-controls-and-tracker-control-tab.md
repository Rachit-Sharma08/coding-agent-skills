# Tracker inspector controls and tracker control tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the tracker node.
[Chapter index](INDEX.md) / [Previous section](introduction-to-tracking-and-tracker-node-overview.md) / [Next section](tracking-transport-analysis-and-pattern-selection.md)
<a id="source-add-trackers"></a> <a id="source-connect-the-image-to-track"></a> <a id="source-motion-tracking-workflow-in-depth"></a> <a id="source-perform-the-track-analysis"></a> <a id="source-position-the-pattern-boxes"></a> <a id="source-refine-the-search-area"></a> <a id="source-the-tracker-control-tab"></a> <a id="source-tracker-inspector-controls"></a>

### Tracker Inspector Controls

How the Tracker node's tabs are laid out in the Inspector mirrors this workflow. It breaks into three principal Tracker tabs, plus the common Settings tab.

- The Tracker Control tab: This is where you build onscreen trackers to aim at patterns, and where the controls for running the required track analysis live.
- The Operations tab: This is where you settle how the tracking data gets used.
- The Display Options tab: This is where you tailor how the onscreen controls

look in the viewer.

The Tracker Operations tab The Tracker Display Options tab

### The Tracker Control tab

### Motion Tracking Workflow In Depth

Tracker nodes serve a pair of purposes. They give you a way to analyze an object you want to follow, and they act as a container for the track data that results. That lets you use one node for the analysis and hand that analysis off to any other node that needs it. What follows is a closer breakdown of the tracking process.

### Connect the Image to Track

Whether or not you actually put the Tracker node itself to work on the tracking data, a successful analysis still depends on the image you mean to track being wired into the background input (yellow) of a Tracker node. The Tracker node does carry a foreground input, but for purposes of tracking analysis it's disregarded at the outset, so even with a foreground attached, only the background gets drawn on throughout the analysis process.

Wiring the output of a MediaIn node into the background input on a Tracker node

### Add Trackers

Although each Tracker node opens with a single tracker pattern, one node can analyze several tracking patterns added to the Tracker List, so several features of an image get tracked together for later use while supporting different kinds of transforms. To add more trackers, click the Add button sitting just above the Tracker List control.

Adding another tracker by clicking the Inspector's Add button. Multiple patterns prove useful while you stabilize, match move, or strip perspective out of a clip. They also spare the Node Editor from clutter, folding into a single node what would otherwise call for several nodes.

Working in the Tracker list:

- To select a tracker: Click whichever Tracker name you'd like to select.
- To rename a tracker: Renaming trackers makes them easier to refer back to down the line. Say you're tracking a car door handle—name that Tracker "Car Handle" and it'll be simple to locate later. The way to do so: just double-click the Tracker's default name in the Tracker list, type a fresh one, and press Return.
- To delete a tracker: Select a tracker and click the Delete button.
- To disable, suspend, or re-enable trackers: Beside each tracker's name in the Tracker List sits a checkbox—click it. The checkbox is a three-way toggle cycling among Enabled, Suspended, and Disabled.

Enabled: Each time the track runs, an Enabled tracker re-tracks its pattern. Other nodes have its path data on hand, and that data is available for stabilization and corner positioning. Suspended: A gray checkbox means it's Suspended. In this state the pattern isn't re-tracked when the track runs. While the data is locked against further changes, the path's data remains on hand for other nodes. It's also available for advanced tracking modes such as stabilization and corner positioning. Disabled: When tracking runs, a Disabled tracker produces no path. Neither other nodes nor advanced tracking operations like stabilization and corner positioning can reach its data.

### Position the Pattern Boxes

A pattern is the patch of pixels targeted for tracking within an image by way of a pattern box. In the viewer, a rectangle marks out the pattern box whenever a tracker is active. A single Tracker node can hold many pattern boxes, each aimed at a different pattern. Every tracked pattern produces a motion path of its own. Click on any portion of a tracker's onscreen controls and it gets selected. Selected pattern boxes turn red, while deselected ones turn green.

A pattern box positioned over an eye you want to track

When you add a Tracker node to the Node Editor, you begin with one pattern box shown in the viewer as a small rectangle. Bring the cursor over the pattern rectangle and the control grows, revealing two rectangles. A dashed line forms the outer rectangle, and a solid line forms the inner one. The outer rectangle is the search area; the inner rectangle is the pattern. To pick a new pattern, you can shift the pattern box by dragging the small (and easily overlooked) handle at the top left of the inner pattern box.

Dragging from its upper-left corner to reposition a pattern in the viewer.

As you move the pattern box, an overlay pop-up appears showing a magnified view of the pixels inside the rectangle to help you place the pattern precisely via the crosshairs within.

A magnified view that surfaces as you drag a pattern box, aiding placement. Sizing a pattern box around the tracking point on the ray gun.

The pattern rectangle can be resized as well by dragging on its edges. Aim to size the pattern box so it wraps the detail you intend to track while excluding whatever is irrelevant. Ideally, see to it that each pixel of the pattern under track sits on one common plane, and that no portion of the pattern is in fact an occluding edge standing ahead of what you truly mean to track. Resizing the pattern box happens outward from the center, so one drag builds any rectangle you require.

TIP: The magnified pattern box pays no attention to viewer LUTs. With Log content, placing the tracker may go easier if you briefly drop a Brightness Contrast node between the source content and the tracker's yellow input. The Brightness Contrast node can then temporarily boost the visibility of the region you're tracking.

### Refine the Search Area

A second rectangle, this one with a dotted border, encloses the pattern box. This is the search area. As tracking advances from one frame to the next, the Tracker examines the region the search area defines, which surrounds the last known tracker position, trying to relocate the pattern. A larger search area improves your odds of successfully tracking fast-moving objects, but it lengthens the track. There are, however, ways to tune tracking for particular content. Tracking a pattern that races across the screen from left to right, for one, calls for a wide search area but not a very tall one, since all the movement is horizontal. Should the search area be smaller than the pattern's frame-to-frame movement, the Tracker will likely fail and latch onto the wrong pixels, so it pays to weigh the motion's speed and direction as you set the search area. To resize the search area, drag along the edges of that dotted outline

### Perform the Track Analysis

Before analysis begins, you'll want a render range laid down in the Time Ruler that covers the stretch of frames where the pattern stays visible. That might be an entire clip or just a small slice of it. According to the kind of motion under track, you may wish to bring in the Adaptive Mode option as an analysis aid (more on that below). With your options settled, any of the tracking transport buttons up at the top of the Inspector will kick off tracking. With tracking underway, the Node Editor stays off-limits until it finishes.
