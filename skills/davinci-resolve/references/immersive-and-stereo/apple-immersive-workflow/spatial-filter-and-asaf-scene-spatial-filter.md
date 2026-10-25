# Spatial filter and asaf scene spatial filter

Version: DaVinci Resolve 20.3 Reference Manual. Context: Apple immersive workflow.
[Chapter index](INDEX.md) / [Previous section](offsets-and-asaf-objects-offsets.md) / [Next section](head-tracker-preferences-and-viewer-overlay.md)
<a id="source-asaf-binaural-monitoring-with-head-tracking"></a> <a id="source-asaf-channel--metadata"></a> <a id="source-asaf-channel-controls"></a> <a id="source-asaf-monitoring"></a> <a id="source-asaf-monitoring-source-selection"></a> <a id="source-asaf-scene--metadata"></a> <a id="source-asaf-scene--spatial-filter"></a> <a id="source-effects"></a> <a id="source-enabling-head-tracking"></a> <a id="source-metadata-1"></a> <a id="source-monitoring-output-format-selection"></a> <a id="source-selecting-a-monitoring-format"></a> <a id="source-selecting-the-asaf-master-as-the-monitoring-source"></a> <a id="source-spatial-filter"></a>

### Spatial Filter

### ASAF Scene – Spatial Filter

- Enable: Ticking the Enable checkbox switches the plugin on and reshapes the scene per the Base Gain plus each of the four filters' settings, every filter governed by its own batch of filtering parameters:
- Base Gain: Fixes the overall gain the plugin applies.
- Filter Enable: Switches the individual filter on.
- Filter Shape: Sets whether the spatial filtering shape comes out an ellipse or a rectangle.
- Filter Azimuth: Fixes the azimuth coordinate at the individual spatial filter's center.
- Filter Elevation: Fixes the elevation coordinate at the individual spatial filter's center.
- Filter Width: Fixes the width of the individual spatial filter shape in degrees.
- Filter Height: Fixes the height of the individual spatial filter shape in degrees.
- Filter Focal Gain: Fixes the gain for whatever audio falls inside the individual filter's spatial boundary.

Filter Focal Gain comes in handy when you need to strip an unwanted sound arriving from one particular place or direction. For that, set the filter's position and spread controls to blanket that area, drop the Base Gain to 0.0 db, and take the Focal Gain to -Inf db.

### Metadata

Rather than handling it in the Track Index, the ASAF Scene Metadata part of the Audio Inspector lets you attach the right metadata information to the scene through the settings below:

### ASAF Scene – Metadata

- Content Type: This drop-down menu sorts the object into either Music and Effects or Interactive.
- M & E Tag: Once the content bears a Music and Effects tag, this dropdown's options help you define the object more precisely—for instance, Music, Effects, Dialogue, Narration, etc.
- Interactivity: Once the content was tagged Interactive, an entry chosen from this list defines the object further, perhaps Commentary or Audio Description.
- Language: This dropdown lets you set the content's language.
- Salience: Hands the object audio a level of importance so the ASAF export

encoder can rank it against the project's other ASAF objects.

- Post Reverb: While active, the object is configured so the playback application, such

as Vision Pro, can read the room characteristics of the users' listening environment and, if they wish, layer in a fitting reverb setting. Post Reverb stacks on top of whatever reverb settings the ASAF Object Reverb noted above applies. It leaves the output from the ASAF Renderer plugins untouched, though.

### ASAF Channel Controls

The parameters below let you set the metadata for a Channel Bed:

### ASAF Channel – Metadata

- Content Type: This drop-down menu sorts the bed into either Music and Effects or Interactive.
- M & E Tag: Once the content bears a Music and Effects tag, this dropdown's options help you define the bed more precisely—for instance, Music, Effects, Dialogue, Narration, etc.
- Interactivity: Once the content was tagged Interactive, an entry chosen from this list defines the bed further, perhaps Commentary or Audio Description.
- Salience: Hands the audio a level of importance.
- Language: This dropdown lets you set the content's language.
- Post Reverb: While active, the Channel Bed is configured so Vision Pro can read the

room characteristics of the users' listening environment and layer in a fitting reverb setting. Post Reverb leaves the output from the ASAF Renderer plugins untouched.

### Effects

Ambisonic-native Fairlight FX plugins — the Limiter, Channel Dynamics, and EQ among them — together with compatible Ambisonic-native third-party effects in AU and VST form. The Fairlight FX plugins are documented more fully in Chapter 181, "Fairlight FX." As for working with VST, VSTi, and Audio Units plugins, that's covered in Chapter 180, “Audio Effects.”

### ASAF Monitoring

Fairlight gives you options for choosing the output monitoring source you'd like to hear, plus the output format you'd like to hear it in.

### Selecting the ASAF Master as the Monitoring Source

To make the ASAF Master bus your monitoring source, click the Bus Monitoring menu off at the far right of the Transport control and pick ASAF out of the dropdown.

### ASAF Monitoring Source Selection

### Selecting a Monitoring Format

To pick a monitoring format, click the dropdown beside the speaker output level control. Among the various options you'll spot Binaural, for monitoring over headphones. With a format chosen, the matching decoder slots automatically into the monitoring path, and the audio travels to your Audio I/O and out to your speaker system.

### Monitoring Output Format selection

### ASAF Binaural Monitoring with Head Tracking

Having picked the Binaural option for your output format, you can also monitor your ASAF mix over headphones with Head Tracking support, delivering the full Apple Spatial Audio experience.

### Enabling Head Tracking

You turn head tracking on by heading to Preferences > Control Panels > Head Tracker. NOTE: These settings only need configuring when you're on a third-party head tracker rather than compatible Apple AirPods.
