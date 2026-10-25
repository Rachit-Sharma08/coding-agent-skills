# Original timeline before a ripple trim operation and sync lock controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Trimming.
[Chapter index](INDEX.md) / [Previous section](timecode-entry-selection-and-trim-commands.md) / [Next section](multiedit-resize-roll-and-ripple.md)
<a id="source-sync-lock-controls"></a> <a id="source-the-original-timeline-before-a-ripple-trim-operation"></a> <a id="source-the-sync-lock-icon"></a> <a id="source-trimming-multiple-edits-or-clips-at-once"></a> <a id="source-using-manual-selections-to-control-which-clips-are-trimmed"></a> <a id="source-using-the-source-track-selector-to-control-trimming"></a> <a id="source-using-the-source-track-selector-to-control-which-clips-are-trimmed"></a>

### The original timeline before a Ripple Trim operation

The starting timeline appears above. Observe how the pink markers on the music track align with the blue markers placed on the source footage. Those pink markers indicate an emotional music beat sitting in flawless sync with the picture. Our aim is to keep that relationship intact as we ripple trim.

Following the ripple trim, the timeline reveals the music track being cut (red rectangle) so sync holds across every other track. Next we ripple trim to shorten an incoming clip in V1 (marked by the red arrow at the highlighted green line). Note how, as the ripple trim happened, every music marker held its sync, and the video clip on track 2 was trimmed by the identical amount as well. Achieving this required a cut at the edit point of the music track, which was then trimmed (red rectangle), leaving a jarring jump cut in that music track. That still needs handling, though it's a far simpler fix than re-syncing the entire timeline. Something had to yield, and the music track was the one sacrificed to keep every other track in sync. Ripple trimming this way, with all Sync Locks active, is generally the most efficient route for the bulk of work, but should you want to shield a particular track, just disable the Sync Locks on whichever timeline tracks you'd like to leave untouched while ripple trimming.

### Sync Lock Controls

Out of the box, sync lock is active on every track. This stops linked clips spread across different tracks from drifting out of sync while a ripple operation runs (for instance, when something is ripple deleted and the remainder of the timeline shifts left to close the gap). That behavior can occasionally cause you to accidentally overwrite a portion of a track you meant to keep, and not every track genuinely has to remain in sync.

To cover those occasions, there's an icon (just right of the track lock icon) controlling the ripple on/off behavior per track. This sync lock toggle operates separately from the source track selector, letting you switch sync on or off according to track type without fussing over toggling track selection states. While it's on, the track ripples alongside the other tracks. While it's off, ripple still functions on its own for that track, but the track won't ripple in response to edit operations occurring on other tracks.

### The Sync Lock icon

What follows is an illustration of how Sync Locks can be applied during Ripple Editing to accomplish different goals

The original timeline before a Ripple Trim operation.

The resulting ripple with all the Sync Locks on

When every Sync Lock is on, running the ripple on EE additionally cuts and trims the video and audio tracks of DD at the ripple point, ensuring the relative sync between EE and DD holds now that EE has been shortened.

The resulting ripple with the Sync Locks off on V1 and A1 Once the Sync Locks are switched off on V1 and A1, carrying out the ripple on EE leaves DD unaffected, but the clips fall out of sync.

### Using the Source Track Selector to Control Trimming

Each track in the Timeline carries Source Track Selector buttons that drive a wide range of operations, broadly indicating that the chosen track is ready to be acted upon. While a track's Track Selector and control is on, clips residing on that track are taken in automatically by these kinds of operations:

- Operations affecting clips that intersect the playhead's location
- Operations affecting clips that intersect a region bounded by timeline In and Out points

While a track's Source Track Selector control is off, those same operation categories skip the clips on that track, unless you select one or more clips or edit points by hand. The sections coming up explain in depth how the Source Track Selector buttons let you steer the trimming operations described in this chapter, plus the variety of "playhead-targeted" trim operations described later on. For additional detail on applying the Source Track Selector controls to define selections and govern other editing operations, see Chapter 36, "Editing Basics."

### Using the Source Track Selector to Control Which Clips Are Trimmed

A primary purpose of the Source Track Selector controls is to give keyboard shortcut-driven editors a way to pick exactly which clips on which tracks an operation will touch, when that operation would otherwise hit every superimposed clip at the playhead's location or enclosed by In and Out points placed in the timeline. As an example, picture several clips stacked across V1, V2, and V3, plus A1, A2, and A3, with the Source Track Selector (red) controls active on all six of those tracks; park the playhead over one of them and run Trim End from Selection mode, and every one of the six stacked clips is trimmed.

Trimming all clips at the position of the playhead

If, however, you wish to trim only the clip in track V3, you can solo that track's Source Track Selector control by Option-clicking it, and then invoking the Trim End command trims the clip on V3 alone, leaving the rest of the clips untouched.

Soloing the V3 Auto Select controls so that the trim affects the V3 clip alone

### Using Manual Selections to Control Which Clips Are Trimmed

Worth remembering: any manual selections you make in the Timeline that highlight particular clips always override whatever the Source Track Selector controls happen to be. For instance, if Source Track Selector is on for tracks V1, V2, and V3, yet you've selected a clip on track V1, only that selected clip will still be affected by whichever operation you choose to run. So if you use Trim End, the clip on track V1 is what gets affected.

A hand-picked clip on track V1 takes priority over the Source Track Selector controls across every track

### Trimming Multiple Edits or Clips at Once

DaVinci Resolve lets you pick several edit points or clips for certain trimming operations, so you can trim multiple edits and clips simultaneously. For straightforward cases, this makes it simple to resize, ripple, slip, and slide a number of superimposed clips together, a genuine time-saver, or you might select the In point of every title generator across a credit sequence at once to prepare for shortening or lengthening them all together. For trickier cases, this opens up more elaborate trimming setups, like multi-track asymmetric trimming, to dispatch difficult tasks quickly. However ambitious the trim operation you intend to build, the procedure stays precisely the same as for a regular trim operation. Just make certain you observe these three broad steps and you'll be in good shape: 1 Pick Selection mode, then highlight whichever edit points or clips you intend to trim. For more than one selection, click once on the first item, then Command-click each additional item you wish to fold into the selection. You're free to grab as many clips and/or edit points spread over as many tracks as you please. 2 If you want to ripple, slip, or slide the full selection together, switch to Trim mode. If instead you want to resize or move every selected item together, remain in Selection mode. 3 Run the trimming operation with the mouse, keyboard shortcuts, or timecode entry, just the same as you would if only a lone edit point or clip were selected. The sections below cover each of the special-case multi-selection trim operations available, together with the particular rules and limits of each.
