# External mattes to limit adjustments and extracting external mattes from openexr layers

Version: DaVinci Resolve 20.3 Reference Manual. Context: Combining keys and using mattes.
[Chapter index](INDEX.md) / [Previous section](key-combinations-and-outside-nodes.md) / [Next section](the-key-mixer-and-adding-two-keys-together.md)
<a id="source-combining-keys-and-using-mattes-part-2"></a> <a id="source-external-mattes-to-limit-adjustments"></a> <a id="source-extracting-external-mattes-from-openexr-layers"></a> <a id="source-key-palette-controls-for-the-external-matte-node"></a> <a id="source-using-external-mattes-to-add-texture"></a> <a id="source-using-external-mattes-to-create-transparency"></a> <a id="source-using-mattes-from-the-fusion-page"></a>

### External Mattes to Limit Adjustments

Returning to the External Matte node's first use, mattes are usually grayscale media files standing for image opacity, meant to serve either as alpha channels that build opacity inside a matching RGB clip, or as a matte that confines effects. The key a green screen keyer produces would be one example of a matte channel. Output just the key and that becomes an external matte. Should you get an external matte alongside an effects clip, you can attach the matte to its matching RGB clip in the Media page. From there, you reach that matte through an External Matte node in the Node Editor, so the key it outputs can confine the various corrections you mean to apply. In the example below, the keyed matte of a green screen composite clip drives different corrections inside and outside a keyed composite, so the subject matches its background more believably.

A matte attached to clip Makeup_Green.mov, shown within the Media Pool To confine an adjustment inside a Clip grade with a clip matte: 1 Right-click any node, then off the contextual menu's Add Matte submenu pick whichever attached matte you want. The EXT MATTE node that turns up has, by default, its first output already hooked up. Run one of the triangular key outputs on that EXT MATTE node into the key input of whatever node it should confine. 2 Pick the node the EXT MATTE node attaches to, and tack on an Outside node so adjustments can sit on either side of the matte.

Node Editor showing how the external matte sways several nodes once their keys are linked 3 If you must, pick Node 1 and lean on the Key palette controls to reshape the incoming key, inverting or blurring it as much as the isolation requires. NOTE: Steer clear of selecting the EXT MATTE node, since it surfaces a different set of Key palette controls for transforming, flipping, looping, and freezing the matte. From here, you can drop adjustments onto the inside and the outside of this composited shot to sharpen the composite.

(Before/After) An external matte driving separate grades onto the foreground and background of a clip composited earlier In an ideal case, external mattes are exported to match the size and duration of the RGB clip they're meant to ride with. Where they don't match, or where you're pressing some other grayscale clip into service as an external matte for an effect, the Key palette holds parameters you can use to retime or transform a matte so it sits better in your grade. To slip a matte's sync against the clip it attaches to: 1 Pick the Ext Matte node you mean to slip. 2 Open the Key palette and clear the Lock Matte checkbox. 3 Raise or drop the Offset parameter until the matte lines up exactly with the clip it should match.

To transform a matte: 1 Pick the Ext Matte you mean to transform. 2 Open the Key palette and clear the Lock Matte checkbox. 3 Reach for the Pan, Tilt, Zoom, Rotate, Width, Height, HFlip, or VFlip parameters to set the matte's geometry right. Worth noting too is that you can attach as many external mattes to one clip in DaVinci Resolve as you please. As an example, should a CGI shot show up bearing an isolation matte apiece for three characters in the scene, all three can be imported and used to single out adjustments you want to make in the Node Editor.

### Extracting External Mattes from OpenEXR Layers

