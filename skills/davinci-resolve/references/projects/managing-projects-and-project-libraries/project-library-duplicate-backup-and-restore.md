# Duplicating project libraries and backing up and restoring project libraries

Version: DaVinci Resolve 20.3 Reference Manual. Context: Managing projects and project libraries.
[Chapter index](INDEX.md) / [Previous section](project-icon-information-and-list-view.md) / [Next section](library-disconnection-deletion-and-recent-projects.md)
<a id="source-backing-up-and-restoring-project-libraries"></a> <a id="source-duplicating-project-libraries"></a> <a id="source-managing-projects-and-project-libraries-part-2"></a> <a id="source-upgrading-project-libraries"></a>

### Duplicating Project Libraries

Inside one and the same database, you can duplicate Local Project Libraries for backup or iteration purposes. 1 Give the Library a right-click, then pick Duplicate off the drop-down menu. 2 In the file system browser, choose the Resolve Database folder. That may be the very one backing the original project, or else a fresh one. 3 Click on the Open button. 4 Give the new Library a name inside the Clone Library dialog.

### Backing Up and Restoring Project Libraries

Project libraries can also be backed up by exporting them and then reimported at a later time. To backup/export a project library: 1 Open the Project Libraries sidebar through the button sitting in the upper-left hand corner of the Projects window. 2 Choose whichever project library you mean to back up. 3 Hit the Display Project Library Details icon (that circled letter “i” over to the right of the project library).

The Display Project Library Details icon 4 Click the Back Up button. 5 In the Backup Project Libraries dialog, settle on a location to store the backup, and click Save.

To import a project library: 1 Hit the button over in the upper-left hand corner of the Projects window so the Project Libraries sidebar opens. 2 Up at the top of the Project Libraries sidebar, click the Restore button.

The Restore button 3 Locate, through the file import dialog, the project library you need to bring in, and click Open. 4 Within the Add Project Library dialog, carry out the following: a) Into the Name field, supply a name for the new project library. That renames the project library you’re importing without disturbing what it holds. Giving it the original project library’s name is fine too. b) Click inside the Location field and turn to the Filesystem navigation dialog to settle on whichever directory contains the DaVinci Resolve project libraries already present. 5 Hit Create, and the local project library you imported turns up in the Local section of the Project Libraries sidebar.

### Upgrading Project Libraries

A selected library shows an upgrade warning within the Project Manager only once you’ve installed a fresh version of DaVinci Resolve while holding project libraries built under older versions of DaVinci Resolve that are due for upgrading.

When the Project Manager shows an upgrade warning, it's telling you the project library has to be upgraded It's usually wise to back a project library up before upgrading, on the off chance something breaks. As a rule, moving from one full version release of DaVinci Resolve to the next full version release calls for an upgrade, whereas moving to a dot release within the same version might not. Should the project library in use need updating, you'll get the notice when the application launches. To upgrade a project library from an old version of DaVinci Resolve: Select a project library marked for updating, then press the Upgrade Project Library button. A dialog pops up asking you to confirm you really mean to upgrade that project library. Press Upgrade to go ahead.
