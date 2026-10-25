# Audio panel and file

Version: DaVinci Resolve 20.3 Reference Manual. Context: Rendering media.
[Chapter index](INDEX.md) / [Previous section](dcp-and-imf-composition-settings-and-subtitle-controls.md) / [Next section](additional-render-outputs-and-overwrite-prevention.md)
<a id="source-audio-panel"></a> <a id="source-file"></a> <a id="source-rendering-media-part-4"></a>

### Audio Panel

Every audio-oriented parameter lives in this panel.

- Export audio: Tick this checkbox to render the source audio — or audio you synced inside DaVinci Resolve — alongside whatever media DaVinci Resolve outputs.
- Format: Choose which audio format to render. Your choice of format brings up different audio codec options beneath it.

MXF OP1A(IMF): Produces media files matching the OP1a (Operational Pattern 1a) SMPTE 378M flavor of MXF media for file exchange. MXF OP-Atom: Produces media files matching the SMPTE 390M flavor of MXF media for file exchange. QuickTime: Surfaces every audio format QuickTime can handle. MP4: Produces media in the MPEG-4 file format. WAVE: Produces media in the WAVE file format. MP3: Produces media in the MPEG-3 file format. FLAC: Produces media in the FLAC file format.

- Codec: Pick among Linear PCM (the default), AAC audio, IEEE Float, or MP3. Encoding to AAC audio is offered on macOS only.
- Sample Rate: Sets the audio output’s sample rate, given in Hz.
- Bit Rate Strategy: (Available for AAC encoding) Pick from Constant Bit Rate,

Average Bit Rate, Variable Bit Rate Constrained, and Variable Bit Rate.

- Quality: (Open during AAC encoding once Bit Rate Strategy rests on Variable Bit Rate) Five settings that balance speed against quality while encoding AAC audio.
- Data Rate: (Open during AAC encoding once Bit Rate Strategy rests on Constant, Variable, or Variable Constrained) Picks the ceiling data rate for AAC encoding.
- Bit Depth: Sets the bit depth used when outputting the source audio.
- Render one track per channel checkbox: This checkbox decides whether each channel is exported as its own track within the exported file’s structure. Multi-channel formats can be named (2.0, 5.1, etc.), or the output can take the form of flat multi-mono files.
- Render as discrete audio tracks checkbox: Much like the one above, this checkbox still writes one channel per track. Discrete tracks, though, carry no positioning info and don’t cluster into multi-channel clips (2.0, 5.1, etc.). A mono file exported via Render one track per channel, for instance, arrives front and centered, whereas the same file exported as a discrete audio track holds no built-in position information.
- Output Track #: This dropdown menu picks which Main or Submix bus to output. The Plus button on its right lets you tack on further tracks for export within this job, so exporting several Mains or several Subs just means adding more Track pop-ups.

Selecting a track that carries several audio channels brings up a field reporting how many channels will be output, and a virtual slider lets you alter that count. Under Single Clip Mode, choosing “All Timeline Tracks renders every audio track in the present timeline as its own track inside the media file you’re outputting. Tracks holding multi-channel clips emit output tracks with the same channel count, so you can put out mixed sets of mono, stereo, 5.1 or 7.1, and adaptive audio tracks, with each independently rendered track mirroring identical channel mappings.

- Language: (Only available when outputting to the IMF format) This dropdown sets the language of a given output track as you output to IMF. Because an IMF file can hold several audio tracks bearing different mixes for different regions, labeling each output track by language matters.
- Content: (Only available when outputting to the IMF format) This dropdown sets the content of a given output track as you output to IMF. Because an IMF file can hold several audio tracks bearing different mixes and content, tagging each output track by content matters.
- Audio Normalization: Loudness standard presets chosen from the Audio tab of the Delivery page’s Render settings have the deliverable normalized to suit automatically. These controls govern audio normalization one output at a time, and clearing this box skips audio normalization and optimization altogether.

Normalize to Standard: Tick this box to bring loudness or peak (whichever crosses thresholds first being scaled) into line with a standard. Optimize to Standard: Tick this box to optimize loudness and peak together against a standard, holding loudness within the wanted range while keeping peaks under threshold. Standard: Pick the normalization standard to apply. Target Level: Enter the normalization level in dBFS. Output Track #: Tick the box to direct the normalization at these outputs.

### File

Every remaining parameter sits in this panel.

- Filename Uses: Three options handle naming the output media file(s) for you.

Use Custom Filename: Lets you type a name of your own into the Custom name/File prefix field. Use Timeline Name: (Applies while a Single Clip renders) Pick this and the Timeline’s name is used. Use Source Filename: (Applies while Individual Clips render) Pick this and the filename of each clip’s matching source media file is duplicated and applied to the media DaVinci Resolve outputs. It’s the go-to choice when you’re making offline media for an editor that you later plan to reconform back to the original DaVinci Resolve project. Clear this checkbox and you can shape filenames through the other options in this batch of settings.

- Custom name: Lets custom text name all rendered files. As long as you’re neither using the source filename nor rendering to a timecode-based file format, you can type a filename here. While editing the Custom Name or File Prefix (or File Suffix), “metadata variables” are available — graphical tags you drop in to surface clip metadata. That comes in especially handy when rendering Individual Source Clips. Add the metadata variable tags %scene*%shot*%take, say, and the File Prefix would read “12_A_3” provided “scene 12,” “shot A,” “take 3” sat in the source clip’s metadata.

