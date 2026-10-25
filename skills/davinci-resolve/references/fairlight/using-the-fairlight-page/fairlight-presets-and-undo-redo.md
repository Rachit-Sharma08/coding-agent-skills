# Fairlight configuration presets and undo and redo in DaVinci resolve

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](timecode-and-fairlight-synchronization-settings.md)
<a id="source-fairlight-configuration-presets"></a> <a id="source-undo-and-redo-in-davinci-resolve"></a>

### Fairlight Configuration Presets

Whole configuration presets for the Fairlight page, or for individual portions of it, can be stored and recalled via the Presets Library functions, which sit under Fairlight > Presets Library. To read up further on working with the Presets Library, turn to Chapter 171, “Setting Up Tracks, Busses, and Patching.”

### Undo and Redo in DaVinci Resolve

Wherever you happen to be in DaVinci Resolve, the Undo and Redo commands let you reverse steps or commands you've carried out, then reinstate them should you change your mind. DaVinci Resolve can roll back the whole sequence of actions you've taken since a given project was created or opened. Closing a project wipes its entire undo history. When you next sit down with that project, its undo history begins fresh. Because so much capability is rolled into this one application, DaVinci Resolve keeps three distinct undo “stacks” to help you stay on top of your work.

- One shared multiple-undo stack serves the Media, Edit and Fairlight pages together, so you can reverse work done across the Media Pool, the Timeline, the Metadata Editor, plus the Viewers.
- Every clip on the Fusion page carries its own undo stack, so you can roll back the changes to each clip's composition on its own.
- Every clip on the Color page carries its own undo stack, so you can roll back the changes to each clip's grade on its own.

Across the board, there's no real ceiling on how many steps can be undone (though your own memory may impose one). To make use of that, you have three ways to undo work and return your project to an earlier state, regardless of which page you're on. To plainly undo or redo your changes one at a time:

- Choose Edit > Undo (Command-Z) to undo the previous change.
- Choose Edit > Redo (Shift-Command-Z) to redo to the next change.

The History submenu and window also let you undo a number of steps at once.

For undoing and redoing through the History submenu: 1 Bring up the Edit > History submenu, where (at most) your last twenty actions are listed. 2 Click whichever entry you want to roll the project back to that moment. Your latest action sits at the very top of this list, and the change you just made carries a check beside it. Steps you've undone but can still redo stay put in this menu, so the available options remain visible. Note, though, that if you've undone a batch of changes and then make a fresh change, no further undo is possible and those steps drop off the menu.

The History submenu, which lets you undo several steps at once As soon as you choose a step to roll back to, the menu shuts and the project refreshes to display its present state. By way of the Undo window, here's how to undo and redo: 1 Choose Edit > History > Open History Window. 2 As soon as the History dialog shows itself, click a list entry to roll back to that spot. Unlike the menu, this window puts your most recent action down at the bottom of the list. Selecting a change here dims the changes still left to redo, while the project refreshes to mirror its present state.

The Undo history window, through which you can scroll the whole undo stack on hand for the page you're on 3 Once you've finished, shut the History window.
