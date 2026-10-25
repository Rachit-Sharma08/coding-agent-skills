# Bender 3D and camera 3D

Version: DaVinci Resolve 20.3 Reference Manual. Context: Bender 3D, Camera 3D.
[Chapter index](INDEX.md) / [Previous section](alembic-mesh-3d-and-bender-3d.md) / [Next section](camera-3d-parallel-3d-camera-setup.md) / [Continue Camera 3D 3Cm / Film Back](camera-3d-parallel-3d-camera-setup.md) / [Bender 3D 3Bn](alembic-mesh-3d-and-bender-3d.md)
<a id="source-basic-node-setup-1"></a> <a id="source-basic-node-setup-2"></a> <a id="source-bender-3d-controls"></a> <a id="source-bender-3d-node-structure"></a> <a id="source-camera-3d-3cm"></a> <a id="source-camera-3d-controls"></a> <a id="source-camera-3d-node-introduction"></a> <a id="source-camera-projection"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab-1"></a> <a id="source-controls-tab-2"></a> <a id="source-inputs-1"></a> <a id="source-inputs-2"></a> <a id="source-inspector-1"></a> <a id="source-inspector-2"></a> <a id="source-off-axis"></a> <a id="source-off-axis-3d-camera-setup"></a> <a id="source-parallel"></a> <a id="source-stereo"></a> <a id="source-stereoscopic"></a> <a id="source-the-camera-3d-node"></a> <a id="source-toe-in-3d-camera-setup"></a>

### Inputs

On the Bender 3D node within the Node Editor the inputs below show up. SceneInput: That orange scene input stands as the required input for the Bender 3D node. Through it you wire in another node that builds or holds a 3D scene or object.

### Basic Node Setup

The way the Bender 3D node operates is by wiring in a 3D node holding geometry, such as an image plane 3D, Shape 3D or Text 3D. Whatever element you feed into the Bender 3D node ends up warped according to the controls over in the Inspector. The Bender 3D node is meant to form part of a bigger 3D scene, its output as a rule feeding on into a Merge 3D.

### Bender 3D node structure

### Inspector

### Bender 3D controls

### Controls Tab

Heading the Inspector is the Controls tab. Within it sit all the controls for the Bender 3D node. Bender Type Through the Bender Type menu you pick which kind of deformation gets applied to the geometry. Four modes are on offer: Bend, Taper, Twist, and Shear.

Amount Dragging the Amount slider varies how strong the deformation is. Axis The Axis control sets which axis the deformation runs along. Its sense changes with the type of deformation in play. When bending, for one, it picks the elbow working together with the Angle control. In the remaining cases, the deform wraps around the named axis. Angle The Angle thumbwheel control fixes which direction about the axis a bend or shear runs. It stays hidden for taper or twist deformations. Range Through the Range control you can pen the reach of a deformation into a slim slice of the geometry. The Range control goes away once the Bender Type is set to Shear. Group Objects Should the input of the Bender 3D node hold several 3D objects, whether by way of a Merge 3D or chained together, the Group Objects checkbox handles every object in the input scene as one object, and the shared center drives the deformation of the objects rather than warping each component object on its own.

### Common Controls

Settings Within the Inspector the Settings tab is shared by every 3D node. Full coverage of this shared tab waits at the close of this chapter inside the “The Common Controls” section.

### Camera 3D [3Cm]

### The Camera 3D node

### Camera 3D Node Introduction

A virtual camera for looking into the 3D environment is what the Camera 3D node produces. It mirrors closely the settings found on real cameras, so that pairing live-action or 3D-rendered elements stays as seamless as it can be. Dropping any cameras into a 3D composite lets you frame the elements of a composite to taste and animate the camera over a scene to build moving camera shots.

### Camera Projection

