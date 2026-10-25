# Soft clip and spherical camera and text 3D

Version: DaVinci Resolve 20.3 Reference Manual. Context: Soft clip, Spherical camera, Text 3D.
[Chapter index](INDEX.md) / [Previous section](soft-clip-basic-node-setup.md) / [Next section](text-3d-text-tab.md) / [Continue Text 3D 3Txt / Text 3D Modifiers](text-modifier-behavior.md) / [Soft Clip 3SC](ribbon-3d-and-shape-3d-and-soft-clip.md)
<a id="source-basic-node-setup"></a> <a id="source-common-controls"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab"></a> <a id="source-controls-tab-1"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-inspector-1"></a> <a id="source-layout"></a> <a id="source-soft-clip-controls"></a> <a id="source-spherical-camera-3sc"></a> <a id="source-spherical-camera-controls"></a> <a id="source-spherical-camera-node-introduction"></a> <a id="source-spherical-camera-placed-inside-a-sphere"></a> <a id="source-text-3d-3txt"></a> <a id="source-text-3d-node-introduction"></a> <a id="source-the-spherical-camera-node"></a> <a id="source-the-text-3d-node"></a>

### Inspector

### Soft Clip controls

### Controls Tab

By way of the Controls tab you set how an object shifts from opaque to transparent as it nears the camera. Enable This checkbox switches the node on or off. It isn't the same thing as the red switch up in the Inspector's top-left corner. That red switch shuts the tool down completely and lets the image pass through unaltered. The Enable checkbox reaches only as far as the tool's effect. The rest, such as scripts on the Settings tab, keeps processing as usual. Smooth Transition By default, an object drawing nearer and nearer to the camera gradually fades away along a linear progression. Switch the Smooth Transition checkbox on, and that fade turns into a nonlinear curve, which is arguably a more natural-looking transition. Radial By default, the soft clipping works off the perpendicular distance to a plane (parallel to the near plane) that passes through the eye point. Tick the Radial option, and the Radial distance to the eye point takes the place of the Perpendicular distance. The trouble with Perpendicular distance soft clipping is that as you swing the camera around, objects along the frustum's left or right edge grow less clipped as they drift toward the center, even though their distance from the eye hasn't changed. Radial soft clip remedies this. Now and then Radial soft clipping isn't what you want. As an example, apply soft clip to an object sitting near the camera, say an image plane, and the image plane's center could stay unclipped while its edges end up fully clipped, since they sit farther from the eye point. Show In Display Views Ordinarily the effect surfaces only when a Camera node is used to view the scene. Switch this on, and the soft clip turns visible in the scene from every vantage point. Transparent/Opaque Distance Sets the soft clip's range. The objects start fading in from an opacity of 0 at the Transparent distance and reach full visibility at the Opaque distance. Every unit is given as distance from the camera along the Z-axis.

### Common Controls

Settings Tab The Inspector's Settings tab recurs across other 3D nodes. These shared controls get a full treatment toward this chapter's close, in the "The Common Controls" section.

### Spherical Camera [3SC]

### The Spherical Camera node

### Spherical Camera Node Introduction

By way of the Spherical Camera, the 3D Renderer node can put out an image spanning every viewing angle, arranged in any of several formats. You might apply that image as a skybox texture or a reflection map, or view it through a VR headset. The Image Width setting over in the 3D Renderer fixes how large each square cube face is, so the resulting image can run to a multiple of that size both horizontally and vertically.

### Inputs

Two inputs sit on the Spherical camera node. Image: This orange image input calls for an image laid out spherically, whose format may be any one of these — LatLong (2:1 equirectangular), VR180, Horizontal/Vertical Cross, plus Horizontal/Vertical Strip. Stereo Input: Working in stereo VR, you'd feed a right stereo camera through the green input. Neither input is mandatory.

### Basic Node Setup

For the most part, setting up the Spherical Camera works just as it does for the ordinary Camera 3D node. The camera's output wires into a Merge 3D. As a rule, the Merge 3D draws on a picture in LatLong or H Cross/V Cross format, fed either straight in or by way of a Panomap node. That image gets wrapped around a sphere, with the camera set inside the sphere.

### Spherical Camera placed inside a sphere

### Inspector

### Spherical Camera controls

### Controls Tab

### Layout

