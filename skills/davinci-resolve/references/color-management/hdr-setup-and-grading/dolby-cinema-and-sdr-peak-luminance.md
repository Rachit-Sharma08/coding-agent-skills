# Dolby cinema projector and standard peak luminance for SDR displays

Version: DaVinci Resolve 20.3 Reference Manual. Context: HDR setup and grading.
[Chapter index](INDEX.md) / [Previous section](hdr-grading-and-display-context.md) / [Next section](dolby-vision-mastering-displays-and-icmu.md)
<a id="source-dolby-cinema-projector"></a> <a id="source-dolby-vision"></a> <a id="source-hdr-viewers"></a> <a id="source-letterboxing-for-dolby-vision-mastering"></a> <a id="source-organizing-your-timeline-for-dolby-vision-mastering"></a> <a id="source-setting-up-color-management-for-dolby-vision-mastering"></a> <a id="source-standard-peak-luminance-for-sdr-displays"></a>

### Dolby Cinema projector

### Standard peak luminance for SDR displays

Reference peak luminance for SDR DCI projection; Dolby Cinema 3D peak 48 luminance

Absolute black

† the 0–3 and 1020–1023 ranges are reserved values

This table of values helps you see where HDR nit levels land on older external scopes, but when you monitor with the video scopes built into DaVinci Resolve, you can enable the “HDR (ST.2084/HLG)” entry under Waveform Scale Style, reached through the Scopes option menu; doing so swaps the scopes’ 10-bit scale for one keyed to nit values (or cd/m2) instead.

The video scopes shown with HDR (ST.2084/HLG) active, set via Waveform Scale Style under the Scopes option menu IMPORTANT: When you run a workflow that isn’t Davinci Resolve Color Managed and you switch on the HDR (ST.2084/HLG) scopes, the waveform keeps reporting HDR levels no matter what — even after you’ve manually chosen Rec.709 as the output color space — so its readings won’t be 100% accurate. TIP: Should the detail visible in the 0–519 range (0–100 nits) of the video scope graphs prove insufficient, you can turn to the 3D Scopes Lookup Table control, found within the Color Management panel of the Project Settings, and assign a fitting “HDR X nits to Gamma 2.4 LUT,” with X standing for the peak nit level of the HDR display in use. That redraws the scopes such that the signal’s 0–100 nit span occupies the scopes’ full height, from 0 through 1023. As a result, the HDR-strength highlights are driven past the visible top edge of the scopes and vanish, yet the payoff is markedly clearer midtone detail in the picture.

### HDR Viewers

On both Mac and Windows systems, the native DaVinci Resolve viewers can be shown in HDR. This setting reaches every DaVinci Resolve viewer — that covers the main page viewers, Cinema Mode, Fairlight Floating Viewer, Scene Cut Dialog, plus the Video Clean Feed. You’ll need an HDR-capable display along with HDR switched on at the OS level:

- Turn on the Windows HDR display settings (System > Display > HDR).
- Turn on the Mac HDR display settings (System Settings > Displays > High Dynamic Range).
- Within DaVinci Resolve Preferences > System > General, you’ll have to enable the “Use 10-bit

precision in viewers if available” box. NOTE: The broader controls/UI and dialogs that aren’t viewers (for instance, the secondary screen, project manager, floating Media Pool) remain unaffected.

Setup and Workflows | HDR Viewers HDR Setup and Grading

### Dolby Vision®

A longtime advocate and innovator in using HDR to improve how consumers experience video, Dolby Laboratories created an HDR mastering and delivery method named Dolby Vision. Like the majority of HDR standards covered in this chapter, Dolby Vision relies on the PQ (perceptual quantizer) electrical-optical transfer function (EOTF, which describes how an electronic video signal appears on a display) as defined by SMPTE ST.2084, paired with a tiered set of metadata carried alongside the video stream. Every piece of metadata Dolby Vision uses is sorted into levels, and the ones below matter most to the colorist:

