# New subclip dialog and removing or changing subclip limits

Version: DaVinci Resolve 20.3 Reference Manual. Context: Modifying clips and clip attributes.
[Chapter index](INDEX.md) / [Previous section](clip-audio-attributes-and-track-addition.md)
<a id="source-camera-raw-decoding"></a> <a id="source-modifying-clips-and-clip-attributes-part-2"></a> <a id="source-organizing-stereo-3d-media"></a> <a id="source-removing-or-changing-subclip-limits"></a> <a id="source-the-edit-subclip-dialog"></a> <a id="source-the-new-subclip-dialog"></a>

### The New SubClip dialog

Built, a subclip shows up and behaves just like any other clip throughout DaVinci Resolve. Subclips can likewise be created over on the Media page as you carry out other organizational work there.

### Removing or Changing Subclip Limits

Once it exists, a right-click on any subclip — whether in the Media Pool or on a timeline — and a choice of Edit Subclip opens a dialog where you can tick a checkbox to draw on the subclip’s full extents, or revise its start or end timecode through the timecode fields, then click Update to apply the change.

### The Edit Subclip dialog

### Organizing Stereo 3D Media

Among the earliest jobs when handling stereo media in DaVinci Resolve is syncing each stereo pair of clips so the two behave as one. That goes smoothly provided you are deliberate about how your media is laid out in the Media Pool. Every set of right- and left-eye media ought always to be filed into separate left-eye bins and righteye bins, which eases the later syncing of these clips through the Stereo 3D Sync command in the Media Pool contextual menu. For fuller guidance on readying media destined for stereo pipelines, “refer to Chapter 15, “Stereoscopic Workflows.” Within the section titled “Stereoscopic Workflows”

### Camera Raw Decoding

Camera raw media formats earn the name because they grab raw color space data straight off the sensor of whichever digital cinema camera shot the footage. Such raw image data is not legible to people; it has to be debayered or demosaiced to turn the original raw data into image data ready to pass along to DaVinci Resolve’s image processing pipeline. You have four levers for governing how camera raw media gets debayered into a usable, “normalized” image for adjustment or output:

- Inside the Project Settings, the Camera Raw panel holds parameter groups, one set per camera raw media format that DaVinci Resolve handles. Working through those parameters in the Camera Raw panel lets you supersede the original camera metadata laid down while recording, and tweak every piece of camera raw media across the whole project at once.
- Over in the Inspector, the Image Panel likewise carries the controls for each raw media format DaVinci Resolve recognizes. That lets you target all clips, a handful, or just one for raw debayering.
- On the Color page, the Camera Raw palette gives you a way to dial Camera Raw parameters one clip at a time for the individual clips sitting in the Timeline.
- Should a project lean on Resolve Color Management (RCM) while also relying on Camera Raw formats, the color science supplied by each camera maker drives the debayer or demosaic of every camera raw file toward defined color primaries under linear gamma, keeping all of the source's image data intact and ready for DaVinci Resolve’s color managed image processing pipeline. Because of that, the Camera Raw project settings together with the Camera Raw palette on the Color page go inactive, since RCM now steers the debayering for all camera raw clips, leaving the full image data of the raw file open for conversion into whichever Timeline Color Space you settle on as you grade.

To read up on each of the Camera Raw formats you can tune within DaVinci Resolve, turn to Chapter 7, “Camera Raw Settings.”
