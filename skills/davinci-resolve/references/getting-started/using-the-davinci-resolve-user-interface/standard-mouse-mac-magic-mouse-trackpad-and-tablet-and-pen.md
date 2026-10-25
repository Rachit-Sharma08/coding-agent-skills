# Standard mouse mac magic mouse trackpad and tablet and pen

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the DaVinci resolve user interface.
[Chapter index](INDEX.md) / [Previous section](scroll-and-middle-mouse-button.md)
<a id="source-2-finger-touch"></a> <a id="source-keyboard-shortcuts"></a> <a id="source-scroll-3"></a> <a id="source-standard-mouse-mac-magic-mouse-trackpad"></a> <a id="source-tablet-and-pen-2"></a> <a id="source-undo-and-redo-in-davinci-resolve"></a> <a id="source-using-the-davinci-resolve-user-interface-part-2"></a>

### Standard Mouse Mac Magic Mouse Trackpad

### Tablet and Pen

Pan Left and Right

—

—

—

### Scroll

Context Menu

— Right Button

### 2 Finger Touch

Right button on the pen.

Gestures employed across common input devices within DaVinci Resolve

### Keyboard Shortcuts

Because most people running DaVinci Resolve are on macOS, every shortcut in this manual follows the macOS style built around the Command key and the Option key. For everyone on other platforms, each shortcut that relies on the macOS Option key maps to the ALT key on Windows and Linux, and each shortcut built on the macOS Command key maps to the Control key on those systems.

TIP: To hold the controls consistent across macOS, Windows, and Linux, no default shortcut is bound to the macOS Control key. You're free to map your own shortcuts onto the Control key, though, which unlocks an entirely fresh set of shortcuts just for your own macOS workflow.

### Undo and Redo in DaVinci Resolve

Wherever you happen to be in DaVinci Resolve, the Undo and Redo commands let you reverse steps or commands you've carried out and then put them back if you reconsider. DaVinci Resolve can roll back the full record of everything you've done since you created or opened a given project. Closing a project clears that project's complete undo history. When you next open the project, its undo history begins fresh from zero.

Since DaVinci Resolve packs so many capabilities into one application, DaVinci Resolve keeps three independent undo “stacks” to help you stay on top of your work.

- A single shared multiple-undo stack spans the Media, Edit and Fairlight pages, so you can step back through edits you made across the Timeline, the Metadata Editor, the Viewers, and the Media Pool.
- On the Fusion page, every clip carries its own undo stack, so you can independently undo edits to each clip's composition.
- On the Color page, every clip likewise has its own undo stack, so you can independently undo edits to each clip's grade.

Across the board, there's no real ceiling on how many steps you can undo (though your memory may impose one of its own). To capitalize on that, three approaches let you roll work back to an earlier project state regardless of the page you're on. For plain one-at-a-time undo or redo of your edits:

- Pick Edit > Undo (Command-Z) to reverse whatever you changed most recently.
- Pick Edit > Redo (Shift-Command-Z) to step forward to the change you just reversed.

Reverting many edits in one move is also possible through the History submenu and its window. As of this writing, that multi-step capability is limited to the Media, Cut, Edit, and Fairlight pages. Here is how stepping backward or forward via that submenu works: 1 Open the Edit > History submenu, which lists (up to) the twenty most recent actions you’ve taken. 2 Pick any entry to roll the project back to that moment. Your latest action sits at the top of the listing, and whatever you just did carries a check mark beside it. Entries you’ve reversed yet could still reapply stay visible in this menu, letting you gauge your remaining options. That said, once you reverse a batch of edits and then introduce a fresh change, further undo is no longer available and those reversed entries vanish from the menu. The instant you pick a step to revert to, the menu dismisses and the project refreshes to reflect its present condition.

The History submenu, the tool for rolling back multiple steps in a single action

Stepping backward or forward by way of the separate Undo window goes like this: 1 Choose Edit > History > Open History Window. Once the History dialog opens, pick an entry from the listing to revert the project to that moment. In contrast to the menu, here your latest action is shown at the foot of the listing. Picking a change in this view dims the changes that remain reapplicable, while the project refreshes to reflect its present condition. 2 After you finish, shut the History window.

The Undo History window, where you can scan through the full undo stack on hand for the page in view
