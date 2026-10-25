# Bin timeline import and folder sync

Version: DaVinci Resolve 20.3 Reference Manual. Context: Importing and organizing media in the cut page.
[Chapter index](INDEX.md) / [Previous section](importing-media-and-import-media-and-import-folder-buttons.md) / [Next section](blackmagic-cloud-shared-folder-import.md)
<a id="source-import-and-export-individual-davinci-resolve-timelines"></a> <a id="source-import-and-export-specific-davinci-resolve-project-bins"></a> <a id="source-sync-media-pool-bins-with-file-system-folders"></a>

### Import and Export Specific DaVinci Resolve Project Bins

Specific bins can be imported and exported between one DaVinci Resolve project and another, which lets you hand bins off rapidly among projects and workstations that reach the same media. The clips in a bin carry along all Metadata, In/Out points, Timelines, and so on, yet none of the actual media files travel with them. To export bins from the Media Pool: 1 Pick one or several bins in the Media Pool. 2 Right-click your selection and pick “Export Bin,” or go to File > Export > Export Bin. 3 In the file system dialog, decide where to save the DaVinci Resolve Bin file (.drb), then click Save.

To import bins into the Media Pool: 1 Right-click inside the Media Pool and pick “Import Bin,” or go to File > Import > Import Bin. 2 Do one of the following:

- Choose a DaVinci Resolve Bin file (.drb) from the file system dialog.
- Double click the .drb file in your file system.

That bin—or bins—then shows up in the Media Pool. Anything imported this route gets the word “import” tacked onto its name so duplicate names are avoided. Import a bin holding clips that already sit in the Media Pool, and those would-be duplicates are left out of the import and instead relinked to the media your project references. That keeps your Media Pool tidy. That said, where the bin or bins have moved to a different computer, relinking offline media may fall to you.

### Import and Export Individual DaVinci Resolve Timelines

Individual timelines can be exported and imported from one DaVinci Resolve project into another, already existing DaVinci Resolve project, which lets you hand timelines off rapidly among projects and workstations without generating extra imported project files. Only the timeline plus its related clip information gets exported; none of the actual media files come along.

To export a timeline from the Media Pool:

1 Pick a timeline from the Media Pool.

2 Choose File > Export > Export AAF, XML, DRT (Shift-Command-O).

3 In the file system dialog, set the format options drop-down to “DaVinci Resolve Timeline Files (\*.drt).”

4 In the file system dialog, decide where to save the DaVinci Resolve Timeline file (.drt), then click Save.

To import a timeline into the Media Pool: 1 In the Media Pool, pick the bin where you'd like the imported timeline kept. 2 Do one of the following:

- Go to File > Import Timeline > Import AAF, XML, DRT (Shift-Command-I); next, in the file system dialog, pick a DaVinci Resolve Timeline file (.drt) and click Open.
- Double click the .drt file in your file system.

The timeline then surfaces in the Media Pool together with every clip tied to it. Anything imported this route gets the word “import” tacked onto its name so duplicate names are avoided. That imported timeline is automatically conformed to whatever matching media already sits in the Media Pool. That said, where the timeline has moved to a different computer, you may have to reimport or relink missing or offline media to bring the imported timeline fully online.

NOTE: This method handles just one timeline per import or export. Where you need several timelines moved at once, fall back on the Import/Export Bin function covered above.

### Sync Media Pool Bins with File System Folders

A Media Pool bin can now be synced to a folder on your computer's file system (MacOS, Windows, Linux, and so on). With that, dropping more media into a folder on your computer makes it import on its own to the matching DaVinci Resolve bin. Setting up a folder for Automatic Syncing goes like this: 1 Over on the Cut page, use the Import Folder icon up on the top menu bar to line up matching folder and sub-folder names.

Use the Import Media Folder icon in the Cut page 2 Give the imported folder a right-click and pick ”Automatically Resync Media Files.“

Right-click on the bin and select Automatically Resync Media Files Whatever clips you add fresh to this folder get pulled into the media bin on their own. That helps when you're dealing with cloud-synced media files (as you are when using DaVinci Resolve's Replay capabilities), or any files that might land in the folder down the road. For a one-time manual resync of a Media Pool bin's contents, right-click a bin and pick ”Resync Media Files.”

Right-click on the bin and select Resync Media Files to carry out the sync by hand.

For both Resync actions, ensure that:

- At least one clip is present in the media bin.
- All existing clips in the media bin share the same file path.
- The media bin's name lines up with the parent folder of the clip paths. To be sure this is configured right, lean on the Cut page's “Import Media Folder,” or instead reach for “Add Folder and SubFolders into Media Pool (Create Bins)” over on the Media page.

Sync actions pull in new clips out of sub-folders wherever the matching sub-bins are present. Even so, freshly

made sub-folders that lack matching media bins go untracked, and new media bins that lack

their matching sub-folders are passed over.

Imagine, for instance, that you're cutting a sporting event while a graphics operator builds animated lower-thirds for every player. Set up a shared network folder called “CG” and have DaVinci Resolve sync it automatically, and each freshly finished, saved lower-third would surface on its own in your bin in the Media Pool, ready to use.

Here’s how you would set this up:

- On your network storage, make a folder named “CG.” Both the editor and the graphics operator must be able to reach this folder.
- Keep in mind that since this folder is empty right now, it isn't eligible for a Resync action yet. A Resync becomes possible only once the folder holds at least one media file.
- The graphics operator wraps up his first animated lower third and saves it into the “CG” folder as a .mov file (though any media format DaVinci Resolve can read would do).
- Next the editor brings the “CG” folder into the Media Pool within DaVinci Resolve and picks Automatically Resync Media Files off the context menu.
- Each time the graphics operator wraps and saves more lower thirds into that folder, they surface on their own in the Editor's “CG” bin in the Media Pool, with no need to import them specifically.
- For tidiness, the graphics operator then makes a fresh folder within “CG” for the other team, naming it “Team B.” Unfortunately, since that folder structure wasn't part of the originally imported bin, it stays absent from the editor's media pool. Had they instead built this Team B folder ahead of the editor's import, with media inside it, it would have shown up.
- In that case, the editor just imports the same bin once more, picks Automatically Resync Media Files, and the new folder along with all its media shows up as expected. Anything further dropped into “Team B” thereafter will turn up in the editor's media pool.

IMPORTANT: Whenever a clip is removed or can't be located on the file system, its media entry gets flagged as offline media. That preserves the metadata and proves handy when a clip path is offline for the moment, sits on cloud storage where file status keeps shifting, or has been moved aside by apps or workflows aiming to write a fresh version in its spot.
