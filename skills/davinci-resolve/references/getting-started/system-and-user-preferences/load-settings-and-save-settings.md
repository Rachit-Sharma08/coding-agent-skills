# Load settings and save settings

Version: DaVinci Resolve 20.3 Reference Manual. Context: System and user preferences.
[Chapter index](INDEX.md) / [Previous section](internet-accounts-and-advanced.md) / [Next section](general-settings-overview.md)
<a id="source-automatic-smart-bins"></a> <a id="source-cache-management"></a> <a id="source-editing"></a> <a id="source-load-settings"></a> <a id="source-media-cache-settings"></a> <a id="source-new-timeline-settings"></a> <a id="source-restoring-a-project-backup-in-the-project-browser"></a> <a id="source-restoring-a-timeline-backup-in-the-media-pool"></a> <a id="source-save-settings"></a>

### Load Settings

By way of the Load Settings preference you steer one key facet of project opening performance: whether or not every timeline inside a given project loads into memory at the moment of opening.

- Load all timelines when opening projects: To sharpen the performance of longer projects holding several timelines, the “Load all timelines when opening projects” checkbox over in the Project Save and Load panel of the User Preferences sits off by default. With this checkbox off, opening a project brings only the last timeline you worked on into memory; the rest stay out of RAM. That quickens the opening of large projects. You may, though, hit brief pauses on opening other timelines inside that project, as each fresh timeline has to load into RAM the moment you open it. Open a truly enormous timeline and a progress bar shows up telling you how long the load will take. A further upside is the smaller memory footprint of each project, which pays off especially while juggling several projects through Dynamic Project Switching.

Switch this on and every timeline loads into RAM, so you'll meet no pauses on opening timelines you haven't opened yet. Projects with many timelines, however, may run slower to open and save.

### Save Settings

The Save settings let you steer how DaVinci Resolve handles automated saving and project backups. Such features can spare you the heartache of work lost to an unexpected problem.

- Live Save: Switched on out of the box, Live Save runs as a quick, progressive, ever-present autosave mechanism that “saves as you go.” Every change across the Cut, Edit, and Fairlight pages gets saved the moment you make it. Every change across the Fusion and Color pages saves on its own when you move to another clip, and also at intervals and unseen in the background as you work, so your work stays saved even where you haven't switched clips in a while.
- Project Backups: Found within the User Preferences, over in the Project Save and Load panel, the Project Backups checkbox — switch it on and DaVinci Resolve writes several backup project files at recurring intervals, by a method akin to a GFS (grandfather father son) backup scheme. This works whether or not Live Save sits on. Each project backup is a full project file, leaving out stills and LUTs. After you've had Project Backups on long enough, whatever saved project backups exist can be pulled back in the Project Manager via the contextual menu that pops up when you right-click a project, by picking Project Backups. Opening a project backup leaves the original project untouched; project backups always open as independent projects.

### Restoring a project backup in the Project Browser

- Timeline Backups: Found within the User Preferences, over in the Project Save and Load panel, the Timeline Backups checkbox — switch it on and DaVinci Resolve writes several backups of a timeline at recurring intervals, by a method akin to a GFS (grandfather-father-son) backup scheme. This works whether or not Live Save sits on.

### Restoring a timeline backup in the Media Pool

Should you wish to roll back to an earlier backup of a timeline, just right-click the timeline in the Media Pool, pick Restore Timeline Backup off the contextual menu, then settle on the backup from the list of options. Backups come arranged by date and time, so locating the particular timeline you want to restore is easy. Restoring a timeline backup leaves your current timeline untouched. Rather, the chosen backup arrives in the Media Pool as a fresh timeline, with the name “Backup” tacked onto it. Project and Timeline backups get saved only once changes have been made to a project. Should DaVinci Resolve sit idle for any stretch, as when your smart watch nudges you to step outside and walk around the block, no further project backups get saved, which keeps DaVinci Resolve from writing over useful backups with needless ones. Three fields let you set how often a fresh backup gets saved, while the fourth lets you pick where the backups land. Both Project and Timeline backups fall under these settings. Perform backups every X minutes: How often a fresh backup gets saved within the last hour you've worked is what this opening field sets. By default a fresh backup gets saved every 10 minutes, yielding six backups inside the last hour. Once an hour of work has gone by, an hourly backup gets saved and the per-minute backups start being dropped, first in and first out. By default that leaves you holding only ever six backups at once, standing for the most recent hour of work. Hourly backups for the past X hours: How many hourly project backups you wish to keep is what this next field sets. By default two hourly backups get kept for the current day. Beyond that count, hourly backups start being dropped, first in and first out. Daily backups for the past X days: Across how many days you wish to keep backups is what this further field sets. The final backup saved on any given day is held as the daily backup for that day, and by default daily backups get kept for two days only. Beyond that count, daily backups start being dropped, first in and first out. Working on a project across a longer stretch, you can always bump this number up. Backup location: Press the Browse button to pick a spot where these backups get saved. By default they land in a “ProjectBackup” directory on your scratch disk, though you could point this at a volume that fits your data backup methodology better. This folder holds both Project and Timeline backups.

### Cache Management

Through this section you can have your local cache deleted on its own after a set number of days, keeping your drive from clogging up with older projects. Naturally, tending these files by hand stays possible through the Playback > Manage Render Cache menu, yet this new preference lets you arrange a cleanup operation and then forget it.

### Media Cache Settings

Delete Cache files older than xx days: Tick the box and pick the number of days past which the automatic deletion of the Cache files happens.

### Editing

What this panel's settings reach into are frame interpolation settings, timeline UI appearance, trim behaviors, editorial default values, plus new timeline settings.

### New Timeline Settings

These settings fix the presets that fill the New Timeline Options window each time you build a new timeline.

- Start Timecode: The Start Timecode can be changed whenever a particular start time is called for.
- No. of Video Tracks: Type in how many video tracks you'd like. You can also drag inside this

field to set the number of video tracks with a virtual slider.

- No. of Audio Tracks: Type in how many audio tracks you'd like. You can also drag inside this

field to set the number of audio tracks with a virtual slider.

- Audio Track Type: Pick the channel mapping you'd like the new audio tracks to adopt.

### Automatic Smart Bins

These settings let DaVinci Resolve build Smart Bins on its own whenever clips bearing relevant metadata land in the Media Pool, or whenever such metadata gets added to clips already sitting in the Media Pool. Through a run of checkboxes you choose which Smart Bins get built automatically.
