# Import blackmagic cloud shared folders to media pool and blackmagic cloud folder link dialog

Version: DaVinci Resolve 20.3 Reference Manual. Context: Importing and organizing media in the cut page.
[Chapter index](INDEX.md) / [Previous section](bin-timeline-import-and-folder-sync.md) / [Next section](filmstrip-view-mode-and-list-view.md)
<a id="source-import-blackmagic-cloud-shared-folders-to-media-pool"></a> <a id="source-media-pool-views"></a> <a id="source-metadata-view"></a> <a id="source-the-blackmagic-cloud-folder-link-dialog"></a> <a id="source-the-icon-view-mode"></a> <a id="source-the-media-sort-options"></a> <a id="source-the-metadata-view-with-clips-sorted-by-scene-shot-take"></a> <a id="source-the-view-mode-buttons"></a> <a id="source-thumbnail-view"></a>

### Import Blackmagic Cloud Shared Folders to Media Pool

Blackmagic Cloud Folders can now be imported and synced into the Media Pool. That lets you

hook up to one or more cloud media folders and pull media down from them selectively to your

local machine. Blackmagic Cloud Folders are online shared storage folders not bound to any

one project. With them you can build a pool of media assets you reach for often, such as title sequences,

credits, bumpers, and so on, and share those online instead of importing them one by one into each

separate project.

The Import Cloud Folder icon at the top of the Media Pool Linking a Blackmagic Cloud Folder to your project goes like this: 1 Within DaVinci Resolve, log into your Blackmagic Cloud account. 2 On any page, click the Import Blackmagic Cloud Folder icon atop the Media Pool. 3 Inside the Blackmagic Cloud Folder dialog, click select to pick a Blackmagic Cloud Folder. What you see listed here are any Blackmagic Cloud Folder you've made or that someone else has shared your way. Click the Add button. 4 Under Download Folder Location, pick a spot on your local system where you'd like the media from the Blackmagic Cloud Folder kept. 5 Decide whether to sync proxies alone, or proxies plus used originals. 6 Hit Download to bring the Cloud Folder into your Media Pool.

### The Blackmagic Cloud Folder link dialog

Open the Blackmagic Cloud Folder in the Media Pool and it starts out empty, filling one clip at a time as their clip names (not their media) come down from the cloud. The Blackmagic Cloud Folder also isn't truly tied to your project yet; the link only forms once the first media clip gets “used.” A “used” clip is fresh terminology in DaVinci Resolve and simply refers to a clip that's been changed in some way inside the project. Dropping a clip onto a timeline certainly counts as using it, but so do other actions—flagging it, editing its metadata, transcribing it, and the like. The moment a clip is used, its media begins downloading to your local machine. Used clips are marked by a red dot beside them in the Media Pool. Any clip left unused stays a virtual clip in the Cloud Folder until that changes. After download, clips in Cloud Folders behave just like every other clip in the Media Pool.

The Cloud Folder linked in List view. A red dot marks a “used” clip whose original media has come down. Clips left unused offer only their proxies for viewing. The Cloud Sync column indicates the media is registered and kept in sync with the Blackmagic Cloud.

### Media Pool Views

After you've brought some clips into the Media Pool, three controls over at the upper-right let you steer how they appear, according to what you're trying to do.

### The View Mode buttons

### Metadata View

Under the Metadata view mode, every clip gets its own card carrying a thumbnail plus basic clip metadata on display. This view aims to surface more metadata than a thumbnail does, yet more focused information than the List view. Paired with its sort modes, this feature gives you a strong way to organize and rearrange your clips in the Media Pool. The Metadata view's metadata fields, running top to bottom:

- Thumbnail: A scrubbable thumbnail image of your clip.
- Row 1: A main description field whose content shifts depending on which sort order you've selected.
- Row 2: Start Timecode, Date Created, Camera #.
- Row 3: Scene, Shot, Take.
- Row 4: Clip Name, Comment.

What makes the Metadata view shine is how it automatically clusters your clips in the Source Tape according to the sort order you set in the Media Pool Sort By menu at the Media Pool's far upper-right corner. Those same sort options are available in the Thumbnail, List, and Filmstrip views too.

The Metadata View icon view (its icon lit up in the top bar), with the thumbnail shown mid-scrub alongside the clip’s metadata

### The Media Sort options

The sort modes you can pick within the Metadata view are:

- Timecode: Groups clips according to creation date, sets the main description field to creation date plus start timecode, and arranges the list by timecode.
- Camera: Groups clips according to Camera #, sets the main description field to camera # plus start timecode, and arranges the list by timecode.
- Date Time: Groups clips by day, sets the main description field to creation date plus file name, and arranges the list by timecode.
- Clip Name: Groups clips by the opening letter of the clip name alphabetically, sets the main description field to clip name, and arranges the list by timecode.
- Bin: Groups clips according to bin, sets the main description field to clip name, and arranges the list by timecode.
- Scene, Shot: Groups clips according to scene, sets the main description field to sceneshot-take, and arranges the list by scene-shot-take.
- Clip Color: Groups clips according to clip color name, sets the main description field to creation date plus start timecode, and arranges the list by timecode.
- Date Modified: Groups clips by day, sets the main description field to creation date plus file name, and arranges the list by when the OS filesystem last modified the clip.
- Date Imported: Groups clips by day, sets the main description field to creation date plus file name, and arranges the list by the date the clip joined the Media Pool.
- Online Status: Groups clips according to proxy or original status.
- Ascending: Arranges the Media Pool running from the lowest numerical value up to the highest, and alphabetically

from A to Z.

- Descending: Arranges the Media Pool running from the highest numerical value down to the lowest, and alphabetically

from Z to A. Each sort mode swaps out the card's main description field and reorders the Source Tape to match the organization method you've picked.

### The Metadata view with clips sorted by Scene-Shot-Take

The Metadata view with the same clips sorted by Camera

### Thumbnail View

A scrubbable thumbnail stands in for each clip. Hover the playhead across a thumbnail and slide it left and right to watch the clip's image play, and tap the I and O keys to flag the stretches of a clip you'd like to use. You can switch hover scrub on and off from the Media Pool option menu over on the Edit page.

### The Icon View mode

A filmstrip of back-to-back frames running the Media Pool's length stands in for each clip. Hover the playhead over the clip and slide it left and right to watch the clip's image play, and tap the I and O keys to flag the stretches of a clip you'd like to use.