OpenEXR media can hold multiple layers and multiple alpha channels, which EXT MATTE nodes can reach as well. Because of that, DaVinci Resolve follows a slightly different but related procedure for getting at these mattes. To pull OpenEXR layers out as external matte nodes: 1 Right-click any node, then off the contextual menu's Add Matte submenu pick the .exr clip name. The EXT MATTE node that turns up has, by default, its first output already hooked up. Run one of the triangular key outputs on that EXT MATTE node into the key input of whatever node it should confine. 2 Double-click the EXT MATTE node to pick it, then right-click it and pick which layer to use off the Select Matte submenu.

Right-clicking the EXT MATTE node of an OpenEXR file to pick which layer is used

An OpenEXR file with several RGBA layers (or passes) tucked inside it (RGBA + RGBA + RGBA and so on), or an OpenEXR file carrying several alpha channels (RGBA + A + A), surfaces multiple entries in this submenu. Whichever you settle on is the layer that EXT MATTE node will treat as a matte. Once you've pulled an OpenEXR layer out, you can put it to work like any other EXT MATTE node covered in this section, to confine adjustments (as shown above), or to lay on texture or transparency (as shown in the sections that follow). On a node holding several matte layers, like an .exr file, you can preview the individual matte layers. To do so, right-click the node, pick Add Matte off the contextual menu, and hover over the file's name. A roster of every layer in the node appears, and holding the Option key while hovering over each layer brings it up in the Viewer. That lets you swiftly confirm whether you're on the right matte layer (arm, wheel, shirt, etc.), no matter what the matte was named in the file.

### Using External Mattes to Add Texture

External mattes can serve as creative tools too, for laying on grain and texture. You might, say, pull in a more abstract animated matte, or a grayscale film scan of grime and specks, applying a correction purely for effect.

Light-leak plus grime-and-speck imagery drawn From Warren Eagles' Scratch FX collection (FXPHD), made to lend texture to your grades After it attaches to a clip, an external matte can be surfaced in the Node Editor, its key output put to work just like any other key in a node tree.

To use a clip matte to build texture for a Clip or Timeline grade: 1 As you apply a matte within a Clip or Timeline grade, right-click any node and pick the attached or timeline matte you want off the Add Matte submenu of the contextual menu. Unattached mattes show up under the Add Matte > Timeline Mattes submenu. 2 Unhook the EXT MATTE node's key output from the Key input of whatever node it defaults to. 3 Tack a Layer Mixer onto the end of the node tree. 4 Unhook the bottom Corrector node's RGB input, then wire it into the EXT MATTE node's square RGB output.

A node tree arranged so an EXT MATTE node's RGB output runs into the input of a node tied to a Layer Mixer, letting it blend into the grade by way of composite modes 5 Right-click the Layer Mixer node and pick Overlay off the Composite Mode submenu to blend the Ext Matte node into the grade most effectively. 6 If you must, lean on the grading controls of the Corrector node you attached the EXT MATTE node to in order to alter the texture clip's character, draining its saturation for instance. You can also pick the EXT MATTE node itself, open the Key palette, and reach for the Transform, Offset, Loop, or Freeze controls covered later to alter how the matte looks.

The texture effect that results, merged into the grade through the Overlay composite mode TIP: When you want the texture you build to dodge any blur or sharpening operations inside the grade, be sure to drop it at the very end of the node tree.

### Using External Mattes to Create Transparency

You can also press an EXT MATTE node into service to build transparency in a clip, for compositing against clips beneath it on the Timeline. To use a clip matte to build transparency in a clip: 1 Right-click any node, then pick the attached matte you want off the Add Matte submenu of the contextual menu. Dropping an EXT MATTE node onto a Clip grade hits only that clip, whereas dropping an EXT MATTE node onto a Track grade hits the whole Timeline. 2 Right-click any empty patch of the Node Editor and pick Add Alpha Output to surface the Node Tree output on the right, which lets you assign a key for defining clip transparency. 3 Wire one of the EXT MATTE node's triangular key outputs into the Alpha output at the right of the Node Editor.

The node setup for using an external matte to composite two layer Wherever the key defines the matte, those areas now render transparent.

The final composite created using the external matte node

