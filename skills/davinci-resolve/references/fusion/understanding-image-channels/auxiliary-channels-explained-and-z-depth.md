# Auxiliary channels explained and z depth

Version: DaVinci Resolve 20.3 Reference Manual. Context: Understanding image channels.
[Chapter index](INDEX.md) / [Previous section](displaying-channels-in-the-viewer.md) / [Next section](combined-x-and-y-disparity-channels-and-cryptomatte-in-fusion.md)
<a id="source-auxiliary-channels-explained"></a> <a id="source-background-rgba"></a> <a id="source-object-id"></a> <a id="source-uv-texture"></a> <a id="source-world-position"></a> <a id="source-x-y-and-z-normals"></a> <a id="source-xy-disparity"></a> <a id="source-xy-vector-and-xy-backvector"></a> <a id="source-xyz-position"></a> <a id="source-z-coverage"></a> <a id="source-z-depth"></a>

### Auxiliary Channels Explained

Fusion can put auxiliary channels to work for depth-based compositing, for building masks and mattes off Object or Material IDs, and for swapping textures. The nodes that read auxiliary channel data were purpose-built to handle it. What follows is a rundown of the auxiliary channels Fusion supports.

### Z-Depth

Every pixel in a Z-Depth channel holds a value standing for how far that pixel sits in the scene relatively. Where objects overlap within a model, most 3D applications grab the depth value of whichever object is nearest the camera whenever two share a single pixel, since the nearer one usually hides the one behind. Where it exists, Z-Depth lets you carry out depth merging through the Merge node or drive simulated depth-of-field blurring through the Depth Blur node.

The rendered Z-Depth channel for the previous RGBA image In this example, we'll look at the situation where the Z-Depth channel arrives as its own separate file. The Z- channel is frequently rendered as an RGB image. The beauty and Z pass then have to be joined with a Channel Booleans node. With the Z pass rendered as an image across the RGB channels, the Channels Booleans node re-routes the Lightness sitting in the foreground RGB channel across to the Z-channel. Here is how to merge the beauty pass with the Z-pass: 1 Wire the MediaIn node holding the beauty pass into the background input of the Channel Booleans node. 2 Wire the MediaIn node holding the Z-Depth pass into the green foreground input of the Channel Booleans node. 3 With the Channel Booleans node selected, open the Inspector; the To Red, To Green, To Blue, and To Alpha menus should each be set to Do Nothing. 4 Move to the Aux tab; the To Z Buffer menu wants Lightness FG. 5 Wire the output of the Channels Booleans node on into the Depth Blur node.

The Aux tab set up so the Foreground Lightness moves across into the Z-Depth channel.

Among the nodes that exploit a Z-channel to produce blurry depth-of-field simulations is the Depth Blur node. To get it going, route the MediaIn node's output into the background input on the Depth Blur.

The Depth Blur draws on the Z-channel switched on inside the Channel Booleans node. How the Depth Blur's Inspector controls behave hinges heavily on the kind of image at hand. Often it's simplest to first nudge the Inspector controls toward saner defaults. Begin by raising the Blur Size to 10. That makes even tiny changes far easier to spot. Then, rather than relying on the Focal Point, choose a focal point right in the picture by dragging the Sample button into the viewer and clicking a pixel that marks the part you want held in focus. To wrap up, drop Z Scale down near 0.2 (assuming a floating-point image), and don't touch the Depth of Field just yet. You should now see a bit of blur appear in the image.

If your image is 16- or 32-bit floating point, kick things off by tuning up the defaults. After seeing how those trial settings land, you can revisit each parameter and adjust it however you need to reach the look you're truly after.

TIP: Z-Depth channels frequently hold negative values. Should that cause trouble, pick Normalize Color Range from the viewer's Options menu to normalize the viewer and hold the image inside a range from 0 to 1.

### Z-Coverage

In most 3D applications the Z-Coverage channel is a fairly obsolete render pass. Its purpose was to bring antialiasing back to rendered color masks and Z-Depth passes. It flagged the Z-Depth pixels where two objects landed. That value reported, as a percentage, how see-through the pixel was within the final depth composite. You can still make use of it now if you render files from the handful of applications that still output it. TIP: Because the open-source matte technology called Cryptomatte has caught on so widely, mattes built from Coverage, Background, Object ID, and Material ID passes have been largely overtaken.

### Background RGBA

Across most 3D applications, this channel is a fairly obsolete render pass. It held the color values belonging to the objects sitting behind the pixels covered by the Z coverage.

### Object ID

Most 3D applications can hand out ID values to the objects in a scene. Each pixel within the Object ID channel carries that ID number, which makes building masks possible. To bring an Object ID into a comp, you must — as with every aux channel — map the Object ID pass onto the Object ID channel within the MediaIn or Loader Node. Putting an ObjectID pass to work goes like this: 1 Inside the MediaIn or Loader node, head to the Channels or Format tab and map the Object ID pass onto the Object ID aux channel. 2 On whichever node you want the ObjectID matte to drive, open the Settings tab, switch on the Object ID checkbox, and choose the ID number given to the object.

