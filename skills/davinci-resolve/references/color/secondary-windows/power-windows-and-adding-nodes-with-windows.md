# Power windows and adding nodes with windows

Version: DaVinci Resolve 20.3 Reference Manual. Context: Secondary windows.
[Chapter index](INDEX.md) / [Next section](window-transform-and-viewer-position.md)
<a id="source-adding-nodes-with-windows"></a> <a id="source-managing-windows"></a> <a id="source-power-windows"></a> <a id="source-secondary-windows"></a> <a id="source-secondary-windows-part-1"></a> <a id="source-serial-nodes-showing-the-window-on-node-2"></a> <a id="source-showing-and-hiding-onscreen-window-controls"></a> <a id="source-the-window-palette"></a> <a id="source-the-window-palette-interface"></a> <a id="source-the-window-palette-with-the-window-list"></a> <a id="source-using-the-high-visibility-power-window-outline-option"></a>

### Secondary Windows

A secondary correction means singling out one region of the frame, or one subject, by means of a key. Within DaVinci Resolve, keys are grayscale images: the white portions mark where your adjustment lands, while the black portions mark what stays untouched. You can produce a key through the Qualifier palette controls, through a Power Window, or by bringing in an external matte. If you'd like details on working with external mattes, refer to Chapter 146, “Combining Keys and Using Mattes.” The current chapter walks through building shapes with Power Windows so you can single out portions of the frame in various ways and apply these focused corrections.

### Power Windows

Another approach to secondary correction is the Power Window — at heart a shape that lets you single out areas of the frame. Separate controls give you oval, rectangular, polygonal, or freely drawn curved geometry. Since the isolation is done by drawing, Power Windows deliver remarkably tidy output, and their borders can be placed and feathered with precision for many different looks.

Before/after of a Curve Power Window singling out the sky for a focused correction. A Power Window (often just called a “window”) shines whenever the thing you're tweaking fits inside a well-bounded geometric region. Think of the oval covering someone's face, the front end of a car, or a broad stretch of sky — each is well suited to a windowed tweak. One downside is that windows generally have to be animated so they stay locked to whatever they're isolating. Happily, that's precisely where the robust tracker in DaVinci Resolve helps out, letting you track Power Windows swiftly and precisely so they keep pace with the subject being singled out.

Circular Power Window to focus attention to the skin Combining several Power Windows in assorted arrangements is straightforward in DaVinci Resolve, so they can overlap each other and yield still more elaborate shapes. As an illustration, you can sum several windows together, or carve one window out of another, which spares you from elaborate keyframing just to animate a window's outline.

Multiple windows combined to isolate and mask the image. The pages that follow address using Power Windows — building and editing them, plus how to merge several windows and how to pair windows with qualifiers for highly targeted isolations.

### Adding Nodes with Windows

Just like with qualifiers, the first step before windowing a correction is to drop a node into the node tree of your grade. The reason is that every window inside a given node operates jointly to confine that node's grade. Recall that a node can switch from a primary operation touching the whole frame into a tighter secondary operation merely by activating a window, applying a qualifier, or switching on an external matte.

### Serial nodes showing the window on Node 2

Skip adding a fresh node before you build a window, and you'll find you've mistakenly turned a primary correction into a secondary one. After making a new serial node, you'd reach for the controls inside the Window palette to switch on a window and tailor it however you like. That said, a handful of commands exist that drop in serial nodes with a window already active, sparing you a click or keystroke or two. To insert a fresh node with a window already active: for a serial node bearing a circular window, Choose Color > Nodes > Add Serial Node + CPW (Option-C). For one carrying a linear window, Choose Color > Nodes > Add Serial Node + LPW (Option-Q). To get a polygonal window on the new node, Choose Color > Nodes > Add Serial Node + PPW (Option-G). And for a Curve window, Choose Color > Nodes > Add Serial Node + PCW (Option-B). Whenever you add a node carrying a Power Window, the Window palette pops open on its own, ready for editing.

### The Window palette

There are three control groupings within the Window palette: the Window list, the Presets, and the Transform and Softness controls.

### The Window Palette Interface

