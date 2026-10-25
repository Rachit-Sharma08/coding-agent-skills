# The project manager and project manager

Version: DaVinci Resolve 20.3 Reference Manual. Context: Managing projects and project libraries.
[Chapter index](INDEX.md) / [Next section](project-icon-information-and-list-view.md)
<a id="source-creating-a-new-project"></a> <a id="source-importing-and-exporting-davinci-resolve-projects-drp-files"></a> <a id="source-managing-projects-and-project-libraries"></a> <a id="source-managing-projects-and-project-libraries-part-1"></a> <a id="source-project-management"></a> <a id="source-project-manager"></a> <a id="source-project-manager-view-options"></a> <a id="source-select-thumbnail-or-list-view"></a> <a id="source-the-create-new-project-dialog"></a> <a id="source-using-the-project-manager"></a>

### Managing Projects and Project Libraries

What this chapter walks through is using the Project Manager to keep the projects you have underway in DaVinci Resolve in order, plus handling the project libraries that act as the organizational backbone of the Project Manager. It also shows the steps for exporting and importing projects, and for archiving a project together with its media so it can be kept over the long term.

### Using the Project Manager

As a rule, the Project Manager is the very first window that greets you once DaVinci Resolve launches. It serves as a handy, single hub for making, arranging, and overseeing every project you have. Whereas other applications lean on your file manager to keep projects in order, DaVinci Resolve expects you to carry out the bulk of project organization inside the Project Manager.

### Project Manager

When a project is already open, you can bring the Project Manager back up whenever you like by clicking the Home button down in the lower right-hand corner of the DaVinci Resolve window, on the Page Navigation bar. Should you have tucked the Page Navigation bar away at the foot of the DaVinci Resolve window, the Project Manager can be opened through File > Project Manager.

Down in the bottom-right corner of the DaVinci Resolve interface sits the Project Manager button Launching DaVinci Resolve for the First Time? When DaVinci Resolve is freshly installed and you’ve just launched it the first time, the moment has come to set the preferences so you can declare your language, scratch disk volume, and the hardware setup for video and audio I/O and control panels (should you own one). To read more about configuring the preferences in DaVinci Resolve, see Chapter 4, “System and User Preferences.”

### Creating a New Project

Your initial move in DaVinci Resolve is making a new Project within the Project Manager, which handily is the very thing that appears when the program starts. Every project holds links to all the media, graphics, and sound files that go into your film, plus timelines on which the editing, color correction, motion graphics, and audio post tasks are carried out. A number of settings, options, and preferences ride along with each project (reach them by clicking the small gear icon down in the far bottom right of the interface), and every one of them gets a full description further along in this section. Even so, bringing a project into being really comes down to only four steps. Creating a New Project: 1 Down at the foot of the Project Manager, hit the New Project button. 2 Enter a name for the project you’re making. 3 Note the folder shown in Media Location where DaVinci Resolve will keep any media it creates. Confirm there’s room to spare on that drive. A click on the Change Location button lets you pick a different drive/folder rather than the default. 4 Click the Create button.

### The Create New Project dialog

### Project Management

For making, renaming, and removing projects, the Project Manager supplies an in-application interface. A good many of these commands sit in the contextual menu that appears once the Project Manager’s background gets a right-click. Methods of project management:

- To create a new project: Give the Default Project icon a double-click, or hit the New Project button at the foot of the window. A fresh project appears, and DaVinci Resolve brings up the Media page. With a project open, its project settings can be changed by clicking the gear icon.
- To open a previously saved project: Give any Project icon a double-click, or an Item if you happen to be in List view. Selecting a project and clicking the Open button works too.
- To open a project in Read-Only Mode: Give a Project icon or Item a right-click, then pick Open in Read Only Mode. That opens a project with no risk of changing it. Should you make edits, the Save As command will store a fresh copy of the project under a new name.
- To rename a project: Right-click a Project icon or Item, pick Rename, and type a fresh name into the dialog that pops up, clicking OK once you’re done.
- To load project settings from another project to the currently open project: On a Project icon or Item (any one besides the project that’s currently open), right-click and pick “Load Project Settings to Current Project.” That lets you adjust a project’s settings before opening it, handy when those settings are triggering some sort of issue that keeps the project from opening.
- To update the thumbnails of a project in the Project Manager: On any project, right-click and pick “Update Thumbnails.”
- To delete a project: Pick one or more projects, then either tap the Backspace key, or right-click one of the chosen projects and pick Delete. Click OK once a dialog prompts you to confirm the action.

