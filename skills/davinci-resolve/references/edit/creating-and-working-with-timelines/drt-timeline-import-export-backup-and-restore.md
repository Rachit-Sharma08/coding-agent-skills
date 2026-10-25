# Import and export DaVinci resolve timelines drt and backing up and restoring timelines

Version: DaVinci Resolve 20.3 Reference Manual. Context: Creating and working with timelines.
[Chapter index](INDEX.md) / [Previous section](creating-timelines-and-customizing-settings.md) / [Next section](naming-timeline-tracks-and-the-tracks-index.md)
<a id="source-backing-up-and-restoring-timelines"></a> <a id="source-creating-and-working-with-timelines-part-2"></a> <a id="source-import-and-export-davinci-resolve-timelines-drt"></a> <a id="source-modifying-timeline-tracks"></a> <a id="source-restoring-a-timeline-backup-in-the-media-pool"></a> <a id="source-restoring-deleted-timeline-backups"></a> <a id="source-the-timeline-view-options-dropdown"></a> <a id="source-timeline-view-options"></a>

### Import and Export DaVinci Resolve Timelines (.drt)

Individual timelines can move from one DaVinci Resolve project into another already-existing DaVinci Resolve project, so you can hand timelines off quickly between projects and workstations without generating extra imported project files. Only the timeline plus its linked clip information travels; the actual media files stay behind. Sending one timeline out of the Media Pool goes like this: 1 Select your chosen timeline there. 2 Choose File > Export > Export AAF, XML, DRT (Shift-Command-O). 3 In the file system dialog, set the format popup to “DaVinci Resolve Timeline Files (\*.drt).” 4 Decide where the DaVinci Resolve Timeline file (.drt) should be saved in the file system dialog, then click Save.

Sending several timelines out of the Media Pool goes like this: 1 Highlight several timelines within the Media Pool. 2 Right-click any timeline and follow Timelines > Export > DaVinci Resolve Timeline Files. 3 Point your file browser at the folder where they should be saved. In contrast to single-timeline export, a batch export gives you no chance to rename the .drt files; each keeps whatever timeline name it carries in the Media Pool. Bringing a timeline back into the Media Pool runs as follows: 1 Pick the Media Pool bin that should hold the imported timeline. 2 Do one of the following:

- Choose File > Import Timeline > Import AAF, XML, DRT (Shift-Command-I), then pick a DaVinci Resolve Timeline file (.drt) in the file system dialog and click Open.
- Double click the .drt file in your file system.

The timeline shows up in the Media Pool together with every clip tied to it, media sync information included. To keep names unique, anything imported this way gets the word “import” added to its name. That imported timeline is conformed automatically against matching media already sitting in the Media Pool. If, however, the timeline traveled to a different computer, you might need to reimport or relink any missing or offline media to bring the imported timeline fully online. NOTE: This method handles just one timeline per import or export. For several timelines at once, turn to the Import/Export Bin function instead.

### Backing Up and Restoring Timelines

Inside the User Preferences, under its Project Save and Load panel, ticking the Timeline Backups checkbox lets DaVinci Resolve store several timeline backups at set intervals, following a scheme much like the GFS (grandfather-father-son) rotation. It works whether or not Live Save is active. To roll back to an earlier backup of a timeline, just right-click the timeline in the Media Pool, pick Restore Timeline Backup from the contextual menu, and select the backup you want from the list. Because backups are sorted by date and time, pinpointing the exact timeline to restore is easy. At certain points during editing it’s wise to lay down a backup by hand before you overhaul the rest of your timeline. The safest route is generally duplicating the timeline, though you may instead drop a manual backup point that gets recalled alongside your other timeline backups. Laying down a named backup point yourself takes either of these forms:

- Select File > Create Timeline Backup (Option-Command-S).
- Right-click your Media Pool timeline and pick Create Timeline Backup from the context menu.

Pulling back a timeline backup leaves your current timeline intact. Rather, the chosen backup arrives in the Media Pool as a new timeline carrying the suffix “Backup” on its name.

### Restoring a timeline backup in the Media Pool

A timeline backup is written only after a project has actually changed. Should DaVinci Resolve sit idle for a stretch — say while your smart watch nudges you to step outside and circle the block — no further project backups are written, which stops DaVinci Resolve from replacing valuable backups with pointless ones. Three of the fields govern how frequently a new backup is saved, and the fourth picks where those backups go. Both Project and Timeline backups obey these settings.

- Perform backups every X minutes: This first field sets the cadence for a new backup inside the most recent hour of work. The default cadence is every 10 minutes, which yields six backups across that hour. As soon as an hour of work elapses, an hourly backup is written and the per-minute ones start dropping off in first in, first out fashion. By default that leaves you holding only six backups at any moment, each covering the past hour’s work.
- Hourly backups for the past X hours: This second field sets how many hourly project backups to keep. By default two hourly backups are held for the current day. Beyond that figure, hourly backups start dropping off in first in, first out fashion.
- Daily backups for the past X days: This third field sets how many days’ worth of backups to keep. Whatever backup is saved last on a given day becomes that day’s daily backup, and by default only two days of daily backups are retained. Beyond that figure, daily backups start dropping off in first in, first out fashion. For a project spanning a longer period, feel free to bump this number up.
- Project backup location: Press the Browse button to point these backups at a chosen location. By default they go to a “Project Backup” directory on your scratch disk, but you may redirect them to a volume that suits your data backup methodology better. That folder holds both Project and Timeline backups.

### Restoring Deleted Timeline Backups

