# 6 mono channel media pool clip and audio channel source menu

Version: DaVinci Resolve 20.3 Reference Manual. Context: The Fairlight inspector.
[Chapter index](INDEX.md) / [Previous section](audio-tab-track-mode-and-effects-tab.md) / [Next section](paste-and-remove-attributes.md)
<a id="source-6-mono-channel-media-pool-clip"></a> <a id="source-adjusting-multiple-clips-in-the-file-tab"></a> <a id="source-adjusting-multiple-clips-simultaneously"></a> <a id="source-animated-inspector-adjustments"></a> <a id="source-audio-channel-source-menu"></a> <a id="source-audio-channel-source-menu---simplified-timeline-menu"></a> <a id="source-audio-channel-source-menu---timeline-menu"></a> <a id="source-file-tab--timecode-section"></a> <a id="source-timecode"></a>

### 6 mono channel Media Pool clip

- Mute: Click this button to silence the channel while it stays put inside the clip. So with the six-channel Media Pool clip, if you ticked the checkbox for channel two and then hit the Mute button, all six channels still travel when the clip is dragged onto the Timeline, yet only channels 1, 3, 4, 5, and 6 can be heard.

TIP: Option-clicking a Mute button or an Active/Inactive checkbox flips all the others to the opposite state, which effectively solos the channel you are touching.

- Channel Source: For multichannel clips made entirely of mono channels, the Audio Configuration pane adds a dropdown showing each waveform’s current audio source by name. Click that dropdown to pick from a roster of mono audio sources. It helps when, for example, you must reroute a person’s lavalier mic signal to a different one, or the boom mic channel got bumped during a take and now carries loud noise that needs swapping to another source.

### Audio Channel Source menu

Changing the Channel Source on the Timeline To swap an audio source on the Timeline, right-click the audio channel that needs fixing and pick an option from the foot of the contextual menu.

### Audio Channel Source menu - Timeline menu

For faster access to these options, Command right-click the audio channel in question.

### Audio Channel Source menu - Simplified Timeline menu

- Transport Controls: After you have begun playback with the Play button, clicking anywhere inside a waveform “solos” that channel and keeps the audio playing on from that spot. With a Media Pool clip, clicking anywhere inside the composite waveform plays the blend of enabled, unmuted channels starting there. With a timeline clip, return to hearing every channel by clicking the Stop button and then the Play button.
- Level: This control wakes up once you have selected one or more channels and serves to trim the level of individual channels in multichannel Media Pool or timeline clips. It comes in handy when a channel or two sits too quiet and must be trimmed up to match the rest. Trim moves you make inside timeline clips stand apart from their clip gain and leave the matching Media Pool clip untouched.

TIP: Command-clicking or Shift-clicking to grab several channels lets you trim every channel in that group at once. Bear in mind, though, that all of them get trimmed by the very same amount (in dB).

### Adjusting Multiple Clips in the File Tab

You may pick several audio clips and adjust their properties together in the Audio Configuration pane. As one example, you can grab a batch of audio files and strip Track 2 from every one of them in a single move. A few things bear noting, though:

- Within a multi-clip selection, only the clip you picked last shows up in the track layout of the Audio Configuration Pane. The top composite waveform, however, takes the name “Multiple Clips” to signal that you have more than one clip selected.
- Whatever you adjust, such as muting or enabling/disabling a track, hits every selected clip together.

### Timecode

This pane holds controls that Clip Attributes in the Media Pool once took care of (that route still works too). With them you can override the timecode details for one or several clips in the Media Pool.

### File tab – Timecode section

- Current Frame: Here is where you give a fresh time to the timecode at the clip’s currently viewed frame.
- Slate: When source media arrives from a shoot that used a timecode slate on set, you can set the slate timecode as a second timecode track for assorted operations, all without disturbing the clip’s primary timecode, which might already be serving program sync.
- To enter the right Slate timecode, choose a Media Pool clip showing a visible timecode slate and park the playhead on a frame where the slate’s timecode reads clearly. Next, open the Timecode panel of the Clip Attributes window and key the timecode value you read in the picture into the Slate Timecode field.
- Offset Source: When a whole batch of clips merely has its timecode shifted, you can fix the timecode offset across as many selected clips as you wish.

