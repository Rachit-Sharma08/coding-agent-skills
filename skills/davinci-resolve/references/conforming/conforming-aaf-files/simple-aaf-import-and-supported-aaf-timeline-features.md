# Simple aaf import and supported aaf timeline features

Version: DaVinci Resolve 20.3 Reference Manual. Context: Conforming aaf files.
[Chapter index](INDEX.md) / [Previous section](aaf-media-and-dnxhd-dnxhr-transcoding.md) / [Next section](avid-aaf-roundtrip-project-setup.md)
<a id="source-simple-aaf-import"></a> <a id="source-supported-aaf-timeline-features"></a>

### Simple AAF Import

A far more detailed look at the Import AAF, EDL, XML dialog occupies this section. A single procedure lets you carry out any of the workflows below:

- Bringing in an AAF file and having it automatically conform to and import the media it links to.
- Bringing in an AAF file and hand-picking a different batch of media, presumably at a different

format or resolution, carrying matching metadata, to conform against instead.

- Bringing in an AAF file linked to offline media that was derived from a camera original format,

and having it automatically conform to and import the camera original media. Through the Timeline Import dialog you can pick several XML, AAF, FCP XML, or EDL timelines (or any mixture of them) all at once. The chosen timelines import one after another, pausing each time once the OK button has been pressed, which lets you set separate Import Settings per timeline. Every one of these workflows becomes possible once you select the right blend of options, all of which the procedure below spells out. To bring in an AAF file and link automatically to its referenced media: 1 Do one of the following:

- From any page, choose File > Import Timeline (Shift-Command-I).
- Head to the Edit page, right-click somewhere within the Media Pool, then pick Timelines >

Import > AAF/EDL/XML/DRT/ADL/OTIO.

2 With the file dialog that comes up, locate the project file you wish to bring in, and click it to open. Depending on what you picked, the Load AAF window comes up.

Options when importing an AAF file 3 Pick whichever options suit your particular project. Out of the box, these options derive from metadata held within the file you selected.

- Source file: The file you selected in the previous step.
- Import timeline: Should the chosen AAF source file hold several sequences, this pop-up

menu lets you decide which sequence comes in as a DaVinci Resolve timeline.

- Timeline name: The name carried by the Timeline you're on the verge of creating. This defaults to the name of

the sequence that was exported, though you may rename it if you wish.

- Master timeline start timecode: The timecode where the imported timeline gets going. This

falls automatically in line with the start timecode of the chosen Import Timeline.

- Automatically set project settings: Keep this option enabled to have the frame size

and frame rate settings in the Project tab of the Config page automatically updated to match the ones in this window. Timelines whose frame rates differ from the Project frame rate can still be imported.

- Automatically import source clips into media pool: Keep this checkbox enabled so the media referenced by the AAF project file you chose is automatically brought into the Media Pool according to the embedded file paths. Should the media files not turn up automatically at those spots, you'll be asked to pick a directory by hand where the clips reside.

Ignore file extensions when matching: Switch this checkbox on whenever you wish to hand-pick a separate directory of media to link against; for instance, when the AAF you're bringing in links to ProRes Proxy media and you wish to relink to a separate directory of matching ProRes 4444 or camera raw media.

- Use sizing information: Lets you bring in position, scale, and rotation transforms out of the originating NLE by way of the imported AAF project file. Each clip's settings in the Edit page Inspector hold these transforms.
- Import log messages as COLOR markers: Switch this checkbox on and pick a color out of the attached drop-down menu for markers that will land on the Timeline carrying note text that describes import errors you may want to look into later.
- Import multi-channel audio tracks as linked groups: Switch this checkbox on whenever multi-channel audio such as stereo, 5.1, and 7.1 should arrive as separate mono timeline tracks bound to one another inside the Fairlight page.

To learn more about Linked Groups, refer to Chapter 171, “Setting Up Tracks, Busses, and Patching.” With this checkbox switched off, multi-channel audio comes into multi-channel audio tracks on the Timeline.

