# Head tracker preferences and head tracking video viewer overlay

Version: DaVinci Resolve 20.3 Reference Manual. Context: Apple immersive workflow.
[Chapter index](INDEX.md) / [Previous section](spatial-filter-and-asaf-scene-spatial-filter.md) / [Next section](bypassing-transitions-and-bypass-transition-settings.md)
<a id="source-asaf-loudness-standard"></a> <a id="source-asaf-metering-options"></a> <a id="source-asaf-rendering"></a> <a id="source-delivery"></a> <a id="source-head-tracker-preferences"></a> <a id="source-head-tracking-video-viewer-overlay"></a> <a id="source-head-tracking-video-viewer-overlay-1"></a> <a id="source-mixer-and-track-header-meters"></a> <a id="source-render-settings-custom-export"></a> <a id="source-space-view"></a> <a id="source-space-view-controls"></a> <a id="source-space-view-of-an-immersive-mix"></a> <a id="source-spherical-plane-view-of-an-immersive-mix"></a>

### Head Tracker preferences

This puts two buttons to the left of the Monitor Bus Source dropdown right beneath the docked Video Monitor panel: HT: Toggles Head Tracking on and off. CAL: Sets the tracker's current direction as the “Front,” or point of origin. With compatible AirPods this button isn't needed and won't show, since calibration runs on its own.

### Head Tracking Video Viewer Overlay

Binaural Head Tracking further lets you lay an overlay over the video viewer for checking your mix against the picture: click Headtracking Display > On, which drops an onscreen crosshair marking the current head (headphone) orientation. That submenu also carries a Show Torso option, dropping a head and torso into the video viewer that turns along with shifts in the head tracking angles and positions.

### Head Tracking Video Viewer overlay

### ASAF Metering Options

### ASAF Loudness Standard

An Apple ASAF loudness standard is on hand within the Metering section of the Fairlight Monitoring Panel. Switching it on means making sure that panel is showing. If it's hidden, click the Meters button in the Interface Toolbar, then pick Apple ASAF off the Loudness menu.

Selecting Apple ASAF from the Loudness menu in the Monitoring Panel

### Mixer and Track Header Meters

Fairlight Ambisonic metering leans on one composite bar-graph meter across the Mixer, Track header, and Meter panel. Unlike other audio formats, these don't line up with particular speaker positions or levels you'd watch to gauge what the signal is doing. As an alternative, bar-graph meters that lay out Ambisonic signals as discrete, separate bus streams are available by choosing Fairlight > Immersive Audio > Ambisonics Channel Metering.

Default Ambisonics metering (left) and Discrete Channel metering (right)

Monitoring Panel meters with Ambisonics Channel Metering enabled

### Space View

Space View is a 3D interactive workspace where you watch the real-time positions and automated movements of your unmuted sound sources, across either of two Scene Modes (Room or Spherical Plane), as covered below. Open Space View by heading to Fairlight > Immersive and picking Space View. NOTE: A source shows up only when it's unmuted and its fader level sits above -70dB.

### Space View Controls

Space View provides the control options below; paired with the track mute and solo buttons, they're highly flexible and let you zero in on individual sources or groups of sources.

### Space View of an Immersive Mix

Over in the workspace's lower left corner sit four buttons letting you view your sound sources from various angles or perspectives. Rotate the workspace freely by holding Command-Option-Shift while you drag. To snap back to a default view, click one of the perspective buttons. Across the window's lower edge sit the following checkboxes:

- Scene Mode: This dropdown flips the Space View mode between Room and Spherical, as shown below.
- Ambisonics Metering: This checkbox switches on Ambisonics sonar-type metering while you work on Ambisonic mixes.
- Auto Zoom: Switched on, this function zooms the view in or out on its own, going by how close the sound sources sit overall to the listening position shown in the 3D space.
- Compact Meters: This option swaps the larger halo-style meters for smaller bar-graphs.
- Show Active Level Only: Click this option to hide the names of silent sound sources.
- Show Beds: This option brings up the labels and meters for ASAF Channel Beds feeding the ASAF Master.

The choices in the drop-down menu to the right of the checkboxes set which objects turn up in the virtual space:

- Show Only Selected: Displays sources based on tracks you've picked in the Mixer or timeline.
- Show Visible: Displays only the active audio sources for tracks left unhidden.
- Show All: Every sound source shows and is labeled.

### Spherical Plane view of an Immersive Mix

Sources can be freely repositioned in the 3D sound field in step with your mouse movements (Left/Right and Forward/Backward):

- Hold Command while moving the mouse forward and back, and the sound

source travels up and down within the sound field.

- Hold Command while moving the mouse left and right, and the sound source travels

left and right within the sound field. Every change you make can be automated (Touch and Pan) and saved.

### ASAF Rendering

With the Timeline Range you want to export set, your ASAF mix can go out as either an ASAF BWF or an APAC MP4: head to the Fairlight menu > Immersive Audio > Export Master File, then from the Format dropdown pick Apple Spatial Audio Format BWF or else Apple Spatial Audio Format MP4, and click the Export button.

### Delivery

On the deliver page, a pair of render settings let you render Apple Vision Pro files for review and final delivery.

### Render Settings– Custom Export

Vision Pro Review: Builds a small MV-HEVC package for previewing. Apple ‘shares’ the resulting file across to the Apple Vision Pro over Wi-Fi, where you watch it in the Apple Immersive Video Utility (AIVU) app, found on the App store. Vision Pro Bundle: Builds a large ProRes file bundle you can archive or run through Apple Compressor to ready it for Apple TV playback. ASAF: Turns out an ASAF audio mix using WAV or MP4 formats. VR180: Produces a stereoscopic video file that conforms to VR180.