### Adjusting Multiple Clips Simultaneously

A simple route exists for tweaking the Inspector parameters of many clips at once, with no need for Paste Attributes (covered later here). Just select every clip you mean to change at the same time, then adjust the parameter you want in the Inspector. The upshot is that each selected clip shifts by the same amount. It works for compositing effects, transforms, text parameters, filters, and audio settings, pretty much anything that can be shown in the Inspector for several selected clips together. Select multiple clips and the Inspector reads “Multiple Clips” as its title. Where the selected clips hold differing values in the parameter you are adjusting, that parameter shows two dashes in its value field. Two routes let you adjust multiple clips:

- To make a relative change across all selected clips while their original offsets from one another stay intact, drag the virtual slider in the parameter field, which shows a + or – ahead of however many units your change spans.

If instead you want every selected clip set to one identical value, double-click the number field, type the value, and press Return.

Applying a relative plus 4.00 shift to the Volume level across every selected clip

### Animated Inspector Adjustments

Key-framing on the Edit page behaves a touch differently from using the Keyframe Editor on the Color page. You can handle most basic key-framing right in the Inspector through three buttons that sit to the right of any parameter able to be keyframed. An animated effect needs at least two keyframes.

Shown in the Inspector are three keyframe controls, reading left to right: Previous keyframe, Create/ Delete keyframe, Next keyframe Ways to key-frame parameters from the Inspector:

- To add a keyframe: Pick a clip, open the Inspector, slide the Timeline playhead to the frame where the keyframe should go, then click the Keyframe button beside the Inspector parameter you wish to animate. After a parameter holds at least one keyframe, every further change you make to Inspector parameters, or with the onscreen Transform/Crop controls in the Timeline Viewer, drops new keyframes on its own whenever the playhead sits on a different frame.
- To move the playhead to the next or previous keyframe: Click the little left or right arrow on either flank of a parameter’s keyframe control to send the playhead to the neighboring keyframe. The Right-Bracket ( [ ) and Left-Bracket ( ] ) keys also step you keyframe to keyframe.
- To edit an existing keyframe of a parameter: Park the playhead right on the keyframe you mean to edit, then change that parameter, whether in the Inspector or through the Timeline Viewer’s onscreen controls.

Methods of changing keyframe interpolation in the Inspector:

- To change a keyframe to Ease In or Ease Out: Eased keyframes make animated changes that start gently and build to full speed, or wind down gradually to a halt. This applies only once two or more keyframes are forming an animated effect. With the next/previous keyframe controls, bring the playhead onto a frame that holds a keyframe; right-click its orange keyframe button, then pick Ease In, Ease Out, or Ease In and Out, depending on the keyframe you are editing and the effect you are after.
- To change a keyframe to Linear: With the next/ previous keyframe controls, bring the playhead onto a frame that holds a keyframe; right-click its orange keyframe button, then pick Linear.

Methods of deleting keyframes and disabling keyframed effects:

- To delete a single keyframe: Open the Inspector, send the Timeline playhead to a frame holding a keyframe, and click the orange Keyframe button in the Inspector to remove it.
- To delete all keyframes for one parameter: In the Inspector, click the reset button on the right of that parameter’s keyframe control.
- To delete every keyframe across a whole parameter group from within the Inspector: Click the reset button sitting on the right of that parameter group’s title bar.
- To disable or enable a single parameter’s keyframed effect: On the Timeline, click the toggle control at the left edge of a parameter’s keyframe track. Orange signals that track is on; gray means off.
- To disable or enable a group of parameters in the Inspector: Within the Inspector, click the toggle control sitting at the left edge of that parameter group’s title bar. Orange signals that group is on; gray means off.
