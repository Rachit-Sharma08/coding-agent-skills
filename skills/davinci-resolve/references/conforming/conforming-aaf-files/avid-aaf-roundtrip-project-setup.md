# Performing an aaf avid round trip and step 1create a project in media composer

Version: DaVinci Resolve 20.3 Reference Manual. Context: Conforming aaf files.
[Chapter index](INDEX.md) / [Previous section](simple-aaf-import-and-supported-aaf-timeline-features.md) / [Next section](graded-aaf-export-and-avid-relinking.md)
<a id="source-conforming-aaf-files-part-2"></a> <a id="source-load-aaf-window-conform-options"></a> <a id="source-load-aaf-window-conform-options-1"></a> <a id="source-performing-an-aaf-avid-round-trip"></a> <a id="source-step-1create-a-project-in-media-composer"></a> <a id="source-step-2exporting-an-aaf-for-davinci-resolve"></a> <a id="source-step-3conforming-your-aaf-in-davinci-resolve"></a>

### Performing an AAF Avid Round Trip

A thorough workflow for building projects in Media Composer that will work with DaVinci Resolve, carrying projects from Media Composer into DaVinci Resolve, then grading, rendering, and returning the finished graded project to Media Composer, is laid out in this section. The procedures within the steps below address these tasks:

- Bringing in all media as high quality MXF-wrapped DNxHD, then round tripping out of Media Composer into DaVinci Resolve.
- Bringing in and editing Resolve-compatible AMA-linked media formats, then round tripping out of Media Composer into DaVInci Resolve.
- Converting AMA-linked media files down to offline-quality DNxHD clips so you can edit, after which an AAF file gets written out and reconformed within DaVinci Resolve against high quality camera original media over the course of the round trip.

Since there are so many ways that Media Composer is able to ingest media and produce AAF projects, acquaint yourself with the procedures that follow before you press on with a project of your own.

### Step 1–Create a Project in Media Composer

1 As you build a project in Media Composer, note the image format details, since these ought to be matched within DaVinci Resolve. Specifically, set the image format (e.g., 1080p/24) along with the raster dimensions (e.g., 1920x1080) to fit the mastering format you're after. As well, color space ought to be set to RGB 709 when you plan on sending ingested/transcoded media out of Media Composer into DaVinci Resolve for grading. NOTE: The Avid Project Format tab can also surface this information.

2 Open your project and bring all the media you need into a fresh bin using one or both of the approaches below: Transcode media for editing: For AAF import and round-trip workflows, the most straightforward path is to ingest transcoded, native MXF-wrapped DNxHD media by way of the Import command. Import AMA-linked clips: AMA-linked clips can be imported as well, provided every AMA-linked file sits in a format that works with DaVinci Resolve. Bear in mind that Media Composer cannot consolidate every AMA-compatible format. Here, bring AMA-linked media into a fresh bin through the Link to AMA File(s) command, and edit as you normally would. After every needed piece of media is ingested, you can edit your project just as you would any other, while staying mindful of which effects work with DaVinci Resolve. To learn more about effects across Media Composer to DaVinci Resolve round trips, refer to Chapter 55, “Preparing Timelines for Import and Comparison.”

### Step 2–Exporting an AAF for DaVinci Resolve

