# What are the project settings and opening and editing project settings

Version: DaVinci Resolve 20.3 Reference Manual. Context: Project settings.
[Chapter index](INDEX.md) / [Next section](video-monitoring-and-optimized-media-and-render-cache.md)
<a id="source-master-settings"></a> <a id="source-opening-and-editing-project-settings"></a> <a id="source-presets"></a> <a id="source-project-manager-and-project-settings-buttons"></a> <a id="source-project-settings"></a> <a id="source-project-settings-part-1"></a> <a id="source-project-settings-window"></a> <a id="source-timeline-format"></a> <a id="source-what-are-the-project-settings"></a>

### Project Settings

The settings that define what each separate project is made of are the focus of this chapter. Getting acquainted with what's here before you build your very first project is a wise move.

### What Are the Project Settings?

Every project-specific parameter stored alongside a given project lives in the Project Settings window. Among them are core project properties: the timeline format, video monitoring choices, the approach to optimizing media, and the destination for cache files. Image scaling properties, color management options, and a host of other properties that shape projects at a deep level are in there too.

### Opening and Editing Project Settings

From any point inside DaVinci Resolve, you reach all of these project-specific settings simply by clicking the gear button at the lower right of the page bar.

### Project Manager and Project Settings buttons

Onscreen, the Project Settings window opens up centered.

### Project Settings window

A sidebar down the left side of the Project Settings window lets you pick from a row of panels into which it's split. Every panel holds a cluster of related settings governing one category of DaVinci Resolve behavior. To alter project settings: 1 In the left sidebar, click the name of whichever settings group you want, which opens that panel. 2 Adjust the settings as required. 3 To commit your changes, do one of these: Click Save to commit them and shut the Project Settings. Option-click Save to commit them yet leave the Project Settings window open for further changes. That choice exists because keeping the Project Settings window open is sometimes needed as you go on making changes whose effect may show up visibly on the clips and timelines in your project.

### Presets

Saving tailored bundles of Project Settings for later reuse is what the Presets menu is for. A preset can capture the condition of nearly every parameter and setting across every panel of the Project Settings window, which makes hopping between different setups for different tasks, or fitting different kinds of projects, painless. You get to the Presets menu by clicking the option menu (three dots) at the top-right corner of the Project Settings window. These are the items the Presets menu shows:

- Project Settings Presets: Every existing Project Preset is listed here, with the Default Preset at the top.
- Set Current Settings as Default Preset: Picking this writes the present Project Settings out as the fresh Default Preset.
- Save Current Settings as Preset: Picking this stores the present Project Settings as a brand-new preset, which then turns up in the menu list overhead.
- Import Preset: Picking this opens a file browser so you can pull in a DaVinci Resolve Project Settings Preset file. These files carry the .preset extension.

Through this menu you can build, import, and export presets of your own, piling up however many you require for the kinds of projects you take on.

Reaching the Presets Menu means clicking the option menu within the Project Settings window

To create a new preset: 1 Do one of the following:

- In the Project Manager, right-click a project and pick Project Settings off the contextual menu.
- Open any project and then bring up the Project Settings.

2 Use the assorted panels of the Project Settings window to set whatever settings you require. You needn't save along the way; it all saves together later. 3 In the top-right corner of the Project Settings window, click the option menu (three dots). 4 Select Save Current Settings as Preset. 5 Into the dialog box, type a descriptive name for the new preset, then press the OK button. 6 The Project Settings Preset menu now lists your new preset name. Once a custom preset or two exists, you're free to load them into a project at any moment. To pull a preset's stored settings into a project: 1 Open the project whose preset you mean to update. 2 Bring up the Project Settings window. 3 In the Project Settings window, click the option menu. 4 Click the Project Preset name you'd like applied to the open project. 5 From the drop-down menu, select Load Preset. The new preset's values are applied to the Project Settings right away. This function has no undo. To update a preset: 1 Bring up the Project Settings window. 2 Run through the assorted panels of the Project Settings window to change whatever needs updating. 3 In the Project Settings window, click the option menu. 4 Click the Project Preset name you want updated. 5 From the drop-down menu, select Update Preset, then pick Update in the dialog box. Your current settings overwrite the preset. This function has no undo. To set the default preset: 1 Out of the Project Settings Presets list, pick the preset you want loaded each time a new project begins. 2 Click the preset and pick Set As Default Preset. or 1 From the Project Settings window's option menu, choose "Set Current Settings as Default Preset" to turn whatever your settings currently are into the new default. 2 Pick Update in the dialog box. Your current settings overwrite the preset. This function has no undo.

To export a preset: 1 Out of the Project Settings Presets list, click the preset you plan to export. 2 From the drop-down menu, choose Export Preset. 3 Within the file browser, supply a name and save spot for the preset, then press Save. The DaVinci Resolve Project Settings Preset file arrives there with a ".preset" extension. To import a preset: 1 Within the Project Settings window, click the option menu. 2 Select Import Preset. 3 Through the file browser, navigate to the DaVinci Resolve Project Settings Preset file you'd like to bring in. The ".preset" extension marks it. Press Open. To delete a preset: 1 Out of the Project Settings Presets list, click the preset you'd like gone. 2 From the drop-down menu, choose Delete Preset. 3 In the dialog box, press Delete. The Project Settings disappear at once. This function has no undo.