The common Settings tab on most nodes contains ObjectID controls.

Most 3D applications can hand out ID values to the materials in a scene. Each pixel within the Material ID channel carries that ID number, which makes masks based on materials possible. Material IDs are configured through the Settings tab, much the way ObjectIDs are.

### UV Texture

The UV Texture channels record how an image's pixels correspond to texture coordinates. They serve to retexture an object inside a 2D image. As an example, If you wanted to drop a logo onto a rendered object, you could feed the UV aux channel into the Texture node.

Texture (left) laid onto a 2D image (right) by way of UV channels and the texture node. Putting a UV pass to work goes like this: 1 Inside the MediaIn or Loader node, head to the Channels or Format tab and map the U and V pass onto the U and V aux channels. 2 Route the MediaIn or Loader node's output into the background input of the Texture node. 3 Route the texture image you intend to use into the foreground input of the Texture node. 4 To blend the original texture with the fresh one, run a merge with the background input fed by the original image and the foreground input fed by the Texture node. 5 Tune Merge's Apply mode, Alpha Gain, and blend until the two textures mix the way you want.

UV channels taken from a MediaIn node, fed through a Texture node, then composited atop the source image TIP: When you've got a separate UV render pass carrying the UV data across the RGB channels, map red onto U and green onto V inside a Channel Booleans node.

### X, Y, and Z Normals

The X, Y, and Z Normal channels hold each pixel's orientation — the way it faces — in 3D space. Normals are commonly drawn as lines projecting out from your object at right angles to the surface, which helps you picture how the surface relates to the camera.

The Normals show which way the surface points. Frequently the Normals X, Y, and Z channels feed a Shader node so relighting tweaks can be applied onto a 2D rendered image. Setting up a Shader node to read XYZ Normals goes like this: 1 Inside the MediaIn or Loader node, head to the Channels or Format tab and map each separate X, Y, and Z Normals pass onto the X Normal, Y Normal, and Z Normal channels. 2 Route the MediaIn or Loader node's output into the background input of the Shader node. 3 If you like, wire a floating-point EXR image to serve as a reflection image into the Shader node's reflection input. 4 Work the Shader controls to carry out the relighting.

Original 2D image (left) and Normals used for relighting (right)

### XY Vector and XY BackVector

The Vector channels record how a pixel moves from one frame to the next. They can drive motion blur on an image or feed optical flow analysis for retiming. The XY Vector aims toward the upcoming frame, whereas the XY BackVector aims toward the prior one.

XY Vector pass (left) paired with Vector Motion Blur to produce motion blur on the spaceship (right) The vector pass is frequently rendered separately as an RGB image. The X and Y vector data resides in the R and G channels. Getting them into the vector channels calls for a Channel Booleans node. Producing motion blur from a Motion Vector pass goes like this: 1 Add a MediaIn or Loader node covering both the image and the Vector render pass. 2 Route the image's output into the background of a Channel Booleans node. 3 Route the Vector render pass output into the Channel Boolean's foreground 4 Within the Channel Booleans inspector, the To Red, To Green, To Blue, and To Alpha menus all want Do Nothing. 5 Switch over to the Aux tab. 6 Switch on Enable Extra Channels. 7 Point the To X Vector drop-down menu at Red FG, then point the To Y Vector drop-down menu at Green FG. 8 Route the Channel Booleans node's output into the yellow background input on a Vector Motion Blur node.

The Channels Booleans node joins the Vector render pass to the beauty image, and its output then drives the Vector Motion Blur node.

### World Position

World Position Pass (WPP) is an auxiliary channel that goes by Point Position, XYZ pass, or WPP as well. Its job is to encode each pixel's 3D (XYZ) location as an RGB color value. That gives you data you can view as a strikingly colorful RGB image. As with Z-Depth, it works for depth-driven compositing. On top of that, it can mask according to 3D position no matter how the camera transforms. Because the colors track a pixel's 3D location, a pixel placed at 0/0/0 in a 3D scene yields a pixel with an RGB value of 0/0/0, that is, black. A pixel placed at 1/0/0 in the 3D scene yields a fully red pixel. Given the enormous spans 3D scenes can cover, the WPP channel should always be rendered in 32-bit floating-point so it carries the precision required.

### XYZ Position

### XY Disparity

XY Disparity stands as the lone channel here that no 3D application produces. These channels mark where a pixel's matching matte sits within a stereo image. Each eye, left and right, follows this vector to find where that pixel would land in the opposite eye. It serves for tuning stereo effects or for masking pixels in stereo space.
