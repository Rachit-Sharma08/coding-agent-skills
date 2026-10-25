# What is a project library and project libraries

Version: DaVinci Resolve 20.3 Reference Manual. Context: Managing project libraries and project servers.
[Chapter index](INDEX.md) / [Next section](shared-projects-and-network-library-collaboration.md)
<a id="source-backing-up-a-local-project-library"></a> <a id="source-connecting-to-an-existing-local-project-library"></a> <a id="source-connecting-to-an-existing-local-project-library-1"></a> <a id="source-creating-a-local-project-library"></a> <a id="source-creating-a-new-local-project-library"></a> <a id="source-disconnecting-from-a-local-project-library"></a> <a id="source-duplicating-project-libraries"></a> <a id="source-local-project-libraries"></a> <a id="source-managing-project-libraries-and-project-servers"></a> <a id="source-managing-project-libraries-and-project-servers-part-1"></a> <a id="source-network-project-libraries"></a> <a id="source-restoring-a-local-project-library"></a> <a id="source-upgrading-a-local-project-library"></a> <a id="source-using-project-libraries"></a> <a id="source-what-is-a-project-library"></a>

### Managing Project Libraries and Project Servers

This chapter walks through configuring and working with project libraries at a deeper level, handing you finer control over the way projects get saved and arranged. It covers configuring local, network, and cloud project libraries that you can lean on to administer DaVinci Resolve projects shared across several DaVinci Resolve workstations.

### What is a Project Library?

A Project Library (once called the project database) is a database file that holds one or more DaVinci Resolve projects. Whenever you build or open a project from the Project Manager, or save the current one, you’re reading from or writing to a project library. One project library houses many projects, and each project in turn carries every timeline, grade, clip metadata, visual effect, audio mix, and so on for your film. What a project library doesn’t keep is the original media; it stores only the directions for turning that media into a finished film. DaVinci Resolve can reach many project libraries, yet it links to just one project library at any moment.

### Using Project Libraries

Laying out a scheme for how projects and project libraries get stored matters a great deal to building lean, efficient workflows. Spinning up a dedicated project library per TV series, commercial, or film a post house handles, for instance, keeps your clients compartmentalized and boosts performance by loading only what a given project actually needs. DaVinci Resolve reaches project libraries in three ways, and which one fits depends largely on how many people share a project and where in the world they sit. Each path is laid out below.

- Local Project Libraries: (the default option) Suits productions that finish the whole film on one workstation. Several people might contribute to one project, but they take turns on the same machine. Here your project libraries live locally on the computer that has DaVinci Resolve installed, and every media drive the project uses is attached locally.
- Network Project Libraries: Suits post houses or productions with several DaVinci Resolve workstations under one roof that want to tackle the same project from any room, or together at once. Here your project libraries sit on a separate computer that runs the DaVinci Resolve Project Server application. Every workstation has to join that computer over the same local area network (LAN), and each must either reach the same media drives through a NAS or MAM system or hold a locally attached copy (or proxies) of the media.
- Cloud Project Libraries: Suits post houses, companies, or productions whose DaVinci Resolve workstations are spread across different parts of the globe and that want to work the same project from each spot on their own, or jointly at the same time. Here your project libraries reside in the Blackmagic cloud service. Every workstation must have internet access, and each system needs a locally attached copy (or proxies) of the media on hand.

The three types of Project Libraries: local, network, and cloud Moving around and operating the Project Libraries sidebar plays out the same way for every type of project library above.

- Project Library: Every reachable project library shows by name, and a click on one hooks that library and the projects inside it up to DaVinci Resolve. Plenty of libraries are available to pick from, though only a single library stays active at once.

Project Libraries sidebar controls (L-R): Sort, Restore, Search

- Sort Libraries: Chooses the order in which the project libraries are listed; the options are Name, Schema (date), Status, and Location. Either Ascending or Descending order is available.
- Restore: Lets you load back a project library you backed up earlier.
- Search: Lets you hunt down a particular project library by text, with the search narrowable by

Name, Schema, Status, and Location.

### Local Project Libraries

Local project libraries are the most basic and widespread kind of project library, demanding no extra setup or configuration from the user beyond installing DaVinci Resolve. They’re saved locally on your workstation; out of the box they land in a folder named Resolve Disk Database, although you can put them by hand anywhere across your file system.

### Creating a New Local Project Library