### Master Settings

Project-specific, this panel is where you establish and tune the most fundamental properties of your project's timelines, the timeline format, the video monitoring method, and conform options among them. Plenty of workflows call for tuning these before you even begin a project. Out of the box, every timeline draws on these project-wide settings. That said, from DaVinci Resolve 16 onward, you may instead build timelines that carry their own individual Format, Monitoring, and Output Sizing settings. Still, switch a timeline over to "Basic Settings" and it falls back in line with the project-wide options picked in the Project Settings.

### Timeline Format

The current project's geometry and image processing are governed by this group of settings.

- Timeline resolution: A drop-down menu from which you pick a frame resolution preset that image processing uses during grading. Because DaVinci Resolve is resolution independent, you're free to swap the resolution whenever, and every window, track, sizing change, and bit of keyframe data is recomputed on its own to suit the new size. You could, say, grade a 4K project while monitoring at HD if your suite holds only an HD monitor, then render the completed project at 4K for final delivery. Or you might shrink an HD project down to SD to produce a second set of deliverables.

For deeper coverage of Resolve's resolution independence, turn to Chapter 152, "Sizing and Image Stabilization.""

- Frame size (Labeled "For X x Y processing"): Lets you dial in resolutions absent from the "Timeline resolution" drop-down menu.
- Use vertical resolution: Ticking this checkbox flips the horizontal and vertical pixels of the Timeline resolution. That lets you lay out a timeline vertically for showing on phones, tablets, or upright-mounted televisions used as digital signage.
- Pixel aspect ratio: Serves to pick PAR settings for image formats outside the default square pixel format. Among the choices: a 16:9 anamorphic PAR, for SD projects a 4:3 PAR, or else a Cinemascope ratio.
- Timeline frame rate: Fixes the project's main frame rate. Both standard and high frame rate (HFR) options are on offer. Importing an AAF or XML file sets this automatically through a choice in the Project Import dialog. The best practice is to settle on a frame rate ahead of bringing media into the Media Pool. Even so, the very first time you import media into an empty Media Pool, you're asked about it when the incoming media's frame rate differs from the Timeline frame rate fixed here, and you may have this setting updated automatically to match the media you're bringing in. After one or more files have landed in the Media Pool, the setting can no longer be altered.
- Use drop frame timecode: Switches drop frame timecode on or off for the current project. Off by default.
- Enable interlace processing: Interlaced media is supported throughout DaVinci Resolve. Ticking the "Enable interlace processing" checkbox makes DaVinci Resolve run every internal operation on separated fields, so the field integrity of your program's interlaced clips stays intact. On top of that, each Media Pool clip has, within the Clip Attributes window's Video panel, a Field Dominance drop-down menu for declaring whether clips are upper- or lower-field dominant; an Auto setting makes that call by default. A matching checkbox named "Field rendering" also sits in the Render Settings panel of the Deliver page, switching field rendering on or off as you render file-based output.

Two situations call for keeping this setting off:

- With progressive-frame media, switching this checkbox on serves no purpose. It only pads processing time needlessly.
- If you've got interlaced clips inside a progressive-frame project and you mean to deinterlace them with the Enable Deinterlacing checkbox in the Clip Attributes window, then "Enable video field processing" has to stay off. If not, the Enable Deinterlacing checkbox goes disabled for every clip.

For more on deinterlacing clips, turn to Chapter 22, "Modifying Clips and Clip Attributes." On a project whose interlaced media you plan to keep interlaced, whether you even need field processing on hinges on the kinds of corrections you put on your clips. When you're mastering your program to an interlaced format and applying any adjustment that would push or smear pixels from one field into neighboring fields, field processing ought to be on; effects that demand it include filtering work such as blur, sharpen, and OpenFX operations, plus sizing transforms covering pan, tilt, zoom, rotate, pitch, and yaw. By contrast, no matter whether your output is interlaced or progressive-frame, when you aren't filtering or resizing clips and you're only tweaking color and contrast, field processing isn't needed on interlaced material, and indeed leaving it off may trim your project's rendering time a little.

- Align Clips to Frame Boundaries: With interlaced material, you get to decide whether edits land on field or frame boundaries. Tick it and every editing action and playhead step happens on full frame boundaries. Since this runs apart from the audio subframe controls, flawless audio sync is still attainable while you handle video at the frame level. Leave it unticked and every editing action and playhead step instead happens on the field boundary.
- Playback frame rate: Normally tracks the frame rate chosen in the "Video format" setting (down in the Video Monitoring section), which itself usually follows the frame rate of the external display wired to your video interface, given the "Timeline Frame Rate" setting. A 50Hz monitor, for one, needs a 25 fps playback frame rate to display in sync without dropping frames. To monitor playback at a lower frame rate, enter the frame rate you want in this field and DaVinci Resolve runs the math to drop or repeat frames as required to hit it. That's handy for briefly checking how clips read in slow motion.
