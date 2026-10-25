# Versions and versions section of the project settings

Version: DaVinci Resolve 20.3 Reference Manual. Context: Grade management.
[Chapter index](INDEX.md) / [Previous section](grade-versions-and-copying-modes.md) / [Next section](deleting-unused-versions.md)
<a id="source-the-importance-of-version-1"></a> <a id="source-the-versions-section-of-the-project-settings"></a> <a id="source-working-with-versions"></a>

### Working with Versions

A clip may carry as many local and remote versions as you wish. There are commands for building, renaming, and removing the versions open to each clip whether you work with the pointer or keyboard shortcuts. On top of that, DaVinci Resolve 15 brought the capacity to batch create, rename, load, and delete versions across several clips selected together. To quickly build a fresh local or remote version across one or several clips you’ve selected:

- Choose Color > Grade Version > Add (Command-Y). A fresh version appears, matching the version type chosen beforehand (remote or local), named “Version x” where x stands for the count of versions created so far. Every keyframe and motion track gets copied from the version selected earlier into the new one.

To build a fresh version across one or several selected clips while choosing a name and deciding about carrying keyframes: 1 Right-click any one of the chosen clip thumbnails, then pick one of these:

- Local Versions > Create New Version
- Remote Versions > Create New Version

2 Into the dialog that pops up, type a version name, and select either “Copy all marks” or “Copy the first mark only,” based on whether each keyframe should travel into the new version. NOTE: Motion tracking travels across regardless of whether “Copy all marks” is selected. 3 If you wish, grab a preset version name from the drop-down list. Those names are established within the Project Settings’ General Options panel, in its Versions section. 4 Click OK. To remove one particular version from one or several selected clips:

- Right-click any one of the chosen clip thumbnails, open the submenu for whichever remote version you’re removing (note it cannot be the one presently active), and choose Delete.

To delete all versions for one or more selected clips:

- Right-click any one of the chosen clip thumbnails, then from the contextual menu pick whichever of these commands fits the range of versions you intend to remove;
- Local Versions > Delete All Versions
- Remote Versions > Delete All Versions
- Delete All Versions

Every version gets deleted as directed, apart from the version currently selected, which is now the only one left. To bring up a specific remote or local version across one or several chosen clips:

- Right-click any one of the chosen clip thumbnails, open the submenu for the matching remote version you’d like duplicated, and choose Load.

To relabel the version on one or several selected clips: 1 Right-click whichever of the chosen clip thumbnails you like, open the submenu for the matching remote version you’re renaming, and choose Rename. 2 Inside the Version Name dialog, key a name into the text field. If you wish, grab a preset version name off the drop-down list. Such names originate in the Project Settings, under the General Options panel’s Versions section.

Choosing a Version name out of the dropdown list, whose entries originate from what you assigned over in the Project Settings, within the General Options panel’s Versions area 3 Click OK. That name then appears below the clip thumbnail over in the Timeline. If you plan on using predefined version names, they have to be configured within the Project Settings’ General Options panel, under its Versions group. A set of ten drop-down menus lets you pick from preset version names or type in your own. Such names will then show in the drop-down menu of the Version Name dialog.

### The Versions section of the Project Settings

### The Importance of “Version 1”

DaVinci Resolve has certain operations where “Version 1,” also called “the default version,” is the sole version applied, no matter how many other versions exist or which version had been selected beforehand. You may name the default version whatever you like, but regardless of that name, the default version sits first in the list, and it matters. A few cases illustrate this: Importing additional timelines that use the same clips: For this case, when bringing in timelines while ”Use local version for new clips in timeline” sits disabled within the Project Settings’ General Options panel under its Color section, then relinking touches only each clip’s default version. Whenever you switch a timeline between local and remote versions: In this situation, every clip across the Timeline drops to the default version, regardless of whatever you’d picked earlier. For that reason, should you plan to reconform your clips against a fresher cut of the edit being imported, or follow other unconventional workflows, it pays to make certain that, no matter how many versions you eventually produce, your most crucial grade is always copied back onto the default version. Quickly placing any version onto the default version goes like this: 1 Choose Color > Memories > Save Memory A (Option-1). Any memory slot works, though Memory A suits this illustration. 2 Now choose Color > Grade Version > Default (Command-U). 3 Finally, choose Color > Memories > Load Memory A (Command-1) so the stored memory lands on the default version. For an instant jump straight to the default version, do one of the following:

- Choose Color > Grade Version > Default (Command-U).
- Press DEFAULT VERSION on the T-bar panel.