NOTE: The project that is currently open or loaded cannot be moved or deleted.

### Importing and Exporting DaVinci Resolve Projects (.drp Files)

The file extension DaVinci Resolve gives saved projects is .drp, which lets you trade files with fellow DaVinci Resolve users. Double-clicking a DaVinci Resolve .drp file within the Windows or macOS file system will, on its own, launch DaVinci Resolve, bring that project into the Project Manager no matter which kind of project library is in use, and open it so you can get straight to work. Importing and Exporting Projects in Local Project Libraries When local project libraries are how you manage your projects, you can copy and import projects through the project folders in either the macOS or Windows file manager. On DaVinci Resolve for Linux this approach doesn’t function. Shifting projects out of one local project library and into another by way of macOS or Windows: 1 Track down the local project library directory in which the project you mean to copy sits. If you’re not sure where the designated local project library directory lives, open DaVinci Resolve and read the directory path for the current local project library off the Project Libraries sidebar. 2 Copy the project folder off the source workstation and into the designated local project library directory on the destination workstation. If you’re still unsure where the designated local project library directory lives, open DaVinci Resolve on whichever workstation you’re copying the project to, then check that workstation’s current local project library directory path inside the Project Libraries sidebar. 3 After the project folder is copied into the right spot, you’ll have to quit DaVinci Resolve and start it again. The imported project ought to turn up in the Project Manager afterward. Importing and Exporting Projects in Network Project Libraries When a network project library is in use, a separate group of commands handle importing and exporting projects via the .drp file format. You may likewise export .drp files out of local project libraries should you wish to send out a more self-contained item for transport. To import a .drp project file, do one of the following:

- Click the Import button at the foot of the Project Manager, then locate and pick a .drp project file by way of the Import Project File dialog, and click Open.
- Take the .drp file you intend to import from your file system and drop it anywhere within the Project Manager window.
- Right-click any blank spot of the Project Manager and pick Import, then locate and pick a .drp project file by way of the Import Project File dialog, and click Open.

To bring in a .drp project file while also resetting the gallery path in one go:

- Keep the Option key held while right-clicking any blank spot of the Project Manager, and pick Import+, then locate and pick a .drp project file, and click Open. As it opens, the gallery path is set automatically to match your workstation’s.

To export the currently open project as a .drp file:

- Pick File > Export Project, and once the Save dialog appears, settle on a location, type a name, and click Save. What you get is a self-contained file carrying a .drp file suffix stored at the location you picked.

To export a .drp project file from the Project Manager:

- Click the Export button at the foot of the Project Manager, and once the Save dialog appears, settle on a location, type a name, and click Save. What you get is a self-contained file carrying a .drp file suffix stored at the location you picked.
- Right-click a Project icon or Item within the Project Manager, then pick one of the commands below;

Export Project: Exports the project data carrying no LUTs and no stills. Ideal when the smallest possible file is what you need to export. Export Project With Stills and LUTs: Exports the project together with both the still frames in the Gallery and the LUTs your grades rely on. Ideal when you want the most self-contained export and can’t be sure the recipient holds the same LUTs you do.

- Once the Save dialog appears, settle on a location, type a name, and click Save. What you get is a self-contained file carrying a .drp file suffix stored at the location you picked.

TIP: Several projects can be exported from the Project Manager at once, either by command-clicking or lassoing the projects, right-clicking one of them, and choosing Export Projects off the drop-down menu. Every project lands at the same location.

### Project Manager View Options

Up at the top right, four buttons govern the way projects display inside the Project Manager.

### Select Thumbnail or List View

- Zoom slider: (Shows up only in Thumbnail view) Lets you change the thumbnails’ size within Thumbnail view.
- Project Sort Order drop-down: (Shows up only in Thumbnail view) Lets you set the order in which projects sort within Thumbnail view.
- Information: (Shows up only in Thumbnail view) Lets you reveal or conceal extra project information shown beneath each project’s thumbnail, taking in the frame size, how many timelines it holds, and the date that project was last modified.
- Thumbnail view: A large image stands in for each project, and you can hover-scrub it to bring out five sample images drawn from that project.
