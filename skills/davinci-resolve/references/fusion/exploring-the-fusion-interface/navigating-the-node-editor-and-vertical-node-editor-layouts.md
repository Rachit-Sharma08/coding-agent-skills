# Navigating the node editor and vertical node editor layouts

Version: DaVinci Resolve 20.3 Reference Manual. Context: Exploring the Fusion interface.
[Chapter index](INDEX.md) / [Previous section](node-editor-and-adding-nodes-to-your-composition.md) / [Next section](keyframes-editor-control-summary-and-adjusting-clip-timings.md)
<a id="source-common-inspector-controls"></a> <a id="source-effects-library"></a> <a id="source-keeping-organized"></a> <a id="source-keyframes-editor"></a> <a id="source-navigating-the-node-editor"></a> <a id="source-nodes-with-several-tabs-worth-of-parameters"></a> <a id="source-parameter-header-controls"></a> <a id="source-parameter-tabs"></a> <a id="source-status-bar"></a> <a id="source-the-effects-library-with-tools-open"></a> <a id="source-the-inspector"></a> <a id="source-the-modifier-panel-showing-a-perturb-modifier"></a> <a id="source-the-templates-section-of-the-effects-library"></a> <a id="source-the-tools-and-modifiers-panels"></a> <a id="source-vertical-node-editor-layouts"></a>

### Navigating the Node Editor

As your Node tree grows, parts of it are bound to slip offscreen. Once a stretch of the node tree falls offscreen, a resizable Navigator pane shows up in the top-right corner. The Navigator is a scaled-down picture of the whole node tree that you can drag inside of to pan over to different parts of your composition in a hurry. You can resize the navigator with a handle down in the lower-left corner, and toggling the Navigator's visibility is done either by tapping the V key or by right-clicking the Node Editor and heading into the contextual menu's Options submenu.

The Navigator pane for accessing offscreen parameters or tools Other standard ways of panning and zooming about the Node Editor exist as well. Methods of navigating the Node Editor:

- Middle-click and drag to pan about the Node Editor.
- Hold Shift and Command down and drag the Node Editor to pan.
- Press the Middle and Left mouse buttons together and drag to resize the Node Editor.
- Hold the Command key down and spin your mouse's scroll control to resize the Node Editor.
- Right-click the Node Editor and pick an option from the Scale submenu of the

contextual menu.

- Press Command-1 to snap the Node Editor back to its default size.
- Drag two fingers across a track pad to pan.
- With the Command key held down, slide two fingers across a track pad to resize the Node Editor.

### Vertical Node Editor Layouts

Alternative Node View Layout presets found on the Fusion page let you stand the Node Editor up vertically, whether beside the Inspector or down the left edge of the screen. That can prove a real help while you're animating in the Spline Editor or Keyframes Editor. Once on the Fusion page, you can grab the layouts from Workspace > Layout Presets. Picking a vertical layout lets the node tree run top to bottom, opening up considerably more room down the screen's bottom portion where the Spline Editor or Keyframes Editor can live.

Here the Mid Flow Vertical layout preset is paired with the Vertical Flow direction setting. While you're on the vertical layouts, switching on the Flow > Build Direction > Vertical option in the Fusion settings makes every new Node tree build vertically, leaving the most possible room for Fusion's animation tools. You can then store alternative layouts built on these two vertical presets by way of the Workspace > Layout Presets submenu. Whenever you'd like to head back to the default horizontal Node Editor layout, just pick Workspace > Layout Presets > Fusion Presets > Default. These Layout options aren't on offer in Fusion Studio; even so, you can rely on the Floating Frame to place the Node Editor anywhere you please.

### Keeping Organized

While you work, keeping the node trees you build tidy matters a great deal toward a clear grasp of what's going on. Happily, the Fusion Node Editor hands you an assortment of methods and options to help with exactly that, sitting inside the Options and Arrange Tools submenus of the Node Editor contextual menu.

### Status Bar

