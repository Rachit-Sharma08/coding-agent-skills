# Text 3D text tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Text 3D.
[Chapter index](INDEX.md) / [Previous section](soft-clip-and-spherical-camera-and-text-3d.md) / [Next section](text-modifier-behavior.md) / [Text 3D 3Txt](soft-clip-and-spherical-camera-and-text-3d.md)
<a id="source-basic-node-setup-1"></a> <a id="source-common-controls-2"></a> <a id="source-force-monospaced"></a> <a id="source-inputs-1"></a> <a id="source-layout-tab"></a> <a id="source-shading"></a> <a id="source-text-3d-controls"></a> <a id="source-text-3d-extrusion-and-bevel-controls"></a> <a id="source-text-3d-shading-tab"></a> <a id="source-text-3d-transform-tab"></a> <a id="source-text-tab"></a> <a id="source-transform-tab"></a> <a id="source-uncapped-3d-text"></a>

### Inputs

SceneInput: The orange scene input takes a 3D scene that can be merged with the 3D text the node builds. ColorImage: The green color image input takes a 2D image and wraps it onto the text as a texture. This input surfaces only when Image is picked in the Material Type menu sitting in the Shading tab. BevelTexture: The magenta bevel texture input takes a 2D image and wraps it onto the bevel as a texture. This input surfaces only when one Material is switched off in the Shader tab and Image is picked in the Bevel Type menu.

### Basic Node Setup

The Text 3D node turns out text, so as a rule this node opens a branch of your node tree. To layer on more believable materials, though, a replace Material node is often dropped in after the Text 3D, ahead of wiring into a Merge 3D node.

Text 3D with a Replace Material node placed afterward to lay on an alternative material Inspector

### Text 3D controls

### Text Tab

The Text 3D text tab in the Inspector splits into three parts: Text, Extrusion, and Advanced Controls. The Text section holds parameters anyone who's worked in a word processor will recognize. It carries the text formatting options people reach for often. The Extrusion section holds controls for extruding the text and forming beveled edges on it. The Advanced controls cover kerning options. Styled Text This tab's Edit box is where you type the text to be built. Any ordinary character can go into this box. The usual OS clipboard shortcuts function here too — copy with Command-C or Ctrl-C, cut with Command-X or Ctrl-X, paste with Command-V or Ctrl-V; right-clicking the Edit box, however, brings up a custom contextual menu carrying several modifiers you can tack on for added animation and formatting options.

Font A pair of Font menus serve to pick the font family along with the typeface, such as Regular, Bold, and Italic. Color This control fixes the text's basic tint color. It's the same Color control shown in the Material type section of the Shader tab. Size This control raises or lowers the text size. It doesn't work like picking a point size in a word processor. Size is gauged relative to the image's width. Tracking The Tracking parameter sets the even spacing placed between each text character. Line Spacing Line Spacing sets how far apart each line of text sits. Word-processing applications sometimes call this leading. V Anchor The Vertical Anchor controls comprise three buttons plus a slider. Those three buttons align the text vertically to the text's top, its middle, or its bottom baseline. The slider serves to fine-tune the alignment. Where you set the Vertical Anchor shapes how the text rotates as well as where line spacing adjustments take effect. This control sees most use with the Layout type at Frame in the Layout tab. V Justify The Vertical Justify slider lets you tune the text's vertical alignment from the V Anchor setting all the way to full justification, so it sits evenly between the top and bottom edges. Reach for it chiefly once Frame is the Layout type over in the Layout tab. H Anchor The Horizontal Anchor controls comprise three buttons plus a slider. Those three buttons set the text alignment to the text's left edge, its middle, or its right edge. The slider serves to fine-tune the justification. Where you set the Horizontal Anchor shapes how the text rotates as well as where tracking (leading) spacing adjustments take effect. Its main use comes with Frame chosen as the Layout type inside the Layout tab. H Justify The Horizontal Justify slider lets you tune the text's justification from the H Anchor setting all the way to full justification, so it sits evenly between the left and right edges. You'll lean on it mostly when Frame serves as the Layout type within the Layout tab. Direction This menu hands you choices for the direction the text gets written in. Line Direction Through these menu choices the text's flow is set to one of four directions: top to bottom, bottom to top, left to right, and finally right to left.

