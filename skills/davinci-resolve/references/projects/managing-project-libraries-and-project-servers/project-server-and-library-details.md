# DaVinci resolve project server window and display project library details icon

Version: DaVinci Resolve 20.3 Reference Manual. Context: Managing project libraries and project servers.
[Chapter index](INDEX.md) / [Previous section](shared-projects-and-network-library-collaboration.md)
<a id="source-the-davinci-resolve-project-server-window"></a> <a id="source-the-display-project-library-details-icon"></a>

### The DaVinci Resolve Project Server window

Three principal UI areas make up this window:

- Project libraries list: Within the Project Server application, the Project libraries list lays out each DaVinci Resolve network project library present on your machine — disconnected ones included. That ease of view helps you locate libraries you’d like to reconnect.
- Projects browser: Displays all projects and folders inside the currently selected project library, either as icons or as a hierarchical list.
- Toolbar: A toolbar across the top of the window presents the functions on hand for managing DaVinci Resolve project libraries on your workstation.

Project Libraries toolbar controls (L-R): Sort, Restore, Search

The three controls along the top of the Project Libraries toolbar serve these purposes:

- Sort Order dropdown menu: Through this menu you decide the ordering of the assorted local and network project libraries shown in the sidebar. You can sort on Database Name, on Schema (by date), on Status, or on Location, each in either Ascending or Descending order.
- Restore: Brings in .resolve.backup files to restore a backed up project library.
- Show Search Field: Reveals a search field plus a search criteria dropdown that lets you find project libraries in the sidebar by Name, Schema, Status, or Location.

Clicking the Display Project Library Details icon — the circled “i” found to the library’s right — opens up further information below each database in the sidebar and brings out the Backup and Optimize buttons.

### The Display Project Library Details icon

The controls surfaced within the Project Library details serve these purposes:

- Project Library Settings: A click on this gear icon lets you opt to Rename, Delete, or Export an Access Key for the library.
- Project Library Enabled: This toggle switches the project library sharing on or off.
- Project Library Information: Surfaces the library’s metadata — among it Location (the Project Server’s IP address), Status (either compatible or upgrade required), plus the dates it was created and modified.
- Backup: A click on this button lets you export the project library out to a backup file.
- Optimize: A click on this button lets you optimize the project library for stronger performance.
- Members: This region shows you which members hold access to the project, and the Manage Members button lets you grant or revoke their access.