The Camera 3D node also serves to carry out Camera Projection, casting a 2D image through the camera out into 3D space. Casting a 2D image works either as a plain Image Plane lined up with the camera, or as a genuine projection — much like how the Projector 3D node behaves — with the extra benefit that it lines up exactly with the camera. The Image Plane, Projection, and Materials tabs stay hidden until you wire a 2D image into the magenta image input on the Camera 3D node within the Node Editor.

### Stereoscopic

Built into the Camera node are stereoscopic features. They hand you control over eye separation and convergence distance. A separate camera node wired into the green left/right stereo camera input can stand in for the right-eye camera. On top of that, the plane of focus control for depth of field rendering lives here as well. Drag the camera icon off the toolbar onto the 3D view and the camera you add hooks up on its own to the Merge 3D you happen to be viewing. What's more, the current viewer gets pointed through the new camera. As another path, you can copy the current viewer onto a camera (or spotlight or any other object) by picking the Copy PoV To option within the viewer’s contextual menu, down under the Camera submenu.

### Inputs

Three optional inputs sit on the Camera 3D node within the Node Editor. SceneInput: That orange input serves to wire in a 3D scene or object. Once wired, the geometry ties to the camera’s field of view. It behaves much like an image hung off the Image Plane input. Where the camera’s Projection tab has projection switched on, the image hung off the orange image input casts onto the geometry. ImageInput: The optional magenta input serves to wire in a 2D image. With camera projection switched on, the image can stand in as a texture. As another path, where the camera’s image plane controls come into play, the parented planar geometry ties to the camera’s field of view. RightStereoCamera: The green input ought to be wired into a second Camera 3D node while crafting 3D stereoscopic effects. It serves to override the internal camera that drives the right eye across stereoscopic renders and viewers.

### Basic Node Setup

A camera 3D node's output ought to feed into a Merge 3D node. You then look at the Merge 3D node and choose the camera out of the viewer’s right-click menu or by right-clicking on the axis label within the viewer.

Camera node connected to and viewed through the Merge 3D Putting a camera node straight into the viewer reveals only a bare scene; the camera has nothing to look at. To peer through the camera at the scene, look at the Merge 3D node where the camera hooks up, or any node downstream of that Merge 3D. After that, right-click on the viewer and pick Camera > [Camera name] off the contextual menu. Right-clicking on the axis label down in the lower corner of each 3D viewer likewise brings up the Camera submenu.

The viewer's aspect can differ from the camera's aspect, so the camera view might not line up with the true bounds of the image that the Renderer 3D node puts out. Guides can be switched on to stand for the slice of the view the camera takes in and help you frame the shot. Right-click on the viewer and pick an option off the Guides > Frame Aspect submenu. By default that option draws on the format switched on in the Composition > Frame Format preferences. To flip the guides on or off, pick Guides > Show Guides off the viewers’ contextual menu, or reach for the Command-G (macOS) or Ctrl-G (Windows) keyboard shortcut while the viewer is active.

### Inspector

### Camera 3D controls

### Controls Tab

Six tabs run across the top of the Camera3D Inspector. The opening one, named the Controls tab, holds several of the most basic camera settings; among them you'll find stereoscopic properties together with the camera’s focal length, its field of view, and its clipping plains. Certain tabs stay hidden until a needed connection reaches the Camera 3D node. Projection Type Through the Projection Type menu you pick between Perspective and Orthographic cameras. By and large, real-world cameras are perspective cameras. An orthographic camera leans on parallel orthographic projection, an approach where the view plane sits perpendicular to the viewing direction. The upshot is a parallel camera output free of perspective distortion. Orthographic cameras surface controls just for the near and far clipping planes, alongside one control that sets the viewing scale. Near/Far Clip By way of the clipping planes you bound which geometry in a scene gets rendered, going by an object’s distance from the camera’s focal point. Clipping planes make sure that objects sitting extremely close to the camera, together with objects too distant to matter, drop out of the final rendering.