After you wrap up editing, you have to write out an AAF that will conform the .mxf media you worked with in Media Composer into a DaVinci Resolve timeline. Depending on whether DaVinci Resolve and Media Composer sit on the same system, two export configuration options exist. 1 Pick the sequence you wish to export, and choose File > Output > Export to File. 2 Within the Export As dialog, key in a name for the AAF file you're about to write out. 3 Pick a place to store the AAF. You may keep it wherever you like, but should you be carrying the project to another workstation, you might wish to store it within a specific folder on a removable hard drive where you keep your AAF and XML files. The spot you settle on can double as the location of the media that gets exported alongside the AAF. 4 Click the Options button to bring up a fuller window of export settings. 5 Switch on the AAF Edit Protocol checkbox. With this option, Media Composer is compelled to write a simplified AAF file that meshes better with the project exchange workflows of various applications. 6 Pick the suitable option out of the Export Method pop-up menu to set how the AAF and the media accompanying it get exported. Your pick hinges on this: Where both Media Composer plus DaVinci Resolve live on a single system: Choose “Link to (Don't Export) Media” so the AAF file you write links back to media that already sits at its current spot. Open the Audio Details tab, then pick “Link to (Don't Export) Media” out of the Export Method pop-up menu. Where Media Composer and DaVinci Resolve instead live on separate systems: pick whichever of these two export methods fits: Copy All Media: For every source clip you've used, its entire matching media file gets duplicated. This can come in handy when you wish to keep the original tie of each clip to the source media file it originated from. Be aware, though, that you'll potentially export a great deal of media whenever you use this option. Consolidate Media: For finished projects this is a leaner media management workflow, since media that went unused won't be copied. Within the Handle Length field you can name extra handles, measured in frames, to tack onto the head and tail of each exported media file. Whenever a media file together with its handles overlaps another media file together with its handles, the two get merged into one exported media file.

7 (Optional) Should your project mix in formats that don't work with DaVinci Resolve, you can optionally switch on the “Transcode Video To” checkbox and pick a media format out of the pop-up menu to its right. This option automatically transcodes every piece of media in your sequence that doesn't fit the format named in the pop-up so it matches that format. 8 When you're copying or consolidating media onto a different drive, choose “Folder” from the Media Destinations Video/Data pop-up menu. Switch on the “Use Same Folder As AAF File” checkbox to store the exported media within the same folder you picked back in step 3. Leaving that checkbox switched off, you can click Select Folder to pick another spot. 9 Click Save, and once you're back at the Export As dialog, click Save once more. After export wraps up, you'll find a duplicate sequence and duplicate media filling your Media Composer bin, the suffix “.Exported” tacked onto the sequence and “.new” tacked onto each media clip. On the file system, the resulting folder holds an AAF file plus an Avid MediaFiles folder containing the exported media.

### Step 3–Conforming Your AAF in DaVinci Resolve

1 Open DaVinci Resolve and create a new project. 2 First of all, you must set DaVinci Resolve so it reads the timecode and reel number information out of the AAF files that Media Composer produces correctly. Click the gear button at the lower right-hand corner of the DaVinci Resolve window to bring up the Project Settings window, click General Options to surface the Conform Options, and do the following:

- Confirm that “Use Timecode” has been set over to “Embedded in the source clip.”
- Turn the “Assist using reel names from the” checkbox on, and choose

“Embedding in source clip file.”

Conform help drawing on reel names that are embedded inside the source clip 3 Click Save. 4 Do one of the following:

- From any page, choose File > Import AAF, EDL, XML (Shift-Command-I).
- Head to the Edit page, right-click somewhere within the Media Pool, then pick

Timelines > Import > AAF/EDL/XML.

5 Once the File Selection window opens, pick the AAF file you exported out of Media Composer, and click Open. 6 Once the Load AAF dialog comes up, whichever settings you pick govern which media files the AAF gets conformed against:

### Load AAF window conform options

To conform to the transcoded or AMA-linked media files you edited: Keep the “Automatically import source clips into media pool” checkbox switched on. For conforming against a separate batch of camera original media files: Tick both checkboxes, “Automatically import source clips into media pool” together with “Link to source camera files,” which lean on the Source Name metadata that Media Composer/Symphony writes into exported AAF files so the naming match between transcoded footage and its camera original counterpart stays tracked. For conforming against a directory of media you've chosen yourself: Tick both the “Automatically import source clips into media pool” checkbox plus “Ignore file extensions when matching.” For conforming against media sitting in the Media Pool already: Leave the “Automatically import source clips into media pool” checkbox unticked. For this to function there have to be clips in the Media Pool. 7 On top of that, make sure the “Automatically set project settings” checkbox is on. 8 Three other options bear on AAF import:

### Load AAF window conform options

Use Sizing Information: (Optional) Turn to this checkbox whenever position, scale, and rotate transform data should carry across from the source Media Composer project over into DaVinci Resolve. Import log messages as COLOR markers: Tick this checkbox and choose a color via the attached drop-down menu for markers that get placed on the Timeline bearing note text that describes import errors you might wish to investigate down the line. Import multi-channel audio tracks as linked groups: Switch this checkbox on whenever multi-channel audio such as stereo, 5.1, and 7.1 should arrive as separate mono timeline tracks bound to one another inside the Fairlight page. To learn more about Linked Groups, refer to Chapter 171, “Setting Up Tracks, Busses, and Patching.” With this checkbox switched off, multi-channel audio comes into multi-channel audio tracks on the Timeline. 9 Click OK.

Provided the media still sits where it lived at the moment you exported it out of Media Composer, both the timeline and every piece of its media ought to import now. That said, should the spot holding the media files you’re conforming against have moved, you might have to point out where the media lives through an extra dialog. Say you’d duplicated the media off the portable hard drive it first conformed to onto a quicker storage volume: a file dialog then pops up, asking you to pick the folder that holds the media your project draws on. When asked, go ahead and click OK. After the import wraps up, the Media Pool populates with the source media the imported project relies on, and the edit shows up as the active Timeline within the Edit page.
