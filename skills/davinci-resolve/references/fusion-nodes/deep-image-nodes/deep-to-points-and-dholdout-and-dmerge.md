# Deep to points and dholdout and dmerge

Version: DaVinci Resolve 20.3 Reference Manual. Context: Deep to points, Dholdout, Dmerge.
[Chapter index](INDEX.md) / [Previous section](deep-to-image-and-deep-to-points.md) / [Next section](drecolor-and-dresize-and-dtransform.md) / [Deep to Points DTP](deep-to-image-and-deep-to-points.md)
<a id="source-basic-node-setup-3"></a> <a id="source-basic-node-setup-4"></a> <a id="source-common-controls-2"></a> <a id="source-common-controls-3"></a> <a id="source-common-controls-4"></a> <a id="source-controls-tab-2"></a> <a id="source-dholdout-dhld"></a> <a id="source-dmerge-dmg"></a> <a id="source-inputs-3"></a> <a id="source-onscreen-transformation-controls"></a> <a id="source-pivot"></a> <a id="source-rotation"></a> <a id="source-scale"></a> <a id="source-the-deep-to-points-transform-tab"></a> <a id="source-translation"></a> <a id="source-viewer-transform-controls"></a>

### The Deep to Points Transform tab

### Translation

X, Y, Z Offset Reach for these controls to position the point cloud.

### Rotation

Rotation Order Reach for these buttons to pick the order in which rotation gets applied along each axis of the object. As an example, XYZ applies the rotation first to the X axis, next to the Y axis, and last of all to the Z axis. X, Y, Z Rotation Reach for these controls to spin the object about its pivot point. With the Use Target checkbox on, the rotation is relative to the target’s position; otherwise the global axis is what’s used.

### Pivot

X, Y, Z Pivot The point an object rotates about is its Pivot point. An object normally turns about its own center, which counts as a pivot of 0,0,0. Reach for these controls to shift the pivot away from the center.

### Scale

X, Y, Z Scale With the Lock X/Y/Z checkbox ticked, just one Scale slider appears. That sets the object’s overall size. Clear the Lock checkbox and separate X, Y, and Z sliders show up so you can scale each dimension on its own. Note: When the Lock checkbox is ticked, you can’t scale individual dimensions, not even by dragging particular axes of the Transformation Widget in scale mode. Use Target Tick the Use Target checkbox and a set of controls opens up for placing an XYZ target. With target on, the object always turns to face the target. Its rotation becomes relative to the target. Import Transform Opens up a file browser where you pick a scene file your 3D application saved or exported. These file types are supported:

LightWave Scene Max Scene Maya Ascii Scene

.lws .ase .ma

Only transformation data gets brought in by the Import Transform button. When it comes to 3D geometry, lights, and cameras, think about reaching for the File > FBX Import option instead.

### Onscreen Transformation Controls

Out in the viewer, most of the Transform tab’s controls show up as onscreen controls for transformation, rotation, and scaling. To switch which mode the onscreen controls are in, click one of the three buttons on the toolbar at the viewer’s upper left. There are keyboard shortcuts for flipping between the modes as well: translation is Q, rotation is W, and scaling is E. Across all three modes, you can drag a single axis of the control to affect just that one, or drag the control’s center to affect all three axes at once.

For most 3D tools the scale sliders start out locked, which scales all three axes uniformly. Clear the Lock X/Y/Z Scale checkbox to scale an object along one axis alone.

### Viewer Transform controls

### Common Controls

Settings Tab The Inspector’s Settings tab is mirrored on other Deep Image nodes too. You’ll find these common controls spelled out fully at the close of this chapter, within “The Common Controls.”

### dHoldout [dHld]

The dHoldout node dHoldout Node Introduction With a foreground Deep Image, this tool occludes background Deep Image samples — either dropping them or working out the value once occlusion has happened Inputs One background input plus a foreground input is what the dHoldout tool relies on. Background: From a node holding the deep image data you mean to serve as the background, this orange input is connected. Foreground: That white foreground input takes the second of two deep images, usually a foreground subject meant to occlude the background.

### Basic Node Setup

Into the dHoldout node comes the background media holding the deep image data. From there it lets you refine the foreground deep image’s depth boundaries so as to occlude the background.

Pulling in deep image data from a pair of sources, dHoldout occludes the background by means of the foreground source. Inspector

dHolodout controls

### Controls Tab

Inside the Controls tab sit parameters that govern how much depth information goes into — or is held back from — occluding the background deep image.

- Compute Occluded Samples: Reach for this checkbox to drop samples out of a semi-transparent foreground input. Visible background pixels get recolored as though glimpsed through a partly transparent foreground.
- Holdout Z Offset: This slider lets you slide the holdout depth samples forward or back. Lower this value to push the holdout forward; raise it and the reverse happens. Sample: Click and drag out of the sample button into the viewer to pick a value.
- Holdout Center: This lets you reposition the holdout along the X and Y axis.

### Common Controls

Settings Tab Other Deep Image nodes likewise hold a copy of the Inspector’s Settings tab. A detailed account of these common controls comes at the end of this chapter in the “The Common Controls” section.

### dMerge [dMg]

The dMerge node dMerge Node Introduction Several data streams get combined by this tool, which merges their depth samples for seamless compositing. Like the merge 3D tool, it sports numerous inputs.

### Inputs

One background input plus multiple foreground inputs is what the dMerge tool relies on. Background: From a node holding the deep image data you mean to serve as the background, this orange input is connected. Foreground: That white foreground input is for wiring in other deep image nodes you’d like to combine with the background. You can feed this tool several foreground inputs simply by dragging extra connections between the nodes.

### Basic Node Setup

Into the dMerge node comes the background holding the deep image data. From there it lets you merge in additional deep image nodes so as to combine the data.

dMerge accepts deep image data from multiple sources and combines them.

### Common Controls

Settings Tab A copy of the Inspector’s Settings tab lives on other Deep Image nodes as well. These common controls receive full coverage at this chapter’s end, in the section called “The Common Controls.”
