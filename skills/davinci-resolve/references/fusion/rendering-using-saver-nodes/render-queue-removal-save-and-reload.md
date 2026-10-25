# Removing a composition from the queue and saving and reloading queue lists

Version: DaVinci Resolve 20.3 Reference Manual. Context: Rendering using saver nodes.
[Chapter index](INDEX.md) / [Previous section](manually-adding-render-nodes-and-removing-render-nodes.md) / [Next section](render-nodes-and-relative-paths.md)
<a id="source-command-line-rendering"></a> <a id="source-preparing-compositions-for-network-rendering"></a> <a id="source-removing-a-composition-from-the-queue"></a> <a id="source-reordering-the-queue-lists"></a> <a id="source-saving-and-reloading-queue-lists"></a> <a id="source-using-third-party-render-managers-with-fusion-studio"></a> <a id="source-viewing-the-render-log"></a> <a id="source-working-with-node-groups"></a>

### Removing a Composition from the Queue

To take a composition out of the queue, highlight it in the queue list and tap the Backspace/Delete key; alternatively, right-click the comp within the queue list and pick Remove Composition from the drop-down menu.

### Saving and Reloading Queue Lists

Preserving a queue list so you can revisit it later is often handy. Your active queue list lives in the Documents > Blackmagic Design > Fusion > Queue folder. If you want to store the active queue under a different name, pick File > Save Queue As from the Render Manager menu bar. Bringing back a stored queue is done by choosing File > Load Queue and browsing to where it was kept.

### Reordering the Queue Lists

While a job is underway, which composition needs to finish first can shift. When deadlines move around, a composition sitting lower in the queue might have to be rendered ahead of others. Relocating comps within the queue is as simple as dragging them around the queue list. Should a composition whose status reads Done be dragged further down, it won’t render again. Forcing a comp to render once more is done by right-clicking it in the queue and selecting Clear Completed frames from the drop-down menu.

### Working with Node Groups

You can organize Render nodes into Groups, which then come into play whenever you submit compositions. Picture, for instance, a setup with five Render nodes. Every one of those Render nodes belongs to the group named All. Because two of them have extra memory and quicker processors, you spin up a fresh group titled Hi-Performance. Any new Render nodes join All on their own, though you’re free to place them in additional groups too. To assign a Render node to a Group: 1 Launch the Render Manager, then highlight whichever Render nodes you’re placing in a group. 2 Pick Render Node > Assign Group, or right-click the chosen Render nodes and select Assign Group via the drop-down menu. 3 Within the Choose Group dialog, type a name for that group. 4 Should you want Render nodes in several groups, divide each group’s name with a comma (e.g., All, Local, or Hi-Performance). Priority follows the sequence in which the groups are listed. See “Using Multiple Groups” below. Whenever a render goes out to the network, it lands in the All group by default. You may, though, opt to direct it toward other groups shown in the list. Routing a comp into a group by way of the Render Manager goes like this: 1 Bring up the Render Manager. 2 Send in the comp. 3 Press the Pause Render button. 4 Right-click the comp within the queue list, then choose Assign Group. 5 Inside the Assign Group dialog, pick an existing group for rendering the comp and press OK. 6 Press the Resume Render button.

Sending a comp into a group by way of the Render Settings dialog works as follows: 1 Press the Render button over in the transport controls area. 2 Within the Render Settings dialog, tick the Use Network checkbox. 3 From the Available groups list, pick an existing group. 4 Press the Start Render button. Returning to the earlier example, the All group holds five Render nodes, and two of them additionally belong to the Hi-Performance group. Dispatch a render to the HiPerformance group and just those two networked computers do the work. Should a composition afterward go to the All group, the other three machines kick off rendering that new composition. As soon as the pair of Render nodes in the Hi_Performance group finish that first task, they pitch in on the render already running for the All group. Using groups is entirely optional. That said, they can streamline and add efficiency to the administration of sizable networks of Render nodes. Using Multiple Node Groups One Render node may belong to several groups at once. Likewise, a single composition can be sent to more than one group. Routing a composition to several groups causes it to render on every Render node within the chosen groups. Where a Render node sits in multiple groups, the sequence of those groups matters, since that sequence sets the priority that Render node observes. As an example, when a Render node’s groups are ordered All, Hi-Performance, then renders sent to the All group win priority. Anything already rendering that came from the Hi-Performance group gets superseded. Flip the order to Hi-Performance, All and the priority swaps the other way.

