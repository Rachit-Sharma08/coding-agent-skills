# Native dcp settings in DaVinci resolve and parameters for adding composition metadata

Version: DaVinci Resolve 20.3 Reference Manual. Context: Delivering dcp and imf.
[Chapter index](INDEX.md) / [Previous section](imf-encoding-decoding-and-composition-metadata.md) / [Next section](dcp-imf-supplemental-packages-and-import.md)
<a id="source-imf-segment-options"></a> <a id="source-native-dcp-settings-in-davinci-resolve"></a> <a id="source-parameters-for-adding-composition-metadata-1"></a> <a id="source-rendering-imf-segments-and-dcp-reels"></a>

### Native DCP settings in DaVinci Resolve

Having picked DCP from the Format dropdown menu, you'll find a Composition Settings group appears — click the disclosure control — bringing these parameters so you can fill in standard DCP composition metadata:

- Composition name: The name of the exported composition. DCPs follow particular naming conventions for the composition name, baking in metadata about the file itself for DCP projectors and playback gear. DaVinci Resolve includes a tool, the Composition Name Generator, to build these names correctly for you; reach it through the “Edit” button beside this field. Just complete the fields and press OK, and DaVinci Resolve renames your composition to match these standards.

For you, the Composition Name Generator hands a standards-compliant name over into the Composition Name field.

- Issuer: The organization providing the composition.
- Use current date: A checkbox letting today's date stand in automatically as the Issue date.
- Issue date: The date the composition is issued.
- Content kind: A dropdown offering a list of valid options for defining the content.
- Content version label: Intended to flag which version of the content is being supplied.
- Annotate xml using composition name: Auto-populates Asset Map, Composition Playlist, and

Packing List using project data. Otherwise, those three fields stay editable by hand.

- Annotate reel index as suffix: Auto-populates Reel Annotation off project data.

Otherwise this one stays editable by hand.

- Annotate media using filename: Fills Main Video Track and Audio Track 1 in for you, pulling

from the project. Otherwise, those three fields stay editable by hand.

### Parameters for adding composition metadata

### Rendering IMF Segments and DCP Reels

Beyond rendering media as one file, DaVinci Resolve can split IMF and DCP projects into separate segments and reels. That helps when you need to chop your timeline down to fit allowed file sizes on legacy file systems, to peel marketing and studio assets away from the final film, or simply to swap out certain stretches of the film without re-encoding the whole thing. To Render an IMF Segment or DCP Reel: 1 Pick IMF or DCP in the format settings on the Render Settings panel's Video tab. 2 Head to the composition settings' “Segment list” or “Reel list” section. 3 Pick from these options: Single segment/reel: Encodes the Timeline as one file (the default). Regular intervals of: Encodes the Timeline as several segments/reels, each one as long as the value you enter in the “mins” field. Align to clips on the first video track: Splits the Timeline into several segments/reels, turning each individual clip sitting on the Timeline's V1 track into a separate file of its own. Keep audio as single segment (IMF only): Tick this checkbox to hold the IMF's audio portion as one file no matter which segment options you chose above. 4 Click the Add to Render Queue button.

### IMF Segment options
