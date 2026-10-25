# Conforming clips during xml and aaf import and when importing clips with different file extensions

Version: DaVinci Resolve 20.3 Reference Manual. Context: Conforming and relinking clips.
[Chapter index](INDEX.md) / [Previous section](project-import-conforming-and-relinking.md) / [Next section](media-pool-metadata-and-reel-names.md)
<a id="source-conforming-and-relinking-clips-part-2"></a> <a id="source-conforming-clips-during-xml-and-aaf-import"></a> <a id="source-essential-clip-metadata-for-easy-conforming-and-relinking"></a> <a id="source-importing-clips-before-importing-an-edl-aaf-or-xml"></a> <a id="source-when-importing-clips-with-different-file-extensions"></a>

### Conforming Clips During XML and AAF Import

In workflows where you bring in AAF or XML projects and then relink the resulting DaVinci Resolve clips to media files sitting on disk, or conform them to clips already present in the Media Pool, the way clip metadata is set for reconforming hinges on a pair of toggles found within the Load AAF or XML dialog. Those toggles are "Automatically import source clips into media pool," along with "Ignore file extensions when matching."

The most important settings for conforming media in the Load dialog How these two checkboxes work together to govern the way media gets conformed to an imported AAF or XML file is intricate, but the rules follow. Bringing In Clips Whose File Extensions Agree With the Ones Cited by Your AAF or XML File Switch "Automatically Import" on and "Ignore file extensions" off. This is the default arrangement, and it serves best when the AAF or XML file you're importing references media you'd like to bring into the Media Pool and put to use.

- First, where clips already populate the Media Pool, DaVinci Resolve attempts to conform as many of them as it can by lining up the file paths inside the AAF or XML file with each Media Pool clip's stored file paths.
- Second, for every clip still not located, DaVinci Resolve brings in as many clips as it can into the Media Pool from whatever storage volumes are visible to DaVinci Resolve, drawing on the file paths held in the XML or AAF.
- Third, for every clip still not located, DaVinci Resolve attempts a clip name match against the clips already in the Media Pool.
- Fourth, for every clip still not located, DaVinci Resolve attempts a timecode match (paired with a reel name match where that's enabled) against the clips already in the Media Pool.
- Finally, for every clip still not located, the user gets prompted to pick another folder to search by hand.

### When Importing Clips With Different File Extensions

Switch "Automatically import" on and "Ignore file extensions" on. Switching both of these options on serves you well where the sequence you're importing was first cut with offline-quality media, and you now want to conform to high-quality online media in an utterly different format, perhaps in the Media Pool, perhaps on a separate disk. One example of

such a case arises when the cut was assembled from QuickTime or Avid DNxHD media, yet your reconform now points at Blackmagic RAW files held on a separate disk so the camera original raw media can be graded. Here you keep "Automatically import source clips into media pool" switched on.

- First, where clips already populate the Media Pool, DaVinci Resolve attempts to conform as many of them as it can by lining up clip names.
- Second, for every clip still not located, the user gets prompted to pick another folder to search, and DaVinci Resolve brings in as many clips as it can by lining up clip names, paying no heed to file extensions.
- Third, for every clip still not located, DaVinci Resolve attempts a timecode match (plus a reel name match where that's enabled within the General Options panel of the Project Settings) against the clips already sitting in the Media Pool.
- Fourth, for every clip still not located, the user gets prompted to pick another folder to search by hand.

Switch "Automatically import" on, and likewise turn "Link to source camera files" on. That "Link to source camera files" checkbox shows up only where you bring in AAF files. Switching this option on while automatically importing media ties the imported project back to the original camera source files that Media Composer/Symphony keeps tabs on through the "Source Name" metadata held inside the AAF file. Relinking Solely Against Clips That Already Sit in Your Media Pool Switch "Automatically import" off. Switching "Automatically Import source clips into media pool" off serves you well where the only thing you want is to conform the imported AAF or XML to the clips already in the Media Pool. This helps most where you've first brought all the camera original media into the Media Pool, say while building the dailies that were subsequently cut, and you'd like to conform the imported AAF or XML to the media that already sits there.

- First, where clips already populate the Media Pool, DaVinci Resolve attempts to conform as many of them as it can by lining up the file paths inside the XML or AAF with the file paths stored against each Media Pool clip.
- Second, for every clip still not located, DaVinci Resolve attempts a clip name match against the clips already in the Media Pool.
- Third, for every clip still not located, DaVinci Resolve attempts a timecode match (paired with a reel name match where that's enabled) against the clips already sitting in the Media Pool. Here the file name plays no part.

Beware When Choosing a Volume or Folder to Search Once prompted to choose a search folder, you may optionally settle on a whole volume; DaVinci Resolve always sweeps through every subdirectory, and in time every media item on that volume turns up. That said, depending on how big and how numerous the files on the chosen volume are, the operation might drag on far longer than anticipated, particularly on a SAN volume.

### Importing Clips Before Importing an EDL, AAF, or XML

Bringing media in ahead of importing an EDL has DaVinci Resolve follow a defined set of rules to work out which Media Pool clips line up with clips in the timeline that results. The same rules hold where you've brought media in ahead of importing an AAF or XML file, in cases where you'd rather give particular media precedence over the file paths baked into those imported timeline formats. The sections that follow dig into exactly what these rules are and how to turn them to your advantage.

### Essential Clip Metadata for Easy Conforming and Relinking

As you conform projects within DaVinci Resolve, the precision and soundness of clip metadata makes or breaks the outcome. Bear the following three criteria in mind while you ready media for use within DaVinci Resolve.

- Accurate timecode: Vital for every clip. To start with, each clip ought to carry a valid timecode track, and — it hardly needs saying — that timecode should line up with the timecode borne by every other instance of the same media file within a given project. Where a clip’s timecode gives trouble, DaVinci Resolve offers tools for editing or offsetting timecode to allow for known discrepancies. Out of the box, the “Use Timecode” project setting reads “Embedded in the Source Clip,” so timecode is drawn from the embedded timecode track within a QuickTime file or an MXF file, or else out of a DPX frame file’s header data. You may instead pick the “From the source clip frame count” option, which lets timecode be taken from the Source clip’s frame count for image sequences.
- File names: With the “Assist using Reel Names” checkbox — found within the General Options panel of the Project Settings — switched off (its default), DaVinci Resolve is compelled to conform clips by file name as it brings in XML and AAF projects. File names come into play solely when conforming XML or AAF files, or when importing a DaVinci project; they are never used when conforming EDLs.
- Reel Name: Enters the conform process only when “Assist using Reel Names” sits on in the General Options panel of the Project Settings. Tagging your media with reel names is not mandatory, though it is advised, and it can smooth media management for certain operations — EDL workflows above all. Still, if conforming clips gives you grief while “Assist using Reel Names” is on, switching it off makes a sensible first troubleshooting move.

The way DaVinci Resolve pairs media files with clips in an imported project hinges on the manner in which you bring that project in.
