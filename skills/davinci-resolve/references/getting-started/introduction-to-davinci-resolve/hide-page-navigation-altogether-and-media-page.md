# Hide page navigation altogether and media page

Version: DaVinci Resolve 20.3 Reference Manual. Context: Introduction to DaVinci resolve.
[Chapter index](INDEX.md) / [Previous section](project-manager-and-preferences-and-project-settings.md) / [Next section](cut-timeline-meters-and-edit-page-layout.md)
<a id="source-audio-meters-exposed"></a> <a id="source-audio-panel"></a> <a id="source-clip-metadata-editor"></a> <a id="source-hide-page-navigation-altogether"></a> <a id="source-media-page"></a> <a id="source-media-page-viewer"></a> <a id="source-media-pool"></a> <a id="source-media-pool-showing-the-selected-bins-clips"></a> <a id="source-media-storage-with-scrubbable-clip-view"></a> <a id="source-metadata-editor"></a> <a id="source-the-cut-page"></a> <a id="source-the-cut-page-1"></a> <a id="source-the-media-page"></a> <a id="source-the-media-pool"></a> <a id="source-the-media-storage-browser"></a> <a id="source-the-single-viewer-in-the-cut-page"></a> <a id="source-the-strip-view-mode"></a> <a id="source-the-viewer"></a> <a id="source-the-viewer-modes-buttons"></a> <a id="source-viewer"></a>

### Hide Page Navigation Altogether

Should you be an artist who works on just one page of the DaVinci Resolve experience, or should you crave more screen room because your monitor’s resolution is limited, choosing Workspace > Show Page Navigation will tuck away the page navigation bar along the bottom of the DaVinci Resolve user interface. Even with that bar closed, the other pages remain reachable through the Workspace > Switch to Page submenu commands or the keyboard shortcuts. To flip the Show Page Navigation function on or off: Check Workspace > Show Page Navigation. Once this interface element is hidden, keyboard shortcuts get you to the individual pages (Shift - 2 through 8), the Project manager (Shift - 1), and the Project settings (Shift - 9). These same functions are also available from DaVinci Resolve’s main menu bar.

### The Media Page

When it comes to bringing in clips, managing media, and organizing clips, the Media page is the main interface in DaVinci Resolve. A core principle of how DaVinci Resolve operates is that a project’s source media is kept apart from the project data you bring in and handle on the Edit page. That separation makes it easy to manage and refresh the clips your current project’s timelines depend on — flipping between offline and online media, rearranging clips, and sorting out whatever problems crop up.

### Media page

A good deal of the essential functionality for on-set workflows also lives on the Media page, as do the ingest, organizing, and sound-syncing steps of digital dailies workflows. These pages walk through most of what the Media page can do, detailing functions that get referenced all through this manual.

Six distinct areas make up the Media page, all arranged to help you locate, choose, and work on the media in your project. A large share of its functionality and the bulk of its commands sit inside the contextual menus that pop up on a right-click of clips within either the Library, the File Browser, or the Media Pool. To go deeper on working with the Media page, turn to Chapter 17, “Using the Media Page.”

### The Media Storage Browser

Every volume presently reachable by your Resolve workstation is listed in the Media Storage browser. You use it to track down media you intend to bring into your project by hand.

### Media Storage with scrubbable Clip view

### Viewer

Whatever clip you pick in any part of the Media page reveals its contents inside the Viewer. Along the bottom runs a jog bar that lets you drag the playhead straight with the pointer, while a jog control nestled between the mode drop-down and the transport controls lets you inch through a long clip more gradually. That jog bar’s entire width stands for the clip’s whole duration in the Viewer. Where the playhead currently sits is reported in the timecode field up at the Viewer’s top right corner. Beneath the jog bar sit straightforward transport controls for Jump to First Frame, Play/Stop, and Jump to Last Frame. To change audio levels, right-click the speaker icon and drag the slider. You may also send the Viewer into Cinema Viewer mode through Workspace > Viewer Mode > Cinema Viewer (Command-F) so it takes over the whole screen; that command switches Cinema Viewer mode on and off. With two monitors attached to your computer, you can have the Viewer fill one screen entirely while the Resolve UI stays on the other by choosing Workspace > Full Screen Viewer On and picking the display you want the Viewer on.

