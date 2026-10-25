# Track selection locking and destinations

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing basics.
[Chapter index](INDEX.md) / [Previous section](marker-flag-color-and-edit-selection.md) / [Next section](deleting-clips-from-the-timeline-and-gaps-in-the-timeline.md)
<a id="source-disabling-and-re-enabling-clips-in-the-timeline"></a> <a id="source-locking-tracks-you-dont-want-to-change"></a> <a id="source-overriding-automatic-selections-by-making-manual-selections"></a> <a id="source-position-lock-for-finishing"></a> <a id="source-position-locking-all-tracks"></a> <a id="source-position-locking-individual-tracks"></a> <a id="source-the-position-lock-button-on-the-toolbar"></a> <a id="source-using-destination-track-selector-controls-to-control-other-operations"></a>

### Overriding Automatic Selections by Making Manual Selections

Keep in mind that whenever you manually highlight particular clips in the Timeline, those manual selections always win out over whatever a track's Destination Track Selector control happens to be set to. Take an example with three superimposed clips where the Destination Track Selector control of every track besides V2 has been switched off. Placing Timeline In and Out points then automatically marks that stretch of the clip on track V2 for deletion, should you press the Delete key. The portion of the Timeline involved stands out because it's highlighted while everything else dims.

Soloing track V2's Destination Track Selector control so a Delete operation stays confined to it However, were you to click the clip on track V1 to grab it by hand, the automatic selection that the In and Out points had set up vanishes, giving way to the highlighted clip you just clicked. That's because manual selections nearly always outrank the automatic ones you set up through the In and Out points and Destination Track Selector controls.

A manual selection takes priority over the Auto Select controls Bear this in mind whenever the quickest route to the operation at hand is simply picking the clip by hand to mark out that operation.

### Using Destination Track Selector Controls to Control Other Operations

