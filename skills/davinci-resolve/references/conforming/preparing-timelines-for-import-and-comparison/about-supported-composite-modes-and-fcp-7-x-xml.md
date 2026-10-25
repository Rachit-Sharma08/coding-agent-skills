# About supported composite modes and fcp 7 x xml

Version: DaVinci Resolve 20.3 Reference Manual. Context: Preparing timelines for import and comparison.
[Chapter index](INDEX.md) / [Previous section](about-supported-transitions-and-transition-names.md) / [Next section](assigning-a-clip-or-timeline-for-offline-comparison.md)
<a id="source-aaf"></a> <a id="source-about-imported-audio-in-aaf-projects"></a> <a id="source-about-imported-text-effects"></a> <a id="source-about-supported-alpha-channels"></a> <a id="source-about-supported-composite-modes"></a> <a id="source-about-supported-still-image-formats"></a> <a id="source-fcp-7x-xml"></a> <a id="source-supported-composite-modes-with-imported-xml-and-aaf"></a> <a id="source-verifying-imported-timelines-using-offline-references"></a> <a id="source-why-set-up-an-offline-comparison"></a>

### About Supported Composite Modes

Bringing in XML project files made by Final Cut Pro 7, by Premiere Pro, or by Final Cut Pro X, DaVinci Resolve will accept eight distinct composite modes. As it brings in AAF files from Media Composer, the Overlay composite mode comes across whenever the source AAF file carries a Superimpose effect.

Add Subtract Difference Multiply Screen Overlay Lighten Hardlight Softlight Darken

### FCP 7/X XML

Yes Yes Yes Yes Yes Yes Yes Yes Yes Yes

### Supported composite modes with imported XML and AAF

### AAF

No No No No No Yes No No No No

### About Supported Still Image Formats

Still image files lasting more than a single frame, in the TIF, JPG, PNG, DPX, TGA, and DNG formats, will come into DaVinci Resolve when they sit inside Final Cut Pro X, Final Cut Pro 7, or Premiere Pro XML files, as well as AAF files exported out of Media Composer. On the DaVinci Resolve Timeline these clips behave as ordinary clips. Exporting still images, however, is confined to the Final Cut Pro 7 and Final Cut Pro X XML formats.

### About Supported Alpha Channels

Media carrying embedded alpha channels works for any project as long as its media format is one DaVinci Resolve handles; that covers TIFF, OpenEXR image sequence formats, and four-channel QuickTime formats like ProRes 4444, DNxHR 444, and QuickTime Animation. Those alpha channels switch on by themselves and serve compositing right inside the DaVinci Resolve Timeline. In round-trip workflows you can export alpha channels while rendering individual source clips. Render a program as a single clip, though, and every composited effect renders together into one output media file.

To read more about rendering clips that carry alpha channels, see Chapter 185, “Delivery Effects Processing.”

### About Imported Text Effects

Text generators come into DaVinci Resolve when you bring in XML project files from either Final Cut Pro X or Final Cut Pro 7. Every imported text effect lands on the DaVinci Resolve Timeline as a Basic text generator. Which formatting parameters carry over is partial rather than complete, varying with the project file format you import.

### About Imported Audio in AAF Projects

No matter how you combine audio track types, the channel map order, MXF alongside QuickTime files, plus rendered or unrendered clips, the whole lot should come in without trouble. NOTE: While exporting an AAF project, DaVinci Resolve can write mono media into stereo tracks. Preparing Unsupported Clips and Effects You Want to Grade Where your chosen NLE holds an unsupported effect that you still want to carry into DaVinci Resolve for grading (clips bearing effects filters native to one particular NLE, for instance), here is a straightforward workflow. To “bake” an effect into a clip bound for DaVinci Resolve: 1 Write that clip out as a self-contained media file using whichever DaVinci Resolve-compatible mastering codec you like. 2 Bring the resulting media file back into your project. 3 Cut it into your project’s timeline in place of the original effects clip. 4 Write out a version of the resulting sequence for DaVinci Resolve to use. This works well for prepping the titles and effects of projects you intend to finish in DaVinci Resolve. Make self-contained media files for every title clip and effect, and those elements import smoothly and easily, after which you can export a full, texted version of your program out of DaVinci Resolve. What is more, when a composited clip leans on unsupported effects (say, a filtered still image with animated position superimposed via the Overlay composite mode at 70% opacity), a fine way to ready it for XML export to DaVinci Resolve is to switch the composite mode to Normal, set Opacity to 100%, then write the clip out as a self-contained QuickTime movie. Bring the result back, cut it into the Timeline to stand in for that original superimposed clip, then return its composite mode to Overlay with Opacity at 70% so the original settings are matched. The unsupported effects are now “baked” into the clip, yet the effects DaVinci Resolve does handle stay live and open to readjustment in context as you grade.

### Verifying Imported Timelines Using Offline References

For holding two versions of a program against each other, DaVinci Resolve offers a dedicated interface. It removes any need to cut a rendered timeline in as a superimposed clip within your own timeline and brings many other features that aid the comparison without crowding your timeline. Switch the Edit page Source Viewer to Offline mode and you can set an Offline Reference Clip or Timeline beside a timeline you have open, both playheads ganged, shown side by side or as a split screen, a box wipe, or a difference operation, every option visible through your video output device. Play the Timeline and the Offline Reference Clip or timeline runs right along with it, so differences between the two are easy to catch. IMPORTANT: Be certain the media you imported or are using as an Offline Reference Clip carries a valid timecode track whose start time lines up with the timecode of the Timeline you compare against; otherwise an offset opens up between the Timeline and offline reference that makes comparing them hard to outright impossible. Small offsets you can patch using an offset field that the Source Viewer provides during offline mode, yet large ones simply prove impractical to fix.

### Why Set Up An Offline Comparison?

No matter how you arrange an offline reference, it gives you a handy way to weigh two versions of a program against each other. Several motives exist for holding an Offline Reference Clip up against a timeline:

- Verifying the clip order: When you are not certain you have cleanly settled reel conflicts or other snags that cropped up while conforming a timeline, you can set each edit beside the program’s offline version to catch problems and pin down which media truly belongs to any clip.
- Recreating effects: Where offline effects exist, such as temporary grades done in the NLE or pan and scan transforms you want to check, Offline reference mode lets you split-screen your present grade against the Offline Reference Clip on the Color page.
- Comparing two versions of a timeline: You can visually hold one timeline beside another version of itself to catch differences worth evaluating.
- Filling holes in timelines with missing or unlinked clips: Living under Preferences > User > Editing > General settings, a pair of options, namely “Show offline clips through conform gaps” plus “Show offline clips through missing clips,” direct DaVinci Resolve to surface Offline Reference Clip media that plugs Timeline gaps or stands in for the contents of unlinked clips. You generally reach for this in a pinch, when a screening or review session has to go ahead even though some media is missing for one reason or another.

To read more, see Chapter 4, “System and User Preferences.”

NOTE: As a rule, the flattened version of the program handed to you runs a low-quality codec and holds effects and color correction that are not final, which is exactly why it goes by Offline Reference Clip.
