# Text layout tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Text.
[Chapter index](INDEX.md) / [Previous section](text-tab-spacing.md) / [Text+ TXT+](multitext-and-plasma-and-text.md) / [Next section](text-character-level-styling.md)
<a id="source-generator-nodes-part-3"></a> <a id="source-layout-tab"></a> <a id="source-shading-tab-1"></a> <a id="source-text-layout-tab-controls"></a> <a id="source-text-shading-tab-controls"></a> <a id="source-text-transform-tab-controls"></a> <a id="source-transform-tab"></a>

### Text+ Layout tab controls

### Layout Tab

The text-positioning controls live in the Layout tab. The Type drop-down menu lets you pick one of four layout types.

- Point: Of all the layout modes, Point layout is the most basic. The text wraps around a center point you can move.
- Frame: With Frame layout you lay out a rectangular frame against which the text gets aligned. The alignment controls handle justifying the text both vertically and horizontally inside the frame's edges.
- Circle: Circle layout runs the text along the arc of a circle or oval. You control the diameter as well as the width of that circular shape. With the layout in this mode, the Alignment controls decide whether the text rides the inner or outer edge of the circle, plus how several lines of text get justified.
- Path: With Path layout you bend your text along the edges of a path. The path may merely lend style to the text, or it can be animated by way of the Position on Path control, which surfaces once this mode is chosen.

Center X, Y, and Z These controls place the layout element's center within space. X and Y act as onscreen controls, whereas Center Z appears as a slider among the node controls. Size This slider governs how large the layout element is scaled. Perspective This slider adds or strips perspective away from the rotations that the Angle X, Y, and Z controls produce. Rotation Rotation is a row of buttons that lets you pick the sequence in which the text's 3D rotations occur. Angle dials are available for setting the Layout element's angle on any axis. Width and Height Whenever the Layout mode is Circle or Frame, the Width control becomes visible. As for the Height control, it appears solely while the Layout mode sits at Frame. The Width and Height controls serve to tune the Layout element's dimensions and aspect. Fit Characters This menu control shows up only when the Layout type is set to Circle. The menu lets you pick how the characters get spaced to sit along the circumference. Position on Path The Position on Path control governs where the text falls along the path. Values below 0 or above 1 push the text past the path, continuing along the same direction as the path's vector between the final two keyframes. Background Color This node usually renders its text against a transparent background. This Color Picker control lets you assign a background color instead. Right-Click Here for Shape Animation This label surfaces only when the Layout type is set to Path. It opens a contextual menu offering options for tying the path to other paths within the node tree and for animating the path's shape across time. For further detail, consult Chapter 73, "Animating with Motion Paths," within the DaVinci Resolve Reference Manual, or else Chapter 11 of the Fusion Reference Manual.

### Text+ Transform tab controls

### Transform Tab

The Transform tab serves to move, rotate, shear, and scale text by character, word, or line. Transform The Transform menu sets which slice of the text the transformations applied in this tab act upon. Transformations can hit the line, word, and character levels all at once. This menu exists merely to hold the count of visible controls to something reasonable.

- Characters: Every text character gets transformed around a center axis of its own.
- Words: Every word gets transformed on its own, around the word's center axis.
- Lines: Every line of the text gets transformed on its own, around that line's center axis.

Spacing The Spacing slider tunes the gap between each line, word, or character. Values under 1 usually start to make the characters overlap. Pivot X, Y, and Z This gives you precise control over where the axis sits. By default the axis lands at the computed center of the line, word, or character. The Axis control acts as an offset, so a value of 0.1, 0.1 here would nudge the axis down and to the right for each of the text elements. Positive values on the Z-axis slider push the axis of rotation farther along the axis (away from the viewer). Negative values draw the axis of rotation nearer. Rotation These buttons set the order the transforms run in. X, Y, and Z would mean the rotation hits X first, then Y, then Z. X, Y, and Z These controls tune the angle of the text elements across any of the three dimensions.

