# Keyframe spreadsheet and editing keyframes in the spreadsheet

Version: DaVinci Resolve 20.3 Reference Manual. Context: Animating in Fusion s keyframes editor.
[Chapter index](INDEX.md) / [Previous section](keyframe-editor-framing-controls-and-segments-in-the-timeline.md) / [Next section](markers-and-a-marker-being-moved-in-the-keyframed-editor.md)
<a id="source-choosing-a-timeline-filter"></a> <a id="source-duplicating-spline-keyframes"></a> <a id="source-editing-keyframes-in-the-spreadsheet-1"></a> <a id="source-selected-filtering"></a> <a id="source-show-values-from-the-keyframes-editor-option-menu"></a> <a id="source-showing-keyframe-values"></a> <a id="source-sorting-in-the-timeline"></a> <a id="source-the-keyframe-spreadsheet"></a> <a id="source-the-keyframes-editor-tree-item-order-selection-menu"></a> <a id="source-the-sort-menu"></a> <a id="source-the-timeline-sort-order-menu"></a> <a id="source-the-tree-item-order-menu"></a> <a id="source-time-stretching-keyframes"></a> <a id="source-time-stretching-keyframes-1"></a> <a id="source-timeline-filters"></a>

### The Keyframe Spreadsheet

Switch on the Spreadsheet, then click a layer’s name in the keyframe track, and each keyframe’s numeric time position and value (or values, for a multi-dimensional parameter) turn up as entries within the Spreadsheet cells. One keyframe occupies each column, while one facet of each keyframe occupies each row.

### Editing keyframes in the Spreadsheet

As an example, while you animate a blur, the Key Frame row reports the frame on which each keyframe sits, and the Blur1BlurSize row reports the blur size at each keyframe. Alter the Key Frame value of any keyframe and you shift that keyframe onto a different frame of the Timeline.

### Duplicating Spline Keyframes

Keyframes can be copied, whether onto the very same keyframe track or onto other tracks. That can spare you time when you need to repeat a keyframe sequence elsewhere on the same segment, or simply to set up keyframes with matching timing on two separate segments. Here is how to duplicate keyframes: 1 Pick the keyframe or keyframes you want copied. 2 With Command held down, drag any one of those selected keyframes over to a new position.

### Time Stretching Keyframes

Select a range of keyframes within a keyframe track and you can switch on the Time Stretch tool at the lower left of the Keyframes Editor, which brings up a box for squeezing and stretching the whole range of keyframes against one another — reshaping the overall timing of a keyframe sequence while holding onto the relative spacing from one keyframe to the next. As an alternative, switch on Time Stretch and draw a bounding box around the keyframes you intend to adjust to set up a time-stretching boundary that way. Click the Time Stretch tool once more to switch it off.

### Time stretching keyframes

### Showing Keyframe Values

When a node and the segment that goes with it carry animated parameters, keyframes show up as colored tick marks in keyframe tracks to flag where animated changes happen. With the tracks and splines open on a parameter, picking Show Values from the Keyframes Editor Option menu surfaces editable fields under each keyframe. Those fields display each keyframe’s present value and let you edit it simply by typing a new number.

### Show values from the Keyframes Editor Option menu

### Timeline Filters

As a composition swells to hundreds of nodes, pinning down particular node layers can soon turn awkward. You can build and apply Timeline filters to weed out nodes that the current operation does not need. The Global Timeline preferences ship with a handful of ready-made filters you can switch on, or you can fashion new ones whenever you like. To use a Timeline filter: Open the Keyframes Editor Option menu and pick an item from the menu’s top. Default Timeline filters include;

- Show All, which reveals every node layer in the current composition.
- Show None, which conceals all layers.
- Show Tools at Current Time, which only shows node layers sitting under the playhead.
- Any custom filters you have built turn up here too, in alphabetical order.

To return to displaying it all: From the Keyframes Editor Option menu pick Show All, and every layer comes back into view.

### Choosing a Timeline filter

To build a Timeline filter: 1 From the Keyframes Editor Option menu, pick Create/Edit Filters; this opens the Timeline panel within the Fusion Settings window. That panel is where new Timeline filters get made.

The Global Timeline preferences for enabling filters 2 Press the New button, give your new filter setting a name, and press OK. Up at the top, the filter you just made now sits selected in the Filter pop-up menu. 3 Through the “Settings for filters” list, tick the checkboxes for nodes you want visible and untick the checkboxes for nodes you want screened out. Whole categories of node can be switched on and off, or you can open a category’s disclosure control to flip individual nodes on and off. A press of Invert All instantly switches off every node category. 4 Once your filters are done, press the Save button to dismiss the Fusion Settings window. Whatever filters you have made inside the Timeline panel of the Fusion Settings window then show up in the Keyframes Editor Option menu.

To remove a filter: 1 From the Keyframes Editor Option menu, pick Create/Edit Filters; this opens the Timeline panel within the Fusion Settings window. That panel is where Timeline filters get deleted. 2 Out of the Filter pop-up menu, pick the filter you want gone. 3 Press the Delete button, and once a dialog checks whether you truly mean it, press OK.

### Selected Filtering

Picking “Show only selected tools” from the Keyframes Editor Option menu screens out every segment apart from the layers matching the selected nodes. You can switch this option on or off. TIP: With “Show only selected tools” turned on, you can go on selecting nodes in the Node Editor to refresh what the Keyframes Editor shows.

### Sorting in the Timeline

The top-to-bottom order in which nodes appear in the Timeline is yours to change.

- The Tree Item Order Selection menu lets you order the tracks by a number you assign.
- The Sort pop-up menu is another option.

### The Tree Item Order Menu

Right-clicking over any track in the Keyframes Editor brings up a contextual menu carrying the Tree Item Order Selection submenu. Picking Start from the submenu lets you begin numbering each item in the track header by clicking on them. Your first click marks an item #1, your second #2, your third #3, and onward. After every item has been clicked in the sequence you want for the Keyframes Editor, give a track a right-click and, out of the Tree Item Order Selection submenu, pick End. The items then line up by the numbers you assigned, with #1 riding above #2, which rides above #3, and so on. The very first items in the Keyframe track list will always be the nodes forming the root of the node tree. After those root nodes, the numbered nodes follow in order. As an example, if the node tree opens with a background node and then runs into a Fast Noise, Blur, and Color Corrector, the background node will always sit at the top of the Keyframes Editor track list, since it is the root node.

### The Keyframes Editor Tree Item Order Selection menu

Should you start numbering nodes in the track header and then reconsider or settle on a different order, you can pick Restart to begin the numbering afresh or pick Cancel to keep the current order.

### The Sort Menu

The Sort menu rearranges how each node’s layers show up in the Keyframes Editor. Returning the menu to All Tools lays them out in linear order, sweeping the Node Editor left to right and top to bottom. This is the default setting.

### The Timeline Sort Order menu

- All Tools: Compels every tool presently sitting in the Node Editor to show up within the Keyframes Editor.
- Hierarchy: Orders things with the most background layers up at the header’s top, running down to the most foreground layers at the bottom, tracing the node connections in the Node Editor.
- Reverse: The flip side of Hierarchy, working back from the final node in the Node Editor toward the most background source node.
- Names: Orders the nodes alphabetically, opening at the top with the start of the alphabet.
- Start: Arranges layers by where they begin in the composition. Nodes beginning earlier in the Global project time sit at the header’s top, while nodes beginning later fall to the bottom.
- Animated: Holds the Timeline to animated layers alone. This mode shines when you are tuning the timing of animations across several nodes at once.
