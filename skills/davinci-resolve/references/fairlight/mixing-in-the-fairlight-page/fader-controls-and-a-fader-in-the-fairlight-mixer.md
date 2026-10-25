# Fader controls and a fader in the Fairlight mixer

Version: DaVinci Resolve 20.3 Reference Manual. Context: Mixing in the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](bus-assignment-buttons-and-legacy-mixer-bus-assignment.md)
<a id="source-a-fader-in-the-fairlight-mixer"></a> <a id="source-fader-controls"></a> <a id="source-level-metering-options"></a> <a id="source-metering-options"></a> <a id="source-pre-fader-metering"></a> <a id="source-solo-and-pre-fader-metering"></a>

### Fader Controls

The vertical fader on each track lets you govern the level that track outputs, whether with your mouse or with a physical fader on your Fairlight console or third party control surface. When you’re on a console, the onscreen faders act as a visual reference for the levels in place.

- dB Indicator: The numeral at the top of the track reports the volume, in decibels, that track currently holds.
- Fader: Drag a track’s vertical fader using your mouse or another pointing device to set that track’s volume and to perform automation recording. An upward drag raises volume; a downward drag lowers it. Fader handles go red while you record level automation, and they go green once automation has been recorded for that track.

Ways to adjust channel faders: To change level: Grab any fader and drag it upward or downward. To reset the level to default level of 0 dB: Give a fader’s handle a double-click. That stops working once a track has recorded automation, unless you clear the automation beforehand.

### A Fader in the Fairlight Mixer

### Metering Options

DaVinci Resolve offers an assortment of metering options letting you fit metering to your workflow. The settings live in Project Preferences > Fairlight in the Audio Metering section, yet they govern mixer, Fairlight effects, or master metering on the Cut and Edit pages.

### Level Metering Options

It’s up to you to set how the level meters respond for channel strips and Fairlight FX. Via the Meter Type dropdown you select among IEC 60268-18, Digital VU, and Custom response characteristics. Each meter type carries its own “hold and fall” metering, so you can spot the highest peak it reaches.

IEC 60268-18: A digital PPM-type meter with a reference standard of -18 dBFS, a quick response to peaks, and a more gradual release characteristic. It’s the default within DaVinci Resolve and is what every Blackmagic Design software and hardware product relies on. Digital VU: A dual-value meter rendering the peak level as one fast-ballistics segment and the RMS (volume unit) in the form of a bar graph. Its quasi linear decay characteristic is far quicker, making average levels easy to watch while still letting sounds with sharp transients and decays be followed more readily. This option can suit audio editing and mixing best. Custom: Lets you choose every facet of the meter response, including level detector, scale, peak, deck, and peak indication.

### Pre-fader Metering

Out of the box, “Pre fader metering on tracks” is unchecked (disabled), which sets the metering on channel strips to sit post (after) the fader level and mute button. As an example, if the source audio file has peaks striking -2 dBFS and the channel fader is pulled down from 0 to -10, then the peaks shown on the meter now land at -12. With pre-fader metering on, the metering point moves to ahead of the fader and the fader’s position no longer touches it. The meter is, however, affected by clip gain settings or key framing, since those level changes happen before the clip’s signal reaches the mixer’s signal path. Under pre-fader metering, you could pull the fader all the way off (minus infinity) and the meter would still read the source signal’s level. That keeps you forever aware of the source signal and its behavior before the mixer’s controls or processing touch it. Plenty of video editors like working with post-fader metering, yet most audio mixers favor pre-fader so they always know what the actual source level is at any moment.

### Solo and Pre-fader Metering

With pre-fader metering switched on, soloing one or more tracks shows a fainter “ghost” version of meter activity on the non-soloed tracks, so you can always see audio levels on tracks the soloing process has muted. That makes it simple to concentrate on the tracks actually audible while still watching activity on those that aren’t. When pre-fader metering is off (the default), soloing one or more tracks leaves no metering on the unsoloed tracks.

Pre-fader metering with light shaded meters on non-soloed tracks
