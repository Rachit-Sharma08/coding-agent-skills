# Deliver page viewer and skimming in the viewer

Version: DaVinci Resolve 20.3 Reference Manual. Context: Delivery overview.
[Chapter index](INDEX.md) / [Previous section](the-deliver-page-and-quick-export.md)
<a id="source-deliver-page-viewer"></a> <a id="source-disabling-viewer-updates-while-rendering"></a> <a id="source-drag-to-reorder-jobs-in-the-render-queue"></a> <a id="source-skimming-in-the-viewer"></a> <a id="source-the-render-queue"></a> <a id="source-the-render-queue-displays-all-jobs"></a>

### Deliver page Viewer

During tape output, the Viewer displays the tape signal so you can lay in insert or assembly edit points, and provided device control is on, the transport controls run the tape inside the deck. The Viewer can also be expanded to fill the whole screen via Cinema Viewer mode, reached by choosing Workspace > Viewer Mode > Cinema Viewer (P). That command flips Cinema Viewer mode on and off.

### Skimming in the Viewer

To skim footage within any viewer across the Media, Cut, Edit, Color, and Deliver pages, hold the C key down while dragging the pointer to and fro inside the viewer.

### Disabling Viewer Updates While Rendering

Inside the Render page Viewer option menu, an Updates During Renders submenu gives you the choice to disable, minimize, or enable Viewer updates as a program renders. Cutting Viewer updates to minimal or off speeds up rendering, particularly on less powerful workstations.

### The Render Queue

Every job you have lined up for delivery appears in the Render Queue. A job can carry its own clip range and render settings, letting you output several sections or clips of one timeline, push the same timeline to multiple formats, or handle several timelines. The Render Queue can be set to display only the jobs in the current project, or instead every job queued and stored across all projects held in the open SQL network project library (for the current user) or the local project library (at the disk location presently selected). That proves especially handy when a program has been split into several reels, each reel living as its own project. Toggle it through the “Show All Projects” entry of the Render Queue Option menu. A job sitting in the Render Queue can be edited via its pencil button, routed to remote rendering workstations, or removed. Jobs already rendered may stay in the Render Queue so they can be re-rendered down the road.

### The Render Queue displays all jobs

TIP: Choosing “Show Job Details” from the Render Queue Option menu surfaces the Render Settings for each entry in the Render Queue. It lays out the particulars of every job — its dimensions, frame rate, codec and so on. At a glance, this is a real aid when you are juggling a complex render queue.

### Drag to Reorder Jobs in the Render Queue

Reordering the Render Queue by hand is a matter of dragging a job up or down within the stack. The job numbers hold their numerical sequence, yet the render settings tied to each will swap accordingly.

In the Render Queue, Job 3 (H.264) being dragged ahead of Job 2 (ProRes)
