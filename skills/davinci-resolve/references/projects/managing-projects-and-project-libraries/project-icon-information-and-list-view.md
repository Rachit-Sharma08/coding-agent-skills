# Hover scrub over project icon information is enabled and project list view

Version: DaVinci Resolve 20.3 Reference Manual. Context: Managing projects and project libraries.
[Chapter index](INDEX.md) / [Previous section](the-project-manager-and-project-manager.md) / [Next section](project-library-duplicate-backup-and-restore.md)
<a id="source-a-folder-in-the-project-manager"></a> <a id="source-creating-and-connecting-to-project-libraries"></a> <a id="source-hover-scrub-over-project-icon-information-is-enabled"></a> <a id="source-managing-project-libraries"></a> <a id="source-managing-project-libraries-in-the-project-libraries-sidebar"></a> <a id="source-moving-projects-from-one-project-library-to-another-on-the-same-workstation"></a> <a id="source-opening-the-project-libraries-sidebar"></a> <a id="source-organizing-projects-in-folders"></a> <a id="source-project-libraries-sidebar-button"></a> <a id="source-project-libraries-sidebar-controls"></a> <a id="source-project-library-types"></a> <a id="source-project-list-view"></a> <a id="source-searching-for-projects"></a>

### Hover-scrub over Project icon; information is enabled

- List view: Each project shows up as a list entry, and the row carries these seven columns — Name, Last Modified, Timelines, Format, Frame Rate, Date Created, plus Note. Click any column header to order the Project Manager’s contents by that field; a second click on the header flips that column between ascending and descending order.

### Project List view

### Searching for Projects

A click on the magnifying glass button up at the Project Manager’s top right-hand corner reveals the Search Options, which serve to track down one or more projects by way of the metadata picked in the Filter By drop-down menu just to its right. Search field open with Filter by search criteria selected Through that drop-down menu you can opt to search by name or by project format. With a criteria chosen, start typing in the search field, and the Project Manager begins filtering by your search text instantly and on the fly.

### Organizing Projects in Folders

When you have a lot of projects to keep in order, folders can be made to hold them.

### A folder in the Project Manager

Methods of working with project folders:

- To create a folder: Hit the New Folder button, then type a name into the Create New Folder dialog and click Create.
- To delete a folder: Right-click a folder, pick Delete, and click Yes at the prompt. Every project sitting in a deleted folder gets deleted along with it.
- To rename a folder: Right-click a folder, pick Rename, then type a fresh name and click OK.
- To copy a folder: Right-click a folder and pick Copy off the drop-down menu, or select the folder and tap Command-C. Whatever projects sit inside that folder are copied as well.
- To paste a folder: With a copy made, right-click the Project Manager’s background and pick Paste off the drop-down menu, or tap Command-V. You may paste into other project libraries, into other folders, or into the very same spot, where a fresh copy of the folder picks up the word (Copy) at its end. Every enclosed timeline copies over too.
- To open a folder: Give a folder a double-click to open it and see what’s inside. Up at the Project Manager’s top left-hand corner, a folder path view tells you which folder stands open, along with your spot inside a nested chain of folders if that’s how you’ve arranged things.
- To exit a folder: Reach for the path control along the top of the Project Manager and click a higher tier in the folder hierarchy.
- To move a project into a folder: Drag the project over a folder icon and drop it there to set it inside the folder.
- To move a project out of a folder: Open a folder, pick one or more projects you intend to move, then right-click the selection and pick Cut off the contextual menu. Next, head to the next spot in the Project manager where you want the cut projects placed, right-click the Project Manager’s background, and pick Paste. The projects ought to show up in their new spot.

### Managing Project Libraries

Whereas other applications write self-contained project files to whatever user-specified spots you choose across your file system, DaVinci Resolve leans toward a more centrally arranged style of project management built on project libraries. Out of the box, DaVinci Resolve relies on a local project library to keep tabs on each project you make. The Project Libraries sidebar is where you manage the projects held inside this project library, all of which are stored to a particular directory on your system (specific to that project library). Where this local project library sits by default hinges on which operating system you run.

That said, you’re free to make extra project libraries for holding other projects if you wish. As an example, you might set up one project library for each year you work. If your work is series television, you could spin up multiple project libraries, one per program you handle. Or you might keep a separate project library for every client you serve. No rigid rule applies; in the end, the way you put project libraries to use comes down entirely to you and your own organizational tastes.

### Project Library Types

There are three different project library types in which project libraries can be kept, each functioning much the same but offering extra connectivity and sharing features that depend on how your network is set up. You pick the Library Type over at the upper left of the Project Manager.

- Local: Keeps your project libraries on your workstation locally. It is the default and suits individual users or single systems best.
- Network: Keeps your project libraries on an outside computer wired to several workstations across the same local network. It also lets you govern who may access the project library. It suits a facility made of multiple workstations in one building working on the same material best.
- Cloud: Keeps your project libraries within the Blackmagic Cloud. This lets several workstations reach the same project library across the internet. It also lets you govern who may access the project library. It suits multiple people working on one project from scattered locations around the globe best.