Chapter 16, “Using Variables and Keywords,” covers how variables are used and lists every variable DaVinci Resolve makes available.

- File suffix: Lets custom text and/or metadata variables (covered above) attach to the tail end of all rendered files.
- Use unique filenames: (Applies as Individual Clips render, and only with Filename uses on Custom name) Switched on, extra characters get appended to each rendered media file so that every one ends up with a wholly distinct name. That keeps several rendered clips off the same source media file from clobbering one another in a shared directory. A “uniquely” named clip tacks the track and clip number — pinpointing the clip’s slot in the active session — onto the clip name. A clip tied to a media file called “DropThatThingCU.mov,” cut in as the twenty-fifth clip on track V2, renders out as “DropThatThingCU_V2-0025.mov.” Turning it on also unveils two further options.

Use unique filename prefix/Use unique filename suffix: (Shown once Use Unique Filenames is active) Radio buttons govern whether the unique identifier lands at a clip’s start or finish. Pick Prefix and you’d get “V2-0025 \_DropThatThingCU.mov,” while Suffix would render as “DropThatThingCU_V2-0025.mov.”

- Add source frame count to filename: (Active as Individual Clips render, provided Filename uses sits on Custom name) Switched on, each clip’s source frame number gets stuck onto the end of the rendered file name — yet another safeguard against custom-named rendered clips overwriting each other.
- Use filename digits: Sets how many digits to use when rendering an image sequence, though the count you pick carries over to any media format. It’s handy when your output feeds an application with strict image sequence numbering rules. The default is eight digits.
- Each clips starts at frame: (When rendering Individual Clips) This allows timecode in the header and a frame count in the filename of the image sequences, well suited to VFX workflows.
- Start timeline timecode at: (When rendering Single Clip) Available only when you render clips in Single clip order, this names the timecode written into the media DaVinci Resolve outputs. With DPX files, the timecode goes into the header data and is at the same time turned into a frame count slotted into each frame file’s name, giving a logical tally of the frame numbers. For other media formats the timecode lands in the appropriate metadata container. Custom start times can prove useful — kicking off each reel of a project at a set value, for instance, according to the standards your shop follows.
- Place clips in separate folders: (When rendering Individual Clips) Comes in handy for holding onto the filenames of your output when clips drawn from one source media file would otherwise overwrite each other. It also sees frequent use rendering VFX shots bound for further post-production, letting the VFX department spot clips fast and parcel out the work.
- Preserve Source directory levels: (When rendering Individual Clips) Keeps a depth you choose of the original directory structure behind a clip’s matching source media file, rebuilding it as new output files render. Your chosen number governs how many subdirectory levels DaVinci Resolve auto-creates inside the active “Render job to” directory to echo the path the source files use. The default is 0, which creates no matching subdirectories.

After Head/From Tail: As you decide how many directory levels of each clip’s file path to keep (via the “Preserve x levels” parameter), one of these buttons marks whether that level count is reckoned from the head or the tail of each media file path. Preserved Path: Gives you a preview of the preserved path you’ve built so you can confirm it’s right.

- File Subfolder: (Only appears in Additional Output panels) Names a subdirectory to render the output media files into. Where that subdirectory is missing, a new one bearing the name is built inside the active “Render job to” directory.
- Use commercial workflow: (When rendering Individual Clips) Auto-renders every version riding on each clip in the session, leaving out any version marked with the “Render Disabled” flag in the Version submenu for that clip in the Timeline. You’d typically reach for it after grading several versions of a clip for VFX work and wanting each grade delivered as its own media file. It also serves when rendering programs for commercial broadcast where each scene carries two or more grade versions. Switch it on and alternate methods for outputting each rendered media file kick in, while four extra settings appear.

Alternative pass offset: Spaces out the timecode values stamped into each version of a clip by an offset. Say the default version timecode is 01:00:20:00 and you set a 10 minute offset in the Alternative Pass Offset timecode entry: the clip’s second graded version then begins at 01:10:20:00, the third at 01:20:20:00, and onward until every version renders. The offset value is yours to pick, the aim being to let editors and VFX artists locate each grade’s versions with ease. Hand the clips to a finishing artist who knows the passes sit 10 minutes apart, and switching clip version is just a matter of adding 10 minutes to the referenced timecode. The next three options streamline things further by sorting separate source reels into separate folders. Place reels in separate folders: Drops all media output under a given reel name into its corresponding folder automatically.

Place clips in separate folders: Files alternate grades of clips into separate folders on its own. Use version name for folders: Names each folder after the version while the Commercial Workflow option is active.

- Render speed: A dropdown that lets you rein in how fast media renders. Normally you'd keep it at its default of Maximum. That said, certain storage setups shared across several rooms in a facility rely on storage area networks (SANs) that lack the bandwidth for many real-time image streams at once. The blazing render speeds of DaVinci Resolve can trip up playback for other people hitting the SAN when there isn't enough bandwidth to go around. Here you can rein the render speed in, capping SAN bandwidth usage at somewhere between 1 to 50 percent of full rendering speed.
- Disk space currently used: Reports how much disk space remains free on the target volume.
- Disk space used after render: Reports the projected disk usage given the specified range of the session you're currently rendering.