Making a fresh local library is quick and uncomplicated. To Create a New Local Project Library: 1 Click the Show/Hide Project Libraries icon at the top left of the Project Manager to reveal the sidebar. 2 Pick the Local icon from the Project Library options. 3 Click the “Add Project Library” button along the bottom of the sidebar. 4 Pick the Create option to build a new project library. 5 Type a fresh name for your project library. 6 Hit the Browse button beside Location to choose where on your local computer the project library is saved. 7 Hit the Create button. From here you can build or import new projects straight into your new local project library.

### Creating a local project library

### Connecting to an Existing Local Project Library

You can hook back up to a project library that already exists by following the steps below. To connect to an existing project library: 1 Click the Show/Hide Project Libraries icon at the top left of the Project Manager to reveal the sidebar. 2 Pick the Local icon from the Project Library options. 3 Click the “Add Project Library” button along the bottom of the sidebar. 4 Pick the Connect option to reach the existing project library. 5 Type a fresh name for your project library. 6 Hit the Browse button beside Location to point to where on your local computer the folder holding the existing project library sits. It’s usually called “Resolve Disk Project library.” 7 Hit the Connect button. From here you can browse and use every existing project straight from the existing local project library.

### Connecting to an existing local project library

### Disconnecting from a Local Project Library

You can detach and drop an existing project library from the Project Libraries list with the steps below. To disconnect from a project library: 1 Click the Show/Hide Project Libraries icon at the top left of the Project Manager to reveal the sidebar. 2 Pick the Local icon from the Project Library options. 3 Right-click the project library you’d like to detach from, and choose disconnect off the context menu. 4 Hit the disconnect button in the confirmation dialog. Detaching a project library merely strips it from the available options in the Project Libraries sidebar. It leaves the project library itself intact. You can either remove it by hand in the OS filesystem, or reconnect to it via the steps outlined in Connecting to an Existing Local Project Library.

### Duplicating Project Libraries

Local Project Libraries may be duplicated within the same database for backup or iteration purposes. 1 Right-click the Library and choose Duplicate from the dropdown menu. 2 Choose the Resolve Database Folder in the file system browser. That can be the very one you use for the original project or a brand new one. 3 Click the Open button. 4 Give the new Library a name in the Clone Library dialog.

### Backing up a Local Project Library

You can likewise back up project libraries by exporting them and reimporting them down the line. To backup/export a project library: 1 Choose the library you intend to back up. 2 Click the Display Project Library Details icon — that’s the “i” inside a circle, sitting just right of the library.

The Display Project Library Details icon 3 Choose the Back Up button. 4 Within the Backup Project Library dialog, settle on a save location, then click Save.

### Restoring a Local Project Library

Bringing in project libraries that already exist lets you carry multiple projects across systems. To restore/import a project library: 1 Up along the top of the Project Libraries sidebar, click the Restore button.

The Restore button 2 Through the file import dialog, find the library you wish to import, and click Open. 3 Within the Add Project Library dialog, handle the following: a) Into the Name field, enter a name for the new project library. That renames the imported one while leaving its contents alone. Nothing stops you from reusing the same name as the original project library. b) Click inside the Location field and, via the Filesystem navigation dialog, point to the directory where the existing DaVinci Resolve project libraries reside. 4 Click Create; the imported local project library then appears within the Local section of the Project Libraries sidebar.

### Upgrading a Local Project Library

A selected library shows an upgrade warning in the Project Manager only once you’ve installed a newer DaVinci Resolve build and you hold project libraries made under older DaVinci Resolve versions that are due for upgrading.

The upgrade warning in the Project Manager signals that a project library is due to be upgraded. As a rule it’s smart to back up a project library before upgrading it, in case anything goes sideways. Broadly, going from one whole version release of DaVinci Resolve to the next whole version release usually calls for an upgrade, whereas moving to a dot release of the same version might or might not. Should the project library in use need updating, you’ll hear about it when the application launches. To bring a project library forward from an outdated DaVinci Resolve build: Click whichever project library needs updating, then choose the Upgrade Project Library button. A dialog pops up to make sure you truly intend to upgrade that project library. Click Upgrade to carry on.

### Network Project Libraries

Several DaVinci Resolve workstations can reach the same project once you stand up a Project Server that shares one or more network project libraries across a local network. With that in place, there are two approaches to using a shared project library.
