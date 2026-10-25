# Creating timelines and customizing settings

Version: DaVinci Resolve 20.3 Reference Manual. Context: Creating and working with timelines.
[Chapter index](INDEX.md) / [Next section](drt-timeline-import-export-backup-and-restore.md)
<a id="source-adding-media-pool-timelines-directly-to-the-render-queue"></a> <a id="source-creating-and-duplicating-timelines"></a> <a id="source-creating-and-working-with-timelines"></a> <a id="source-creating-and-working-with-timelines-part-1"></a> <a id="source-creating-blank-and-stringout-timelines"></a> <a id="source-creating-timelines-by-drag-and-drop"></a> <a id="source-creating-timelines-from-bins-and-selections"></a> <a id="source-creating-timelines-using-an-imf-or-dcp-composition-playlist-cpl"></a> <a id="source-disabling-timelines"></a> <a id="source-duplicating-timelines"></a> <a id="source-individual-timeline-settings-for-format-monitoring-output-and-color"></a>

### Creating and Working with Timelines

This chapter covers how timelines are built and reshaped — the containers where clips are cut together into the finished sequences that make up your programs.

### Creating and Duplicating Timelines

When you aren’t bringing in a project cut somewhere else, a fresh timeline lets you start an edit from nothing, gather clips destined for a Fusion composition, grade a batch of dailies, or build an audio program over on the Fairlight page. At creation time you may either populate the timeline with every clip sitting in the Media Pool — a fast route to a large set of offline dailies — or begin with an empty one and add chosen clips yourself. Whatever timelines you make land in the Media Pool bin that is currently active. For a quick way to view every timeline across the project at once no matter where each one lives, switch on the “Smart Bin for Timelines” option found in the Editing panel of the User Preferences. Doing so adds a Smart Bin to the Media Pool’s Bin list that gathers all project timelines, letting you survey them all while leaving your existing layout untouched.

### Individual Timeline Settings for Format, Monitoring, Output, and Color

A freshly made timeline can be tailored in several ways, though out of the box it simply inherits the project-wide timeline values for resolution, frame rate, and the rest of the format and monitoring parameters.

The Create New Timeline dialog with standard customization settings That said, each timeline can instead carry its own Format, Monitoring, Output Sizing, and Color Management values — handy whenever a job requires several timelines producing distinct deliverables whose resolutions, pixel aspect ratios, frame rates, monitoring, output scaling choices, and color management differ from the project as a whole, “Mismatched Resolution Files” settings included. Picking per-timeline values is a matter of clearing the Use Project Settings box inside the New Timeline dialog, after which extra controls show up.

Clicking Use Custom Settings exposes additional panels for individualized timeline settings After a timeline has been built with its own values, revisit them by right-clicking the timeline in the Media Pool and selecting Timelines > Timeline Settings from the contextual menu. That opens an Edit Timeline dialog whose distinct Format, Monitor, Output, and Color panels you can work through. Clicking Use Project Settings instead reverts that timeline to the project-wide values. The custom timeline settings even let you adjust the starting timecode of several timelines together. To change the start timecode for multiple timelines at once: 1 Highlight every Timeline whose timecode needs adjusting. 2 Right-click any one of those selected Timelines and pick Timelines > Starting Timecode from the contextual menu. 3 Type the replacement timecode into the Time Start field. 4 Click on OK.

### Creating Blank and Stringout Timelines

For a brand-new video or audio program you’ll generally reach for a blank timeline. That very same command, though, produces stringout timelines for dailies once the “Empty Timeline” checkbox is switched off. To create a new blank timeline: 1 (Optional) Pick or make a folder within the Bin list to hold the new timeline. 2 Do one of the following:

- Choose File > New Timeline (Command-N).
- Right-click within the Media Pool, and choose Timelines > Create New Timeline.

3 Once the New Timeline Options window appears, configure these options: Start Timecode: Adjust the Start Timecode whenever a particular start time is needed. Timeline Name: Type a name into the Timeline Name field.

No. of Video Tracks: Specify the count of video tracks you’d like. Dragging across this field also nudges the video-track count via a virtual slider. Use Fairlight Preset: With this box ticked, the timeline is built with audio tracks pre-assigned from a Fairlight Configuration preset you saved earlier. A drop-down then surfaces so you can pick the exact preset for the Timeline. That preset stands in for the No. Of Audio Tracks setting further down. Fairlight Configuration presets are built through the Fairlight Presets Library, which the Fairlight menu opens. Chapter 171 of the DaVinci Resolve Manual, “Setting Up Tracks, Busses, and Patching,” goes deeper. When no Fairlight Configuration presets exist, this option stays hidden. No. of Audio Tracks: Specify the count of audio tracks you’d like. Dragging across this field likewise sets the audio-track count via a virtual slider. Audio Track Type: Pick the channel mapping the new audio tracks should adopt. Empty Timeline: On by default, this makes new timelines start out empty. Clearing the Empty Timeline checkbox means the resulting Timeline gathers every piece of media across all Media Pool bins, in effect producing a stringout of everything imported. Use Selected Mark In/Out: Surfaces only while “Empty Timeline” is off. Ticking this checkbox makes each clip’s length in the new Timeline follow the In and Out points stored on that clip. Clips lacking In/Out points contribute their full duration. Use Custom Settings: Press this button to reveal the Format, Monitor, and Output tabs that hold per-timeline unique settings. 4 Click Create New Timeline. A new timeline is created. Should the need arise, copying an existing timeline lets you rework an edit or spin up an alternate grade. TIP: When you expect to spin up several new timelines sharing one parameter set, open the User pane of the Preferences and revise the New Timeline Settings under the Editing panel. From then on those presets feed the New Timeline Options window.

