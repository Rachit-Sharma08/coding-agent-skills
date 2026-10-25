# Transport controls and jkl navigation and transport controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Transport controls timeline navigation and markers.
[Chapter index](INDEX.md) / [Next section](how-to-enter-timecode-values-and-absolute-timecode-entry.md)
<a id="source-dragging-the-playhead-to-scrub"></a> <a id="source-fairlight-page-transport-controls"></a> <a id="source-j-k-l-press-j-repeatedly"></a> <a id="source-loop-jog-scrubbing"></a> <a id="source-looping-playback"></a> <a id="source-moving-the-playhead-using-timecode"></a> <a id="source-press-l-repeatedly-shift-j"></a> <a id="source-transport-controls"></a> <a id="source-transport-controls-and-jkl-navigation"></a> <a id="source-transport-controls-timeline-navigation-and-markers"></a> <a id="source-transport-controls-timeline-navigation-and-markers-1"></a> <a id="source-using-jkl-to-control-playback"></a>

### Transport Controls, Timeline Navigation, and Markers

Distinct transport control, zooming, and scrolling choices live on the Fairlight page that the rest of the DaVinci Resolve pages lack, and they let you handle audio more productively. This chapter explains getting around the Fairlight take on the Timeline.

### Transport Controls and JKL Navigation

Owing to the audio-centered workflow of the Fairlight page, its transport and playback controls aren't the same as the ones over on the Media, Edit, Color, and Deliver pages.

### Transport Controls

### Fairlight page transport controls

The Fairlight transport controls are likewise built to echo the matching controls found on the Fairlight control panels. They cover these functions:

- Rewind and Fast Forward: Kicks off sped-up playback along the Timeline either way. Hitting either button repeatedly ramps the motion up, stepping through 8x, 24x, 60x, 150x, and 360x play speeds.
- Play: Plays forward. The same as hitting the Spacebar or L keys with playback stopped.
- Stop: Halts playback. The same as hitting the Spacebar or K keys while playback runs.
- Record: Begins recording provided you've patched an audio source to a track, and provided that track is

enabled for recording. For more information about recording, see Chapter 173, “Recording.”

- Loop: Switches looped playback on and off. With looped playback turned on, playback loops at the

end of the Timeline, loops too when you invoke the Play In to Out command, and keeps looping on its own until you halt playback.

- Automation controls: Pressing this button reveals the automation toolbar.

For more information about recording automation, see Chapter 178, “Mix Automation.”

### Using JKL to Control Playback

Plenty of editing applications share the JKL keyboard shortcuts, and seasoned editors regard them as among the handiest playback and editing controls going. Below is a rundown of the numerous ways you can put these three keyboard shortcuts to use, playing through clips and timelines while you work.

### J K L Press J repeatedly

### Press L repeatedly Shift-J

Runs backward at 100%. Halts playback. Runs forward at 100%. Steps up the reverse play speed with every press of J, across a spread of fast-reverse speeds. Steps up the forward play speed with every press of L, across a spread of fast-forward speeds. Runs in fast reverse.

Shift-L K+J K+L Holding K as you tap J Holding K as you tap L

Runs in fast forward. Runs backward in slow motion (audio plays back slowed too). Runs forward in slow motion (audio plays back pitch-corrected on OS X). Nudges the playhead back by a single frame. Nudges the playhead forward by a single frame.

When you're driving Fairlight from the keyboard, this is likely to turn into one of your principal means of shifting the playhead about within DaVinci Resolve.

NOTE: Every keyboard command this document lists assumes the DaVinci Resolve keyboard customization preset. Remapping keyboard commands to layouts you might know better, such as Premiere Pro or Pro Tools, carries real benefits. That said, if their command set lacks the same commands the DaVinci Resolve keyboard commands provide, they won't behave identically. As an example, the Pro Tools keyboard preset offers no J-K-L timeline navigation.

### Dragging the Playhead to Scrub

The playhead can also be dragged side to side to scrub across the visible stretch of the Timeline by clicking and dragging anywhere inside the Timeline ruler up top of the Timeline, just under the toolbar. When you're zoomed in at a sensible editing level, scrubbing the playhead with your pointer yields smooth, tape-style slow and fast audio playback, handing you plenty of precision as you trim audio.

### Looping Playback

A pair of controls run looping over on the Fairlight page, much like the way looping behaves on the Edit page.

- Loop: Command-Forward Slash (/). Switches looped playback on and off. With looped playback on, playback you kick off using any of the commands below will loop on its own until you halt playback.
- Play In to Out: Option-Forward Slash (/). Once you've bracketed a portion of a clip or timeline using In and Out points, this command gives you a preview of how that stretch plays.

### Loop Jog Scrubbing

For now offered only on the Fairlight page, picking Timeline > Loop Jog lets a short sample preview play back as you scrub the playhead along the Timeline. That can help you pick out snippets of dialog or music while rapidly scrubbing through tracks, in cases where you're hunting for particular lines or music cues. It likewise lets that short sample preview loop without end while you hold the playhead on a frame, so you can pause mid-scrub and hear (by default) the latest 80 ms ahead of the playhead as it loops. A couple of settings within the User Preferences let you tailor this behavior.

- Loop Jog Alignment: Three choices let you decide whether the audio loops Pre the playhead's position, Centered on the playhead, or Post the playhead's position.
- Loop Jog Width: A field lets you set how many milliseconds of audio loop once Loop Jog is on. How many milliseconds of audio a single frame works out to depends on the video's frame rate. To illustrate, with a 25 fps frame rate, the math is 1000/25 = 40 ms per frame, meaning the default value of 80 ms covers two frames' worth of looping.

### Moving the Playhead Using Timecode

Absolute or relative timecode entry can be used to shift the playhead within the Timeline. Entering timecode lets you nudge the playhead with great accuracy or leap to particular timecode values in a hurry.