The three types of project libraries: local, network, and cloud. To read more about setting up and configuring the various project library types, see Chapter 196, “Managing Project Libraries and Project Servers.”

### Opening the Project Libraries Sidebar

When several project libraries already exist, a click on the button up in the Projects Browser’s upper-left hand corner reveals a sidebar down the left side of the Project Manager that lists every project library on your workstation, complete with assorted options for managing those project libraries and for browsing the projects inside them. This sidebar serves to open different project libraries and to browse the projects held within.

### Project Libraries sidebar button

Project Manager with the Project Libraries sidebar displayed

### Moving Projects From One Project Library to Another on the Same Workstation

Having relied on multiple project libraries to keep your projects in order, you can browse what each project library holds to hunt down whatever you’re after, then copy one or more projects between project libraries should you need to shuffle how they’re arranged. To view the contents of a project library: 1 Open the Project Libraries sidebar via the button up in the Projects window’s upper-left hand corner. 2 Click a project library in the sidebar to select it, and an orange highlight will show up If a project was already open, a prompt asks whether to save it before closing, because every open project must be shut before another project library’s contents can be inspected. After that, the projects belonging to that user inside the selected project library show up in the Project Manager window.

To pull a project in from a different project library by way of the Project Libraries sidebar: 1 Reach for the button in the upper-left hand corner of the Projects window and open the Project Libraries sidebar with it. 2 Click a project library in the sidebar to select it, and if you must, use the drop-down menu over at the right of the project library listing to settle on a specific user. The projects belonging to that user inside the selected project library show up in the Project Manager window. 3 Pick a project you intend to import, and tap Command-C to copy it. 4 Click the current project library once more to select it (the project library you mean to work inside). 5 Tap Command-V to paste the project you copied. A copy lands in the current project library. For fuller detail on how shared project libraries are set up and run, consult Chapter 196, “Managing Project Libraries and Project Servers.” To bring Project Settings in from another project through the Project Libraries sidebar: 1 Using the button tucked in the Projects window’s upper-left hand corner, bring up the Project Libraries sidebar. 2 Pick a project you intend to import Project Settings into so that it’s highlighted. 3 Right-click any project and pick “Load Project Settings to Current Project.” The settings of that project get copied onto the project you picked back in step 2.

### Managing Project Libraries in the Project Libraries Sidebar

The controls inside the Project Libraries sidebar make it straightforward to spin up new project libraries (through the button at the bottom), upgrade project libraries that carry a flag (through circular badges), import and export project libraries (through buttons at the top), and surface extra information about each project library (through buttons up at the top of this sidebar).

### Project Libraries sidebar controls

The trio of controls up at the top of the Project Libraries sidebar serve these purposes:

- Sort Order drop-down menu: Through this menu you decide the way the assorted local and network project libraries in the sidebar get ordered. The available keys are Project Library Name, Schema (by date), Status, or Location, each usable in either Ascending or Descending order.
- Restore: Imports .resolve.backup files to restore a backed up project library.
- Show Search Field: Brings up a search field plus a search criteria drop-down letting you hunt for project libraries in the sidebar by Name, Schema, Status, or Location. A click on the Display Project Library Details icon (the circled letter “i” over to the right of the project library) brings up extra information below each project library in the sidebar. Exactly what information depends on the project library’s type. Local project libraries show their status (compatible/incompatible) plus their location (directory path). For network and cloud project libraries, what’s shown is the schema (its created and modified dates), the status (compatible/incompatible), the IP location, and underneath, whichever members can reach the project library.

### Creating and Connecting to Project Libraries

Local, network, and cloud libraries can run side by side so you can switch over to one or the other as your needs dictate. The instructions here cover setting up local project libraries. Network and cloud libraries call for extra configuration and setup beforehand. Network and cloud project library setup and operation are covered more fully in Chapter 196, “Managing Project Libraries and Project Servers.” To build a fresh local project library: 1 In the Projects window’s upper-left hand corner, click the button that opens the Project Libraries sidebar. 2 Hit the Add Project Library button down at the foot of the sidebar. 3 Move to the Create tab and click it. The Add Project Library window ought to resemble the screenshot below:

Creating a local project library 4 Across the remaining fields, proceed as follows: a) Into the Name field, enter a name for your new project library b) Click inside the Location field and lean on the Filesystem navigation dialog to pick the spot for the directory destined to contain every DaVinci Resolve project directory 5 Hit Create, after which the new local project library appears within the local project library portion of the Project Libraries sidebar. To hook up with a local project library that already exists: 1 Click the Projects window’s upper-left hand corner button, the one that brings up the Project Libraries sidebar. 2 Hit the Add Project Library button down at the foot of the sidebar. 3 Switch over to the Connect tab and click it. The Add Project Library window ought to resemble the screenshot below:

Connecting to an existing local project library 4 Across the remaining fields, proceed like so: a) Into the Name field, type a name for the new project library. b) Click inside the Location field and lean on the Filesystem navigation dialog to point at where the existing project library you mean to connect to resides. 5 Click Connect, and the new local project library surfaces inside the local project library section of the Project Libraries sidebar.
