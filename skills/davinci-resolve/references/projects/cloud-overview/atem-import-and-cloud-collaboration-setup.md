# Atem import and cloud collaboration setup

Version: DaVinci Resolve 20.3 Reference Manual. Context: Cloud overview.
[Chapter index](INDEX.md) / [Previous section](blackmagic-cloud-and-cloud-project-libraries.md)
<a id="source-blackmagic-cloud-support-for-importing-atem-projects"></a> <a id="source-create-the-proxy-media"></a> <a id="source-set-up-the-cloud-storage"></a> <a id="source-setting-up-a-cloud-based-collaboration-workflow"></a> <a id="source-setup-the-davinci-resolve-project-and-settings"></a>

### Blackmagic Cloud Support for Importing ATEM Projects

When you're running ATEM switchers and follow the workflow of producing several ISO feeds plus the matching DaVinci Resolve project, you can now sign into a Blackmagic Cloud project library, pick an existing DaVinci Resolve cloud project, and rely on the Camera Uploads mechanism to bring recorded media across to DaVinci Resolve in sync. Fellow DaVinci Resolve collaborators will see the switcher's edit decisions show up as a fresh timeline within that project.

- For the uploaded media from the switcher to appear, the DaVinci Resolve project has to be configured to synchronize camera originals.
- Should the ATEM resolution or frame rate not match the project settings, new timelines may adopt custom settings.

### Setting up a Cloud-Based Collaboration Workflow

With internet bandwidth climbing over the years, collaborating on a project entirely online has lately become feasible. Where you once had to share a single building wired to a fast LAN and Network Attached Storage (NAS), you can now work together live from anywhere on earth by leaning on the internet and cloud storage instead. What follows are the steps for building an entirely cloud-based workflow with the tools and settings inside DaVinci Resolve 18 or higher. This example workflow features Editor A, Colorist B, and Audio Engineer C, each in a different corner of the world, all wanting to collaborate on one project simultaneously. The aim is to cut down on how much media management is required and to avoid passing individual project files to and fro.

Set up the Blackmagic Cloud and a Cloud Library

- Users A, B, and C register for the Blackmagic cloud service.
- Users A, B, and C sign into the cloud through the Project Manger within their own DaVinci Resolve installations.
- User A builds a fresh cloud library and invites Users B and C to share it. Because User A is the editor,

they'll situate the cloud library's server closest to themselves.

### Set up the Cloud Storage

- Users A, B, and C register with a cloud storage provider (Dropbox, iCloud, OneDrive, Google Drive, etc.)
- Users A, B, and C set their cloud storage up so they can all reach the same cloud-based folder together. That folder belongs at the top level of the cloud storage. They settle on naming the folder Episode 12.
- Within their shared Episode 12 folder, Users A, B, and C build a file hierarchy system, for instance fresh subfolders for Audio, Proxies, and Graphics.
- Users A, B, and C mount the shared storage folder onto their own machines. Editor A drops a few logos and still photos into the Graphics folder. Audio Engineer C drops some music and sound effects into the Audio folder. Uploading and distributing this from the cloud takes a while, but in time every user holds the same media locally on their own computer.

### Create the Proxy Media

- Colorist B keeps the RAW camera masters on a hard drive wired to their system. Given that they alone require the RAW camera files for color grading, they'll generate low bandwidth proxies for the Editor and Audio Engineer to use. Those files are compact enough to upload and keep in their cloud storage folder.
- Colorist B generates proxy files from the RAW media using the Blackmagic Proxy Generator application.

To learn more about working with the Blackmagic Proxy Generator, refer to Chapter 8, “Improving Performance, Proxies, and the Render Cache.”

- Colorist B sends the proxy files up to the Proxies folder within their cloud storage.

### Setup the DaVinci Resolve Project and Settings

- Colorist B builds the new project inside the cloud library and configures its resolution, frame rate, and so on.
- Colorist B switches on the File > Multiple User Collaboration setting.
- Users A, B, and C open the project and point their individual file paths at their cloud storage folder

“Episode 12” within the Path Mapping section of the Project Settings. To read more about Path Mapping, refer to Chapter 6, “Project Settings.”

- Colorist B brings the RAW media in from their local hard drive into their Media Pool, then links it to the proxies he sent up to the Episode12/Proxies folder. From this point, Editor A and Audio Engineer C have the proxy media available, while Colorist B can flip between RAW media and Proxies whenever needed. If it proves necessary, Colorist B may also choose to upload the RAW media into the shared folder where space and time permit. While the rest of the users wait on that media to finish uploading, if they've got the “Prefer Camera Originals” setting ticked under Playback

> Proxy Handling menu, they can keep editing with the proxies, and as the RAW media files arrive, those will swap in for the proxy files automatically as they come.

- Editor A brings their still photos into the Media Pool out of the Episode 12/Graphics folder. They become available straight away to Users B and C with no relinking.
- Audio Engineer C brings their music tracks into the Media Pool out of the Episode 12/Audio folder. They become available straight away to Users A and B with no relinking.
- As the users go on adding more media into the shared folder and pulling it into the Media Pool, there can be a delay while the media uploads to the cloud storage and then downloads to the other users. Throughout that window the clip shows as media offline, yet it relinks automatically the moment the file completes its download onto the local computer.

Continue working in DaVinci Resolve’s Collaborative Workflow From this point, the editor edits, the colorist grades, and the audio engineer takes care of the sound design, every one of them relying on the existing collaborative workflow tools in DaVinci Resolve. For more information on using these tools, see Chapter 197, “Collaborative Workflow.”