### Viewing the Render Log

You’ll find the Render Log shown across the bottom portion of the Render Manager window, though it can equally appear in the console window. What the log records is the activity of the Render Manager: which frame went to which Render node, which Render nodes pulled in the queued compositions, and per-render statistics once each finishes. To view the Render Log in the console:

- Open the Render Manager and choose Misc > Show Render Log.

The Render Log offers two settings: a Verbose mode and a Brief mode. Under Verbose mode every Render Manager event is recorded, whereas Brief mode notes only the frame assignments per Render node along with their completion times. To disable Verbose mode:

- Choose Misc > Verbose Logging from the Render Manager’s menu bar.

### Using Third-Party Render Managers with Fusion Studio

Network rendering can be driven by third-party render manager software if you prefer. Doing so lets the many programs competing for your machine’s resources share them efficiently. Products in this category include Uberware LLC’s Smedge, Seriss’s Rush, plus GetRender’s Deadline. As a rule, these render managers rely on a command line renderer. Out of the box, Fusion’s Render nodes run as a service tied to the Fusion internal Render Manager. You can, however, launch the Render nodes from the command line so third-party render managers can drive them. Bear in mind that adopting a third-party render manager rules out certain Fusion network rendering capabilities, like generating network rendered Flipbook Previews and disk caches.

### Command Line Rendering

When a studio relies on third-party render farm managers such as Deadline, Smedge, or Rush, the Fusion Render node accepts invocation from the command line together with arguments and file paths. The Windows sample below invokes a Render node to open a composition named exampleV001 and produce 10 frames: //pathtoRN/FusionRenderNode.exe //pathtoProject/exampleV001.comp -render -start 101 -end 110 -quit That command launches, renders the span from 101 through 110, then exits. Further command line options appear in the table that follows.

Command "Fusion Server -i" "Fusion Server -S" (capital S) <filename.comp> -render -frames &lt;frameset&gt; -start &lt;frame&gt; -end &lt;frame&gt; -step &lt;step&gt; -quit -join &lt;host&gt; -listen

Description Sets up the license server as a service or daemon and starts it at boot ahead of any user login. Keeps the Fusion Server alive continuously in the background until it is force-quit. The comp name together with its full path, for example /storage/project/episode/shot/filename.comp. Instructs the Render Node to perform a render. Hands over a set of frame ranges for rendering—e.g., 101..110,120,121,130..150. Defines the render’s first frame. Defines the render’s final frame. Defaulting to 1, step skips frames during rendering. As an example, 2 renders every other frame Makes the Render Node exit once the render finishes. Directs the node to reach a manager at <hostname,IP> and (re)join whatever renders are in progress. Keeps the node alive, awaiting requests arriving from a manager.

Command -log &lt;filename&gt; -cleanlog -verbose -quiet -version -pri high|above|normal|below|idle -args &lt;arg1&gt; [, &lt;arg2&gt; ...]

Description Has the Render Node write render details out to a log file. The text is appended onto whatever the log file already holds. Wipes the current contents of a log file. Writes fuller detail into the log file. Hides pop-ups and interface buttons so nothing requires interaction. Reports the Render Node version number. Assigns the node’s process priority among high, above, normal, below, or idle. Lets you stash custom values retrievable through the script function GetArgs(), which hands back a table of { &lt;arg1&gt;, &lt;arg2&gt;, ... }

TIP: Running a headless Linux command line interface depends on having an X11 virtual frame buffer in place.

### Preparing Compositions for Network Rendering

How you assemble a composition inside Fusion Studio can either smooth or obstruct network rendering. The footage you load, the location of installed plugins, and the assortment of operating systems across your networked machines each influence how cleanly the network render proceeds. Before network rendering can function, your environment has to satisfy a handful of must-have conditions:

- The License dongle, the Render Master, and every Render node have to share one local network (subnet).
- Fusion Server must be running as a background service on the same

computer where the dongle is installed.

- Every piece of source media belonging to the comp ought to sit on a network volume.
- That network volume has to be mounted on every Render node.
- Loaders need to reference the media residing on the mounted volumes.
- Savers have to output to a drive mounted on every Render node.
- Save the Fusion comp onto a volume that is mounted across every Render node.
- Both Render Nodes and Render Masters require read plus write permission for any volume named as a

source media location or render destination.

- Confirm that every font the comp’s Text+ and 3D text nodes draw on is present across all the
