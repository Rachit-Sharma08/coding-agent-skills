# Dragging a control point and or right click to delete a point

Version: DaVinci Resolve 20.3 Reference Manual. Context: Apple immersive workflow.
[Chapter index](INDEX.md) / [Previous section](final-node-graph-and-color-grading.md) / [Next section](setting-up-an-asaf-mix-and-creating-an-asaf-master-bus.md)
<a id="source-apple-spatial-audio-format-asaf"></a> <a id="source-apple-vision-pro-cst-settings"></a> <a id="source-asaf-file-support"></a> <a id="source-audio"></a> <a id="source-cst-apple-vision-pro-monitoring"></a> <a id="source-cst-color-management"></a> <a id="source-cst-grading-monitor-mapping"></a> <a id="source-cst-nodes"></a> <a id="source-cst-settings-for-node-2"></a> <a id="source-cst-timeline-mapping"></a> <a id="source-cst-tone-mapping"></a> <a id="source-dragging-a-control-point"></a> <a id="source-enabling-asaf"></a> <a id="source-icc-profiles"></a> <a id="source-or-right-click-to-delete-a-point"></a>

### Dragging a control point

### Or right-click to delete a point

- Over in the 3D palette’s right column, the Feather parameter softens the frame’s edge.
- Tick ‘visionOS Effect’ so the fresh edge data gets handled properly during playback

on the Apple Vision Pro. Leave it off and the edge ends up baked into the rendered video file.

- In the left column, the Left and Right tabs flip between eyes in the viewer.

Bear in mind that a good many of the 3D palette’s controls sit greyed out. Across DaVinci Resolve, parameters turn grey whenever they don’t apply to whatever media you’re actively handling — here, the immersive content.

- In the center column, the Stereo and Mono tabs toggle between single- and double-lens views of the immersive video clip.

### CST Color Management

Applying the Color Space Transform (CST) effect to nodes within the color page’s node editor gives you precise color mapping plus tailored command over the timeline’s peak output nit luminance. The suggested workflow leans on four CST nodes:

### CST nodes

### CST Timeline Mapping

To begin, you map from the camera source input color space into the ‘working’ timeline color space. The Blackmagic URSA Cine Immersive camera runs in the Blackmagic Design Wide Gamut Gen 4/5 color gamut, paired with the DaVinci Intermediate log curve. 1 Bring up the Effects panel. 2 Onto an empty node (01), drag Color Space Transform within the node editor. While mapping the input color space into the timeline color space, this node belongs near the front of the node tree, ahead of any grading operations. Where you instead map straight from the input color space to the monitoring or delivery color space, set this node near the back of the node tree, past the grading work. 3 Give node 01 the label INPUT CST. NOTE: The node labels in these steps exist purely to keep the documentation and screenshots easy to follow. Feel free to adopt whatever naming scheme suits you, or skip labelling entirely. 4 For the Input Color Space, choose Blackmagic Design Wide Gamut Gen 4/5. 5 Make the Input Gamma DaVinci Intermediate. 6 Put the Output Color Space at DaVinci Wide Gamut. 7 Leave the Output Gamma on DaVinci Intermediate.

CST settings for node 1 8 Create a fresh serial node (02). 9 Copy the first node (01) and paste it onto that new node (02). 10 Label node 02 as OUTPUT CST. In this new serial node you’ll want the earlier output color space and gamma to serve as the input, keeping the node tree’s timeline color space consistent. 11 Hit the Swap button to trade the input and output parameters. The Input Color Space and Gamma now suit this CST node. 12 Set the Output Color Space to P3-D65. That’s the present default gamut for Mac displays. 13 Set the Output Gamma to Rec.2100 ST2084, the HDR standard governing a 1000-nit signal.

Every grading operation takes place between those two nodes. Yet because you’re using node‑based color management, you also gain the rare option to act outside the bounds of the timeline color management — something many colorists exploit to bring in particular grading operations, effects, or third-party elements.

### CST settings for Node 2

### ICC Profiles

As an added safeguard that the Blackmagic URSA Cine Immersive signal maps properly to your Mac display, head into System Settings > Displays and confirm the color profile Preset reads Apple XDR Display (P3-1600 nits).

### CST Grading Monitor Mapping

Extra CSTs let you temporarily cap the peak nit output values for monitoring while you grade. 1 Create a fresh serial node (03) following the color management OUTPUT CST (02). 2 Label node 03 as MONITOR.

CST node graph 3 Add the Color Space Transform effect onto the MONITOR node (03). Its input values must line up with the signal coming out of the prior CST. 4 For the Input Color Space, choose P3-D65. 5 Make the Input Gamma Rec.2100 ST2084. Since this CST node exists only to remap the image’s luminance down to a smaller nit value, the input and output parameters can stay identical. 6 Put the Output Color Space at P3-D65. 7 Leave the Output Gamma on Rec.2100 ST2084.

