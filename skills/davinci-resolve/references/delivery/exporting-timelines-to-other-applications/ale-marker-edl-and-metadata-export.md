# Ale marker edl and metadata export

Version: DaVinci Resolve 20.3 Reference Manual. Context: Exporting timelines to other applications.
[Chapter index](INDEX.md) / [Previous section](edit-index-csv-txt-and-ale-export.md)
<a id="source-001-001"></a> <a id="source-002-001"></a> <a id="source-003-001"></a> <a id="source-004-001"></a> <a id="source-23976-1"></a> <a id="source-colu-m-n-1"></a> <a id="source-data-1"></a> <a id="source-exporting-and-importing-media-pool-metadata"></a> <a id="source-exporting-timeline-markers-to-edl-1"></a> <a id="source-exporting-timelines-to-other-applications-part-2"></a> <a id="source-field_delim-1"></a> <a id="source-heading-1"></a> <a id="source-tabs-1"></a> <a id="source-trim-this-montage-three-seconds-shorter"></a> <a id="source-v-c-01000909-01000910-01000909-01000910"></a> <a id="source-v-c-01002012-01002013-01002012-01002013"></a> <a id="source-v-c-01003012-01003013-01003012-01003013"></a> <a id="source-v-c-01003013-01003014-01003013-01003014"></a> <a id="source-video_format-1"></a>

### ALE with CDL illustration

| Header field | Value |
| --- | --- |
| FIELD_DELIM | TABS |
| VIDEO_FORMAT | 1080 |
| AUDIO_FORMAT | – |
| FPS | 23.976 |

### Column names

Name, Tracks, Start, End, Take, Tape, UNC, FPS, Reel, Scene, Shoot date, Manufacturer, Source Resolution, Source Bit Depth, DESCRIPT, Comments, Audio SR, Audio Bit Depth, Auxiliary TC1, KN Start, Source File Path, Display Name KeyKode, ASC_SOP, ASC_SAT, RESOLVE_SIZING

### Illustrated data values

A001_C002_V01.CBF6A4FD139AD.mxf, V, 10:28:27:03, 10:28:28:00, A001_C002_V01.CBF6A4FD139AD /Volumes/Disk_1/Avid MediaFiles/MXF/1/A001_C002_V01.CBF6A4FD139AD.mxf 23.98, DaVinci Resolve, 1920x1080, 10 /Volumes/Disk_1/Avid MediaFiles/MXF/1/A001_C002_V01.CBF6A4FD139AD.mxf A001_C002_V01.CBF6A4FD139AD (1.0260 1.0260 1.0260)(-0.0260 -0.0260 -0.0260)(0.8237 0.8237 0.8237) 0.8640 (0.0000 0.0000 1.0000 0.0000 0.0000 0 0)

The manual illustrates these fields using commas and wrapped values for readability. This is not an importable ALE record; actual ALE fields use tabs. Export an ALE and CDL file from Resolve to obtain correctly aligned fields.

### Exporting Timeline Markers to EDL

This command puts out a quick report that gathers, as EDL notes, the text of every marker dropped onto the Timeline. Clip markers don’t count. The report arrives in EDL format, one event per Timeline marker, each bearing a stand-in reel number (001 unless changed) along with source and record timecodes matching where that marker sits on the Timeline (running one frame long). For every event, the EDL note carries the Marker note where one exists. No note records the markers’ color

An example of an exported Timeline Marker EDL follows:

```text
TITLE: ( no title )
001 001 V C 01:00:09:09 01:00:09:10 01:00:09:09 01:00:09:10
Replace with another car door sound effect
002 001 V C 01:00:20:12 01:00:20:13 01:00:20:12 01:00:20:13
Trim this clip shorter
003 001 V C 01:00:30:12 01:00:30:13 01:00:30:12 01:00:30:13
Find another stock footage clip of the bridge
004 001 V C 01:00:30:13 01:00:30:14 01:00:30:13 01:00:30:14
Trim this montage three seconds shorter
```

### Exporting and Importing Media Pool Metadata

DaVinci Resolve lets you write metadata out of one project’s Media Pool so it can be brought into another project’s clips, for those times you have to shift metadata around. The operation puts out the entire Media Pool’s metadata as a .csv file. Picture a DIT who loaded plenty of metadata into the DaVinci Resolve project used to turn out dailies, after which a hurried editor spun up a separate project to start cutting those dailies. Rather than make the editor retype every clip’s metadata from scratch, you can export the metadata out of the DIT’s project and import it into the editor’s fresh project, with the relevant metadata matched to each corresponding clip on its own. To export Media Pool metadata: 1 Open a project that holds Media Pool metadata you’d like to export. 2 Should you wish, single out which Media Pool clips the metadata export covers. 3 For metadata covering the whole Media Pool, choose File > Export Metadata From > Media Pool; to keep the export to just the clips you singled out back in step 2 earlier, instead choose File > Export Metadata From > Selected Clips. 4 As the Export Metadata dialog comes up, key in a name, choose where the file should be written, then click Save. The whole of the metadata goes out into a .csv file you can open and edit in any spreadsheet application.

To import Media Pool metadata: 1 Open a project whose clips you’d like to fill in with the metadata you’re bringing in. 2 If you wish, highlight the specific clips in the Media Pool that should receive the metadata. 3 Pick File > Import Metadata To > Media Pool to push metadata onto possibly every clip in the Media Pool, or pick File > Import Metadata To > Selected Clips to limit the metadata to whichever clips you highlighted back in step 2. 4 Once the Import Metadata dialog opens, point it at a metadata .csv file to bring in and click Open. 5 Once the Metadata Import dialog opens, set the Import Options that will pair the .csv file’s metadata with the right clips in the project that’s currently open. Out of the box, DaVinci Resolve leans on “Match using filename” together with “Match using clip start and end Timecode” to line up each row of metadata in the .csv file against a clip in the Media Pool, yet additional choices exist, among them disregarding file extensions, relying on Reel Name, and relying on source file paths. 6 After that, decide which Merge Option to apply within the Metadata Import dialog. Three choices are available: Only update metadata items with entries in the source file: This is the default. A clip’s metadata changes only where the imported .csv file holds a valid entry. The clip’s remaining metadata fields stay exactly as they stood prior to the import. Update all metadata fields available in the source file: Across every clip that lines up with a metadata row in the imported .csv file, the option overwrites each separate metadata field the .csv file points to, no matter whether that field has a valid entry. Update all metadata fields available in the source file and clear others: Here too, for any clip matching a metadata row in the imported .csv file, every distinct metadata field referenced by the .csv file is overwritten regardless of whether a valid entry is present. Beyond that, whatever metadata fields go unreferenced by the imported .csv file get emptied of any metadata they previously held.

The Metadata Import dialog, where you select how incoming metadata should be matched and merged 7 Through the Metadata Import dialog you set the matching and merging behavior for the metadata you bring in 8 Once you’ve settled on your options, click Ok and every available piece of metadata from the source .csv file gets imported.
