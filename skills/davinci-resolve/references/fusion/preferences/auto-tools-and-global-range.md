# Auto tools and global range

Version: DaVinci Resolve 20.3 Reference Manual. Context: Preferences.
[Chapter index](INDEX.md) / [Previous section](user-interface-and-view.md) / [Next section](settings-and-color-depth.md)
<a id="source-auto-tools"></a> <a id="source-default-format"></a> <a id="source-flow-1"></a> <a id="source-force"></a> <a id="source-frame-format-1"></a> <a id="source-global-range"></a> <a id="source-group-opacity"></a> <a id="source-link-grab-distance"></a> <a id="source-options"></a> <a id="source-pipe-grab-distance"></a> <a id="source-the-flow-preferences"></a> <a id="source-the-frame-format-preferences"></a> <a id="source-time-code"></a>

### Auto Tools

The Auto Tools section decides which tools get added automatically for the most common Background tool operations and Merge operations.

- Background: When set to None, a standard Background tool is used; the drop-down menu, however, lets you pick from an assortment of tools, including 2D and 3D tools, to shape the operation to your workflow.
- Merge: When set to None, nothing occurs. When set to Merge, joining the outputs of two tools or dragging several clips onto the Node Editor uses a standard Merge. Other valid choices here are Anaglyph, Channel Booleans, and Dissolve.
- Use Merge Only When Connecting Outputs Directly: With this option active, Merges are not added automatically when you drag several clips from the Finder or Windows Explorer onto the Flow area.

### Global Range

Through the Start and End fields, you define the Global Start and End frames applied when new compositions are created.

### Time Code

You use this option to decide whether new compositions default to showing SMPTE Time Code or frames (Feet + Frames) for representing time.

### Flow

A good number of the options living in the Node Editor’s contextual menu — among them the settings for Tile Picture, the Navigator, and Pipe Style — are gathered in this category.

### The Flow preferences

### Force

The Force section can set the default so that certain tool tiles in the Node Editor display pictures rather than plain tiles. The Active checkbox turns pictures on for the actively selected tool, the All checkbox enables pictures for every tile, and the Source and Mask checkbox enables tile pictures only for Source and Mask tools.

When All is enabled, the picture shown is either a thumbnail of the image the tool rendered if the tool has rendered, or — when the Show Thumbnails option is off — the tool’s default icon. Concatenated transforms also show a default icon.

- Show Modes/Options: Switching this on places icons on the tool tile that depict various states, like Disk Caching or Locked.
- Show Thumbnails: With this checkbox ticked, tool tiles set to show tile pictures display the rendered output of the tool. With the checkbox cleared, the tool’s default icon is used instead.

### Options

The Options section gathers several settings that control or assist the layout and alignment of tools in the Node Editor.

- Arrange to Grid: This switches on a new node tree’s Snap to Grid option so the tool layout lines up with the grid marks in the flow.
- Arrange to Connected: A tool snaps onto the vertical or horizontal position held by whichever other tools it links with.
- Auto Arrange: This option lets the Node Editor shift tool positions as needed to clear space when inserting new tools or auto-merging layers.
- Show Grid: This switches the Node Editor’s background grid display on or off.
- Auto Remove Routers: Pipe Routers, or “elbow nodes,” in the Node Editor count as

“orphaned” once the tools wired to either their input or output are deleted. With this option on, Orphaned Routers are deleted automatically.

- Pipes Always Visible: When on, the lines linking one tool to another are rendered on top of the tool tiles themselves.
- Keep Tile Picture Aspect: Switching this on forces tool tile thumbnail pictures to hold the aspect of the original image in the thumbnail.
- Full Tile Render Indicators: Ticking this checkbox makes the whole tile change color while it is processing. That can make it easier to spot which tools are processing in a large composition. The coloring itself acts as a progress bar, signaling how near slower tools are to finishing.
- Show Instance Links: This option picks whether Instance tools show links, drawn as green lines, between Instance tools.
- Navigator: The Navigator is a small square overview of the whole composition. It lets you jump quickly to different parts of a node tree while zoomed in. The checkboxes in this section decide when, if ever, the Navigator appears.

On: The Navigator stays visible at all times. Off: The Navigator stays hidden at all times. Auto: The Navigator appears only when the Node Editor’s contents spill beyond the currently visible Work area.

- Pipe Style: This drop-down menu picks the method used to draw connections between tools. The Direct method runs a straight line between tools, while Orthogonal uses horizontal and vertical lines.
- Build Direction: While auto-building or laying out a node tree, Build Direction decides whether tools are arranged horizontally or vertically.
- Scale: The Scale menu lets you pick the default zoom level of the Node Editor whenever a new composition is created.

### Pipe Grab Distance

The Pipe Grab Distance slider lets you choose how near the pointer must come (in pixels) to a connection line in the node tree to select it.

### Link Grab Distance

The Link Grab Distance slider lets you choose how near the pointer must come (in pixels) before a node’s knot makes or breaks a connection. At 0 pixels you must land right on the knot, whereas a top setting of 20 lets you sit 20 pixels away from a knot and still connect to it.

### Group Opacity

This slider governs the opacity of an expanded group’s background in the Node Editor.

### Frame Format

The Frame Format preferences let you pick the resolution and frame rate for the nodes that generate images, such as Background, fast noise, and Text+. On top of that they fix the color bit depth applied to final renders, to previews, and to interactive updates shown in the viewer. Those color bit depth choices take effect in Fusion Studio alone. Rendering in DaVinci Resolve always uses 32-bit float.

### The Frame Format preferences

### Default Format

This drop-down menu lets you pick the default resolution for Generator tools from a list of presets. It is only a default, and a node’s Inspector can override it by way of its Resolution settings. Any of the default settings is changed through the Edit boxes. To make a new setting, press the New button, enter a name in the dialog box that appears, and enter the parameters.
