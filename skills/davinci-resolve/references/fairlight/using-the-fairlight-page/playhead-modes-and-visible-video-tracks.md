# Playhead modes and visible video tracks

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](zoom-presets-and-customizing-zoom-presets.md) / [Next section](3d-pan-window-and-monitoring-panel.md)
<a id="source-mixer"></a> <a id="source-playhead-modes"></a> <a id="source-repositioning-the-scroller-playhead"></a> <a id="source-showing-video-tracks-on-the-fairlight-page"></a> <a id="source-the-channel-strip-dynamics-control-window"></a> <a id="source-the-channel-strip-eq-window"></a> <a id="source-the-pan-control-window"></a> <a id="source-video-and-audio-scrollers"></a> <a id="source-visible-video-tracks"></a> <a id="source-zooming-the-video-scroller"></a>

### Playhead Modes

As described in the Timeline View Options section earlier, you’ll find settings for Page Scrolling (“Page”) and No Scrolling (“Disabled”). On top of that, Fixed Playhead mode can be switched on whenever you aren’t in Focus mode. Reach it through the Timeline View Options dropdown menu, or via View > Timeline Scrolling > Fixed. Once it’s on, the playhead stays put while the Timeline glides beneath it as you drive the transport controls or JKL to play, shuttle, or scrub in either direction. NOTE: Fixed playhead scrolling isn’t presently offered while Focus mode is active. Bear in mind, too, that switching DaVinci Resolve > Keyboard Customization away from the default DaVinci Resolve mapping to another one rewrites many of the default key commands. As one example, the Pro Tools Keyboard Customization provides no JKL transport.

### Visible Video Tracks

In the toolbar’s Timeline View Options dropdown menu, a checkbox lets you show short-height video tracks in the Fairlight timeline as a reference. That’s quite handy, since it reveals which audio clips line up with which video clips. Those video clips can additionally serve as snapping targets when you position audio. While the Video Tracks option is active:

- The Track Index lets you decide which video tracks show.
- The video track(s) are editable — both their placement and their clip trimming.
- Editing an embedded clip carrying both video and audio drops a clip holding both audio and

video onto the right matching tracks. Turn the Video Tracks option off, and dropping a clip with both video and audio onto the timeline places only the audio on the matching tracks.

### Showing video tracks on the Fairlight page

### Video and Audio Scrollers

Within the Timeline View Options, checkboxes give you the choice of displaying a single Video Scroller plus as many as two Audio Scrollers along the bottom of the Fairlight timeline.

Video and Audio Scrollers at the bottom of the Fairlight timeline When left at the default Low zoom level, the Video Scroller delivers a scrollable filmstrip of your program’s video, frame by frame, with a single scroller frame matching a single frame of your footage. The two Audio Scrollers, by contrast, each let you concentrate on an unbroken waveform view of one chosen audio track. Set which track an Audio Scroller shows using the dropdown menu over in the Timeline header.

Audio Scrollers with their dropdown menu open, the one that picks the track each will display What Are They Used For? No matter how the Timeline tracks overhead are zoomed, the Audio Scrollers consistently give you a magnified look at the particular audio tracks you care about. That lets you zero in on fine details in the audio of the one or two tracks you’re handling, even as the rest of the Timeline lays out the full stack of tracks whose clips play together right then. The Video Scroller, for its part, always presents the precise video frame tied to the present instant, making it a help for exact editing that hinges on frame‑specific tweaks. Beyond that, both the filmstrip and the waveform viewers keep scrolling throughout playback, offering a glimpse of the visual actions and audio cues arriving a moment ahead, which you can lean on while running automation or laying down foley.

### Repositioning the Scroller Playhead

As long as the scrollers are showing, you can drag the Scroller playhead either way across the Timeline to grant yourself more or less preview space on the right.

### Zooming the Video Scroller

A right-click on the Video scroller offers a Low, Medium, or High zoom level. With Low, you see the program frame by frame, much like dragging a strip of film across a Steenbeck flatbed editor. Move to Medium and High and the film strip grows steadily more condensed and scrolls faster. Scrolling the Fairlight Timeline Using the Scroller Tracks Dragging the scroller tracks in either direction scrubs through the Timeline smoothly and in finer detail, no matter how the Timeline tracks above are zoomed.

