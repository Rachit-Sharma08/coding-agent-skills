# Visualizing loudness monitoring and metering options

Version: DaVinci Resolve 20.3 Reference Manual. Context: Audio meters and audio monitoring.
[Chapter index](INDEX.md) / [Previous section](loudness-meters-and-what-is-lufs.md)
<a id="source-cinema-viewer-on-fairlight-page"></a> <a id="source-level-metering-options"></a> <a id="source-metering-options"></a> <a id="source-pre-fader-metering"></a> <a id="source-solo-and-pre-fader-metering"></a> <a id="source-target-loudness-level"></a> <a id="source-viewer"></a> <a id="source-visualizing-loudness-monitoring"></a>

### Visualizing Loudness Monitoring

Bring a Main bus’s track into view on the Timeline and, so long as the track stands high enough (ahem, tall enough), you can reveal or hide a set of “Loudness History” curves that picture the loudness analysis of that bus’s mix across the whole length of the mix. On offer are these curves:

- Integrated: A thick curve traces the averaged “integrated” loudness analysis of the present mix, a reading drawn from the start of playback through to its end. This graph stands as the chief gauge of whether the measured loudness passes muster. Each segment’s color signals whether that part of the mix sits “to spec.” Blue points to loudness levels under tolerance, yellow to those inside tolerance, and red to those above tolerance. Read the curve’s colors and you can readily pick out which parts of your mix might want adjusting to hit the required specification.
- Momentary: A reading of the loudness over the past 400ms, drawn as a thin green-blue curve, which reports on transient shifts in level.
- Short Term: A reading of the loudness over the past 3 seconds, drawn as a thin blue line, which gives a more averaged take than the Momentary curve while still conveying the mix’s dynamics.

To bring Main 1’s loudness history into view: 1 Open the Automation controls with a click of the automation button over on the Fairlight toolbar. 2 Bring up the Index, then click the eye button for whichever Main you want to view on the Timeline. Loudness History turns up among the track header controls as long as the track stands tall enough to show those controls. On short tracks they stay hidden. 3 Switch on the Loudness History toggle, then tick the curves you’d like to see. The Integrated, Momentary, and Short Term loudness analyses can each be shown or hidden on their own, opening up overlapping graphs within that track where your program’s loudness is visible across time.

Viewing the loudness graph of the mix leaving a Main NOTE: For now, loudness history is supported on Main 1 alone.

### Metering Options

DaVinci Resolve offers an assortment of metering options for shaping metering around your workflow. Their settings live under Project Preferences > Fairlight on the Audio Metering pane, yet they reach the mixer, Fairlight effects, and master metering on the Cut and Edit pages.

### Level Metering Options

You get to pick the response characteristic for the level meters covering channel strips and Fairlight FX. The Meter Type dropdown lets you settle on IEC 60268-18, Digital VU, or Custom response characteristics. Each meter type keeps its own “hold and fall” metering, so the highest peak reached stays visible.

IEC 60268-18: A digital PPM-style meter set to a -18 dBFS reference standard, quick to answer peaks yet slower on release. It’s the default within DaVinci Resolve and runs throughout every Blackmagic Design software and hardware product. Digital VU: A two-value meter showing the peak level via a single fast-ballistics segment, with the RMS (volume unit) drawn as a bar graph. Its decay is far quicker and roughly linear, which makes average levels easy to watch while still letting sounds with sharp transients and decays be followed more readily. This one tends to suit audio editing and mixing best. Custom: Lets you choose every facet of the meter response, level detector, scale, peak, deck, and peak indication included.

### Pre-fader Metering

Out of the box, “Pre fader metering on tracks” sits unchecked (disabled), which places the metering on channel strips post (after) the fader level and mute button. Say the source audio file peaks at -2 dBFS and you pull the channel fader down from 0 to -10, after which the peaks shown on the meter land at -12. Turn pre-fader metering on and the metering point moves ahead of the fader, untouched by where the fader sits. The meter does still respond to clip gain settings or keyframing, though, since those level shifts happen before the clip’s signal reaches the mixer’s signal path. Under pre-fader metering you could drop the fader all the way off (minus infinity) and the meter would keep reading the source signal’s level. That keeps you forever aware of the source signal and what it’s up to before the mixer’s controls or processing touch it. Plenty of video editors lean toward post-fader metering, whereas most audio mixers favor pre fader so the true source level is known at every moment.

### Solo and Pre-fader Metering

With pre-fader metering switched on, soloing one or more tracks paints a fainter “ghost” of meter activity onto the tracks that aren’t soloed, so audio levels stay visible even on tracks the soloing has muted. That makes it simple to concentrate on the tracks you can actually hear while still catching what’s happening on the ones you can’t. Where pre-fader metering is off (the default), soloing one or more tracks leaves the unsoloed tracks with no metering at all.

Pre-fader metering, the non-soloed tracks showing lightly shaded meters

### Target Loudness Level

Lets you set the master Loudness meters’ target loudness level, in LUFS, to whatever output target you’re aiming for. DaVinci Resolve’s default loudness standard target, for one, is -23 LUFS, while YouTube’s target LUFS specification calls for -14 LUFS. Set -14 LUFS and the “0” mark on the loudness meter scale shifts to that level, helping you steer your master mix levels toward that loudness standard.

### Viewer

A compact viewer set to the right of the Monitoring panel displays the video frame sitting under the playhead. It’s the very image fed to your workstation’s external broadcast display, should one be hooked up.

The Viewer shows you the picture you’re mixing against. Click the Expand Viewer button down in the bottom right corner and the Viewer opens into a floating window you can then drop wherever you please. To shut the floating Viewer, click the Dock Viewer button in the upper right corner of the floating viewer window.

Click the button in the upper right corner to dock the Viewer once more.

### Cinema Viewer on Fairlight Page

There are times, when you have to confirm lip sync or sound effects sync, or just look over a fresh stretch of a mix you’ve been shaping, that watching the program’s visuals full screen while your mix plays really helps. The Fairlight page Viewer can now be put into Cinema Mode by choosing Workspace > Viewer Mode > Cinema Mode (Command-F).
