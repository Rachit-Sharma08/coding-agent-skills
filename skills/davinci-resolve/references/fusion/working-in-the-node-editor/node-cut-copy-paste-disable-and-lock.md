# Cut copy and paste in the node editor node modes including disable and lock

Version: DaVinci Resolve 20.3 Reference Manual. Context: Cut copy and paste in the node editor.
[Chapter index](INDEX.md) / [Previous section](node-cut-copy-paste-and-icon-only-display.md) / [Cut, Copy, and Paste in the Node Editor](node-view-indicators-and-clipboard.md)
<a id="source-node-editor-options"></a> <a id="source-node-modes-including-disable-and-lock"></a> <a id="source-node-tooltips-and-the-status-bar"></a>

### Node Modes Including Disable and Lock

When you right-click one or more nodes and bring up the contextual menu, the Modes submenu surfaces a set of commands, several of them with keyboard shortcuts attached, for governing control visibility and for disabling, locking, updating, and caching nodes.

- Show Controls: Determines whether the node exposes its parameters in the Inspector once selected and whether its onscreen controls turn up in viewers. On by default.
- Pass Through: (Command-P) Works just like the toggle switch in the Inspector that flips nodes off and on. A disabled node is skipped, with image data handed straight from the upstream node before it to the downstream node after it. On by default.
- Locked: (Command-L) Works just like the Inspector's lock button, which blocks a node from being edited in the Inspector. Off by default.
- Update: (Command-U) On by default. As long as this option stays on, every change you make to the node triggers a re-render. With Update switched off, you can still tweak the node's parameters, yet those tweaks won't process or refresh the image until Update is switched back on. While it's off, the node's last processed image stays put as a freeze frame. This proves handy, for instance, with a big or processor-heavy composition (say a particularly demanding particle system), where turning the option off for a while lets you rattle off several quick parameter changes across different nodes without waiting out a full node-tree re-render after each one. It's also useful when you want to glance at how animated downstream nodes behave while stopping upstream nodes that are too processor-heavy to play in real time from rendering more frames.
- Force Cache: With this on, the node's output for the current frame carries an extremely high cache priority, all but pinning it in memory. Off by default.

Flipping any of these node modes on or off puts a badge inside that node to signal its state.

### Node Editor Options

A right-click on a blank stretch of the Node Editor opens the contextual menu along with the Options submenu. Inside the Options submenu sit several choices for tailoring how the Node Editor looks and acts.

- Pipes Always Visible: Switching this on makes a connection pass over the top of a node rather than under it, which can make the connection's route easier to trace.
- Show Hidden Pipes: With this on, the Inspector's Hide Incoming Connections option on every node is overridden so that all connections show up in the Node Editor.
- Aspect Correct Tile Pictures: Aspect Correct Tile Pictures makes the thumbnail display render with aspect correction; it's slower but truer to the eye. This option is on by default.
- Full Tile Render Indicators: Turn this on and the thumbnail flashes green during rendering, which helps you spot which node is processing within a big, intricate node tree.
- Show Grid: This option lets you switch the Node Editor's background grid on or off.
- Show Instance Links: With this on, the Node Editor renders a green connection running between an

instanced node and its parent.

- Auto Remove Routers: Whenever routers get disconnected from a tool, they're deleted on their own

out of the Node Editor. This option ships on by default so you don't have to clear out orphaned routers yourself.

- Show Navigator: Switch this on to show a compact overview window of the whole node tree up in the Node Editor's top-right corner. The Navigator section later in this chapter covers it more fully.
- Auto Navigator: The Navigator surfaces only when at least one node lies beyond the visible portion of the Node Editor. Refer to this chapter's Navigator section for further detail.
- Build Flow Vertically/Horizontally: A node tree can grow either horizontally from left to right or vertically from top to bottom. Turning on one of these options sets whether fresh nodes attach below the current node or to the right of the current tool.
- Orthogonal/Direct Pipes: This pair of options lets you set how the links joining nodes get rendered — either as Direct (straight) lines or as Orthogonal (bent) lines.

### Node Tooltips and the Status Bar

Even with a straightforward node tree, some key fact about the nodes in your comp slips your mind easily. To jog your memory about what each one does, hover the pointer over any node in the Node Editor and the Status bar along the bottom of the Node Editor will show that node's name, frame size, pixel aspect, resolution, and color depth.

The Status bar located beneath the Node Editor. Wait a couple more moments and a richer rendition of that same information shows up inside a floating tooltip in the Inspector. That tooltip hands you extra detail concerning the Domain (Image and DoD) and the data range the clip uses.

The floating tooltip showing node information that appears within the Node Editor.
