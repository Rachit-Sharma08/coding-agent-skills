# Loading audio wav files in Fusion studio overview

Version: DaVinci Resolve 20.3 Reference Manual. Context: Getting clips into Fusion.
[Chapter index](INDEX.md)
<a id="source-getting-clips-into-fusion-part-3"></a> <a id="source-loading-audio-wav-files-in-fusion-studio"></a>

### Loading Audio WAV Files in Fusion Studio

Fusion Studio accepts audio-only files in WAV format. Because the whole WAV file gets pulled into RAM so its waveform shows up fast in the Keyframe Editor, you should pick the briefest audio file the Comp actually requires, which keeps memory use down. TIP: AIFF files can be loaded on macOS. The audio file may be brought in on its own, separate from any nodes, or you can load it into the Saver node instead. Routing the audio through a Saver node carries the benefit of revealing the audio waveforms inside the Keyframes Editor. Loading a WAV audio file works like this: 1 Over the speaker icon, right-click and choose Choose from the contextual menu. 2 Within the file browser window, pick the audio WAV file track you intend to use. Bringing in a WAV audio file by way of a Saver node goes as follows: 1 Place a Saver node into the Node Editor. 2 Within the Inspector, open the Audio tab and click the Browse button. 3 From that same file browser window, again select the audio WAV file track you want. Displaying the Audio Waveform inside Fusion Studio is done this way: 1 Open the Keyframes Editor. 2 Expand the Saver track so the audio waveform appears. To pinpoint where an audio beat, transient, or cue sits, drag slowly across the audio waveform and listen as it plays.
