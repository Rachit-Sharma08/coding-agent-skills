# General settings overview

Version: DaVinci Resolve 20.3 Reference Manual. Context: System and user preferences.
[Chapter index](INDEX.md) / [Previous section](load-settings-and-save-settings.md) / [Next section](text-and-color.md)
<a id="source-general-settings"></a> <a id="source-system-and-user-preferences-part-3"></a>

### General Settings

These settings fix the timing of resolve-generated effects along with editing operations.

- Standard generator duration: Sets, whether in Seconds or Frames, how long generators run by default once you edit them into the Timeline. Out of the box that value sits at 5 seconds.
- Standard transition duration: Fixes the duration of transitions, in Seconds or Frames, that you add at an edit point in DaVinci Resolve. The default value is 1 second.
- Standard still duration: Sets, whether in Seconds or Frames, how long imported stills last — TIFF, PNG and the other supported graphic file formats among them. Out of the box that value sits at 5 seconds.
- Pre-roll time: Sets how much of the Timeline ahead of the current playhead position plays while you run the Play Around command.
- Post-roll time: Sets how much of the Timeline beyond the current playhead position plays while you run the Play Around command.
- Audio subframe nudge: Sets the count of milliseconds or subframes nudged when you use the Subframe Left/Right controls.
- Default handles length: The value applied while building a timeline with handles. The default is one second worth of frames.
- Default fast nudge length: The count of frames nudged when you use the Shift-Comma (,) and Shift-Period (.) keyboard shortcuts.
- Pre-playhead shadow length: The count of frames in the Timeline ahead of the playhead that the Playhead Shadow covers, where switched on by ticking the “Show playhead shadow box” in the User UI Settings preferences.
- Post-playhead shadow length: The count of frames in the Timeline beyond the playhead that the Playhead Shadow covers, where switched on by ticking the “Show playhead shadow box” in the User UI Settings preferences.
- Automatically switch to single viewer mode when opening trim editor: Switch this checkbox on where you'd like DaVinci Resolve to always bring up the trim editor in one larger viewer while you carry out trim operations. Clearing this box keeps dual viewer operation going even during trimming.
- Timeline overlay retains the last performed action: Switch this checkbox on where you'd like DaVinci Resolve to always recall the last edit type you used in the Timeline Viewer Overlay and flag it on this Overlay each time you drag another clip over the Timeline Viewer, signaling that the last edit you carried out is the new default edit should you drop clips to the left of the overlay.
- Always highlight current clip in the media pool: Switched on, any clips sitting at the playhead position on the Edit or Color pages get flagged on their own in the Media Pool.
- Limit timecode display to 24 hours: With this box ticked, timecode loops back round to 00:00:00:00 after 23:59:59:xx instead of running on. That keeps time of day timecode more consistent to work with.
- Prioritize pasting to the in and out range: As a rule, pasted clips show up at the playhead position in the timeline. Tick this box should you want them pasted according to the timeline in and out points instead.
- Sync the Master Timeline to the current frame: Where you switched on “Automatically match master timeline with media pool” over in the Color settings, this option then lets you make certain that each time you open the Master Timeline, the playhead lands on the same clip and frame it held in the previous Timeline you had going.
- Show offline reference for timeline gaps: Where a missing clip in a conformed timeline leaves a gap in the Timeline Editor, switching this option on tells DaVinci Resolve to show the matching frames of an “offline reference movie,” if one has been tied to that timeline, in place of black. That can rescue you in emergencies where timeline clips go missing right before a screening or review session; the feature lets you play or output the missing frames off the matching media from the offline reference movie rather than outputting black.

To read further on putting Offline Reference Movies to work and assigning them, turn to Chapter 55, “Preparing Timelines for Import and Comparison.”

- Show offline reference for non-conformed edits: Where missing media in a project leaves an unlinked clip in the Timeline Editor (shown by a red exclamation point overlay on that clip), switching this option on tells DaVinci Resolve to show the matching frames of an “offline reference movie,” if one has been tied to that timeline, in place of black. That can rescue you in emergencies where source media goes missing right before a screening or review session; the feature lets you play or output the missing frames off the matching media from the offline reference movie rather than outputting black.

For deeper guidance on applying Offline Reference Movies and assigning them, head to Chapter 55, “Preparing Timelines for Import and Comparison.”

- Use custom safe area overlays: Switching this on surfaces Action Area and Title Area fields where you set your own percentage for each. Their defaults stand at 93% for Action Area and 90% for Title Area.
- Retain sync and avoid overwrites with ripple edits: Tick this box and DaVinci Resolve tries to hold sync during ripple trimming whenever that means overwriting media on certain tracks. Leave it unticked and no media gets overwritten, but ripple trimming will throw clips out of sync.
- Align audio edits to frame boundaries: With this on, the In and Out points of audio clips always snap to whole frame boundaries, exactly as video clips do. With it off, you’re free to make subframe audio edits on audio-only clips, or on linked audio once you’ve suspended linked selection.
- Configure clips as multi-mono on import: Ticking this box lets you bring in any multichannel audio laid out as multiple mono. Any Stereo, 5.1, or other multichannel source then gets set up automatically as multiple mono files carrying the same track count the moment you drop it into the Media Pool.
- Limit Media Pool audio sync to first timecode match: Where a video clip shares timecode overlap with two or more audio clips, the usual behavior syncs every overlapping audio clip by spawning as many fresh tracks as required. Tick this box and that gives way to DaVinci Resolve picking the single audio track it judges most likely and syncing only that one clip, while the rest are left alone.
- Import Finder tags as Keywords (Mac only): With this on, whatever color tags Mac OS has assigned to a media file come in automatically as keyword metadata riding alongside that file.

NOTE: Even with Align audio edits to frame boundaries switched off, having linked selection on stops you from making subframe edits while you resize both the audio and video of linked clips at once.
