# Ucamera and uduplicate

Version: DaVinci Resolve 20.3 Reference Manual. Context: Ucamera, Uduplicate.
[Chapter index](INDEX.md) / [Previous section](ucamera-universal-scene-descriptor-usd-files.md) / [Next section](uexport-and-uimage-plane-and-uloader.md) / [uCamera uCa](ucamera-universal-scene-descriptor-usd-files.md)
<a id="source-basic-node-setup-1"></a> <a id="source-common-controls"></a> <a id="source-control-visibility"></a> <a id="source-controls-tab-1"></a> <a id="source-inputs-1"></a> <a id="source-introduction"></a> <a id="source-scale"></a> <a id="source-the-uduplicate-controls"></a> <a id="source-the-usd-duplicate-node"></a> <a id="source-transform-method"></a> <a id="source-uduplicate-udp"></a> <a id="source-usage"></a>

### Control Visibility

From here you can pick and choose which of the onscreen controls shown beside the camera get turned on.

- Show View Controls: Shows or conceals every onscreen camera control in the viewers.
- Frustum: Shows the camera’s actual viewing cone.
- View Vector: Shows a white line running through the viewing cone that you can use to find the

center of the frame.

- Near Clip: The Near Clipping plane. You can subdivide this plane to see it more clearly.
- Far Clip: The Far Clipping plane. You can subdivide this plane to see it more clearly.
- Focal Plane: The plane established by the Focus Distance. You can subdivide this plane to see it

better.

- Convergence Distance: Where convergence occurs while in Stereo mode. You can subdivide this plane

to see it more clearly.

### Common Controls

Transform and Settings Tab The Inspector’s Transform and Settings tab is repeated across the other USD nodes as well. You’ll find a thorough description of these shared controls in the “The Common Controls” section near the close of this chapter.

### uDuplicate [uDp]

### The USD Duplicate node

### Introduction

Much like the 2D and 3D Duplicate nodes, the uDuplicate node lets you copy any USD asset within a scene, stacking a transformation onto each successive copy to build repeating models and elaborate arrays of objects. Settings on the Jitter tab make non-uniform transformations possible, for instance randomized placement or sizing.

### Inputs

By default the uDuplicate node offers just one input, into which you plug a USD scene. Depending on how the node is configured, an optional Mesh input may also show up. SceneInput: The orange Scene Input must be connected. Whatever scene or object you feed into this input gets duplicated according to the settings on the Inspector’s Control tab. MeshInput: A green optional mesh input shows up once the Region menu on the Region’s tab is set to mesh. That mesh may be any 3D model, whether built inside Fusion or brought in from elsewhere.

### Basic Node Setup

Most of the time the output of a uDuplicate node feeds a uMerge node, folding it into a bigger scene. The USD scene you’d like copied, here a USD scene of a Tokyo shophouse, gets wired into the orange input.

A USD scene of a Tokyo shophouse is duplicated.

### Usage

### The uDuplicate controls

### Controls Tab

On the Controls tab you’ll find every parameter for making, offsetting, and scaling copies of the USD object plugged into the node’s scene input. USD Instancing Switch this on and Fusion reuses the same USD data for every copy as an efficiency gain. That said, there are cases where the copies vary so much from one another that efficiency drops instead, in which case you can switch this setting off. Copies This range control determines how many copies get produced. Every copy derives from the previous one, so if you set the control to [0,3], first the parent gets duplicated, next that duplicate gets duplicated, after which the duplicate of the duplicate is duplicated, continuing onward. This opens the door to interesting effects once you apply transformations to each copy via the controls underneath. Raising the First Copy above 0 leaves the original object out and displays only the copies.

Time Offset The Time Offset slider shifts whatever animations sit on the source geometry by a fixed amount for each copy. As an illustration, set the value to -1.0 and feed in a cube animated to spin on the Y-axis as the source. The first copy plays the animation one frame back; the second copy plays it from one frame earlier still, and so on. Used on textured planes this can be striking—say, when each successive frame of a clip is put on display.

### Transform Method

