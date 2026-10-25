# Shared title generator parameters and title generator settings parameters

Version: DaVinci Resolve 20.3 Reference Manual. Context: Titles generators and stills.
[Chapter index](INDEX.md) / [Previous section](adding-titles-and-safe-area-overlays.md) / [Next section](saving-titles-in-the-media-pool-for-future-use-and-generators.md)
<a id="source-a-simple-spreadsheet-saved-in-csv-format"></a> <a id="source-fusion-titles-and-fusion-templates"></a> <a id="source-multitext-titles"></a> <a id="source-shared-title-generator-parameters"></a> <a id="source-text"></a> <a id="source-text-viewer-controls"></a> <a id="source-the-text-title-generator"></a> <a id="source-title-generator-settings-parameters"></a>

### Shared Title Generator Parameters

Apart from the Text+ generator, every other title generator in DaVinci Resolve can do rich text styling. What that means is you can grab any stretch of a generator's text and style it differently. You might, for instance, run three lines of text inside one generator and style each line on its own to land a particular design.

A lone generator holding three lines of text, each styled its own way Every title generator leans on the same parameters within the Inspector's Video Title panel for editing and styling text:

- Rich Text: A control group made up of a text entry field plus parameters for styling different stretches of the text on their own. Text: A text entry field where you edit the title being generated. With no characters selected, the styling controls hit the whole block of text. Select a particular run of characters, though, and the styling controls touch only that selection. Text in this field is also editable directly in the Timeline Viewer. Font family: A pop-up where you select whichever font family your workstation has installed. Font face: A pop-up where you select which face within the currently chosen font family to apply. Color: Summons the standard color picker so you can settle on a font color. Size: Slider that dials in the text size. Tracking: Slider governing how much space sits between characters. Line spacing: Slider governing how much space falls between the selected line of text and the one directly under it.

Font style: Buttons that lay styling onto the text—underline, plus overhead line, strikethrough, then superscript along with subscript. Font case: A pop-up that pushes the text selection toward any one of these: Mixed Case (the default), or All Caps, or All Lowercase, or Small Caps, or else Title Caps. Alignment: Buttons fixing the alignment method, where your choices run left, then centered, then right, then justified. Anchor: Buttons fixing how text anchors against the current position—on the horizontal axis between top, centered, bottom, and on the vertical axis between right, centered, left. Position: A pair of X and Y parameters pinning the bottom left-hand corner (under the default Anchor settings) of the rich text block being generated. It mirrors what happens as you drag a selected text box around inside the Timeline Viewer. Zoom: A pair of X and Y parameters pinning the text's scale. There's a link button to hold the X and Y parameters locked together. It mirrors what happens as you resize a selected text box inside the Timeline Viewer, be it from the corners (for proportional resizing) or by way of the top, bottom, and sides (where you stretch or squeeze the text). Rotation Angle: A slider that spins the text's orientation. It mirrors what happens when you rotate a selected text box inside the Timeline Viewer by way of the rotation handle.

- Drop Shadow: A cluster of controls letting you lay a customizable drop shadow over every character of text being generated.

Color: Summons the standard color picker so you can settle on a drop shadow color. Offset: A pair of X and Y parameters pinning how far the drop shadow strays from where the original text sits. Blur: A slider that softens the drop shadow. Opacity: A slider that sets how see-through the drop shadow becomes.

- Stroke: Lets you wrap an outline around every character of text being generated. Color: Brings up the standard color picker for picking the stroke color. Size: A slider lets you pick the stroke thickness, in pixels.
- Background: This cluster of controls hands you an exceptionally flexible rectangle or rounded rectangle shape you can use to drop in a background, bar, outline, or other intersecting shape while designing a title.

Color: Summons the standard color picker so you can settle on the interior color of the background shape. Outline color: Summons the standard color picker so you can settle on the outline color of the background shape. Outline width: A slider where you dial in how thick, in pixels, the background shape outline runs. Width: A slider where you dial in how broad the background shape becomes. Height: A slider where you dial in how high the background shape rises. Corner radius: A slider where you dial in how rounded the rectangle edges turn out. Center: A pair of X and Y parameters handy for nudging the background shape away from the text being generated. Opacity: A slider where you dial in how see-through the background shape is.

### Title Generator Settings Parameters

Beyond that, the Video Inspector's Settings panel gives each generator its Composite, Transform, and Cropping parameters, which you use to composite, resize, and animate titles over other Timeline clips when you're chasing motion graphics effects. Those parameters match the ones available for every clip, covered later in this chapter.

### The Text+ Title Generator