Via the Media Pool Options menu, choosing Deleted Timeline Backups lets you inspect removed timelines along with the backup files on hand for each one. From there you may flag backups for restoration or opt to wipe selected backups permanently.

### Timeline View Options

While you cut an edit, reshaping how the Timeline looks is frequently handy — resizing video or audio clips, deciding whether audio waveforms get drawn, and the like. The Timeline View Options dropdown sitting at the Timeline’s far left is where you apply such adjustments on the fly.

### The Timeline View Options dropdown

You have the following options:

- Timeline View Options: A trio of buttons toggles particular Timeline interface elements into or out of view, namely: Display Stacked Timelines: This option presents stacked timelines so several can be shown at once, one above another. Display Subtitle Tracks: Reveals or conceals the Timeline’s subtitle tracks region. Concealing subtitle tracks won’t switch off subtitle display; for that you must disable whichever subtitle track is currently shown. Display Audio Waveforms: Flips audio waveform viewing off or on. With Audio Waveform off, audio tracks shrink to their minimum.
- Thumbnail View Options: A trio of buttons sets the overall look of the video track. From left to right:

Filmstrip: Renders every clip as a run of frames spanning its length. How many frames appear hinges on the clip’s present zoom level in the timeline. Thumbnail: Renders every clip as a solid color, placing a thumbnail of the clip’s In point at its start and a thumbnail of the Out point at its end. Which thumbnails show depends on the clip’s current zoom level and track height in the timeline. When a clip lacks room for both, only the In point thumbnail shows. None: Renders every clip as a solid color across its length.

- Viewer Background: Four choices — Checkerboard, Black, Grey, or Alert Red — set the color used for the transparent background inside the Viewer.
- Fixed Playhead: This option switches between a fixed playhead, which holds the playhead anchored mid-timeline while the tracks slide beneath it, and Free Playhead, where the playhead runs along the timeline during playback.

With the Fixed Playhead option active, you’re free to position the Fixed Playhead wherever you like along the timeline instead of leaving it centered. Just rest the pointer on the playhead’s top within the Timeline Ruler, then drag toward whatever spot you prefer. Relocating the Fixed Playhead can help by widening the timeline working area available for clips ahead of or behind the current point.

- Audio View Options: A trio of buttons controls how audio waveforms appear in the Timeline whenever they’re shown.

Display Non-Rectified Waveform: Switches the waveform between rising from the bottom of the audio track and being centered with a mirror image of itself. Display Full Waveform: Removes the divider bar separating the waveform from each audio clip’s file name region, letting the waveform fill the entire audio bar in the Timeline. Display Waveform Border: Adds a dark outline around each waveform’s edges so they stand out more clearly.

- Video track height slider: Scales every video track together in one move, apart from the audio tracks.
- Audio track height slider: Scales every audio track together in one move, apart from the video tracks.

Beyond that, you can resize a single Timeline track on its own by dragging its top divider within the Track Header region. Edit page track heights operate independently of the Thumbnail and Waveform view choices set in the Timeline View options. In the past, certain Timeline viewing modes like Filmstrip or Thumbnail view carried minimum track height limits. These days track height is fully adjustable regardless of your chosen options, and shrinking one or more tracks beneath the filmstrip or thumbnail minimum quietly folds them into Simple view to keep things tidy.

Adjusting one timeline track’s size by dragging its upper border within the Track Header

### Modifying Timeline Tracks

As you prepare to cut clips into the Timeline, confirm you have enough tracks for the task. The procedures below walk through the various ways to add, remove, and reorder tracks while you work. Every one of these commands lives in the contextual menu that pops up when you right-click anywhere in the Timeline header area (that header is the strip on the left holding each track’s assorted buttons and controls). You may bind Keyboard Shortcuts to track header context menu actions — adding, deleting, moving, recoloring, and linking tracks among them. Track selection is possible from the Track index as well as the Edit and Fairlight timelines. As an illustration, you can bind a keyboard shortcut for adding a new Audio Track on the Edit page by going to Commands > Edit Timeline > Track Controls > Add Track > Audio inside the Keyboard Customization window. Methods for adding, deleting, and rearranging tracks:

- Adding a track to the Timeline: right-click a Track Timeline header and pick Add Track. A fresh video track lands directly above whichever track you right-clicked, while a fresh audio track lands directly below it. When the addition is an audio track, you get to pick the kind of channel mapping it uses.

Audio track channel mappings get fuller treatment in Chapter 45, “Working with Audio in the Edit Page.”

- Adding several tracks to the Timeline at a chosen position: Anywhere within the Timeline header, right-click and pick Add Tracks. Once the Add Tracks dialog opens, set how many video and audio tracks you'd like, pick whether the tracks go in above or below, and pick the Audio Track Type you want when audio tracks are part of the addition. After that, click “Add Tracks.”
- Removing a track from the Timeline: Inside a track's Timeline header, right-click and pick Delete Track. Should the track you take out hold any clips, those clips are removed from the Timeline along with it.
- Clearing every unused track out of the Timeline: Anywhere across the track header area, right-click and pick Delete Empty Tracks. Every track lacking clips is deleted in one go.
- Shifting tracks, plus the clips riding on them, upward and downward: Inside a track's Timeline header, right-click; from the contextual menu, pick either Move Track Up or Move Track Down. That track, together with all of its clips, moves up or down relative to the other tracks in the Timeline. Track order can also be rearranged from the Tracks Index. Just click the track in the # field and drag it to wherever you want it.

The Add Tracks Dialog makes it possible to insert several tracks in one step and position them within the timeline.
