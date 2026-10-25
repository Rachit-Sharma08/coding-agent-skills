# Render nodes and relative paths

Version: DaVinci Resolve 20.3 Reference Manual. Context: Rendering using saver nodes.
[Chapter index](INDEX.md) / [Previous section](render-queue-removal-save-and-reload.md) / [Next section](render-several-frames-at-once-and-simultaneous-branching.md)
<a id="source-automatic-rejoining-of-the-queue"></a> <a id="source-disk-cache"></a> <a id="source-flipbook-previews"></a> <a id="source-frame-timeouts"></a> <a id="source-heartbeats"></a> <a id="source-installing-all-fonts-on-render-nodes"></a> <a id="source-installing-third-party-plugins-on-render-nodes"></a> <a id="source-managing-memory-use"></a> <a id="source-other-uses-of-network-rendering"></a> <a id="source-override-composition-settings"></a> <a id="source-relaunching-render-nodes-with-fusion-server"></a> <a id="source-render-nodes"></a> <a id="source-using-mapped-drives"></a> <a id="source-using-relative-paths"></a> <a id="source-when-renders-fail"></a>

### Render nodes

- Verify that each Render node carries any third-party OFX plugins the comp happens to use.

A few of these points are expanded on below.

### Using Relative Paths

The paths that load a composition along with its media, and that write out the composition’s rendered output, sit at the heart of how network rendering operates. Every machine taking part in network rendering has to reach the media location each Loader in the comp points to. Savers need configuring so they write into folders visible to all Render nodes and where all Render nodes hold write permission. The composition itself, too, has to live in a folder every Render node can reach, and you should add it to the queue list via a path that all Render nodes can see. Suppose, for instance, you open a composition sitting at c:\compositions\test1.comp within Fusion Studio and drop that composition into the network rendering queue; the Render Manager then signals each Render node to load and render it. The catch is that every machine probably has its own c:\drive lacking the comp you built. More often than not, the Render nodes can’t load the composition, so it fails. Path Maps, found in Fusion Preferences, are virtual paths that swap out portions of file paths. They let the absolute paths Loader and Saver nodes use become relative ones. Fusion ships with several Path Maps, yet you’re also free to define your own. The path you’ll lean on most is the Comp:\ path. Comp:\ stands in for the folder housing the saved composition. Consequently, putting Comp:\ in a Loader renders the media file’s path relative to wherever the comp file was saved. Provided all your source media lives within the same folder as your comp file, or a subfolder of it, Fusion finds the media no matter what the physical hard drive is called. What follows is a sample file structure that lets you work with relative file references. The composition resides at this file path: Volumes\Project\Shot0810\Fusion\Shot0810.comp And your source media lives here: Volumes\Project\Shot0810\Fusion\Greenscreen\0810Green_0000.exr The screenshot below illustrates this entire directory layout:

Relative paths can be derived from where the saved comp file sits. Here, applying the Comp:\ path anchors your media location to your comp file’s spot. So the relative path entered in the Loader node becomes: Comp:\Greenscreen\0810Green_0000.exr

Swapping the start of the Loader’s path for Comp:\ yields a path relative to the comp file’s location.

When your source media’s real file path sits in a subfolder alongside the comp file’s folder: Volumes\Project\Shot0810\Footage\Greenscreen\0810Green_0000.exr the Loader node’s relative path becomes: Comp:\..\Footage\Greenscreen\0810Green_0000.exr The pair of dots .. tells the path to climb up a single folder.

TIP: Certain Path Maps don’t configure themselves on a Fusion Render Node. For example, if your comp uses macros, you’ll have to add an entry for macros by hand.

### Using Mapped Drives

Setting the comp and media to relative paths only addresses part of the issue. Every machine taking part in the render must reach the drive holding the comp and source media. Mapping a drive grants lasting access to a folder living on another computer or a network storage device. Windows hands that folder a fresh drive letter, after which you use it exactly like any other drive attached to your computer. A mapped drive ties one alphabet letter to a shared network resource. The drive letters of your shared drives must match across all Render nodes. For instance, should your media sit on drive Z, the network drive has to show up as letter Z on each Render node. Under macOS, mapping a network drive is done through Connect to Server on the Go menu. Typing the drive’s smb:// path mounts it onto the computer. Via Accounts > LogIn Items, you can additionally arrange for the network drive to mount itself automatically following a reboot.

### Installing All Fonts on Render Nodes

Whatever fonts the composition’s Text tools rely on have to be reachable by every node taking part in the render. Otherwise the render breaks down on any Render node lacking that font.

### Installing Third-Party Plugins on Render Nodes

Every third-party plugin and tool a composition draws on has to be present in the plugins directory of each Render node. Any Render node that tries to render a composition relying on an uninstalled plugin will not render. Each Render node needs its licensed plugins in place.

### Other Uses of Network Rendering

