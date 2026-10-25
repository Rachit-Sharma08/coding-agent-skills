# Camera raw formats and source media color space metadata

Version: DaVinci Resolve 20.3 Reference Manual. Context: Data levels color management and ACES.
[Chapter index](INDEX.md) / [Previous section](identifying-the-input-color-space-of-different-clips.md) / [Next section](sdr-hdr-conversion-and-advanced-rcm.md)
<a id="source-automatic-color-management"></a> <a id="source-output-color-space"></a> <a id="source-resolve-color-management-presets"></a> <a id="source-simple-rcm-setup"></a> <a id="source-using-camera-raw-formats"></a> <a id="source-using-source-media-color-space-metadata"></a>

### Using Camera Raw Formats

While you run RCM on a project built around Camera Raw formats, color science data from each camera maker debayers every camera raw file to particular color primaries with linear gamma, so that all of the source’s image data survives and reaches DaVinci Resolve’s color managed image processing pipeline. Consequently, the Camera Raw project settings and the Camera Raw palette of the Color page are switched off, since RCM has taken over debayering for all camera raw clips, and the whole of the raw file’s image data is on hand regardless of which Timeline Color Space you decide to work in.

### Using Source Media Color Space Metadata

Once switched on, RCM identifies on its own the color space details of imported media that was either transcoded or recorded straight to supported non-raw media formats. It does so by reading several sources: the NCLC metadata inside QuickTime-wrapped files, the color space metadata inside .mxf-wrapped files, plus the XML sidecar files tracking color management across ACES workflows. The process happens automatically; no visible controls steer it beyond the individual Input Color Space and Input Gamma settings tied to each clip in the Media Pool. Color Space Metadata in QuickTime For correct color management, DaVinci Resolve is able to read the NCLC metadata held inside media files that a QuickTime container has wrapped. That metadata is made of three values written as (for instance) 1-1-1. Taken from left to right, the trio of digits identifies, in turn, the Color Primary (or color space), then the Transfer Function (or gamma), and lastly the Color Matrix the media file relies on. The SMPTE Registered Disclosure Document RDD 36:2015 standardizes these values. For reference, the various codes appear in the table below. In the earlier instance, a code of 1-1-1 marks a standard dynamic range clip relying on the BT.709 primaries, transfer function, and color matrix.

Color Primary 0 Reserved 1 ITU-R BT.709 2 Unspecified 3 Reserved 4 ITU-R BT.470M 5 ITU-R BT.470BG 6 SMPTE 170M 7 SMPTE 240M 8 FILM 9 ITU-R BT.2020 10 SMPTE ST 428-1

Transfer Function 0 Reserved 1 ITU-R BT.709 2 Unspecified 3 Reserved 4 Gamma 2.2 curve 5 Gamma 2.8 curve 6 SMPTE 170M 7 SMPTE 240M 8 Linear 9 Log 10 Log Sqrt

Color Matrix 0 GBR 1 BT709 2 Unspecified 3 Reserved 4 FCC 5 BT470BG 6 SMPTE 170M 7 SMPTE 240M 8 YCOCG 9 BT2020 Nonconstant Luminance 10 BT2020 Constant Luminance

Color Primary 11 DCI P3 12 P3 D65 –– –– –– –– –– ––

Transfer Function 11 IEC 61966-2-4 12 ITU-R BT.1361 Extended Colour Gamut 13 IEC 61966-2-1 14 ITU-R BT.2020 10 bit 15 ITU-R BT.2020 12 bit 16 SMPTE ST 2084 (PQ) 17 SMPTE ST 428-1 18 ARIB STD-B67 (HLG)

Color Matrix –– –– –– –– –– –– –– ––

The Default Input Color Space The default Input Color Space is available to set only when the “Resolve color management preset” drop‑down menu sits on Custom. Otherwise it falls back to “Rec. 709 Gamma 2.4” across all presets. Beyond that, this setting is the default color space that every clip in the Media Pool not otherwise identified will adopt. Manually Tagging Clip Color Space Where needed, you can identify by hand the color space of one or more chosen clips in the Media Pool, right-clicking them and picking the Input Color Space (and, if you like, the Input Gamma) from the contextual menu.

### Simple RCM Setup

The moment you first pick DaVinci YRGB Color Managed out of the Color science drop-down menu on the Color Management panel within the Project Settings, two plain menus appear for shaping how Resolve Color Management should operate for you: the “Resolve color management preset,” along with the “Output Color Space.”

### Automatic Color Management

