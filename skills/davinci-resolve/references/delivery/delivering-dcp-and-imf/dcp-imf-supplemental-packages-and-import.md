# Creating dcp imf supplemental packages and importing a dcp or imf into a timeline

Version: DaVinci Resolve 20.3 Reference Manual. Context: Delivering dcp and imf.
[Chapter index](INDEX.md) / [Previous section](dcp-settings-and-composition-metadata.md) / [Next section](imf-photon-and-media-pool-validation.md)
<a id="source-creating-dcpimf-supplemental-packages"></a> <a id="source-dolby-vision-metadata"></a> <a id="source-editing-the-resulting-timeline"></a> <a id="source-exporting"></a> <a id="source-importing-a-dcp-or-imf-into-a-timeline"></a> <a id="source-setting-an-export-to-be-a-supplemental-package"></a>

### Creating DCP/IMF Supplemental Packages

After one is created, DaVinci Resolve can reimport a DCP or IMF so you can overwrite parts needing fresh media, then export a “Supplemental Package” — in effect a new version of the program marrying its newly overwritten parts to the old version, letting you deliver only what changed. NOTE: Supplemental packages work solely with the Kakadu encoder and decoder; they don't work with DCP or IMF packages made through EasyDCP. To steer clear of trouble, turn “Use easyDCP decoder” off within the DaVinci Resolve System Preferences, over in its Decode Options panel.

### Importing a DCP or IMF Into a Timeline

1 In the Media page, use the Media Storage browser to locate and pick the DCP or IMF, then look at the Metadata Editor's header to confirm your media can serve as the basis for a supplemental package. The Metadata Viewer lists the IMF profiles that are supported.

The Metadata Editor's header displaying an IMF fit for building a supplemental package 2 Start a new project and bring the DCP/IMF package you mean to alter into the Media Pool. Should a dialog ask whether to switch your timeline frame rate to match the incoming media, click Change so the project lines up with the media. 3 Build a timeline off the composition playlist (XML) held inside the imported DCP or IMF: right-click that imported package within the media pool and pick “Create New Timeline Using Composition Playlist” from the contextual menu.

A right-click on an imported IMF or DCP clip within the Media Pool surfaces, on the contextual menu, a command for making a fresh timeline from the composition playlist 4 The New Timeline dialog carries an “Import Dolby Vision Project Settings” checkbox. Switch it on and clicking Create does this: a) Dolby Vision turns on in the Project Settings' Color Management panel, and the Mastering Display menu is set to match the IMF package's. b) When Resolve Color Management (RCM) is off, the Timeline Color Space is set to match the Dolby Vision metadata. But when RCM is already on, you have to set this yourself by enabling “Use Separate Color Space and Gamma,” then changing the Timeline settings to P3-D65” and “ST.2084” respectively.

5 Building the Timeline brings in Dolby Vision metadata (where it applies). That lets a Tone Mapping preview on the Color page draw on the original metadata.

Dolby Vision metadata will be imported if present when importing an IMF After import finishes, every video and audio clip from the DCP or IMF lands in a new bin named for the package. Its icon marks the resulting timeline as a DCP/IMF timeline.

The imported media and timeline when you import an IMF

### Editing the Resulting Timeline

From here you can edit the program in the Timeline however you need.

- You can overwrite stretches of the Timeline with new clips. Every change folds into the supplemental package on its own.
- You can reach for the Blade tool or the Insert Edit command to carve out stretches of the existing program where Fusion effects, audio grading, or color correction are needed. Whenever you do, you must right-click that stretch and pick “Include in Supplemental Package” so it exports properly.

A right-click on a section of the program followed by picking Include In Supplemental Package With IMF Dolby Vision packages, be sure every change sits on the first video track (V1). NOTE: When RCM is in play, confirm that the inserts' input color space and gamma are right.

### Dolby Vision Metadata

You can reuse the Dolby Vision metadata from the imported DCP/IMF file by picking “Original Metadata” in the Tone Map Using dropdown menu of the Color Page's Dolby Vision palette

Setting a clip to Original Metadata in the Color Page As an alternative, you can bring this metadata in on its own from an existing XML through the “Import Metadata from XML” command in the option menu of the Color page's Dolby Vision palette. On success, “Imported Metadata” switches on.

### Exporting

To export a supplemental package, switch on “Supplemental Package” in the video panel of the Deliver page Render Settings list.

### Setting an export to be a Supplemental Package

The codec type and profile are chosen automatically to match the original DCP/IMF package, and the audio tracks are set to mirror the Timeline tracks. Be sure the remaining audio settings line up with the original version, since they begin at their default values.

Setting the audio settings of a Supplemental Package export
