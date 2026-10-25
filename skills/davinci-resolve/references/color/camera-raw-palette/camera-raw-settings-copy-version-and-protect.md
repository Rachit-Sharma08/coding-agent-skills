# Introduction to the camera raw palette and copying versioning and protecting camera raw settings

Version: DaVinci Resolve 20.3 Reference Manual. Context: Camera raw palette.
[Chapter index](INDEX.md)
<a id="source-camera-raw-clip-decoder-settings-for-braw-media"></a> <a id="source-camera-raw-master-settings-for-braw-media"></a> <a id="source-camera-raw-palette"></a> <a id="source-camera-raw-palette-1"></a> <a id="source-clip-decoder-settings"></a> <a id="source-copying-versioning-and-protecting-camera-raw-settings"></a> <a id="source-introduction-to-the-camera-raw-palette"></a> <a id="source-making-changes-to-clip-camera-raw-settings"></a> <a id="source-resetting-camera-raw-settings"></a> <a id="source-updating-sidecar-settings-for-blackmagic-raw-braw-clips"></a>

### Camera Raw Palette

Through the Camera Raw palette you can apply clip-by-clip tweaks to the settings that govern how a raw clip gets debayered into a picture you can then grade inside DaVinci Resolve.

### Introduction to the Camera Raw Palette

Whenever a timeline contains clips tied to camera raw source media shot on cameras from Blackmagic Design, RED, ARRI, Sony, and Vision Research, every clip stored in a raw format starts out debayered according to whatever is configured in the Camera Raw panel of the Project Settings. That said, should certain clips need different raw treatment — say you want to shift the ISO so more detail emerges from the highlights or the shadows — the controls inside the Camera Raw palette let you tune those parameters one clip at a time.

The Camera Raw palette showing the available parameters for Blackmagic RAW media. Whichever clip is selected at the moment, the palette switches itself automatically to the matching mode (visible in the Mode drop-down menu). Should the active clip not be a raw format, every parameter inside the Camera Raw palette becomes disabled. General usage of the palette is what this section addresses. To dig deeper into the meaning of each individual raw parameter, refer to Chapter 7, “Camera Raw Settings.”

### Copying, Versioning, and Protecting Camera Raw Settings

Normally a clip carries its camera raw settings along with the grade, or tucked inside any stills you grab from that clip, as you employ the assorted grade management methods discussed in a later Chapter, see Chapter 142, “Grade Management.” Creating a new version copies the present Camera Raw settings over to it, yet whatever edits you then make belong only to that version, which means each version is free to hold its own Camera Raw adjustments. You might, for instance, weigh two distinct camera raw treatments against each other on one and the same clip.

### Camera Raw master settings for BRAW media

When you’re copying and rippling grades across several clips, the “Copy Grade: Preserve Camera Raw Settings” entry in the Gallery’s contextual menu also lets you shield every clip’s camera raw settings from being clobbered. The Copy Grade settings are described further in Chapter 142, “Grade Management.”

### Making Changes to Clip Camera Raw Settings

Should you wish to tweak one specific clip’s camera raw settings on their own, pick “Clip” from the Decode Using drop-down menu within the Camera Raw palette. Doing so unlocks all of the palette’s parameters for editing, and the edits you apply take precedence over the settings configured project-wide. Edits to the palette’s parameters can likewise be rippled to several clips together. To ripple camera raw adjustments across multiple clips: 1 To begin, choose a span of clips within the Color page timeline. 2 Bring up the Camera Raw palette, then apply whatever tuning the current clip requires. Each parameter you touch has its label turn amber, so you can see at a glance which ones changed and which stayed put. 3 To ripple your changes, do one of the following:

- Press the Use Changes button so that only the modified parameters (the amber ones) ripple out to the rest of the clips you’ve highlighted in the Timeline. The parameters you left untouched (in gray) keep their per-clip differences intact.
- Press the Use Settings button so every single parameter from the current clip ripples to the rest of your selected clips, replacing all the camera raw settings in one shot.

The Use Changes and Use Settings buttons in the Camera Raw palette

### Clip Decoder Settings

You’ll find a great deal more about the various format-specific Master settings, plus the sometimes format-specific Clip Decoder settings, over in Chapter 7, “Camera Raw Settings.” Setting aside the RED Clip Decoder settings shown for R3D clips, though, the bulk of the remaining formats rely on a common group of DaVinci Resolve-specific controls offering wide-latitude reach into the raw image data so you can perform assorted sorts of adjustments.

### Camera Raw Clip Decoder settings for BRAW media

