# Video input output options in the system preferences and audio i o

Version: DaVinci Resolve 20.3 Reference Manual. Context: System and user preferences.
[Chapter index](INDEX.md) / [Previous section](preferences-system-settings.md) / [Next section](audio-plugin-and-control-panel-preferences.md)
<a id="source-audio-io"></a> <a id="source-audio-plugins"></a> <a id="source-audio-plugins-preferences---vst-effects"></a> <a id="source-dolby-atmos-preferences"></a> <a id="source-immersive-audio-controls"></a> <a id="source-immersive-audio-preferences"></a> <a id="source-monitor-speaker-configuration"></a> <a id="source-monitor-system-external-inputs"></a> <a id="source-video-inputoutput-options-in-the-system-preferences"></a> <a id="source-video-plugins"></a>

### Video input/output options in the System Preferences

### Audio I/O

This area lets you specify the audio hardware plus the various speaker sets you'll use to monitor audio playback. To go beyond the default stereo system output that most workstations fall back on, you'll need whatever utility your operating system provides to select the audio hardware you want and to declare how many audio outputs your chosen monitoring type calls for (stereo, immersive, and the like). On macOS, for instance, you'd turn to the Audio Midi Setup utility to pick output hardware and choose a speaker configuration to make available on your system.

I/O Engine: Lets you select the audio hardware DaVinci Resolve uses to process audio. The options span System Audio, Desktop Video, Fairlight Audio Accelerator, and ASIO (Windows only).

- System Audio: System Audio talks to your computer's native audio hardware and unlocks the parameters below.

Playback processing buffer size: Lets you set the Playback buffer size; off to the right a latency readout shows roughly how much latency your pick adds in milliseconds. Record buffer size: Lets you set the Record buffer size; off to the right a latency readout shows roughly how much latency your pick adds in milliseconds. Input Device: Lets you pick the audio input device from the hardware wired to your system. Output Device: Lets you pick the audio output device from the hardware wired to your system. Automatic speaker configuration: Ticking this box has DaVinci Resolve route audio through your workstation's built-in audio output, even when a compatible video I/O interface is active for capture and playback or for Resolve Live. Clearing this box reveals extra controls for declaring your own speaker arrangement.

Assigning various audio I/O devices, with the buffer tweaks they call for, plus background on audio monitoring and audio input: every bit of the audio processing across DaVinci Resolve—the Fairlight page included, and likewise processing run through Fairlight FX plugins—behaves identically on each platform DaVinci Resolve supports: macOS, Windows, and Linux alike. To be precise, DaVinci Resolve manages audio monitoring and audio input through (i) the audio of a supported Blackmagic Design I/O device along the lines of an UltraStudio or Decklink, (ii) the on‑board audio of your macOS, Windows, or Linux workstation, (iii) whatever third party audio interface qualifies as Core Audio‑compatible or Windows-compatible, as ASIO, or else as Advanced Linux Sound Architecture (ALSA)supported. As another route, you can monitor audio through the optional Fairlight Audio Accelerator, a PCI card built to manage even larger channel counts of audio I/O monitoring and recording, which can also accelerate audio processing tasks for stronger audio performance. NOTE: ASIO is a trademark and software of Steinberg Media Technologies GmbH.

### Monitor Speaker Configuration

Clearing the Automatic Speaker Configuration box exposes a further panel within the Video and Audio I/O Preferences. From there you can map your monitors to the default Main or Near sets, and you can spin up an extra 15 monitor sets tailored to whatever you require.

- Monitor Set: Pick the default Main or Near, or build as many as 15 additional user-definable configurations.
- Rename: This button lets you rename any monitor set to something more

meaningful for your individual needs.

- Format: A drop-down menu lets you pick the format type you want, ranging from Mono up through

Dolby Atmos 9.1.6. Underneath the Format type sit three windows used to build the Monitor Set: Layout: Splits out the channels matching the chosen format. Output: Where you map the Output channels onto your system. Trim: Where you can pull each level down by as much as -24dB of gain or push it up by as much as +10dB of gain to fine-tune the speaker calibration your specific playback room needs.

### Monitor System External Inputs

From this panel you can assemble several monitoring sets, up to 16 user-definable setups. That gives you the flexibility to keep distinct combinations of monitoring speakers on hand and flip among them while checking, reviewing, and building different mixes.

- External Monitor Source: Pick None or as many as 16 definable configurations.
- Rename: Lets you assign a name to an External Monitor Source.
- Format: Picking a Format brings up a drop-down menu letting you choose the

format type you want, from Mono up through Dolby Atmos 9.1.6. After a format is picked, three further windows appear: Layout: Which splits out the channels matching the chosen format. Source: Where you assign either Input Destination or Audio Repro. Input: Where you assign an individual track while on Audio Repro, or assign the specific channel while on Input Destination.

- Rename: This button lets you rename any of the numbered monitor sets to something more meaningful for your individual needs.

Renaming and patching assorted external inputs from within Video and Audio I/O Preferences

### Immersive Audio Controls

This pair of Preference panels lets you set up the flavor of immersive audio you want on hand within your project and also lets you link to a Dolby RMU for handling Dolby Atmos mixing.

- Immersive Audio: From this panel you switch on the assorted immersive audio types DaVinci Resolve provides. Among the supported formats you'll find Ambisonics, Apple Spatial Audio, and Audio Vivid; also Auro 3D, BS.2051, and Dolby Atmos; together with MPEG-H Audio, 22.2 Surround, SMPTE ST 2098, plus 360 Reality Audio.

### Immersive Audio Preferences

- Dolby Atmos: Ticking this box permits use of an external Dolby Atmos renderer. After it's ticked you can key in the RMU's IP address and pick the base audio output.

### Dolby Atmos Preferences

### Video Plugins

You can choose which specific Open FX plugins load at startup, turning others off. Use this to trim and tidy the Open FX list down to just the plugins you reach for often, or to leave out a troublesome plugin that destabilizes the system. On top of that, DaVinci Resolve checks each startup for the last plugin loading result and bypasses any plugins that previously triggered a crash or hang. You can switch individual Open FX plugins on or off by hand in the Video Plugins panel, ticking or clearing the boxes tied to each plugin.

The Video Plugins panel lets you switch specific Open FX plugins on or off at startup.

### Audio Plugins

A trio of parameter sections lets you handle VST effects, enabled plugins, and external audio processes.

- VST Effects: A list up top lets you manually add or drop VST plugin effects directories when needed. Because VST effects don't land in one standard spot, you may now and then have to add a freshly installed directory of VST plugins you've just put on your system.

### Audio Plugins Preferences - VST Effects

- Available Plugins: Once a VST directory or two has been added up top, a follow-on list underneath surfaces every audio plugin discovered inside those directories. Each plugin in the list carries a checkbox indicating whether it's currently active. Any VST plugins that crash DaVinci Resolve while loading at startup get disabled automatically. Use this list to see which plugins were disabled, for troubleshooting, and to switch such "blacklisted" plugins back on by re-ticking their checkboxes.
- Category Column: VST and Audio Units plugins get sorted into categories inside the Fairlight Mixer. To shift a plugin into a different category, click its category name and choose a new one from the Category popup list.

NOTE: This does not apply to Fairlight FX plugins.
