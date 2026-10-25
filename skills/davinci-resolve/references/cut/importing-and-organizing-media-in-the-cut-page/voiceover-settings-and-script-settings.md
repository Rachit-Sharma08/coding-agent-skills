# Voiceover settings and script settings

Version: DaVinci Resolve 20.3 Reference Manual. Context: Importing and organizing media in the cut page.
[Chapter index](INDEX.md) / [Previous section](relink-media-and-relink-selected-clips.md)
<a id="source-atem-switcher-integration"></a> <a id="source-importing-atem-mini-pro-iso-projects"></a> <a id="source-relinking-blackmagic-camera-masters-to-atem-isos"></a> <a id="source-script-settings"></a> <a id="source-voiceover-settings-1"></a>

### Voiceover Settings

- Audio Input: Pick which computer interface your microphone plugs into.
- Record Track: Pick which audio track on the timeline the VO records onto. The Cut page makes a fresh track named VO by default, though this setting lets you redirect it to a different track yourself.
- Monitoring

Timeline & Microphone: Lets the timeline audio and your voice input both reach your ears

as you’re recording.

Timeline Audio Only: Routes just the timeline audio to your ears as you’re recording.

Microphone Audio Only: Routes only your voice input to your ears and silences the timeline as you’re recording.

Mute Monitoring When Recording: Silences every bit of audio playback as you record. Handy for sidestepping audio feedback in some headphone-less recording setups.

- No Countdown: No visual countdown shows up — once you hit Record, just start talking.
- 3 Secs Countdown: Shows a three second visual countdown on the viewer ahead of the

recording, leaving you a brief moment to get set first.

- 5 Secs Countdown: Drops a five second visual countdown onto the viewer ahead of the recording, giving you a moment to get set first.
- Voiceover Recording File Location: Pick where your new audio files get saved.

### Script Settings

- Enable Prompter Overlay: Switches the loaded script’s text overlay on or off.
- Load Script File: Brings up a file selector for picking a text file to load into the prompter.
- Clear Script File: Takes the text file back out of the prompter.
- Font Size: Lets you set the font size of the on screen text.
- Line Spacing: Lets you set the line spacing of the on screen text.
- Side Margin: Lets you set how wide a margin the on screen text uses.
- Background Opacity: Lets you set how transparent the on screen text is.

Audio Meters: A small bank of audio meters reports your microphone’s audio levels. Input Monitoring: Click the headphone icon to switch between hearing your microphone input as you record and muting it.

Cue: Snaps the playhead back to the initial record In point.

Record: Begins recording audio onto the timeline. Stop: Halts the audio recording. Voice Isolation: Switches on the Voice Isolation effect while you record to cut down background noise. Dialog Leveler: Switches on the Dialog Leveler effect while you record to hold your track at a steady volume. Stereo Fixer: Switches on the Stereo Fixer effect while you record to clear up the usual channel errors that crop up when converting between mono and stereo sources.

### ATEM Switcher Integration

When you’ve captured a multi-camera event on the ATEM Mini Pro ISO or ATEM Mini Extreme ISO, the whole project can be brought across into DaVinci Resolve. An ATEM project carries the master program clip, plus the “ISO” (isolated) clips from each separate camera, along with the audio captured for every camera angle. Every transition, all the timecode, and the camera number metadata come over, along with whatever graphics had been kept in the ATEM’s Media Pool. With the project loaded, you can pick your multi-camera edit right back up in the Cut page. Pairing this opening live recording with later post-production editing is a workflow commonly known as “Live to Tape.” Live to Tape hands you all the spontaneity, verisimilitude, and quick turnaround that come with live production, while adding the freedom to insert or cut sections afterward and reshape the program’s editorial flow. Live to Tape also lets you patch up minor slip-ups, like swapping in a better camera angle or refreshing a title or graphic. That flexibility is why Live to Tape is the go-to method for shooting nearly every broadcast network game show, current events show, and sitcom. In short, any multicamera production whose core purpose doesn’t hinge on being live in real time (the way news or sports does) gets shot Live to Tape instead. Everything the Live to Tape workflow calls for is supplied by the ATEM Mini Pro ISO and ATEM Mini Extreme ISO:

- A program master clip shot live that holds all the mixed camera angles, audio, transitions, and so on, running from the show’s opening to its close, kept for reference.
- A separate ISO recording from each camera that fed the program master clip. An ISO is an isolated (ISO) camera recording covering the whole show from that single camera’s point of view, start to finish and uninterrupted.
- A timeline of the live-recorded show marking where every camera angle got switched, which transitions were applied, and which graphics took part.

NOTE: Only on MacOS can you get the ATEM’s live webcam view.

### Importing ATEM Mini Pro ISO Projects

Bringing in an ATEM project basically reconstructs the master program clip as a timeline within DaVinci Resolve out of the camera ISOs, transitions, and graphics. The resulting timeline lines up with the master program clip in every respect, only it’s assembled from the original source materials rather than delivered as one compressed video file. Consult your ATEM’s own documentation on configuring ISO recording, but one key setting is making sure the “ISO Record All Inputs” setting is checked in the ATEM software control before shooting begins. Here is how to import an ATEM Mini Pro ISO Project: 1 Ahead of shooting, confirm that, within the ATEM software control, the “ISO Record All Inputs” setting is turned on. 2 Now record your show on the ATEM device and take note of where the project’s folder lives. 3 Select File > Import Project. 4 In the file browser, choose the DaVinci Resolve Project file (.drp) sitting in the ATEM project folder. 5 Click on the Open button.

An ATEM Mini Pro project opened in the Cut page Sync bin

### Relinking Blackmagic Camera Masters to ATEM ISOs

The ATEM captures every camera’s ISO as an H.264 HD video stream, whose resolution or quality may fall short for certain needs. You can swap your ATEM camera ISOs over to the original camera recordings made on a Blackmagic Camera in an instant instead. This workflow unlocks the top visual quality of Blackmagic RAW plus the option to deliver at higher resolutions (4K or UHD, for example) beyond what the ATEM handles internally. In effect, the ATEM can point to an extra set of higher-quality ISOs recorded inside the cameras rather than the ones from the ATEM itself. The feature works only with Blackmagic Cameras. This workflow adds one more step, which is making certain each camera has enough recording space attached to capture the entire show. Consult your ATEM’s own documentation on configuring ISO recording and camera control, but one key setting is making sure both the “ISO Record All Inputs” and the “Record in All Cameras” settings are checked in the ATEM software control before shooting begins.

Here is how to relink to Blackmagic Camera masters from ATEM ISO recordings: 1 Ahead of shooting, confirm within the ATEM software control that the “Record in All Cameras” setting is on. 2 Ahead of shooting as well, confirm that the same control has the “ISO Record All Inputs” setting on. 3 Now record your show on the ATEM device and take note of where the project’s folder lives. 4 Copy every resulting camera master off each camera’s memory card into the ATEM project’s “Video ISO Files” folder, then import the project into DaVinci Resolve. 5 DaVinci Resolve makes a separate Blackmagic RAW folder in your project on its own and shifts all the camera masters there. 6 Through the menu Timeline > Switch to Camera Originals, you can flip in an instant between pointing at the ATEM H.264 ISOs and pointing at the Blackmagic Camera masters.

After your project comes into DaVinci Resolve successfully, you can cut it with the array of dedicated Multicam editing tools the Cut page provides, the Sync Bin, Live Overwrite, and the DaVinci Resolve Speed Editor included.

To read up on putting these tools to work, turn to Chapter 28, “Fast Editing in the Cut Page.”
