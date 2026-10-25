# Native imf encoding and decoding and parameters for adding composition metadata

Version: DaVinci Resolve 20.3 Reference Manual. Context: Delivering dcp and imf.
[Chapter index](INDEX.md) / [Next section](dcp-settings-and-composition-metadata.md)
<a id="source-delivering-dcp-and-imf"></a> <a id="source-delivering-dcp-and-imf-part-1"></a> <a id="source-native-dcp-encoding-parameters"></a> <a id="source-native-imf-encoding-and-decoding-studio-version-only"></a> <a id="source-native-unencrypted-dcp-encoding-and-decoding-studio-version-only"></a> <a id="source-parameters-for-adding-composition-metadata"></a>

### Delivering DCP and IMF

When a project calls for Digital Cinema Package (DCP) or Interoperable Master Format (IMF) mastering bound for digital cinema or broadcast distribution, DaVinci Resolve handles native DCP and IMF encoding and decoding so you can build and play back unencrypted DCP and IMF deliverables, and it can also tie into Fraunhofer's easyDCP application to master fully encrypted DCP files, replay them for testing, and produce Key Delivery Messages (KDMs) for theatrical distribution — every step right inside DaVinci Resolve. In other words, you can encode a DCP or IMF master directly off your program's source media, the whole job staying inside DaVinci Resolve's 32-bit floating point image processing pipeline, for the best quality achievable.

### Native IMF Encoding and Decoding (Studio Version Only)

Over in the Render Settings, the Video panel's Format dropdown now carries a native IMF option that exports to the SMPTE ST.2067 Interoperable Master Format (IMF) for tapeless deliverables headed to networks and distributors. Outputting to IMF takes no extra licenses or plugins. The IMF format handles several video tracks, several audio tracks, and several subtitle and closed caption tracks, all designed to carry multiple output formats and languages within one deliverable. Beginning with DaVinci Resolve 16, IMF export can also output IMF packages built on ST.2098 and Dolby immersive audio drawn from selected Main busses. The whole thing works by wrapping a timeline's various video and audio tracks (media essences) plus subtitle tracks (data essences) into a “composition” inside the Material eXchange Format (MXF). On top of that, a dropdown menu beside this preset supplies Generic, 20th Century Fox, and Netflix versions of it.

Within the Render Settings, the IMF Generic preset offers choices for various output resolutions Pick IMF from the Format dropdown and the Codec drop-down menu offers Kakadu or EasyDCP encoding, where Kakadu is the one bundled with DaVinci Resolve Studio. A Type dropdown lets you settle on the kind of JPEG2000 output you're after, among them RGB, YUV, Dolby Vision, and HDR Vivid. Further parameters take in:

- Package Type: Its default is App2 Extended (App2e), used to encode JPEG 2000 as high as 4K.
- Bit Depth: The bit depth of the encoded IMF video.
- Encoding Profile: A dropdown letting you pick among Auto, IMF, and Broadcast.
- Encoding Level: Offers varying choices depending on the Encoding Profile selection.
- Maximum bit rate: Lets you set how much the result is compressed.
- Lossless Compression: Lets you opt to encode with lossless compression.
- Slope-Rate Control: A checkbox for specifying lossless compression.
- QStep: (DCP, IMF) Lets you go with automatic or hand-set DCP quantization levels

at which the video signal compresses when the Kakadu JPEG 2000 encoder is in use.

Render settings in the Export Video section for the IMF format A distinct cluster of parameters called Composition Settings, sitting below the Advanced Settings, lets you attach metadata to your IMF package, among them:

- Composition name: The name of the exported composition.
- Issuer: The organization providing the composition.
- Use current date: A checkbox letting today's date stand in automatically as the Issue date.
- Issue date: The date the composition is issued.
- Content kind: A dropdown offering a list of valid options for defining the content.
- Content version label: Intended to flag which version of the content is being supplied.
- Annotate xml using composition name: Auto-populates Asset Map, Composition Playlist, and

Packing List from project data. If left off, you can edit those three fields by hand.

- Annotate media using filename: Fills Main Video Track and Audio Track 1 in automatically, drawing

on project data. If left off, you can edit those three fields by hand.

### Parameters for adding composition metadata

### Native Unencrypted DCP Encoding and Decoding (Studio Version Only)

DaVinci Resolve carries native DCP encoding and decoding support of its own, though only for unencrypted DCP files. So you can output and bring in (for test playback) unencrypted DCP files without having to buy an EasyDCP license. Should you hold a license, a setting in the System Preferences' Configuration panel lets you decide whether to lean on EasyDCP (for producing encrypted DCP output) or the native DaVinci Resolve encoding.

### Native DCP Encoding Parameters

Pick DCP from the Format dropdown menu and these extra parameters come into view:

- HDR: (DCP, IMF) Marks the package as carrying HDR content.
- Use interop packaging: (DCP only, located under Type parameter) Lets you build an Interop

DCP package, founded on an older DCP delivery standard that isn't forward compatible with SMPTE DCP packages.

- Maximum bit rate: (DCP, IMF) Lets you set how much the result is compressed.
- Lossless Compression: (IMF) Lets you opt to encode with lossless compression.
- Slope-Rate Control: (DCP, IMF) A checkbox for specifying lossless compression.
- Quality: (DCP, IMF) Lets you go with automatic or hand-set DCP quantization levels at which the video signal compresses when the Kakadu JPEG 2000 encoder is in use.
