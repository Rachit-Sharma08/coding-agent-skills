# Two up display when rolling an edit and two up display when rippling an edit

Version: DaVinci Resolve 20.3 Reference Manual. Context: Trimming.
[Chapter index](INDEX.md) / [Previous section](trim-tool-and-selection-based-trimming.md) / [Next section](timecode-entry-selection-and-trim-commands.md)
<a id="source-function"></a> <a id="source-function-1"></a> <a id="source-function-2"></a> <a id="source-important-trimming-keyboard-shortcuts"></a> <a id="source-key-shortcut-shift--shift-command--shift-command-"></a> <a id="source-key-shortcut-t-a-command-l-and-j-w"></a> <a id="source-the-precision-trim-editor"></a> <a id="source-trim-tool-operations-with-the-keyboard"></a> <a id="source-trimming-edits-in-the-timeline-viewer"></a> <a id="source-trimming-using-timecode-entry"></a> <a id="source-turning-off-the-heads-up-display-while-you-trim"></a> <a id="source-two-up-display-when-rippling-an-edit"></a> <a id="source-two-up-display-when-rolling-an-edit"></a>

### Two-up display when rolling an edit

- Ripple edit: To ripple the outgoing or incoming part of an edit, adding or removing media from a clip while at the same time shifting every other clip to the left in the Timeline to open space, click the Trim tool and drag an edit point to a fresh spot in the Timeline.

Selected outgoing half of an edit point before ripple

Now shorter, the rippled clip leaves the remainder of the Timeline shifted leftward to close the gap. When you ripple an edit, a 2-up display reveals how the action carries from the outgoing frame of the clip on the left to the incoming frame of the clip on the right. The frame that refreshes hinges on which side of the edit you're rippling.

TIP: You can briefly turn off this two-up display by holding the Shift key as you ripple, leaving only the frame at the playhead position visible. That lets you watch which frame crosses the playhead while you ripple the Timeline. To switch this two-up display off entirely, select View > Enable Multiview Edit Preview.

### Two-up display when rippling an edit

### Turning Off the Heads Up Display While You Trim

Holding the Shift key during most drag and trim operations lets you suspend the multi-frame heads up displays that show up in the Timeline window, so you can concentrate on the frame that meets the playhead. Switching those two- and four-frame heads up displays on or off is done one way: Choose View > Enable Multiview Edit Preview.

### The Precision Trim Editor

The Edit Page viewer offers an upgraded trim mode much like the precision trim editor of the Cut page. It swaps the source viewer for one large display showing frame changes on both sides of your edit, so you get a closer look at the edit point. As soon as trimming wraps up, it reverts to its earlier state on its own. The Precision Trim Editor shows up automatically when you carry out a trim operation, or when you double-click an edit point. Should you favor the older trim editor, which leaves the source viewer in place, you can turn this off via a User Preference under DaVinci Resolve > Preferences > User > Editing, by selecting or clearing the box beside "Automatically switch to single viewer mode when opening trim editor."

### Trimming Edits in the Timeline Viewer

Double-clicking any edit point between two clips in the timeline opens the Precision Trim Editor, a detailed way to adjust both halves of an edit point. A graphical A/B roll interface presents two filmstrips, the outgoing clip on top and the incoming clip on the bottom. You can drag these controls:

- To trim the outgoing clip's Out point, drag the left edge of the handle on the top filmstrip.
- To trim the incoming clip's In point, drag the right edge of the handle on the bottom filmstrip.
- For a roll of the edit point, drag the white handle sitting between the upper and lower filmstrips,

adjusting the outgoing and incoming edit points together. Numbers above each frame show you precisely how many frames you're trimming, and a pair of buttons flanking the transport controls in the Viewer toolbar let you shift the outgoing clip's Out point and the incoming clip's In point one frame at a time.

The Precision Trim Editor, as it appears after a double-click on a timeline edit

### Trim Tool Operations With the Keyboard