### Media page Viewer

### Media Pool

Every bit of video, audio, and still image media you bring into the current project resides in the Media Pool, as does whatever media rides in automatically alongside timelines imported into DaVinci Resolve. As a rule, media brought into a project lands in the Master bin, but you are free to split the Media Pool across as many bins of your own making as your needs call for. Inside the Media Pool, media moves from one bin to another without restriction. The Media Pool turns up on the Edit, Fusion, Color, and Fairlight pages too, so you can browse and open clips and timelines wherever they matter.

### Media Pool showing the selected bins’ clips

### Metadata Editor

Pick a clip anywhere on the Media page and its metadata shows up in the Metadata Editor. Should you select several clips, only the final one’s information is shown. Across the Metadata Editor’s header runs read-only information about the chosen clip — its file name, directory, duration, frame rate, resolution, and codec. Below that, a run of editable fields in the Metadata Editor lets you look over and revise whichever metadata items are on hand. A drop-down at the Metadata Editor’s top right offers a host of different sets of metadata fields and checkboxes, each bundled for a particular task or workflow.

### Clip Metadata Editor

### Audio Meters exposed

### Audio Panel

A pair of buttons above the audio meters flips the Audio panel between its two modes. Under the default Meters mode, Audio Meters appear and report the audio levels of whatever clips are playing. Switch to Waveform mode and you can lay audio clips next to the video clips open in the Viewer so as to sync them by hand. The Audio panel may also be tucked out of view.

### The Cut Page

As a tight, focused space for fast editing, the Cut page shines when you must rapidly cut a news segment, assemble an episode of web content, edit a no-frills program, try out several arrangements of a scene, or throw together a first assembly edit. It also serves as a friendly first editing interface for newcomers, putting forward a pared-down toolset that learns fast and stays simple. No matter where you come from, the Cut page proves a worthwhile addition to how you edit in DaVinci Resolve. By default its workspace gathers the Media Pool, a lone Viewer, and the Timeline area. Across those three regions you can swiftly import and sort clips, edit them, and even export what you have made — all without stepping outside the Cut page.

### The Cut page

To learn more about the Cut page, head to Chapter 26, “Using the Cut Page.”

### The Media Pool

On the Cut page too the Media Pool turns up, holding all the video clips, audio clips, graphics, and other media you import into your project. To keep that media tidy and quick to locate, you can spin up Bins, which open from the bin drop-down at the top left corner. Whatever you import — video, audio, or graphics — appears as its own clip, and each one can be selected, scrubbed for a fast look, shuffled into bins, opened in the Viewer for playback, or dropped into a timeline by way of the edit buttons or a drag and drop. Since the Cut page is built to speed editing up, the Media Pool brings along its own viewing options (the Strip view among them) and ways to customize.

### The Strip View mode

### The Viewer

Through the Viewer you watch clips from the Media Pool or those in the Timeline play back, and it carries a wealth of controls over what you see and how playback runs.

### The single Viewer in the Cut page

Four mode options live in the Viewer. Four buttons up in the Viewer’s top left corner both show which one is active and let you swap between them.

### The Viewer modes buttons

A range of actions drops you into each of these options on its own (reading left to right):

- Double-click any clip and it opens in the Viewer as a Source Clip.
- A whole bin’s worth of clips can be viewed at once via the Source Tape.
- Your edited program plays back in the Timeline.
- Every piece of your synced material can be seen together through the Multi Source Viewer.

Press the Tools button at the Viewer’s lower left and an effects toolbar opens, letting you add and tweak clip effects straight inside the Viewer with no Inspector required. That Tools button surfaces an assortment of controls for sizing, cropping, audio, speed effects, stabilization, dynamic zoom, and compositing.