Shear X and Y Work these sliders to skew the text elements' slant along the X- and Y-axis. Size X and Y Work these sliders to alter the text elements' size along the X- and Y-axis.

### Text+ Shading tab controls

### Shading Tab

Within the Shading tab sit the controls for tuning the text's shading, texture, and softness. Transformations are steerable from here as well, layering extra transformations onto as many as eight separate text shading elements on their own. Shading Element The menu's eight number values let you pick which element the adjustments in this tab affect. Enabled Tick this checkbox to switch each layer of shading elements on or off. Element 1, the fill color, is on by default. A shading element's controls stay hidden until this checkbox is ticked. Sort By This menu lets you order the shading elements by number priority, with 1 the topmost and 8 the bottommost element, or by Z depth, going off the Z Position parameter. Name This text label lets you hand each shading element you build a more descriptive name.

Appearance The four Appearance buttons set how the shading element gets laid onto the text. Which controls turn up below hinges on the appearance type you pick.

- Text Fill: Here the shading element covers the whole of the text. This serves as the default mode.
- Text Outline: Here the shading element renders as an outline tracing the text's edges.
- Border Fill: Here the shading element fills a border that wraps the text. Five extra controls come

with this shading mode.

- Border Outline: In Border Outline mode an outline is rendered around the border that wraps the

text. A handful of extra controls come with it. Opacity The Opacity slider sets the shading element's overall transparency. Generally it's wiser to apply opacity to a shading element than to tweak the Alpha of the color on that element. Blending This menu lets you pick how the renderer handles an overlap between two characters in the text.

- Composite: Merges the shading over the top of itself.
- Solid: Sets the pixels in the overlap region to opaque.
- Transparent: Sets the pixels in the overlap region to transparent.

Thickness (Outline only) Thickness sets how thick the outline is. Larger values yield thicker outlines. Adapt Thickness to Perspective (Outline only) Ticking this checkbox makes your outline taper thinner where the text recedes from the camera and thicker where it draws nearer. This yields a more believable outline on text transformed in 3D, though it adds considerably to render time. Outside Only (Outline only) Ticking this checkbox confines the outline to the text's outer edge alone. Out of the box, the outline straddles the edge and overlaps the text in part. Join Style (Outline only) These buttons present choices for how the outline's corners are rendered. The choices include Sharp, Rounded, and Beveled. Line Style (Outline only) This menu supplies further choices for the line's style. Apart from the standard solid line, an assortment of dash and dot patterns is on offer. Level (Border Fill only) This governs which slice of the text border gets filled.

- Text: This draws a border around the entire text.
- Line: This draws a border around each line of text.
- Word: This draws a border around each word.
- Character: This draws a border around each character.

Extend Horizontal and Extend Vertical (Border only) This slider alters each border's dimensions. Round (Border Fill and Border Outline only) Use this slider to round off the border's corners. Color Types Apart from solid shading, you can also apply a gradient fill or wrap an external image onto the text. This menu decides whether the shading element's color comes from a color or gradient the user picked, or instead from an outside image source. Which controls turn up below depends on the Color Type you've chosen.

- Solid: With the Type menu in Solid mode, color selector controls appear so you can pick the text's color.
- Image: A node's output from the node tree gets used to texture the text. Which node serves is set through the Color Image control that surfaces once this option is picked.
- Gradient: With the Type menu set to Gradient, extra controls appear letting you customize the gradient colors and their direction.

Using the Gradient Color Bar You pick the gradient's colors with the gradient color bar. Its two default color stops fix the start and end colors. To swap the gradient's colors, select a color stop and then set a fresh color via the Eyedropper or the color swatch. The gradient bar lets you add, move, copy, and delete color. To recolor one of them, click the triangle beneath that color on the bar. Adding a color stop onto the gradient bar goes like this: 1 Click any point along the foot of the gradient bar. 2 Lean on the Eyedropper or the color swatch to choose what color that stop takes. Shifting a color stop across the gradient bar: Pull a stop left or right along it. Duplicating a color stop: Keep Command (macOS) or Ctrl (Windows) held down while pulling a stop. Removing a color stop: Pull it up and off past the gradient bar. Image Source (Image Mode only) Three options for getting the image that fills the text live in the Image Source menu.

