# Dcolorcorrector and speedwarp

Version: DaVinci Resolve 21 New Features Guide. Context: Dcolorcorrector, Speedwarp.
[Chapter index](INDEX.md) / [Previous section](dcolorcorrector-correction-tab-histogram-menu.md) / [dColorCorrector dCC](reliefmap-and-dcolorcorrector.md)
<a id="source-a-simple-speedwarp-setup"></a> <a id="source-basic-node-setup"></a> <a id="source-common-controls"></a> <a id="source-controls-tab"></a> <a id="source-improved-guides-and-rulers"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-mediain-nodes-show-clip-name"></a> <a id="source-motion-vector-layers-generated-from-optical-flow"></a> <a id="source-nudge-spline-keyframes"></a> <a id="source-open-keyframes-and-spline-editor-as-a-new-window"></a> <a id="source-speedwarp-controls"></a> <a id="source-speedwarp-node-introduction"></a> <a id="source-speedwarp-spdw"></a> <a id="source-support-for-remote-monitoring-of-fusion-previews"></a> <a id="source-the-speedwarp-node"></a> <a id="source-up-to-2x-faster-relight-tool"></a> <a id="source-up-to-6x-faster-depth-map-tool"></a>

### Motion Vector Layers Generated from Optical Flow

An update has come to Fusion’s Optical Flow tool, which now emits motion vectors as separate layers. The vector channels that the Optical Flow tool produces are now fully compatible with Fusion’s multi‑layer pipeline. Thanks to this change, tools that once relied on vector auxiliary channels can now reach the new Vector and Back Vector layers. Tools able to take in motion vector layers are:

- Smooth Motion
- Vector Denoise
- Vector Transform
- Vector Warp
- TimeSpeed (Flow Interpolation Mode)
- TimeStretcher (Flow Interpolation Mode)

### Improved Guides and Rulers

In Fusion 21 the Guides and Rulers gained upgrades: locked persistence, guide presets, and improved snapping.

### MediaIn Nodes Show Clip Name

Under Fusion 21, MediaIn nodes will display the clip name rather than showing MediaIn#.

### Open Keyframes and Spline Editor as a New Window

When you need extra room, the Fusion Keyframe and Spline editors can now be popped out into a fresh resizable window by clicking the Undock icon in the Keyframes or Spline toolbar.

Undocking the Keyframe editor into it’s own resizable window.

### Nudge Spline Keyframes

Within the Spline editor, the comma (,) and period (.) keys let you nudge a Spline keyframe to the left or right respectively.

### Up to 2x Faster Relight Tool

Fusion’s Relight tool now runs as much as twice as fast as it did before.

### Up to 6x Faster Depth Map Tool

The Depth Map tool runs much faster now, gaining as much as a sixfold speed boost over the earlier version.

### Support for Remote Monitoring of Fusion Previews

You can now stream Fusion Previews live through DaVinci Resolve’s Remote Monitoring tools and application.

### SpeedWarp [SPDw]

### The SpeedWarp node

### SpeedWarp Node Introduction

SpeedWarp is an AI-driven retiming node that studies the motion across existing frames to build fresh in-between frames, delivering smooth slow-motion free of stutter. Drawing on DaVinci’s neural network, SpeedWarp can rebuild intricate motion that ordinary interpolation or frame blending would usually smear or warp.

### Inputs

Input: The 2D image you want the SpeedWarp to act on is fed into the orange input.

### Basic Node Setup

A straightforward case has the SpeedWarp node retiming the video clip wired into it (A001\_), and then handing that retimed video off to the MediaOut node.

### A simple SpeedWarp setup

### Inspector

### SpeedWarp controls

### Controls Tab

Speed The speed wheel sets how fast the Speed Warp output runs. It sits at 1.0 by default, where nothing changes. Drop the speed to 0.5 to cut the output speed in half; raise it to 2.0 to double it, and so forth. Delay The delay shifts where the Speed Warp output begins. A delay of 10.0 pushes the output 10 frames forward, while a delay of -10.0 pushes it 10 frames backward. Mode Pick the SpeedWarp’s mode.

- Faster: Faster processing for a quicker result.
- Better: Higher quality at a performance cost.

### Common Controls

Transform and Settings Tabs The Transform and Settings tabs that remain are shared across many nodes. You’ll find their descriptions under “The Common Controls” at this chapter’s end.