Write On This range control quickly lays simple Write On and Write Off animation over the text. For a Write On effect, animate the control's End portion from 1 to 0 across the span of time you need. For a Write Off effect, animate the range control's Start portion from 0 to 1. Extrusion Depth An extrusion of 0 yields wholly 2D text. Any value above 0 extrudes the text to build text carrying depth.

### Text 3D extrusion and bevel controls

Bevel Depth Raise the Bevel Depth slider's value to bevel the text. The text has to carry extrusion before this control does anything. Bevel Width Reach for the Bevel Width control to widen the bevel. Smoothing Angle Use this control to set the smoothing angle laid onto the bevel's edges. Front/Back Bevel Use these checkboxes to switch beveling on for the text's front and back faces independently Custom Extrusion While in Custom mode, the Smoothing Angle governs how the normals smooth around a text character's edges. The spline on its own governs the smoothing along the extrusion profile. Smooth a spline segment, say by pressing the shortcut Shift-S, and its normals smooth as well. Where the control point is linear, the shading edge stays sharp. The spline's first and last control points mark out the text's extent. Custom Extrusion Subdivisions Governs how many subdivisions fall within the smoothed stretches of the extrusion profile. TIP: Splines are editable from inside the Spline Editor panel as well. It affords a roomier workspace for handling any spline, the Custom Extrusion included. Extrusion profile spline control: Don't try to shrink to zero size at the Front/Back face. Doing so brings on Z-fighting that stems from self-intersecting faces. To steer clear of this, see that the first and last point have their profiles set to 0.

### Force Monospaced

This slider control lets you bypass the kerning (the spacing between characters) the font defines. Leaving this slider at zero (its default value) makes Fusion lean entirely on the kerning each character carries. A value of one makes the spacing between characters perfectly uniform, that is, monospaced.

Text 3D Advanced Controls let you kern letters by hand. Use Font Defined Kerning This switches on kerning as the True Type font spells it out, and it's on by default. Manual Font Kerning Manual Font Kerning happens through the Text+ node alone. To kern Text3D by hand, build the text with the Text+ node and kern it there. Next, right-click the tool's name in the Inspector and pick Copy. With the settings copied, select the Text 3D node and pick Paste Settings out of the Inspector's contextual menu. Once the manual kerning lands in the Text 3D node, the Inspector's two buttons clear either the selected character's kerning or every kerning adjustment across the current text.

### Layout Tab

The Layout Tab serves to place the text in one of four different layout types.

Text 3D Layout tab for switching the text block's layout

Layout Type This menu picks the layout type the text uses.

- Point: Of all the layout modes, Point layout is the most basic. The text wraps around a center point you can move.
- Frame: With Frame layout you lay out a rectangular frame against which the text gets aligned. The alignment controls handle justifying the text both vertically and horizontally inside the frame's edges.
- Circle: Circle layout runs the text along the arc of a circle or oval. You control the diameter as well as the width of that circular shape. With the layout in this mode, the Alignment controls decide whether the text rides the inner or outer edge of the circle, plus how several lines of text get justified.
- Path: With Path layout you bend your text along the edges of a path. The path may merely lend style to the text, or it can be animated by way of the Position on Path control, which surfaces once this mode is chosen.

Center X, Y, and Z These controls place the layout's center. As an instance, shifting the center X, Y, and Z parameters while the layout sits at Frame moves where the frame holding the text falls. Size This slider governs how large the layout element is scaled. As an instance, raising size while the layout sits at Frame enlarges the frame holding the text. Width and Height Setting the Layout mode to either Circle or Frame brings the Width and Height controls into view. With the Layout mode at Frame alone, those same Width and Height controls appear. They serve to tune the Layout element's dimensions and aspect. Rotation Order These buttons let you pick the sequence in which the text's 3D rotations occur. X, Y, and Z These angle controls serve to set the Layout element's angle along any axis. Fit Characters This menu control becomes visible solely once the Layout type is set to Circle. The menu lets you pick how the characters get spaced to sit along the circumference. Position on Path The Position on Path control governs where the text falls along the path. Values below zero or above one push the text past the end, carrying on in the same direction the path's final two points set. Right-Click Here for Shape Animation This label surfaces solely once the Layout type is set to Path. It opens a contextual menu offering options for tying the path to other paths within the node tree and for animating the path's spline points across time.

