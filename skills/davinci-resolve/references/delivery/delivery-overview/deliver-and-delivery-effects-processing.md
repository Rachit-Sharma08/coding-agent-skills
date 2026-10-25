# Deliver and delivery effects processing

Version: DaVinci Resolve 20.3 Reference Manual. Context: Delivery overview.
[Chapter index](INDEX.md) / [Next section](the-deliver-page-and-quick-export.md)
<a id="source-alpha-channels"></a> <a id="source-color-corrections-composite-modes"></a> <a id="source-deliver"></a> <a id="source-deliver-1"></a> <a id="source-delivery-effects-processing"></a> <a id="source-delivery-effects-processing-1"></a> <a id="source-delivery-effects-processing-using-the-deliver-page"></a> <a id="source-determining-the-rendered-output-resolution-of-clips-in-mixed-timelines"></a> <a id="source-export-alpha-channels-in-individual-clips-mode"></a> <a id="source-export-alpha-channels-in-single-clip-mode"></a> <a id="source-more-about-rendering-speed-effects"></a> <a id="source-overview"></a> <a id="source-rendering-edit-and-input-sizing-adjustments"></a> <a id="source-rendering-mixed-frame-rate-timelines"></a> <a id="source-when-rendering-a-single-clip-or-when-outputting-to-tape"></a> <a id="source-when-rendering-individual-source-clips-for-round-trip-workflows"></a>

## Overview

Covers: Deliver; Delivery Effects Processing; Using the Deliver Page.

## Deliver

### Deliver

## Delivery Effects Processing

### Delivery Effects Processing

The way that various video effects get treated as you drive the Deliver page controls is the subject of this chapter.

The handling of effects in your finished output hinges on the choice between Single Clip and Individual Clips mode.

### When Rendering a Single Clip or When Outputting to Tape

No matter whether you produce a QuickTime or MXF master of the project as one clip, generate a DPX image sequence destined for film, or send signal straight to tape, every supported compositing, speed, and transform effect gets processed by DaVinci Resolve and “baked” into the resulting media. Anything unsupported is simply skipped over, never visible, and leaves no mark on the media you render and output.

### When Rendering Individual Source Clips for Round-Trip Workflows

When your goal is to render separate media files so the project can return to an NLE or finishing application for the last stages (laying in titles and similar effects ahead of delivery), DaVinci Resolve treats each category of effect on its own terms. Anything unsupported stays hidden inside DaVinci Resolve. That said, the underlying effects data is held onto internally, so once you export an XML or AAF file headed back to whichever NLE you prefer, those effects come back into view, sitting atop the color corrected media you rendered out of DaVinci Resolve and returned. The effects DaVinci Resolve actually supports — composite modes, opacity settings, speed effects, transitions and the like — get a separate treatment. While you can see them inside DaVinci Resolve during your session, they are never “baked” into the finished media you render ahead of handing it back to the NLE or finishing application. Rather, only the slice of each media clip your project draws on becomes its own rendered file, and the XML file you export from DaVinci Resolve carries every bit of effects metadata required to rebuild the rendered footage into a timeline whose Final Cut Pro effects ride on top of DaVinci Resolve-graded media.

### Color Corrections Composite Modes

### Alpha Channels

Transitions Opacity Settings Position, Scale, Rotation Linear Speed Effects Variable Speed Effects Long Duration Still Images Freeze Frames

The per-format status values are tabulated below, one value per cell.

| Format           |           |           |                     |           |           |             |           |           |     |          |
| ---------------- | --------- | --------- | ------------------- | --------- | --------- | ----------- | --------- | --------- | --- | -------- |
| EDL              | N/A       | N/A       |                     |           |           |             |           |           |     |          |
|                  | N/A       |           |                     |           |           |             |           |           |     |          |
|                  | Sent Back | N/A       | N/A                 | Sent Back | N/A       | N/A         | N/A       |           |     |          |
| FCP 7            | N/A       | Sent Back | Optionally Rendered | Sent Back | Sent Back | Conditional | Sent Back | Sent Back | N/A | N/A      |
| FCP X            | Rendered  | Sent Back | Optionally Rendered | Sent Back | Sent Back | Conditional | Sent Back | Sent Back | N/A | N/A      |
| Premiere Pro     | N/A       | Sent Back | Optionally Rendered | Sent Back | Sent Back | Conditional | Sent Back | Sent Back | N/A | N/A      |
| Media Composer\* | N/A       | Rendered  | Optionally Rendered | Sent Back | Sent Back | Conditional | Sent Back | Sent Back | N/A | Rendered |

- These effects come back solely during AAF round trips in the case where you refresh an AAF file that already exists, as opposed to producing a brand-new AAF file. What the table illustrates is which effects DaVinci Resolve renders versus which ones are handed back across the various round trip workflows.

Once the project has been reimported into your NLE or finishing application, you can tweak those effects again as you wrap up the program, with no requirement to re-render individual clips inside DaVinci Resolve. IMPORTANT: The single case where media and effects are not carried through round-trip workflows is nested sequences originating in Final Cut Pro 7 and Media Composer, which DaVinci Resolve cannot read; any XML and AAF files that hold nested sequences will fail to import. Conversely, projects from Final Cut Pro X that include compound clips do import fine.

### More About Rendering Speed Effects

