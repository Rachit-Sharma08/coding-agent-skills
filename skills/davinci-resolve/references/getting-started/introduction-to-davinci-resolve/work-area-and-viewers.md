# Work area and viewers

Version: DaVinci Resolve 20.3 Reference Manual. Context: Introduction to DaVinci resolve.
[Chapter index](INDEX.md) / [Previous section](effects-library-and-edit-index.md) / [Next section](node-editor-and-color-page-timeline.md)
<a id="source-effects-library"></a> <a id="source-gallery"></a> <a id="source-node-editor"></a> <a id="source-status-bar"></a> <a id="source-the-color-page"></a> <a id="source-the-color-page-1"></a> <a id="source-the-console"></a> <a id="source-the-console-window"></a> <a id="source-the-effects-library-with-tools-open"></a> <a id="source-the-work-area"></a> <a id="source-thumbnail-timeline"></a> <a id="source-toolbar-1"></a> <a id="source-viewer"></a> <a id="source-viewer-with-transport-controls"></a> <a id="source-viewers"></a>

### The Work Area

This term probably won't come up often, since you'll favor the names of the specific panels within it that you actually use, but the region labeled the Work Area is the portion at the lower half of the Fusion page UI where you can reveal the three principal panels for assembling compositions and editing animations on the Fusion page. Those panels are the Node Editor, plus the Spline Editor and the Keyframes Editor. Out of the box the Node Editor is what greets you first, and it's the chief area you'll operate in, but it can sit alongside the Spline Editor and Keyframes Editor when needed, and you can free up more horizontal space on screen for these three panels by setting the Effects Library and Inspector into half-height mode if necessary.

The Work Area with the Node Editor, Spline Editor, and Keyframes Editor visible

### Viewers

The Viewer Area takes in the Time Ruler along with the transport controls. The Time Ruler serves as the main “timeline” of the Fusion page, concentrating solely on the composition you're currently building, which might be one clip or many. You can configure this area to present either one viewer or two at the top of the Fusion page, the choice made through the Viewer button sitting at the far-right end of the Viewer title bar. A given viewer is able to present a single node's output drawn from any spot in the node tree. You decide which node lands in which viewer. That makes it simple to load different nodes into each viewer for side-by-side comparison. As an example, you might drop a Keyer node into the left Viewer and the finished composite into the right Viewer, letting you watch the image you're tuning and the final outcome together.

A pair of viewers lets you tweak an upstream node in one while watching how it changes the whole composition in the other Ordinarily, a viewer renders the 2D nodes of your composition as one flat image. When you're inspecting a 3D node, though, you get the option to switch that viewer into one of several 3D views, including a perspective view granting a repositionable stage on which to lay out the elements of the world you're constructing, or a quad view that shows your composition from four angles, making it simpler to position and edit objects and layers across the XYZ axes of the 3D space you're working in.

### Toolbar

Positioned just below the Time Ruler, the toolbar holds buttons that let you rapidly drop commonly used nodes into the Node Editor. Clicking any of them inserts that node after whichever node is currently selected in the node tree, or drops an unconnected copy of it when nothing is selected. Toolbar buttons for placing frequently used nodes into the Node Editor

Six sections divide the toolbar, grouping commonly used nodes together. As you move the pointer over a button, a tooltip reveals that node's name.

### Effects Library

On the Fusion page the Effects Library exposes every node and effect on offer there, encompassing the effects shipped with DaVinci Resolve along with third-party OFX where present. Whereas the toolbar surfaces many of the most frequent nodes you'll reach for in any composite, the Effects Library holds every single tool the Fusion page provides, sorted by category, with each node poised for quick insertion into the Node Editor. Put simply, the Effects Library offers far, far more nodes than the toolbar, covering an enormous range of purposes.

### The Effects Library with Tools open

### Node Editor

The Node Editor is the core of the Fusion page, since it's where you construct the tree of nodes forming each composition. Each node you tack onto the node tree contributes one specific operation that yields a single effect, whether that's softening the image with blur, shifting color, laying down paint strokes, drawing then attaching a mask, pulling a key, generating text, or merging a pair of images together.

The Node Editor presenting a node tree that builds a composition Inspector The Inspector sits as a panel on the right-hand side of the Fusion page, where you view and adjust the parameters belonging to one or several selected nodes. Selecting a node in the Node Editor brings that node's parameters and settings into the Inspector, ready for editing. Two panels make up the Fusion Inspector. The Tools panel surfaces the parameters of whatever nodes are selected. The Modifiers panel presents different content depending on the node. Across all nodes it surfaces the controls for Modifiers, which are adjustable expressions you've attached to particular parameters so they animate themselves in various ways.

