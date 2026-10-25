# Combined x and y disparity channels and cryptomatte in Fusion

Version: DaVinci Resolve 20.3 Reference Manual. Context: Understanding image channels.
[Chapter index](INDEX.md) / [Previous section](auxiliary-channels-explained-and-z-depth.md)
<a id="source-combined-x-and-y-disparity-channels"></a> <a id="source-creating-auxiliary-channels-in-fusion"></a> <a id="source-image-formats-that-support-aux-channels"></a> <a id="source-nodes-that-use-auxiliary-channels"></a> <a id="source-propagating-auxiliary-channels"></a> <a id="source-using-cryptomatte-in-fusion"></a>

### Combined X and Y Disparity channels

### Using Cryptomatte in Fusion

Cryptomatte is an open-source technology that 3D applications have taken up broadly. In contrast to Z-Depth mattes or Object IDs, Cryptomatte builds anti-aliased ID mattes from 3D renders on its own, handling motion blur, transparency, and depth of field. The Cryptomatte format isn't supported in Fusion out of the box. That said, a free third-party plugin lets you bring Crypotmatte render passes into Fusion. You can grab and set up Crypotmatte for Fusion at no cost here: https://github.com/Psyop/ Cryptomatte Or, for a smoother install, grab Reactor, which ships with Cryptomatte alongside plenty of other free and handy Fusion plugins. Reactor can be found at: https://www.steakunderwater.com

### Propagating Auxiliary Channels

Normally auxiliary channels ride along with RGBA image data from one node to the next, traveling through gray-colored nodes such as those in the Blur, Filter, Effect, Transform, and Warp categories. In short, the bulk of nodes that merely process channel data pass auxiliary channels through (and may alter them) without trouble. But once you composite two image layers with the Merge node, auxiliary channels carry through only on the image wired to the background input. That's because in most composites involving computer-generated imagery, the background tends to be the CG layer holding auxiliary channels, while the foreground is a live-action green screen plate of subjects or elements composited over the background and carrying no auxiliary channels.

### Nodes That Use Auxiliary Channels

Having auxiliary channels available unlocks a whole realm of advanced compositing power. The list here covers each Fusion node built to handle images that carry auxiliary channels.

- Copy Aux: The Copy Aux tool can copy auxiliary channels over to RGB and then copy them back again. It offers some handy options for remapping values and color depths, plus stripping auxiliary channels out.
- Channel Booleans: The Channel Boolean tool serves to merge or copy values from one channel into another in numerous ways.
- Custom Tool, Custom Vertex 3D, pCustom: The "Custom" tools can pull data from the auxiliary channels at the per-pixel, per-vertex, or per-particle level and apply it to whatever processing you have in mind.
- Depth Blur: The Depth Blur tool blurs an image according to what the Z-Depth holds. A focal point is picked from the image's Z-Depth values and how much falls in focus is set with the Depth of Field control. Since the Scale value default assumes an 8-bit image, be sure to drop the scale value down whenever you run the Depth Blur on 16- or 32‑bit float files.
- Disparity to Z, Z to Disparity, Z to WorldPos: These tools draw on the built-in ties between depth, position, and disparity to translate one channel into another.
- Fog: The Fog tool taps the Z-Depth to make a fog that stays thin near the camera and grows denser in areas farther off. The Pick tool lets you grab the Depth values from the image and mark the Near and Far planes of the fog's reach.
- Lumakeyer: The Lumakeyer tool can pull a key on the Z-Depth channel by picking Z-Depth from the channel drop-down list.
- Merge: Beyond ordinary compositing work, Merge can blend two or more images by way of the Z-Depth, Z-Coverage, and BG RGBA buffer data. You do this by ticking the Perform Depth Merge checkbox over on the Channels tab.
- New Eye: With stereoscopic footage, New Eye taps the Disparity channels to build fresh viewpoints or shift RGBA data from one eye over to the other.
- Shader: The Shader tool feeds data from the RGBA, UV and the Normal channels to reshape the lighting on objects in the image. You get control over specular highlights, ambient and diffuse lighting, and where the light source sits. A second image can serve as a reflection or refraction map.
- Shadow: The Shadow tool can lean on the Z-Depth channel as a Z-Map. That lets the shadow drape over the shapes of the objects in the image.
- Smooth Motion: Smooth Motion taps Vector and Back Vector channels to blend other channels across time. It can strip high frequency jitter out of troublesome channels like Disparity.
- SSAO: SSAO stands for Screen Space Ambient Occlusion. Ambient Occlusion is the lighting that arises when a scene sits inside a uniform diffuse spherical light source. Out in the real world, light reaches surfaces from every direction, not merely from a handful of directional lights. Ambient Occlusion records this low frequency lighting, yet it misses sharp shadows and specular lighting. That's why Ambient Occlusion is typically paired with Specular lighting to form a complete lighting solution. The SSAO tool taps the Z-Depth channel but needs a Camera3D input.
- Stereo Align: With stereoscopic footage, Stereo Align can use the Disparity channels to warp one or both eyes, correcting misalignment or moving the convergence plane.
- Texture: The Texture tool taps the UV channels to lay an image from the second input on as a texture. Paired with the Object ID or Material ID masks, it can swap textures on one specific object.
- Time Speed and Time Stretcher: These tools can lean on the Vector and BackVector channels to retime footage.
- Vector Distortion: The forward XY Vector channels can drive this tool to warp an image.
- Vector Motion Blur: Drawing on the forward XY Vector channels, the Vector Motion Blur tool can apply

