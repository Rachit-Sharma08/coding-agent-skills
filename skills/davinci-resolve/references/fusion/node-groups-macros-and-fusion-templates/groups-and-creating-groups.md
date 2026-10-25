# Groups and creating groups

Version: DaVinci Resolve 20.3 Reference Manual. Context: Node groups macros and Fusion templates.
[Chapter index](INDEX.md) / [Next section](fusion-title-template-creation.md)
<a id="source-creating-groups"></a> <a id="source-creating-macros"></a> <a id="source-deleting-groups"></a> <a id="source-expanding-and-collapsing-groups"></a> <a id="source-groups"></a> <a id="source-groups-can-be-accessed-like-macros"></a> <a id="source-macros"></a> <a id="source-node-groups-macros-and-fusion-templates"></a> <a id="source-node-groups-macros-and-fusion-templates-part-1"></a> <a id="source-other-macro-examples"></a> <a id="source-panning-and-scaling-within-open-group-windows"></a> <a id="source-re-editing-macros"></a> <a id="source-saving-and-reusing-groups"></a> <a id="source-ungrouping-nodes"></a> <a id="source-using-macros"></a>

### Node Groups, Macros, and Fusion Templates

What this chapter shows is how groups, macros, and templates work in Fusion, so that handling complex effects turns out tidier, faster, and less of a chore.

### Groups

As you tackle complex visual effects, node trees have a way of growing sprawling and hard to handle, so bundling tools together helps you keep all the nodes and connections in better order. A group is a container within your node tree able to hold several nodes, much the way a folder on your Desktop holds several files. No cap exists on how many nodes one group may contain, and you can even build subgroups inside a group.

### Creating Groups

Making a group amounts to little more than picking the nodes you wish to bundle and running the Group command. To create a group: 1 Highlight whichever nodes you intend to bundle. 2 Give one of the chosen nodes a right-click and pick Group off the contextual menu (Command-G).

A handful of nodes highlighted ahead of building a group (top), alongside the group that results (bottom). The chosen nodes fold down into a group, which appears as one single node within the Node Editor. Depending on how the nodes inside it connect, the Group node may carry inputs and outputs. Only for nodes already wired to nodes outside the group does the Group node surface inputs. An unconnected input inside the group shows no Input knot on the Group node.

### Deleting Groups

Removing a group works just like removing any other node in the Node Editor. Pick a group and hit Delete, Backspace, or Forward-Delete, and that group, along with every node held inside it, drops out of the node tree.

### Expanding and Collapsing Groups

In the node tree, a collapsed group appears as one single “stack” node. Should you wish to alter any node held inside the group, open the group with a double-click, or by picking the group node and hitting Command-E.

An open group window showing the minimize button. Opening a group brings up a floating window that shows the nodes inside it. That floating window is a Node Editor in its own right, one you can resize, zoom, and pan apart from the main Node Editor. Inside the group window you can pick and tweak whatever node you want, and even add, insert, and remove nodes while it stays open. Once you’re set to collapse the group once more, hit the minimize button up in the floating window’s top left corner, or reach for the keyboard shortcut (Cmd-E).

### Panning and Scaling within Open Group Windows

The same mouse buttons that pan and scale the main Node Editor also pan and scale an open group window. That said, while you work inside an expanded group and are at the same time altering the main node tree, you might wish to keep the expanded group from being panned or scaled on its own. Switching off the Position button over at the right of the group title bar pins the group nodes to the size of the nodes throughout the rest of the overall node tree. Switching this Position button on lets you scale group nodes apart from the rest of the node tree.

### Ungrouping Nodes

Should you conclude a given group is no longer needed, or you just find constant access to all its nodes at once more convenient, you can break apart or “ungroup” the group without losing the nodes inside it, doing away with the group while its contents stay put in the Node Editor. To ungroup nodes, proceed thus: 1 Give the group a right-click. 2 Off the contextual menu, pick Ungroup. Whatever nodes were inside the group return to the main node tree.

### Saving and Reusing Groups

Among the strongest points of groups is that any group, settings and all, can be stored for reuse later in other shots or projects. There are several ways to bring groups and their settings back. One good case for wanting to Save and Load a group is a studio staffing two or more compositing artists. The lead artist at your studio might assemble the master comp and build a group made specifically for keying greenscreen. That key group can then be handed off to another artist, who tightens the key, constructs the mattes, and tidies up the clips. The setting can then be exported and reloaded into the master comp. As newer versions land, these settings can be reloaded to refresh the master comp. Ways to store and reuse groups run as follows: To save a group: On a group, right-click and choose Settings > Save As off the contextual menu. To reuse a group: Pull it straight out of your computer’s file browser and into the Node Editor. Doing so spawns a fresh group node in the node tree carrying every node the group you saved held. To load the settings from a saved group to another group built on the same nodes: On a group within the Node Editor, right-click and choose Settings > Load off the contextual menu. Within Fusion Studio, groups can also be stored and reused by way of the Bins window: To save a group: Drag the group out of the Node Editor and into the opened Bin window. A dialog comes up so you can name the group setting file and pick where on disk it gets stored. The .setting file lands at the location you named and goes into the bins, ready for quick access down the road.

