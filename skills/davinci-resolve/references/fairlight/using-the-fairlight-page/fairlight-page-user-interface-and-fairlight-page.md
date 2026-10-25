# Fairlight page user interface and Fairlight page

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the Fairlight page.
[Chapter index](INDEX.md) / [Next section](track-header-and-zooming-audio-waveform-height.md)
<a id="source-controls-in-the-audio-timeline"></a> <a id="source-fairlight-page-automation-toolbar"></a> <a id="source-fairlight-page-transport-controls"></a> <a id="source-the-audio-page-timeline"></a> <a id="source-the-audio-timeline"></a> <a id="source-the-fairlight-page"></a> <a id="source-the-fairlight-page-user-interface"></a> <a id="source-the-interface-toolbar"></a> <a id="source-the-interface-toolbar-1"></a> <a id="source-the-monitoring-controls"></a> <a id="source-using-the-fairlight-page"></a> <a id="source-using-the-fairlight-page-part-1"></a>

### Using the Fairlight Page

The fully rebuilt Fairlight Audio Core engine can play back as many as 2,000 tracks at once, and it leans on smart load balancing to support the largest possible number of plugins. That higher track ceiling answers what both clients and immersive formats like Dolby Atmos demand. Big studio features and episodic television lean on large track counts so they can hold elaborate mixes and turn out several deliverables. Immersive formats such as Dolby Atmos push those counts even higher, since deliverables span anywhere from 7.1 all the way to 22.2. The pages ahead walk through the fundamental interface controls on the Fairlight page — what each one is, where to find it, and its purpose — so you gain a broad sense of how this combined audio workspace operates.

### The Fairlight Page User Interface

When run on a single display, the Fairlight page gives you a workspace tuned for working on audio tracks. A larger mixer plus dedicated monitoring controls let you cut and shape your audio media with ease, while you check and tweak program levels to land a clean, well-balanced mix.

### The Fairlight page

### The Interface Toolbar

A toolbar sits across the top of the Fairlight page, holding buttons that reveal or conceal the various sections of the interface. Reading from the left edge toward the right, those buttons are:

### The Interface toolbar

Media Pool: Reveals or conceals the Media Pool, the source you draw from to cut audio clips into the Fairlight page Timeline. Effects: Brings up the Audio FX panel within the Effects Library, where you can drop Fairlight FX, or AU or VST audio effects, onto clips or tracks in the Timeline. Index: Toggles the Index together with its Edit Index, Tracks, and Markers panels. Edit Index: Lists every edit event across the visible tracks of the Timeline. Tracks: Gives you control over which Timeline tracks are shown or hidden so you can focus on the ones in play. Markers: Surfaces all of the markers in the Timeline plus the data tied to each one. Scan through every marker together to track down the detail you want fast.

Groups: Toggling this button reveals or hides the Groups list, which you reach for when several tracks need mix changes applied together. The list stays put even after you dismiss the Track Index or switch to a different Index tab. To dig deeper into Track Groups, refer to Chapter 179, “Track Groups.” Sound Library: Toggles the Sound Library panel. Search and filter fields help you pinpoint the sounds you need, and a playback window lets you preview them before cutting them into the Timeline. ADR: Toggles the ADR panel, whose List, Record, and Setup tabbed controls drive how the ADR panel behaves. Mixer: Reveals or hides the Mixer along the right of the Timeline, the place where you tune the effects and levels of every audio track to build your mix. Meters: Toggles the Monitoring audio meters together with the Fairlight viewer across the top of the page. Metadata: Reveals or hides the clip Metadata panel.

Inspector: Reveals or hides the Inspector, the place where individual clip attributes are edited.

### The Audio Timeline

At the core of the Fairlight page sits the Audio Timeline, which lays out the audio channels and tracks belonging to whichever Timeline is active. The number of lanes a given audio track holds depends on its Track Type, or format. Clips you cut into the Timeline show up inside each track, and any multichannel content in a clip fills as many lanes as the track type provides (say, 2 channel stereo, or 6 channels for 5.1). A header packed with controls runs along the left edge of every track. These multi-lane tracks look different here than on the Edit page, which is geared toward simple audio-for-video work and renders multichannel files as composite waveforms on single-lane tracks. There is no way to close the Fairlight page Timeline.

### The Audio page Timeline

### Controls in the Audio Timeline

These are the controls available in the Audio Timeline.

- Timecode fields and Range buttons: These readouts show the Playhead's present timecode along the Timeline Ruler, where the Range In and Range Out points sit, and how long the Range runs. Pressing the Range In and Range Out buttons — positioned to the left of each timecode field — assigns those values and pins their spots on the Timeline Ruler.

Timecode fields and Range buttons in the Fairlight page

- Transport controls: This bar at the top of the Timeline holds transport controls specific to audio, which aren't quite the same as the ones on the Media, Edit, Color, and Deliver pages because recording is part of the mix here. Among them are Fast Reverse, Fast Forward, Play Forward, Stop, Record, Loop, plus the icons that toggle Automation and show the Automation toolbar.

### Fairlight page transport controls

- Toggle Automation button: Pressing this turns on automation recording and playback and inserts an Automation Follows Edit button into the Toolbar, sitting between the Flags and Markers buttons. To read more about the Toolbar, look ahead to “Toolbar,” which appears later in this chapter.
- Automation toolbar: Pressing this reveals a second toolbar that carries every control required to record mixer automation.

To go further on Automation, consult Chapter 178, “Mix Automation.”

### Fairlight page automation toolbar

- Monitoring controls: Three monitoring controls sit at the far right end of the transport controls and give you fast command of your mix's output level. A click on the Speaker icon toggles muting of the audio, and that icon glows red while the audio is silenced.

Sliding the horizontal control raises or lowers the output level by degrees, and the matching signal level appears in decibels as you drag. Pressing DIM briefly drops the output, which comes in handy when you want a short word with your client about sports or current events while still half-listening to the mix. Engaging the DIM function tints the slider yellow.

### The monitoring controls

- Timeline Ruler: The Timeline Ruler shows the program's timecode and, together with the playhead, marks the frame (or sample) you're currently on in the Timeline. A handle sits atop the playhead inside the Timeline Ruler, and you reposition the playhead by grabbing and dragging that handle.

Any Markers you place in the Timeline show up at their matching spots inside the Timeline Ruler as well.

- Playhead: Marks the frame and sample being played and gives you a visual cue of your spot as you play, shuttle, and jog across the Timeline. Meanwhile the big timecode readout in the Timeline's top-left corner also reports where the playhead is. That playhead position doubles as a reference point for editing tasks.
- Audio tracks: Multiple audio tracks are supported on the Fairlight page. A track can carry several lanes to fit the audio channels inside multi-channel clips, drawing on any of the supported mappings: stereo, then 5.1 and 7.1, along with Dolby Atmos, Ambisonics, or an Adaptive track of 1–24 channels. Clips you cut into the Timeline land inside the tracks, and the captured channels take up as many lanes as the clip offers.

To the left of every track sits a matching header region filled with various controls.

The Fairlight timeline splits into tracks and lanes; track A1 is mono and carries one lane for mono audio. Track A2 is stereo and carries two lanes for stereo audio.
