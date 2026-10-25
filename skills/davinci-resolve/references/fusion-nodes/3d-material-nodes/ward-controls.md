# Ward controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Ward.
[Chapter index](INDEX.md) / [Previous section](phong-and-reflect-and-stereo-mix.md) / [Next section](ward-specular.md) / [Continue Ward 3Wd / Specular](ward-specular.md)
<a id="source-basic-node-setup-4"></a> <a id="source-controls-tab-4"></a> <a id="source-inputs-4"></a> <a id="source-inspector-2"></a> <a id="source-the-ward-node"></a> <a id="source-ward-3wd"></a> <a id="source-ward-controls"></a> <a id="source-ward-node-introduction"></a>

### Ward [3Wd]

### The Ward node

### Ward Node Introduction

A basic illumination material, the Ward node can be draped over geometry within the 3D scene. It sets out the object’s response to light and exposes several texture map inputs for fine command of the material’s diffuse, specular, and bump map components. In particular, the Ward node excels at faking brushed metal surfaces, since its highlight can be stretched along the U or V axes of the mapping coordinates — what’s termed an anisotropic highlight. The Ward node emits a 3D Material that wires into the material inputs of any 3D geometry node.

### Inputs

Six inputs live on the Ward node, every one taking a 2D image or a 3D material. They command the overall color and imagery of the 3D object plus the color and texture driving the specular highlight. Each scales the texture map’s pixels by the matching parameter on the node itself, a tidy way to scale portions of the material. Diffuse Material: The orange Diffuse material input takes a 2D image or a 3D material supplying the object’s main color and texture. Specular Color Material: The green Specular Color material input takes a 2D image or a 3D material supplying the object’s highlight color and texture.

Specular Intensity Material: The magenta Specular Intensity material input takes a 2D image or a 3D material that works as an intensity map for the material’s highlights. Where that input is a 2D image, its Alpha channel forms the map while the color channels get dropped. Spread U Material: The white Spread U material input takes a 2D image or a 3D material. Within the Alpha channel of that material, the per-pixel values get multiplied by the Spread U option’s setting from the node’s controls. Spread V Material: The white Spread V material input takes a 2D image or a 3D material. Likewise, inside that material’s Alpha channel the per-pixel values are multiplied by the Spread V control’s setting. Bump Map Material: The white Bump Map material input takes only a 3D material. The usual approach is to wire the texture into a Bump Map node and then feed that Bump Map node into this input. The RGB data here functions as texture-space normals. When a node holds this many inputs — some sharing a color — making accurate connections is often fiddly. While you drag another node’s output over the node tile, keep the Option or Alt key pressed, holding it still as you release the left mouse button. A little drop-down then enumerates all the node’s inputs. Click whichever one you want to complete the connection.

### Basic Node Setup

In the example beneath, the Ward node builds a glossy glass surface and stands in for the 3D text material. Its diffuse color material arrives from a Reflect node, while a gradient-colored Fast Noise node reshapes the specular color.

A Ward node used with a diffuse connection and specular color connection

### Inspector

### Ward controls

### Controls Tab

The Controls tab gathers parameters that adjust the main color, highlight, and lighting traits of the Ward shader node. Diffuse Diffuse covers the underlying surface traits before any add-ons such as reflections or specular highlights enter the picture. On top of defining an object’s base color, the diffuse color also fixes how transparent the object is. The Alpha within a diffuse texture map can make chosen parts of the surface see-through. Diffuse Color The Diffuse Color of a material is the base hue it presents under indirect or ambient light. When a diffuse texture map is supplied, the color value here is multiplied by the texture’s color values. Alpha This slider establishes the material’s Alpha channel value. It bears equally on diffuse and specular colors and on the rendered material’s Alpha value. When a diffuse texture map is supplied, the Alpha value here is multiplied by the texture map’s Alpha values. Opacity Cutting a material’s Opacity lowers the color and Alpha values of specular and diffuse colors in equal measure, rendering the material transparent.
