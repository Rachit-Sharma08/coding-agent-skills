# Adding media with offset timecode and import blackmagic cloud shared folders to media pool

Version: DaVinci Resolve 20.3 Reference Manual. Context: Adding and organizing media with the media pool.
[Chapter index](INDEX.md) / [Previous section](clone-tool-media-copy-jobs.md) / [Next section](adding-media-to-the-cut-edit-fusion-and-fairlight-pages.md)
<a id="source-adding-media-with-offset-timecode"></a> <a id="source-import-blackmagic-cloud-shared-folders-to-media-pool"></a> <a id="source-sync-media-pool-bins-with-file-system-folders"></a> <a id="source-the-blackmagic-cloud-folder-link-dialog"></a>

### Adding Media With Offset Timecode

Now and then source media ends up with wrongly offset timecode because of slip-ups made earlier in postproduction. When that offset stays consistent, the "Add Folder with Source Offset" command lets you bring media into the Media Pool as clips carrying a timecode offset. To bring a folder of clips into the Media Pool with offset timecode: 1 Within the Media Storage panel, right-click a directory and pick one of these commands:

- Add Folder with Source Offset
- Add Folder and SubFolders with Source Offset 2 In the "Change Frame Offset" dialog, pick how many frames the timecode should be offset by and press Apply.

The media enters the Media Pool as clips bearing offset timecode. The original source timecode of the clips on disk, however, stays unchanged. Any media you render from the Deliver page will carry the offset timecode.

### Import Blackmagic Cloud Shared Folders to Media Pool

Importing and syncing Blackmagic Cloud Folders into the Media Pool is now possible. Through this you can connect to one or more cloud media folders and pick and choose which media to pull down onto your local machine. Blackmagic Cloud Folders are shared online storage folders not bound to any one project. That lets you assemble a pool of frequently used media assets — title sequences, credits, bumpers, and so on — and share them online without importing them one by one into each separate project.

The Import Cloud Folder icon up at the Media Pool's top To attach a Blackmagic Cloud Folder onto your project: 1 Within DaVinci Resolve, sign into your Blackmagic Cloud account. 2 On any page, click the Import Blackmagic Cloud Folder icon up at the top of the Media Pool. 3 In the Blackmagic Cloud Folder dialog, click select to pick a Blackmagic Cloud Folder. The options shown here list any Blackmagic Cloud Folder you've created or that someone else has shared with you. Click the Add button. 4 Under Download Folder Location, pick a spot on your local system where the media from the Blackmagic Cloud Folder should be stored. 5 Decide whether to sync proxies alone or proxies plus used originals. 6 Press Download to bring the Cloud Folder into your Media Pool.

### The Blackmagic Cloud Folder link dialog

Opening the Blackmagic Cloud Folder in the Media Pool, you'll find it empty, filling one clip at a time as the clip names (not the media itself) come down from the cloud. What's more, the Blackmagic Cloud Folder isn't truly tied to your project yet; that link forms only once the first media clip gets "used." A "used" clip is fresh terminology in DaVinci Resolve, simply meaning a clip that's been changed in some way within the project. Sure, a clip counts as used when you drop it on a timeline, but other acts qualify too — flagging it, editing its metadata, transcribing it, and the like. As soon as a clip is used, its media begins downloading onto your local machine. Used clips are marked by a red dot beside them in the Media Pool. Clips left unused stay on as virtual clips in the Cloud Folder until they're used. After downloading, Cloud Folder clips work just like any other clip in the Media Pool.

The Cloud Folder shown linked in List view. Clips bearing red dots are "used," their original media downloaded. Unused clips offer only their proxies to view. The Cloud Sync column confirms the media is registered and in sync with the Blackmagic Cloud.

### Sync Media Pool Bins with File System Folders

A Media Pool bin can be kept in sync with a folder living on your computer's file system (MacOS, Windows, Linux, and the like). That way you can drop extra media into a folder on your computer and have it import to the matching bin in DaVinci Resolve by itself. To set up a folder for Automatic Syncing: 1 Over on the Cut page, use the top menu bar's Import Folder icon to establish matching folder and sub folder names. 2 Right-click the imported folder and pick "Automatically Resync Media Files."

Use the Import Media Folder icon in the Cut page

Right-click on the bin and select Automatically Resync Media Files

Fresh clips dropped into this folder join the media bin on their own. This proves handy with cloud-synced media files (such as when you're using DaVinci Resolve's Replay capabilities), or with any files that might get added to the folder down the line. To resync a Media Pool bin's contents once by hand, right-click a bin and pick "Resync Media Files."

Right-click the bin and choose Resync Media Files to run the sync by hand.

For both Resync actions, ensure that:

- At least one clip sits in the media bin.
- Every clip already in the media bin shares one common file path.
- The media bin's name matches the parent folder of the clip paths. To get this set up properly, rely on the Cut page's "Import Media Folder" command, or else the Media page's "Add Folder and SubFolders into Media Pool (Create Bins)" command.

A sync action pulls in new clips from sub-folders provided the matching sub-bins exist. Sub-folders newly created without matching media bins, though, go untracked, and new media bins lacking matching sub-folders get passed over. Picture, for instance, editing a sporting event where a graphics operator is building animated lower-thirds for each player. Set up a shared network folder named "CG" and sync it automatically in DaVinci Resolve, and every time a new lower-third is finished and saved it would show up in your Media Pool bin on its own, ready to use. Here's the way you'd set this up:

- Make a folder named "CG" on your network storage. The editor and the graphics operator both need access to this folder.
- Bear in mind that since this folder is empty for now, it can't take part in a Resync action yet. Only once the folder holds at least one media file can you run a Resync.
- The graphics operator wraps up his first animated lower third and saves it into the "CG" folder as a .mov file (though any media format DaVinci Resolve can read would do).
- The editor next brings the "CG" folder into the Media Pool in DaVinci Resolve and chooses Automatically Resync Media Files from the context menu.
- As the graphics operator wraps up and saves more lower thirds into that folder, they surface in the Editor's "CG" bin in the Media Pool on their own, with no need to import them specifically.
- To stay organized, the graphics operator then makes a new folder inside "CG" for the other team, named "Team B." Regrettably, since that folder structure wasn't part of the originally imported bin, it doesn't appear in the editor's media pool. Had they made this Team B folder before the editor imported, with media inside it, it would have been there.
- Here, then, the editor merely imports that same bin once more, chooses Automatically Resync Media Files, and the new folder along with all its media shows up as expected. Anything dropped into "Team B" afterward will surface in the editor's media pool.

IMPORTANT: Media entries for clips that get removed or can't be found on the file system are marked as offline media. This keeps the metadata around and comes in handy when the clip path is temporarily offline, sits on cloud storage where file status may be shifting, or has been moved aside by apps or workflows looking to write a new version in its place.
