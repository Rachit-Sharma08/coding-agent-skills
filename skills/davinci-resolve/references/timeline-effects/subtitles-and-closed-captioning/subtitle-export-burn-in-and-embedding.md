# Exporting burning or embedding subtitles during delivery overview

Version: DaVinci Resolve 20.3 Reference Manual. Context: Subtitles and closed captioning.
[Chapter index](INDEX.md) / [Previous section](caption-language-and-country-codes.md)
<a id="source-exporting-burning-or-embedding-subtitles-during-delivery"></a>

### Exporting, Burning, or Embedding Subtitles During Delivery

Once one or more subtitle tracks exist in a program, a cluster of Subtitle Settings appears low in the Video panel of the Render Settings on the Deliver page, and these govern whether and in what manner subtitles or closed captions ship alongside that timeline.

The choices you have for writing out subtitles sit at the foot of the Video panel within the Render Settings

The controls on this panel are as follows:

- Export Subtitle checkbox: Switches subtitle/closed caption output on or off.
- Format pop-up: Offers four ways to write out subtitles/closed captions.

As a separate file: Writes each subtitle track you pick to its own file, in whatever format the Export As pop-up names. A row of checkboxes lets you pick which subtitle tracks get written. Burn into video: Renders every frame of video with the subtitle track now selected baked permanently into the picture. As embedded captions: Writes the currently selected subtitle track as a metadata layer embedded inside media formats that support it. At present, CEA-608 closed captions are supported inside MXF OP1A and QuickTime files. The Codec pop-up that shows up lets you pick the subtitle format.

- Export As: (shown only while Format reads “As a separate file”) Lets you settle on which subtitle/closed captioning format gets written. The choices are IMSC1, DFXP, SRT, and WebVTT.
- Include the following subtitle tracks in the export: (shown only while Format reads “As a separate file”) A set of checkboxes activates the subtitle tracks you wish to write out.
- Codec: (shown only while Format reads “As embedded captions”) Determines how embedded closed captions are formatted; the choices are Text and CEA-608.

NOTE: At this time, neither analog (Line 21) nor digital (CEA-708) closed caption output is supported over Decklink or UltraStudio.