Your first decision under RCM is whether to lean on Automatic Color Management or on the Manual Presets. Ticking the Automatic Color Management box, DaVinci Resolve hands you a pared-down set of options aimed at the most common use cases. For the Color Processing Mode, you pick SDR or HDR, and going by the file types and codecs present in the Media Pool, DaVinci Resolve picks the fitting input color space on its own. After that, choose from a list of common Output color spaces for delivery. Should you want hands-on control of these parameters, clear the Automatic Color Management box and pick from the Color Management Presets below.

Automatic Color Management presets for fast, simple color management set up

### Resolve Color Management Presets

The Resolve Color Management preset menu lets you decide how RCM is put to work grading your program. Every one of these presets fully arranges your project’s color management, and whichever setting you pick has a direct bearing on how you will grade. For that reason, once you settle on a way of working and grade every clip in your program, those grades count on the preset you used staying selected so that they appear as intended.

Resolve Color Management presets for manual color management set up A sound way to think about which preset to use is to reach for an SDR or HDR preset matching the primary deliverable you intend to output. Each of the SDR and HDR presets comes in several variations to pick among. Although these presets line up with how you plan to output your program, they do not box you in, because you can always switch the Output Color Space (covered below). That makes it possible to export several versions of your program, each meant for a different venue, no matter which color management preset is in play. Each time you pick a preset, a short description spells out the workflow that preset is built to support. Below is a list of the presets on offer, with somewhat fuller explanations.

- SDR Rec.709: (default) Builds a Rec. 709 SDR grading environment. On output, what you create may be converted to HDR where called for, yet it stays bounded to a Rec. 709 gamut, with any out-of-bounds colors clipped. The name leaves out Gamma 2.4 because scene-versus-display OOTF is handled for you. A fit for everyday streaming and broadcast.
- SDR P3 Broadcast: Builds a P3-D65 SDR grading environment. On output, what you create may be mapped to HDR where called for, yet it stays bounded to a P3-D65 gamut, with any out-of-bounds colors clipped. The name leaves out Gamma 2.4 because scene-versus-display OOTF is handled for you. A fit for broader gamut streaming and broadcast held at SDR levels.
- SDR P3 Cinema: Builds a P3-D60 SDR grading environment. On output, what you create may be mapped to HDR where called for, yet it stays bounded to a P3-D60 gamut, with any out-of-bounds colors clipped. A fit for everyday Cinema projection.
- SDR Rec.2020: Builds a Rec. 2020 SDR grading environment. On output, what you create may be mapped to HDR where called for. Well suited to wide gamut streaming and broadcast.
- DaVinci Wide Gamut: Builds an extra wide gamut grading environment that serves equally for grading SDR or HDR. It can export at maximum image fidelity, holding onto highlight details as far as 10,000 nits. This is a log-encoded grading space for colorists who prefer that approach. A fit for turning out mezzanine intermediates or final deliverables, or for grading HDR at high nit levels.
- HDR P3 Broadcast: Builds a P3-D65 HDR grading environment. The output gamut stays bounded to P3‑D65, with any out-of-bounds colors clipped. A fit for grading wide gamut SDR or HDR as far as 1000 nits.
- HDR Rec.2020: Builds a Rec. 2020 HDR grading environment. A fit for wide gamut SDR or HDR deliverables as far as 1000 nits.
- Custom: When none of the presets on offer matches the way you must work, pick Custom, which lays bare the entire set of RCM settings for you to arrange however suits you.

IMPORTANT: With every preset, bringing in media whose gamut matches or is smaller maps the image data into the preset’s larger color space and leaves it untransformed. Bringing in media whose gamut is wider than the preset’s color space remaps the image data so it fits the smaller color space, while holding onto as much image detail as it can.

### Output Color Space

On most DaVinci Resolve installations and projects, you will set your Output Color Space to suit the needs of your program, in keeping with what your display can do (or with the capabilities your display is configured to use for the project in hand). You will typically pair that with a Resolve Color Management preset matching those same capabilities. Even so, RCM gives you the freedom to grade in one color space and then output to others when the situation calls for it. Take this case: you might easily grade an SDR Rec. 709 cut of a program meant for streaming or for broadcast, after which you flip the Output Color Space over to SDR P3 Cinema to put out an extra deliverable for theatrical exhibition. To make that possible, you can set the Output Color Space to any value, separate from whichever Resolve Color Management preset you have picked, and DaVinci Resolve converts on its own from your Color Management Preset to the Output Color Space you chose. Doing so, the rules below govern the image transform that results. When going SDR to HDR:

- Within your program, 0-50 nits (18% mid-gray) lands at 0-50 nits on output (no change).
- Within your program, the 51-90 nits band gets shifted to 51 to 100 nits (slightly

expanded).

- Within your program, the 91-100 nits band gets shifted to 101 to 1000 nits

(greatly expanded).

Original SDR grade seen within an HDR scale,
