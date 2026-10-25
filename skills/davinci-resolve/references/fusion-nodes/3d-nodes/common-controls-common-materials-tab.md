# Common controls common materials tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Common controls.
[Chapter index](INDEX.md) / [Previous section](weld-3d-and-common-controls.md) / [Next section](common-controls-settings-tab.md) / [The Common Controls](weld-3d-and-common-controls.md)
<a id="source-common-materials-3d-tab"></a> <a id="source-common-materials-tab"></a> <a id="source-common-transform-3d-tab"></a> <a id="source-common-transform-tab"></a> <a id="source-diffuse"></a> <a id="source-material-id"></a> <a id="source-onscreen-transformation-controls"></a> <a id="source-pivot"></a> <a id="source-rotation"></a> <a id="source-scale"></a> <a id="source-specular"></a> <a id="source-translation"></a> <a id="source-transmittance"></a> <a id="source-viewer-transform-controls"></a>

### Common Materials Tab

Controls on the Materials tab govern how the 3D object looks once it is lit. Nearly all of them directly shape the way the object responds to light through a basic shader. When you need finer command over an object’s look, reach for the tools in the 3D Materials category of the Effects Library. Those tools let you put together a more richly detailed and exact shader.

### Common Materials 3D tab

Once a shader assembled from the 3D Material tools is wired into the 3D Object’s material input, this tab’s controls give way to a label noting that an external material is presently in play.

### Diffuse

Diffuse covers the fundamental surface qualities before extras such as reflections or specular highlights enter the picture. Diffuse Color The Diffuse Color fixes an object’s base color when its surface is lit either indirectly or by an ambient light. Should a valid image feed the tool’s diffuse texture input, the RGB values set here are additionally multiplied against the color values of the diffuse texture’s pixels. The diffuse material’s Alpha channel can govern how transparent the surface is. Alpha This slider establishes the material’s Alpha channel value. It bears equally on diffuse and specular colors, and it shapes the Alpha value the material carries in the rendered output. When the tool’s diffuse texture input is in use, the Alpha value here gets multiplied against the Alpha channel of the image’s pixels. Opacity Lowering the material’s Opacity pulls down the color and Alpha values of both specular and diffuse colors equally, rendering the material transparent so that objects behind it show through.

### Specular

The Specular section supplies controls that define the qualities of the light reflecting back toward the viewer. They shape how the specular highlight on the object’s surface looks. Specular Color Specular Color sets the hue of the light bouncing off a glossy surface. A more specular material reads as glossier. Materials such as plastics and glass usually carry white specular highlights, whereas metallic surfaces like gold show highlights that tend to take on the color of the material itself. This basic shader material has no input through which textures can drive the object’s specularity. Turn to tools in the 3D Material category whenever finer command over the specular look is needed. Specular Intensity Specular Intensity sets how strong the specular highlight reads. When the specular intensity texture input is validly connected, this value is multiplied against the Alpha value of that input. Specular Exponent Specular Exponent governs the falloff of the specular highlight. A higher value sharpens that falloff and makes the material read smoother and glossier. This basic shader material offers no input by which textures can drive the object’s specular exponent. Turn to tools in the 3D Material category whenever finer command over the specular exponent is required.

### Transmittance

Transmittance shapes how light moves through a material. As an example, a solid blue sphere throws a black shadow, while one made of translucent blue plastic would throw a far lighter-density blue shadow.