### Mixer

Through a collection of graphical controls, the Audio Mixer lets you route track channels to output channels, shape EQ and Dynamics, drop in filters and Fairlight FX, dial in levels and capture automation, pan stereo, surround, and immersive audio, plus mute and solo tracks. The Audio Mixer puts up two banks of channel strips whose controls map to the Timeline’s tracks. As a default, the left-hand bank of channel strips presents one set of controls per Timeline track, while the right-hand bank presents a separate set per bus you’ve built to steer signal flow from the audio tracks into submixes and the outputs you want. TIP: Right-click the number atop a mixer channel strip to copy/paste settings, and you can likewise copy/paste settings inside the mini views of the channel dynamics and EQ. On top of that, effects plugins (Fairlight FX, AUs and VSTs) carry their own local 3 dot Options menus in the upper right for copying and pasting settings.

The Audio Mixer, with channel strips that map to the Timeline’s tracks

- Track color: To stay organized, give every track its own color through the contextual menu you get by right-clicking that track, whether in the Timeline or over in the Tracks Index.
- Track number: This shows the number of the Timeline track that goes with each channel strip.
- Input: A dropdown menu through which you patch inputs, busses, and utility signals, plus set up the input

settings for audio signals coming through Blackmagic Design or other hardware interfaces.

- Track FX: This part of the channel strip provides purpose-built, built-in Fairlight FX plugins, fed straight

off disk and then passed along to further effects processing. Among the Track FX you can reach are Voice Isolation and Dialogue Leveler, plus the more recent trio of plugins: Dialogue Separator, Music Remixer, and Ducker. As a DaVinci Neural Engine AI effect, Voice Isolation ships only with DaVinci Resolve Studio. Chapter 181, “Fairlight FX,” covers the Track FX in depth.

- Order: A dropdown menu where, per track, you set the processing sequence among the EQ, Dynamics, and Effects.
- Effects: The Fairlight FX, VST, and Audio Unit effects you’ve added to tracks from the Effects Library show up here, accompanied by controls to enable/disable each one, to open an effect’s floating user interface or Inspector controls, and to remove that effect.
- Effects In: A button that mutes or enables, all at once, every insert effect on a track (Fairlight FX, AU or VST). This control leaves Track FX and the built-in channel dynamics and EQ untouched.
- Dynamics: A double-click brings up a bank of dynamics controls — three groupings that map to an Expander or Gate, a Compressor, and a Limiter — usable alone or together to govern the dynamics of that track’s audio.

### The channel strip Dynamics control window

- EQ: A double-click brings up a four-band parametric equalizer, rounded out by High and Low Pass filters, offering both graphical and numeric controls to lift or cut various frequency ranges of each track’s audio. From the Equalizer Type dropdown menu you can pick one of four EQ filtering flavors: Earth (the default), Air, Ice, and Fire. Those four equalizer types alter the Curves aspect and Q-factor of the transfer function. Each band gives you a filter-type choice (Bell, Lo-Shelf, Hi-Shelf, Notch) together with Frequency, Gain, and Q-factor settings (Q-factor governing the band’s sharpness), and the exact controls an EQ band presents vary with whichever filter type you’ve selected.

### The channel strip EQ window

- Bus Sends: Hit the + sign to create bus sends. They’re offered only when two or more busses exist. Making a bus send calls for at least one extra bus beyond the main output bus.
- Pan: A pan control that works for both stereo and surround panning. Drag inside it to set pan, or double-click to bring up a pan window. Which controls that window holds rides on how the audio track is mapped, but stereo and surround panning controls are both present, each with matching numeric controls.

### The Pan control window

An Option-double-click on the Mixer’s Pan control launches a different 3D Audio Pan window. Where the ordinary Pan window handles stereo and the usual 5.1 and 7.1 surround panning, the 3D Audio Pan window handles the spatial audio placement that advanced surround formats make possible, including Dolby Atmos, Auro 3D, and NHK 22.2.
