# Creating mix automation and why use track automation

Version: DaVinci Resolve 20.3 Reference Manual. Context: Mix automation.
[Chapter index](INDEX.md) / [Next section](timeline-audio-keyframe-editing.md)
<a id="source-audio-panning-to-video"></a> <a id="source-automation-view"></a> <a id="source-creating-curves"></a> <a id="source-creating-mix-automation"></a> <a id="source-drawing-automation"></a> <a id="source-drawing-mix-automation"></a> <a id="source-enabling-and-viewing-automation"></a> <a id="source-fairlight-automation-view-menu-choices"></a> <a id="source-fairlight-automation-view-showing-none"></a> <a id="source-mix-automation"></a> <a id="source-mix-automation-part-1"></a> <a id="source-recording-automation"></a> <a id="source-toggle-automation-button"></a> <a id="source-track-automation-line"></a> <a id="source-vector-based-automation"></a> <a id="source-what-can-be-automated"></a> <a id="source-why-use-track-automation"></a>

### Mix Automation

For mixing audio, the Fairlight page offers automation that is uncomplicated, adaptable, and capable. You can build automation data by drawing the changes graphically, or by capturing the movement of onscreen mixer or effects controls as you operate them with a mouse or a Fairlight control surface. There's even the option to generate panning automation from how on-screen people or objects move within the Fairlight Viewer. After it's recorded, automation for any kind of mix parameter—faders, sends, panning, or effects—plays back in flawless sync with both the audio and the video. The focus of this chapter is automation mixing driven by the combined controls of the on-screen mixer and the timeline.

To learn more about the fundamentals of mixing, refer to Chapter 177, "Mixing in the Fairlight Page."

### Creating Mix Automation

A full set of tools for building and editing mix automation ships with the Fairlight page. You're able to draw the automation data, capture mix changes by operating on-screen controls, or call on IntelliTrack-powered Audio Panning to Video, which generates panning automation from how people or objects move within the Fairlight Viewer. And yes, this really is "a thing."

### Why Use Track Automation?

As a video editor, you might be more accustomed to reaching for clip-based automation when altering your audio mix, yet that route carries limitations. There are occasions where you'll want to apply global changes to a track across the timeline, or to tweak groups of tracks together see Chapter 179, "Track Groups." With time-based effects such as reverb or a recurring delay, you might want to dynamically tune the level of the "trails" as a track develops. As an example, you might have a scene shifting perspective from a wider space into a tighter one, where the room ambience or the dialogue's tonal character must evolve over time as the characters travel through the scene. That's exactly where track automation techniques (drawing or recording control movement) become powerful and a source of creative inspiration.

### What Can Be Automated

Almost every control on a Mixer channel strip can have automation recorded for it, the fader, sends, mute, and panning included. Plugin parameters for audio can be automated too.

### Audio Panning to Video

IntelliTrack-powered Audio Panning to Video speeds up the creative process by tracking people or objects in the Fairlight viewer on its own to produce pan automation that mirrors their on-screen motion, with the accuracy that Resolve's cutting-edge object tracking engine provides.

### Drawing Automation

For a video editor or audio creative, drawing mix automation data is often the more direct option in many situations, when you're making static or ramped level shifts or switched changes to controls like a mute button, particularly if you're working with a mouse and don't have the advantages of Fairlight hardware control. As an example, where you'd struggle to finesse a real-time "performance" of fader movements or effect parameter shifts, you could instead select a timeline range and mute several tracks together, "carve out" fixed level boosts or drops on tracks at precisely the moment you want them based on an on-screen event or dialogue, or gradually build up the strength of a reverb on foley footsteps as a character heads into a long, dark cavern. Drawing automation means you needn't concern yourself with the various Fairlight automation recording modes or the control enables/disables for the parameter you want to create or edit; you simply draw or tweak your automation data right in the matching track "lane" on the Timeline.

### Recording Automation

Mix automation can also be built by capturing real-time on-screen fader and control movements, or plugin parameter changes, as playback runs. Your "performance" can then be reproduced faithfully afterward. A further benefit of recording your automation is that you can naturally "perform" the changes against the picture as the action unfolds. This way you can craft a dynamic mix where varying audio levels, pan, EQ, dynamics, and audio processing settings shift over time to bring music up or down against effects or dialogue, pan the sound of a passing car from one speaker across to another, or steadily grow the strength of a reverb as your character heads into that long, dark cavern. Although recording keyframe automation is usually thought of in terms of either the on-screen mixer or the Fairlight console, you can equally record automation using the controls in the Inspector, or via the controls of the Pan, EQ, and Dynamics plugin effects, which lets you record automation for the various audio effects you've placed on a track.

