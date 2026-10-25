# Uexport and uimage plane and uloader

Version: DaVinci Resolve 20.3 Reference Manual. Context: Uexport, Uimage plane, Uloader.
[Chapter index](INDEX.md) / [Previous section](ucamera-and-uduplicate.md) / [Next section](uloader-and-umaterialx-and-umerge.md)
<a id="source-basic-node-setup-2"></a> <a id="source-basic-node-setup-3"></a> <a id="source-common-controls-1"></a> <a id="source-common-controls-2"></a> <a id="source-controls-tab-2"></a> <a id="source-controls-tab-3"></a> <a id="source-export"></a> <a id="source-inputs-2"></a> <a id="source-inputs-3"></a> <a id="source-inputs-4"></a> <a id="source-inspector-1"></a> <a id="source-inspector-2"></a> <a id="source-inspector-3"></a> <a id="source-replacing-materials-with-imported-materialx-files"></a> <a id="source-the-uexport-controls"></a> <a id="source-the-uimage-plane-controls"></a> <a id="source-the-usd-loader-controls"></a> <a id="source-uexport-uex"></a> <a id="source-uimage-plane-uim"></a> <a id="source-uloader-uld"></a>

### uExport [uEx]

The uExport node uExport Node Introduction The uExport node exists to write scenes out in the Universal Scene Description (USD) format. Through it you can save your USD scene—geometry, materials, animations, and lighting included—into a USD file. This addition is a notable step forward for Fusion, letting you pass complex USD assets around effortlessly and making collaborative workflows run more smoothly. The node provides controls for picking among the various USD formats, namely usd, .usda, .usdc, and .usdz. You can also write out chosen nodes from the source tree as a hierarchy of linked USD files.

### Inputs

The Background node carries a single input meant for a USD scene.

### Inspector

### The uExport controls

### Export

Use the Export controls to choose the format that your exported USD scene is saved in.

- Export Stage: Click this button to bring up a file browser where you choose where your USD scene is saved.
- Format: Pick a format for your USD scene.
- USD (\*.usd)
- USD UTF-8 (\*.usda)
- USD binary (\*.usdc)
- USD packaged (\*.usdz)

### Common Controls

Settings Tab The Inspector’s Settings tab is repeated on the other USD nodes too. A full account of these shared controls appears in the “The Common Controls” section toward the end of this chapter.

### uImage Plane [uIm]

The USD Image Plane node uImage Plane Node Introduction Within 3D space, the uImage Plane node builds flat 2D geometry. Its most typical job is to show 2D images on “cards” inside the 3D space. The aspect ratio of the image plane follows the aspect ratio of whatever image you feed in.

### Inputs

This node’s input takes the image that gets texture mapped onto the plane. Input: The yellow input is where you wire in a MediaIn image.

### Basic Node Setup

The uImage Plane Node takes in a 2D image and drops it into a 3D USD scene.

### Inspector

### The uImage Plane controls

### Controls Tab

Common controls fill most of the Controls tab. The handful of Image Plane-specific controls sitting at the top of the Inspector handle small tweaks.

Filename The uImagePlane carries an input so an image can be routed straight into the node. The node can also load an image directly when you browse for one, after which it shows the name and path in the filename. Click the Browse button to bring up the file browser and choose an image. Size Size sets how big the image plane is within the USD 3D scene.

### Common Controls

Transform and Settings Tab You’ll also find the Inspector’s Transform and Settings tab repeated on the other USD nodes. These shared controls are spelled out fully in the “The Common Controls” section at the end of this chapter.

### uLoader [uLd]

The USD Loader node uLoader Node Introduction You rely on the uLoader node to pull USD files into your Fusion Composition. It handles the .usd, .usda, .usdc, and .usdz formats.

### Replacing Materials with Imported MaterialX files

You can bring MaterialX files (.mtlx) in through the USD Loader and then call on the uReplaceMaterial tool to apply those imported materials to a chosen USD object and reach the look you’re after.

### Inputs

None.

### Basic Node Setup

After the uLoader node brings in a USD scene, it combines that scene with a USD Camera so you can control the view.

### Inspector

### The USD Loader controls

### Controls Tab

Filename With this control you point to a USD file to pull into the Fusion project. Click the Browse button to bring up the file browser and choose a USD file (.usd, .usda, .usdc, or .usdz). Trim Lets you mark an In and Out point on a USD file so only that span comes into the Fusion project. Time Scale With time scale you can speed up or slow down the playback of animated .usd scenes. Frame Offset Sets the point at which an animation begins, letting you slide its timing along the timeline. Reverse Tick this and the animation of the USD file plays backward. Loop Tick this and the animation of the USD file repeats. Reload Clicking this button reloads the USD file named in the Filename field above. That way you can edit the USD file in some other application and view the results in Fusion simply by reloading it.
