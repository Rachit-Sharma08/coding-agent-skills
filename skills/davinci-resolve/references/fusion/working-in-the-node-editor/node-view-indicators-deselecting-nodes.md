# Node view indicators deselecting nodes

Version: DaVinci Resolve 20.3 Reference Manual. Context: Node view indicators.
[Chapter index](INDEX.md) / [Previous section](adding-replacing-and-selecting-nodes.md) / [Next section](node-view-indicators-drag-and-drop-nodes-into-a-viewer.md)
<a id="source-deselecting-nodes"></a> <a id="source-loading-nodes-into-viewers"></a> <a id="source-node-view-indicators"></a> <a id="source-viewed-nodes-when-you-first-open-fusion"></a> <a id="source-working-in-the-node-editor-part-2"></a>

### Deselecting Nodes

Deselecting nodes, when you need to, behaves about how you'd guess. Ways to deselect nodes:

- A single click on the Node Editor's background clears every selection.
- Pressing Command-Shift-A clears every selection.
- Command-click peels off selected nodes one at a time.
- A Command-drag bounding box clears a batch of selected nodes all at once.

### Loading Nodes into Viewers

Once a composition is underway, your next lesson is how to view the particular nodes you intend to work on. This matters because the pairing of which node you're viewing with which node is selected (and they aren't always one and the same) frequently decides which onscreen controls show up and what they look like. The example below has you rigged to rotoscope an image with a Polygon node hooked into the garbage mask input of a MatteControl node that's bringing the mask in as an alpha channel.

A node tree set up to handle a straightforward rotoscoping task.

The screenshot above shows why you'd send the upstream MediaIn or Loader node to a viewer while keeping the Polygon node selected for editing: it lets you see the whole image you're rotoscoping and still keep the Polygon node's spline on display.

### Viewed Nodes When You First Open Fusion

The first time you open the Fusion page in DaVinci Resolve, viewer 2 typically shows the output of the present empty composition (the MediaOut1 node). In Dual-viewer mode, viewer 1 stays blank until you hand a node to one of them. The first time you launch Fusion Studio with an empty comp, both viewers stay blank even after you've read in media through a Loader node. The viewers show content only once you assign a node to one of them. A handful of different methods exist for putting a node in a viewer, and which you pick comes down to your own working style.

### Node View Indicators

Sitting beneath every node, the View indicators do two jobs. For one, they act as a clickable means of pushing a node's output into one of the viewers. For another, they signal which nodes in the Node Editor are currently being viewed. By default you get two round indicators standing in for the two viewers. The left one maps to the left viewer and the right one to the right viewer, no matter whether both viewers are on screen or only one.

A viewer indicator switched on for the right viewer and off for the left one. To send a node to a viewer by way of the Node View indicators:

- A click on an indicator turns it white, signaling that node now sits in the matching viewer. Click once more and the indicator goes black, pulling the node out of the viewer. A node only shows its View indicators while it's being viewed. To bring the indicators up otherwise, hover the pointer over the node and they appear, ready to click.
- Keyboard shortcuts can toggle each View indicator as well. The two default viewers carry the numeric shortcuts 1 and 2. Press the matching number once to send the selected node to the right display, and press it again to clear that display.

With elaborate compositions you might find yourself opening extra viewers. As an illustration, you could devote one viewer to the finished comp's end result, hand a second viewer the source, point a third at a mask, and turn a fourth into a broadcast monitor wired through a Blackmagic DeckLink card or some other display hardware. The moment you go past two viewers, further View indicators get added, each tagged with a running number somewhere between 3 and 9.

As the viewer count climbs, it can get harder to recall which View indicator stands for which viewer. Park the pointer over the View indicator in question and a tooltip pops up naming the viewer it stands for.