### Macros

Certain effects come together not from a single tool but from a whole chain of operations, at times across complex branches whose parameter controls interlink. Fusion hands you a wealth of individual effects nodes to work with, yet also lets users re-bundle them in assorted combinations as self‑contained “bundles,” which are either macros or groups. Such “bundles” bring a few benefits:

- They reduce visual clutter in your node tree.
- They keep user interaction on track by letting you limit which controls drawn from each node of

the macro are available to the user.

- They lift productivity by letting artists swiftly tap ready-made answers to everyday compositing

challenges and creative adjustments that have already been built and saved. Although macros and groups serve much the same function, they part ways a little in how each is made and shown to the user. You can regard a group as a fast means of tidying a composition by trimming the visual complexity of a node tree. A macro, by contrast, takes longer to build owing to how customizable it is, yet it’s simpler to reuse across other comps.

### Creating Macros

Even though macros let you bank complex functions for reuse in highly customized ways, building one is honestly fairly straightforward. To make a macro from nodes in the Node Editor: 1 Pick the nodes you intend to fold into the macro you’re building. Since the macro you’re building serves a particular purpose, the nodes you pick ought to be wired together so they yield a specific output out of a specific set of inputs. TIP: Should you wish to govern the sequence in which each node’s controls turn up in the macro you’re building, Command-click each node in the sequence you want it to appear. 2 Give one of the chosen nodes a right-click and pick Macro > Create Macro off the contextual menu. A Macro Editor window comes up, listing each node you picked, ordered by the sequence in which each node was picked.

The macro editor with a Blur node and Color Corrector node.

3 To begin, type a name for the macro into the field up at the top of the Macro Editor. Keep this name brief yet telling of what the macro is for. Spaces aren’t permitted, and you’d do well to steer clear of special characters. 4 After that, open the disclosure control to the left of every node whose controls you wish to expose to the user, and, for each node output, node input, and node control you intend to expose, tick its checkbox over on the right. Whatever controls you tick get exposed to users following the sequence they hold in this list, which shows why governing the sequence in which you pick nodes back in Step 1, ahead of editing your macro, pays off. On top of that, the inputs and outputs already wired in your node tree come pre-ticked, so if you’re happy with those serving as the inputs and outputs of the macro you’re building, that bit is handled for you. For every control checkbox you switch on, a row of fields to the left of that control’s line lets you set the default value of that control plus the minimum and maximum values it will allow to start. 5 Having settled on your controls, click Close. 6 Click Yes when a dialog prompts you to store the macro. 7 Up comes a Save Macro As dialog in which you can revise the Macro Name (if need be) and pick a location for your macro. To make a macro show up in the Fusion page Effects Library Tools > Macros category, store it in these locations: On macOS: `Macintosh HD/Users/username/Library/Application Support/Blackmagic Design/ DaVinci Resolve/Fusion/Macros/` On Windows: `C:\Users\username\AppData\Roaming\Blackmagic Design\DaVinci Resolve\ Support\Fusion\Macros` On Linux: `home/username/.local/share/DaVinciResolve/Fusion/Macros` To make a macro surface within the Fusion Studio Effects Library Tools > Macros category instead, store it at these spots: On macOS: `Macintosh HD/Users/username/Library/Application Support/Blackmagic Design/ Fusion/Macros/` On Windows: `C:\Users\username\AppData\Roaming\Blackmagic Design\Fusion\Macros` On Linux: `home/username/.fusion/BlackmagicDesign/Fusion/Macros` 8 Once you’re finished, click Save.

### Using Macros

A macro can be brought into a node tree by way of the Add Tool > Macros or Replace Tool > Macros submenus on the Node Editor contextual menu.

### Re-Editing Macros

To rework a macro that already exists, simply right-click anywhere inside the Node Editor and pick the macro you wish to edit off the Macro submenu of that same contextual menu. Up comes the Macro Editor, where you can apply your changes and store the outcome.

### Groups Can Be Accessed Like Macros

A group can likewise be loaded off the Insert Tool > Macros submenu provided you store a group’s setting file in the Macros folder somewhere on your file system. As an example, on macOS, the `Macintosh HD/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/ Macros/` directory.

### Other Macro Examples

A macro can serve as a custom LUT too. Simply copy the macro’s .setting file into the LUTs: folder, and the macro becomes pickable as a LUT within the viewers. Such LUT macros stretch well past a mere color tweak; you could build a macro handling YUV 4:2:2 resampling, or a resize, or a sharpening filter, or even plain watermarking.
