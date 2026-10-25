# Disconnecting and deleting project libraries and quick access to recent projects from the file menu

Version: DaVinci Resolve 20.3 Reference Manual. Context: Managing projects and project libraries.
[Chapter index](INDEX.md) / [Previous section](project-library-duplicate-backup-and-restore.md) / [Next section](project-notes-and-dynamic-project-switching.md)
<a id="source-auto-save-controls-in-the-user-preferences"></a> <a id="source-disconnecting-and-deleting-project-libraries"></a> <a id="source-live-save"></a> <a id="source-opening-a-recent-project-from-the-file-menu"></a> <a id="source-project-backups"></a> <a id="source-quick-access-to-recent-projects-from-the-file-menu"></a> <a id="source-restoring-a-project-backup-in-the-project-browser"></a> <a id="source-restoring-a-timeline-backup-in-the-media-pool"></a> <a id="source-restoring-deleted-timeline-backups"></a> <a id="source-saving-projects"></a> <a id="source-selecting-a-backup-that-you-want-to-restore"></a> <a id="source-timeline-backups"></a>

### Disconnecting and Deleting Project Libraries

DaVinci Resolve won't actually let you delete project libraries; all you can do is disconnect them so they drop off the Project Library list. That said, a disconnected project library can be reconnected later as long as you recall its name. Wiping out a project library entry in PostgreSQL completely is only possible from the command line, or through the PGAdmin III application that ships with the PostgreSQL installation bundled into the DaVinci Resolve installation process. When a project library has outlived its usefulness, disconnect it like so:

- Right-click a project library that isn't presently selected and pick Remove off the contextual menu. A dialog pops up asking you to confirm you really mean to disconnect that project library. Press Disconnect to go ahead.

Locating Local Project Library Directories in Your File System Since each local project library ties to a particular directory on your file system, there's a means of tracking that directory down. To locate a project library on your system:

- Right-click any local project library and pick "Reveal in Finder." A file system window opens to reveal where that local project library lives, with all its projects sitting inside.

### Quick Access to Recent Projects from the File Menu

Recent projects can be opened straight from the File > Open Recent Project menu, sparing you a trip to the Project Manager to hunt one down by hand.

### Opening a recent project from the File menu

### Saving Projects

After a project is created and open, you'll want to be sure you save your work on a regular basis. Methods of saving projects:

- Choose File > Save Project (Command-S).
- To keep the project's present state as a fresh copy under a new name, choose File > Save Project As (Command-Shift-S), then type a name into the Save Current Project window and click Save. Should you reuse the name of a project that already exists, a dialog box surfaces and lets you confirm whether to overwrite that existing project or back out and pick a different name.
- Media Location: If you like, you can switch the disk or location where every piece of DaVinci Resolve generated media in the project gets written. This has no bearing on where your original source material lives (such as video and audio clips); it only governs where media made within DaVinci Resolve itself (such as fresh audio files from Voice Convert, or recordings from the Voice Over tool) ends up.

To revert to the last saved state of a project:

- When you'd rather not save and instead want to roll back to the project's last saved state, choose File > Revert to Last Save.

While you work on a project, the word "Edited" shows up to the right of the project name atop the DaVinci Resolve UI to signal you've got unsaved changes. Go past 15 minutes without saving and the word "Edited" goes yellow; go past 30 minutes still unsaved and it turns red, a hint that you really ought to save. Hover the pointer over the word "Edited" and a tooltip tells you when the most recent save happened.

Sitting to the right of the project name, the word "Edited" flags that changes remain unsaved DaVinci Resolve also offers two auto save features you can switch on within the Save Settings group of controls, named Live Save and Project Backups.

### Auto Save controls in the User Preferences

### Live Save