- Import AAF to current timeline: Brings the AAF into the Timeline currently loaded, rather than building a fresh timeline in the Media Pool.

Insert Additional Tracks: Hands fresh tracks to the Timeline automatically, keeping the AAF referenced media from writing over clips that already sit on the existing timeline. Insert with offset: Writes the AAF referenced media onto the Timeline, then nudges it along by whatever amount you've set using timecode format.

- Set timeline resolution to: A pair of fields let you state the width and height of the frame size you wish to work at within DaVinci Resolve. The default amounts to whatever resolution is named in the AAF file being imported.
- Timeline frame rate: By default this comes from the frame rate of the AAF file being imported. When you bring an AAF file into a project that already holds media in the Media Pool, the Timeline frame rate gets locked and can't be altered.
- Use drop frame timecode: As a default, this gets taken from whichever AAF file is being imported.
- EDL frame rate: As a default, this gets taken from the frame rate carried by the chosen file.
- Use drop frame timecode: As a default, this gets pulled from the frame rate carried by the chosen file.
- Mixed frame rate format: Through this drop-down menu you pick the method that conforms

mixed frame rates for rendering and playback. The “Final Cut Pro 7” or “Final Cut Pro X” conform methods are selectable, whereas for projects brought in out of Media Composer, Premiere Pro, Smoke, or other NLEs, you ought to leave it set to “DaVinci Resolve.” That same drop-down menu turns up within the Load AAF dialogs while you import a project. 4 Once every needed setting is chosen, click OK.

5 Provided you kept “Automatically import source clips into media pool,” enabled, then if the media that the AAF file links to isn't sitting at the expected disk location, or if you switched on the “Ignore file extensions when matching” checkbox, a further dialog comes up asking you to pick the folder holding the media for this project. Do one of the following: Should you wish to attempt relinking to media sitting at a different disk location: Click Yes, then navigate over to the folder housing your media (every subfolder gets walked automatically as well), highlight it, and click OK. Should you instead wish to merely bring in the Timeline carrying every offline clip: Click No.

A prompt appears if all the media was not found IMPORTANT: You can always pick the top level of any volume so that all media in any directories nested within gets found automatically, but should the volume be large and packed with many files, sweeping every folder and document on the volume can turn into a remarkably timeintensive process. 6 If you clicked Yes to picking another folder, then work the folder selection dialog to browse to a different folder, and click Ok. Repeat this cycle as many rounds as you require until you've located every piece of media that timeline links to.

Picking the source folder that holds the clips your AAF brought in. The import of the AAF file completes. A fresh timeline alongside the referenced media files turns up in the Media Pool, and the Timeline opens up so its contents are visible to you. Straightforward nested clips ought to come across as well. Any clips that couldn't be linked to a matching file on disk show up red in both the Media Pool and Timeline to signal that they're offline and unlinked.

TIP: By opening the Edit Index and picking Filter Offline Clips out of the option menu, you can view a list of every offline clip on the current Timeline.

### Supported AAF Timeline Features

The extra AAF timeline information listed below gets brought into DaVinci Resolve automatically:

- Timeline Markers: Whatever timeline markers sit inside the AAF get imported. Timeline markers can likewise be written out of DaVinci Resolve to AAF for round-trip workflows.
- Nested Clips: AAF files carrying simple nested clips will be imported by DaVinci Resolve.
- Boris Continuum FX: The effects and settings of Boris Continuum FX get brought in together with a timeline through AAF export. The same Continuum suite of effects has to be installed on both machines (the OFX version for DaVinci Resolve, AVX for Avid). Upon importing an AAF, the Boris Continuum effects applied in the original NLE turn up on every affected clip within the resulting DaVinci Resolve timeline, with every parameter you'd applied earlier on hand in the Inspector. For now, the Sapphire and Mocha suites can't be imported through AAF.
