# Delivering dolby vision and rendering a dolby vision master

Version: DaVinci Resolve 20.3 Reference Manual. Context: HDR setup and grading.
[Chapter index](INDEX.md) / [Previous section](davinci-resolve-grading-workflow-for-dolby-vision.md) / [Next section](hdr10-monitoring-and-grading.md)
<a id="source-delivering-dolby-vision"></a> <a id="source-rendering-a-dolby-vision-imf"></a> <a id="source-rendering-a-dolby-vision-master"></a> <a id="source-smpte-st2084-and-hdr10"></a>

### Delivering Dolby Vision

After the HDR grade is done and the SDR tone mapping trimmed, your program has to be output properly over on the Deliver page.

### Rendering a Dolby Vision Master

For a Dolby Vision master once grading wraps, confirm that the Output Color Space in the Project Settings’ Color Management panel sits on the right HDR ST.2084 setting for whatever peak output you intend (anything beyond it gets clipped). Next, configure your render around one of these Format/Codec pairings:

- TIFF, RGB 16-bit
- EXR, RBG-half (no compression)

Rendering for tapeless delivery writes all Dolby Vision metadata into a Dolby Vision XML that ships alongside either the Tiffs or the EXR renders. To produce a Dolby Vision XML file, highlight your timeline in the media pool and go to File > Export >Timeline. Browse to your save location, choose Dolby Vision v2.9 (or v4.0) MXF files in the file type selector, and click save. Those two file sets then go off to a facility equipped to build the Dolby Vision deliverable file.

### Rendering a Dolby Vision IMF

Delivery can go straight to an IMF whose package carries an MXF with Dolby Vision metadata baked in. For a Dolby Vision IMF, apply these Video settings on the Deliver page:

- Format: IMF
- Codec: Kakadu JPEG 2000
- Type: Dolby Vision (HD, 2K, UHD, or 4K), chosen to match your deliverable resolution.

Set whatever remaining IMF settings your project demands.

Deliver-page Video settings for building a Dolby Vision IMF Rendering a Dolby Vision H.265 file You can ship straight to a Dolby Vision-compatible H.265 file, letting video play back in a way that flips your television or computer screen into Dolby Vision mode. For a Dolby Vision H.265 file, apply these Video settings on the Deliver page:

- Format: MP4 or QuickTime
- Codec: H.265
- Dolby Vision Profile: Pick the Dolby Vision profile you intend to use, or None to handle the

Tone Mapping manually.

Setup and Workflows | HDR Viewers HDR Setup and Grading

- Tone Mapping: Set None for no tone mapping, or Dolby Vision to reveal a roster of common deliverables you can tone map toward.

Set whatever remaining H.265 settings your project demands.

Where the Deliver page’s H.265 Video section holds the Dolby Vision Profile and Tone Mapping settings Rendering an Ordinary SDR Media File or Other Specific HDR Trim Pass To put out the SDR trim pass, pick Dolby Vision from the Tone Mapping drop-down within the Advanced Settings of the Deliver page’s Render Settings list, then select the 100-nit, BT.709, BT.1886, Full entry below it. With that on, the SDR version of your program can go out in any format you please. You may likewise export trims at other HDR nit levels for particular displays — 600, 1000 or 2000 nits — within either the BT.2020 or P3 gamuts.

Where the Render Settings list’s Advanced Settings carry the Tone Mapping control

### SMPTE ST.2084 and HDR10

Plenty of display makers with no appetite for licensing Dolby Vision into their sets take the easier road instead, building their displays to comply with SMPTE ST.2084. That route needs only one stream for distribution, carries no licensing fees, demands no special mastering hardware beyond an HDR mastering display, and involves no special metadata to author or wrangle. Tellingly, SMPTE ST.2084 elevates the “PQ” EOTF — first devised by Dolby and used by Dolby Vision — into a general standard that supports encoding HDR at peak luminance figures reaching 10,000 cd/m2. The standard calls for a 10-bit signal at minimum for distribution, with the EOTF framed mathematically so the video signal squeezes the most out of a 10‑bit signal’s available code values while still spanning such a broad luminance range in the image. SMPTE ST.2084 also belongs to the “Ultra HD Premium” industry specification, which requires televisions carrying the Ultra HD Premium logo to offer the following capabilities:

- A UHD resolution no lower than 3840 x 2160
- A gamut covering at least 90% of P3
- A dynamic range that is either 0.05 nits black through 1000 nits peak luminance (suiting

LCD displays), or 0.0005 nits black through 540 nits peak luminance (suiting OLED displays)

- Compatibility with SMPTE ST.2084

Setup and Workflows | HDR Viewers HDR Setup and Grading

Lastly, ST.2084 is folded into the HDR 10 standard that the Blu-ray Disc Association (BDA) adopted for Ultra HD Blu-ray. HDR 10 demands these traits of Ultra HD Blu-ray discs:

- UHD resolution of 3840 x 2160
- Up to the Rec. 2020 gamut
- SMPTE ST.2084
- Mastered to a peak luminance reaching 1000 nits

The catch is that an HDR10 mastered program on its own won’t play back-compatibly on BT.709 displays running BT.1886 (though the up-and-coming HDR10+ standard covered later tackles that). On top of that, nothing scales the image’s above-100 nit region to suit displays whose peak luminance differs. Say you grade and master an image to a peak luminance of 4000 nits and then feed that signal to an HDR10-compatible television (using ST.2084) topping out at 800 nits: everything past 800 nits clips off, while everything under 800 nits appears precisely as graded. The reason is that ST.2084 keys to absolute luminance. Grade an HDR image against a 1000 nit peak luminance display, per HDR10’s recommendation, and any ST.2084 display will honor and reproduce every level of the HDR signal it’s able to, exactly as you graded them, right up to its own peak luminance ceiling. On an HDR10-compatible television able to push 500 nits, for instance, every mastered level from 501–1000 clips away, as the screenshot below shows.

Setting the original 1000 nit waveform, which stands for the grading monitor, against a clipped 500 nit waveform that stands for the consumer television Just how much trouble this poses really hinges on how you grade your HDRstrength highlights. If only the most extreme peak highlights are pushed to maximum HDRstrength levels, the audience may well never register that the display puts out just 800 nits of signal and clips off image detail from 801–1000 nits — there weren’t many details above 800 to begin with. But grade big explosive fireballs wholly above 800 nits because it looks cool, and the audience might notice after all. The upshot: when grading for displays limited to ST.2084, these are the sorts of things you have to keep in mind.

Setup and Workflows | HDR Viewers HDR Setup and Grading