### Transform Tab

The Text 3D Inspector in fact holds two Transform tabs. The first Transform tab belongs to the Text 3D tool alone, whereas the second is the common Transform tab that shows up on many 3D nodes. What follows covers the Text 3D-specific Transform tab, since it carries some controls unique to this node.

### Text 3D Transform tab

Transform This menu sets which slice of the text the transformations applied in this tab act upon. Transformations can hit the line, word, and character levels all at once. This menu exists merely to hold the count of visible controls to something reasonable.

- Characters: Every text character gets transformed around a center axis of its own.
- Words: Every word gets transformed on its own, around the word's center axis.
- Lines: Every line of the text gets transformed on its own, around that line's center axis.

Spacing The Spacing slider serves to tune how much space falls between each line, word, or character. Values below one usually start to make the characters overlap. Pivot X, Y, and Z This gives you precise control over where the axis sits. By default the axis lands at the computed center of the line, word, or character. The pivot control acts as an offset, so a value of 0.1, 0.1 here would nudge the axis down and to the right for each of the text elements. Positive values on the Z-axis slider push the axis farther along the axis (away from the viewer). Negative values draw the axis of rotation nearer. Rotation Order These buttons set the order the transforms run in. X, Y, and Z would mean the rotation hits X first, then Y, then Z. X, Y, and Z These controls serve to set the text elements' angle across any of the three dimensions. Shear X and Y Work these sliders to skew the text elements' slant along the X- and Y-axis. Size X and Y Work these sliders to alter the text elements' size along the X- and Y-axis.

### Shading

The Shading tab for the Text 3D node governs the text's overall look and how lights play across its surface.

### Text 3D Shading tab

Opacity Dropping the material's opacity pulls down the specular and diffuse colors' color and Alpha values in equal measure, rendering the material transparent and letting hidden objects show through. Use One Material Clearing this option exposes a second batch of Material controls covering the text's beveled edge. Type For a solid color texture, pick the Solid mode. Picking the Image mode exposes a fresh external input on the node, one you can wire to another 2D image. Specular Color Specular Color fixes the color of light that bounces off a shiny surface. The more specular a material runs, the glossier it looks. Surfaces such as plastics and glass usually carry white specular highlights, while metallic surfaces such as gold carry specular highlights that tend to take their color from the material color. The basic shader material offers no input for textures to govern the object's specularity. Turn to nodes in the 3D Material category whenever finer control over the specular look is called for. Specular Intensity Specular Intensity governs how strong the specular highlight is. Should the specular intensity texture port hold a valid input, this value gets multiplied by that input's Alpha value.

Specular Exponent Specular Exponent governs the specular highlight's falloff. The larger the value, the sharper that falloff, and the smoother and glossier the material looks. The basic shader material offers no input for textures to govern the object's specular exponent. Turn to nodes in the 3D Material category whenever finer control over the specular exponent is called for. Image Source This control fixes where the texture laid onto the material comes from. Set the option to Tool, and an input shows up on the node that lets you feed a 2D node's output in as the texture. Picking Clip opens a file browser for choosing an image or image sequence off disk. The Brush option hands you a list of clips sitting in the Fusion\brushes folder. Bevel Material This option surfaces solely while the Use One Material checkbox control is ticked. The controls beneath this option duplicate the Material controls above exactly, but apply only to the text's beveled edge. Position, Rotation, Shear, and Size These transform controls behave much like the transform controls on the Transform tab while a single shading element is switched on from the top of the Shading tab. Once two or more shading elements are switched on, though, these transform controls act on whichever shading element is currently selected. That lets you steer the position, rotation, shearing, and size of borders, fill colors, and shadows on their own.

### Uncapped 3D Text

To conceal the front face of extruded text, clear Use One Material on the Shading tab and drop the first material's color to black, its Alpha value included.

### Common Controls

Transform and Settings Tabs The Inspector's Transform and Settings tabs recur across other 3D nodes. These shared controls get a full treatment toward this chapter's close, in the "The Common Controls" section.