By default the perspective camera pays this setting no mind unless the Adaptive Near/Far Clip checkbox sitting under the Near/Far Clip control is switched off. The clip values run in units, so a far clipping plane of 20 means any object beyond 20 units from the camera goes unseen by the camera. A near clipping plane of 0.1 means any object nearer than 0.1 units likewise goes unseen. NOTE: Keeping a tighter range between the near and far clipping planes affords more precision throughout every depth calculation. Should a scene start to throw odd artifacts on distant objects, try pushing the distance for the Near Clip plane higher. Adaptive Near/Far Clip Switched on, the renderer tunes the camera’s near/far clipping plane on its own to fit the reach of the scene. This setting trumps the values of the Near and Far clip range controls covered above. The option is missing for orthographic cameras. Viewing Volume Size Once the Projection Type sits at Orthographic, the viewing volume size adjustment surfaces. It fixes the size of the box forming the camera’s field of view. An orthographic camera's Z-distance from the objects it takes in has no bearing on how those objects are scaled; the viewing size alone governs that. Angle of View Type Reach for the Angle of View Type buttons to settle how the camera’s angle of view gets measured. Certain applications go by vertical measurements, some by horizontal, others by diagonal measurements. Switching the Angle of View type makes the Angle of View control below recompute. Angle of View Angle of View sets out the slice of the scene viewable through the camera. As a rule, the human eye takes in more of a scene than a camera does, and assorted lenses record differing shares of the whole image. A big value yields a wider angle of view, while a smaller one yields a narrower, or more tightly framed, angle of view. Exactly as on a real-world camera, the angle of view and focal length controls tie directly together. Shorter focal lengths yield a wider angle of view, so nudging one control nudges the other to keep pace. Focal Length Out in the real world, a lens’ Focal Length measures how far the film plane sits from the lens's center. The briefer that focal length, the nearer the focal plane draws to the back of the lens. Focal length gets measured in millimeters. The angle of view and focal length controls tie directly together. Shorter focal lengths yield a wider angle of view, so nudging one control nudges the other to keep pace. The bond between focal length and angle of view runs angle = 2 \* arctan[aperture / 2 / focal_length]. Feed in the vertical aperture size to land the vertical angle of view and the horizontal aperture size to land the horizontal angle of view. Plane of Focus (For Depth of Field) Much like a focal point on a real-world camera, this setting fixes the span from the camera out to an object. The OpenGL renderer within the Renderer 3D node draws on it to work out depth of field.

### Stereo

Within the Stereo section sit options for arranging 3D stereoscopic cameras. The way 3D stereoscopic composites operate is by grabbing two slightly different views, shown apart to the left and right eyes. Through the mode menu you settle whether the current camera runs as a stereoscopic setup or a mono camera. Left at the default mono setting, the camera takes in the scene the way a traditional 2D film camera would. Three further options in the mode menu fix which method drives the 3D stereoscopic cameras. Toe In Under a toe-in setup, both cameras swing inward toward a single focal point. The outcome is stereoscopic, yet the vertical parallax this method brings in can leave the audience uncomfortable. Toe-in stereoscopic holds up for convergence around the middle of the images but shows keystoning, or image separation, toward the left and right edges. Such a setup can come into play when the focus point and the convergence point have to coincide. It also serves in cases where it stands as the only route to match a live-action camera rig.

### Toe In 3D camera setup

### Off Axis

Held to be the proper way to build stereo pairs, this is the method Fusion picks by default. Off Axis brings in no vertical parallax, thereby producing stereo images that ease eye strain. At times dubbed a skewed-frustum setup, it parallels a lens shift out in the real world. Rather than swinging the two cameras inward as a toe-in setup does, Off Axis slides the lenses inward.

### Off Axis 3D camera setup

### Parallel

Here the cameras slide parallel to one another. Because this amounts to a purely parallel shift, no Convergence Distance control exists, which caps how much say you have over placing objects ahead of or behind the screen. That said, Parallel brings in no vertical parallax, thereby easing the strain on the eyes.