The Inspector shows parameters from one or more selected nodes

Nodes with different tabs expand the Controls, Transform, and Settings parameters

On top of that, plenty of nodes present several tabs' worth of controls in the Inspector, appearing as icons across the top of each node's parameter section. Click any tab to bring up that group of controls.

### Thumbnail Timeline

Concealed by default, the Thumbnail timeline opens when you click the Clips button in the UI Toolbar, and it shows up beneath the Node Editor while it's open. The Thumbnail timeline displays every clip in the current Timeline, offering a means of moving from one clip to the next when handling several compositions in your project, and giving you an interface for building and switching between multiple versions of compositions and resetting the active composition whenever that's needed.

The Thumbnail timeline helps you move through the Timeline and handle composition versions Media Pool On the Fusion page, the Media Pool carries on in its role as the storehouse for every piece of media you've brought into your project. This makes it painless to pull extra clips into your compositions just by dragging whatever clip you want out of the Media Pool and into the Node Editor. The media you bring in shows up as a fresh MediaIn node within your composition, ready to be woven into your node tree however suits you.

The Media Pool in Thumbnail mode showing video clips

### Status Bar

Sitting at the foot of the Fusion page, directly above the Resolve Page bar, the status bar presents a range of current information about whatever you're selecting and whatever is going on in the Fusion page. To illustrate, hovering the pointer over any node surfaces details about that node in the status bar (and in a floating tooltip too), the frame rate currently being hit shows up whenever playback starts, and the share of the RAM cache in use stays visible at all times. Further information, updates, and warnings turn up in this region as you work.

The status bar below the Node Editor reporting details on the node beneath the pointer, alongside a floating tooltip

### The Console

Reachable through Workspace > Console, the console is a window where you can read the error, log, script, and input messages that may shed more light on whatever the Fusion page is attempting to do. It's likewise the place where you can review FusionScript outputs or type FusionScripts in directly. Now and then the status bar (covered above) will show a badge to signal there's a message in the console worth a look. That badge tells you whether the message is an error, log, or script message.

### The Console window

### The Color Page

The Color page is where you handle color correction, or grading, for your program. It carries every control for working with color and contrast, cutting noise, making limited secondary color corrections, crafting various image effects, tweaking clip geometry, and applying many other corrective and stylistic changes. Seven principal areas make up the Color page, and they cooperate to help you assemble a grade. For fuller detail on the Color page, refer to Chapter 126, “Using the Color Page.”

### The Color page

### Viewer

The Viewer presents the frame sitting at the playhead's current spot in the Timeline. Its contents are nearly always sent out to video through whatever I/O interface you've hooked up. A header runs across the top of the Viewer showing the Project and Timeline names, plus a Viewer Timecode display that by default reports each clip's source timecode. That Timeline name doubles as a drop-down that lets you jump to any other timeline in the project. Beneath the image, a jog bar (sometimes called a scrubber bar) lets you drag the playhead through the clip's full length, while transport controls below that govern playback. Across the top, a toolbar supplies controls for Image Wipes, Split-Screen, and Highlight display. Other controls let you switch audio playback on or off, or tune it by right-clicking the speaker icon and dragging the slider. You can also pick which onscreen controls are showing at the moment.

### Viewer with transport controls

You can additionally drop the Viewer into Cinema Viewer mode via Workspace > Viewer Mode > Cinema Viewer (Command-F) so it covers the whole screen. Issuing this command again toggles Cinema Viewer mode off. Two further modes, Enhanced Viewer (Option-F) and Full Screen Viewer (Shift-F), exist to grant more working room for chores such as window positioning and rotoscoping.

### Gallery

You use the Gallery to hold still frames that serve as reference when comparing one clip against another. Every still frame also keeps that clip's grade so you can reapply it down the line; stills and grades live together. A button opens the Album browser, which you use to arrange your stills. Across the top of the Gallery, Memories let you stash grade information you can call up through a control panel or keyboard shortcuts. You can also bring up a bigger Gallery window inside the Color page that affords more space for arranging your saved stills and grades. For more on the Gallery page, refer to Chapter 141, “Using the Gallery.”

The Gallery has Memories, stills saved in albums, and your PowerGrades
