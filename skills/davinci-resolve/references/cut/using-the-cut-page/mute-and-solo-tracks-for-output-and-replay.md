# Mute and solo tracks for output and replay

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the cut page.
[Chapter index](INDEX.md) / [Previous section](edit-actions-and-all-of-the-edit-actions-functions.md)
<a id="source-mute-and-solo-tracks-for-output"></a> <a id="source-replay"></a> <a id="source-the-cut-page-timeline-controls"></a> <a id="source-undo-and-redo-in-davinci-resolve"></a>

### Mute and Solo Tracks For Output

Activating the Mute or Solo controls within the Audio Mixer turns track audio off, not only while playing back but also when delivering for output. Be certain you have switched any tracks you require back on before you move on to the Deliver page. Mute and solo tracks can be changed only from the Edit, Cut, and Fairlight pages.

### Replay

On the Cut page you can do live multi-camera broadcast editing, playout, and replay complete with speed control. A number of the Replay features show up only alongside Blackmagic Design hardware, for instance a desktop video interface, cloud store and ATEM switcher.

For fuller detail, please refer to the dedicated DaVinci Resolve Replay Editor Instruction Manual.

### The Cut page Timeline controls

### Undo and Redo in DaVinci Resolve

Wherever you happen to be inside DaVinci Resolve, the Undo and Redo commands let you reverse steps or commands you have carried out, and then put them back should you reconsider. DaVinci Resolve can roll back the whole record of what you have done ever since you created or opened a given project. Closing a project wipes its complete undo history. The following time you return to a project, its undo history begins fresh. Since DaVinci Resolve packs so much capability into a single application, three distinct sets of undo “stacks” exist to help you stay on top of your work.

- The Media, Edit and Fairlight pages all draw on one shared multiple-undo stack, which lets you reverse edits you performed across the Media Pool, plus the Timeline, along with the Metadata Editor, as well as the Viewers.
- Within the Fusion page, every clip keeps its own undo stack, so each clip’s composition changes can be undone on their own.
- Within the Color page, every clip keeps its own undo stack, so each clip’s grade changes can be undone on their own.

For every one of these, there is effectively no ceiling on how many steps you may undo (though your own memory might be the real limit). To make use of that, three approaches exist for undoing work and returning to an earlier state of your project, whatever page you are on. When you simply want to undo or redo your changes one step at a time:

- Pick Edit > Undo (Command-Z) to reverse the most recent change.
- Pick Edit > Redo (Shift-Command-Z) to move forward to the next change.

There is also a way to undo a number of steps in one go by means of the History submenu and window. As of this writing, this multi-step undo is limited to the Media, Cut, Edit, and Fairlight pages.

To undo and redo by way of the History submenu: 1 Open the Edit > History submenu, which lists (at most) the previous twenty actions you have taken. 2 Click an item in the list to roll back to that point. The action you took most recently sits at the top of the list, and the change you just made is marked with a check beside it. Steps you have undone that remain available to redo stay visible in this menu, so you can tell what options exist. That said, once you have undone a handful of changes and then make a fresh change, further undo is no longer possible and those steps vanish from the menu. The History submenu, which lets you roll back through a run of steps in one move Once you have picked a step to roll back to, the menu shuts and the project refreshes to display its present state. To undo and redo by way of the History window: 1 Pick Edit > History > Open History Window. 2 When the History dialog opens, click an entry in the list to roll back to that point. In contrast to the menu, here the action you took most recently sits at the bottom of the list. Picking a change in this view dims the changes still open to redo, while the project refreshes to display its present state. 3 Once you are finished, shut the History window.

The Undo history window through which you can scroll across the whole undo stack on hand for the page you are on