NOTE: There are times when a CST’s color space or gamma needn’t be set at all if input and output match (nothing maps). Here it’s required, because how the custom nit mapping behaves depends on the value and shape of the signal’s log curve. 8 Tick ‘Use Custom Max. Output’. 9 Set the Max. Output (nits) to 250.

### CST tone mapping

That 1000 nit signal now gets remapped down to 250 nits by way of the DaVinci Tone Mapping Method. The upshot is an image that comes very close to the rendered Apple Vision Pro signal as seen on an HDR grading monitor (the Flanders XMP310, Sony BVM-HX310, and the like). To actually monitor your project on an Apple Vision Pro, though, one further tone mapping step is required.

### CST Apple Vision Pro Monitoring

One last CST node opens the door to live monitoring, preview, and final delivery onto Apple Vision Pro devices. 1 Create a fresh serial node (04) following the MONITOR node (03). 2 Copy MONITOR node (03) and paste it onto node 04. You’ll keep the same input and output parameters and alter nothing but the nit count. 3 Label node 04 as AVP.

Apple Vision Pro Monitoring node graph 4 Tick ‘Use Custom Max. Input’. 5 Set the Max. Input (nits) to 250 so the mapped signal arriving from the MONITOR node is read correctly. 6 Set the Max. Output (nits) to 108, the ceiling nit value for monitoring and delivery onto the Apple Vision Pro.

### Apple Vision Pro CST settings

With that in place you can carry on grading, switching off the CST nodes if and when your workflow calls for it. During the first grading pass on your external grading monitor, for instance, turn off the AVP node (04) so you’re seeing the 250-nit signal accurately on that HDR grading monitor. Once you move to previewing in the Apple Vision Pro or to final delivery, switch the AVP node (04) back on. Can the CSTs live in the timeline node editor? No. For now, clip tonal mapping depends on applying the Color Space Transform Adaptation parameter precisely, and that has to happen one clip at a time.

### Audio

Both the Apple Vision Pro and DaVinci Resolve back the spatial and ambisonic varieties, plus AVP (Apple Vision Pro) audio and the AIA (Apple Immersive Audio) formats. Plenty of audio post-production carries on the same way once you’re working in spatial audio. A key departure is that, instead of monitoring on high-end speakers, sound engineers ought to reach for headphones or Airpods to get genuine spatial immersion and a truer take on the audience’s listening environment. Where 2D mixes park most of the dialogue in the center channels, spatial audio has to be placed wherever the sound actually comes from. Ducking, equalization, and balancing have to shape the audio stems so the listener is never overwhelmed or confused. Immersive spatial elements can sit alongside an ordinary stereo stem, letting certain sounds hold steady regardless of how the head turns. That’s useful for keeping non-diegetic material — the music score, voiceovers — clear and easy to follow. Environmental sounds tend to read quieter in spatial audio, so they frequently need a heavier hand in the mix to register, though never to the point of disorienting the listener. Reverb adds a great deal to immersion, being something listeners encounter naturally each day — every sound made inside a given space rebounds off the surfaces around the listener, yielding a ‘blooming’ reverb character. For that reason, reverb is welcomed in spatial audio design to guarantee full immersion. The Apple Immersive Audio (AIA) format acts as a container holding several formats:

- Apple Spatial Audio Format (ASAF): ASAF serves as the raw working audio format.
- Apple Positional Audio Codec (APAC): APAC is the encoded .mp4 format that plays on

APAC-supported devices such as Airpods, or out of an AIVU file on the Apple Vision Pro.

### Apple Spatial Audio Format (ASAF)

The Apple Spatial Audio Format (ASAF) is an immersive audio format built chiefly for VR and AR work on the Apple Vision Pro. macOS-only, ASAF is handled through ProTools (by way of plugins) and DaVinci Resolve (natively). Among ASAF’s advanced technical strengths are built-in support for Ambisonics sources (termed Scenes) and routing through bus assigns. Mixing happens virtually, free of any physical bus, and users can pick from a range of monitoring formats, binaural with headtracking through direct Apple AirPod integration among them. Panning runs through DaVinci Resolve’s established tools — the pan dialog, automation, SpaceView, and in-viewer pan tools — backed by secondary controls in the Inspector. Together they enable exact spatial placement of sources, including automatic tracking against lat-long video. You can export ASAF mixes as WAV or MP4 (with their metadata alongside) through the Immersive Audio > Export Master File option, though for now they can’t be imported or played back inside DaVinci Resolve.

### ASAF File Support

Beyond Ambisonic Scene formats spanning 1OA to 7OA, ASAF Object sources may take on any channel width, from mono through stereo and on to multi-channel immersive audio. That latitude makes it simple to build and draw on beds in any format when assembling intricate immersive experiences.

### Enabling ASAF

Turn ASAF on by heading to Preferences > Video and Audio I/O and ticking the Apple Spatial Audio Format checkbox within the Immersive Audio section.
