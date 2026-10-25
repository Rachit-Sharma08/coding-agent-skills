# Effect import format support

Version: DaVinci Resolve 20.3 Reference Manual. Context: Preparing timelines for import and comparison.
[Chapter index](INDEX.md) / [Previous section](project-migration-and-video-track-preparation.md) / [Next section](about-supported-transitions-and-transition-names.md)
<a id="source-aaf-no"></a> <a id="source-about-supported-color-corrections"></a> <a id="source-creating-an-offline-reference-movie"></a> <a id="source-edl-no-no-no-yes-no"></a> <a id="source-effects-supported-with-imported-aaf-xml-and-edl"></a> <a id="source-fcp-7-xml-no"></a> <a id="source-fcp-x-xml-yes"></a> <a id="source-flip-and-flop"></a> <a id="source-flipflop-effects"></a> <a id="source-freeze-frames"></a> <a id="source-importing-effects-when-conforming-edits"></a> <a id="source-linear-speed-effects"></a> <a id="source-linked-clip-audio"></a> <a id="source-mixed-frame-rate-format-selection"></a> <a id="source-mixed-frame-rates"></a> <a id="source-mixed-frame-rates-1"></a> <a id="source-mixed-frame-sizes-and-mixed-codecs"></a> <a id="source-move-clips-to-the-lowest-video-track"></a> <a id="source-nested-sequences"></a> <a id="source-no"></a> <a id="source-no-1"></a> <a id="source-no-10"></a> <a id="source-no-11"></a> <a id="source-no-12"></a> <a id="source-no-13"></a> <a id="source-no-14"></a> <a id="source-no-15"></a> <a id="source-no-16"></a> <a id="source-no-17"></a> <a id="source-no-18"></a> <a id="source-no-2"></a> <a id="source-no-3"></a> <a id="source-no-4"></a> <a id="source-no-5"></a> <a id="source-no-6"></a> <a id="source-no-7"></a> <a id="source-no-8"></a> <a id="source-no-9"></a> <a id="source-opacity-settings"></a> <a id="source-organize-unsupported-media-files"></a> <a id="source-overlay-only"></a> <a id="source-pitch-and-yaw"></a> <a id="source-position-scale-rotation-no"></a> <a id="source-preparing-timelines-for-import-and-comparison"></a> <a id="source-preparing-timelines-for-import-and-comparison-part-1"></a> <a id="source-preparing-to-move-your-project-to-davinci-resolve"></a> <a id="source-still-image-clips"></a> <a id="source-text-generators"></a> <a id="source-variable-speed-effects"></a> <a id="source-yes"></a> <a id="source-yes-1"></a> <a id="source-yes-10"></a> <a id="source-yes-11"></a> <a id="source-yes-12"></a> <a id="source-yes-13"></a> <a id="source-yes-14"></a> <a id="source-yes-15"></a> <a id="source-yes-16"></a> <a id="source-yes-17"></a> <a id="source-yes-18"></a> <a id="source-yes-19"></a> <a id="source-yes-2"></a> <a id="source-yes-20"></a> <a id="source-yes-21"></a> <a id="source-yes-22"></a> <a id="source-yes-23"></a> <a id="source-yes-24"></a> <a id="source-yes-25"></a> <a id="source-yes-26"></a> <a id="source-yes-27"></a> <a id="source-yes-28"></a> <a id="source-yes-29"></a> <a id="source-yes-3"></a> <a id="source-yes-30"></a> <a id="source-yes-31"></a> <a id="source-yes-4"></a> <a id="source-yes-5"></a> <a id="source-yes-6"></a> <a id="source-yes-7"></a> <a id="source-yes-8"></a> <a id="source-yes-9"></a> <a id="source-yes-via-3d-warp"></a> <a id="source-yes-via-3d-warp-1"></a> <a id="source-yes-via-flip-flop-or"></a>

### Importing effects when conforming


A portion of the effects carried inside XML, AAF, and EDL project files can be turned by DaVinci Resolve into their DaVinci Resolve equivalents. The chart below shows which effects come across, and for which project import formats. Effects that are unsupported get neither imported nor shown in DaVinci Resolve. Even so, most unsupported effects are held internally and written back into exported XML or AAF files, so those effects surface again in your NLE the moment the project is reimported.

| Effect | EDL | FCP 7 XML | FCP X XML | AAF |
| --- | --- | --- | --- | --- |
| Color corrections | No | No | Yes | No |
| Composite modes | No | Yes | Yes | Overlay only |
| Multiple tracks | No | Yes | Yes | Yes |
| Video transitions | Yes | Yes | Yes | Yes |
| Audio transitions | No | No | No | Yes |
| Opacity | No | Yes | Yes | 3D Warp or Superimpose |
| Position, scale, rotation | No | Yes | Yes | 3D Warp |
| Flip and flop | No | No | No | Flip, Flop, or Flip-Flop effects |
| Pitch and yaw | No | No | No | 3D Warp |
| Linear speed effects | Yes | Yes | Yes | Yes |
| Variable speed effects | No | Yes | Yes | Yes |
| Still image clips | No | All Resolve-supported formats | All Resolve-supported formats | All Resolve-supported formats |
| Freeze frames | No | No | No | Yes |
| Nested sequences | No | Yes | Yes | No |
| Linked clip audio | Yes | Yes | Yes | Yes |
| Mixed frame rates | No | Yes | Yes | Yes |
| Text generators | No | Yes | Yes | No |

### About Supported Color Corrections

As of this writing, Final Cut Pro X XML projects alone can export color correction data that arrives in DaVinci Resolve as primary grades. For plain reasons, bringing color correction in runs only one direction, and imported color corrections cannot be sent back out to Final Cut Pro. Color adjustments imported from Final Cut Pro X land on the Color page as primary corrections. To pull color correction information from other applications there are further routes, using ColorTrace to import grade data out of CDLs (Color Decision Lists). For deeper coverage, turn to Chapter 186, “Copying and Importing Grades Using ColorTrace,” and its “Copying Grades Using ColorTrace” section.
