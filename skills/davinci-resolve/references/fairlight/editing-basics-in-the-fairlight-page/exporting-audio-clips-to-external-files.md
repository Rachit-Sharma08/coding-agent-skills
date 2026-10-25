# Exporting audio clips to external files

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing basics in the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](playhead-fades-and-overlap-crossfades.md) / [Next section](sample-editing-and-waveform-zero-crossing-indicator.md)
<a id="source-editing-basics-in-the-fairlight-page-part-4"></a> <a id="source-exporting-audio-clips-to-external-files"></a>

### Exporting Audio Clips to External Files


Whenever a workflow calls for writing clips out of the Timeline into external files while still giving you broad control over how those files are altered, reach for the Export Audio Files command. To export clips to external files: 1 Pick one or more clips within the Timeline. 2 Right-click the files you've selected and pick Export Audio Files from the contextual menu. 3 As the Export Audio Files dialog comes up, set these: a) Click Browse to point at where the exported audio files should be saved. b) (Optional) Type in a tag plus one of the assorted Name options. c) Set a File Format, Sample Rate, and Bit Depth for what you're exporting. d) Set a Channel Format — either Multi-Mono or Interleaved — for the exported files. e) Set a Source of Individual Clips or Consolidated Clips; a dropdown menu then pins down the ranges, covering the whole timeline, a selected range, or only the selected clips. f) Checkboxes let you narrow things further to just the chosen tracks, fold in hidden tracks, and pad out to frame boundaries. g) On export you're free to bundle in several attributes: Clip Level, Clip Fades, Clip EQ and FX, plus Clip iXML. h) Those exported files can be normalized to preset target levels and target loudness figures using every one of the standards the Fairlight page makes available.

The dialog where you pick the settings for writing clips out to files 4 Click Export. The audio files you selected get written to the spot you picked.
