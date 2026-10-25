# Conforming xml files and more about conforming xml files

Version: DaVinci Resolve 20.3 Reference Manual. Context: Conforming overview.
[Chapter index](INDEX.md) / [Previous section](digital-dailies-ingest-and-edit-metadata.md)
<a id="source-conforming-xml-files"></a> <a id="source-conforming-xml-files-1"></a> <a id="source-importing-xml-project-files"></a> <a id="source-manage-your-media-before-exporting-an-xml"></a> <a id="source-more-about-conforming-xml-files"></a>

## Conforming XML Files

### Conforming XML Files

Among the simplest ways to move edits carrying as many video tracks as you need out of various NLEs and into DaVinci Resolve is XML. A bonus of XML import is that an assortment of supported effects can come across alongside the edit data, together with several tracks of video. The pages here describe the fairly easy procedure for importing XML projects into DaVinci Resolve. It might be a one-way trip, where you finish the project inside DaVinci Resolve, or part of a round-trip, where you head back to the originating NLE to finish. XML round-trip workflows are reasonably simple; if you need detail on exporting individual clips, look to Chapter 187, “Rendering Media.”

### More About Conforming XML Files

Projects exported in the Final Cut Pro 7 or Final Cut Pro X XML formats can be brought into DaVinci Resolve. Adobe’s Premiere Pro along with Autodesk Smoke and Flame Premium can likewise tap the Final Cut Pro XML project exchange format for round-trip workflows. For the cleanest results, though, make sure the XML you write comes out of Premiere Pro version 5.5.1 or a later build — and preferably from the most current Premiere Pro release you can run. Producing XML for DaVinci Resolve is simple, and beyond choosing which XML version to write, there really isn’t much to configure when exporting an XML file. Because of that, it’s wise to finish any timeline and/or media management you need before you export the XML.

### Manage Your Media Before Exporting an XML

When you’re bringing in XML or AAF projects (or even EDLs), relinking and conforming to the accompanying media files goes most smoothly if every file sits under one directory path. Spreading media across several directories is fine too, provided they all live within one parent directory you can point to at the right step of project import.

### Importing XML Project Files

Here we look at the Import AAF/EDL/XML dialog in far greater depth. A single procedure can carry out any of these workflows:

- Bringing in an XML file while automatically conforming to, and importing, the media it references.
- Importing an XML file while hand-picking a separate set of media instead, presumably in a different

format or resolution, with identical metadata, to conform to instead.

- Importing an XML file linked to offline media derived from a camera original format, and

automatically conforming it to and importing the camera original media. You reach each of these workflows by selecting the right mix of options, all of them explained in the procedure that follows. Using the Timeline Import dialog, you can pick several XML, AAF, FCP XML, or EDL timelines together (in any combination). Those chosen timelines import one after another, pausing each time you press the OK button so you can set separate Import Settings per timeline. To bring in an XML file and have it link up to its referenced media on its own: 1 Take one of these actions:

- On any page, choose File > Import Timeline (Shift-Command-I).
- Go to the Edit page, right-click anywhere within the Media Pool, and pick Timelines >

Import > AAF/EDL/XML/DRT/ADL/OTIO. 2 In the file dialog that opens, locate the project file you want and click it to open. Depending on what you chose, the Load XML window appears.

Options when importing an XML file 3 Set the options that suit your particular project. These default to values drawn from metadata inside the file you picked.

- Source file: Whatever file you chose during the prior step.
- Import timeline: When the selected XML source file holds more than one sequence, this pop-up

menu is where you pick which of those sequences becomes the imported DaVinci Resolve timeline.

- Timeline name: The label for the Timeline you’re creating. It starts out matching the name of the exported sequence, though you’re free to rename it.
- Master timeline start timecode: The timecode where the imported timeline begins. This is set automatically to the start timecode of the selected Import Timeline.
- Automatically set project settings: Keep this on so the frame size and frame rate in the Project tab of the Config page are updated automatically from the values shown in this window. Timelines whose frame rates differ from the Project frame rate can still be imported.
- Automatically import source clips into media pool: Keep this checkbox on so the media that the chosen XML project file points to is brought into the Media Pool automatically using the embedded file paths. Should the media not turn up at those locations on its own, you’ll be asked to pick a directory that holds the clips by hand.

Ignore file extensions when matching: Switch this checkbox on when you’d rather hand-pick a different media directory to link against — say the incoming XML references ProRes Proxy media yet you’d like to point instead at a separate directory holding the equivalent ProRes 4444 or camera raw media.

- Use sizing information: Brings in position, scale, and rotation transforms from the source NLE by way of the imported XML project file. Those transforms live in each clip’s settings within the Edit page Inspector.
- Use color information: Applies to Final Cut Pro X XML files only. With it, you can pull in a portion of the color correction data from the Final Cut Pro X color board controls.
- Import multi-channel audio tracks as linked groups: Enable this checkbox when you want multi-channel audio — stereo, 5.1, and 7.1, for example — brought in as separate mono timeline tracks that are linked together on the Fairlight page.

To read more on Linked Groups, head to Chapter 171, “Setting Up Tracks, Busses, and Patching.” Leaving this checkbox off causes multi-channel audio to come in as multi-channel audio tracks in the Timeline instead.

- Set timeline resolution to: A pair of fields where you enter the width and height of the frame size you intend to work at inside DaVinci Resolve. It defaults to whatever resolution the imported XML file specifies.
- Timeline frame rate: By default this comes from the frame rate of the XML file you’re importing. When you import an XML file into a project whose Media Pool already holds media, the Timeline frame rate is locked and can’t be altered.
- Use drop frame timecode: By default this comes from the XML file being imported.
- EDL frame rate: By default this comes from the frame rate of the chosen file.
- Use drop frame timecode: By default this comes from the frame rate of the chosen file.
- Mixed frame rate format: From this pop-up menu you select the method used to conform

mixed frame rates during rendering and playback. The “Final Cut Pro 7” or “Final Cut Pro X” conform methods are available, but for projects coming from Media Composer, Premiere Pro, Smoke, or other NLEs, keep it set to “DaVinci Resolve.” The same pop-up menu also shows up in the Load XML dialogs as you import a project. 4 Once all the needed settings are in place, click OK. 5 Provided you kept “Automatically import source clips into media pool,” turned on, then if the media the XML file references isn’t at the expected disk location, or if you ticked the “Ignore file extensions when matching” checkbox, a further dialog opens asking you to point to the folder where this project’s media lives. Do one of the following:

- If you’d like to attempt relinking to media at a different disk location: Click Yes, then browse to the folder that holds your media (every subfolder gets scanned too), select it, and click OK.
- If you’d simply like to bring the Timeline in with every clip offline: Click No.

A prompt appears if all the media was not found

IMPORTANT: You can always point to the top level of any volume so all media in any directories beneath it is found automatically, but on a large volume packed with files, combing through every folder and document on it can take an extremely long time. 6 If you clicked Yes to pick another folder, use the folder selection dialog to browse to a different folder and click Ok. Repeat this cycle as many times as necessary until every piece of media the timeline links to has been located.

Selecting the source folder for your XML imported clips With that done, the XML file comes in. A fresh timeline together with the referenced media files shows up in the Media Pool, and the Timeline opens so you can view its contents. Any clips that couldn’t be matched to a file on disk show up red in both the Media Pool and Timeline, marking them as offline and unlinked. TIP: Opening the Edit Index and picking Filter Offline Clips from its option menu surfaces a roster of every offline clip in the Timeline you’re working on.