A fresh kind of title generator, called Text+, lives within the Effects Library toolbox under the Titles category. This is the wildly full-featured 2D text generator out of Fusion, ready for editing and customizing right in the Edit page. It handles most of what the Text generator manages, rich text editing and on-screen controls in the Timeline Viewer included. It also brings far more styling and animation controls than the Text generator. TIP: As of this writing, the Text generator stays plenty useful for quickly knocking out text pages carrying multiple styles, whereas the Text+ generator shines at building text for animated motion graphics.

The new Text+ title generator, along with new Fusion titles below You work the Text+ generator the same way you work any generator in the Edit page. Just drop it onto a Timeline video track, select it, and head into the Inspector to edit and keyframe the many properties it carries so you can build whatever sort of title you're after. On top of its far larger pile of styling options, the fact that the Text+ generator grew out of a compositing tool means it brings many more panels' worth of keyframable parameters, advanced animation controls baked right in. Among them are keyframable Write On/Write Off controls; shape-driven layout and animation (the choices here being point, frame, circle, and path); transforms and animation at the character, word, and line level; shading of an advanced sort; plus interlacing support that's full.

A quartet of the Text+ title generator's panels, namely Text, Layout, Transform, and Shading

Better still, once the playhead rests on your new Text+ "Fusion Title," opening the Fusion page lets you get at its parameters from there too, should you care to start expanding this one generator into a multi-layered motion graphics extravaganza.

Open the Text+ node on the Fusion page and it shows up there as a genuine Fusion page operation NOTE: Should you receive a project carrying a Text+ title while a specific font used in that title is missing from your local machine, an overlay surfaces on the Viewer letting you know.

### Text+ Viewer Controls

You can carry out assorted editing actions on Text+ straight in the viewer overlay—editing text, showing a cursor, and selecting text among them. That reach extends to the viewer inside the Edit page once the Fusion overlay is switched on.

The Text+ Viewer controls switch on when you pick Fusion Overlay (circled) from the Timeline Viewer Overlay menu.

- To enable Text+ Viewer controls: Pick Fusion Overlay from the Timeline Viewer Overlay drop-down menu. From there your mouse can work the text in the Viewer to select and edit it, plus shift it around within the frame.

For fuller detail on the wide reach of the Text+ generator, see Chapter 104, "Generator Nodes."

### Fusion Titles and Fusion Templates

The many additional Fusion titles you'll find across the Effects Library are custom-built text compositions, animation baked in, that surface custom controls in the Inspector.

A Fusion title that builds an animated lower third, its controls sitting open in the Inspector In truth, these text generators amount to Fusion templates—Fusion compositions turned into macros that ship alongside DaVinci Resolve for use inside the Edit page like any other generator. All sorts of Fusion title compositions can be crafted on the Fusion page and kept for Edit-page use: build a macro and place it inside the directory at /Library/Application Support/ Blackmagic Design/DaVinci Resolve/Fusion/Templates/Edit/Titles, though that's a story for another time. Text+ generators carry one further perk: they can be graded like any other clip, with no need to build a compound clip first.

### MultiText Titles

Built atop Text+, the MultiText tool in the Titles category hands you more room to add and format several text layers, all inside the one tool. It brings in a Text List along with a mild reshuffle of controls, putting functionality first based on what editors need.

The MultiText tool in the Titles section lets you build several text layers and styles and composite them all inside a single interface.

### Text

The Text List acts as a master panel, laying out every text layer you've made. The list and its controls stay on hand across the Inspector tabs, giving you quick reach to adjust both the text and its properties whenever you like. Right under the Text List, the Add Text buttons present three commonly used layout types: Point, Text Box, and Circle, making it painless to drop in your preferred input style.

- Point: The text springs from a single point on the screen, with no horizontal or vertical limits.
- Text Box: The text is held in horizontally and vertically by a bounding box. With Text Box

selected, the Wrap to Text Box and Clip to Text Box checkboxes turn up under the Layout tab. With Wrap to Text Box on, your text automatically rolls onto the next line once it reaches the text box edge. With Clip to Text Box on, any text spilling past the text box's boundaries gets visually trimmed away, heading off overflow while leaving the surplus content intact.

- Circle: The text is laid along an arc you define.
- CSV: Pulls a Comma Separated Value (.csv) spreadsheet into MultiText and formats it automatically as columned aligned text. Once it's in MultiText, you can rework the titles however suits you.

### A simple spreadsheet saved in .csv format

When that .csv file lands in MultiText, every column arrives as its own separate text list item The Text tab additionally bundles an array of animation and text formatting tools much like those in a word processor. Layout This set of parameters decides where the text lands. Shading This set of parameters decides the text's attributes—drop shadows and outlines among them. Page This set of parameters lets you set a custom-colored background behind the text layers. Image This set of parameters lets you manage the overall image: aspect ratio, along with color and gamma spaces. Settings This set of parameters supplies the standard Settings controls for Fusion Generator Nodes. To dig further into the assorted options, turn to Text+ Tool in MultiText see Chapter 104, "Generator Nodes."
