# Fbx exporter and text3d

Version: DaVinci Resolve 20.3 Reference Manual. Context: 3D compositing basics.
[Chapter index](INDEX.md) / [Previous section](importing-an-fbx-scene-fbx-scene-import-dialog.md) / [Next section](world-position-pass-and-point-clouds.md)
<a id="source-assembling-text-objects"></a> <a id="source-entering-text"></a> <a id="source-fbx-exporter"></a> <a id="source-fog-3d-and-soft-clipping"></a> <a id="source-layout-parameters"></a> <a id="source-material-and-object-ids"></a> <a id="source-repositioned-text-objects-to-create-a-title-sequence"></a> <a id="source-shading"></a> <a id="source-split-screen-with-and-without-fog"></a> <a id="source-text3d-nodes-also-have-transform-parameters-built-in"></a> <a id="source-transforming-individual-words-in-two-different-ways"></a> <a id="source-using-text3d"></a>

### FBX Exporter

The FBX Exporter node lets you send a 3D scene out of Fusion into other 3D packages. At render time it stores geometry, cameras lights, and animation across various file formats such as .dae or .fbx. You can keep the animation data within a single file, or have it baked out across sequential frames. Textures and materials, though, can’t be exported.

### Using Text3D

For motion graphics artists building titles and graphics out of Fusion, the Text3D node is likely the most widely used node of all. It’s a capable node packed with enough controls to produce just about any text effect you’d want, fully in three dimensions. The aim of this section is to get you up and running fast with all the Text3D node can do. Further detail lives in Chapter 89, “3D Nodes,” of the DaVinci Resolve Reference Manual, or over in the Fusion Reference Manual at Chapter 29.

### Assembling Text Objects

Every Text3D node is a scene unto itself, and within it each text character stands as its own object. For that reason, when you want many text objects you can animate or style apart from one another, the cleanest approach is to feed however many Text3D objects you'd like to control separately into one or more Merge3D nodes.

Merging multiple text objects to create an intricately styled scene TIP: Click the Text icon in the toolbar to make a Text3D node, then click it once more while that freshly made Text3D node is still selected, and a Merge3D node is created and selected automatically to join the pair. Keep clicking the Text icon and additional Text3D nodes attach to that same selected Merge3D node.

### Entering Text

Select a Text3D node and open the Inspector, and the Text tab presents a “Styled Text” text entry field right at the top where you type whatever text should show onscreen. Underneath sits a group of overall styling parameters for setting the Font, Color, Size, Tracking, and the like. Everything you style on this tab applies to the whole block of text together, which is precisely why you need several text objects to have differently styled words within one scene.

The text entry and styling parameters in the Text tab Toward the foot of the Text tab sit the Extrusion parameters, tucked inside a disclosure control.

The Extrusion parameters near the bottom of the Text tab Out of the box, any text made with the Text3D node is flat, yet the Extrusion Style, Extrusion Depth, and the assorted Bevel parameters let you lend thickness to your text objects.

Unextruded text (left), and Extruded text (right) Positioning and Transforming Text Out of the box, each new Text3D node lands at 0, 0, 0, so adding several Text3D nodes leaves them all stacked in one spot. Happily, every Text3D node carries its own transform controls in the Transform tab.

### Text3D nodes also have Transform parameters built-in

On top of that, selecting a Text3D node brings up all the onscreen transform controls covered elsewhere in this chapter. With those controls you can place and animate each text object on its own.

### Repositioned text objects to create a title sequence

Pairing Text3D nodes with Merge3D nodes builds a scene, but it also lets you transform your text objects one at a time or in clusters:

- Pick a single Text3D node, or a piece of text in the viewer, and you can reposition just that one text object on its own, with no effect on the scene’s other objects.
- Pick a Merge3D node and a transform control appears that acts on every object wired into that Merge3D node together, so the whole scene transforms as one.

### Layout Parameters

On the Layout tab you’ll find parameters for picking how text gets laid out: along a straight line, a frame, a circle, or a custom spline path, plus contextual parameters that shift with whichever layout you choose (every one of them animatable).

Text using two different layouts “Sub” Transforms There’s a second Transform tab (the documentation calls it the “Sub” Transform tab) that lets you lay a separate tier of transform onto characters, words, or lines of text, opening up still more layout variety. As an instance, picking Transform by Words lets you adjust word spacing, spin each word, and so forth. Transforms can run on characters, words, and lines all at the same time, so you can stack every one of these capabilities together if you truly want to push it. And naturally, all these parameters can be animated.

### Transforming individual words in two different ways

### Shading

On the Shading tab you can shade or texture a text object with the standard Material controls.

### Fog 3D and Soft Clipping

Atmospheric depth cues are easy to build with the Fog3D node.

### Split screen with and without fog

The Fog3D node pairs nicely with the depth of field and antialiasing the OpenGL renderer provides. Because it isn’t a post-processing node (unlike the VolumeFog node sitting in the Nodes > Position menu, or the Fog node under Nodes > Deep Pixel), it gets by without extra channels such as Position or Z-channel color. It also handles transparent objects. The SoftClip node leans on how far a pixel sits from the viewpoint to drive opacity, letting objects fade out gracefully as they near the camera. That keeps objects from “popping off” when the camera moves through them, which proves handy especially with particles the camera might travel through. Geometry nodes like the Shape3D node carry a Matte Objects checkbox for masking away portions of the 3D scene. In practice, anything sitting behind a matte object goes unrendered. Even so, matte objects can feed data into the Z-channel and the Object ID channel while leaving every other channel at its defaults. They neither delete nor alter any geometry; picture them as a 3D garbage matte serving the renderer.

A Circle shape acting as a Matte object so the floor shows through Matte Object Parameters Open the Matte disclosure control and the Is Matte option appears, and switching it on unlocks two further options.

Matte parameters within a Shape3D node; turning on Is Matte surfaces extra options Is Matte Found on the geometry’s Controls tab, this serves as the principal checkbox for matte objects. With it on, any object whose pixels sit behind the matte object’s pixels in Z goes unrendered. Opaque Alpha Switching on the Is Matte checkbox brings up the Opaque Alpha checkbox. Turning it on forces the matte object’s alpha value to 1. If you don’t, the alpha — like the RGB — comes out 0. Infinite Z Switching on the Is Matte checkbox brings up the Infinite Z checkbox. Turning it on drives the Z-channel value to infinite. Otherwise the mesh feeds the Z-channel as it normally would. You can’t pick matte objects in the viewer unless you right-click there and choose 3D Options > Show Matte Objects from the contextual menu. That said, the matte object can always be picked by selecting its node within the node tree.

### Material and Object IDs

In Fusion, the bulk of nodes that allow effect masking can draw on Object ID and Material ID auxiliary channels to build a mask. You’ll find the parameters for doing so on each node’s Common Controls tab.

Material ID parameters shown among a Shape3D node’s Inspector controls The Material ID is a value that marks which material an object uses. The Object ID parallels the Material ID closely, save that it tags objects rather than materials. Fusion hands out both the Object ID and the Material ID automatically in counting order, starting at 1. You’re free to give several objects or materials the same ID even when they aren’t alike. Override 3D gives you a quick path to reassign the IDs across a number of objects. During rendering, the Renderer writes the assigned values into the frame buffers whenever those buffers have their output channel options switched on. The usable value range runs from 0 to 65534. Since empty pixels carry an ID of 0, manually handing a value of 0 to an object or material is allowed but unwise, because a 0 signals Fusion to pick an unused ID at render time.

The ground plane and the object both given an identical Object ID number
