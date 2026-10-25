# Dcp and imf composition settings and subtitle controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Rendering media.
[Chapter index](INDEX.md) / [Previous section](advanced-controls-overview.md) / [Next section](audio-panel-and-file.md)
<a id="source-dcp-and-imf-composition-settings"></a> <a id="source-subtitle-controls"></a>

### DCP and IMF Composition Settings

Pick either DCP or IMF from the Format, click the disclosure control, and a Composition Settings group surfaces carrying the parameters below — together they let you fill in generic DCP and IMF composition metadata along with assorted studio-specific settings:

- Composition name: What the exported composition is called.
- Issuer: The organization supplying the composition.
- Use current date: A checkbox that automatically adopts today’s date as the Issue date.
- Issue date: The date on which the composition goes out.
- Content kind: A dropdown listing the permitted choices for defining the content.
- Content originator: A text field naming whoever is accountable for this content.
- Include volume index and output profile list: Tick this box to fold those xml files into

the package.

- Content version label: Intended to mark which version of the content is being supplied.
- Annotate xml using composition name: Fills Asset Map, Composition Playlist, and

Packing List automatically from project data. Left off, you edit those three fields by hand.

- Annotate reel index as suffix (DCP only): Fills Reel Annotation automatically from project

data. Left off, this one is hand-editable.

- Annotate media using filename: Fills Main Video Track and Audio Track 1 automatically from

project data. Left off, you edit those three fields by hand.

### Subtitle Controls

Controls in the Subtitle Settings group dictate how your program’s subtitles get exported:

- Export Subtitle checkbox: Toggles subtitle/closed caption output on or off.
- Format pop-up: Offers four routes for outputting subtitles/closed captions.

As a separate file: Writes each subtitle track you pick to its own file in whatever format the Export As pop-up names, with a bank of checkboxes governing which subtitle tracks get output. Burn into video: Bakes the currently selected subtitle track right into all the rendered video. As embedded captions: Tucks the currently selected subtitle track into supported media formats as an embedded metadata layer. CEA-608 closed captions are presently handled within MXF OP1A and QuickTime files, and the subtitle format comes from the Codec pop-up that turns up.

- Export As: (Surfaces solely with Format on “As a separate file.”) Picks which subtitle/closed captioning format to write out, among IMSC1, DFXP, SRT, and WebVTT.
- Include the following subtitle tracks in the export: (Shown only while Format sits on “As a separate file.”) A row of checkboxes flags which subtitle tracks to output.
- Codec: (Only available when Format is set to “As embedded captions.”) Sets how embedded closed captions are formatted, choosing between Text and CEA-608.

NOTE: At present, neither analog (Line 21) nor digital (CEA-708) closed caption output over Decklink or UltraStudio is supported.
