# Conforming otio files and more about conforming otio files

Version: DaVinci Resolve 20.3 Reference Manual. Context: Conforming overview.
[Chapter index](INDEX.md) / [Next section](conforming-adl-files-and-more-about-conforming-adl-files.md)
<a id="source-conforming-otio-files"></a> <a id="source-conforming-otio-files-1"></a> <a id="source-conforming-otio-files-conforming-adl-files"></a> <a id="source-importing-otio-project-files"></a> <a id="source-importing-otioz-files"></a> <a id="source-more-about-conforming-otio-files"></a> <a id="source-overview"></a>

## Overview

Covers: Conforming OTIO Files; Conforming ADL Files.

## Conforming OTIO Files

### Conforming OTIO Files

Every workflow for bringing in and conforming timelines by way of the .otio and .otioz formats is what this chapter walks through.

### More About Conforming OTIO Files

For passing timelines back and forth between applications, DaVinci Resolve handles the Open Timeline IO (OTIO) format on both import and export. OTIO is an open source interchange format for media and timelines, the work of the Academy Software Foundation. Built to stay neutral toward any application or platform, it carries your timeline and its media assets from one program to another with broader compatibility than either AAF or XML offers. Putting out an OTIO for DaVinci Resolve to use is uncomplicated, and aside from settling on whether you want just the Timeline exported (.otio) or the Timeline together with every associated media file (.otioz), there really aren’t settings to fuss over on export. DaVinci Resolve recognizes two distinct OTIO formats .otio: A file of this kind holds nothing but the timeline’s metadata, with no media attached. Such files stay small and easy to move around, and they leave it to the recipient to hook the Timeline up to their own copies of the media. .otioz: A bundle file of this kind wraps the Timeline metadata together with all of the Timeline’s media assets, zipped up into a single file. That can make the file enormous, since it carries the full-length media of every asset the Timeline draws on. The trade-off is that anyone importing it receives all the needed media, automatically linked, so the Timeline can be recreated on their system.

### Importing OTIO Project Files

A far closer look at the Import OTIO dialog is what this section provides. A single procedure carries you through any of these workflows:

- Bringing in an .otioz file together with its associated media, automatically.
- Bringing in an .otio file and conforming to plus importing the media it points at, automatically.
- Bringing in an .otio file while hand-picking a different set of media — presumably at another

format or resolution, but carrying identical metadata — to conform to in its place.

- Bringing in an .otio file tied to offline media that traces back to a camera original format, and

conforming it to plus importing the camera original media automatically. By way of the Timeline Import dialog you can pick several XML, AAF, FCP XML, or EDL timelines at once (or any mix of them). Those chosen timelines come in one after another, halting each time you press the OK button so you can set separate Import Settings per timeline. Picking the right blend of options — every one of which the procedure below spells out — is what makes each of these workflows possible. Here’s how to bring an OTIO file in and have it link itself to the media it references: 1 Take either of these routes:

- From any page, choose File > Import Timeline (Shift-Command-I).
- Head into the Edit page, right-click somewhere within the Media Pool, then go to Timelines > Import >

AAF/EDL/XML/DRT/ADL/OTIO. 2 In the file dialog that comes up, locate the project file you mean to import, highlight it, and click the Open button. Depending on what you picked, the Load OTIO window then opens.

Options when importing an .otio file 3 Pick whichever options fit your particular project. Out of the box, those options take their cue from the metadata held inside the file you chose.

- Source file: Whatever file you highlighted back in the previous step.
- Timeline name: The label for the Timeline you’re on the verge of creating. By default it echoes the name of

the exported sequence, though you’re welcome to rename it.

- Timeline start timecode: The timecode where the imported timeline kicks off. This

falls into line automatically with the start timecode of the selected Import Timeline.

- Automatically set project settings: Keep this option on so the frame size

and frame rate values in the Project tab of the Config page get swapped for the ones in this window. Timelines whose frame rates differ from the Project frame rate can still be imported.

- Automatically import source clips into media pool: Keep this checkbox on so the media the OTIO project file you chose points at gets pulled into the Media Pool, going by the embedded file paths. Should those media files not turn up automatically at those spots, you’ll be asked to point manually at a directory holding the clips.

Ignore file extensions when matching: Switch this checkbox on when you’d rather hand-pick a different media directory to link against. Say the OTIO you’re importing points at ProRes Proxy media and you want to relink to a separate directory of matching ProRes 4444 or camera raw media.

- Import multi-channel audio tracks as linked groups: Flip this checkbox on when you want multi-channel audio — stereo, 5.1, and 7.1, for instance — brought in as separate mono timeline tracks bound together on the Fairlight page.

Further detail on Linked Groups lives in Chapter 171, “Setting Up Tracks, Busses, and Patching.” Leave this checkbox off and multi-channel audio comes in as multi-channel audio tracks within the Timeline instead.

- Set timeline resolution to: A pair of fields where you state the width and height of the frame size you intend to work at inside DaVinci Resolve. By default it takes on whatever resolution the imported OTIO file specifies.
- Timeline frame rate: By default this is taken from the frame rate of the OTIO file being imported. Should you import an OTIO file into a project whose Media Pool already holds media, the Timeline frame rate locks and can’t be altered.
- Use drop frame timecode: By default this is taken from the OTIO file being imported.
- EDL frame rate: By default this is taken from the frame rate of the selected file.
- Use drop frame timecode: By default this is taken from the frame rate of the selected file.
- Mixed frame rate format: This pop-up menu is where you settle on the method used to conform mixed

frame rates for rendering and playback. The “Final Cut Pro 7” or “Final Cut Pro X” conform methods are available, whereas for projects brought over from Media Composer, Premiere Pro, Smoke, or other NLEs, you’ll want to keep this on “DaVinci Resolve.” This same pop-up menu turns up in the Load OTIO dialogs whenever you import a project. 4 Once every needed setting is chosen, click Ok. 5 Assuming “Automatically import source clips into media pool,” stayed switched on, then should the OTIO file’s linked media be missing from the disk spot it was expected at — or should you have ticked the “Ignore file extensions when matching” checkbox — yet another dialog surfaces, asking which folder this project’s media sits in. Do one of the following:

- Should you wish to attempt a relink to media at some other disk spot: Click Yes, then steer to the folder that holds your media (its subfolders all get traversed automatically too), highlight it, and click OK.
- Should you instead wish to bring the Timeline in with every clip left offline: Click No.

A prompt appears if all the media was not found. IMPORTANT: You can always point at the top level of a volume to sweep up every bit of media across the directories it contains, yet on a large volume packed with countless files, combing through every folder and document on it can turn into an extraordinarily time‑intensive process. 6 Should you have clicked Yes to picking a different folder, then turn to the folder selection dialog, steer to another folder, and click Ok. Repeat this loop as often as it takes until every piece of media that timeline links to has been located.

Selecting the source folder for your OTIO imported clips With that, the OTIO file comes in. A fresh Timeline plus the referenced media files show up in the Media Pool, and the Timeline opens so its contents are in view. Any clip that couldn’t be matched to a file on disk shows up red across both the Media Pool and the Timeline, flagging it as offline and unlinked. TIP: Pull up the Edit Index and pick Filter Offline Clips from the option menu to get a rundown of every offline clip in the current Timeline.

### Importing .otioz Files

Importing .otioz files follows the same path as above, with this one wrinkle: when an .otioz file is the one chosen for import, its media assets unpack themselves into a folder right beside the .otioz file and link up on their own. Be sure you’ve got the room for it.
