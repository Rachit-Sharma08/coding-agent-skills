# Project notes and dynamic project switching

Version: DaVinci Resolve 20.3 Reference Manual. Context: Managing projects and project libraries.
[Chapter index](INDEX.md) / [Previous section](library-disconnection-deletion-and-recent-projects.md)
<a id="source-archiving-and-restoring-projects"></a> <a id="source-dynamic-project-switching"></a> <a id="source-project-notes"></a>

### Project Notes

Every DaVinci Resolve project now offers Project Notes, a plain "scratch pad" for jotting down text notes tied to that project. You reach these notes through the File > Project Notes command, and a Project Notes command also lives in the contextual menu on project icons within the Project Manager, putting the notes within reach of anyone connected to that project library.

Setup and Workflows — Timeline Backups — Managing Projects and Project Libraries reference.

### Dynamic Project Switching

Found in the Project Manager contextual menu, Dynamic Project Switching is an option letting you load several projects into RAM at once, so flipping between them is quick when you want to copy and paste clips, timelines, and node settings around. Planning to open lots of projects, or even a handful of really big ones? Make certain your workstation carries enough RAM, or performance may bog down.

Flipping between open projects via the Project Title drop-down up top in the DaVinci Resolve UI Methods of using Dynamic Project Switching:

- To enable Dynamic Project Switching: Open the Project Manager, right-click anywhere inside it, and pick Dynamic Project Switching so a check appears. Dynamic Project Switching stays on until you switch it off.
- To open multiple projects in RAM: Open one project, then reopen the Project Manager and open another. Every project you open stays on hand in RAM.
- To switch among open projects: Choose File > Switch Project and pick the project you'd like to jump to from the submenu. Other projects already sitting in RAM are likewise selectable from the drop-down beside the project name, up at the top center of the DaVinci Resolve user interface.
- To close a specific project: Choose File > Close Project and pick the project you'd like to close from the submenu. A save prompt may appear, after which the project closes.
- To close all other open projects: Open the Project Manager. Every open project carries a check mark in its top right corner; the project currently open shows an orange corner mark, while others held in memory show a gray one. Right-click anywhere inside the Project Manager and pick Close Projects in Memory to shut every project but the current one.

Using dynamic project switching, you can do the following:

- Copy and paste clips out of one project's Media Pool into another.
- Copy and paste timelines out of one project's Media Pool into another. Pasting a timeline from another project brings along every clip it uses, dropping them into the matching location too.
- Copy and paste clips from a timeline in one project into a timeline in another.
- Copy a node's settings out of one project and paste them onto a node in another.

You're also free to copy and paste clips, timelines, and node settings between projects without dynamic project switching, but switching speeds the whole thing up.

Setup and Workflows — Timeline Backups — Managing Projects and Project Libraries chapter.

### Archiving and Restoring Projects

DaVinci Resolve includes a handy feature for swiftly archiving every last media file a project draws on, subtitle files included, together with the project itself, all into one location. You might do this to pass a project to a fellow DaVinci Resolve user, or to package a project and its media for short- or long-term archiving by whatever backup methodology you favor. It's a straightforward process. To Archive a project: 1 Open the Project Manager. 2 Find and right-click the project you'd like to archive, then pick Archive.

The contextual menu command for archiving projects 3 Once the Archive Project window shows up, pick where to write the archive. Be sure to pick a volume roomy enough to hold all the media from the project you're archiving, then click Save. 4 Once the Archive dialog shows up, double-check where the archive will be written, and pick which optional media to include in it. You may optionally include Optimized media and/or Render Cache media tied to a project.

A dialog where you decide whether Optimized and/or Render Cache media gets included 5 Click Ok, and a dialog carrying a progress bar shows how long the archive operation will run. Any errors stemming from missing or offline media surface once the process wraps up.

The resulting archive that gets written is a directory bearing the .dra file extension. Within that folder sits a set of subdirectories holding all the media the archived project relies on. Each directory of media files used is written along a directory path that mirrors precisely the path it originated from, giving you a record of where every clip first came from. To restore an Archived project: 1 Copy the .dra archive directory you'd like to restore onto the volume where you want those media files held. Restoring doesn't relocate this directory; it merely adds the project file inside it to the Project Manager, so be sure the .dra archive directory sits on a storage volume fast enough for you to work on. 2 Open the Project Manager, right-click anywhere, and pick Restore off the contextual menu. Pick the .dra archive directory you just copied, then click Open. 3 When prompted, type a unique project name for the restored project, then click OK. The project lands back in the Project Manager and stays linked to the media held inside the .dra archive. 4 Or you can simply drag the .dra folder straight out of your file system into the Project Manager. If, once an archive is restored, you'd like to relocate its media elsewhere, you can lean on Media Management to run a move operation across every clip the project holds. For a fuller account of Media Management, turn to Chapter 46, “Media Management.”

Setup and Workflows — Timeline Backups — Managing Projects and Project Libraries closing.