Although each raw format brings its own controls, the shared standard ones are:

- Color Temp: Made to shift how “warm” the picture reads. Tuned in degrees Kelvin. Dropping the value compensates for “warmer” light, whereas raising it compensates for “cool” light. +6500 is unity. The range is +2000 to +50,000.
- Tint: Corrects the color balance on pictures carrying a green or magenta tinge — say, the cast from a fluorescent tube or a sodium vapor lamp. Unity sits at 0. Its span runs from –150 up to +150.
- Exposure: Pushes image brightness up or down, measured in increments that track ƒ-stops. Even if the exposure shift you dial in pushes image data past the top white level, there’s nothing to fear; every bit of image data stays intact and can be recovered by later adjustments. 0 is unity. The range is –5 to +5.
- Sharpness: A sharpening filter tied to the debayer stage that lends the picture a look of heightened detail. 20 is unity. The range is 0 to 100.
- Highlights: Pulling this parameter down makes it simple to reclaim clipped highlight detail in high-dynamic-range media, blending the recovered highlights smoothly into the untouched midtones for a natural-looking outcome. 0 is unity. The range is –100 through +100.
- Shadows: Gives you selective control to brighten or deepen shadow detail. Pushing this value up recovers shadow detail captured below 0 percent while the midtones stay put. 0 is unity. The range is –100 through +100.
- Color Boost: A non-uniform saturation control that works on weakly saturated areas more strongly than heavily saturated ones. Some people call this a vibrance operation. 0 is unity, presenting the source color values. Pushing color boost up from 0-100 intensifies color, though weakly saturated regions of the picture climb more sharply. Pulling Color Boost down from 0 to -100 reduces color, though weakly saturated regions of the picture drop more sharply. 0 is unity, presenting saturation unchanged. The range is –100 through +100.
- Saturation: A uniform saturation control that lifts (past 50) or drops (under 50) the color intensity across every color value in the picture. 50 is unity, presenting saturation unchanged. The range is -100 (completely desaturated) through +100 (saturation is doubled).
- Midtone Detail: Pushing this parameter up boosts contrast across image regions rich in edge detail, heightening the sense of sharpness, a quality also called definition. Pulling it into negative territory smooths out regions that hold little detail while leaving high-detail zones untouched. 0 is unity. The range is –100 through +100.
- Lift: Sets the media’s black point, lifting or dropping it while every midtone value between it and the white point gets rescaled. No matter how you move this control, every bit of image data stays intact and can be recovered by later adjustments. The range is –100 to +100.
- Gain: Sets the media’s white point, lifting or dropping it while every midtone value between it and the black point gets rescaled. No matter how you move this control, every bit of image data stays intact and can be recovered by later adjustments. 0 is unity. The range is –100 to +100.
- Contrast: Pushing contrast up pulls shadows down and lifts highlights, all while the midtones at 50 percent stay unaffected. No matter how you move this control, every bit of image data stays intact and can be recovered by later adjustments. 0 is unity. The range is –100 to +100.

### Resetting Camera Raw Settings

Having altered the Camera Raw palette’s parameters, should you then conclude you need to undo them, the Options menu offers two choices.

- Reset: Returns each of the Camera Raw palette’s parameters to the values they ship with by default.
- Revert: Working much like the “Original Memory” command, Revert restores every camera raw parameter

to whatever condition it held the moment you first picked the clip you’re working on.

### Updating Sidecar Settings for Blackmagic RAW (BRAW) Clips

A Blackmagic RAW clip can hold both look metadata baked into the .braw media clip itself and a separate external look in .sidecar files. As a rule those two travel together as a pair across any BRAW media workflow, and any time a .sidecar file accompanies the clip, its settings take priority over the metadata embedded in the .braw clip proper. Because the .sidecar metadata sits in human-readable JSON-formatted text, editing it is straightforward and it suits a broad spectrum of onset-through-post workflows.

The .braw and .sidecar files as seen in the file system Should you wish, the raw look metadata on a .braw clip can be edited and the .sidecar metadata refreshed straight from the Color page of DaVinci Resolve, so that the on-disk media carries those edits into any other BRAW compatible application.

To update the .sidecar raw look metadata: 1 Go to the Color page, pick out a .braw clip from the Thumbnail timeline, and bring up the Camera Raw palette. 2 Switch Decode Using over to Clip so the palette controls become active. 3 Dial in whichever tweaks you have in mind by way of the controls in the Camera Raw palette. 4 Once finished, click Update Sidecar to commit. The Update Sidecar button shown in the Camera Raw palette while a .braw clip is loaded
