# Grading windows and a convergence adjusted window in stereo

Version: DaVinci Resolve 20.3 Reference Manual. Context: Stereoscopic workflows.
[Chapter index](INDEX.md) / [Previous section](stereo-clip-generation-and-optimized-media.md) / [Next section](grading-mastered-stereoscopic-media-from-tape.md)
<a id="source-a-convergence-adjusted-window-in-stereo"></a> <a id="source-conforming-projects-to-stereo-3d-media"></a> <a id="source-grading-windows"></a> <a id="source-matching-media-from-left-and-right-eyes"></a> <a id="source-step-5--output-offline-or-online-media-for-editing"></a>

### Grading Windows

When you work with windows, look inside the Project Settings, within its General Options panel, where the Color group carries a checkbox labeled “Apply stereoscopic convergence to windows and effects” that holds a window’s position correctly — once it’s been placed properly over each eye — as convergence changes.

A checkbox in the Project Settings has to be enabled before stereo convergence applies to windows With that option active, the Window palette gains an extra Transform parameter, “Convergence,” which lets you build correctly aligned convergence for a window set onto a stereoscopic 3D clip.

The Convergence control in the Transform section of the Window palette

Once you’ve set a window over some feature in the image while watching a single eye, turn on Stereo output in the Stereo 3D palette and work the Pan and Convergence controls so that window sits in correct stereo alignment over that same feature in both eyes. From there, moving the Convergence control in the Stereo 3D palette keeps the window’s position right within each eye’s grade.

### A convergence-adjusted window in stereo

### Matching Media From Left and Right Eyes

To help you cope with the visual gaps between left- and right-eye clips, three automatic color matching commands are on hand that can batch process however many clips you need to fix in one go.

- Stereo Color Match (Primary Controls): Relies on the Lift/Gamma/Gain controls to bring one eye into agreement with the other. It’s a straightforward, easily customized adjustment, though in certain cases it won’t do as well as Custom Curves.
- Stereo Color Match (Custom Curves): Leans on the Custom Curves to build a multipoint adjustment matching one eye to the other. It can do better on tougher shots.
- Stereo Color Match (Dense Color Match): Runs a pixel-by-pixel, frame-by-frame color match of remarkable accuracy. The process is heavy on the processor, so when you plan to batch process numerous clips, or to match lengthy ones, make sure you’ve allowed enough time. Given how exact this match is, the advice is to run Dense Color Match only after you’ve applied one of the stereo alignment commands.

Controls for matching the grade of the left and right eye media

### Step 5 – Output Offline or Online Media for Editing

Once you’ve finished whatever grading the media needs to become suitable for editing, you’ll export each clip as separate left- and right-eye clips by way of the Deliver page controls. 1 Open the Deliver page and configure your render to output the media format you need. Make sure to do the following:

- Set Render Timeline As to Individual source clips.
- Switch on the “Filename uses Source Name” checkbox.
- To render media for both eyes, select “Both eyes as” from the Render Stereoscopic 3D option and select Separate Files in the pop-up menu beside it. If you prefer, you can instead render only the left-eye or right-eye media.

2 Decide how much of the Timeline to render through the Render pop-up menu in the Timeline toolbar; pick Entire Timeline to do the whole thing. 3 Click “Add Job to Render Queue.” 4 Click Start Render. At this point DaVinci Resolve renders either two sets of left- and right-eye clips or a single set of media for the eye you picked. So that the edited project conforms back to the originating DaVinci Resolve project without trouble, it’s vital to render individual source clips and to enable the “Filename user Source Name” checkbox, which reproduces the timecode, reel numbers, and file names of the source media.

### Conforming Projects to Stereo 3D Media

Because DaVinci Resolve handles stereo through one set of purpose-built stereo 3D clips, you import stereo 3D projects with the very same import methods you’d use on any other project. Just one imported timeline is required. It also follows that you can cut stereo projects in NLEs that have no stereo awareness and then finish them in full stereo 3D within DaVinci Resolve. For that, be sure to edit the left-eye media in your NLE and afterward export either an EDL or XML file to conform inside DaVinci Resolve. Conforming an EDL against stereo 3D media goes like this: 1 On the Media page, build the needed set of stereo 3D clips that will line up with the project you’re about to import, following the earlier description. Open the Edit page, then run the Import AAF/EDL/XML command to bring in your edit. 2 Once the Load EDL/XML dialog opens, do the following:

- When importing an EDL, confirm the frame rate is right, then click OK.
- When importing XML, be sure to clear the “Automatically import source clips into

Media Pool” checkbox, because you want the imported project relinked to the stereo 3D clips you made back in step one. The left-eye media timecode and reel data baked into each stereo 3D clip is what conforms the stereo 3D clips against the imported EDL, after which you should be set to work.