After you've made a node to host a Power Window correction, you'll want to open the Window palette unless it's already up. To bring up the Window palette: Click the Window palette button. Most of the Window palette's real estate goes to the Window list, where you can build as many windows as the job calls for. Five distinct window types are available, and each carries its own geometry. They can be applied on their own, or merged together to build even more intricate shapes and interactions. Four clusters of controls in the Window palette let you put these windows to work in various ways.

### The Window palette with the Window list

- Window list: Across the top of this list sits a row of buttons for adding fresh windows, which you can then tailor as needed. Every window listed surfaces an On/Off button displaying the shape type, a Layer Name field (empty until you type something in) you can use to label each window's purpose, an Invert button, and a Mask button that controls how the window relates to the other currently active windows (by default it adds to them, while in Mask mode it carves out from them).
- Transform parameters: Governs the overall size, aspect ratio, placement, and rotation of whichever window is currently selected.
- Softness parameters: Governs the edge softness of whichever window is currently selected. The softness choices vary by window shape.
- Option drop-down menu: The Option drop-down menu holds commands for building and editing custom window presets you can recall later, for resetting windows, deleting windows, saving and organizing window presets, and copying and pasting track data.

Across the top of the Window palette, the buttons let you build five window types:

- Linear: A four-point shape you can reshape into whatever rectangle or trapezoid you require. Beyond the center and corner controls, dragging any of the four sides also reshapes it.
- Circular: An oval you can reshape, resize, and feather to handle a remarkable range of problems.
- Polygonal: A four-point shape that can grow extra control points to form intricate sharp-cornered polygons.
- Curve: A Bezier drawing tool for producing any shape you might need — curved, polygonal, or a blend.
- Gradient: A straightforward two-handled control that splits the screen into halves, with settings for the shape's center, angle, and feathering. Handy for quick sky tweaks.

### Managing Windows

Working on a window starts with making the type you want, or — when you already have a batch of windows built — picking the one you want to work on. Ways to create and pick windows:

- To create a new window: Click either the Shape icon button or the Create Window button (sitting at the top of the Window list) matching whichever window type you'd like to build.
- To pick a window via the onscreen controls: Click somewhere inside a window to select it in the Viewer.
- To pick a window out of the Window list: Click the Shape icon button matching the window you'd like to select.

To remove a window you've finished with:

- Select a window, then click the Delete button.

To reset a window:

- To return a single window to its default shape: Pick the window, then choose Reset Selected Window from the Option drop-down.

### Showing and Hiding Onscreen Window Controls

Opening the Window palette switches the Viewer into Power Window mode. Turning a window on brings that window's onscreen controls up inside the Viewer, and they're mirrored to video out so the window controls show on your external display too. You're free to adjust how and where those onscreen controls show up. To decide whether onscreen controls mirror to video out or get switched off, do either of these: Pick a setting from the Window Outline submenu found in the Viewer’s option menu. Three choices exist there. Off: removes the outline from the Viewer as well as the external display. On: the default, which keeps the outline visible in the Viewer and on the external display alike. Only UI: drops the outline from your external display while keeping it shown in the Viewer. Or press Option-H to cycle through all three modes listed above.

That command cycles three ways. Run it once and the window outline vanishes from your external display while staying in the Viewer. Run it a second time and the outline disappears from both the external display and the Viewer. Run it a third time and the outline returns to both the external display and the Viewer. TIP: When you keep the onscreen controls showing in the Viewer, you may at times want to briefly hide or reveal them so you get a clean view of the image you're working on. Any set of onscreen controls can be flipped off and back on without picking Off in the menu — just press Shift-` (tilde).

### Using the High-Visibility Power Window Outline Option

Normally, Power Window outlines render white (the center shape) and gray (the softness shapes). That palette can be hard to make out at times, though, so the Color panel of the User Preferences offers an option under General Settings labeled “High visibility Power Window outlines.” Switching it on makes Power Window outlines draw as green (the center shape) and yellow (the softness shapes), so these windows stand out better in certain situations. (Left) the default window outlines; (Right) the High Visibility outlines switched on via the Color panel of the User Preferences