blur in the direction of the velocity, creating a motion blur effect.

- Volume Fog: Volume Fog is a raymarcher that taps the World Position channels to figure out ray termination and where the volume dataset sits. It can also draw on cameras and lights from a 3D scene to fix the right ray start point and Illumination parameters.
- Volume Mask: Volume Mask taps the World Position channels to place a mask in 3D space instead of screen space. That lets a mask hold flawless tracking right through a camera move.

TIP: Some tools in Fusion can turn the Object ID and Material ID auxiliary channels into a mask. The "Use Object" and "Use Material" settings that drive this live on the Settings tab of that node's controls within the Inspector.

### Image Formats That Support Aux Channels

Fusion reads auxiliary channel data held in an assortment of image formats. The channel counts and the methods involved vary from one format to the next.

- OpenEXR (\*.exr): The OpenEXR file format is the leading format for holding any number of extra image channels. Plenty of renderers that output to the OpenEXR format will let you create channels carrying wholly arbitrary data. A channel of specular highlights, for instance, might live inside an OpenEXR. Usually the channel carries a custom name that lets you map the extra channel onto one Fusion recognizes.
- SoftImage PIC (_.PIC, _.ZPIC and \*.Z): A legacy format, the PIC image format (which SoftImage uses) can stash Z-Depth data in its own separate file flagged by the ZPIC file extension. Those files have to sit in the same directory as the RGBA PIC files and share the same names. Fusion spots the extra information automatically and loads the ZPIC images right alongside the PIC images.
- Wavefront RLA (_.RLA), 3ds Max RLA (_.RLA) and RPF (\*.RPF): Here's a legacy format able to hold any of the image channels named above. Every channel lives inside a single file, RGBA included, along with the auxiliary channels. The RLA or RPF file extension identifies these files. Auxiliary channel data isn't in every RLA or RPF file, though most carry it. RPF files add the ability to store several samples per pixel, so different layers of the image can load for highly intricate depth composites.
- Fusion RAW (\*.RAW): Fusion's own native RAW format can hold every auxiliary channel plus other metadata Fusion relies on.

### Creating Auxiliary Channels in Fusion

The following nodes create auxiliary channels:

- Renderer 3D: Builds these channels just the way any other 3D application would, and you get to output any of the auxiliary data channels the Fusion page supports.
- Optical Flow: Builds Vector and Back Vector channels by studying pixels over successive frames to work out the probable movement of features in the image.
- Disparity: Builds Disparity channels by matching up stereoscopic image pairs.