- Tool: Shows a Color image text field into which you can drop a tool from the node tree as the text's fill.
- Clip: Offers a Browse button for picking a media file off your hard drive as the text's fill.
- Brush: Shows a Color Brush menu from which you can pick one of Fusion's paint brush bitmaps as

the fill for text.

Color Image/Color Brush (Image Mode only) You pick the tool or paint brush that fills the text through the Color Image text box and the Color Brush menu. Within the Color Image text box, type the name of the node tree node that supplies the image. You can key the name in by hand, drag the node out of the node tree into the text box, or right-click and pick Connect To off the contextual menu to choose the image to use. For the Color Brush, pick the Brush off the menu. Image Sampling (Image Mode only) This menu picks the sampling type used for rendering and transforming the shading. The Pixel shading default covers 90% of jobs just fine. To cut visible aliasing in the text, switch the sampling type to Area. That's slower yet can yield finer results. Set it to None and rendering goes faster, but with no extra sampling applied the quality drops. Image Edges (Image Mode only) This menu picks how transformations laid on image shading elements behave when they spill off the text's edges. Shading Mapping (Image Mode only) This menu chooses whether the whole image is stretched to fill the text or scaled to fit—holding the aspect ratio while cropping part of the image as required. Mapping Angle (Image and Gradient Modes only) Rotating the image or gradient around the Z-axis is what this control does. Mapping Size (Image and Gradient Modes only) Scaling the image or gradient is this control's job. Mapping Aspect (Image and Gradient Modes only) Stretching or squeezing the image or gradient up and down falls to this control. Mapping Level (Image and Gradient Modes only) The Mapping Level menu picks how the image gets mapped onto the text.

- Full Image: Applies the entire image to the text.
- Text: Applies the image to fit the entire set of text.
- Line: Applies the image per line of text.
- Word: Applies the image per each word of text.
- Character: Applies the image per individual character.

Softness X and Y How soft the text outline behind the shading element is gets set by these sliders. You control the X- and Y-axis on their own. Apply Softness to Fill Color Tick this checkbox and blur (softness) lands on the shading element. You see the result best on a shading element that draws on an external image. Softness Glow This slider lays a glow over the softened part of the shading element.

Softness Blend How much the softness control's result blends back in with the original is set by this slider. You can use it to ease off the soften operation's outcome. Priority Back/Front Live only when the Sort By menu sits on Priority, this slider overrides the priority setting and fixes the layering order of the shading elements. Slide it rightward to draw an element nearer the front. Push it leftward to slip one shading element behind another. Offset X, Y, and Z These controls lay an offset on the shading elements from the text's global center (the one fixed in the Layout tab). Set X0.0, Y0.1 in the coordinate controls and the shading element lands centered with 10 percent of the image pushed further down the screen along the Y-axis. Positive values on the Z-Offset slider shove the center further from the camera, while positive values draw it nearer the camera. Pivot X, Y, and Z These controls pin down the exact spot of the axis for whichever shading element is chosen. Out of the box the axis sits at the worked-out center of the line, word, or character. The axis control behaves as an offset, so that 0.1, 0.1 here would shove the axis down and to the right for the shading element. Positive values on the Z-axis slider push the rotation axis further along the axis (away from the viewer). Negative values pull the rotation axis nearer. Rotation X, Y, and Z These controls tune the angle of the chosen shading element in any of the three dimensions. Shear X and Y Tune these sliders to alter how the chosen shading element slants along the X and Y axis. Size X and Y Tune these sliders to alter the chosen shading element's size along the X and Y axis.
