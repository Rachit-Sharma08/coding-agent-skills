# Phantom cine master settings

Version: DaVinci Resolve 20.3 Reference Manual. Context: Phantom cine.
[Chapter index](INDEX.md) / [Previous section](nikon-raw-and-panasonic-varicam-raw.md) / [Next section](phantom-cine-project-settings.md) / [Continue Phantom Cine / Project Settings](phantom-cine-project-settings.md)
<a id="source-master-settings-3"></a> <a id="source-phantom-cine"></a>

### Phantom Cine

The Phantom family of high-speed digital cinema cameras captures wide-latitude, high-gamut media in the Cine Raw format.

### Master Settings

These parameters let you choose, for raw Phantom Cine clips, the decode quality plus the white balance, color space, and gamma they convert to as they are debayered.

- Decode Using: Whatever you choose here dictates whether all Phantom Cine media across the project is decoded with the original Camera Metadata settings (the default pick), with Project settings where you set custom values for every clip, or with the Cine default settings.
- Timecode: Phantom Cine files can use one of four timecode types: Set to zero: Camera timecode is ignored, with a plain frame count used instead and the first frame treated as 0.

Time of day (Local): Records time of day timecode. Time of day (GMT): Records time of day timecode keyed to Greenwich Mean Time. SMPTE: Standard SMPTE timecode.
