# Introduction to collaborative workflow and collaborative render cache support

Version: DaVinci Resolve 20.3 Reference Manual. Context: Collaborative workflow.
[Chapter index](INDEX.md) / [Next section](collaboration-bin-and-timeline-locking.md)
<a id="source-collaborative-marker-flag-and-clip-color-support"></a> <a id="source-collaborative-render-cache-support"></a> <a id="source-collaborative-support-for-hdr"></a> <a id="source-collaborative-support-for-individual-monitoring"></a> <a id="source-collaborative-support-for-lut-and-colorspace-context-options"></a> <a id="source-collaborative-workflow"></a> <a id="source-collaborative-workflow-part-1"></a> <a id="source-customizing-your-collaborator-identification"></a> <a id="source-enabling-multiple-user-collaboration"></a> <a id="source-introduction-to-collaborative-workflow"></a> <a id="source-opening-projects-to-collaborate"></a> <a id="source-read-only-mode"></a> <a id="source-requirements-for-collaboration"></a>

### Collaborative Workflow

When several people open one shared project, the multi-user collaborative workflow relies on “bin locking” to govern who is permitted to touch which items. Beyond that, this mode lets a group of artists edit, composite, grade, and enter metadata on clips belonging to a shared timeline, all inside one project where Collaboration has been switched on. A timeline inside a given project can be reached by many people at once for concurrent editing, compositing, and grading, and meanwhile assistants and other editors may open separate bins holding separate timelines in that same project to handle editorial tasks and media management. The pages that follow explain how several DaVinci Resolve workstations are configured to cooperate, and how bin locking lets them work as a team.

### Introduction to Collaborative Workflow

Within one project that has collaboration switched on, the multi-user collaborative workflow lets a number of people handle editing, compositing, grading, and Media Pool clip organization at the same time. There are three distinct shapes this collaboration can take:

- Through bin locking, several editors are able to edit separate timelines housed in separate bins of one shared project at once, and assistant editors can rearrange clips and revise the metadata living in the project’s other bins. A bin locks itself the moment a given user selects it and releases when that same user clicks away, though you can also force a bin into a locked or unlocked state by hand whenever the situation calls for it.
- Through clip locking, a group of colorists and compositing artists are free to share one timeline — whether on the Color page or the Fusion page — without worrying that they’ll clobber each other’s changes. Selecting a clip to work on locks it automatically, and choosing a different clip releases it (checking the work in as it goes). Because the Fusion page keeps its clip locks apart from those on the Color page, a colorist and a compositing artist are able to share a single shot.
- A trio consisting of one editor, one compositing artist, and one colorist can all share the same clip on the same Timeline within the same project without clashing.

By and large, using DaVinci Resolve in Collaborative Workflow mode feels no different from running it in noncollaborative mode. That said, a handful of collaboration-specific features deserve a mention.

### Collaborative Render Cache Support

The render cache format settings are matched automatically on every machine so that all collaborators on a project share identical ones. When your collaboration spans different operating systems (Mac, Windows, Linux), take care that the Render Cache Format points at a codec every one of those platforms can handle.

### Collaborative Support for Individual Monitoring

Should the need arise, any collaborator on a project may override that project’s output and monitoring settings just on their own workstation. Once a project is switched to Collaborative Workflow, a “Use Local Overrides” checkbox shows up within the Video Monitoring group of the Project Settings, giving you control over how monitoring happens at your own workstation.

### Collaborative Marker, Flag, and Clip Color Support

From the Color page, collaborative workflow lets you change markers, flags, clip metadata, and clip color. On top of that, FrameIO comment markers also work under collaborative workflow.

### Read Only Mode

Collaborative projects can be opened by users in Read Only Mode.

### Collaborative Support for HDR

As of DaVinci Resolve 16, collaborative workflows gained support for Dolby Vision and HDR10+.

### Collaborative Support for LUT and Colorspace Context Options

In multi-user projects you’re able to tweak LUTs and Colorspace settings straight from nodes — just right-click a node and pick the choice you’re after from the context menu, the same way you would in a single user project.

### Requirements for Collaboration

To make use of collaborative workflow:

- Every user has to be on a project saved either to the Blackmagic Cloud or to a correctly set up remote project library server. That remote project library server may live on one of the DaVinci Resolve workstations already in use, or on some other machine on your network whose only job is hosting the shared projects — but it ought to sit on a computer that never sleeps or powers down, so that projects don’t abruptly go missing.
- Every machine joining a collaborative workflow has to be networked together. A shared local area network (LAN) is fine, yet you’re equally able to link computers sitting on separate subnets.
- For the best results, shared projects ought to keep their media on a fast storage area network (SAN) of some kind, with each collaborator hooked into that SAN so every workstation tied to the collaborated project reaches the very same media directly. Shared volumes across a network can do the job when you’re stuck, though a proper SAN delivers a real performance boost. Sites running a mix of computer platforms (macOS, Windows, and Linux) side by side can lean on the Mapped Mount option in the Media Storage Locations list — located in the DaVinci Resolve System Preferences — to ease cross platform drive connections.
- As another option, every workstation can reach the same cloud storage folder over the internet, provided the correct Path Mapping has been arranged in the Project Settings.

To learn more about standing up a project library server, refer to Chapter 196, “Managing Project Libraries and Project Servers.”

### Enabling Multiple User Collaboration

Before the collaboration toolset can be used, a project must have Multiple User collaboration mode turned on. To launch a project and kick off a collaborative workflow: 1 Start DaVinci Resolve on a machine wired to a remote project library or Blackmagic Cloud server. 2 Using the Project Manager, open whatever project lives on the remote project library that DaVinci Resolve currently points at. 3 With the project open, pick File > Multiple User Collaboration. As soon as collaboration switches on, a pair of extra buttons shows up at the bottom-right of the DaVinci Resolve interface, beside the Project Manager and Project Setting buttons. Those are the Collaboration Chat and Collaboration buttons.

At far left sits the Collaboration Chat button, with the Collaboration button just next to it (second from the left)

NOTE: Switching collaboration on disables, automatically, the Project Settings’ General Options panel setting labeled “Auto conform missing clips as media is added to Media Pool,” because it interferes with collaborative workflow. Live Save, meanwhile, gets enabled by itself within the Auto Save panel of the User Preferences, ensuring each collaborator’s work is saved at regular intervals and clashes between collaborators are avoided.

### Opening Projects to Collaborate

Once Collaboration is enabled on a project, its thumbnail in the Project Manager carries a badge that signals the project is open for collaboration.

Within the Project Manager, an icon flags a project as open for collaboration From this point, anyone else holding access to this remote project library server can launch the project and start collaborating with you. Every time someone joins whatever project you’re currently in, that Collaboration Chat button at the foot of the DaVinci Resolve UI brightens to flag a waiting message. When highlighted, the Collaboration Chat button alerts you to a message Open the Collaboration Chat window and you’ll see who you’re collaborating with.

In the Collaboration Chat window, an incoming message tells you which other person has opened your current project

### Customizing Your Collaborator Identification

After a project is configured for collaboration, you’ll want it to be simple to distinguish your collaborators from one another. A click on the Collaboration button brings up a roster of every collaborator, or project member, active in that project.

Opening the Collaboration list shows all the current project members You sit at the top of that roster, and you can revise the name you go by simply by typing into the text field. The image you picked in either your Blackmagic Cloud account or the DaVinci Resolve Project Server determines your user icon automatically. With no image selected, it falls back to the first two letters of your user name. You’re also shown each other member’s workstation OS, displayed as an icon just to the right of that member’s name.