### Drawing Mix Automation

For any parameter, automation can be drawn in the Timeline by globally turning on automation recording and playback, displaying a parameter to be automated, then drawing the automation in the Timeline.

### Enabling and Viewing Automation

Sitting to the right of the transport controls, the Toggle Automation button switches automation recording and playback on and off. It has to be on for you to draw or record track-based automation and to view busses on the Timeline.

### Toggle Automation button

TIP: You can rapidly switch automation safe on or off for a chosen group of channel strips, or for every channel strip, by keeping held, across all selected tracks, the Option key (Mac) or Alt key (Windows), or for every mixer channel strip Command-Option (Mac) or Control-Alt (Windows), prior to carrying out the operation. These shortcuts can shave a great deal of time off your workflow.

### Automation View

Ordinarily, audio tracks show an arrangement of clips on the Timeline ("Clips View"). Within Clips View, clips can be placed or edited, and the clip gain of individual clips can be set, see Chapter 176, "The Fairlight Inspector." Effects can be applied to clips as well, and these can be handled in the Inspector.

Tracks can additionally present an Automation View, which surfaces once the automation button is on. While it's active, a dropdown menu shows up beneath the track controls in the track header. By default that menu reads "None," signaling that you're working with clips alone; no automation data will be shown.

### Fairlight Automation View showing "None"

Clicking that dropdown menu lets you pick an automation parameter to view or edit. There are options for each parameter that a track can control: fader, sends, pan, mute, plus built-in dynamics and EQ, along with AU or VST plugin effects.

### Fairlight Automation View menu choices

For a quicker route, right-click the Mixer channel control you intend to view or edit, or right-click that same target parameter when it lives on a Fairlight FX plugin, a supported Audio Unit, or a VST plugin. After a parameter is picked, the automation view shifts so the emphasis moves to editing track automation data instead of manipulating clips. The clips dim and the automation data line appears in light gray. Once automation is drawn or recorded for that parameter, the line switches to bright green. NOTE: While in Automation View you can still move and trim clips, though cut/copy/paste and delete act on automation keyframe data alone. While in Automation View, timeline-based clip gain keyframe adjustment isn't available, but overall clip gain can still be set with the Volume slider in the Audio tab of the Inspector.

### Vector-based Automation

Audio keyframe automation is vector-based, so levels ramp smoothly between any 2 points on the Timeline according to the direction of the change in control value and the gap in time between the points. As an illustration, say you have one keyframe putting fader level at 0 dB landing at 01:00:20:00 on the timeline; add a further point at 01:00:28:00 set to -10.5 dB, and the level glides smoothly from 0 dB down to -10 dB over the 8 seconds between the 2 points. This lets you draw individual keyframes to quickly assemble different transition shapes, like fade-ins or fade-outs, with only a handful of points, or to bump them up or down by precise amounts quickly and easily.

### Creating Curves

Bear in mind that audio automation keyframes aren't Bezier keyframes, so each one only allows a single level adjustment at that moment in time. Make a large adjustment with just one new keyframe and you can wind up with an abrupt level change, or with level changes lacking the curve you might want (exponential changes can be especially helpful on fade ins or outs to land a natural result). You can produce convex or concave shapes when drawing by laying down just a few keyframes to form your curve, or you can carry out the change exactly to your liking by recording the automation (refer to "Recording Mix Automation" further along in this chapter).

A fade out transition with 5 keyframes for an exponential shape

### Track Automation Line

Audio automation on a track is depicted by a line running across the length of the Timeline, known as the automation line, or "curve." That line's level can be altered by dragging, by entering keyframes one at a time, or by drawing a series of keyframes with the Pencil tool.

Automation line for fader level showing multiple keyframes

Sample Accuracy: With audio keyframes you can place exactly positioned parameter changes onto timeline tracks. Audio keyframes on the Fairlight page are sample accurate, which is to say they can sit at any sample location to sub-millisecond precision, offering finer precision than how keyframes are handled on the Cut and Edit pages. That said, sample-accurate audio automation data made on the Fairlight page plays back accurately on the other pages too. Sample accuracy matters when working to picture, since the location of audio events frequently doesn't land on exact frame or sub-frame boundaries.
