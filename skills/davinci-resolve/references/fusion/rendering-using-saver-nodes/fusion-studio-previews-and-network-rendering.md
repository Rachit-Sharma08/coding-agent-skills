# Rendering previews and setting up network rendering in Fusion studio

Version: DaVinci Resolve 20.3 Reference Manual. Context: Rendering using saver nodes.
[Chapter index](INDEX.md) / [Previous section](rendering-overview-and-rendering-in-the-fusion-page.md) / [Next section](manually-adding-render-nodes-and-removing-render-nodes.md)
<a id="source-configuring-the-render-master-and-render-nodes"></a> <a id="source-licensing-for-network-rendering"></a> <a id="source-multi-license-dongles"></a> <a id="source-preparing-render-nodes"></a> <a id="source-preparing-the-render-master"></a> <a id="source-rendering-previews"></a> <a id="source-scanning-for-render-nodes"></a> <a id="source-setting-up-a-license-server"></a> <a id="source-setting-up-a-license-server-with-environment-variables"></a> <a id="source-setting-up-network-rendering-in-fusion-studio"></a> <a id="source-setting-up-the-render-manager"></a>

### Rendering Previews

Flipbook previews can be rendered straight into a viewer. Such Flipbook previews reside wholly in RAM. To make one, right-click a node in the Node Editor and, from the drop-down menu, follow Create > Play/Preview on > Left viewer/Right viewer. Up comes the Render Settings dialog, where you set up the preview and start the render. Another route is to Option-drag a node right out of the Node Editor into a viewer; the Render Settings dialog shows up and the preview lands on whichever viewer you aimed for. For fuller detail on rendering RAM previews, the DaVinci Resolve Reference Manual handles it in Chapter 69, “Using Viewers.” and the Fusion Reference Manual handles it in Chapter 7.

TIP: Option-Shift-dragging a node into a viewer bypasses the Render dialog and reuses your previous settings.

### Setting Up Network Rendering in Fusion Studio

Fusion Studio can parcel out an assortment of rendering tasks to any number of networked computers, letting several machines pitch in on network-rendered previews, disk caches, and final renders. Through the Render Settings dialog or the built-in Render Manager, you can hand compositions off to other Fusion Studio copies, and likewise to a Fusion Render node or several. You can also drive rendering from the command line to tie in with third-party render managers such as Deadline, Rush, and Smedge. Render nodes are machines lacking the full Fusion application but carrying the Fusion Render node software. That software isn't laid down by default when you install Fusion Studio, yet you can add it whenever you like through the Fusion Render node Installer. Look for that installer bundled inside the Blackmagic Fusion Studio installer.dmg (on macOS) and, for Linux and Windows, inside the Blackmagic Fusion Studio.zip. Since Fusion Studio is licensed for an unlimited number of Render nodes, you can put the Render node software on however many macOS, Windows, and Linux machines you'd like pitching in on a network render. To install a Render node: 1 Download the Blackmagic Fusion Studio archive, unzip it, then track down the Render Node Installer. 2 Copy the Install Fusion Render Node [version] onto every networked computer you want carrying out rendering operations. 3 Install the Render node. Out of the box, the Render node application lands in the Start Menu on Windows under Blackmagic Design. On macOS it joins the menu bar, and on Linux it shows up in the app launcher. The Render node application fires up on its own each time you log in to the computer. To stop it from launching automatically, pick Quit at the Render node icon over in the macOS menu. Under Linux, right-click the icon and pick Kill Process; under Windows, delete the shortcut from the Windows Startup directory.

### Licensing for Network Rendering

Most editions of Fusion Studio get their license by plugging a single-seat hardware key (dongle) into the very computer where Fusion is installed. Every dongle carries an unlimited supply of cross-platform Render node licenses, which you may install on as many macOS, Windows, and Linux machines as you require. So that Fusion Studio can reach the Render nodes, the machine holding the Fusion Studio dongle must sit on the same local network subnet as those Render nodes. This network licensing needs no individual license files; the Render nodes hunt down the dongle on the subnet by themselves, which keeps setup simple. Single-seat dongles won't “float” across a network — they have to stay plugged into the same machine running Fusion Studio.

### Multi-License Dongles

With a multi-license dongle, plugging it into any machine on the same subnet licenses 10 copies of Fusion Studio. Because these licenses “float” across a network, Fusion Studio needn't run on the very machine holding the dongle. So long as Fusion Studio shares the subnet, it locates the license server on its own and checks out a free license.

You can stack multi-seat dongles together to dial in the number of Fusion seats at a larger facility. Three dongles each licensed for 10 Fusion Studios, for instance, would deliver 30 licenses. It also buys you redundancy: in that same example, three machines can serve as license servers, and should the first server go down for any reason, Fusion Studio falls through to the next one automatically. As another option, you can plug several dongles into one computer.

### Setting Up a License Server

Getting the license ready for network rendering starts by plugging either a single-seat or multi-seat dongle into a machine that will host the license server. The Render node installer lays down Fusion Server to act as that license server, though the Render node itself needn't run on the same machine. Fusion Server is configured to launch at startup and sit quietly in the background as a service/daemon, standing by to dish out licenses and Fusion bins. Because Fusion Server is what hands out the various licenses, it has to be running any time you want to run Fusion Studio or use the Render nodes for network rendering. By default it starts on its own and keeps running for as long as another machine holds a license or a Render node is working. With nothing drawing on it, Fusion Server shuts down after 30 seconds. You'll need your network administrator to write firewall rules that let the Fusion Server, FusionScript, and the Fusion Render node applications talk to and verify licensing with the machine carrying the Fusion Studio dongle. Should you pull a dongle or should the network cut out for any reason, the licenses on every connected Fusion Studio application drop as well. The moment it loses its license, Fusion Studio sets off looking for another one, whether locally or on a different machine. Turn up no license and Fusion halts rendering, presenting a dialog that lets you retry the search or autosave the comp and quit. Render nodes only look for a network license once, at startup, so removing the dongle or hitting network trouble leaves them unaffected.

