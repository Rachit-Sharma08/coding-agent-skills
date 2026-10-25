# Media interface toolbar and viewing clip metadata

Version: DaVinci Resolve 20.3 Reference Manual. Context: Blackmagic cloud storage.
[Chapter index](INDEX.md) / [Previous section](blackmagic-cloud-storage-interface-and-web-app.md) / [Next section](cloud-sync-manager-proxy-generation-and-upload.md)
<a id="source-cloud-folders"></a> <a id="source-personal-storage-folders"></a> <a id="source-setting-up-a-blackmagic-cloud-project-in-davinci-resolve"></a> <a id="source-the-cloud-folders-section-of-cloud-storage"></a> <a id="source-the-media-interface-toolbar"></a> <a id="source-viewing-clip-metadata"></a>

### The Media Interface toolbar

- Storage Space Panel: Pressing this icon flips the left Storage Spaces panel into view or out of it.
- Navigate Up one Level: Pressing the “<“ icon walks you one step higher within the file hierarchy.
- Navigate File Hierarchy : Lays out the file path within your project as a drop-down menu, so you

can leap straight to particular enclosing folders.

- Search: Lets you hunt down clips by their file name.
- Sort: Lets you arrange the clips on screen by name, size, modified and created times, plus

kind — running either ascending or descending.

- List View: Shows the clips in List view.
- Thumbnail View: Shows the clips in Thumbnail view.
- New Folder: Creates a new bin in the Project.
- Information: Shows the metadata associated with the clip.
- Option Menu: Shows media operations; currently these are:

Download: Pulls a chosen clip, or several, down from the cloud storage onto your computer. Delete: Removes folders or clips out of a project. There's no undoing this action.

Park the pointer above the thumbnail, then glide the mouse one way or the other to scrub the clip Scrubbing Video Clips Resting your pointer over a clip's thumbnail lets you scrub the clip both directions to take in its whole stretch of media. Just rest over the clip and drag the red line left and right across it with your mouse. Selecting Multiple Clips Picking several clips for an operation in the Media Interface works precisely the way it does in DaVinci Resolve. A blue outline ringing the chosen clips, plus an on-screen note along the bottom, tells you which clips are selected and how many.

- Selecting a Range of Clips: Shift-click, or drag a bounding box across whichever clips you mean to grab.
- Selecting Individual Clips: Command-click whichever clips you mean to grab.

### Viewing Clip Metadata

With the Information icon active in the toolbar, a clip's metadata shows up to the right of the Media Interface. You can read this metadata in the Blackmagic Cloud Storage web app, though you can't change it there. Editing a clip's metadata has to happen from the File inspector in DaVinci Resolve.

Choosing the Info icon on the Media Interface toolbar surfaces a clip's metadata for reading, though not for editing.

### Cloud Folders

Cloud Folders are shared online storage folders with no link to any single project. That lets you build up a stockpile of frequently reused media assets — music, title sequences, credits, and the like — and pass them around online rather than importing them one by one into every separate project.

### The Cloud Folders section of Cloud Storage

Making a fresh cloud folder goes like this: 1 Within the Storage Space type drop-down, pick Cloud Folders. 2 Press the Create Cloud Folder icon, sitting just to the right of the Storage Space drop-down. 3 Give the new Cloud Folder a name. 4 Drop in whatever media you'd like the folder to share. Sharing that cloud folder goes like this: 1 Over in the Cloud Folders interface, press the “i” information icon up in the toolbar's top right. 2 Open the Sharing tab. 3 Press the Sharing Settings button down at the foot of the tab. 4 Type in the user email addresses of whichever Blackmagic Accounts you'd like as recipients. 5 Press Save. Those users get a notification that the shared folder is now theirs to reach, and they can open it in DaVinci Resolve by hitting the “Import Blackmagic Cloud Folder” icon over in the Media Pool, covered later on in this chapter.

### Personal Storage Folders

You're also free to set up personal media storage folders that only your account can reach — not shared with anyone else and not bound to any single project. At the time of writing, personal folders live only in the web interface and have no tie-in with DaVinci Resolve. Making a fresh personal folder goes like this: 1 Within the Storage Space type drop-down, pick Personal Folders. 2 Press the Create Cloud Folder icon, sitting just to the right of the Storage Space drop-down. 3 Give the new Personal Folder a name. 4 Drop whatever media you'd like into the folder.

### Setting up a Blackmagic Cloud Project in DaVinci Resolve

Standing up a project built on Blackmagic Cloud became smoother and simpler with 18.6, which lets you settle every configuration option — Blackmagic Cloud Storage among them — on one no-fuss setup screen. NOTE: Before Blackmagic Cloud will work for you, register a Blackmagic Cloud account over at cloud.blackmagicdesign.com, after which you sign into that account from within DaVinci Resolve. Standing up a new Cloud Project goes like this: 1. Inside DaVinci Resolve's Project Manager, choose Cloud out of the Project Library options over in the top left. Your Blackmagic Cloud Library ought to be live (lit up in orange). 2. Press the New Project button, or right-click the background and choose New Project off the contextual menu. Alternatively, bring in a local DaVinci Resolve project you already have and want folded into the Blackmagic Cloud. 3. Set whatever options suit you in the Create New Cloud Project dialog. 4. Press the Create button.

Select Remove Unused Clips from the Media Pool optwion menu

Through the Create New Cloud Project dialog box you settle where your project's media lives and how it gets shared.

- Name Your Project: Key in a name for your Cloud Project.
- Choose a Location for your Project Media: Pick a spot on your file system to hold the imported

media files, graphics, and audio files you plan to draw on for the project.

- Share Project with Multiple Users?: Lets you decide whether this project gets shared out to

other users. Allow Multiple Simultaneous Users: Turns on collaboration mode so several people can work the same project at once. Set Project to Single User: Switches collaboration mode off, built for a lone person on the project at any given time.

- Synchronize Storage with Blackmagic Cloud?: Through these options you decide which media gets uploaded and synced to your Blackmagic Cloud Storage account so other users can reach it.

Don't Sync Media: Sends no media at all up to Blackmagic Cloud Storage. Sync Proxies Only: Pushes only proxy media to Blackmagic Cloud Storage. Sync Proxies and Originals: Pushes the proxies together with the original media to Blackmagic Cloud Storage. Depending on how much original media there is and how big it runs, this can eat a huge quantity of storage.

- Allow Remote Camera Access: Governs the access rights granted to people using the Blackmagic Camera app.
- Allow Remote Cameras Access: Lets Blackmagic Camera app users who belong to this

project send media off their phones up to the Blackmagic Storage account, dropping it straight into the project's Media Pool.

- Don't Allow Remote Cameras: Bars Blackmagic Camera app users from sending footage up to this project, even when they're members of it. Once Create is pressed, a fresh project comes into being carrying whatever parameters you dialed in above.

Should you ever want to revise these parameters once a project already exists, you can reach them again by opening the Project settings and choosing the Blackmagic Cloud tab.

Every cloud setting on an existing Blackmagic Cloud project stays adjustable from the Project Settings.