- Level 0 metadata, the global metadata describing the Mastering Display (the one the colorist works on), covering aspect ratio, frame rate, color encoding, plus details about all the target displays referenced by the Level 2 and Level 8 trim metadata noted below.
- Level 1 metadata, the Dolby Vision v2.9 analysis metadata produced automatically whenever you employ the Dolby Vision controls to analyze the timeline’s clips. Every DaVinci Resolve Studio user has access to the controls that auto-generate Level 1 metadata.
- Level 2 metadata, the Dolby Vision v2.9 trimming metadata the colorist sets through the version 2.9 trim controls found in the Dolby Vision palette of the Color page. This trim governs how the Dolby Vision image gets mapped onto a target display (for example, a 100 nit BT.709 display) that differs from the mastering display (for example, a 1000 nit BT.2020 display). Its role is to safeguard a program’s artistic intent by letting the colorist guide how the program’s signal is fitted into the varying luminance ranges of displays whose peak luminance capabilities differ. Hand-adjustable Level 2 metadata is offered to DaVinci Resolve Studio users only through a license acquired from Dolby.
- Level 3 metadata, the Dolby Vision v4.0 offset added to the Level 1 metadata produced by the analyze buttons in the Dolby Vision controls. It additionally holds the mid tone offset data.
- Level 5 metadata, which reports the deliverable format’s aspect ratio together with the aspect ratio of the actual picture sitting inside that format. This metadata applies at the per clip level as well.
- Level 6 metadata, which holds the MaxCLL and MaxFALL levels that the HDR10 mastering standard of HDR requires.
- Level 8 metadata, the revised Dolby Vision v4.0 trimming metadata the colorist sets through the v4.0 trim controls found in the Dolby Vision palette of the Color page. This more advanced collection of trim commands permits finer control over how the Dolby Vision image is mapped onto a target display (for example, a 100 nit BT.709 display) distinct from the mastering display (for example, a 1000 nit BT.2020 display). As with Level 2 metadata, Level 8 metadata exists to protect a program’s artistic intent by letting the colorist steer how the program’s signal fits into the differing luminance ranges of displays of varying peak luminance capability. Hand-adjustable Level 8 metadata is available to DaVinci Resolve Studio users solely via a license obtained from Dolby. Which set you use — the Level 2 trim controls or the Level 8 trim controls — hinges on the Dolby Vision version setting you pick in the Color Management panel of the Project Settings.

NOTE: At present every user is advised to select Dolby Vision v4.0 for both analysis and trimming, since it yields better results. Should you need to supply Dolby Vision v2.9 metadata when mastering for backwards compatibility, DaVinci Resolve is now able to export v2.9 metadata out of projects built on v4.0 workflows. The metadata levels outlined above reflect the situation as of this writing. Because Dolby Vision evolves quickly, though, you should consult Dolby’s website to stay abreast of new features and metadata levels as Dolby introduces them: https:// professionalsupport.dolby.com/s/article/Dolby-Vision-Metadata-Levels?language=en_US

Setup and Workflows | HDR Viewers HDR Setup and Grading

