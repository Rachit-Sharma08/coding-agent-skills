# Ushape and uswitch and utransform

Version: DaVinci Resolve 20.3 Reference Manual. Context: Ushape, Uswitch, Utransform.
[Chapter index](INDEX.md) / [Previous section](urenderer-and-ureplacematerial-and-ushape.md) / [Next section](utransform-and-uvariant-and-uvisibility-and-uvolume.md) / [uShape uSh](urenderer-and-ureplacematerial-and-ushape.md)
<a id="source-basic-node-setup-3"></a> <a id="source-common-controls-2"></a> <a id="source-common-controls-3"></a> <a id="source-config"></a> <a id="source-controls-1"></a> <a id="source-controls-tab-1"></a> <a id="source-inputs-3"></a> <a id="source-inputs-4"></a> <a id="source-inspector-2"></a> <a id="source-inspector-3"></a> <a id="source-material-tab"></a> <a id="source-the-usd-shape-controls"></a> <a id="source-the-usd-shape-material-controls"></a> <a id="source-the-uswitch-configuration"></a> <a id="source-uswitch-usw"></a> <a id="source-utransform-uxf"></a>

### Inspector

### The USD Shape Controls

### Controls Tab

Shape This menu is where you select which primitive geometry the Shape 3D node builds. The rest of the Inspector's controls adapt to match your chosen shape. The available Shape primitives: Capsule, Cone, Cube, Cylinder, Ico sphere, Plane, Sphere and Torus. Double Sided Gives the polygons a pair of faces, letting them receive lighting from both sides. Lock Width/Height/Depth Only for Plane and Cube shapes. Tick this checkbox and the width, height, and depth controls bind together into one size slider; leave it unticked and you get separate control over the shape's size along each axis. Size Width/Height/Depth Only for Plane and Cube shapes. Governs how big the shape is. Radius With a Capsule, Sphere, Cylinder, Cone, or Torus chosen in the shape menu, this control sets the chosen shape's radius. Height With a Capsule, Cone, or Cylinder chosen in the shape menu, this control sets the chosen shape's height. Top Radius With a cone chosen in the Shape menu, this control defines a radius for the cone's top, which makes truncated cones possible. Subdivision Level/Base/Height/Cap/Cylinder The Subdivision controls govern the mesh tessellation on every shape. A higher subdivision means more vertices and polygons per shape.

Subdivision Scheme Which algorithm tessellates the polygons in the shapes is set by the Subdivision Scheme. The methods are None, Bilinear, Loop and Catmull-Clark. Angle With the Capsule, Cone, Cylinder, Sphere, or Torus shape chosen in the Shape menu, this range control sets how much of the shape gets drawn. A start angle of 180° together with an end angle of 360° would render only half the shape. Latitude With a Sphere or Torus chosen in the Shape menu, this range control crops or slices the object by carving out a latitudinal subsection of it. Cap Bottom/Top With Cylinder or Cone chosen in the Shape menu, the Bottom Cap and Top Cap checkboxes decide whether these shapes get end caps or are left open Section With the Torus chosen in the Shape menu, Section governs the thickness of the tube that forms the torus.

### Material Tab

### The USD Shape Material controls

Diffuse Mode Diffuse captures a surface's base traits, leaving out extras such as reflections or specular highlights.

- Color: Supplies controls for adjusting the shape's diffuse color.
- Texture: This control lets a source image serve as the diffuse surface color. Press the

Browse button to bring up the file browser and pick an image file. Emissive Emissive lends a shape a global lighting effect, laying a color layer over the texture already in place. Its intensity is adjustable across various levels, and it can mimic the emission of light.

Workflow Mode Lets you set the mode between Metallic and Specular.

- Metallic: Once enabled, this control reveals the Metallic slider, which lends objects a reflective character, conjuring the look of metal and strengthening a shape's reflective properties.
- Specular: Once enabled, this surfaces the Specular Color controls. Specular Color fixes the color of light bouncing off a shiny surface; the more specular the material, the glossier its look.

Roughness Shapes how much light a surface reflects and scatters, lending it a smoother or rougher appearance per the setting. It's central to producing believable reflections. Clearcoat Alters a surface's look by laying a glossy layer over it, imitating a protective coating. Materials such as car paint or polished metal commonly use it. Clearcoat Roughness Dials in how flawed or smooth that overlaid glossy layer appears, which can sway how realistic and reflective materials such as car paint or polished metal look. Opacity Cuts the opacity of the material and object, affecting the shape's color and Alpha values.

### Common Controls

Transform and Settings Tab Other USD nodes likewise duplicate the Inspector's Transform and Settings tab. Detailed coverage of these common controls sits at this chapter's end, in the "The Common Controls" section.

### uSwitch [uSw]

The uSwitch node uSwitch Node Introduction Much like Switch, uSwitch works in a comparable way but is built specifically for the USD environment. uSwitch is a tool letting artists flip among several USD input sources and pick a single output from whichever inputs they've chosen. That makes it particularly handy for switching between different visual elements inside a composition. The count of input connections is flexible, the node accommodating a dynamic number of inputs that can be renamed at will. Controls on the Config tab let users add or drop inputs and rename them.

### Inputs

A uSwitch node accepts as many as nine inputs, added via the slider in the Config tools. Need more than nine sources? You can type that figure straight into the Number of Inputs field.

### Basic Node Setup

Hook up however many input sources you want to the uSwitch Node, then wire its output into the remainder of the node tree.

The uSwitch tool taking in five USD media inputs, letting you select one to send out to uRender.

### Inspector

Through the uSwitch controls you select which source passes through the switch.

### Controls

A Source switcher makes up the Switch Controls, letting you decide which source passes through the switch.

### The uSwitch configuration

### Config

Through the uSwitch configuration you set the input count and rename them.

- Number of Inputs: Drag the slider to set how many inputs you want, up to nine. For more than nine inputs, click into the number field and enter the figure by hand.
- Name X: A numerical input name can be swapped for something more descriptive.

### Common Controls

Settings Tab Across the other USD nodes, the Inspector's Settings tab appears in duplicate form too. A thorough rundown of these common controls lives in the closing "The Common Controls" section of this chapter.

### uTransform [uXF]

The USD Transform node uTransform Node Introduction When your USD scene holds several objects or prims, the uTransform node lets you single out individual groups of objects and adjust their transform on their own, apart from the rest of the scene.

### Inputs

One required input for a USD scene or USD object feeds the uTransform node. Scene Input: Wire the orange scene input to a USD scene or USD object to layer on a second set of transformation controls.