The Destination Track Selector controls also steer every command whose result hinges on "the clip on the lowest-numbered track with Destination Track Selector enabled." Among such commands are these: Copy and Paste; Mark Clip; Go To Next Edit/Previous Edit; Selection Follows Playhead mode; Next Gap/Previous Gap; plus more (you'll find a full roster of the affected operations further on). One frequent case where this counts is any time you reach for the Mark Clip command to have In and Out points set automatically to span a Timeline clip's length. Should that clip fall at a spot on the Timeline holding several superimposed clips of differing lengths, then by default the In and Out points (first and last frames) belonging to the clip on the lowest numbered track drive the Timeline In and Out points whenever Mark Clip runs.

With Mark Clip run while every Destination Track Selector control stays enabled, the outcome is set by whichever clip sits on the lowestnumbered video track that still has Destination Track Selector enabled However, switch off the Destination Track Selector control for track V1, and whichever clip now sits on the lowest video track whose Destination Track Selector remains enabled becomes the target for the Mark Clip operation. Here, the briefer clip on track V2 takes over setting where the In and Out points land.

A Mark Clip run while the Destination Track Selector controls remain enabled Here are the ways to switch the Destination Track Selector controls on and off:

- To toggle Destination Track Selector for any track: A click on that track's Destination Track Selector control does it.
- To toggle Destination Track Selector for video tracks: Hit Option-F1 through F8, each flipping Destination Track Selector on its matching track.
- To toggle Destination Track Selector for audio tracks: Hit Option-Command-F1 through F8, each flipping Destination Track Selector on its matching track.
- To flip every video track's Destination Track Selector off and on together: Press Option-F9.
- To flip every audio track's Destination Track Selector off and on together: Press OptionCommand-F9.
- To "solo" one track's Destination Track Selector while switching Destination Track Selector off everywhere else: An Option-click on any Destination Track Selector control keeps that one active and shuts off every other Destination Track Selector control of the matching kind (video or audio).
- To switch on or off every audio or video Destination Track Selector control at once: A Shift-click on any video or audio Destination Track Selector control flips every Destination Track Selector control of the matching kind (video or audio) on or off at once.

Each track's Destination Track Selector control state bears on the following operations:

- Cutting, copying, or deleting clips: With Timeline In and Out points marking a span of media to clear from the Timeline, only the media on tracks whose Destination Track Selector control is enabled gets cut, copied, or deleted.
- Deleting gaps: As you pick and clear gaps in the Timeline, clips on other tracks that cross the chosen gap are deleted as well on tracks whose Destination Track Selector control is enabled. Media sitting to the right on the affected tracks ripples leftward to seal the gap.
- Selecting edit points using the keyboard: Pressing V to grab the nearest edit point lands on the edit point belonging to the lowest track with Destination Track Selector enabled. When you walk the selection from one edit point to the next with the Up Arrow and Down Arrow keys, edit points on tracks whose Destination Track Selector control is off get skipped.
- Selecting clips using the keyboard: With a clip selected, the Up Arrow and Down Arrow keys walk the selection from clip to edit clip, yet clips on tracks whose Destination Track Selector control is disabled stay invisible to this operation.
- Using Mark Clip: While the Mark Clip command runs, clips on tracks whose Destination Track Selector controls are disabled get passed over. This lets you single out a target clip for marking the clip whenever several overlapping superimposed clips are present.
- Match Frame: During a Match Frame operation, clips on tracks whose Destination Track Selector controls are disabled get passed over. This lets you single out a target clip for matching a frame whenever several overlapping superimposed clips are present.
- Pasting clips: Every copied clip lands on the lowest numbered track whose Destination Control is enabled. Should all tracks of a given type have their Destination Track Selector controls switched off, then none of that type's clips get pasted whatsoever.
- Finding gaps: When you invoke Playback > Previous Gap (Command-Option-Semicolon), or alternatively Next Gap (Command-Option-Apostrophe), any gaps residing on tracks whose Destination Track Selector is off get skipped.
- Using Selection Follows Playhead: Switching on "Selection Follows Playhead" makes whichever clip the playhead crosses get picked automatically. When more than one clip crosses the playhead, the one on the highest track gets chosen. Clips on tracks whose Destination Track Selector is disabled won't be picked.

### Locking Tracks You Don't Want to Change

One more move you can make before launching into any editorial operation is to lock down tracks holding media you'd rather keep clear of whatever's coming. As an instance, if track A3 carries an intricate batch of music edits you want shielded from operations that would ripple the Timeline, locking track A3 keeps those clips untouched.

Here tracks V2, V1, and A1 stay unlocked, whereas tracks A2, A3, and A4 are locked Clips sitting on locked tracks can't be moved, deleted, cut, or otherwise touched by editorial operations. On top of that, you can't edit a locked clip's parameters in the Inspector. Even so, clips on locked tracks remain open to grading and other changes over in the Color page. To flip tracks between their locked and unlocked states, take one of these routes:

- A click on any track's lock control flips that track's lock on or off.
- A Shift-click on any track's lock control flips locking on or off across all tracks at once.
- Option-Shift-1 through 8 locks or unlocks the tracks V1 through V8.
- Option-Shift-9 locks or unlocks every video track.
- Option-Shift-F1 through F8 locks or unlocks the tracks A1 through A8.
- Option-Shift-F9 locks or unlocks every audio track.

### Position Lock for Finishing

Put briefly, switching position lock on stops clips from sliding left or right and blocks every ripple operation. Its main value comes near the close of post on a project whose cut is locked (or as close to "locked" as directors and producers will still permit) while you still need surgical tweaks that won't risk knocking the video out of sync with audio that could be getting edited and mixed elsewhere, all from one stray rippled edit. With position lock engaged, you remain free to perform edits (Replace among them), slip clips, roll edits, drop in Resolve FX and other Open FX, and adjust every sort of effect in the Inspector. The one thing you can't do is anything that moves clips around the Timeline or ripples whole stretches of it. Position Lock can be switched on in two ways.

### Position Locking All Tracks

A single button in the toolbar over the Timeline lets you switch Position Lock on and off for all tracks at once.

### The Position Lock button on the toolbar

Once you switch position lock on, every track's Lock button turns red to signal that position lock is now active instead. Position lock indicated by each track's Lock icon changing

### Position Locking Individual Tracks

For an extra-clever touch, you can engage position lock track by track by Command-clicking any track's Lock button. To release position lock, just click that same track's Lock icon.

### Disabling and Re-Enabling Clips in the Timeline

Now and then a video or audio clip or two sits in the Timeline that you'd rather not have play with the rest of the cut sequence, yet you also aren't ready to pull it out of the Timeline in case you reconsider down the line. That's why you can Disable clips, switching them off without taking them out. Disabled clips show up dimmed in the Timeline. They won't play back, they aren't rendered, and they don't get output to video. Their spot in the Timeline stays intact, though, so you can re-enable them whenever you reconsider and decide you'd like to use them after all.

A disabled clip shown dimmed and flanked by two enabled clips To disable or re-enable one or more clips you've selected:

- On part of the selection, right-click and pick Enable Clip out of the contextual menu.
- Choose Clip > Enable/Disable Clip.
- Press D.

NOTE: Dedicated Enable and Disable clip actions can now be mapped to keyboard shortcuts within the Keyboard Customization Dialog. The toggle shortcut for enable / disable clip stays "D", yet mapping these dedicated actions sidesteps the problem of a selection holding both disabled and enabled clips merely flipping their on / off states instead of all turning enabled or all turning disabled. 1. Open DaVinci Resolve > Keyboard Customization. 2. Beneath Commands, pick Clip. 3. Enter "able" within the search box. 4. Map a keyboard shortcut onto both Disable Clip and Enable Clip.
