# Transformations and transform tab of a merge3d node

Version: DaVinci Resolve 20.3 Reference Manual. Context: 3D compositing basics.
[Chapter index](INDEX.md) / [Previous section](3d-view-navigation-camera-and-light-transforms.md) / [Next section](camera-view-focus-plane-and-depth-of-field.md)
<a id="source-a-torus-facing-its-onscreen-target-controls"></a> <a id="source-cameras"></a> <a id="source-onscreen-transform-controls"></a> <a id="source-parenting"></a> <a id="source-pivot"></a> <a id="source-selecting-objects"></a> <a id="source-target"></a> <a id="source-the-transform-tab-of-a-merge3d-node"></a> <a id="source-transformations"></a> <a id="source-using-onscreen-transform-controls"></a>

### Transformations

Merge3D, 3D Objects, and Transform3D each carry Transform parameters gathered into a Transform tab within the Inspector. The parameters in this tab govern how the object is positioned, rotated, and scaled inside the scene.

### The Transform tab of a Merge3D node

The Translation parameters place the object in local space, the Rotation parameters turn the object about its own center, and the Scale slider(s) change its size (which depends on whether they are locked together). Those same adjustments can be done in the viewer through onscreen controls.

### Onscreen Transform Controls

A selected object shows onscreen Transform controls in the viewers so you can set the object's position, rotation, and scale. You switch modes either with buttons in the Transform toolbar or with the keyboard shortcuts. The keyboard shortcuts for changing Transform modes are:

- Press Q for Position
- Press W for Rotation
- Press E for Scaling

The Position, Rotation, and Scale modes in the Transform toolbar

### Using Onscreen Transform Controls

Across all three modes, red stands for the object's local X-axis, green for the Y-axis, and blue for the Z-axis (just keep RGB = XYZ in mind). Drag straight on the red, green, or blue part of any onscreen control to pin the transform to that axis, or drag the onscreen control's center to transform with no constraint. Holding Option and dragging in the viewer lets you translate freely along all three axes without clicking any particular control.

From left to right, the Position, Rotation, and Scale onscreen Transform controls With the Scale's Lock XYZ checkbox turned on in the Inspector, dragging the red or center onscreen control changes only the object's overall scale, and the green and blue parts of the control do nothing. Unlock the parameters and you can scale an object on individual axes one at a time, squishing or stretching it.

### Selecting Objects

While the onscreen controls show in the viewer, click an object's center control to select it. You can equally select any 3D object by clicking its node within the Node Editor.

### Pivot

Within 3D scenes, objects turn and scale about an axis known as a pivot. By default that pivot runs through the object's center. To shift the pivot away from the object's center, reach for the X, Y, and Z Pivot parameters in the Inspector.

### Target

Targets help aim a 3D object at a particular point in the scene. Wherever the object travels, it turns in the local coordinate system so that it keeps facing its target, which you can place and animate.

To switch on a target for a 3D object: 1 Pick that object's node. 2 Within the Inspector, open the object's Transform panel. 3 Tick the Use Target checkbox.

Turning on the Use Target checkbox of a 3D object 4 Place the target with the Inspector's X/Y/Z Target Position controls or the viewer's Target onscreen control, which in turn places the object tied to it. The viewer draws a line from the target to the center of the 3D object it is attached to, conveying the link between these two control sets. Every time the target moves, the object transforms automatically to face the new position.

### A torus facing its onscreen Target controls

For instance, when a spotlight in the scene must aim at an image plane, switch on the spotlight's target in the Transform tab and tie the target's XYZ position to the image plane's XYZ position. From then on, wherever the spotlight moves, it turns to face the image plane.

A light made to face the wall using its enabled target control

### Parenting

A notable benefit of the node-based take on 3D compositing is that parenting among objects falls out implicitly from how a 3D node tree is built. Every bit of parenting rests on the Merge3D node. Connect the various 3D objects you build for your scene thoughtfully, and several Merge3D nodes can govern which groups of objects transform and animate as a unit and which do so on their own. Picture, for example, a scene holding two spheres both wired to a Merge3D. That Merge3D can spin one sphere around the other, the way the moon circles the earth. The Merge3D can then feed another Merge3D so the earth and moon orbit the sun together.

A single Merge3D whose two spheres are parented to a further Merge3D, plus parenting built from three connected spheres

The two plain rules for transforming parented Merge3D nodes are:

- Any transform or animation put on a Merge3D carries to every 3D object wired to that Merge3D node, cameras, lights, geometry, and other merge nodes connected upstream included.
- Any transform or animation put on upstream merge nodes leaves downstream merge nodes untouched.

### Cameras

As you build and animate a 3D scene, the camera metaphor ranks among the most intuitive ways to frame how you want the scene rendered and to animate your path through it. On top of that, compositing artists are often asked to match cameras drawn from live-action clips or from 3D applications. To serve all of this, Fusion supplies a flexible Camera3D node carrying familiar camera controls like Angle of View, Focal Length, Aperture, and Clipping planes, so you can either build your own camera or pull in camera data from other applications. The Camera3D node acts as a virtual camera you view the 3D environment through.

A camera shown in the viewer with onscreen Transform controls, its Focal Plane indicator switched on in green A Merge3D node usually connects and views cameras; even so, you can wire cameras upstream of other 3D objects when you want a camera to transform alongside that object as it moves.
