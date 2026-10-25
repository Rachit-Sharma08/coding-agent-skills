# Audio selection and edit modes

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing basics in the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](compatible-audio-formats-and-adm-import.md) / [Next section](range-mode-and-multiclip-selection.md)
<a id="source-click-a-clip-to-select-it"></a> <a id="source-fairlight-edit-mode-remains-between-application-restarts"></a> <a id="source-making-audio-clip-selections-in-the-timeline"></a> <a id="source-selecting-tracks"></a> <a id="source-using-pointer-mode"></a> <a id="source-why-are-there-three-edit-modes"></a>

### Making Audio Clip Selections in the Timeline

Almost every editing action covered in this chapter and elsewhere asks you to make a selection that pins down which clips get affected. Three editing modes on the toolbar hand you different approaches to selecting clips, shaped by your goal and your working style. Reading left to right, they are the Pointer mode, the Range mode, and the Focus mode. The mode you pick dictates how clips and clip segments get selected on the Timeline ahead of every sort of editorial action.

The Pointer, Range, and Focus modes seen in the toolbar

### Fairlight Edit Mode Remains Between Application Restarts

Across restarts, Fairlight holds on to whichever Edit Mode the project was saved in. The edit mode you had active before quitting the application is the one that greets you on reopening.

### Why Are There Three Edit Modes?

Although the Pointer and Range modes work with the pointer too, their real purpose is to drive automatic selections keyed to where the playhead sits. That happens as you steer Timeline transport with the Fairlight Editing console, the Fairlight Desktop Console, or keyboard shortcuts while particular tracks are selected to permit selection and editing on them. Focus mode, by contrast, is built for quick selections drawn with the pointer through a mouse, trackpad, or pen and tablet, paired with an assortment of commands for stretching and editing selections fired off by keyboard shortcuts. For anyone cutting with a keyboard and mouse, this mode aims to keep you fast by switching on a range of selection behaviors tied to where on a clip you click.

### Selecting Tracks

Grasping clip selection means first grasping track selection. On the Fairlight page, the Timeline lets you select whole tracks so that clips crossing the playhead on those tracks get picked automatically through keyboard shortcuts, the Fairlight Desktop Console, or the Fairlight Editing panel while in Pointer and Range modes (both covered in sections ahead). Suppose you select tracks A2, A3, and A4: nudging the playhead in Pointer mode so it crosses two clips on those tracks selects them on its own, leaving them ready for whatever you want to do to both. As a sampling, you might now split the two at the playhead, apply Cut Head or Tail relative to it, Delete the pair, or Copy them to paste somewhere else. On top of that, clicking or dragging on one or more clips with the pointer will sometimes select those clips together with the tracks beneath them. Selecting clips via Focus mode, for one, also picks the tracks those clips live on.

Command-clicking several track headers selects those tracks When you select tracks by hand with the pointer, several approaches are open to you. Ways to select and deselect tracks on the Fairlight page Timeline:

- To select one track: Click somewhere in the header background, or hit that header’s track number (steer clear of a button). Under Range mode you may also click any empty spot on the track itself.
- To deselect one track: Click somewhere in the header background of an already-selected track, or hit its track number (not a button). Under Range mode you may also click any empty spot on the track itself. With several tracks selected, Command-clicking one peels just that track out of the selection.
- To select several tracks: Command-click in the track header background of each track you want. Under Range mode you may also Command-click any empty spot on the tracks themselves. A Command-click on a track that’s already selected deselects it.
- To select several adjacent tracks: Click anywhere in the background or on a track header’s track number, then drag a bounding box upward or downward across the other tracks you want. Under Range mode you may also drag a bounding box over any part of the tracks themselves, which simultaneously sets a range you wish to work within.
- To shift the selection up or down the tracks: Press Control-Option-Up Arrow or Down Arrow to carry the selection state to the next track up (Control-Option-Up Arrow) or down (ControlOption-Down Arrow). When several tracks are selected, the whole multi-selection moves as a block; selecting tracks A2 and A3 and then pressing Control-Option-Down Arrow, for instance, leaves tracks A3 and A4 selected.

### Using Pointer Mode

Pointer mode leans on where the playhead sits to make automatic selections whenever you select clips on chosen tracks through the Fairlight Editing console or keyboard shortcuts. You can equally pair this mode with the pointer and keyboard shortcuts for a different selection style. The chief aim of Pointer mode is to support quick editing of entire clips.

- When no tracks are selected: Clips the playhead crosses stay unselected. With the pointer you can grab a clip or several through a click, a Command-click, or a dragged bounding box. Clips chosen this way glow orange. Working like this mirrors how you select clips on the Edit page Timeline.
- When tracks are selected: Every clip the playhead crosses on the chosen tracks is highlighted automatically, though no In and Out points get set. Clips on deselected tracks are passed over. Grabbing a clip or several with the pointer (via a Command-click or a dragged bounding box) yields an orange-highlighted selection.
- When you set In and Out points: Certain functions act on ranges of clips lying between the In and Out points on chosen tracks. Clips on unselected tracks are passed over.

To switch on Pointer mode:

- Click the Selection tool (the arrow) on the toolbar.
- Choose Trim > Pointer mode.
- Press A.

To have the playhead position auto-select clips in Pointer mode: 1 Press A to drop into Pointer mode. 2 Select one or more tracks holding the clips you’re after. 3 Move the playhead so it crosses those clips. Each clip the playhead crosses on the Timeline’s chosen tracks gets selected automatically in full. The automatic selections glow brighter to mark them as selected. Crossed clips on tracks that aren’t selected stay unselected.

In Pointer mode, clips the playhead crosses get picked on their own and glow with orange highlights

Ways to select clips with the pointer:

- Click any clip and it’s selected.

### Click a clip to select it

- Command-click several clips to grab them all in one go.

Command-clicking several clips picks those clips even when other clips sit between them

- Click anywhere in the Timeline background and drag a bounding box across several clips.

Dragging a bounding box across several clips selects every one of them
