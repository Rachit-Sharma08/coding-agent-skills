# Preview and audition controls and sound effect list

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](list-panel-of-the-adr-interface-and-record-panel.md) / [Next section](mpeg-h-options-in-the-tracks-panel-overview.md)
<a id="source-audio-monitor-checkbox"></a> <a id="source-edit-index"></a> <a id="source-index"></a> <a id="source-preview-and-audition-controls"></a> <a id="source-sound-effect-list"></a> <a id="source-tracks"></a>

### Preview and Audition Controls

Choose an item in the Sound Effect list and it loads into the preview player, where the controls beneath the search field let you play it or audition it in your timeline.

- Clip name: The name of the clip you've got selected right now.
- Next/Previous buttons: A pair of buttons that step you to the next or previous sound effect clip in the

Sound Effect list.

- Duration display: Reports how long the current clip runs, or how long the stretch marked off with

In and Out points runs.

- Playhead timecode display: Where the playhead sits right now.
- Waveform overview display: Here the whole sound effect's waveform appears, giving you a

pulled-back look at the selected clip. Every channel is summed together in this view.

- Zoomed in waveform display: A magnified slice of the selected clip that reveals finer waveform detail for placing In, Out, and Sync points.
- Jog bar: Lets you move through or scrub across the clip.
- Transport controls: Play, stop and loop buttons hand you command of playback, though you can equally

reach for the space bar and JKL controls. Right-click the Stop button to flip it into “Stop and Go to Last Position” mode.

- Marking controls: The Sync Point button lets you flag a particular frame on the sound effect that you want lined up with the Timeline's current playhead spot when you reach for the Audition controls. The In and Out buttons let you flag which stretches of the sound effect clip you mean to cut into the Timeline.
- Audition controls: The Audition button drops you into Audition mode, where the sound effect clip you've got selected is set down automatically at the playhead's spot on whichever Timeline track is active. You can then head over to the timeline and hear the clip within your mix. Cancel and Confirm buttons let you decide whether to pull the clip out of the Timeline and try another one, or keep the sound effect clip where it is.

To audition clips you've picked in the Sound Library against the Timeline: 1 Pick a sound effect clip you've found in the list that you'd like to audition in the Timeline. 2 (Optional) Within the Sound Library, slide the scrubber bar so the playhead reaches whichever part of the sound effect you'd sync to, then click the Sync Point button to drop a sync mark on that clip. Say you're syncing the sound of a car door closing — you might line up the first frame of the door fully shut with the peak of the “slam,” rather than any earlier door squeak in the sound effect. 3 (Optional) Set In and Out points to mark off the stretch of the sound effect you might use. 4 Pick a track to preview the sound effect on by clicking its track header or Mixer channel strip. 5 Park the playhead at the spot in the Timeline where the clip should go. 6 Click the Audition button in the Sound Library. The clip now shows up, for the moment, in the Timeline, and you can play that part of the Timeline to judge how the sound effect sits alongside the rest of the mix. 7 If the sound effect works, click Confirm to keep it in the Timeline. If it doesn't, click Cancel and it leaves the Timeline.

NOTE: Before the Audition function will run, a track must be selected first. On top of that, picking another sound effect after an audition without first confirming the prior one cancels the Audition process, and the prior sound is pulled from the timeline.

### Sound Effect List

Every sound effect clip matching the current search criteria turns up in this scrollable list. Double-click anywhere on a list item to play that sound effect from start to finish.

- Clip Name: The name that sound effect file carries in the storage system.
- Description: Whatever metadata sits embedded inside the files of professionally produced sound effect

libraries shows up here.

- Duration: How long that sound effect file runs.
- Audio Channel: How many channels that sound effect file holds.
- Star Rating: A clickable control for rating sound effects inside DaVinci Resolve.

Star rating data isn't stored anywhere outside of DaVinci Resolve.

- Waveform: The full sound effect library's overall waveform is stretched or squeezed

to fit the width the Sound Library has on hand, no matter the true length of each clip.

### Index

The Index hands you a convenient interface for listing every clip in the current edit, every track in the current Timeline, and every marker in the current Timeline. Through these lists you can select several items at once, manage tracks, and check marker notes with ease. Each of the three information categories sits in its own panel: the Edit Index, Tracks, and Markers.

### Edit Index

Shows the Edit Index just as it looks on the Edit page. Each audio clip in the open Timeline gets its own Edit Index row, whose columns cover video track, Source In and Out, Record In and Out, Name, plus further descriptive metadata. Any selected clip (those grabbed automatically for crossing the playhead among them) shows as selected over in the Edit Index. Through the Option menu you can screen the Edit Index along various lines — say, showing only clips bearing a certain flag, marker, or color, only clips carrying speed effects, only clips with audio filters, or compound audio clips.

In the Tracks panel, every track in the Timeline gets its own row of information

### Tracks

Every track in the open Timeline lines up with a row of controls and information in this panel. Reading left to right, a track offers a color control, then a visibility control, plus a number, a name, its track controls, a format, ADC, Tags, and — where a VCA is at work — that VCA group's number. These controls let you hide or reveal tracks, color-code them, rename them, switch track controls on singly or by dragging over several, alter their format, place them onto (or take them off) the audio monitor list, and shuffle their order by dragging one or several rows up or down the list, plus flip the automatic delay compensation (ADC) on or off (on by default).

Within the Tracks panel, each Timeline track is represented by one row of information.

NOTE: The ADC column (automatic delay compensation) carries a check box that lets you switch ADC on track by track.

### Audio Monitor Checkbox

A monitor checkbox shows up next to each bus or track in the Tracks list. Check it and that track or bus joins the Audio Monitoring dropdown menu as a monitoring choice. Every bus is checked on by default and appears in the list unless you uncheck it here.
