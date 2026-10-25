# Supported media types in aaf workflows and transcoding to dnxhd or dnxhr always works

Version: DaVinci Resolve 20.3 Reference Manual. Context: Conforming aaf files.
[Chapter index](INDEX.md) / [Next section](simple-aaf-import-and-supported-aaf-timeline-features.md)
<a id="source-codec"></a> <a id="source-conforming-aaf-files"></a> <a id="source-conforming-aaf-files-part-1"></a> <a id="source-fast-imported-media"></a> <a id="source-linking-to-media-using-ama-and-consolidating"></a> <a id="source-logged-errors-when-importing-aaf"></a> <a id="source-supported-media-types-in-aaf-workflows"></a> <a id="source-transcoding-to-dnxhd-or-dnxhr-always-works"></a>

### Conforming AAF Files

A project exchange format, AAF (Advanced Authoring Format) was first created by the Advanced Media Workflow Association (AMWA). Widely used video applications capable of writing out project data in the AAF format take in Avid Media Composer, Avid Symphony, Autodesk Smoke plus Flame Premium, along with Adobe Premiere Pro. Detailed guidance on the suggested workflows for carrying projects out of Media Composer (or Symphony) into DaVinci Resolve for grading fills this chapter, whether as a one-way trip or as a round-trip workflow where you head back to Avid Media Composer to finish. Because round-trip workflows in Media Composer involve so many variables, the chapter treats the topic thoroughly. Toward the end, the chapter also explains bringing in audio projects out of Pro Tools that were exported to AAF.

### Supported Media Types in AAF Workflows

Several ways of ingesting and handling compatible media formats are offered by Media Composer. In the end, which formats will serve for a one-way or round trip from Media Composer to DaVinci Resolve hinges on whether they work with DaVinci Resolve. Keep one further point in mind while you handle media inside Media Composer: not every format works with every media management operation. Because format compatibility and operational compatibility combine this way, you have to shape your workflow carefully around the particular media files you intend to use.

### Transcoding to DNxHD or DNxHR Always Works

Because DNxHD and DNxHR were built to serve as the core codecs of Media Composer, any workflow in which you transcode other media formats into MXF-wrapped DNxHD/DNxHR ahead of editing is guaranteed to function, and these are the most straightforward when round tripping across Media Composer and DaVinci Resolve. Both MXF-wrapped and QuickTime-wrapped DNxHD/DNxHR media are supported by DaVinci Resolve.

### Linking to Media Using AMA and Consolidating

A way to link clips straight to media files within Media Composer, without having to either transcode them into DNxHD/DNxHR MXF files or copy them across to an Avid MediaFiles directory, is Avid Media Access (AMA). Handy as it is, any workflow that involves media linked through AMA calls for somewhat more planning. Media Composer cannot consolidate every AMA-compatible media format, which caps your ability to assemble a smaller, more portable batch of media for moving into DaVinci Resolve. Whether a given AMA-linked clip is consolidatable comes down to its media format; the only formats Media Composer can consolidate are ones it is able to write. As an example, because Media Composer is unable to write R3D media, R3D media cannot be consolidated. On top of that, not every AMA-compatible media format works with DaVinci Resolve. The mere fact that you can edit a media format on a Media Composer timeline is no assurance that it is usable in DaVinci Resolve. Which media formats are AMA-linkable in Media Composer, which ones can be consolidated, and which ones work for use in DaVinci Resolve are all set out in the table that follows. When you are prepping a sequence drawing on an assortment of media formats, where some can be consolidated and some cannot, transcode every clip that won't consolidate into an Avid native codec before you start consolidating media and writing out an AAF for DaVinci Resolve.

### Fast Imported Media

A further complication is that Media Composer offers a media ingest approach termed “Fast Import,” in which imported media gets copied swiftly to the Avid MediaFiles directory by dropping the original image data, using its original codec, inside an MXF wrapper. Although this is a remarkably quick and efficient route for pulling media into Media Composer projects, the files it leaves behind usually won't work with DaVinci Resolve. That said, remember that whatever media format can be Fast Imported is also consolidatable. Should you intend to round trip a sequence built on Fast Imported media, the advice is to either transcode the Fast Imported clips into DNxHD ahead of AAF export, or instead conform your exported AAF project against the camera original media inside DaVinci Resolve. TIP: Any time your project mixes in media formats that don't work with DaVinci Resolve, the “Transcode Video To” checkbox, located among the options of the Export As dialog, is available while you export an AAF project. With that option you can transcode every piece of media that isn't a compatible format into one that is. A few nonstandard frame sizes won't transcode within Avid and instead come back with an unsupported resolution error.

### Codec

Compatible AMA-linked formats, with each codec rated for the three columns below:

| Codec                  | Can be Natively AMA-Linked | Can be Consolidated | DaVinci Resolve Compatible |
| ---------------------- | -------------------------- | ------------------- | -------------------------- |
| ARRI ALEXA Raw         | Non-native support         | No                  | Yes                        |
| AVCHD                  | Yes                        | No                  | Yes                        |
| AVC-Intra and Long GOP | Yes                        | Yes                 | Yes                        |
| Blackmagic RAW         | Non-native support         | No                  | Yes                        |
| Canon XF               | Yes                        | Yes                 | Yes                        |
| Cine (Phantom)         | Yes                        | Yes                 | Yes                        |
| CinemaDNG              | No                         | No                  | Yes                        |
| DVC PRO P2             | Yes                        | Yes                 | No                         |
| QuickTime (ProRes)     | Yes                        | Yes                 | Yes                        |
| R3D (RED)              | Non-native support         | No                  | Yes                        |
| Sony F65 Raw           | Yes                        | No                  | Yes                        |
| Sony HDCAM SR (SStP)   | Non-native support         | No                  | Yes                        |
| Sony XAVC              | Yes                        | Yes                 | Yes                        |
| Sony XDCAM             | Yes                        | Yes                 | Yes                        |

### Logged Errors When Importing AAF

When the “Import log messages as markers” checkbox is switched on within the Load AAF dialog, particular error messages that warn you about problems with the AAF import you're attempting get attached as markers, complete with notes, on the Timeline. Through a pop-up tucked inside the text of that checkbox, you can pick the color of the markers that hold this information. Markers will be produced by the following messages:

- The ‘XXXX’ transition type isn't handled by this release, so a Cross Dissolve gets dropped in instead.
- This release doesn't handle the ‘XXXX’ effect type, so plain clips come in instead.
- This release doesn't handle the ‘XXXX’ SMPTE Wipe Transition type, so a Cross Dissolve gets

dropped in.

- The ‘XXXX’ interpolation type isn't handled by this release, so Linear interpolation gets used.
- Linking the ‘XXXX’ clip failed, since its timecode extents line up with no clip inside

the Media Pool.

- A mismatch sits between the stated target timecodes ‘XXXX’ and the located file timecodes ‘YYYY.’
- The stated target timecodes ‘XXXX’ and the located file timecodes ‘YYYY’ share no overlap.
- The ‘XXXX’ clip on track ‘XXX’, timecode ‘UNKNOWN’, carrying reel name ‘XXXX’ plus filename ‘XXXX.’
- The ‘XXXX’ clip on track ‘XXX’, timecode ‘UNKNOWN’, carrying reel name ‘XXXX’ plus filename ‘XXXX.’
- No file turned up across the search directories.

At the moment this is being written, the feature is offered solely while you import AAF files.
