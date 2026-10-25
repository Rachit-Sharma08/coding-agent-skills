# Comments and editing individual tool controls from the inspector context menu

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing parameters in the inspector.
[Chapter index](INDEX.md) / [Previous section](inspector-node-selection-and-versioning.md) / [Next section](picking-colors-from-an-image.md)
<a id="source-a-matte-threshold-range-control"></a> <a id="source-button-arrays"></a> <a id="source-checkboxes"></a> <a id="source-checkboxes-used-to-select-options-for-tracking"></a> <a id="source-color-chooser-and-picker"></a> <a id="source-comments"></a> <a id="source-drop-down-menu-in-the-timespeed-node"></a> <a id="source-drop-down-menus"></a> <a id="source-editing-individual-tool-controls-from-the-inspector-context-menu"></a> <a id="source-fusion-slider-controls"></a> <a id="source-inspector-controls-explained"></a> <a id="source-range-controls"></a> <a id="source-the-color-chooser"></a> <a id="source-the-color-panel-with-transparency-preview"></a> <a id="source-the-fusion-edit-control-dialog"></a> <a id="source-thumbwheel"></a> <a id="source-windows-color-dialog"></a>

### Comments

Every node also has a Comments field, a lone text field for attaching comments and notes to that node. Just click inside the field to drop a cursor and start typing. Add a note and the comments icon turns up in the Control Header, visible in a node's tooltip when you hover the cursor over the node in the Node Editor. If you need it, the contents of the Comments tab can be animated across time. When the node is a Loader, extra controls show up under this tab. For the details, turn to Chapter 104, "Generator Nodes." In the DaVinci Resolve Reference Manual, or to Chapter 44 of the Fusion Reference Manual.

### Editing Individual Tool Controls From the Inspector Context Menu

Right-clicking inside the Inspector and choosing Edit Control summons the Control Editor, where you can tweak the parameters of that one specific tool within the node tree.

### The Fusion Edit Control Dialog

### Inspector Controls Explained

A handful of nodes rely on wholly bespoke interface elements found nowhere else, but most nodes draw on a blend of sliders, angle wheels, and checkboxes. Working with those controls is what this section explains.

### Fusion Slider Controls

You pick a single value out of a range with Slider Controls. Change that value either by dragging the slider or by typing a number into the edit box. So far this is ordinary slider behavior. There's more on offer, though, that can speed up the changes you make with sliders. Click the gutter on the handle's left or right side to raise or lower the value. Hold Command while clicking the gutter to nudge the values in finer steps. Hold Shift while clicking to step the value in coarser amounts.

Hold Command while clicking in the gutter to move in smaller increments

Slider controls run between a minimum and a maximum, yet typing an out-of-range number into the edit box will frequently stretch the slider's range to take in the new value. You can, for example, type 500 into a Blur Size control even though the Blur Size slider tops out at 100 by default. The slider widens its displayed maximum on its own so those bigger numbers can be entered. Once a slider differs from its default value, a tiny round marker appears beneath the gutter. Click that circle to send the slider back to its default.

### Thumbwheel

A Thumbwheel control behaves just like a slider apart from having no maximum or minimum. Adjust it by dragging its middle portion left or right, or by typing a value straight into the edit box. Angle parameters are the usual home for Thumbwheel controls, though they serve other purposes too.

Thumbwheel controls handling X, Y, and Z rotation, flanked by arrows at each end for precise tweaks With the thumbwheel selected, the Up and Down Arrows on your keyboard let you refine the values further. Just as with the slider control, the Command and Shift keys raise or lower how much the value shifts in finer or coarser steps. Once a thumbwheel differs from its default value, a tiny round marker appears above the thumbwheel. Click that circle to send the thumbwheel back to its default.

### Range Controls

The Range controls are really a pair of separate controls, one fixing the Low Range value and the other the High Range value. Drag the handle at either end of the Range bar to adjust the values. Drag from the middle of the Range bar to shift the high and low ends of the range together. You can also widen or narrow the range evenly by holding Command and dragging either end of the Range bar. Range controls turn up on parameters that call for both a high and a low threshold, such as the Matte Control, Chroma Keyer, and Ultra Keyer nodes. TIP: Floating-point numbers can go into the Range controls too, just key them into the Low and High numeric entry boxes.

### A Matte Threshold Range control

### Checkboxes used to select options for tracking

### Checkboxes

A checkbox is a control holding one of two states, On or Off. Clicking the checkbox control switches it from selected to not selected and back. You can animate a checkbox, where 0 stands for Off while 1.0 or anything above it stands for On.

### Drop-Down Menus

A drop-down menu serves to pick one option out of a menu. With the menu open, clicking an item selects that entry. Once the menu shuts, the Inspector shows the chosen selection. A drop-down menu's selection can be animated as well, where 0 stands for the list's first item, 1 for the second, and onward from there.

### Drop-down menu in the TimeSpeed node

### Button Arrays

A button array is a cluster of buttons letting you choose from a set of options. They behave almost exactly like drop-down menu controls, except a button array makes all of the choices visible together at once. Button arrays frequently rely on icons to make their options easier to grasp at a glance.

The Lens Type button array in the Defocus node

### Color Chooser and Picker

Wherever a parameter wants a color for its value, like the Fill or Outline color in the Text+ node, the Color panel appears. A swatch shows the chosen color with an Eyedropper beside it, and the Color Chooser sits below the swatch. The Color panel is remarkably versatile, offering four separate ways to pick and show colors.

### The Color panel with transparency preview

TIP: Pick the range you prefer in the Preferences > General panel and color is then expressed as 0–1, 0.255, or 0–65000. macOS and Windows Color Nodes A click on the color swatch summons the operating system's own Color Selection node. The layout differs a little on each operating system, but the overall concept holds. Pick a color from the swatches on offer, from the color wheel on macOS, or from the color palette on Windows. Whatever way you settle on a color, you have to click OK for it to take effect.

macOS Colors panel

### Windows Color dialog

### The Color Chooser

A built-in color chooser is also at your disposal, with areas for choosing grayscale values plus the hue you've currently picked across varying ranges of saturation and value. A hue bar, and an alpha bar on some nodes, let you settle on different values.
