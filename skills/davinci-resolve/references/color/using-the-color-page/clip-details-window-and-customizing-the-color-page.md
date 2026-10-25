# Clip details window and customizing the color page

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the color page.
[Chapter index](INDEX.md) / [Previous section](curves-palette-and-colorslice-palette.md)
<a id="source-customizing-the-color-page"></a> <a id="source-the-clip-details-window"></a> <a id="source-undo-and-redo-in-davinci-resolve"></a> <a id="source-using-the-color-page-part-2"></a>

### The Clip Details window

None of this is editable; it’s provided for easy reference, and it includes:

File Name Start Timecode End Timecode Duration Frames Reel Name Version Format Codec Folder Description Comments EDL Comments

At the top sits the media’s disk file name. The first frame’s source timecode value within the clip. The last frame’s source timecode value within the clip. How long the clip runs, expressed in timecode. How long the clip runs, expressed in frames. That clip’s reel name, provided one is being read correctly. Which remote or local version the clip uses. The format the source clip uses, together with its frame size and bit depth. Which codec the source clip uses. The disk directory where the source media lives. The Metadata Editor’s description field. The Metadata Editor’s Comments field. Any EDL comments tied to that event, where they exist.

### Customizing the Color Page

The Color page’s assorted sections can be resized, hidden, and rearranged as needed to suit different working styles. This section covers every method available for Color page customization. It’s easy to resize the Viewer, Gallery, and Nodes Editor against one another, so you can make the Viewer bigger, broaden the Node Editor for extra workspace, or free up more or less space for stills inside the Gallery. To resize the Viewer, Gallery, and Node Editor: hover the pointer over the vertical divider sitting between any two areas. When the resize icon appears, drag that divider sideways to enlarge one area at the other’s expense. In the same way, the Gallery, the Memories, the Node Editor, and the Keyframe Editor can each be expanded fully to take over whatever interface area lies next to them. To expand the Keyframe Editor, Viewer, and Gallery: click the Expand control in the top right of whichever interface area you want enlarged. Click the Expand control once more afterward and that area shrinks back to its starting size, bringing back whatever had been hidden. Within Display mode the Viewer can be hidden completely, shoving the Gallery to the far right of the DaVinci Resolve window while the Node Editor stretches to fill the remainder. To toggle Display mode: right-click in the Node Editor’s empty area and pick Toggle Display Mode off the contextual menu. Repeat to switch Display Mode off and set the interface back the way it was.

To reveal or conceal the Mini-Timeline: click the Timeline button sitting at the far right of the palette button bar. To reveal or conceal the Color page Viewer’s upper toolbar: open the Viewer option menu and pick Show Viewer Options to clear its checkmark. To send every page back to its default layout: choose Workspace > Reset UI Layout.

### Undo and Redo in DaVinci Resolve

Wherever you happen to be in DaVinci Resolve, the Undo and Redo commands let you step out of actions you’ve taken or commands you’ve run, and reapply them should you change your mind. DaVinci Resolve can undo the whole history of what you’ve done since you created or opened a given project. Close a project and its entire undo history is wiped; the next time you take up that project, its undo history begins fresh. Since DaVinci Resolve packs so much capability into a single application, it keeps three distinct sets of undo “stacks” to help you stay organized.

- The Media, Cut, Edit, and Fairlight pages draw on one shared multiple-undo stack, letting

you retrace your steps out of changes made within the Media Pool, the Timeline, the Metadata Editor, and the Viewers.

- On the Fusion page, every clip keeps a separate undo stack, letting you roll back compositing tweaks for that one clip on its own.
- On the Color page, each clip likewise carries its own undo stack, so grade changes can be reversed clip by clip without affecting the others.

For all of these, the count of steps you can step back through is effectively unbounded (though your own memory of them might run out first). To make the most of that, three different methods let you walk a project back to an earlier state regardless of which page you happen to be on. If you just want to step backward or forward one change at a time:

- Choose Edit > Undo (Command-Z) to undo the previous change.
- Choose Edit > Redo (Shift-Command-Z) to redo to the next change.
