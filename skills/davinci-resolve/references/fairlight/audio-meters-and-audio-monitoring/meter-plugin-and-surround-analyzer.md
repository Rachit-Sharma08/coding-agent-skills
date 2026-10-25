# Meter plugin and surround analyzer

Version: DaVinci Resolve 20.3 Reference Manual. Context: Meter plugin, Surround analyzer.
[Chapter index](INDEX.md) / [Next section](loudness-meters-and-what-is-lufs.md)
<a id="source-audio-meters-and-audio-monitoring"></a> <a id="source-audio-meters-and-audio-monitoring-1"></a> <a id="source-bus-meters"></a> <a id="source-bus-monitoring-menu"></a> <a id="source-compound-meters-and-output-bus-selection-menu"></a> <a id="source-control-room-meters"></a> <a id="source-for-more-information-see-chapter-181-fairlight-fx"></a> <a id="source-meter-plugin"></a> <a id="source-monitoring-menus"></a> <a id="source-monitoring-with-multiple-speaker-sets"></a> <a id="source-speaker-set-monitoring-menu"></a> <a id="source-surround-analyzer"></a> <a id="source-the-double-height-monitoring-panel"></a> <a id="source-the-meter-fairlight-fx"></a> <a id="source-the-monitoring-panel"></a> <a id="source-the-monitoring-panel-1"></a> <a id="source-the-peak-meter-at-top"></a> <a id="source-track-meters-and-monitoring-controls"></a>

### Audio Meters and Audio Monitoring

Sitting along the top of the Fairlight page, the Meters panel gives you an at-a-glance read on your mix’s track levels, dedicated meters for the busses, meters that watch over the mix and its loudness, and a video Viewer that keeps the current project in view as you work. The pages here walk through how to use these meters and lay out the assorted options on offer.

### The Monitoring Panel

Switch the meters on from the UI toolbar and up comes the Monitoring panel, stretched across the top of the Fairlight page; it presents every audio meter tied to the Timeline’s tracks, plus the Bus meters tied to your mix’s Mains, Subs, and Aux busses, the Control Room meters, and a video viewer alongside.

### The Monitoring panel

Because immersive audio pushes track counts higher, DaVinci Resolve hands you extra metering choices so more tracks stay visible in real time. A right-click anywhere on the meters brings up a menu where you decide whether the Track display shows as a single row or at double height. That same menu also lets you swap between narrow and wide meters. While the wide meter view is active, a double-click anywhere on the Tracks meters panel flips between the single-row and double-height layouts. Move the mouse just under the Tracks panel and a cursor appears that lets you resize the Monitoring panel’s height. You can also resize the Compound meters and the Bus Output meters by hovering at the right edge of the Loudness meter and dragging out to whatever dimensions you want.

### The double-height Monitoring panel

### Track Meters and Monitoring Controls

Over on the left, a row of audio meters lines up with the Mixer’s channel strips, a meter apiece for every audio track on the timeline. The meter count a track shows follows its audio mapping: a mono track carries one audio meter, a stereo track two, a 5.1 track six, and onward from there. Every track and bus meter, the Loudness meters aside, reads out RMS (root mean square) levels against a dB scale. Just above the live RMS levels, a lone line marking the peak value at that instant lingers briefly, while the levels themselves rise as a solid bar climbing up from the meter’s base. What an RMS meter shows is a weighted “average” of the audio level, nearer to how the ear truly hears it, though it gauges perceived loudness less precisely than the loudness meters covered further on in this section.

Track audio meters whose meter count varies with each track’s audio mapping

### The peak meter at top

Color coding on each meter bar flags three distinct sound level “zones,” running from low through medium (green) up to moderately high (yellow) and on to very high (red). A meter is labeled by the track number it stands for (track names don’t appear above track meters), along with that track’s color.

### Bus Meters

Off to the right of the track meters sit the bus meters, where every user-created main and bus shows up, grouped by type, each carrying the meter count that matches that track’s audio mapping. They let you watch the combined level of all tracks routed into a given bus, just as you can from the bus channel strips.

Bus meters for the Mains, Subs, and Aux busses

### Meter Plugin

A Meter plugin is on hand for dropping a meter onto a specific track or FlexBus for a while, or, under fixed busing, onto a Sub, Aux, or Main. These run as sample peak processing meters, handy whenever you’d like one large meter trained on a particular bus as you work.

The presentation here is stripped down: a gray bar tracks the level, and a red peak line, marking the highest peak, lingers for two seconds. Up top, a numeric reading reports the precise level in dB. That figure keeps holding, showing the loudest level caught over any given stretch of playback. From the option menu in this meter’s floating window, you can pick among various settings.

### For more information, see Chapter 181, “Fairlight FX.”

### The Meter Fairlight FX

Here the signal leans further rightward, a sign of how the audio is panned.

### Surround Analyzer

Rather than the usual bar graph, the Surround Analyzer is a graphical meter that paints a spatial picture of the audio under measurement. Since its form keeps shifting with whatever signal plays, people sometimes call it the “jellyfish meter.” This kind of metering proves quite useful; instead of leaning on bars to point out which directions the audio is radiating, you get a clear view of how all the channels relate to one another.

### Compound Meters and Output Bus Selection Menu

Set to the right of the bus meters, the compound meters bring together Control Room meters and Loudness meters, placed side by side to deliver a full picture of your overall audio mix. Underneath, dropdown menus let you settle on which bus to monitor and which set of speakers to do that monitoring through.

The Control Room meters (at left) and Loudness meters (at right)

### Monitoring Menus

### Bus Monitoring Menu

Which bus your audio output (speakers or headphones) monitors comes down to the bus monitoring dropdown menu, and that in turn fixes which bus the compound meters analyze, so you get to pick the bus you monitor as you work. Your pick might be a main, or whatever other bus (or track) you’ve configured and would like to concentrate on for closer work.

From the monitoring menu you select whichever bus you’d like to keep tabs on as you work.

### Speaker Set Monitoring Menu

Just right of the Monitoring menu, the output defaults to “Auto” (provided Automatic speaker configuration is ticked on under Preferences > Video and Audio I/O > Audio I/O). What that does is route your basic speaker setup, on its own and with no room to change it, to whichever stereo or surround output your hardware can manage.

### Monitoring with Multiple Speaker Sets

Should you wish to set up several speaker sets by hand, clearing the automatic speaker configuration preference brings a dropdown into view at the right and lets you pick one of the available speaker sets, once they’ve been set up in the System Preferences’ Video and Audio I/O panel. That gives you the freedom to swiftly check your mix across an array of speakers and configurations, gauging how it stands up under differing conditions. For more on setting up the various speaker arrangements, turn to Chapter 4, “System and User Preferences.”

This monitoring menu is where you settle on the bus to keep an ear on as you work.

### Control Room Meters

The mustard-hued Control Room audio meters present the combined level of every audio channel feeding the bus you currently have selected for monitoring (the one picked in the dropdown menu below). They are peak meters read in dBFS. A true peak audio reading sits at the top of the Control Room meter.
