# ACES amf 2 0 and amf files

Version: DaVinci Resolve 20.3 Reference Manual. Context: Data levels color management and ACES.
[Chapter index](INDEX.md) / [Previous section](graphics-white-level-and-display-hdr-on-viewers-if-available.md)
<a id="source-aces-amf-20"></a> <a id="source-amf-delivery-behaviors"></a> <a id="source-exporting-amf-files"></a> <a id="source-the-timeline-color-space-in-aces-workflows-is-fixed"></a> <a id="source-tips-for-rendering-out-of-an-aces-project"></a> <a id="source-working-with-amf-files"></a>

### ACES AMF 2.0

DaVinci Resolve can import and export ACES AMF 2.0 files. An ACES AMF is a sidecar file authored in XML that spells out the clip's input and output transforms. It guarantees that the right input and output transforms get applied all the way through the post production pipeline. You can load these files either at the project level or the clip level. A clip whose “applied” attribute reads true is flagged accordingly and carries no transforms applied. When that attribute reads false instead, DaVinci Resolve applies the transform itself. NOTE: AMF files call for version 1.3 or higher of the ACEScc or ACEScct Color Science.

### Working with AMF Files

Project level AMF: Here every transform ends up applied. (That is, whatever input, look, or output transforms are defined with their “applied” attribute reading false get applied.) Those input and output transforms come in through the project settings “ACES Input Transform” and “ACES Output Transform” menus, and either menu reads “From AMF” whenever it's pulling a transform out of the loaded AMF file. Clip level AMF: You load an AMF from the Color page clip thumbnail context menu, by way of the Clip AMF menu. That same list draws from the ACES Transforms AMF subfolder too. An AMF at the clip level skips the output transform, which is something only project settings can apply. Whatever input or look transforms it holds carry their “applied” attribute reading false. Those look transforms get applied inside a compound node called AMF LMTs. ACES Gamut Compression: Should the AMF name the ACES reference gamut compress algorithm within a look transform, it ticks the “Apply ACES reference gamut compress” checkbox on. You can review which input, gamut compress, look, and output transforms are in effect by clicking the “View Transforms” button down at the foot of the “Color Space & Transforms” area under the Settings > Color Management section. To Import an AMF 1 Drop your AMF files into the ACES Transforms/AMF directory on your machine. You'll locate that folder at: MacOS: the user's `Library/Application Support/Blackmagic Design/DaVinci Resolve/Aces Transforms/AMF` Windows: the user's `AppData\Roaming\Blackmagic Design\DaVinci Resolve\Support\ACES Transforms\AMF` Linux: `opt/resolve/Developer/DaVinciCTL/AcesTransforms/AMF` 2 Within the Project Settings, switch the Color Management > Color Science setting over to ACEScc or ACEScct. 3 Pick an ACES version of 1.3 or higher. 4 Click the ACES AMF drop-down menu and choose the AMF off the list.

### Exporting AMF Files

When exporting an AMF file, you pick from one of three options. Source Master mode:

- Every applied attribute gets switched to false.
- A source master ties to no clips or images at all. Dailies Request mode:
- You get to pick which folder holds the exported AMFs.
- One dailies AMF is generated for each clip and bound to it, and its applied attribute is

set to false. VFX Request mode:

- A VFX AMF holds only the input transform, whose applied attribute is set to false.

### AMF Delivery Behaviors

- To deliver an AMF, tick the export AMF option found in the Deliver page render settings.
- Under Source Master, the images render to ACES AP0 or Linear masters carrying only their

input transforms applied, while every other transform is marked applied false.

- The AMF this produces stays unbound to any clips or images, its purpose being to spell out and pass along a

color pipeline together with its post production look beside ACES AP0 or Linear data.

- Under Dailies Request, the rendered images have all transforms applied, and every transform is

marked applied true.

- The AMF this produces is bound to each clip across the project.
- Under VFX Request, the clips render to ACES AP0 or Linear bearing only the input transform

applied, while all the rest are set to false. To Export an AMF 1 Right-click your timeline within the Media Pool. 2 Pick Timelines > Export > AMF from the contextual menu. 3 Settle on the export type for your AMF — Source Master, Dailies Request, or VFX Request. 4 Type the AMF file's name and where to save it in the file browser. 5 Click the Save button.

### The Timeline Color Space in ACES Workflows is Fixed

While you operate in ACES, changing the Timeline Color Space isn't an option the way it is under Resolve Color Management. The ACES working color space happens to be a log-encoded color space, which nudges you toward a more classic, film-style way of grading.

### Tips for Rendering Out of an ACES Project

As you settle on an output format over in the Deliver page, bear these points in mind:

- For graded media headed to broadcast, set the ACES Output Device Transform to Rec. 709, after which you're free to output to whatever media format suits your workflow.
- For graded media files going to a different ACES-capable facility through the DCDM or ADX ODCs, choose, within the Render Settings, the OpenEXR RGB Half (uncompressed) format, then switch the ACES Output Device Transform over to “No Output Device Transform.”
- For media you're rendering toward long-term archival, choose, within the Render Settings, the OpenEXR RGB Half (uncompressed) format, then switch the ACES Output Device Transform over to “No Output Device Transform.”
