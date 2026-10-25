# Enabling the ambisonics meter overlay and ambisonic effects

Version: DaVinci Resolve 20.3 Reference Manual. Context: Immersive audio workflows.
[Chapter index](INDEX.md) / [Previous section](dolby-atmos-integration-and-binaural-audio-monitoring.md) / [Next section](parallel-loudness-measurement-and-selecting-a-downmix-option.md)
<a id="source-ambisonic-effects"></a> <a id="source-ambisonic-rendering"></a> <a id="source-binaural-monitoring-with-head-tracking"></a> <a id="source-enabling-head-tracking"></a> <a id="source-enabling-the-ambisonics-meter-overlay"></a> <a id="source-export-immersive-master-options"></a> <a id="source-exporting-adm-bwf"></a> <a id="source-head-tracker-preferences"></a> <a id="source-head-tracking-video-viewer-overlay"></a> <a id="source-head-tracking-video-viewer-overlay-1"></a> <a id="source-immersive-audio-workflows-part-2"></a> <a id="source-immersive-format-configuration"></a> <a id="source-monitoring-source-selection"></a> <a id="source-output-format-selection"></a> <a id="source-parallel-ambisonic-and-channel-based-workflows"></a> <a id="source-setting-up-an-ambisonic-mix"></a>

### Enabling the Ambisonics Meter overlay

### Ambisonic Effects

Most Fairlight FX plugins — the Multiband Compressor, Limiter, Reverb, and Channel Dynamics and EQ among them — are Ambisonic-native, and DaVinci Resolve additionally works with compatible Ambisonic-native third-party AU and VST effects. To read up on the Channel Dynamics and EQ plugins, turn to Chapter 177, “Mixing in the Fairlight Page.”

To learn how Audio Effects plugins can be put to use within DaVinci Resolve, turn to Chapter 180, “Audio Effects.” And for the individual Fairlight FX plugins, turn to Chapter 181, “Fairlight FX.”

### Setting Up an Ambisonic Mix

To arrange and configure your Ambisonic mix:

- Begin by deciding which Ambisonic order you wish to work in. A higher one such as third order (16 channels) suits precise positioning best.
- Build Ambisonic busses and route your source tracks or other busses into them. Ambisonic busses can be assigned to other Ambisonic busses, even where the orders differ. The Fairlight engine and FlexBus take care of any up- or down-mixing needed automatically.
- Apply the 2D or 3D Spherical Panners on each channel to set the placement of your sources within the Ambisonic space. Any channel-based format works, from mono through stereo up to, say, 7.1.2, and you can position them freely across the spherical sound field.

To read up on the 2D and 3D Panners, turn to Chapter 177, “Mixing in the Fairlight Page.”

- Click the Bus Monitoring menu at the far right of the Transport control, and pick the source you wish to monitor.

### Monitoring Source selection

- Pick your output format from the Monitor section dropdown beside the speaker output level control. The options on offer include Binaural for headphone monitoring. As soon as you choose a format, the matching decoder is dropped into the monitoring path automatically, and the audio is routed to your Audio I/O and out to your speaker system.

### Output Format selection

### Binaural Monitoring with Head Tracking

When Binaural is your chosen output format, you can also monitor your Ambisonics mix over headphones with Head Tracking support for a richer monitoring experience.

### Head Tracker preferences

### Enabling Head Tracking

Turn head tracking on by going to Preferences > Control Panels > Head Tracker. Doing so places two buttons to the left of the Monitor Bus Source dropdown, just beneath the docked Video Monitor panel:

- HT: Switches Head Tracking on and off.
- CAL: Sets the present tracker heading as the “Front,” treating it as the point of origin.

### Head Tracking Video Viewer Overlay

Binaural Head Tracking also lets you place an overlay on the video viewer to study your mix against the picture: click Headtracking Display > On to add an onscreen crosshair that marks the present head (headphone) orientation. This submenu further holds a Show Torso option that adds a head and torso to the video viewer, which turn as the head tracking angles and positions shift.

### Head Tracking Video Viewer overlay

### Parallel Ambisonic and Channel-based Workflows

Within a single timeline you can build both Ambisonic and channel-based mixes and render several outputs in different formats at once. Thanks to the shared panning data, you can also stand up a parallel mix inside an Ambisonic timeline by converting an existing production of another surround format (e.g., Dolby Atmos) to Ambisonics and pulling that into your production.

### Ambisonic Rendering

On the Deliver page, Ambisonic mixes can render either as a multichannel adaptive file whose stream count follows the Ambisonic order of the mix (e.g., 1OA, 2OA, etc.) or as a downmix to whatever format you pick, such as 7.1.4.

### Immersive Format Configuration

Within Preferences > Video and Audio I/O > Immersive Audio, you can switch on the various Immersive options on offer. The choices include Dolby Atmos, Ambisonics, and Auro 3D; Audio Vivid and MPEG-H Audio; plus BS.2051, 22.2 Surround, SMPTE ST 2098, and 360 Reality Audio. Within Preferences > Video and Audio I/O > Dolby Atmos, you can configure an external Dolby Atmos Renderer to handle the monitoring and mastering for Dolby Atmos. Type the server's IP address in yourself, or choose a discovered server using the dropdown menu. You should also pick the base audio output — the one from among your audio outputs that carries the audio over to the external renderer.

The toggles, under the Video and Audio I/O preferences, that turn on immersive audio formats

### Exporting ADM BWF

Right from the Fairlight timeline, a Dolby Atmos master file can be exported as an audio-only ADM BWF. Those same options are present on the Deliver page too. When you export a Dolby Atmos master file from the Fairlight timeline, the filename comes from the Timeline name. Be sure to rename the Timeline to the filename you want.

- In the Media Pool, locate the current Timeline.
- Change the Timeline name to your desired export filename.
- Just like every other bouncing and delivery method, a range has to be marked in the

Timeline to export.

- Hit R to bring up the Range Selection tool. To set a range spanning a whole clip, double-click any Timeline clip

for the entire clip.

- Choose Fairlight > Immersive Audio > Export Master File.

### Export Immersive Master options

- Within the Export Immersive Master dialog, point the File Name at Timeline Name and the Format at Dolby Atmos ADM BWF. For the exported file's Sample Rate you may pick either 48000 (delivery) or 96000 (delivery). The Source defaults on its own to the Atmos Send Patching. That patching routes the signal by way of the sends into the internal Dolby Atmos Renderer, both to process it and to build a fresh Dolby Atmos master file.
- Click Export. Within the Export Immersive Master finder window, browse to the folder where the file should be saved. Click Save.

The Export Immersive Master dialog laying out the source and format behind the fresh ADM export.

The Export allows for several types of file types:

- Dolby Atmos ADM BWF
- Dolby Atmos IMF IAB
- Fraunhofer MPEG-H Production
- Fraunhofer MPEG-H Production XML
