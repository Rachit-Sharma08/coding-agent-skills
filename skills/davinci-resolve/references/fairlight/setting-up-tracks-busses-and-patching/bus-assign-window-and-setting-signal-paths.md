# Bus assign window and setting signal paths

Version: DaVinci Resolve 20.3 Reference Manual. Context: Setting up tracks busses and patching.
[Chapter index](INDEX.md) / [Previous section](multichannel-link-groups-and-element-editing.md) / [Next section](legacy-fixed-bus-patching-and-a-channel-strips-input-menu.md)
<a id="source-bus-assign-window"></a> <a id="source-choosing-source-and-destination-controls"></a> <a id="source-creating-a-patch"></a> <a id="source-patching-in-icon-view"></a> <a id="source-setting-signal-paths"></a> <a id="source-using-the-patch-inputoutput-window"></a>

### Bus Assign window

NOTE: As long as the dialog stays open, every assignment you've made can be undone one at a time, or redone, through Command-Z and Command Shift-Z respectively.

Assigning Using Icon View Pick a button within the Busses section to highlight that bus's Send or Out, then either click a target track button or pull a bounding box across all the buttons of the available tracks you'd like assigned to that bus. After assignment, the Available Tracks buttons show which bus now holds them. Once assigned, an “o” or an “s” trails the Bus number, signalling whether it's that bus's send or out.

Pulling a bounding box in Icon view to assign several tracks onto one bus at once

### Setting Signal Paths

Although building and assigning busses lets you submix tracks or pass signal from one bus into another, you'll frequently have to route signals from individual external sources onto a track or bus. For instance, recording audio onto a track means patching your hardware's audio input over to the track you intend to record on. In Fairlight this kind of connection is termed “patching,” and it's carried out via the Patch Input/Output window, present on the Fairlight, Edit and Deliver pages, so patching changes can happen on any of them.

### Using the Patch Input/Output Window

Selecting Fairlight > Patch Input/Output brings up the Patch Input/Output window, which you can show in either List (default) or Icon view. The window splits down the middle, the left half holding whichever Source controls you select and the right half holding whichever Destinations you select.

### Creating a Patch

Out of the box, the available Audio Inputs sit as the Source within the Patch Input/Output window, while the Track Inputs sit as the destination. That makes routing any audio source (a microphone on a USB audio interface, say) over to a particular audio track of the Timeline simple in readiness for recording. Connecting and disconnecting a source from a destination is uncomplicated. In the screenshot below, the Audio 1 Input of an audio interface is highlighted and getting patched over to a track called “Walla.”

The Patch Input/Output window with Source Audio Inputs alongside Destination Track Inputs To patch a source onto a destination: 1 Pick a source type from the Source dropdown menu at the upper left of the window. 2 Click the entry on the source list (or action button in Icon view) you wish to patch from along the left side of the Patch Input/Output window. 3 Pick a destination from the Destination dropdown menu at the upper right of the window. 4 Click the list entry (or action button) for the destination you wish to patch to along the right side. 5 Click the Patch button at the lower right of the window. Both the source and destination then display whatever connection now joins them. To break a source-and-destination pairing: 1 Click a list entry or action button for the source or destination you'd like unpatched. 2 Click Unpatch.

### Patching in Icon view

### Choosing Source and Destination Controls

Through the Audio Source and Destination dropdown menus you select various categories of sources and destinations to patch together. These Source options exist:

- Audio Inputs: The physical audio inputs available on your workstation, such as the Fairlight SX-36 audio interface, MADI, third party interfaces (USB or Thunderbolt, for instance), or system audio. Handy while patching to record audio.
- Bus Out: Any Busses.
- Monitor Direct: Monitor system Direct Out, taken post fold up/down matrix and pre the Monitor VolumeLevel/Dim/Mute.
- Monitor Out: Monitor system output. Taken post fold up/down matrix and Monitor VolumeLevel/Dim/Mute.
- System Generator: Supplies assorted utility sources, beeps and timecode generation among them:

OSC: Supplies a test oscillator. Its controls show up in a floating window reached through Fairlight > Test Tone Settings. Noise: Relies on the Noise generator offering a white or pink noise choice, selectable through Fairlight > Test Tone Settings. Beeps: Means the beeps that ADR panel operations produce, whose controls sit on the ADR setup page. Timecode generator: Produces timecode once enabled and the transport runs, its controls living in a floating window reached through Fairlight > Remote Control Settings.

- Track Direct: Track Direct Out, available pre or post the track fader, carrying an offset.
- Track Reproduction: This is the track playback signal, straight off disk, ahead of any processing.
- Dolby Atmos Renderer: The output from the Dolby Atmos Renderer in whatever

Atmos output monitoring format is currently selected. A parallel stereo binaural output exists too for feeding headphones. These Destination options exist:

- Audio Outputs: For instance, the Fairlight SX-36 audio interface, MADI, third party interfaces (USB or Thunderbolt, for example), or system audio. Handy while patching to play audio back to speakers or headphone systems.
- Talk Back: The mechanism that patches the General Purpose Input and General Purpose Output devoted to talkback.
- Track Input: The inputs of the available audio tracks within the current timeline, which feed the Record and Thru path.
- Dolby Atmos Send: When you're authoring original content this needs patching by hand. Import a Dolby Atmos master file, though, and the Send patching across the bed and object tracks comes together on its own. Whenever an external Dolby RMU renderer is on, each source patched onto these sends gets duplicated across the physical outputs that feed the external renderer, following the base audio outputs set in system preferences.
