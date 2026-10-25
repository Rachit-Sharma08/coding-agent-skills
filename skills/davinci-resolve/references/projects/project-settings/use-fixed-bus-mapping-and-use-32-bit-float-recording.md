# Use fixed bus mapping and use 32 bit float recording

Version: DaVinci Resolve 20.3 Reference Manual. Context: Project settings.
[Chapter index](INDEX.md) / [Previous section](general-audio-sample-rate.md) / [Next section](apple-immersive-processing-overview.md)
<a id="source-apple-immersive"></a> <a id="source-audio-metering"></a> <a id="source-enable-ramp-up-on-play"></a> <a id="source-enable-soft-fades"></a> <a id="source-path-mapping"></a> <a id="source-project-media-locations"></a> <a id="source-the-path-mapping-project-settings"></a> <a id="source-use-32-bit-float-recording"></a> <a id="source-use-fixed-bus-mapping"></a>

### Use Fixed Bus Mapping

Should you prefer the older fixed-bus mapping approach, you can apply it to fresh projects by going to the Fairlight panel within the Project Settings and ticking the “Use fixed bus mapping” checkbox. Where a project already runs fixed busing and you’d rather move over to FlexBus, clear the “Use fixed bus mapping” checkbox. Bear in mind that after committing to this switch, there’s no going back to legacy busing afterward. Trading legacy busing for FlexBus brings such big benefits that you won’t look back once you’ve done it.

### Use 32-Bit Float Recording

Ticking this checkbox lets you capture 32-bit floating point audio. You may only adjust this setting before your first timeline gets created.

### Enable Soft Fades

Starting with version 14.0, Fairlight has been dropping in a 1.5ms (72 samples) crossfade automatically wherever timeline clips sit next to each other, so you can cut your audio quickly without hand-placing crossfades to stop clicks or pops while it plays back. The behavior stays on by default, yet you can disable Soft Fades by clearing the checkmark, which proves useful whenever you want to hear each audio clip from start to finish.

### Enable Ramp Up on Play

With this feature switched on, your mix eases in to ward off clicks each time playback gets going. By default the eased-in (ramp-up) duration is 2.1ms, though you can push it as high as 100ms. Ramp Up on Play earns its keep particularly when you’re working on mixes carrying lots of tracks.

### Audio Metering

Within this part of the Fairlight Project Settings, the options let you tailor the Loudness Meters over on the Fairlight page, whereas the remaining ones govern every other audio meter throughout DaVinci Resolve.

- Meter Type: Lets you pick whichever Meter Type you want. Picking Custom out of this dropdown menu switches on the options below:

Level detector: Here you can pick Sample Program, VU, or RMS to drive audio level metering detection. Scale: This option lets you pick either IEC 60268-18 or Quasi Linear to govern audio level metering scaling. Decay: This fixes how many seconds level metering takes to decay in 20 dB increments once peak levels show up on the meters. Peak Indicator: This fixes how long peak level indication is held on the meters.

- Off
- Short hold + fall
- Medium hold + fall
- Medium hold
- Long hold
- Infinite hold
- Pre fader metering on tracks: With this checkbox you decide the way meters over on the Fairlight page present their audio analysis. Two choices exist:

Post Fader (unchecked): The meters always reflect each clip’s signal level once any fader moves have been applied. Pulling a track’s level down shrinks how that audio signal shows up in the meter. Pick this if you’d rather have a visual readout of the relative levels you’ve dialed in across your assorted audio tracks, which leans heavily toward NLE-style behavior. Pre Fader (checked): The meters always go by the volume of the audio clips on that track, even after you’ve dropped the level via the sliders. Should you have keyframed a clip’s volume, the audio meters will mirror that, while fader moves won’t show. Reading the meters this way means you can constantly gauge how much level remains for clips in your mix, no matter where the current fader levels sit, in case you’d like to track audio you might bring back into the mix down the road. That leans heavily toward DAW-style behavior.

- Target Loudness level: Lets you fix the LUFS figure that serves as a reference level for loudness metering. Its default of –23 LUFS handily makes these meters display on a scale much like the traditional audio meters you’re already familiar with.
- Loudness Scale: Lets you pick which scale the meters get measured against. For now the choices cover the default EBU +9 Scale (–18 to +9), plus EBU +18 Scale (–36 to +18).
- Bus Meter Alignment Level: Fixes the bus meter’s peak.
- Bus Meter High Level: Fixes the dB level where the meter begins turning red.
- Bus Meter Low Level: Fixes the dB level where the meter begins turning yellow.

### Path Mapping

Through the Path Mapping panel you arrange your system’s file paths, which lets you link and pass media clips around smoothly while teaming up with other users on their own machines. Take Editor A and Colorist B, who are teaming up on one project. Editor A runs a Mac in L.A., whereas Colorist B runs a PC in Bangkok. The two of them keep media inside a cloud service’s folder, yet the file paths leading to that cloud folder differ locally for each of them.

- On the Editor’s Mac, the folder lives here: /Users/editor/cloudfolder/Episode 12
- Over on the Colorist’s Windows machine, it sits here: D:\Projects\Episodes\cloudfolder\Episode 12

Under normal collaboration, each of them would forever be re-linking the other’s files before carrying on, since the path names wouldn’t line up. Once both of them register the “Episode 12” location and map their own local paths here, DaVinci Resolve switches the file paths over automatically as they go. Re-linking the clips would never be needed so long as every piece of media they touched sat in the same hierarchy beneath the Episode 12 folder. Path Mapping smooths things out for solo workflows too. Picture one user on a laptop: they might build a link running from their local media folder to their NAS. That spares them from relinking media every time they head out and come back to the office. NOTE: Path Mapping isn’t the same as the older Mapped Mount option living in the Media Storage preferences. Mapped mount demands that each user know the file path belonging to all the others. Path Mapping simply lets a user hand over their own file path, and DaVinci Resolve handles the translation on behalf of everyone else.

### Project Media Locations

With this setting you lay out your project’s media locations so they’re simple to share and translate among other DaVinci Resolve users. The aim is keeping a shared media folder among all the users (that is, everyone tied into one shared cloud storage folder) and setting up the path leading to your own personal folder right here.

- Location: Displays the name belonging to the shared folder.
- Local Path: Displays where this folder lives on your filesystem.
- Add: Brings up a filesystem dialog so you can pick the shared folder.

After the location is picked, hit the Browse button and walk through the file system to point the local path at that folder on your machine.

- Remove: Takes a shared folder back out of the Path Mapping settings. Your system keeps the folder; it isn’t deleted.
- Automatically setup when relinking: Switch this setting on and, as you relink offline media, DaVinci Resolve builds a mapping for you automatically. It weighs the path held in the project file against the path the user picked and works out a relative path joining the pair. It then sees whether other offline media in this project turns up along those relative paths and relinks whatever fits. It runs the same check against proxies sitting in proxy subfolders too.

### The Path Mapping Project Settings

### Apple Immersive

With these controls you dial in parameters for producing Apple Immersive content aimed at the Vision Pro VR headset.
