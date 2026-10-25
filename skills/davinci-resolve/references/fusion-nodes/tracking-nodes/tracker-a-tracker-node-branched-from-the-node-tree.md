# Tracker a tracker node branched from the node tree

Version: DaVinci Resolve 20.3 Reference Manual. Context: Tracker.
[Chapter index](INDEX.md) / [Previous section](surface-tracker-result.md) / [Next section](tracker-pattern-list-and-trackers-tab.md) / [Continue Tracker Tra / Trackers Tab](tracker-pattern-list-and-trackers-tab.md)
<a id="source-a-pattern-rectangle-identifies-the-area-to-track"></a> <a id="source-a-tracker-node-branched-from-the-node-tree"></a> <a id="source-basic-node-setup"></a> <a id="source-inputs"></a> <a id="source-intellitrack-ai-point-tracker"></a> <a id="source-legacy-point-tracker-onscreen-controls"></a> <a id="source-repositioning-the-tracker"></a> <a id="source-the-tracker-node"></a> <a id="source-tracker-node-introduction"></a> <a id="source-tracker-onscreen-controls"></a> <a id="source-tracker-tra"></a>

### Tracker [Tra]

### The Tracker node

### Tracker Node Introduction

The Tracker exists to spot and follow one or more pixel patterns as they move from frame to frame in video. You can then feed that tracking data to drive the position or values of other nodes in the composition (the center of a Light Rays node, say). On top of that, trackers can steady an image or impose destabilization on one image derived from the movement of another.

For further detail, turn to "Using the Tracker Node" (Chapter 82) within the DaVinci Resolve Reference Manual, or to Chapter 22 of the Fusion Reference Manual.

### Inputs

Three inputs feed the Tracker: Background: The orange image input takes the primary 2D image you want tracked. Foreground: The optional green foreground takes a 2D image that gets composited atop the background, serving as a corner pin or a match move. Effect Mask: A mask shape is what the blue input expects — one built from polylines, simple primitive shapes, paint strokes, or bitmaps coming from other tools. Wiring a mask into this input restricts the tracking to particular regions.

### Basic Node Setup

You can drop Tracker nodes inline among other nodes or hang them off as a branch from the clip you’re tracking. Inline, an image is stabilized by wiring it into the orange background input. Once the image is tracked, switching the Tracker’s Operation menu to Match Move stabilizes the connected image.

A Tracker node connected inline to an image for stabilization Used as a branch off the node tree, an image gets tracked and then its tracking data is published so another node elsewhere in the node tree can use it. The Tracker’s output needn’t feed into any other node. With the tracking data published, you can call on it through the Connect To contextual menu.

### A Tracker node branched from the node tree

In match-moving setups, the Tracker can also stand in for a Merge tool. In the example below, the Tracker tracks the image fed to the orange background input and then applies that tracking data to the image fed to the foreground input. The Tracker node carries the very same foreground-over-background merge capabilities.

A Tracker node configured so a match move is applied onto the foreground input

### IntelliTrack AI Point Tracker

By default, the Fusion Tracker node now relies on IntelliTrack, the new DaVinci Neural Engine tracker. Leaning on AI makes tracking simpler and more accurate, particularly when many points are involved. As with other AI tools, IntelliTrack works without fixed rulesets or heuristics; instead it learns from real world examples. That makes it less prone to breaking down in situations such as following a subject through brief occlusions. In most cases it proves more accurate and more dependable than the ordinary point tracker. Every bit of the IntelliTrack analysis runs out of sight, demanding nothing extra from you beyond selecting the IntelliTrack setting, placing the tracking crosshairs over high contrast areas on a single moving subject, and then pressing one of the tracker direction controls.

Placing a Tracking Point while in IntelliTrack mode within the Fusion Tracker NOTE: You can still reach the original Point tracker by selecting the Point button.

### Legacy Point Tracker Onscreen Controls

Even though Fusion now defaults to IntelliTrack, the old Point tracker remains within reach via the Point button should you prefer it. Within the tracker, each pattern carries its own onscreen controls for choosing which pixels in the image get tracked. Those controls appear in the viewers any time you select a tracker in the node tree.

### Tracker onscreen controls

Pattern Rectangle Inside the viewer, the tracker shows a red rectangle drawn with a solid line, known as the pattern rectangle. The pattern used for tracking consists of every pixel sitting inside that rectangle. When needed, you can resize the pattern by dragging the rectangle’s edges.

### A pattern rectangle identifies the area to track

Search Rectangle Any time the mouse passes over the pattern rectangle, a second rectangle outlined with dashes shows up. That dashed outline marks the search area, which sets how far from the current pattern the Tracker hunts in the following frame. The search area ought to always exceed the pattern in size and be big enough to cover the largest frame-to-frame movement in the scene. Quicker-moving objects call for bigger search areas, whereas slower-moving objects manage with smaller ones. A bigger search area lengthens the track, so avoid making it larger than it needs to be. When the selected Tracker carries a custom name, that name shows as a label at the lower right of the search area rectangle.

The search rectangle marks the region scanned from frame to frame to find the pattern.

### Repositioning the Tracker

A small handle sits at the pattern rectangle’s upper-left corner. Dragging that handle moves the pattern. While you do, an enlarged view of the pattern appears beneath your mouse pointer to help you place it precisely. That thumbnail goes away as soon as you let go of the mouse button. The magnification ratio can be tuned in the Inspector’s Options tab.

Dragging the handle magnifies the pattern rectangle for precise placement. TIP: A single composition can hold any number of trackers, and any number of objects may draw on the tracking data. Likewise, one Tracker node can track any number of patterns. Although this chapter documents the Tracker’s assorted controls, we strongly encourage you to study the broader background — see "Using the Tracker Node" (Chapter 82) in the DaVinci Resolve Reference Manual, or alternatively Chapter 22 of the Fusion Reference Manual. There are two ways to use the Tracker: as a node within the Node Editor, or as a modifier bound to a parameter. As a node in the Node Editor, the tracked image arrives from whatever feeds the Tracker node’s input. As a modifier, its controls surface in the Modifiers tab of the node holding the connected control. A Tracker Modifier can follow just one pattern, yet its image source may originate anywhere in the composition. Reach for this approach when you want to track a quick position for an element.
