# Blackmagic ursa cine immersive and apple vision pro

Version: DaVinci Resolve 20.3 Reference Manual. Context: Apple immersive workflow.
[Chapter index](INDEX.md) / [Next section](image-output-scaling-settings-and-color-management.md)
<a id="source-apple-immersive-workflow"></a> <a id="source-apple-immersive-workflow-part-1"></a> <a id="source-apple-vision-pro"></a> <a id="source-apple-vision-pro-1"></a> <a id="source-blackmagic-ursa-cine-immersive"></a> <a id="source-blackmagic-ursa-cine-immersive-1"></a> <a id="source-davinci-resolve-studio"></a> <a id="source-davinci-resolve-studio-interface"></a> <a id="source-hardware-recommendations"></a> <a id="source-image-scaling"></a> <a id="source-immersive-monitoring-requirements"></a> <a id="source-immersive-video-and-spatial-audio"></a> <a id="source-master-settings"></a> <a id="source-minimum-system-requirements"></a> <a id="source-project-setup"></a> <a id="source-timeline-format-settings"></a> <a id="source-video-monitoring"></a> <a id="source-video-monitoring-settings"></a> <a id="source-workstation-recommendations"></a>

### Apple Immersive Workflow

This chapter walks through producing immersive material for the Apple Vision Pro VR headset out of footage captured on the Blackmagic URSA Cine Immersive camera.

### Blackmagic URSA Cine Immersive

Standing as the first commercial camera system built expressly to record immersive material for the Apple Vision Pro, the Blackmagic URSA Cine Immersive leads the field. A pair of 8K sensors capture 3D video across a 180-degree field of view, delivering genuine stereoscopic depth. Backed by 16 stops of dynamic range and 90 fps recording, it lets filmmakers craft ultra-realistic, high-fidelity cinematic experiences. Footage is recorded in the stereoscopic Blackmagic RAW Immersive format, which opens the door to precise color management and HDR postproduction within DaVinci Resolve Studio.

### Blackmagic URSA Cine Immersive

### Apple Vision Pro

The Apple Vision Pro, a mixed-reality headset, fuses virtual and augmented reality together with real-world interaction to deliver a seamless experience.

### Apple Vision Pro

### Immersive Video and Spatial Audio

As a next-generation cinematic format, Immersive Video is built to surround viewers in lifelike, three-dimensional experiences. Where conventional 360° or VR formats fall short, Immersive Video puts realism and depth first, captured through dual lenses and per-eye sensors at a fidelity nearing human 20/20 vision. Purpose-built encoding formats — MV-HEVC and AIVU — keep playback smooth and motion hyperrealistic. Paired with Spatial Audio, the format produces the feeling of actually standing inside the scene. Spatial Audio, for its part, is a transformative sound technology that yields a three-dimensional listening experience. Through advanced algorithms and object-based mixing, it places individual sounds within a virtual space. That permits exact positioning of voices, instruments, and effects, deepening immersion whether you’re watching a film, listening to music, or gaming. Thanks to head tracking, the soundscape shifts on the fly with the viewer’s movements, pinning audio to the live environment for a realistic effect.

### DaVinci Resolve Studio

As a comprehensive post-production application, DaVinci Resolve Studio knits together editing, color correction, visual effects, motion graphics, and audio postproduction in one place. It accommodates workflows shaped around the Blackmagic RAW Immersive format’s distinct traits – stereoscopic video at ultra high resolution, frame rates reaching 90 fps, plus mixing for Spatial Audio. Thoroughly capable of producing, monitoring, and delivering Apple Immersive Video, DaVinci Resolve Studio makes a potent tool for anyone creating immersive content.

### Davinci Resolve Studio Interface

### Workstation Recommendations

### Hardware recommendations

- Mac Studio M3 Ultra Desktop
- High refresh rate monitor (minimum 60Hz)

### Minimum system requirements

- macOS 15 or later
- 64 GB of system memory
- For monitoring, Blackmagic Design Desktop Video 12.9 or later
- Apple Silicon based computer or GPU which supports Metal

### Immersive monitoring requirements

- Apple Vision Pro
- High-speed wireless network (Wi-Fi 5 minimum; Wi-Fi 6 preferred)

### Project Setup

Ahead of importing Blackmagic URSA Cine Immersive raw media, it pays to step through DaVinci Resolve’s project settings so the footage is debayered and processed properly, giving you the best visual results and an easier edit.

### Master Settings

It matters greatly that you flag, while setting up a project, that your content is bound for the Apple Vision Pro. Doing so surfaces every correct setting and workflow option as you prepare, assemble, and deliver the project. 1 Launch DaVinci Resolve Studio. 2 At the Project Manager window’s bottom-right edge, click New Project. 3 Type a project name, set the Media Location (where required), and click Create. 4 Bring up the Project Settings by clicking the gear icon at the lower right of DaVinci Resolve Studio. 5 To begin, you’ll establish the project’s resolution and frame rate. 6 Pick Master Settings from the sidebar. 7 Within the Timeline Format section, tick ‘Enable Apple Immersive workflow’.

Tick the Enable Apple Immersive workflow option found within the Timeline Format section of the Master Settings window. That single choice sets numerous DaVinci Resolve settings to best suit immersive workflows. Whenever you start an immersive project, always select this option before anything else. 8 Switch the ‘Timeline resolution’ to ‘8160 x 7200 Immersive’ so the clips process at their native sensor resolution. Short on processing power? Pick ‘4080 x 3600 Immersive’ to halve the resolution and play back faster. The ‘Timeline frame rate’ ought to read 90 frames per second. Enabling Apple Immersive workflows sets this parameter for you automatically. 9 Put the ‘Playback frame rate’ at 90 frames per second for the truest reproduction of your Immersive video material. With limited processing power (or a monitor whose refresh rate is lower), drop the frame rate for steadier playback. The advice is to pick a frame rate that divides evenly into the native one, such as 30fps or 60fps.

### Timeline Format Settings

### Video Monitoring

Should you run an external monitor (through a capture/playback device such as Decklink or UltraStudio), set up the video monitoring settings according to that monitor’s specs. 1 Within the Video Monitoring section, make the Video Resolution equal your monitor’s resolution. E.g. 1920 x 1080 HD or 3840 x 2160 Ultra HD. Even though immersive video runs at a native 90 fps, that’s a frame rate few broadcast monitors can handle. 2 Make the Format equal your monitor’s frame rate. E.g. 30p.

### Video Monitoring Settings

### Image Scaling

The Image Scaling settings make certain the immersive media’s resolution and aspect ratio show up correctly in the viewer. Enabling the Apple Immersive workflow option back in the Master Settings would already have set these parameters, but it’s worth confirming they’re right. 1 Pick Image Scaling from the Project Settings sidebar. 2 Within the Output Scaling section, confirm that ‘Match timeline settings’ is unticked.

3 Confirm the ‘Output resolution’ is Custom and reads 4320 x 4320. Drop it by half (2160 x 2160) for smaller displays and/or quicker playback. Square aspect ratio resolutions like these are mandatory both for playing Apple Immersive video material inside DaVinci Resolve Studio and for streaming it to the Apple Vision Pro (over wifi or a developer strap). 4 Confirm that ‘Mismatched resolution files’ is set to ‘Stretch frame to all corners’.
