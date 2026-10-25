# Primatte and relight

Version: DaVinci Resolve 20.3 Reference Manual. Context: Primatte, Relight.
[Chapter index](INDEX.md) / [Previous section](primatte-replace-tab.md) / [Next section](relight-and-ultra-keyer.md) / [Primatte Pri](matte-control-and-primatte.md)
<a id="source-basic-node-setup"></a> <a id="source-controls"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-light-properties"></a> <a id="source-relight-node-introduction"></a> <a id="source-relight-rlt"></a> <a id="source-removing-spill"></a> <a id="source-surface-properties"></a> <a id="source-the-relight-controls"></a> <a id="source-the-relight-node"></a>

### Removing Spill

Those first three sections produced a clean matte. From here, the foreground is ready to be composited over any background image. Yet if color spill clings to the foreground subject, one last step is needed to clear that screen spill and yield a more natural-looking composite. 1 From the View Mode menu, pick Composite. 2 Over the viewer, press the Alpha/RGB toggle button to view the RGB image. Primatte offers two routes for removing the spill color: Spill Sponge: The fastest is to press the Spill Sponge button and then sample the spill regions away. You can take out further spill with the tools under the Fine Tuning tab or via the Spill(-) button. Fine Tuning Tab: To work spill through the Fine Tuning tab, begin by scrubbing over the spill color in the viewer. On most images, tweaking the Spill slider is all it takes to clear whatever spill is left. NOTE: When the Fine Tuning tab’s slider is used to remove spill, spill color replacement follows whatever the Spill Replacement options are set to. The remaining two sliders serve the same way for other key adjustments. The Detail slider governs matte softness for the color sitting nearest the background color. As an example, you can salvage lost wispy smoke in the foreground by entering Fine Tuning mode, clicking where the smoke begins to fade out, and dragging the Detail slider left. The Transparency slider governs matte softness for the color sitting nearest the foreground color. For instance, with thick opaque smoke in the foreground, you can render it semitransparent by dragging the Transparency slider right after selecting the pixels in Fine Tuning mode.

### Relight [RLT]

### The Relight node

### Relight Node Introduction

Relight lets you drop light sources into your scene, lighting the objects there in a believable way. Whereas a plain shape node carries a polygon pinned to the screen, Relight studies the forms of people and objects to build a Surface Map and leans on that map to bounce light correctly. Tuned well, the effect conjures the impression of light tracing an object’s curves, glinting off highlights and fading away into shadow. Relight earns its keep when you wish there’d been an extra light on set, when you want to play up an existing light so it matches another shot, or when you’re after more convincing day-for-night grading.

NOTE: Though the Relight effect fabricates a sense of depth by analyzing a scene’s surfaces, it stops short of computing the 3D relationships among the scene’s objects. Shapes can’t be set to throw shadows, and no depth information gets generated.

For more information on Relight, see Chapter 162, “Resolve FX Refine.”

### Inputs

Three inputs feed the Relight tool. Input: The orange input takes the primary footage you intend to relight. Effect Mask: A mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps produced by other tools is what the optional blue effect mask input accepts. Wiring a mask here confines the filter to nothing but the pixels inside that mask. An effects mask gets applied to the tool only after the tool has been processed. Normals: The green input lets you attach an externally created normal maps in place of the one the Relight tool makes on its own.

### Basic Node Setup

Putting the Relight tool to work means assembling some extra node structure around it. Beyond the usual MediaIn node, you’ll want a Merge node plus another effect such as the ColorCorrector or Brightness/Contrast tools.

- MediaIn: The MediaIn node’s output feeds the orange inputs of the Relight, the ColorCorrector (or whatever effect node you use), and the Merge node.
- ColorCorrector (effect): Takes its input from the MediaIn node, and its output runs into the Merge node’s green foreground input.
- Relight: Takes its input from the MediaIn node, and its output runs into the Merge node’s blue effect mask input. Set this node to show in whichever viewer you prefer.
- Merge: Pulls its background input from the MediaIn node, its green foreground input from the ColorCorrector, and its blue effect mask input from Relight. From there its output carries on to the rest of the node tree or to media out. Set this node to show in whichever viewer you prefer.

The node tree laying out the node structure that surrounds the Relight tool. Bear in mind the ColorCorrector can give way to any other effect you favor.

Once the node structure above is in place, you ought to see something close to the arrangement shown below. Viewer 1 carries the finished relight effect that moves on to the rest of the node tree. Viewer 2 holds the relight interface, where you can drag the lighting position around the frame. Which form it takes depends on your Relighting Map Preview option — either a black-and-white embossed image or the RGB image atop a semi-transparent background.

On the left, Viewer 1 shows the Merge node; on the right, Viewer 2 shows the Relight node, with both groups of on-screen controls switched on.

### Inspector

### The Relight controls

### Controls

The Controls give you the run of every parameter on the Relight tool. The viewer carries extra on-screen controls too, which vary with the kind of Relight effect you pick. To learn more about working the Relight controls, turn to Chapter 162, “Resolve FX Refine.”

- Surface Map: This sets which mode you’ll use to build the Surface Map. Use Internal: Builds the Surface Map within the tool itself. Use Normals Input: Pulls in an externally created Surface Map from another node. Wire that map into the green input of the Relight node.
- Output Surface Map: Ticking this box makes this copy of the effect put out a multi-colored map of the input frame. That Surface Map can afterward feed a second Relight node where you place and tune the light sources.
- Directional / Point Source / Spotlight: Directional: Makes a light source casting from one specific direction at infinite distance. Point Source: Makes a light source casting outward from a central point. Spotlight: Is likewise a point source, only aimed into a cone shape.
- Relighting Map Preview: Ticking this box exposes the Alpha channel of this light’s effect. Clearing it shows the current image instead, with the light mask sitting in the Alpha channel. The Map Preview’s bright areas mark where the Relight is acting on the image.

A car image shown with the Map Preview box ticked. The brighter zones reveal where and how strongly the Relight tool acts on the image.

### Light Properties

- Brightness: This governs how strongly whatever grading applied to the scene comes through. It introduces no brightness shifts by itself but magnifies the ones you dial in with the grading tools.
- Reach: This governs how steeply reflections fade as distance from the light source grows.
- Contrast: This sets how abrupt or gentle the gradient running between light and dark turns out.

### Surface Properties

- Glossiness: Lends reflective surfaces the impression of a metallic sheen.
- Specularity: Once any glossiness is present, this dictates how metallic/shiny that glossiness reads.
- Shadow Softness: Dictates how far the light reaches into shadows by way of ambient reflections, past where it would otherwise land.

Light Direction (Directional only)

- Azimuth/Elevation XY : Dictates the direction from which the light arrives.

Spotlight (Spotlight only)

- Beam Angle: Sets how wide the cone of light spreads. This control can also be handled graphically within the viewer.
- Edge Softness: Sets how soft the edges of the light cone/beam appear. Light Position (Point Source and Spotlight).

Light Position (Point and Spotlight only)

- These controls handle the position of the light emitter for the Point and Spotlight types. You can set them right here, though it’s usually easier to do so graphically by means of the Viewer controls.