A distinct opacity option exists as well. Opacity sets how see-through the actual surface is once rendered. Fusion lets you tune opacity and transmittance independently of one another. Artists new to 3D software may find this a little unintuitive at first. You can have a surface that is completely opaque yet passes 100% of the light reaching it, in effect turning it into a luminous/emissive surface. Attenuation Attenuation sets how much color makes it through the object. For an object to throw transmissive shadows, dial the attenuation to (1, 1, 1), meaning 100% of the green, blue, red light travels through it. Setting that color to RGB (1, 0, 0) means the material lets through 100% of the red reaching the surface yet none of the green or blue. This is what permits “stained glass” shadows. Alpha Detail With the Alpha Detail slider at 0, the object’s Alpha channel is disregarded and the whole object throws a shadow. At 1, the Alpha channel dictates which parts of the object cast a shadow. Color Detail The Color Detail slider tints the light passing through the surface by the diffuse color + texture colors. Use it to throw a shadow holding color detail from the texture applied to the object. Pushing the slider from 0 toward 1 carries more of the diffuse color + texture color into the shadow. Note that an object’s Alpha and opacity are disregarded while color is transmitted, so an object with a solid Alpha can still pass its color into the shadow. Saturation The Saturation slider sets how saturated the color component carried into the shadow is. At 0.0 the shadows come out monochrome. Receives Lighting/Shadows These checkboxes decide whether the material responds to the scene’s lighting and shadows. Switched off, the object stays fully lit and/or free of shadow at all times. Two-Sided Lighting This renders the surface effectively two-sided by laying a second set of normals, facing the other way, on the surface’s back side. It usually stays off to keep rendering quick, but you can switch it on for 2D surfaces or for objects that aren’t fully closed, so the reverse or interior faces become visible too. Ordinarily, in a 3D application, only a surface’s front face shows and its back face is culled, so that if a camera circled a plane in a 3D application, the plane would vanish once it reached the back. Making a plane two sided in a 3D application is much like stacking another plane atop the first but spun 180 degrees so its normals point the opposite way on the back. Thus, circling around to the rear, you see that second image plane with normals facing the other direction. Fusion behaves exactly as 3D applications do when you make a surface two sided. The puzzlement over what two-sided lighting actually does comes from the fact that Fusion does not cull backfacing polygons by default. Circle a one-sided plane in Fusion and you still see it from behind (though what you see is the front bits carried through to the back as if the plane were transparent). Making the plane two sided in effect lays a second set of normals onto the plane’s back. Be aware this can grow rather confusing once the surface is transparent, since the same rules still hold and yield a counterintuitive result. View from the front a transparent twosided surface lit from behind, and it appears unlit.

### Material ID

This control assigns the numeric identifier given to this material. The Material ID is a whole number written into the rendered image’s MatID auxiliary channel whenever the Renderer 3D tool has its Material ID option switched on. Additional detail appears in Chapter 85, “3D Compositing Basics,” of the DaVinci Resolve Reference Manual, or in the Fusion Reference Manual at Chapter 25.

### Common Transform Tab

### Common Transform 3D tab

A great many tools within the 3D category carry a Transform tab for positioning, rotating, and scaling the object in 3D space.

### Translation

X, Y, Z Offset Use these controls to place the 3D element.

### Rotation

Rotation Order These buttons set the order in which rotation is applied along each of the object’s axes. As an example, XYZ rotates the X axis first, then the Y axis, and lastly the Z axis. X, Y, Z Rotation These controls spin the object about its pivot point. With the Use Target checkbox on, that rotation is measured relative to the target’s position; otherwise the global axis governs it.

### Pivot

X, Y, Z Pivot A Pivot point is the spot an object turns around. By default an object turns about its own center, taken to be a pivot of 0,0,0. These controls let you shift the pivot away from the center.

### Scale

X, Y, Z Scale With the Lock X/Y/Z checkbox checked, a lone Scale slider appears. It resizes the object overall. Uncheck the Lock checkbox and separate X, Y, and Z sliders show up so you can scale each dimension on its own. Note: With the Lock checkbox checked, you cannot scale individual dimensions, not even by dragging particular axes of the Transformation Widget while in scale mode. Use Target Ticking the Use Target checkbox brings up a group of controls for placing an XYZ target. With the target on, the object always turns to face it. The object’s rotation then becomes relative to the target. Import Transform Brings up a file browser where you select a scene file your 3D application saved or exported. It accepts these file types:

LightWave Scene Max Scene Maya Ascii Scene dotXSI

.lws .ase .ma .xsi

The Import Transform button pulls in transformation data only. For 3D geometry, lights, and cameras, look instead to the File > FBX Import option.

### Onscreen Transformation Controls

### Viewer Transform controls

Most of the Transform tab’s controls also appear in the viewer as onscreen handles for transformation, rotation, and scaling. To switch the mode of those onscreen controls, click one of the three buttons in the toolbar at the viewer’s upper left. The modes also respond to keyboard shortcuts: translation maps to Q, rotation to W, and scaling to E. Within all three modes, dragging an individual axis of the control affects only that axis, while dragging the control’s center affects all three at once. The scale sliders for most 3D tools start out locked, which scales all three axes uniformly. Clear the Lock X/Y/Z Scale checkbox to scale an object along a single axis alone.
