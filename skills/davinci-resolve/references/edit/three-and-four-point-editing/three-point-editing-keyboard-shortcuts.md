# Three point editing keyboard shortcuts

Version: DaVinci Resolve 20.3 Reference Manual. Context: Three and four point editing.
[Chapter index](INDEX.md) / [Next section](timeline-in-out-points-and-clip-marking.md)
<a id="source-choosing-a-track-to-edit-and-using-the-source-track-selector"></a> <a id="source-function-choose-media-pool-bin-list"></a> <a id="source-introduction-to-three-point-editing"></a> <a id="source-key-shortcut-f12"></a> <a id="source-keyboard-shortcuts-in-this-chapter"></a> <a id="source-shift-f10-shift-f11-shift-f12-undo-redo"></a> <a id="source-three--and-fourpoint-editing"></a> <a id="source-three-and-four-point-editing-part-1"></a>

### Three- and Four‑Point Editing

When you need tighter control over how footage lands in your program, three- and four-point editing lets you map a chosen span of source media onto a chosen span of the Timeline. The pages ahead walk through the fundamentals of these techniques and survey the broad range of edit commands they put at your disposal.

### Keyboard shortcuts

These use the manual’s macOS modifier names and default keyboard mapping.

| Shortcut | Action |
| --- | --- |
| Command-1 | Focus the Media Pool bin list. |
| Command-2 | Focus the Media Pool browser. |
| Arrow keys | Move the bin or clip selection. |
| Return or Enter | Open the selected clip or timeline in the Source Viewer. |
| Q | Toggle Source/Timeline Viewer focus. |
| I; O | Set In; set Out. |
| Shift-I; Shift-O | Go to In; go to Out. |
| Option-I; Option-O | Delete In; delete Out. |
| Shift-A | Mark the selected timeline clip. |
| X | Mark the timeline clip under the playhead. |
| Option-X | Delete both In and Out. |
| Command-Shift-Up/Down | Move video destination up/down. |
| Command-Option-Up/Down | Move audio destination up/down. |
| Option-1 through 8 | Set video destination; repeat to enable/disable. |
| Command-Option-1 through 8 | Set audio destination; repeat to enable/disable. |
| Option-F1 through F8 | Toggle video auto-select for that track. |
| Option-F9 | Toggle all video auto-selects. |
| Option-Command-F1 through F8 | Toggle audio auto-select for that track. |
| Option-Command-F9 | Toggle all audio auto-selects. |
| Option-Shift-Q | Toggle Switch to Timeline After Edit, enabled by default. |
| F9 | Insert selected clip(s) from Media Pool or Source Viewer. |
| F10 | Overwrite selected clip(s) from Media Pool or Source Viewer. |
| F11 | Replace with the first selected clip. |
| F12 | Place on Top. |
| Shift-F10 | Ripple Overwrite. |
| Shift-F11 | Fit to Fill. |
| Shift-F12 | Append to End. |
| Command-Z | Undo. |
| Command-Shift-Z | Redo. |

### Introduction to Three-Point Editing

Because three-point editing is a common editorial convention found across plenty of other post-production tools, the workflow should already seem natural to you. The principle is simple: place any three In and Out points across the source clip and Timeline to drop a clip into your program at a precise moment, and DaVinci Resolve works out the remaining fourth edit point on its own to carry out the edit. In practice, overwrite and insert edits are the usual vehicles for three-point editing.

### Choosing a Track to Edit and Using the Source Track Selector

Use the Source Track Selector to map the audio and video parts of a source clip onto the specific timeline tracks you intend them for. Pointing each track's destination control where it belongs is both a simple action and an essential part of building any edit.

In the Source Track Selector, blue denotes the source tracks on the left while red marks the timeline tracks over on the right

On the blue left-hand column you see the tracks belonging to whichever source clips are picked in the media pool or open in the source viewer (say, a clip carrying one video track V1 plus four audio tracks A1-6). The red right-hand column stands for the timeline's destination tracks (for instance, two video tracks V1-2 and six audio tracks A1-6). Through the Source Track Selector you assign each source-clip track to a particular timeline track. You can reach the source tracks either by dragging them onto different destination tracks or through the Timeline > Source Track Selector menu. To illustrate, grab the video portion of a source clip (blue v1) and place it on video track 2 of the timeline (red v2) by dragging the blue v1 icon over beside the red V2 icon. The equivalent menu route is Timeline > Source Track Selector > Select/Deselect v2.

Pulling the Source (blue) video track 1 across so it patches to the Timeline destination (red) video track 2 for editing into that track To route the destination tracks of incoming (blue) source clips, take any one of these approaches:

- Drag the blue source control onto whatever timeline track you want.
- Click the blue source control, then click whichever red destination control on the timeline you're after.
- Use Command-Shift Up Arrow and Down Arrow to shift the Video source control between video tracks, or Command-Option Up Arrow and Down Arrow to shift the Audio source control between audio tracks.
- Hit Option-1 through 8 to route a source to a video destination, and Option-Command-1 through 8 to route a source to an audio destination across tracks 1 through 8.
- Pick whichever command you need from the Timeline > Source Track Selector submenu, where every Source Track Selector choice appears next to its keyboard shortcut.

Audio sources offer one more selection route, since a clip can hold several of them rather than the lone video source. Right-click a blue source audio channel and choose a different source audio track from the context menu to send it to the timeline track instead.

As another option, right-click an audio source track (A3 blue) and use the context menu to pick a different source audio track that gets patched to timeline track A3 Red

When you'd like to bring a source video clip into the Timeline minus its audio (or the reverse), switch off the relevant Video or Audio destination controls. Here is how to turn a source or destination control off and back on:

- Click any source or destination icon that's already assigned to flip it off and then back on. A disabled destination control loses its highlight. Should repeated tweaking of the track selectors leave you muddled, you can return them to their default state at any time.

To return every track selector to default: choose Timeline > Source Track Selector > Reset Track Selectors.