### Setting Up a License Server with Environment Variables

Environment variables give you a route to declaring flexible or “variable” configuration options. While network rendering in Fusion, they help when you need to set a location for a moment or single out a preference file. Through the FUSION*LICENSE_SERVER environment variable, you can point to different locations for the File Server. Rather than searching one place for the Fusion Server, you can list several license servers split by semicolons. Take, for example, fu:SetPrefs("Global.EnvironmentVars.FUSION_LICENSE* SERVER", "192.168.1.12; 192.168.10.55;_") The environment variable also lets you sweep a subnet for license servers—as in, “bobs-mac.local;10.0.0.23;_;license.mystudio.com”. An asterisk (_) thrown in calls for a broadcast search of the local subnet. As with most environment variables, the license server can be lodged in the Global Preferences by editing the Prefs text file. EnvironmentVars: `fu:SetPrefs("Global.EnvironmentVars. FUSION_LICENSE_SERVER", "10.0.0.23;_")` `fu:SavePrefs()`, and for more on wielding environment variables, the DaVinci Resolve Reference Manual devotes Chapter 75, “Preferences,” to it while the Fusion Reference Manual devotes Chapter 15. NOTE: Those straight quotes (" ") shown in the environment variables above are deliberate and must not be swapped for typographer's, or curly, quotes (“ ”).

### Configuring the Render Master and Render nodes

Machines taking part in network rendering fall into two roles.

- The Render Master keeps the list of compositions awaiting render (the queue) and parcels out frames to the Render nodes for rendering. Picture the Render Master as the traffic cop of the whole operation.
- The Render nodes are the workhorse machines that carry out the rendering. Every machine in a network render has to share one network subnet, and each must be able to reach the various files (Fonts and third-party plugins among them) that built the composite. That file path has to read the same on every machine taking part in the render.

### Preparing the Render Master

The Render Master holds the queue of compositions awaiting render and doles out frames to the Render nodes. On top of that, it keeps the Render node list current and pushes updates out to the various Render nodes whenever the need arises. At least one machine in the render farm has to be configured as the Render Master, and any copy of Fusion can fill that role once you've set up the Fusion Network Preferences.

The Network panel is where machines get designated as Render Masters. Taking on the Render Master role barely dents render performance, since the system resources it draws are negligible. Even so, a few particular steps stand between you and turning one of your machines into a Render Master.

Here's how you configure the Render Master: 1 Put a copy of Fusion Studio onto whichever machine you've earmarked as the Render Master. 2 From within Fusion Studio, on macOS pick Fusion Studio > Preferences, while on Windows and Linux pick File > Preferences 3 Inside the Preferences dialog, head to the Global > Network Preferences panel. 4 Type the Render Master's name into the Name field and enter the IP address. 5 Tick the Make This Machine a Render Master checkbox. 6 Want this machine pulling its weight in the render farm too? Then also tick the checkbox labeled Allow This Machine to Be Used as a Render Node. To have the Render Node act as the Render Manager:

- Highlight a node within the Render Manager, then from its contextual menu choose Set Default Master. After a machine is cleared to act as the master, lean on the Render Manager to add the Render nodes it will oversee. A thorough rundown of the Render Manager dialog comes later in this chapter.

### Preparing Render Nodes

Before any network render can start, the Render nodes have to be set up to take orders from the Render Master. Fusion Studio gives you two ways to clear a machine for use as a Render node:

- Pick File > Allow Network Renders.
- Over in the Global > Network Preferences, switch on the option named Allow This Machine to Be Used as a Network Render Node.

On a macOS Render Node computer:

- Click the Render Node icon in the menu bar and pick Allow Network Renders.

Reaching the Render Node menu by way of the macOS menu bar When you're on a Linux Render Node computer:

- Inside the App Launcher, right-click the Fusion Render Node icon, then pick Allow Network Renders.

On a Windows Render Node computer:

- Within the taskbar Notification area, right-click the Fusion Render Node icon, then pick Allow Network Renders.

### Setting Up the Render Manager

You watch rendering progress through the Render Manager window. It also lets you reorder, add, or drop compositions from a queue and tend the list of Render nodes doing the rendering. To bring up the Render Manager window in Fusion Studio, pick File > Render Manager.

The Render Manager is where you reorder, add, and drop compositions in a render queue. The Render Master always heads the Render Node list down the right side as the first machine. That lets the Render Manager render local queues without touching the network. For the Render Master to drive extra Render nodes, those nodes have to join the Render Node list. Right-click in the Render Node list to add Render nodes by typing a Render node's name or IP address. You can also pick Scan and have the Render Manager hunt for Render nodes across the local network.

The Render Manager is where you add Render nodes.

### Scanning for Render Nodes

While the Render Manager is open, you can launch a scan for Render nodes: right-click inside the Render Manager's Render Node list, then pick Scan for Render Nodes from the drop-down menu. The scan combs every IP address on the network subnet to see whether other machines on the local network are actively answering on the port Fusion reserves for network rendering. For the scan to spot a remote machine, a copy of the Fusion Render node has to be running there.