- VCross and HCross: VCross and HCross take the six square faces of a cube and lay them out in a cross, either vertical or horizontal, the forward view sitting at the cross's center, within a 3:4 or 4:3 image.
- VStrip and HStrip: VStrip and HStrip take the six square faces of a cube and lay them in a line, vertically or horizontally, in the order Left, Right, Up, Down, Back, Front (+X, -X, +Y, -Y, +Z, -Z), within a 1:6 or 6:1 image.
- LatLong: LatLong is a lone 2:1 image carrying equirectangular mapping.
- VR 180 is a 1:1 180 degree stereoscopic image.

Near/Far Clip The clipping plane serves to cap which scene geometry gets rendered, going by each object's distance from the camera's focal point. This comes in handy for keeping objects sitting extremely close to the camera out of the render, and for trimming a render so objects too distant to matter in the final output get left out. Unless the Adaptively Adjust Near/Far Clip checkbox control further down is switched off, the default perspective camera pays this setting no mind. The values come in units, so a far clipping plane of 20 means anything past 20 units from the camera stays invisible to it. Likewise, a near clipping plane of 0.1 means anything nearer than 0.1 units stays invisible too. Adaptively Adjust Near/Far Clip With this on, the Renderer tunes the camera's near/far clipping plane on its own to fit the scene's extents. The setting supersedes the values held by the Near and Far clip range control covered above. The option isn't on offer for orthographic cameras.

Viewing Volume Size The Viewing Volume Size control turns up only when the Projection Type is set to Orthographic. It fixes how large the box forming the camera's field of view is. How far, along Z, an orthographic camera stands from the objects it captures doesn't change those objects' scale; only the viewing size does. NOTE: Keeping the gap between the near and far clipping plane tighter buys greater precision across all depth calculations. Should a scene start rendering odd artifacts on distant objects, try pushing the near clip plane's distance up. Read the vertical angle of view off the vertical aperture size, and the horizontal angle of view off the horizontal aperture size. Plane of Focus (for Depth of Field) The OpenGL renderer leans on this value to work out depth of field. It marks the distance to a virtual target set ahead of the camera. Stereo Method This control lets you tailor your stereoscopic method to the working model you favor. Toe In Both cameras aim at one shared focal point. The outcome is stereoscopic, yet the vertical parallax this method brings in can leave the audience uncomfortable. Off Axis Widely held to be the proper way to build stereo pairs, this is Fusion's default method. Off Axis brings in no vertical parallax, so it yields less stressful stereo images. Parallel The cameras get shifted parallel to one another. Because this amounts to a purely parallel shift, no Convergence Distance control exists. Parallel brings in no vertical parallax, so it yields less stressful stereo images. Eye Separation Sets how far apart the two stereo cameras stand. Should Eye Separation carry a value above 0, each camera's controls show up in the viewer whenever this node is selected. Parallel mode carries no Convergence Distance control. Convergence Distance This control fixes the stereoscopic convergence distance, taken as a point sitting along the camera's Z-axis where both the left and right eye cameras meet. Control Visibility Lets you pick and choose which of the onscreen controls shown alongside the camera are active.

- Frustum: Displays the actual viewing cone of the camera.
- View Vector: Shows a white line within the viewing cone, handy for gauging the

shift when in Parallel mode.

- Near Clip: The Near clipping plane. You can subdivide it so it shows up more clearly.
- Far Clip: The Far clipping plane. Subdividing this one likewise improves how visible it is.
- Plane of Focus: The camera focal point, going by the Plane of Focus slider covered above. Subdivide it for clearer visibility.
- Convergence Distance: Where convergence falls while Stereo mode is in use. This plane, too, can be subdivided to read more clearly.

### Common Controls

Settings Tab The Inspector's Settings tab recurs across other 3D nodes. These shared controls get a full treatment toward this chapter's close, in the "The Common Controls" section.

### Text 3D [3Txt]

### The Text 3D node

### Text 3D Node Introduction

The Text3D node is the 3D counterpart of the 2D Text+ node. This node's controls match those of the 2D version almost point for point, save that Text 3D handles just one shading element. The Text 3D node grew out of a tool predating the Fusion 3D environment. For that reason, some of the controls present on the basic primitive shapes and geometry loaders, among them many of the material, lighting, and matte options, don't turn up among this node's controls. Text 3D ships with a built-in material, yet unlike the other 3D nodes it carries no material input. The Shading tab holds controls for tuning the diffuse and specular components. To swap that default material for a more capable one, place a Replace Material 3D node after the Text Plus node. The Override 3D node lets you steer this node's lighting, visibility, and matte options. While network rendering a comp holding Text 3D nodes, every render machine must carry the needed fonts, or the network rendering breaks down. Fusion neither shares nor copies fonts out to render slaves.
