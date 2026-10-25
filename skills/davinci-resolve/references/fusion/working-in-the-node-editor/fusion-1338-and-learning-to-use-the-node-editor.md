# Fusion 1338 and learning to use the node editor

Version: DaVinci Resolve 20.3 Reference Manual. Context: Working in the node editor.
[Chapter index](INDEX.md) / [Next section](bookmarks-and-underlays-as-bookmarks.md)
<a id="source-automatic-node-editor-navigation"></a> <a id="source-fusion-1338"></a> <a id="source-learning-to-use-the-node-editor"></a> <a id="source-navigating-within-the-node-editor"></a> <a id="source-node-view-bookmarks"></a> <a id="source-using-the-node-navigator"></a> <a id="source-working-in-the-node-editor"></a> <a id="source-working-in-the-node-editor-part-1"></a>

### Working in the Node Editor

Across this chapter you'll learn the ins and outs of working in the Node Editor, covering the several approaches to adding, connecting, rearranging, and deleting nodes so you can build whatever effect comes to mind.

### FUSION 1338

### Learning to Use the Node Editor

Sitting at the center of Fusion's compositing interface is the Node Editor (which used to go by the Flow or Flow Editor). It relies on a flowchart-style layout known as a node tree, letting you assemble a composition from interlinked nodes rather than stacking layers in a layer list. Every clip you bring into the composition, plus every image-processing operation you run on those clips, shows up as a node, and connections wire them all together to carry image data from one node onward to the next. Any single node does a fairly modest job on its own, yet taken together they add up to remarkably intricate results.

The Node Editor. Here the chapter digs deeper into working in the Node Editor, walking you through adding, connecting, rearranging, and deleting nodes to produce whatever effect you dream up. To bring up the Node Editor:

- Click the Nodes button on the UI toolbar.

The Nodes button in the UI toolbar.

### Navigating within the Node Editor

Everything to do with nodes and the assembly of your composites unfolds in the Node Editor. The better you get at moving around inside it, the quicker your work will go. A handful of conventional ways exist to pan and zoom across the Node Editor, and many of them carry over from other Fusion panels. Ways to pan the Node Editor:

- Hold middle-click and drag to roam around the Node Editor.
- Keep Shift and Command pressed, then click and drag inside the Node Editor to pan.
- Use two fingers on a track pad and drag to pan across the Node Editor

Ways to zoom the Nod4e Editor:

- Push the Middle and Left buttons at once and drag to rescale the Node Editor.
- Keep the Command key held and spin your pointer's scroll control to rescale the Node Editor.
- Right-click the Node Editor and pick something from the contextual menu's Scale submenu.
- Hit Command-1 to send the Node Editor back to its default size.
- Keep the Command key held while dragging two fingers on a track pad to rescale the Node Editor.

### Automatic Node Editor Navigation

Whenever a node that's currently off-screen in the Node Editor gets selected, whether through the Find command or by clicking a node's header in the Inspector, the Node Editor pans on its own to bring that node into the visible area.

### Using the Node Navigator

One more handy way to move about the Node Editor is the Node Navigator. This is a little rectangular overview tucked into the Node Editor's upper-right corner. It offers a bird's-eye look at the whole composition, and an inner outline marks which slice of that composition the panel is currently showing. Reach for the Node Navigator when you've zoomed into a node tree and want to scan around the composition.

The Node Navigator.

To show or conceal the Node Navigator, take one of these actions:

- Right-click an empty stretch of the Node Editor, then pick Options > Show Navigator.
- Tap the V key.

To let the Node Navigator pop back up automatically as needed after you've dismissed it:

- Right-click an empty stretch of the Node Editor, then pick Options > Auto Navigator.

To resize the Node Navigator, do this:

- Drag its lower-left corner to make it bigger or smaller.

Drag the corner to resize the Navigator. To restore the default Node Navigator size, do this:

- Right-click any spot inside the Node Navigator and pick Reset Size.

To pan the Node Editor by way of the Node Navigator, do this:

- Drag inside the Node Navigator to travel between the different regions of your node tree.
- Inside the Navigator, drag two fingers on a track pad to travel between the different regions of your node tree.

### Node View Bookmarks

Bookmarks give you yet another route for getting around the Node Editor. Each bookmark stores the Node Editor's position and scale, letting you leap fast and exactly from one cluster of nodes to viewing a different one. To create a bookmark, follow these steps: 1 Pan and scale within the Node Editor until a cluster of nodes you care about is in view. 2 From the Options menu at the Node Editor's upper right, pick Add Bookmark, or hit Cmd-D. 3 When the Manage Bookmarks dialog opens, type a name for the bookmark and click the Add button.

Your first nine saved bookmarks each receive a keyboard shortcut and appear in the Options menu. The Go To Bookmarks dialog lists them too, alongside whatever bookmarks you've saved past that initial nine.

The Node Editor Options menu with nine bookmarks added

TIP: To put the Node Editor back at default scale, right-click within it and pick Scale > Default Scale, or press Cmd-1. Should your Node Tree shift and you need to revise Bookmark names or drop bookmarks, the Manage Bookmarks dialog is where you handle that. To rename or remove a bookmark, follow these steps: 1 From the Options menu at the Node Editor's upper right, pick Manage Bookmarks. 2 In the Manage Bookmarks dialog that appears, right-click the bookmark and pick Rename or Remove. 3 Click OK to dismiss the Manage Bookmarks dialog.
