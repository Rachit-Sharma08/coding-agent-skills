# Dolby atmos integration and binaural audio monitoring

Version: DaVinci Resolve 20.3 Reference Manual. Context: Immersive audio workflows.
[Chapter index](INDEX.md) / [Previous section](about-immersive-audio-formats-and-dolby-atmos.md) / [Next section](enabling-the-ambisonics-meter-overlay-and-ambisonic-effects.md)
<a id="source-ambisonic-file-support"></a> <a id="source-ambisonic-metering-options"></a> <a id="source-ambisonic-orders"></a> <a id="source-ambisonics"></a> <a id="source-ambisonics-metering"></a> <a id="source-binaural-audio-monitoring"></a> <a id="source-binaural-render-options"></a> <a id="source-dolby-atmos-integration"></a> <a id="source-enabling-ambisonics"></a> <a id="source-the-binaural-monitoring-option"></a>

### Dolby Atmos Integration

The internal Dolby Atmos workflow is natively supported on Mac M1, Windows, and Linux, covering:

- Input
- Content creation
- Internal renderer
- Export of Dolby Atmos Master Files

A purpose-built Dolby Atmos Master bus format supplies a master fader in the Mixer for the Dolby Atmos Renderer and carries the Dolby logo in its header. It likewise shows a loudness history graph in its Timeline view, reporting integrated, momentary, and short term loudness figures. The Bus Format window reveals that this track has no outputs; it serves to control the Dolby Atmos Renderer. You may create only one master bus, and it will at all times reflect the format and metering of the internal renderer. With no patches present on the Dolby Atmos Sends, every source routed to a Dolby Atmos Master bus aims at the master, just as a traditional bus workflow would. Within this send workflow, buses turn into beds while tracks turn into objects. On Mac and Windows systems, the external Dolby Atmos Renderer integration has been refreshed for a much tighter fit when you run an external workflow. That has brought the tools of the internal renderer workflows into line with those of the external renderer. It covers:

- External Renderer discovery within the preferences.
- UI enable to switch between the internal and external workflow.
- Tally of the master connection state and master file status.
- Saving and recalling the program metadata inside the DaVinci Resolve Timeline, taking in every input

configuration, trims, down-mix, and binaural settings.

- Hands-on control over the renderer's metadata plus the binaural controls inside DaVinci Resolve, with two-way control of that program metadata reaching back from the server.
- Tally of the input configuration within the Patch page.
- Support for multi-client workflows, so several DaVinci Resolve instances can run while attached to

the same server for larger workflows.

- A tally, on the Patch page, of the bed and object assignments currently active on the Dolby Atmos Sends.

As you map a bed or track to the Atmos Master on the Patch page, a purple marking flags beds and a green marking flags objects.

### Binaural Audio Monitoring

To monitor your Dolby Atmos Master in Binaural, pick Binaural in the monitor section.

### The Binaural monitoring option

According to your monitoring rig, you can additionally build a parallel speaker monitoring setup alongside Binaural. You might, say, run a 5.1. external monitor mix together with a binaural headphone mix. Under Preferences > Video and Audio I/O, within the Audio I/O panel you can route Binaural to the headphone outs, and set a 5.1 monitor under the Monitor Speaker configuration. After that, in the Patch Input/Output panel, you can route to whichever positional channels suit your system and settings while also assigning the channels available for the headphones.

Using the Patch Input/Output to assign parallel binaural monitoring

### Binaural Render Options

Binaural rendering models the gap between a sound source and the listener. The Index offers choices for how you would like the binaural objects rendered. Mid is the default choice, but Off, Near, or Far are also available, according to the binaural rendering you want. Every one of these choices is saved into the Dolby Atmos file.

Binaural choices in the Tracks Index for assigning perceived distance You can rely on Clip Attributes to render a Dolby Atmos Master in Binaural. Just right click the file to bring up Clip Attributes, choose Binaural, then right-click to spin up a new Timeline containing the file. In the case below, a 7.1.4 file gets rendered out to a Binaural audio file.

Using Clip Attributes to render to a Binaural file

### Ambisonics

As a full-sphere, multi-channel, immersive “adaptive” audio format, Ambisonics enables placement of sounds throughout both the horizontal and the vertical planes. Set against other surround formats, the transmission channels of Ambisonics are not tied to particular speakers; they convey a whole sound field that a specialized microphone captures for a precise positional rendering of “sound in space,” or that sophisticated encoders generate out of channel-based sources. That flexibility lets Ambisonics work with a range of speaker layouts — 5.1 and 7.1.4, headphones, and big arrays — across many uses, among them theme parks, art installations, video games, and virtual reality. You can even mix and move between channel-based and Ambisonics formats with no third-party audio plugins required. The full Ambisonics support in DaVinci Resolve Fairlight covers spherical panning, Ambisonic bussing, Fairlight, AU, and VST Ambisonics effect plugins, precision reaching fifth order High Order Ambisonics (HOA), along with decoding — both channel and binaural — out to headphones.

### Ambisonic Orders

The “orders” of Ambisonics set the mathematical precision and the count of discreet channels used to depict the sound field, spanning the first through the seventh order. First order draws on four discreet audio channels, whereas higher orders call on more channels and thus more processing power. DaVinci Resolve Fairlight goes up to fifth order Ambisonics — which needs 36 channels — yet you can achieve strong results with third order and 16 channels.

### Ambisonic File Support

For Ambisonic files, the formats DaVinci Resolve accepts are WAV, BWAV, and .caf (1OA AMB and AmbiX included). Dropping a Media Pool clip onto the timeline, or building a new timeline that points at a clip, generates a track of the matching type, mirroring the file's Ambisonic order and channels.

### Enabling Ambisonics

Switch Ambisonics on by opening Preferences > Video and Audio I/O and ticking the Enable Ambisonics checkbox within the Immersive Audio section.

### Ambisonic Metering Options

Mixer and Track Header Meters Fairlight Ambisonic metering relies on one composite bar-graph meter across the Mixer, Track header, and Meter panel. In contrast to other audio formats, these do not map to particular speaker positions or levels that we would visually track to read what the signal is doing. As an alternative, you may prefer bar-graph meters that present Ambisonic signals as separate, discrete bus streams by choosing Fairlight > Immersive Audio > Ambisonics Channel Metering.

Default Ambisonics metering (left) and Discrete Channel metering (right)

### Ambisonics Metering

This Fairlight FX audio plugin provides two distinct visual metering views for examining your audio. You can drop the Ambisonics meter onto an audio track or bus through the Effects section of the channel strip. For details about the Ambisonics Meter, consult Chapter 181, “Fairlight FX.” Video Viewer Overlay On the Fairlight page, Ambisonic metering is likewise offered as overlays sitting on top of the Video viewer, so you can weigh the sound intensity against the picture. To switch on the Ambisonics Meter overlay:

- Activate 360 Viewer Mapping in the Video Viewer tools menu.
- Open the Ambisonics Meter submenu, click On, then pick one of the available metering modes.