Even though your main reason for configuring network rendering is likely to speed up the delivery of final renders, Fusion can put the network to work in other ways too. The Render nodes across your network can likewise hasten the building of Flipbook Previews and disk caching.

### Flipbook Previews

Fusion Studio can enlist Render nodes to speed up generating Flipbook Previews, delivering previews at blistering pace. When previews aren’t network rendered, their frames render straight into memory. Tick the Use Network checkbox plus the Render nodes so the preview frames render into the folder defined at Preferences Global > Path > Preview Renders. Every Render node joining the network render should be able to reach this folder. Its default value is Temp\, a virtual path aimed at the system’s default temp folder. You’ll have to alter this before network rendered previews can work. After the preview render wraps up, the frames each Render node produces are spooled into memory on the local workstation. The moment a frame lands in memory, it’s erased from disk.

### Disk Cache

When you right-click a node within the Node Editor and select Cache to Disk, a dialog appears for building the disk cache. Should you have ticked the Use Network checkbox and then press the Pre-Render button to send the disk cache, the networked Render nodes pitch in to speed up building that disk cache.

Beyond final renders, Render nodes serve for disk caching too.

### When Renders Fail

Render queues failing now and then is simply unavoidable. Common triggers include a flawed composition, a power outage, or a machine that gets unplugged from the network by accident. When nobody’s around to watch the render, the danger of a whole queue stalling idle for hours can turn into a real headache. Fusion Studio bundles in several safeguards meant to shield the queue and keep the render going through even the harshest circumstances.

### Automatic Rejoining of the Queue

Should a Render node drop off the Render Master’s radar for whatever reason, the frames it was handling get redistributed to the other Render nodes on the list. Once that Render node is back in service, it tells the Render Master it’s ready again, and fresh frames flow to it.

That’s precisely why configuring the Render Master within the Render nodes’ network preferences matters. Leave the master unset and a Render node has no idea which master to reach out to once it’s available again. Inside the Fusion Render Node Preferences, open the Tweaks panel. The Last Render Node Restart Timeout field lets you specify how many seconds Fusion holds on after the final Render node drops offline before it abandons the queue and pauses for hands-on intervention.

### Relaunching Render Nodes with Fusion Server

Fusion Server is a compact helper that ships alongside Fusion Studio and the Render node. The application is Fusion Server, a lightweight tool bundled with both Fusion Studio and the Render node. The application is brought up quietly by every Fusion Render node at startup. What Fusion Server does is keep an eye on the Render node to confirm it stays alive throughout a render. Its appetite for CPU cycles and RAM is tiny. Should the watched Render node vanish from the system’s process list without a clean shutdown signal — which can occur following a crash — Fusion Server fires the Render node back up so it can return to the render. Fusion Server picks up only the cases where a Render node has terminated abnormally. Where the Render node is still listed in the processes yet has gone unresponsive for some cause, Fusion Server has no way to spot the trouble. Stalled processes of that kind get caught and dealt with through frame timeouts, covered below.

### Frame Timeouts

Frame timeouts act as a safety net that halts a Render node’s render whenever a frame runs past the set duration (which defaults to 60 minutes, or one hour). This timeout guarantees an overnight render presses on if some composition stalls or starts swapping heavily and can’t finish the frame it was given. You set the timeout on a per-composition basis within the queue. To shift a composition’s timeout away from the 60-minute default, right-click that composition in the Render Manager’s queue list and pick Set Frame Timeout from the contextual menu.

Right-click a comp inside the Render Manager to define a timeout value. To adjust the frame timeout value, select Set Frame Time Out from the Render Manager’s Misc menu and type the number of seconds you’d like for the Time Out.

### Heartbeats

At steady intervals the Render Master pings each node with a heartbeat signal and waits for the node to answer. In essence, a heartbeat is the manager asking the Render node whether it remains responsive and in good shape. When a Render node misses several heartbeats back to back, Fusion concludes that node is gone. Its assigned frames then shift to the other Render nodes on the list. Both the count of consecutive missed heartbeats that triggers the manager to drop a Render node from the list, and the gap of time between heartbeats, are adjustable in the master’s Network Preferences panel. For roughly 90% of situations the defaults on these settings work fine. Where the rendered compositions tend to demand more memory than the machine physically holds, memory gets swapped out to disk. In that case raising these two settings a bit can be worthwhile, offsetting the laggy response until you can fit more RAM into the Render node.

### Managing Memory Use

Frequently a network is a mix of machines sporting all kinds of CPU and memory setups. Whatever memory settings the workstation that authored a composition used might not suit every Render node across the network. The Render node software lets you override the memory settings baked into the composition and substitute custom ones better matched to a given Render node’s system configuration. Reaching a node’s preferences is done by right-clicking its icon in the Windows Notification area, or on the macOS menu bar, and selecting Preferences. Within the Preferences dialog, open the Memory panel.

### Override Composition Settings

Switch this option on so the Render node’s own local settings drive the rendering of whatever compositions arrive. Turn it off to fall back on the default settings stored inside the composition.