For some time to come, the consumer display field will include a broad mix of televisions and projectors with differing performance, all but certain to get better year after year. The upshot is that grading for the displays of today can leave content looking less vibrant than material produced five years down the road. That is particularly frustrating for narrative work destined to live a long time on streaming services, where fresh waves of viewers keep finding it. One remedy would be to re-grade your program repeatedly at assorted nit levels so you have deliverables matched to a span of display capabilities — but that is a staggering amount of labor. Dolby Vision provides a shortcut, applying advanced algorithms to derive auto-analyzed metadata that smartly directs the reshaping of a picture graded at a single nit level (4000 nits, for instance) so it appears perceptually equivalent to a viewer on a 1000 nit display. Highlights and saturation too intense for a given display are reined in so as to preserve nearly the same impression without clipping or flattening detail. On top of that, a colorist can manually trim this automatic analysis to honor the program authors’ artistic aims wherever the auto pass falls short of what’s desired. That pairing of auto-analysis with manual trimming is central to how Dolby Vision simplifies mastering programs for backward compatibility with SDR displays and for the assorted peak luminance capabilities of various makes and models of HDR consumer displays, now and going forward. You need only perform a single 100 nit trim pass to direct the HDR program’s downconversion all the way to SDR, and the Dolby Vision system can lean on that data to determine how intermediate presentations (for instance, at 700 or 1200 nits) ought to be adjusted. You may even run several trim passes at chosen nit levels, like a 100 nit pass plus a 1000 nit pass, giving the Dolby Vision system richer information to steer intermediate presentations across different displays accurately. Moreover, trimming every clip isn’t necessary. Where the analysis holds up, you can leave those clips alone and trim only the ones that call for it. The system as a whole was designed to be as efficient as possible for colorists so the broadest range of viewers see the image the way it was intended. That, in essence, is what makes the Dolby Vision system valuable. It’s possible to grade on a more future-proofed 4000 nit display, then lean on auto-analysis plus one or two hand-done trim passes to keep things backward compatible with SDR televisions, all while the HDR highlights are scaled intelligently to deliver the best possible rendition of the mastered picture for whatever peak luminance and color volume a given television can manage. Every part of this is driven by the choices the colorist makes during the grade. Currently, every one of the seven major Hollywood studios masters in Dolby Vision for cinema. Among the studios that have committed to mastering content in Dolby Vision for home distribution are Universal, Warner Brothers, Sony Pictures, and MGM. Content providers that have signed on to distribute streaming Dolby Vision content include Netflix, Vudu, and Amazon. And if you’d like to watch Dolby Vision content on a television at home, consumer television makers LG, TCL, Vizio, HiSense, Sony, Toshiba, and Bang & Olfusen have all released models that support Dolby Vision.

### Organizing Your Timeline for Dolby Vision Mastering

Among the very first tasks before starting a Dolby Vision grade is arranging your timeline to suit it. Since every clip is run through a visual analysis to support the Dolby Vision workflow, particular restrictions apply to how clips may be laid out in a timeline.

- Any clip you want analyzed in a Dolby Vision workflow has to sit on video track V1; clips on the other tracks are disregarded.
- Clips that overlap one another to form a composite must be consolidated into a single timeline item before they can be analyzed properly. In practice, that means every cluster of clips forming a composite in a timeline — whether overlapping clips joined through keys or alpha channel transparency, overlapping clips joined via composite or blend modes, or text generators sitting over one or more video clips — has to be converted into a compound clip for Dolby Vision analysis to function correctly.

Setup and Workflows | HDR Viewers HDR Setup and Grading

### Letterboxing for Dolby Vision Mastering

When a Dolby Vision workflow analyzes clips, it records both the timeline aspect ratio and the image aspect ratio of each clip within that timeline. The Dolby Vision analysis can handle programs that combine various aspect ratios of letterboxing (or blanking); however, Dolby Vision won’t support letterbox on two sides at once (both pillarbox and letterbox), only one at a time.

### Setting Up Color Management for Dolby Vision Mastering

So that an HDR signal displays correctly, you have to output your graded program with the EOTF appropriate to the HDR standard you’re mastering. That EOTF translates the various levels DaVinci Resolve sends to your HDR display, using the SMPTE ST.2084 PQ setting that Dolby Vision output requires. There are three ways to configure this:

- Output Color Space and Gamma settings in RCM or ACES
- Color Space and Gamma settings inside a chain of Resolve FX Color Transform plugins that

you place after each individual grade or following a Timeline grade

- 3D LUTs that convert signals from one standard into another, dropped in after

each clip’s grade or once a Timeline grade is complete Although Dolby Vision content isn’t tied to any one color space, Resolve Color Management offers a P3 D65 setting that lines up with what most mastering displays in use as of this writing can do.
