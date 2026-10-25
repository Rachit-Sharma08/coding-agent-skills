# Commands for editing and extending the selection and locking audio tracks

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing basics in the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](focus-mode.md) / [Next section](remove-silence-and-audio-clip-with-silence-indicators.md)
<a id="source-commands-for-editing-and-extending-the-selection"></a> <a id="source-locking-an-audio-track"></a> <a id="source-locking-audio-tracks"></a> <a id="source-splitting-clips"></a>

### Commands For Editing and Extending the Selection

With one or more selections made in the Timeline, a set of commands stands ready to tweak or grow that selection. They were conceived to pair with Focus mode, yet they function in any mode. Editing the Selection Six commands handle changing the current selection, carrying it from one clip or batch of clips in the Timeline to another. They shift only the selected span of clips/frames, never the clips themselves. You'll find them in the Timeline contextual menu under Edit Operations after right-clicking a clip.

- Move To Previous/Next Edit: Carries the current selection to the neighboring clip/edit point on the left or right in the Timeline.
- Move To Previous/Next Track: Carries the current selection to the adjacent track above or below in the Timeline.
- Move to Previous/Next Frame: Bumps the current selection left or right in the Timeline.

Extend Edit Selection Four commands grow what's selected in the Timeline, a single clip or track at a step. You'll find them in the Timeline contextual menu under Edit Operations after right-clicking a clip.

- To Previous Edit: Stretches the selection to take in the clip just to its left in the Timeline.
- To Next Edit: Stretches the selection to take in the clip just to its right in the Timeline.
- To Previous Track: Stretches the selection to take in the clip on the track just above in the Timeline.
- To Next Track: Stretches the selection to take in the clip on the track just below in the Timeline.

### Locking Audio Tracks

A further bit of prep ahead of any editorial operation is locking the tracks whose media you'd rather your next move not disturb. Say track A3 carries an intricate set of music edits you don't want touched by an operation that deletes overlapping media — lock track A3 and those clips stay safe.

### Locking an audio track

Clips sitting on locked tracks can't be moved, deleted, cut, or otherwise touched by editorial operations, and their parameters are off-limits in the Inspector as well. They can, however, still play back and mix just like any other audio clips. To flip audio tracks between locked and unlocked on the Fairlight page, do one of the following:

- Click a track's lock control to switch its lock on or off.
- Click a track's lock control and drag across the lock controls of other Timeline tracks to lock or unlock a run of adjacent clips fast.
- Open the Index and click or drag one or more track lock controls to switch lock on or off.

### Splitting Clips

Beyond splitting timeline clips by hand in Pointer or Range mode, Fairlight gives you two more ways to wrangle your timeline audio. Those are Remove Silence and AI Checkerboard to New Tracks, which together with AI Create ADR Cues make up the Intellicut feature set.

For a fuller account of AI Create ADR Cues, turn to “ADR (Automated Dialog Replacement)” over in Chapter 174.
