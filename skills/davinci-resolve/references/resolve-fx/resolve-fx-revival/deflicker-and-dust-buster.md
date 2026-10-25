# Deflicker and dust buster

Version: DaVinci Resolve 20.3 Reference Manual. Context: Deflicker studio version only, Dust buster studio version only.
[Chapter index](INDEX.md) / [Previous section](dead-pixel-fixer-and-deband.md) / [Next section](dust-buster-patch-type.md) / [Continue Dust Buster (Studio Version Only) / Patch Options](dust-buster-patch-type.md)
<a id="source-deflicker-studio-version-only"></a> <a id="source-dust-buster-studio-version-only"></a> <a id="source-general-1"></a> <a id="source-main-parameters"></a> <a id="source-output"></a> <a id="source-restore-original-detail-after-deflicker"></a> <a id="source-speed-optimization-options"></a> <a id="source-temporal-nr"></a>

### Deflicker (Studio Version Only)

The Deflicker plugin copes with problems as varied as flickering exposure in timelapse clips, flickering fluorescent lighting, flicker in archival film sources, and in some subtle cases even the “rolling bars” seen on video screens shot with cameras whose shutter speeds don’t match. Two things stand out about this filter: it goes after only rapid, temporally unstable swings in lightness, and it can confine its attention to just the image areas where flickering shows up, leaving the rest of the image alone. Thanks to that, the plugin can frequently mend problems once written off as “unfixable.”

The unprocessed image, its blue screen marred by flicker bars The outcome once Deflicker is set to Fluoro Light, (clip courtesy Redline Films)

### Main Parameters

By default the plugin’s top section surfaces just one control, which in plenty of cases is all you’ll require.

- Deflicker Settings pop-up menu: The first two options, Timelapse and Fluoro Light, are presets that do a solid job of clearing two distinct categories of flickering artifact. Should neither preset perform quite as well as you’d hoped, a third option, Advanced Controls, unlocks the Isolate Flicker controls sitting at this plugin’s core so you can tailor it further to your needs.

### Temporal NR

Concealed by default, these controls surface only once you set Deflicker Setting to Advanced Controls; they govern how motion in the scene gets detected, so that flickering is handled correctly in relation to the movement of subjects and objects in the frame where it shows up.

- Frames Either Side: Sets the count of frames analyzed to work out what’s moving. More isn’t always better; the optimal setting, once again, depends on the scene. The default is 3.
- Mo.Est. Type: Picks the technique DaVinci Resolve applies to analyze the image and detect motion. The option names notwithstanding, which one performs best leans heavily on the scene. The default, Faster, demands less of the processor and gives up some accuracy; that can actually be a plus, doing a better job on high-detail images that would trip up the Better option. Picking Better buys more accuracy at a higher processor cost, and Better strains harder to match fine details, which can occasionally cause trouble. None switches off motion analysis entirely, which can serve well (and runs far faster) where the scene holds no motion whatsoever. The default is Better.
- Motion Range: Three settings — Small, Medium, and Large — let you set the speed of frame motion that ought to be detected.
- Luma Threshold: Sets the threshold past which luma changes won’t count as flicker. The range is 0–100; at 0 nothing is deflickered, at 100 everything is. The default is 100.
- Chroma Threshold: Sets the threshold past which chroma changes won’t count as flicker. The range is 0–100; at 0 nothing is deflickered, at 100 everything is. The default is 100.
- Luma Chroma Same Threshold: Lets you decide whether or not to gang the Luma and Chroma Threshold sliders.
- Motion Threshold: Sets the threshold past which motion won’t count as flicker.

### Speed Optimization Options

Collapsed by default, expanding this control group brings up two controls:

- Reduced-Detail Motion checkbox: On by default, it trims how much detail gets analyzed during flicker detection. Often it makes no visible difference yet speeds processing up. Switch it off if your clip carries fine detail that’s being smoothed too aggressively.
- Limit Analysis Area checkbox: Switching this on brings up controls for a sample box that you can use to pen deflickering into a particular region of the image. The option earns its keep when: a) only one part of the image flickers, so concentrating on that area alone speeds the operation up considerably, or b) deflickering that’s handling one part of the image beautifully is smoothing another part too much.

### Restore Original Detail After Deflicker

Collapsed by default, expanding this control group brings up two controls:

- Detail to Restore slider: Quickly singles out grain, fine detail, and sharp edges that the deflicker operation should leave alone, holding those fine details exactly as they were.
- Show Detail Restored checkbox: Switching this checkbox on reveals the edges that the Detail to Restore slider detects and uses, which helps you tune the operation.

### Output

The Output pop-up menu lets you set what Deflicker sends out, with options geared toward troubleshooting problem clips. The available options are:

- Deflickered Result: The finished, repaired result. This is the default setting.
- Detected Flicker: This option presents a mask that highlights the image parts being

flagged as flickering, helping you judge whether the right parts of the image are getting targeted. That mask can be quite subtle, though.

- Magnified Flicker: This option presents an exaggerated take on the Detected Flicker mask, making it easier to see what the Deflicker plugin is up to.

### Dust Buster (Studio Version Only)

This plugin, too, sets out to clear away dust and dirt, plus other imperfections and artifacts, from clips — but it works only under your guidance, on clips where the Automatic Dirt Removal plugin comes up short. That guidance amounts to stepping through the clip frame-by-frame and drawing boxes around the imperfections you want gone. The moment you’ve drawn a box, the offending imperfection vanishes auto-magically, as seamlessly as can be. It handles dirt and dust well, and it copes with really large stains and blotches too, as shown below.

The Dust Buster shares a lot with the Dead Pixel Fixer, yet the Dust Buster effect is meant to mend fleeting bits of dust and dirt that survive only a frame or two, whereas the Dead Pixel Fixer is meant for blemishes locked in place across a clip’s whole length.

### General

These top-level controls govern how you draw the patches used to mend temporally unstable dust and dirt in the frame, along with whether their on-screen controls appear and in what manner.

- Navigation Controls: Four buttons let you leap to frames where you’ve drawn patches. The four buttons are:

First Modified Frame: Sends the playhead to that clip’s first frame holding a patch. Previous Modified Frame: Sends the playhead back to the nearest earlier frame holding a patch. Next Modified Frame: Sends the playhead ahead to the nearest later frame holding a patch. Last Modified Frame: Sends the playhead to that clip’s last frame holding a patch.

- Draw Rect: Click and drag to lay a rectangular patch of any size from one corner across to the opposite corner. After it’s drawn, click any edge of the overlay and drag to reposition it.
- Draw Ellipse: Click and drag to lay an elliptical patch of any size from one corner across to the opposite corner. After it’s drawn, click any edge of the overlay and drag to reposition it.
- Place Patch: For laying small patches aimed at tiny details such as dead pixels. Picking this option brings up a New Patch Size slider that sets the size of the patches you’re about to place before you place them. After one’s drawn, click the edge of any patch and drag to reposition it.
- New Patch Size: (active only while Place Patch is selected) Sets how big a patch the Place Patch tool lays down.
- Show Patches: A checkbox that reveals or conceals every patch’s onscreen outline in the Viewer.
- Reset Frame: Wipes all patches off the current frame.
