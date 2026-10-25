# Media pool and node editor

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the color page.
[Chapter index](INDEX.md) / [Previous section](color-page-interface-and-default-layout-of-the-color-page.md) / [Next section](curves-palette-and-colorslice-palette.md)
<a id="source-a-clip-thumbnail-in-the-thumbnail-timeline"></a> <a id="source-all-palettes-seen-in-the-palette-bar"></a> <a id="source-center-palette-selection-buttons"></a> <a id="source-left-palette-selection-buttons"></a> <a id="source-media-pool"></a> <a id="source-mini-timeline"></a> <a id="source-node-editor"></a> <a id="source-palette-area"></a> <a id="source-the-thumbnail-timeline-with-a-mini-timeline-below"></a> <a id="source-thumbnail-timeline"></a> <a id="source-timeline"></a>

### Media Pool

The Media Pool is on hand in the Color page, which makes it simple to drag and drop clips you’d like to use as external mattes straight into the Node Editor for quick, easy hookup when building various Color page effects. Opening it swaps out the Gallery, since it occupies the same area. For the most part, the Color page Media Pool behaves like the Media Pool on almost every other page of DaVinci Resolve.

The Media Pool is available in the Color page. Dragging a clip from the Color page Media Pool over to the Node Editor triggers two things:

- The clip becomes an external matte within the current grade, usable as a matte for secondary adjustments or — paired with the Layer mixer — as a compositing layer for blending textures or images into your grade.
- The clip is also hooked up automatically, as a clip matte, to the Media Pool clip that matches the one you’re grading, which helps you keep straight which clips draw on others as mattes.

For more about the Media Pool, turn to Chapter 18, “Adding and Organizing Media with the Media Pool.”

### Node Editor

The Node Editor is where you stitch one or more individual corrections (nodes) into a finished multi-correction grade (node tree). It’s a potent way to assemble grades, since the various node types let you create different blends of corrections and very precise adjustments by reordering operations, combining keys, or shifting how the various adjustments are layered. For more about the Node Editor, consult Chapter 143, “Node Editing Basics.”

Node Editor to construct your grade processing signal flow

### Timeline

The Timeline gives you several ways to navigate the clips in your project and to track what has been done to which ones. It splits into two parts, each showing different information and offering different controls, and each able to be opened or closed on its own through the Clips and Timeline buttons on the Interface toolbar.

### The Thumbnail timeline with a Mini-Timeline below

### Thumbnail Timeline

Up top is the Thumbnail timeline, where each clip stands for a single frame. The Thumbnail timeline (or its alternate form, the Lightbox) is the simplest way to pick which clip you want to work on and to make clip selections for various grade-management tasks. Whichever clip is currently selected — the one whose controls appear in the Color page’s various palettes — is highlighted in orange. A good deal of useful information surrounds each thumbnail above and below it — among it a clip’s clip number, source timecode, and track number, plus whether the clip is flagged, automatically linked or grouped, tracked, and so on.

### A clip thumbnail in the Thumbnail timeline

You can change what appears beneath each thumbnail by double-clicking the space below it. Several options exist, and you can keep double-clicking to cycle among them:

- Clip format or codec (the default)
- Clip Name (either the clip name or the file name, according to how View > Show File Names is set) or

Multicam Angle (when you’re working with multicam clips)

- Version name or number

### Mini-Timeline

Below it, the Mini-Timeline presents a compact view of the Edit page Timeline’s video tracks, where each clip stretches to its real duration. This gives the most faithful view of how the current timeline is built, because clip length stands in for duration and the multiple tracks appear, so you can spot which clips overlap. A Timeline Ruler scrubs the playhead over several clips and zooms out far enough to show every clip in your entire program.

The Mini-Timeline reveals timeline structure, while small track header controls let you switch tracks on, switch tracks off, and have the playhead bypass particular tracks Small track labels down the left of each track in the Mini-Timeline let you turn a track on or off with a click (white labels mark enabled tracks, gray ones disabled). Option-click one of these controls and the track stays enabled but the playhead passes it over during the Next and Previous Clip commands — useful when you’d rather skip clips you don’t need to grade (such tracks show a red label). Inside the Mini-Timeline, whichever clip is selected appears highlighted in orange, and you select any clip by clicking it. A scroll bar at the bottom moves you left and right, while the mouse scroll wheel zooms in and out. The Mini-Timeline shows six tracks of video at most. Should your project hold more, you can scroll up and down to expose the hidden ones. Any markers placed on clips or on the Timeline back in the Edit page turn up here too, and clicking any marker reveals and lets you edit its color and notes.

As pictured above, a colored outline encircles the clip number of any shot that’s been graded, and that outline doubles up once extra versions are applied to the clip. For fuller detail on the Color page Timeline, see Chapter 130, “Camera Raw Palette.”

### Palette Area

Most of the everyday tools and functions for grading are spread across a series of palettes in the Color page’s palette area. You reach these palettes through a row of palette buttons along the Palette bar at the top of the area.

### All palettes seen in the Palette bar

These buttons also tell you which palettes carry adjustments for the node currently selected in the Node Editor. A palette holding adjustments shows a small orange dot on its corresponding palette button.

An orange dot on a palette button signals that the palette holds adjustments Left Palettes A row of palettes along the Color page’s lower left brings up different sets of grading tools, used chiefly to work color, contrast, and raw media format settings. You open any individual palette by clicking its matching icon at the top of the Palette panel.

### Left palette selection buttons

Camera Raw palette: For metadata adjustments to raw media formats Color Match palette: Automatic grading driven by test charts Primaries: Graphical color balance controls plus master wheels, together with a Slider mode that adjusts YRGB Lift/Gamma/Gain HDR palette: Sophisticated primary grading controls built for wide-gamut media and SDR or HDR mastering RGB Mixer: For blending color channels into one another Motion Effects palette: Carrying controls for noise reduction and artificial motion blur The five palettes work individually or in combination, according to your goal. For more on most of them, see Chapter 131, “Primaries Palette.” For the Motion Effects palette specifically, see Chapter 153, “The Motion Effects and Blur Palettes.” Center Palettes Once you’re at 1920x1080 resolution or beyond, a second cluster of palettes lines up at the Color page’s lower center. These palettes range across many functions, and what you achieve with them can be folded together with what you do using the Color palettes.

### Center palette selection buttons

NOTE: When the resolution is lower, the Left and Center palettes combine so the DaVinci Resolve interface fits a tighter space.

Among the center palettes are the Curves palette, Color Slice palette, Color Warper palette, Qualifier palette, Window palette, Tracker palette, Magic Mask palette, Blur palette, Key palette, Sizing palette, and Stereoscopic 3D palette.
