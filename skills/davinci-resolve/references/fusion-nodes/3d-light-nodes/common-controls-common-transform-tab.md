# Common controls common transform tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Common controls.
[Chapter index](INDEX.md) / [Previous section](spot-light-common-controls.md)
<a id="source-common-settings-3d-controls"></a> <a id="source-common-transform-3d-tab"></a> <a id="source-common-transform-tab"></a> <a id="source-import-transform"></a> <a id="source-onscreen-transformation-controls"></a> <a id="source-pivot"></a> <a id="source-rotation"></a> <a id="source-scale"></a> <a id="source-settings-tab"></a> <a id="source-the-common-controls"></a> <a id="source-translation"></a> <a id="source-use-target"></a> <a id="source-viewer-transform-buttons"></a> <a id="source-x-y-z-rotation"></a>

### The Common Controls

Several of the same controls in the Inspector are shared by the nodes responsible for 3D lighting. The controls detailed in this section are the ones held in common across the 3D lighting nodes.

### Common Transform Tab

### Common Transform 3D tab

A great many tools belonging to the 3D category carry a Transform tab, which serves to position, rotate, and scale the object throughout 3D space.

### Translation

X, Y, Z Offset You can rely on these controls to place the 3D element.

### Rotation

Rotation Order These buttons let you choose the sequence in which Rotation gets applied to each of the object’s axes. As an illustration, XYZ would rotate the X axis first, then the Y axis next, and lastly the Z axis.

### X, Y, Z Rotation

These control let you spin the object about its pivot point. Whenever the Use Target checkbox is turned on, the rotation references the target’s position; if it is not, the global axis governs instead.

### Pivot

X, Y, Z Pivot An object turns about its pivot point, which is exactly the spot it rotates around. By default an object spins about its own midpoint, treated as a pivot of 0,0,0. With these controls you can shift the pivot away from the center.

### Scale

X, Y, Z Scale With the Lock X/Y/Z checkbox enabled, only one Scale slider appears. It changes the object’s size as a whole. Should the Lock checkbox be turned off, separate X, Y, and Z sliders show up so each dimension can be scaled on its own. Note: While the Lock checkbox stays enabled, you cannot scale individual dimensions, not even by dragging particular axes of the Transformation Widget in scale mode.

### Use Target

Turning on the Use Target checkbox brings up a group of controls for placing an XYZ target. With Target active, the object will continually rotate so it faces the target. The object’s rotation then becomes relative to the target.

### Import Transform

Brings up a file browser in which you can choose a scene file that your 3D application has saved or exported. The file types it accepts are:

LightWave Scene Max Scene Maya Ascii Scene dotXSI

.lws .ase .ma .xsi

Only transformation data is brought in by the Import Transform button. To handle 3D geometry, lights, and cameras, look instead to the File > FBX Import option.

### Onscreen Transformation Controls

### Viewer Transform buttons

Viewer Transform buttons The majority of the controls on the Transform tab also appear in the viewer as onscreen handles for transformation, rotation, and scaling. You switch the mode of these onscreen controls by clicking one of the three buttons sitting in the toolbar at the viewer’s upper left. The modes are also toggled from the keyboard, where each shortcut maps a mode: Q for translation, then W handles rotation, while E covers scaling. Within any of the three modes, you may drag a single axis of the control to affect that axis alone, or drag the control’s center to affect all three axes together. For the bulk of 3D tools the Scale sliders start out locked, producing uniform scaling across all three axes. Release the Lock X/Y/Z Scale checkbox in order to scale an object along just one axis.

### Settings Tab

### Common Settings 3D controls

Nearly every tool in Fusion carries the Common Settings tab. The controls described below are the settings particular to 3D nodes. Hide Incoming Connections Turning on this checkbox lets you conceal the connection lines coming from incoming nodes, which keeps a node tree looking tidier and easier to follow. Once enabled, a field for each input on a node shows up. When you drag a connected node out of the node tree and into the field, that incoming connection line stays hidden so long as the node remains unselected within the node tree. As soon as the node is selected in the node tree, the line comes back. Comment Tab Inside the Comment tab is a lone text control meant for attaching comments and notes to the tool. Once a note is attached to a tool, a tiny red dot icon shows up beside the setting’s tab icon, and a text bubble surfaces on the node. You can view the note in the Node Editor by holding the mouse pointer over the node briefly. If you need it, the material in the Comments tab can be animated across time. Scripting Tab Every tool in Fusion includes the Scripting tab. Within it are several edit boxes for entering scripts that run as the tool renders. For fuller detail on what this tab holds, please refer to the scripting documentation.
