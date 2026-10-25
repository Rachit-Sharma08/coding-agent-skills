# Toolbar and buttons in the Fairlight page toolbar

Version: DaVinci Resolve 20.3 Reference Manual. Context: Introduction to DaVinci resolve.
[Chapter index](INDEX.md) / [Previous section](node-editor-and-color-page-timeline.md) / [Next section](deliver-page-viewer-and-render-queue-displays-all-jobs.md)
<a id="source-a-new-floating-timecode-window-is-available"></a> <a id="source-buttons-in-the-fairlight-page-toolbar"></a> <a id="source-dedicated-channel-strip-controls"></a> <a id="source-floating-timecode-window"></a> <a id="source-mixer"></a> <a id="source-render-settings"></a> <a id="source-the-channel-strip-dynamics-control-window"></a> <a id="source-the-channel-strip-eq-window"></a> <a id="source-the-deliver-page"></a> <a id="source-the-deliver-page-1"></a> <a id="source-the-deliver-page-timeline"></a> <a id="source-the-monitoring-panel"></a> <a id="source-the-monitoring-panel-1"></a> <a id="source-the-pan-control-window"></a> <a id="source-the-render-settings-list"></a> <a id="source-toolbar"></a>

### Toolbar

Some buttons on the toolbar select among the audio-specific working modes, while others trigger commands like dropping markers and flags.

### Buttons in the Fairlight page toolbar

### Mixer

Through the Audio Mixer you get graphical controls for routing track channels to output channels, shaping EQ and Dynamics, setting levels, recording automation, panning stereo and surround audio, and muting or soloing tracks, all without pausing your edit. The Audio Mixer lays out a row of channel strips whose controls map to the Timeline tracks, one strip per track, alongside a Master strip tied to the Timeline's Master audio track that lets you pick how many audio channels go out and dial in the overall mix level.

### Dedicated Channel Strip Controls

On top of that, the Mixer offers a set of dedicated channel strip controls that bring strong mastering features to DaVinci Resolve. These include:

- EQ
- Dynamic
- Pan

The Audio Mixer, whose channel strips line up with each track found in the Timeline

EQ: A double-click brings up a four-band parametric equalizer that adds Hi and Lo Pass filters and offers graphical plus numeric controls for shaping each track's audio frequencies. From the Equalizer Type dropdown menu you can pick among four EQ filtering varieties: Earth (the default), Air, Ice, and Fire. Each band gives you a choice of filter type — (Bell, Lo‑Shelf, Hi-Shelf, Notch) — together with Frequency, Gain, and a Q-factor that sets how sharp the band is.

### The channel strip EQ window

Dynamics: Double-clicking opens a panel of dynamics controls holding compressor, limiter, and expander or gate sections. Up in the top-left corner, the Equalizer button switches all EQ on or off. You can flip the first section between Expander and Gate operation, complete with Threshold/Range/Ratio and Attack/Hold/Release controls. Compressor controls fill the second section and Limiter controls fill the third. Use these controls on their own or together to shape the dynamics of that track's audio.

### The channel strip Dynamics control window

Pan: A pan control that works for both stereo and surround panning. Dragging inside it adjusts the pan, or a double-click opens a Pan window. Exactly which controls show up in the Pan window hinges on how the audio track is mapped, though stereo and surround panning controls both appear, each with matching numeric controls.

### The Pan control window

### The Monitoring Panel

Every audio meter for the Timeline tracks shows in the Monitoring panel, together with the Master Output meter, Control Room meters, and a video viewer.

### The Monitoring panel

On the left, a column of audio meters lines up with the Mixer's channel strips, one meter per Timeline audio track. Just past these sit all the buses, giving you meters for the Mains and Subs (submixes) you rely on to mix your show down. Further right, a bank of Control Room meters reports the monitored output and loudness meters for an exact read on how loud your mix is perceived to be. Lastly, a compact viewer at the right of the Monitoring panel displays the video frame wherever the playhead sits. A button in the lower right-hand corner lets you undock this viewer.

### Floating Timecode Window

On every page, the Fairlight page included, the Workspace menu offers a timecode window. Selecting it brings up a floating timecode window that reports the timecode for whichever Viewer or Timeline holds focus at the moment. Because the window is resizable, you can scale the timecode up or down.

### A new floating timecode window is available

### The Deliver Page

After your project's grade is complete, you'll need to either render it or send it out to tape so it can reach your client, and that's exactly the role of the Deliver page. Depending on the mode you switch on, the Deliver page handles both digital deliverables and tape output. Whichever path you take, the Deliver page splits into five functional zones, each governing a separate piece of a render or tape output. The Deliver page is built so you can stack up a series of individual jobs, each carrying its own settings or aimed at rendering different stretches of the Timeline. That way you can put out several deliverables or re-render various parts of a timeline however your needs dictate.

### The Deliver page

Further detail on how to work with the Deliver page lives in Chapter 186, “Using the Deliver Page.”

### The Render Settings List

Inside the Render Settings list live the customizable settings that govern how media gets rendered out of DaVinci Resolve. Those settings get fuller treatment later under “Output Scaling.” The Render Settings you can pick from when outputting from DaVinci Resolve are spread across three panels that logically split the Video, Audio, and File information-based settings. Out of the box, this list surfaces only the key criteria needed to define a render, but clicking the “Advanced settings” disclosure triangle at the foot of each settings group reveals further controls.

### Render settings

### The Deliver Page Timeline

What you see here mirrors the Timeline from the Color page. In the Deliver page Timeline you can switch off tracks holding clips you'd rather leave out of the operation, mark the span of clips to render or send to tape, and select which versions of each clip to output. If you prefer, there's also an option to make the Deliver page Timeline look like the Color page Timeline instead. The Deliver page Timeline carries a Timeline Filter drop-down over on the right end of the toolbar too. Filtering the Timeline's contents through this drop-down lets you narrow the range of media you want to output in various ways. Say you've already rendered a timeline but have

made some changes; you can apply the “Show Modified Clips” option to surface only the clips altered within a given timeframe. Alternatively, the “Show Unrendered Clips” option reveals every clip that hasn't been rendered yet.

On the Deliver page the Thumbnail and Mini-Timeline mirror those of the Color page The Viewer When you render file-based media, the Viewer presents exactly how the output media will appear under the current settings, and the transport controls drive the playhead across the active Timeline. To change audio levels, right-click the speaker icon and drag the slider. During tape output, the Viewer reveals the tape output so you can establish insert or assembly edit points, and the transport controls run the tape inside the deck when device control is switched on. You can likewise switch the Viewer into Cinema Viewer mode via Workspace > Viewer Mode > Cinema Viewer (Command-F) so it takes over the whole screen. That same command flips Cinema Viewer mode on and off.