Switching Live Save on tells DaVinci Resolve to save your edits incrementally as you change the project, with no action needed from you. Switch Live Save off and DaVinci Resolve returns to a mode where saving is manual via Command-S (handy during demos when you'd rather not commit changes to a project). Live Save ships on by default and is strongly advised to guard against losing work should trouble strike. It even covers previously unsaved projects you forgot to save, if anything goes wrong. NOTE: Whenever you turn to Collaborative Workflow so several artists can share one project, Live Save switches on automatically and can't be turned off.

### Project Backups

Over in the User Preferences, ticking the Project Backups checkbox within its Project Save and Load panel lets DaVinci Resolve write several backup project files at set intervals, following a scheme akin to a GFS (grandfather father son) backup approach. You can do this whether or not Live Save is on. Every project backup written is a full project file, minus stills and LUTs, which are left out to conserve storage space. After Project Backups has run a while, the saved project backups it has produced can be pulled up in the Project Manager through the contextual menu that appears on right-clicking a project, by selecting Project Backups to bring up the backups list dialog. The backups list dialog lays out every backup on hand for a given project and provides controls for sorting the list by various columns, removing some or all backups in it, and loading the backups you'd like to retrieve. Opening a project backup leaves the original project untouched; project backups always open as standalone projects. To enable Project Backups: 1 Choose DaVinci Resolve > Preferences > User, then open the Project Save and Load panel. 2 Tick the Project Backups checkbox. 3 Pick the settings governing how many Project Backups get kept. Project Backups follow a first in, first out order. Three fields let you set how frequently fresh backups are written and how many are kept, and the fourth lets you pick where the backups go. Perform backups every X minutes: The first field sets how frequently a fresh backup is written inside the most recent hour of work. By default, a fresh backup lands every 10 minutes, giving six backups across the last hour. After a full hour of work elapses, an hourly backup is written and the per-minute ones start dropping off on a "first in, first out" basis." By default this leaves you with only ever six backups at once, covering the latest hour's work. Hourly backups for the past X hours: The second field sets how many hourly backups you'd like kept. By default, 8 hourly backups are kept for the day you're currently working, on the assumption of an eight hour day (wouldn't that be nice). Beyond that count, hourly backups start dropping off on a "first in, first out" basis.

Daily backups for the past X days: The third field sets how many days' worth of backups you'd like kept. Whatever project backup is written last on a given day becomes that day's daily backup, and by default daily backups stick around for only five days (not necessarily back to back, if you take some days off from editing during the week). Beyond that count, daily backups start dropping off on a "first in, first out" basis. Working on a project across a longer span? You can always bump this number up. Project backup location: Press the Browse button to pick where these project backups get written. By default they land in a "ProjectBackup" directory on your scratch disk, though you could point this at a volume that suits your data backup methodology better. 4 Press Save to lock in your change, then close the Preferences window. NOTE: With this feature on, the very first backup written on a given day might run a touch slow, but every backup after that should go unnoticed. After one or more Project Backups exist, you can reach them from the Project Browser. Opening a saved Project Backup runs like this: 1 Open the Project Manager. 2 Right-click a project; pick Project Backups off the contextual menu. 3 Pick a backup to restore out of the Auto Backups list. If the exact backup you're after isn't showing, press the Refresh button to refresh the list, or sort by one of the columns (Auto Backup, Date Modified, Width, Height) to work through it more easily. 4 With your chosen backup selected, press Load to open it as a fresh project. If the project it came from is already open, it stays unaffected.

### Restoring a project backup in the Project Browser

### Selecting a backup that you want to restore

### Timeline Backups

Over in the User Preferences, ticking the Timeline Backups checkbox within its Project Save and Load panel lets DaVinci Resolve write several backups of a timeline at set intervals, following a scheme akin to a GFS (grandfather-father-son) backup approach. You can do this whether or not Live Save is on. To roll back to an earlier backup of a timeline, just right-click the timeline in the Media Pool, pick Restore Timeline Backup off the contextual menu, and select the backup from the list shown. Backups are sorted by date and time, so pinpointing the exact timeline you want to restore is easy. At certain points during editing it pays to make a backup point by hand before you overhaul the rest of your timeline. You might do this by duplicating the timeline (usually the safest route), or you can set a backup point by hand for recall alongside your other timeline backups. To lay down a custom-named backup point on a timeline by hand, take either route:

- Select File > Create Timeline Backup (Option-Command-S).
- Right-click your timeline within the Media Pool and pick Create Timeline Backup off the context menu.

Restoring a timeline backup leaves your current timeline as is. Rather, the chosen backup arrives in the Media Pool as a fresh timeline, carrying the name "Backup" tacked onto it.

### Restoring a timeline backup in the Media Pool

Setup and Workflows — Timeline Backups — Managing Projects and Project Libraries section.

Timeline backups get written only once a project has actually changed. When DaVinci Resolve sits idle a while — say your smart watch nudges you to step outside and stroll around the block — no further project backups are written, which keeps DaVinci Resolve from trading useful backups for needless ones. Three fields let you set how frequently a fresh backup is written, and the fourth lets you pick where the backups go. These settings govern both Project and Timeline backups.

- Perform backups every X minutes: The first field sets how frequently a fresh backup is written inside the most recent hour of work. By default, a fresh backup lands every 10 minutes, giving six backups across the last hour. After a full hour of work elapses, an hourly backup is written and the per-minute ones start dropping off on a first in, first out basis. By default this leaves you with only ever six backups at once, covering the latest hour's work.
- Hourly backups for the past X hours: The second field sets how many hourly project backups you'd like kept. By default, two hourly backups are kept for the current day. Beyond that count, hourly backups start dropping off on a first in, first out basis.
- Daily backups for the past X days: The third field sets how many days' worth of backups you'd like kept. Whatever backup is written last on a given day becomes that day's daily backup, and by default daily backups stick around for only two days. Beyond that count, daily backups start dropping off on a first in, first out basis. Working on a project across a longer span? You can always bump this number up.
- Project backup location: Press the Browse button to pick where these backups get written. By default they land in a "ProjectBackup" directory on your scratch disk, though you could point this at a volume that suits your data backup methodology better. This folder holds both Project and Timeline backups.

### Restoring Deleted Timeline Backups

Off the Media Pool Options menu you can pick Deleted Timeline Backups and review deleted timelines together with the backup files on hand for each one. From there you can mark backups for restoring or opt to permanently remove the ones you select.
