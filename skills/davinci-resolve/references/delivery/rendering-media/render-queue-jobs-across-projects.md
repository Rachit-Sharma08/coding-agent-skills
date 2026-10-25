# A selected job in the render queue and rendering jobs from multiple projects at once

Version: DaVinci Resolve 20.3 Reference Manual. Context: Rendering media.
[Chapter index](INDEX.md) / [Previous section](additional-render-outputs-and-overwrite-prevention.md)
<a id="source-a-selected-job-in-the-render-queue"></a> <a id="source-remote-rendering"></a> <a id="source-rendering-jobs-from-multiple-projects-at-once"></a> <a id="source-setting-up-a-headless-remote-rendering-workstation"></a> <a id="source-setting-up-and-using-remote-rendering"></a> <a id="source-sharing-storage"></a> <a id="source-using-multiple-project-libraries-in-remote-rendering"></a> <a id="source-when-youre-finished-remote-rendering"></a>

### A selected job in the Render Queue

Media Offline Warning in Render Queue Should you try adding a job to the Render Queue whose timeline holds any offline material, DaVinci Resolve throws up a warning on its own. You can either back out of adding the job, or add it regardless, aware you're set to render one or more offline clips.

The Media Offline warning box that pops up when a timeline carrying offline clips or frames gets added to the Render Queue

To show more details about jobs in the Render Queue: Open the Render Queue Option menu (at the upper right-hand corner) and pick Show Job Details. Beneath the name and location path, every job then spells out its frame size and format, the frame rate, the audio channels alongside sample rate, plus the duration.

A selected job in the Render Queue with job details shown

To rename a job: A job takes a custom name when you simply click its default name (Job 1, Job 2, and so on) and type one of your own. That's handy for labeling jobs you expect to re-render again and again as a project moves along. To start rendering: 1 To limit rendering to only certain jobs in the Render Queue, pick one or more by clicking a job, then Command-clicking others for a scattered set, or Shift-clicking another to grab a whole stretch of jobs. Once you pick one or more jobs, only those selected get rendered. With nothing selected, the queue's every job gets rendered. 2 Click the Start Render button, found below the Viewer over on the right of the interface. 3 Should the Render Queue hold jobs already rendered, a dialog asks whether, since the selection includes items already rendered, you'd like to re-render those. Click Yes to re-render every job in the Render Queue. Click No to render only the jobs not yet done. Click Cancel to scrap the whole rendering operation. Rendering kicks off from the topmost job in the list. The Overall Progress bar begins filling, right to left, showing how much of the queue has rendered so far. As rendering runs, the Start Render button becomes the Stop Render button, which you can click any time to stop rendering. TIP: While a render is underway, a small progress bar appears over the DaVinci Resolve icon — in the Mac OS X dock, or down on the Windows taskbar.

To remove jobs from the Render Queue, do one of the following:

- To clear a specific job: In the Render Queue, click the X up at the top right of that job's entry.
- To clear all previously rendered jobs: Open the Render Queue Option menu (at the upper righthand corner) and pick Clear Rendered.
- To clear all jobs: Open the Render Queue Option menu (at the upper right-hand corner) and pick Clear All.

To flip a rendered job back to looking unrendered: Right-click any rendered job and pick Clear Render Status. Several jobs can also be grabbed to switch their rendered status all together. That makes re-running the exact same job simple. To edit a job, whether or not it's been rendered: 1 In the Render Queue, click the Pencil button to select it.

Clicking the pencil icon to revise a Render Queue job The chosen Render Queue's settings reload into the Render Settings list and reset the Timeline's selected range matching that job. 2 Adjust whatever settings you need. 3 Once you're done editing the job, click the Update Job button that shows up at the bottom of the Render Settings, or click Add New Job to spin up a fresh job carrying your changes while the earlier job stays put. NOTE: Click the Pencil button again without having clicked Update Job and you'll be prompted to Save, Cancel, or Don't Save.

To look over the clips tied to rendered jobs: To surface a rendered clip within the Media Storage browser: Right-click any rendered job and pick Reveal in Media Storage. To bring up a rendered clip within your computer's own file system (Mac OS only): right-click a rendered job, then pick Reveal in Finder.

### Rendering Jobs from Multiple Projects at Once

You can likewise drop several projects from the open PostgreSQL or local project library into the render queue all in one go. That proves especially handy when you've split a program into multiple reels, each reel a separate project. Rendering output across several projects in one pass goes like this: 1 Open each project, line up whichever jobs you want rendered in the Render Queue, and save that project without rendering it. 2 After the last project is set up, open the Render Queue Option menu (at the upper right-hand corner) and pick Show All Projects. Every queued item across projects owned by the currently selected user (on a network project library) or held in the currently named disk location (on a local project library) now shows in the Render Queue.

