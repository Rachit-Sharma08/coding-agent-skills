# Manually adding render nodes and removing render nodes

Version: DaVinci Resolve 20.3 Reference Manual. Context: Rendering using saver nodes.
[Chapter index](INDEX.md) / [Previous section](fusion-studio-previews-and-network-rendering.md) / [Next section](render-queue-removal-save-and-reload.md)
<a id="source-loading-and-saving-render-node-lists"></a> <a id="source-manually-adding-render-nodes"></a> <a id="source-removing-render-nodes"></a> <a id="source-rendering-using-saver-nodes-part-2"></a> <a id="source-submitting-comps-to-network-render"></a> <a id="source-using-the-render-manager-window-for-network-rendering"></a> <a id="source-using-the-render-settings-dialog-for-network-rendering"></a>

### Manually Adding Render Nodes

To add a Render node to the Render Node list by hand, right-click in the Render Manager's Render Node list and pick Add Render Node from the drop-down menu.

The Add Render Node dialog lets you type a Render Node name or IP address by hand to find it on the subnet. In the Add Render Node dialog that appears, type the remote Render node's name or its IP address. The Render Manager will try, on its own, to turn names into IP addresses and IP addresses into names. This approach lets you list Render nodes even while they aren't currently reachable on the network.

### Removing Render Nodes

To drop a machine from the Render Node list, right-click the Render Node within the Render Node list and pick Remove Render Node(s) from the pop-up menu. Hold Command on macOS or Ctrl on Windows and Linux to pick several Render nodes for removal at once.

### Loading and Saving Render Node Lists

When you quit the Render Manager, your Render node list is saved automatically into the Documents > Blackmagic Design > Fusion > Queue folder. To store and bring back alternative Render node lists, the menu offers Render Node > Save Render Node List together with its counterpart Load Render Node list.

### Submitting Comps to Network Render

Sending a comp off to render on the network can go by way of three avenues: the Render Manager, the Render Settings dialog, or some third-party render farm application. Speed favors the first of those dialogs, whereas richer feedback and tighter control over the process come from the Render Manager and from third-party render farm applications.

### Using the Render Settings Dialog for Network Rendering

As you launch a preview or a final render, ticking the Use network checkbox in the Render Settings dialog and submitting the job tacks a composition onto the tail of the current queue in the Render Manager. Which Render Master gets used follows the Fusion preferences of the workstation that submitted the comp.

The Use Network checkbox turns on network rendering from the Render Settings dialog.

NOTE: Distributed network rendering handles image sequences such as EXR, TIFF, and DPX. It won't work for Quicktime, H264, ProRes, or MXF files.

### Using the Render Manager Window for Network Rendering

The Render Manager runs a render queue that lets you batch render comps. Compositions render in whatever order they sit in the Render Manager — the top entry first, then the one beneath it, and onward. Several comps in a queue can render at the same time, depending on which group of Render nodes they draw on and on the priority each comp carries. Here's how a comp joins the queue within the Render Manager:

- Press the Add Comp button, then browse to where the comp lives on your local disk.
- Within the queue list, right-click and pick Add Comp from the drop-down menu; afterward, browse to the comp on your local disk.
- From an OS window, drag a comp file directly onto the Render Manager’s queue list.

Pressing the Add Comp button inside the Render Manager places a comp into the queue so it can be batch rendered across the network.
