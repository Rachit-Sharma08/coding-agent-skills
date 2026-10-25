# Camera 3D control visibility

Version: DaVinci Resolve 20.3 Reference Manual. Context: Camera 3D.
[Chapter index](INDEX.md) / [Previous section](camera-3d-parallel-3d-camera-setup.md) / [Next section](camera-3d-and-cube-3d-and-custom-vertex-3d.md) / [Camera 3D 3Cm](bender-3d-and-camera-3d.md)
<a id="source-camera-3d-image-plane-tab"></a> <a id="source-camera-3d-projection-tab"></a> <a id="source-common-controls"></a> <a id="source-control-visibility"></a> <a id="source-image-tab"></a> <a id="source-import-camera"></a> <a id="source-materials-tab"></a> <a id="source-projection-mode"></a> <a id="source-projection-tab"></a>

### Control Visibility

Here you can pick and choose which onscreen controls accompanying the camera get switched on.

- Show View Controls: Toggles every camera onscreen control in the viewers on or off.
- Frustum: Shows the camera's real viewing cone.
- View Vector: Shows a white line within the viewing cone, useful for gauging the

shift while you're in Parallel mode.

- Near Clip: The Near clipping plane. For clearer visibility, this plane is subdividable.
- Far Clip: The Far clipping plane. For clearer visibility, this plane is subdividable.
- Focal Plane: The plane derived from the Plane of Focus slider covered in the Controls tab above.

For clearer visibility, this plane is subdividable.

- Convergence Distance: Where convergence falls while Stereo mode is active. For clearer

visibility, this plane is subdividable.

### Import Camera

A dialog for bringing in a camera from another application opens when you press the Import Camera button. The file types it handles are these:

*LightWave Scene *Max Scene *Maya Ascii Scene *dotXSI

.lws .ase .ma .xsi

NOTE: FBX cameras come in by way of the Fusion > Import > FBX Scene menu within DaVinci Resolve, or through File > Import > FBX Scene over in Fusion Studio.

### Image Tab

Wire a 2D image into the magenta image input on the Camera3D node and an Image tab is generated at the inspector's top. That connected image always orients itself to fill the camera's field of view.

Apart from the controls noted below, this tab's options match those you'd typically meet on other 3D nodes. For fuller coverage of visibility, lighting, matte, blend mode, normals/tangents, and Object ID, consult the "The Common Controls" section at the close of this chapter.

### Camera 3D image plane tab

Enable Image Plane This checkbox switches use of the Image Plane on or off. Fill Method Should the camera carry a different aspect ratio, this menu sets how the image plane gets scaled.

- Inside: Uniform scaling grows the image plane until one of its dimensions (X or Y) meets the inside dimensions of the resolution gate mask. According to how the image source and the mask background compare in size, either the source's width or height may be trimmed to suit the mask's dimensions.
- Width: Uniform scaling grows the image plane until its width (X) meets the mask's width. According to how the image source and the resolution gate mask compare in size, the source's Y-dimension may fall short of the mask's Y-dimension, so the source is either cropped in Y or leaves the mask's height not fully covered.
- Height: Uniform scaling grows the image plane until its height (Y) meets the mask's height. According to how the image source and the resolution gate mask compare in size, the source's X-dimension may fall short of the mask's X-dimension, so the source is either cropped in X or leaves the mask's width not fully covered.
- Outside: Uniform scaling grows the image plane until one of its dimensions (X or Y) meets the outside dimensions of the resolution gate mask. According to how the image source and mask compare in size, either the source's width or height may be cropped or may not suit the respective dimension of the mask.
- Depth: The image plane's distance from the camera is governed by the Depth slider.

NOTE: How far the image plane sits from the camera is unaffected by the Camera Z position.

### Materials Tab

Whatever options the Materials tab presents line up with the ones you'd commonly meet on other 3D nodes. For more on the Diffuse, Specular, Transmittance, and Martial ID controls, consult the "The Common Controls" section at the close of this chapter.

### Projection Tab

Connect a 2D image to the camera node and a fourth projection tab shows up at the Inspector's top. Through this Projection tab, the image can be cast into the scene. What sets a projection apart from an image plane is that the projection lands on the scene's geometry precisely as though a real projector stood there in the scene. Because the image is cast as light, the Renderer 3D node has to have lighting enabled for the projection to show. Enable Camera Projection Tick this checkbox to switch on projection of the 2D image wired into the camera's magenta input. Projection Fit Method With this menu you choose the method that fits the projected image's aspect to the camera's field of view.

### Projection Mode

- Light: Defines the projection as a spotlight.
- Ambient Light: Defines the projection as an ambient light.
- Texture: Permits a projection that other lights can relight. To use this setting, a Catcher node must be wired to the relevant inputs of the material in question.

### Camera 3D projection tab

### Common Controls

Transform and Settings Tabs Whatever the Transform and Settings tabs present, you'll commonly find on other 3D nodes. For more on the controls held in these tabs, consult the "The Common Controls" section at the close of this chapter.