- Linear: With Linear chosen, each transform is scaled by that copy’s number, and the overall scale, rotation, and translation are applied one after another, with no dependence on the other copies.
- Accumulated: With Accumulated chosen, every object copy begins where the previous object ended and is transformed onward from there. That outcome is then transformed again to produce the next copy

Transform Order This menu lets you set the sequence in which the transforms are worked out. Its default is ScaleRotation-Transform (SRT). Picking other orders lands your final objects in different positions.

Translation The X, Y, and Z Offset sliders fix the offset position given to each copy. An X offset of 1 shifts every copy 1 unit along the X-axis away from the preceding one. Rotation The row of buttons at the top of this rotation control group sets the sequence in which rotations hit the geometry. Choosing a rotation order of XYZ rotates around the X-axis first, then around the Y-axis, and finally around the Z-axis. The trio of Rotation sliders decides how much rotation each copy receives. Pivot The pivot controls fix where the pivot point sits as each copy is rotated.

### Scale

- Lock: With the Lock XYZ checkbox ticked, whatever you change on the duplicate scale takes effect on all three axes together. Untick the checkbox and the single Scale slider gives way to separate sliders for the X, Y, and Z scales.
- Scale: The Scale controls inform Duplicate how much scaling each copy should get.

uDuplicate Jitter tab Jitter Settings on the Jitter tab let you randomize the placement, rotation, and size across all the copies produced on the Controls tab. Random Seed The Random Seed slider seeds a random starting point for how much jitter lands on the duplicated objects. Take two Duplicate nodes with matching settings but distinct random seeds and they’ll yield two utterly different outcomes. Randomize Hit the Randomize button to have a random seed value generated for you. Jitter Probability Moving this slider sets what fraction of the copies the jitter touches. A setting of 1.0 reaches 100% of them, and a setting of 0.5 reaches 50%. Time Offset The Time Offset slider nudges whatever animations sit on the source geometry by a fixed amount for each copy. For instance, set the value to –1.0 and supply a cube animated to spin on the Y-axis as the source. The first copy plays the animation one frame back; the second copy plays it from a frame earlier still, and so on. On textured planes this works wonderfully—for example, when each successive frame of a clip is shown. Translation Jitter With these three controls you dial in the degree of variation across the X, Y, and Z translation applied to the duplicated objects.

Rotation Jitter With these three controls you dial in the degree of variation across the X, Y, and Z rotation applied to the duplicated objects. Pivot Jitter With these three controls you dial in the degree of variation in the rotational pivot center of the duplicated objects. This bears only on the extra jitter rotation, not on the rotation coming from the Rotation settings on the Controls tab. Scale Jitter This control lets you tune how much spread there is in the scale of the duplicated objects. Untick the Lock XYZ checkbox to vary the scale spread on each of the three axes on its own.

uDuplicate Region tab Region Tab Settings on the Region tab let you mark out a zone in the viewer where copies are either allowed to show up or kept from doing so. As with most Fusion parameters, you can animate this zone so the copied object pops on and off the screen according to the region’s shape and setting. Region Tab The Region section carries two settings that govern the region’s shape and how the region acts on the duplicate objects.

- Region Mode: The Region Mode menu offers three choices. Its default, “Ignore region,” skips the node altogether and leaves the object copies exactly as the Controls and Jitter tabs set them. The choice “When inside region” makes the copied objects show up only while their position lies within the region marked out on this tab. The final choice, “When not Inside region,” makes the copied objects show up only while their position lies beyond the region marked out on this tab.
- Region: The Region menu picks the region’s shape. Among its five choices are the cube, sphere, and rectangle primitive shapes. The mesh choice lets you wire a 3D model into the node’s green mesh input. That green input only turns up once the Region menu is set to Mesh. The All choice covers the whole scene. This lets the copies pop on and off whenever the Region mode is animated. Setting the Region menu to Mesh brings up two more options, covered just below.

Limit by Object ID: Once a scene holding several meshes is wired into the node’s green Mesh input, every mesh serves as the region. Tick this checkbox and you can use the Object ID slider to pick the ID of whichever mesh you want as the Region. Object ID: With the Limit by Object ID checkbox ticked, this slider chooses the number ID of the mesh object you intend to use for the Region.