The Nudge keyboard shortcuts also let you carry out every trim operation with greater precision. To trim with the keyboard: 1 Press T to choose the Trim tool. 2 Trim the selection using any one of these approaches: To slide a clip: With a clip chosen via Shift-V, tap the Comma key for a single-frame leftward slip, or the Period for a single-frame rightward one. Holding Shift-Comma and Shift-Period moves the clip in 5-frame steps. To slip a clip: After Shift-V picks a clip, hit the S key to switch into Slip mode (a further S returns you to Slide mode), then use Comma or Period to drive its contents leftward or rightward. Here Shift-Comma and Shift-Period shift the contents in 5-frame steps. To roll an edit: With V selecting an edit point, tap the Comma key to nudge leftward by one frame, or the Period to nudge rightward by one. Shift-Comma and Shift-Period roll that edit in 5-frame steps. To ripple an edit: After V picks an edit point, press U to isolate just the incoming or outgoing side of that edit. From there, the Comma key ripples the chosen In or Out point of the clip leftward, while the Period sends it rightward by a frame. In this case Shift-Comma and ShiftPeriod ripple in 5-frame steps. 3 Should you wish to suspend the 2- or 4-up display that turns up in the Timeline Viewer mid-trim, the route is Choose View > Enable Multiview Edit Preview, which switches those trimming displays on and off. TIP: When you hold the Shift key while nudging to perform a "fast nudge," the length of the nudge can be set in the Editing panel of the User Preferences. Its default sits at five frames, though you may dial in any value you wish.

### Important Trimming Keyboard Shortcuts

When you trim with the keyboard, the shortcuts below are worth committing to memory. The majority of these commands, plus many more that have no shortcut assigned, are also available in the Trim menu. A good number of them can be remapped to different shortcuts via the User Preferences' Keyboard Mapping panel. For more information, see Chapter 4, "System and User Preferences."

Default shortcuts use the manual’s macOS modifier names.

| Shortcut | Action |
| --- | --- |
| T | Trim mode: ripple edits, slip or slide clips |
| A | Selection mode: resize edits or move clips |
| Command-L; Command-J | Fast trim forward; reverse at normal playback speed |
| W | Dynamic trim/resize with JKL |
| S | Toggle Slip/Slide for a selected clip in Trim mode |
| V | Select nearest edit and move playhead there |
| Shift-V | Select the clip/gap at the playhead; disable Auto Select on unwanted overlapping tracks |
| Shift | Temporarily hide the 2-up/4-up trim display |
| Option-F1 through F9 | Toggle video Auto Select for tracks 1–9 |
| Command-Option-F1 through F9 | Toggle audio Auto Select for tracks 1–9 |
| U | Cycle outgoing, centered, incoming edit selection |
| Option-U | Cycle video+audio, video-only, audio-only selection |
| Comma | Nudge left one frame; Shift uses the configurable fast-nudge interval, default five frames |
| Period | Nudge right one frame; Shift uses the configurable fast-nudge interval, default five frames |
| / | Preview around playhead, selected edit, clip, or multiple clips; pre/post-roll is configurable |
| Command-/ | Toggle loop playback |
| Down; Up | Next; previous edit and selection, visiting overlapping clips from lowest track upward |
| E | Extend selected edits to the playhead |
| Shift-[ | Trim Start: resize in Selection mode or ripple in Trim mode on auto-select-enabled tracks |
| Shift-] | Trim End: resize in Selection mode or ripple in Trim mode on auto-select-enabled tracks |
| Shift-Command-[ | Ripple Trim Start to playhead regardless of mode |
| Shift-Command-] | Ripple Trim End to playhead regardless of mode |

IMPORTANT: The Slip, Roll, and Slide tools alter the sync relationship of whichever clips you're adjusting against a matching soundtrack, yet leave the rest of the Timeline untouched. Ripple, by contrast, can shift the overall sync relationship across large stretches of your timeline and its matching soundtrack, so reach for it only with extreme care.

### Trimming Using Timecode Entry

Absolute or relative timecode entry is another way to trim clips and edits. Exactly what gets trimmed comes down to whatever selection you set before typing the timecode. To use timecode for trimming the selection forward from where it currently sits, make sure to type an equal sign or plus (= or +) ahead of the timecode value; to trim the selection backward in relative terms, type minus (–) ahead of the timecode value.

- To roll an edit: Pick the center of an edit point, key in a timecode value, then press Return.
- To ripple an edit: Pick either the outgoing or incoming half of an edit point, then key in a timecode

value, and press Return.

- To slip a clip: Pick a clip, pressing S where needed to switch into Slip mode, then key in a timecode

value, and press Return.

- To slide a clip: Pick a clip, pressing S where needed to toggle to Slide mode, then key in a timecode

value, and press Return.
