# Display audio clip waveforms in media pool and media storage and deleted timeline backups

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the media page.
[Chapter index](INDEX.md) / [Previous section](thumbnail-list-and-metadata-views-in-the-media-pool.md)
<a id="source-audio-meters-exposed"></a> <a id="source-audio-panel"></a> <a id="source-clip-metadata-editor-showing-the-clip-details-panel"></a> <a id="source-customizing-the-media-page"></a> <a id="source-deleted-timeline-backups"></a> <a id="source-display-audio-clip-waveforms-in-media-pool-and-media-storage"></a> <a id="source-dual-monitor-layout"></a> <a id="source-metadata-editor"></a> <a id="source-the-media-page-in-dual-screen-mode"></a> <a id="source-undo-and-redo-in-davinci-resolve"></a>

### Display Audio Clip Waveforms in Media Pool and Media Storage

Within the Media Pool option-menu sits a Show Audio Waveforms choice. Enabling it makes each audio clip in the Media Pool display an audio waveform inside its thumbnail region. Provided Live Media Preview is active in the Source Viewer, you're then able to scrub a clip and listen to what it holds. Should you prefer not to view audio waveforms, simply switch this choice back off.

### Deleted Timeline Backups

Choosing Deleted Timeline Backups from the Media Pool Options menu lets you inspect timelines you've removed along with whatever backup files exist for each one. From there you can pick backups to bring back, or opt to erase chosen backups for good.

### Metadata Editor

A Metadata Editor lives on both the Media and Edit pages. Pick a clip anywhere on the Media page and its metadata shows up in the Metadata Editor. Selecting several clips at once leaves only the final clip's details on view. Across the top, the Metadata Editor's header holds read-only facts about the chosen clip: its file name and directory; its duration; the video codec, the frame rate, and the resolution; the audio codec together with the sample rate; plus the channel count. Given how enormous the pool of metadata fields is, a pair of drop-down menus up top lets you swap which collection of metadata the Metadata Editor presents.

Metadata Presets (to the left): Whenever you've built your own custom metadata sets through the Metadata panel of the User Preferences, this drop-down picks which of them to display. Unsurprisingly, its starting value is “Default.” Metadata Groups (to the right): With this drop-down menu you move between the assorted metadata groups on offer, each grouped around particular tasks or workflows. What really drives the Metadata Editor is the run of editable fields sitting below the header, where you inspect and revise the various metadata criteria provided.

### Clip Metadata Editor showing the Clip Details panel

### Audio Panel

By way of an option menu, the Audio Panel can sit in either of two modes. Under the default Meters mode, audio meters appear that report the audio levels of the clips you play back. Switch to Waveform mode and you can place audio clips beside video clips in the Viewer to line them up by hand. Set to Levels mode, it lets you examine the audio carried inside clips you've brought into the Media Pool. While a clip plays, every audio meter reflects the levels of whichever of those tracks hold audio. The Viewer carries a Mute button for turning audio playback off and back on. To learn more about hand-syncing audio to video, consult Chapter 21, “Syncing Audio and Video.”

### Audio Meters Exposed

### Dual-Monitor Layout

A dual-monitor layout on the Media page devotes the most room on the primary monitor to the Media Storage browser and Media Pool, while the secondary monitor carries an enlarged Viewer, Audio Panel, and Metadata Editor plus a full bank of video scopes to help you judge media as you sort it. You can resize the second screen of a dual-screen layout, though you can't rearrange it. Owning just one ultra-wide monitor doesn't shut you out of the Dual-Monitor Layout; DaVinci Resolve will fit the interface as though two ordinary monitors stood side by side. Entering dual screen mode works like this:

- Choose Workspace > Dual Screen > On.

### The Media page in dual-screen mode

To flip which UI elements land on which monitors: Choose Workspace > Primary Display > Display 1 or Display 2, an action that swaps what each of the two monitors shows while in dual screen mode.

### Customizing the Media Page

You can tailor the Media Page to open up extra room in various spots for the task at hand. To resize any region of the Media page: Drag the vertical or horizontal divider sitting between two panels so one grows while the other shrinks. Ways to conceal individual parts of the Media page: Show or hide the Clone Tool by clicking its Clone Tool button along the UI toolbar up top. Show or hide the Audio Panel through the Audio button on that same top toolbar. Toggling the Metadata Editor is a matter of clicking the Metadata button in the toolbar overhead. As for the Media Storage browser folder list, flip it on or off via the button tucked into the top-left of the Media Browser. The Media Pool Bin list likewise switches on or off from the button at that pool's top-left corner. Ways to manage favorite file system locations inside the Media Storage browser: Adding a favorite means right-clicking any folder within the Media Storage browser folder list, then picking “Add folder to favorites” off the contextual menu. Dropping a favorite means right-clicking the one you'd like gone, then picking “Remove folder from favorites” off that same contextual menu. Restoring every page to its default arrangement is done by choosing Workspace > Reset UI Layout.

### Undo and Redo in DaVinci Resolve

Wherever you happen to be inside DaVinci Resolve, the Undo and Redo commands let you reverse actions or commands you've carried out, then reinstate them should you have second thoughts. DaVinci Resolve can roll back the complete record of everything you've done since you first made or opened a given project. Closing a project clears its entire undo history. When you next start working on that project, the undo history begins fresh. Since DaVinci Resolve packs so much capability into a single application, three distinct undo “stacks” exist to keep your work organized.

- A single multiple-undo stack is shared by the Media, Cut, Edit, and Fairlight pages, letting you step back out of edits you've performed across the Media Pool, within the Timeline, inside the Metadata Editor, and among the Viewers.
- Over on the Fusion page, every clip keeps its own undo stack, so you can reverse the compositing changes on each clip on its own.
- Likewise on the Color page, each clip carries its own undo stack, letting you reverse grading changes per clip independently. Across the board, the count of undoable steps has no real ceiling (though your own memory may be another matter). To make use of this, there are three routes for undoing work and returning your project to an earlier state, whatever page you happen to be on.

To reverse or reinstate your edits one step at a time: Choose Edit > Undo (Command-Z) to drop the most recent change. Choose Edit > Redo (Shift-Command-Z) to move forward to the next change. Several steps can also be undone together through the History submenu and window. As things stand now, this multi-step undo is limited to the Media, Cut, Edit, and Fairlight pages. To undo and redo via the History submenu: 1 Open the Edit > History submenu, which lists as many as the last twenty actions you've taken. 2 Pick an entry in the list to roll back to that moment. Your most recent action sits at the top of the list, with the change you just made marked by a check beside it. Steps you've undone that can still be reinstated linger in this menu, so the available options stay visible. That said, once you undo a batch of changes and then introduce a new one, further undo becomes impossible and those steps vanish from the menu.

The History submenu, your means of undoing a batch of steps together

After you choose a step to roll back to, the menu shuts and the project refreshes to reflect where it now stands. To undo and redo through the Undo window: 1 Choose Edit > History > Open History Window. 2 Once the History dialog opens, click an entry in the list to revert to that point. In contrast to the menu, here your most recent action sits at the bottom of the list. Picking a change grays out the ones still open to redo, while the project refreshes to reflect where it now stands. 3 Once finished, close the History window.

The Undo history window, where you can scan through the whole undo stack available for the current page
