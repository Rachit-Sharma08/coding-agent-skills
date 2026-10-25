# Linking multiple clips in the timeline and commands for slipping audio video sync

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing basics.
[Chapter index](INDEX.md) / [Previous section](audio-video-linking-and-controlling-linked-selection.md)
<a id="source-commands-for-slipping-audiovideo-sync"></a> <a id="source-linking-multiple-clips-in-the-timeline"></a>

### Linking Multiple Clips in the Timeline

Linking isn't limited to audio and video clips that already sync together, though. You're free to link as many video and audio clips as you like so they can be selected, moved, and edited as a single unit, even ones that were never intended to be in sync. That turns linking into an organizing device every bit as much as a sync-management one.

Here are some examples of how you can use this:

- You can tie a text generator carrying a subtitle to the clip it runs alongside.
- You can tie a stack of overlapping audio sound effects to the video clip they go with.
- You can tie off-camera audio to the on-camera shot it belongs to.
- You can tie the background and foreground clips of a green screen composite together, with the sound from each.

Linking several clips in the Timeline behaves just like linking one audio and video clip pair; each linked item shows a chain icon at the left of the clip name, and pausing linked selection to knock any single clip out of sync triggers an "out-of-sync" indicator. Several audio and video items hand-linked into one unit that acts like a single clip on the Timeline while Linked Selection stays on

### Commands for Slipping Audio/Video Sync

A further group of commands under the Trim > Slip Audio submenu lets you slip what's inside one or more chosen clips to adjust the sync between their audio and video, working either in full-frame steps or in sub-frame steps for clips whose borderline sync you'd like to tighten up.

- One Frame Forward (Option-Period)
- One Frame Reverse (Option-Comma)
- One Subframe Forward (Option-Right Arrow)
- One Subframe Reverse (Option-Left Arrow)