### Key Palette Controls for the External Matte Node

Pick an EXT MATTE node and the Key palette shows a different set of parameters meant only for mattes. Note that you have to clear the Lock Matte checkbox before any adjustments to transform the matte will take.

The Key Palette with a texture layer brought in as an EXT MATTE node

- Transform: The usual Pan, Tilt, Zoom, Rotate, Width, and Height parameters let you reshape a matte for a closer fit to the image.
- Flip Image: A pair of buttons flip the matte clip across the horizontal or the vertical.
- Offset: Tweak this parameter to shift where a matte clip starts.
- Freeze: Ticking this checkbox locks the matte clip onto one frame. Tweak the Offset

parameter to pick which frame it freezes on.

- Loop: Ticking this checkbox lets matte clips loop without end, so shorter matte

clips can span longer stretches.

- Lock Matte: Switched on, this pins a matte's sizing to whatever shifts are made to the

Input Sizing of that clip, so the matte reshapes in step with the clip. You can press external mattes into service as creative tools as well. You might, say, pull in a more abstract animated matte, or a grayscale film scan of grime and specks, applying a correction purely for effect.

### Using Mattes From the Fusion Page

When you're grading a composite built on the Fusion page, you can pipe mattes made in various parts of a Fusion composition over to the Color page to use in the grade too. Say you're grading a composite of a foreground actor green-screen keyed against a background layer; you might want to lean on the matte made for the key to shield the foreground subject from a grade operation you mean to land on the background alone. Fortunately, that's simple to arrange. In the Fusion composition that follows, two DeltaKeyer nodes (one to build an overall matte, one to build a solid matte guarding the core) plus one BSpline node (to build a garbage matte) work in concert to craft a finely-tuned matte. The Merge1 node leans on this matte to keep the subject's hair intact and set them in front of a gently blurred (via the LensBlur node) planet, the finished result wiring into the MediaOut1 node, which pipes this image to the Edit page and Color page for further adjustment.

A Fusion page green screen composition that sends its RGB out through MediaOut1 and the foreground matte out through MediaOut2 Since the Merge1 node puts out the whole composition as one image, a second MediaOut node (highlighted) is tacked on to output the matte, just in case the colorist wants it down the line. TIP: Within this composition the foreground and background images differ in size, so outputting the alpha channel of the DeltaKeyer1 node would yield a matte sized to the foreground image, which doesn't suit the composition, since that crops the foreground image's top and bottom against the frame size of the widescreen background image. To sidestep this, the foreground and background images get composited a second time through the Merge2 node, whose Operator parameter is set to "In" so it outputs just the foreground image and matte, resized by the Merge operation. The resulting MediaOut2 node thus puts out a foreground matte sized correctly to suit the composition. On the Color page, the grade in node 1 lands on the overall final result, which is a single image. After grading, the call is made that the woman reads a touch warm against the cool blue of the planet behind her.

How the composition looks within the Color page Node Viewer When you right-click the Node Editor's background and pick Add Source, a second source shows up over on the left side of the Node Editor.

Bringing in the matte output of the MediaOut2 node from the Fusion page composition via an added source This second source lines up with the second MediaOut node you placed in the Fusion page composition, the one that sends the Matte out as a key over in the Color page, where it behaves just like any other key. Hover your pointer over each source and a tooltip pops up telling you which output goes with which node.

Resting the pointer on a source names it through a tooltip As a rule, the sources run from top to bottom following the order of MediaOut nodes in the Fusion composition, first through last. From here, you can wire the second Source into the Key input of a second corrector node, then lean on that key to grade only the woman up front (her grade pushed hard for emphasis) while sparing the background. Here the Viewer has Splitscreen set to Highlight Modes, letting you view both the outcome and the key coming off the Fusion page that Node 2 relies on.

Wiring the second source into a second Corrector node's KEY input so the matte confines a correction to the foreground character
