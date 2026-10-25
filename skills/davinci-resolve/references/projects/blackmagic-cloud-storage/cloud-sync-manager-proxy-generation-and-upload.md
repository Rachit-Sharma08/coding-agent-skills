# Blackmagic cloud sync manager and automatic proxy generation and upload to blackmagic cloud storage

Version: DaVinci Resolve 20.3 Reference Manual. Context: Blackmagic cloud storage.
[Chapter index](INDEX.md) / [Previous section](media-interface-toolbar-and-viewing-clip-metadata.md)
<a id="source-automatic-proxy-generation-and-upload-to-blackmagic-cloud-storage"></a> <a id="source-blackmagic-cloud-sync-manager"></a> <a id="source-cloud-storage-sync-icons"></a> <a id="source-import-blackmagic-cloud-shared-folders-to-the-media-pool"></a> <a id="source-sync-specific-media-originals-in-proxy-synced-cloud-projects"></a> <a id="source-the-blackmagic-cloud-folder-link-dialog"></a> <a id="source-the-proxy-processing-icon-in-the-upper-left"></a> <a id="source-the-successful-sync-icon-in-the-upper-left"></a> <a id="source-the-upload-queue-icon-in-the-upper-left"></a>

### Blackmagic Cloud Sync Manager

While you have a project open in a cloud library, a handful of the most-used cloud management functions are within reach straight away by clicking the Blackmagic Cloud Sync Manager down in the lower right of the interface. That icon surfaces only while you're working in a cloud library.

The Blackmagic Cloud Sync Manager brings up a spread of handy cloud management tools. Reading the top bar Left to Right, here's what's on hand: Pause/Resume Sync: Halts or restarts how media uploads and downloads from the host computer. Enable/Disable Multi User Collaboration: Brings up a dialog box for flipping between Set to Single User and Allow Multiple Users (collaboration mode). Enable/Disable Camera Capture: Brings up a dialog box for flipping between Allow and Don't Allow, governing whether Blackmagic Camera app users push footage to storage and bring the clips into the project's Media Pool. Open in Finder/File Explorer: Pops open the Project Media Location within the computer's file system. Open Settings: Pops open the Blackmagic Cloud tab inside the Project Settings window. Go to Blackmagic Cloud Storage: Launches your web browser onto the Blackmagic Cloud Storage page out on the internet.

Beneath that toolbar sit two status areas. The upper one names the user signed into the Blackmagic Cloud account along with how much Blackmagic Cloud Storage is spent and how much remains. Its ring display puts the grand total of all media in the outer ring, the share synced locally in the middle ring, and the amount still waiting to upload in the inner ring. The lower one tracks how the media sync is coming along over the internet. Its top display carries the progress bar for the sync status plus how much material is yet to sync. Right below that, the media list calls out the clip syncing right now together with a roll of media already synced.

### Automatic Proxy Generation and Upload to Blackmagic Cloud Storage

While you're on the Media, Cut, Edit and Fairlight pages, DaVinci Resolve is able to spin up proxies on its own in the background to push to Blackmagic Cloud. No matter which page you're on, you can still trigger proxy media generation by hand from the media pool to set uploads going. Switching automatic proxy generation and upload on goes like this: 1 Within the Project Settings, press the Blackmagic Cloud tab. 2 Inside the “For media files” section, press “Sync proxies only.” 3 Tick the “Generate proxies automatically” box. 4 Inside the “Proxies are created as” section, choose the codec you'd like the proxy format rendered into. 5 Press the Save button. Switching automatic proxy generation and upload off goes like this: 1 Within the Project Settings, press the Blackmagic Cloud tab. 2 Inside the “For media files” section, press “Don't sync media.” 3 Clear the “Generate proxies automatically” box. 4 Press the Save button.

### Cloud Storage Sync Icons

Whenever you work inside a cloud library, Sync icons ride at the upper left of a clip in the Media Pool, telling you where each clip stands in the cloud.

### The Proxy Processing icon in the upper left

White Cloud with 3 Dots: Signals that proxy media is in the middle of being processed right now.

### The Upload Queue icon in the upper left

### The Successful Sync icon in the upper left

Yellow Cloud with an Up Arrow: Signals that the clip is waiting its turn in line to head up to the cloud.

White Cloud with a Checkmark: Signals that the clip made it up and synced to the cloud without a hitch.

### Sync Specific Media Originals in Proxy Synced Cloud Projects

Within Blackmagic Cloud projects that sync only proxies up to Blackmagic Cloud, you're able to sync originals for particular files in the Media Pool. That comes in handy when you have to upload or download originals for a few files but not the whole set. Just right-click the Media Pool clips whose originals you want, and pick Sync Original Media from the context menu.

Picking out single media proxies lets you pull down the originals for only those particular clips

### Import Blackmagic Cloud Shared Folders to the Media Pool

You're now able to import and sync Blackmagic Cloud Folders straight into the Media Pool. This lets you hook up to one or several cloud media folders and pull media down from them to your local machine on a pick-and-choose basis. Blackmagic Cloud Folders are shared online storage folders with no tie to any single project. That lets you assemble a stockpile of frequently reused media assets — title sequences, credits, bumpers and so on — and pass them around online instead of importing them one by one into every separate project.

The Import Cloud Folder icon sitting atop the Media Pool Tying a Blackmagic Cloud Folder to your project goes like this: 1 Sign into your Blackmagic Cloud account from within DaVinci Resolve. 2 On any page, press the Import Blackmagic Cloud Folder icon up at the top of the Media Pool. 3 Within the Blackmagic Cloud Folder dialog, press select to pick a Blackmagic Cloud Folder. What shows up here is every Blackmagic Cloud Folder you've built yourself or that another person has shared your way. Press the Add button. 4 Under Download Folder Location, point to a spot on your local system where the media out of the Blackmagic Cloud Folder should land. 5 Decide whether you'd rather sync proxies alone, or proxies plus used originals. 6 Hit Download to fold the Cloud Folder into your Media Pool.

### The Blackmagic Cloud Folder link dialog

When you first open the Blackmagic Cloud Folder in the Media Pool, it starts out empty and fills in a clip at a time as the clip names (rather than the media itself) arrive from the cloud. On top of that, the Blackmagic Cloud Folder isn't truly tied to your project yet; the link forms only once the first media clip gets “used.” The term “used” clip is fresh terminology in DaVinci Resolve, meaning nothing more than a clip that's been changed in some fashion within the project. Dropping a clip on a timeline counts as using it, of course, but so do other moves like flagging it, editing its metadata, transcribing it, and similar. As soon as a clip is used, its media begins downloading to your local machine. A red dot beside a clip in the Media Pool marks the ones that are used. Whatever clips go unused stay on as virtual clips inside the Cloud Folder until they're used. After they download, clips in Cloud Folders behave just like any other clip in the Media Pool.

The Cloud Folder shown linked in List view. A red dot marks the “used” clips, whose original media has come down already. Clips left unused offer only their proxies for viewing. Over in the Cloud Sync column, you can confirm the media is registered and in sync with the Blackmagic Cloud.