Down in the lower-left corner of the Fusion window, the Status bar surfaces an assortment of current information about what you're selecting and what Fusion is up to. As an instance, hovering the pointer over a node shows details about that node in the Status bar. On top of that, the frame rate currently being hit appears the moment you kick off playback, and the share of the RAM cache in use stays on display at all times. Further information, updates, and warnings turn up in this area as you go. The Status bar beneath the Node Editor presenting details about whatever node sits under the pointer, alongside a popup box carrying still more pertinent info. Every so often the Status bar puts up a badge to tip you off that there's a message waiting in the console you might care about. That message could be a log, a script message, or an error. A notification that there's a message in the Console

### Effects Library

Fusion's Effects Library lays out every node and effect Fusion has on offer, third-party OFX plugins among them, if those are installed. When you're in DaVinci Resolve, Resolve FX turn up in the OFX category as well. Whereas the toolbar surfaces a good many of the most common nodes you'll reach for in any composite, the Effects Library holds every single tool Fusion offers, sorted by category, each node set to be dropped quickly into the Node Editor. Suffice it to say the Effects Library carries far, far more nodes than the toolbar does, covering a broad spread of purposes.

### The Effects Library with Tools open

### The Templates section of the Effects Library

The Effects Library's hierarchical category browser breaks into several sections according to whether you're in Fusion Studio or on the Fusion page within DaVinci Resolve. The Tools section sees the heaviest use, since it holds every node standing for an elemental image-processing operation in Fusion. Hover the pointer over a particular tool and a tool-tip explaining what it does appears at the bottom right of the DaVinci Resolve interface. The OpenFX section carries third-party plugins, and if you're on the Fusion page, it also carries ResolveFX, which ship with DaVinci Resolve. A third section, on view only while you're on the Fusion page in DaVinci Resolve, is the Templates section. An assortment of extra content fills that Template section: you'll find templates covering Lens Flares, Backgrounds, Generators, Particle Systems, plus Shaders, the latter meant for texturing 3D objects, along with yet more resources to draw on in your composites.

A button sitting at the far left of the UI toolbar switches the Effects Library's list between full height and half height.

### The Inspector

Over on the right side of the Fusion window sits the Inspector, a panel you use to show and work with the parameters of one or more selected nodes. Select a node in the Node Editor and its parameters and settings turn up in the Inspector.

The Inspector shows parameters from one or more selected nodes.

### The Modifier panel showing a Perturb modifier

### The Tools and Modifiers Panels

The Fusion Inspector splits into two panels. The Tools panel is the primary one, surfacing the parameters of selected nodes. The Modifiers panel shows optional add-ons to a tool's standard parameters. In the image below, a Perturb modifier has been attached to a parameter to lend that parameter random animation, and the controls in the Modifier panel let you tailor exactly what sort of randomness gets applied.

Other nodes put node-specific items here. For instance, Paint nodes present each brush stroke as its own set of controls in the Modifiers panel, on hand for further editing or animating.

### Parameter Header Controls

Sitting atop each node's controls in the Inspector, you'll find a cluster of controls.

### Common Inspector controls

Set Color: A pop-up menu letting you hand a node one of 16 colors, overriding the node's own color. Versions: Click Versions and another toolbar of six buttons appears. Each button can keep its own set of adjustments for that node, which you can use to bank several versions of an effect. Pin: The Inspector can also show, all at once, every parameter for the multiple nodes you've selected in the Node Editor. On top of that, sitting in the title bar of each node's parameters is a Pin button, which "pins" those parameters into the Inspector so they linger even once the node has been deselected—handy for key nodes you have to tweak while inspecting other nodes of your composition. Lock: Locks that node so nothing about it can be changed. Reset: Resets every parameter within that node.

### Parameter Tabs

A good many nodes lay out several tabs' worth of controls in the Inspector, shown as icons across the top of each node's parameter section. Click any tab to bring up that set of controls.

### Nodes with several tabs' worth of parameters

### Keyframes Editor

The Keyframes Editor presents every node in the current composition as a stack of layers inside a scaled-down timeline. The layer order barely matters, since it's the order and flow of connections in the node tree that drive the order of image-processing operations. The Keyframes Editor is what you reach for when trimming, extending, or sliding Loader, MediaIn, and effects nodes, or when fine-tuning keyframe timing—those keyframes sitting layered over each effect node until you open them out into their editable track.

Tuning the timing of clips, effects, and keyframes is the job of the Keyframes Editor.