### Creating Timelines by Drag and Drop

At the moment a project is first made, the Timeline Editor holds no timeline, which gives you a chance to spin one up via drag and drop. Building a timeline this way takes a single move: pull any clip down into the vacant Timeline Editor region beneath the Viewers on the Edit page, and a fresh timeline is generated on its own.

### Creating Timelines From Bins and Selections

Through the “Create Timeline Using Bin” and “Create Timeline Using Selected Clips” commands you can rapidly build a timeline out of Media Pool contents, honoring whichever In and Out points each clip carries and relying on the host bin’s sort order to set the sequence the clips fall into. TIP: Such commands shine when you want fast assembly edits from metadata-rich media — scene, shot, and take fields for sorting clips, plus In and Out points you’ve already recorded. Assembling a timeline from everything inside a bin works like this: 1 (Optional) Switch the Media Pool to List mode, mark In and Out points on every clip in your Bin, and order the Media Pool by the column that arranges all clips the way you want them assembled. 2 Right-click that bin within the Bin list, then pick Create Timeline Using Bin. 3 Name the new timeline inside the New Timeline Properties dialog. To honor each clip’s In and Out points, confirm “Use Selected Mark In/Out” is ticked, then click Create New Timeline. Building one from clips you choose by hand instead goes as follows: 1 (Optional) Flip the Media Pool into List mode, log In and Out points across each clip in your Bin, and re-sort the Media Pool on whichever column lines the clips up in your intended assembly order. 2 Highlight one or more clips to gather into a fresh timeline. 3 Right-click any of those highlighted clips, then pick Create Timeline Using Selected Clips. 4 Name the new timeline inside the New Timeline Properties dialog. To honor each clip’s In and Out points, confirm “Use Selected Mark In/Out” is ticked, then click Create New Timeline. Out of the box, Audio Track Type sits at “Based on selected media,” so the timeline’s audio tracks mirror the channel mapping of whatever clips you chose, though you may set other specific mappings by hand when needed.

### Creating Timelines Using an IMF or DCP Composition Playlist (CPL)

DaVinci Resolve lets you generate a timeline that faithfully mirrors the Composition Playlist (CPL) belonging to a DCP or IMF package. For now this remains a DaVinci Resolve Studio only feature. The procedure built around a Composition Playlist (CPL) runs as follows: 1 Bring an IMF or DCP package into the Media Pool just as you would any other media. 2 Right-click the imported clip, then pick “Create New Timeline Using Composition Playlist” off the contextual menu. 3 Within the New Timeline dialog box, select the specific CPL from the package via the “Composition Playlist” drop-down menu. 4 Apply whatever ordinary new Timeline tweaks the job calls for (Resolution, Aspect Ratio, and the like), then click the “Create” button.

### Duplicating Timelines

Existing timelines can also be copied — useful for preserving a snapshot before you alter anything, or as the seed for an alternate version of your work. Duplicating a Timeline happens by either of these routes:

- Highlight a timeline in the Media Pool, then choose Edit > Duplicate Timeline. The copy shows up with “copy” tacked onto its name.
- Right-click a Media Pool timeline and pick Duplicate Timeline out of the contextual menu.

### Disabling Timelines

Within the Media Pool you can toggle timelines on or off for reasons of both speed and tidiness. Editors who keep a running record of a program’s edit through a steady stream of periodically copied timelines benefit most. Because a project file packed with many timelines may drag down performance, the option to switch them off lets you keep those backup or alternate timelines around at no cost. Switched-off timelines never get loaded into RAM, leave the speed of opening, saving, exporting, or loading a project untouched, and don’t weigh on program performance. Such a timeline also drops out of the viewer drop-down menus across the program. It stays visible in the Media Pool, yet wears a crossed out eye icon at the lower left to signal its state. None of the DaVinci Resolve pages will open a timeline that’s been disabled. Switching a timeline off works like this:

- Highlight the Timeline, right-click it, and pick “Disable Timeline” from the drop-down menu.

To enable a timeline:

- Highlight the Timeline, right-click it, and pick “Enable Timeline” from the drop-down menu.

TIP: Grouping and arranging Enabled versus Disabled timelines across the whole project is simple — build a Smart Bin keyed on the MediaPool Properties > Timeline fields and set it to “is Enabled/Disabled.” The crossed-out eye at the lower left of the thumbnail marks this Timeline as disabled.

### Adding Media Pool Timelines Directly to the Render Queue

A timeline can be dropped straight onto the Deliver page’s Render Queue: right-click the timeline, hover over Add to Render Queue Using, and pick one of the listed presets. Your own presets join that list whenever you save a fresh custom preset over on the Deliver page. At that point you’re asked where the file should be rendered. The timeline then lands in the Deliver page’s Render Queue, though nothing renders until the Render All button is clicked.

Choosing a Preset under the “Add to Render Queue Using” menu option pushes the timeline straight onto the Render Queue