Should your project include speed effects, keep in mind that DaVInci Resolve has the option to process them through Optical Flow, which yields crisp slow motion and fast motion results that come ready-made out of DaVinci Resolve. When Optical Flow processing inside DaVinci Resolve meets your needs, a round-trip export may be unnecessary if your sole motivation was handing slow motion clips to a separate application for rendering; choosing Single clip mode for the Timeline “bakes” the speed effects in according to the project-wide settings, or the per-clip values if you assigned individual Retime Process settings to particular clips. On the other hand, when your aim is to pass unrendered speed effects along to a different application, rendering in Individual source clips mode ensures that the entire span of every original media clip is rendered, with the speed effect itself carried inside the exported XML, AAF, or EDL file. NOTE: DaVinci Resolve tacks three frame handles onto any clip carrying speed changes, plus onto rendered clips whose frame rate differs from the project’s. The purpose is to ease reconform in NLEs that need handles stretching past the genuine length of each such clip.

### Determining the Rendered Output Resolution of Clips in Mixed Timelines

As a rule, when you render individual source clips, each one comes out at either the project resolution or whatever the Resolution dropdown in the Render Settings dictates (that dropdown takes precedence over the project resolution), and clips whose size differs from the project resolution are scaled or left alone per your picks in the Image Scaling panel of the Project Settings. That said, when you generate dailies for a project whose clips carry mixed resolutions, you have the choice to keep each clip at its native resolution by enabling the “Render at source resolution” checkbox within the Video group of controls.

### Rendering Edit and Input Sizing Adjustments

Whether sizing ends up baked into your delivered media is governed by the “Disable sizing and blanking” checkbox found among the Advanced Settings options of the Render Settings panel. Sizing and blanking can be switched off whether you render the current Timeline as one clip or render individual clips. Leave “Disable sizing and blanking output” off and the following all get written into the finished media through the optical-quality sizing algorithms DaVinci Resolve provides: Output Blanking; the sizing adjustments made on the Cut and Edit pages; the Color page’s Input and Output Sizing adjustments; and Image Stabilization. That is the preferred route once your sizing adjustments are signed off and locked, and you intend to “bake” them into the media you deliver. Switch “Disable sizing and blanking output” on instead and those same items — Output Blanking, the Cut and Edit page sizing work, the Color page Input plus Output Sizing changes, along with Image Stabilization — stay out of the render; every clip then emerges either at the source resolution when “Render at source resolution” is active in individual clips mode, or at whatever resolution the Timeline or project currently specifies. The sizing adjustments you applied are still written into the XML or AAF file you export, though. That suits workflows in which the editor plans to keep refining sizing, measured against the clips’ original dimensions, after you have handed over the graded project. Bear in mind that to render Input Sizing adjustments into your output media, the “Force sizing to highest quality” checkbox makes certain DaVinci Resolve picks the top-tier sizing setting even when you have briefly opted for a quicker, lower-quality choice to suit a slower machine. NOTE: “Disable sizing and blanking output” leaves untouched any transform operations occurring inside the Fusion page, and likewise does not stop transforms produced by an Open FX or Resolve FX plugin attached to one or more clips on the Cut, Edit, or Color pages. Every one of those effects keeps getting rendered into the finished output.

### Rendering Mixed Frame Rate Timelines

DaVinci Resolve accommodates mixed frame rates as soon as you pick anything besides none in the “Mixed Frame Rate format” dropdown menu. You will find that dropdown two places: under Conform Options within the Project Settings’ General Options panel, or over in the Import AAF or XML dialog. Pick the entry matching the application you trade projects with (or DaVinci Resolve itself when you stay entirely inside DaVinci Resolve), and DaVinci Resolve will conform and process every clip on the Timeline so it plays at the rate chosen in the “Timeline frame rate” dropdown menu. By way of illustration, clips at 23.98, 29.97, 30, 50, 59.94, and 60 fps would each play at 24 fps if the “Timeline frame rate” in the Master Settings panel of the Project Settings is set there. The way clips on mixed frame rate timelines get rendered hinges on whether the Render Settings call for Individual source clips or a Single clip.

- Individual source clips: Every clip renders on its own at the frame rate it originally had.
- Single clip: Every clip is brought to the “Timecode calculated at” frame rate and written out as one media file. Conversion follows whichever method the Retime process dropdown specifies — that dropdown lives in the Project Settings under the Master Settings panel — unless a per-clip Retime process setting in the Video inspector overrides the project-wide choice. Selecting Optical Flow processing gives you the best-quality conversion DaVinci Resolve offers.

### Export Alpha Channels in Individual Clips Mode

You will only see this option when the target media format can hold alpha channels. Where your media carries an Alpha channel, the Export Alpha checkbox — sitting in the render settings’ Video panel — can be enabled whenever you render individual source clips. With that enabled, DaVinci Resolve outputs clips containing alpha channels under one of two conditions:

- If the clip’s source media already has an Alpha channel baked in, that embedded Alpha channel is carried over to the rendered copy of the clip.
- If the clip’s grade routes a key into an Alpha output, that Alpha output becomes an Alpha channel on the rendered clip.

Either way, exporting Alpha channels is possible solely when you render individual source clips into an RGBA format like TIFF, OpenEXR, ProRes 4444, ProRes 4444 XQ, or DNxHR 444.

### Export Alpha Channels in Single Clip Mode

In Single Clip mode, DaVinci Resolve will render Alpha channels provided the chosen codec is one that handles an Alpha channel (i.e., ProRes 4444, DNxHR 444, etc.). That makes it possible to attach one Alpha channel across a whole timeline at export time instead of working clip by clip. To Render an Alpha Channel in Single Clip Mode: 1 Switch the Render Settings to “Single Clip” mode. 2 Within the Video tab’s Codec and Type selection boxes, pick a codec capable of an Alpha channel. 3 Tick the “Export Alpha” checkbox that shows up beneath the Frame rate selector. 4 Where the codec permits it, you can chose the Alpha Mode type; Premultiplied serves as the default. Should the codec you picked lack Alpha channel support, no “Export Alpha” box will surface as a choice.