3 Hit Start Render and rendering runs through every job across every project queued up. 4 Once you're done, switch Show All Projects off to return to showing only the current project's render queue items.

### Remote Rendering

When several DaVinci Resolve workstations share one network, you can hand a job in the Render Queue off from the machine you're on (called the "artist workstation") to one of the network's "remote workstations" through remote rendering. This puts any of your idle secondary workstations to work rendering your jobs while you keep going on your main one. To make use of remote rendering, you have to meet the following three criteria:

- DaVinci Resolve Studio has to be installed on both the artist workstation and the remote workstation. The free version of DaVinci Resolve won't do remote rendering.
- The artist workstation and the remote workstation can both draw on the same shared network project library, or any other Postgres project library tied to either machine, or to a dedicated Remote Project Library Server.

For a fuller account of configuring and working with shared project libraries, turn to Chapter 196, “Managing Project Libraries and Project Servers.”

- Both the artist workstation and the remote workstation have to reach the same media files, whether on the same storage volumes or on identically named ones.

### Using Multiple Project Libraries in Remote Rendering

Remote renders can be set up for projects across every connected Davinci Resolve project library, not solely the one that's active. To switch this on, tick the "Automatically scan other project libraries for Remote Rendering jobs" box under the General settings of the System tab, within the DaVinci Resolve Preferences.

### Sharing Storage

For remote rendering to behave, it matters that both the artist and remote workstations can reach the same media on the same named storage volume. One route is shared storage of some kind, such as a SAN. Another is mounting the same volume across your network. That's slower, but it does the job. When remote rendering spans a mix of Mac OS X, Windows, and Linux workstations, you'll need the Mapped Mount column found in the Media Storage Locations list, which sits within the System Preferences' Media Storage panel; there you add each volume's path as the workstation it's attached to understands it. As an example, on a Windows workstation reaching volumes off a Linux workstation, enter the Linux-style file paths in the Mapped Mount column for every scratch disk shown.

### Setting Up and Using Remote Rendering

Remote rendering is simple to use, though it takes a little setup. 1 Confirm the storage volume holding the media the project you mean to render points to is mounted on both the artist and remote workstations. 2 Launch DaVinci Resolve on the remote workstation, then take one of these steps:

- As the Project Browser opens, right-click anywhere and choose Remote Rendering.
- If a project is already open in DaVinci Resolve, you can instead choose Workspace >

Remote Rendering. DaVinci Resolve jumps straight to the Deliver page on its own, sitting ready for jobs to be handed over for automatic rendering. 3 Back on the artist workstation, queue up a job in your usual way. 4 For that job in the Render Queue, click the Remote Rendering button and one of the choices the list presents: Any: Hands the job off automatically to whichever workstation isn't busy rendering at the moment. Should every remote rendering workstation already be busy, it queues the job to run next. YourComputer.local: The artist workstation bearing the name "YourComputer." Pick this to render the job right here locally rather than out on the network. Other Workstations on Network: Every other remote rendering workstation appears below, letting you point the job at one particular machine.

Clicking the Remote Render button to send a job out for remote rendering 5 Click Start Render. The job heads off to the remote workstation you chose and renders there, leaving you free to keep working at your artist workstation.

### When You’re Finished Remote Rendering

After you've finished running a given DaVinci Resolve workstation in Remote Rendering mode and want it back as an artist workstation, choose Workspace > Remote Rendering to leave remote rendering and head back to the Project Manager.

### Setting Up a “Headless” Remote Rendering Workstation

DaVinci Resolve lets remote rendering clients run in a so-called "headless" mode without any GUI. You pull this off from the command line: open the directory where the app sits, then launch DaVinci Resolve in Remote Rendering (–rr) mode with the command line syntax that fits your operating system. Launched like this, DaVinci Resolve sits silent and out of sight on that machine, ready for any remote rendering jobs routed to it. On macOS Launch Terminal. Switch into the directory: cd /Applications//DaVinci\ Resolve/DaVinci\ Resolve.app/ Contents/MacOS/ Then issue: ./Resolve -rr On Windows Launch the Command Prompt. Switch into the directory: C:\Program Files\Blackmagic Design\DaVinci Resolve\ Then issue: Resolve.exe -rr On a Linux CentOS 6.8 system Launch Terminal. Switch into the directory: cd /home/resolve/Cyclone/ Then issue: ./script.start -rr On a Linux CentOS 7.x system Launch Terminal. Switch into the directory: cd /opt/resolve/bin Then issue: ./resolve -rr
