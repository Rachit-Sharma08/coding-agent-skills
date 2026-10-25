# Exporting the edit index as a csv or txt file and exporting to ale

Version: DaVinci Resolve 20.3 Reference Manual. Context: Exporting timelines to other applications.
[Chapter index](INDEX.md) / [Previous section](timeline-and-otio-export.md) / [Next section](ale-marker-edl-and-metadata-export.md)
<a id="source-23976"></a> <a id="source-48khz"></a> <a id="source-colu-m-n"></a> <a id="source-data"></a> <a id="source-exporting-the-edit-index-as-a-csv-or-txt-file"></a> <a id="source-exporting-to-ale"></a> <a id="source-exporting-to-ale-with-cdl"></a> <a id="source-field_delim"></a> <a id="source-heading"></a> <a id="source-tabs"></a> <a id="source-video_format"></a>

### Exporting the Edit Index as a CSV or TXT File

Whatever the Edit Index currently holds, on the Edit page, can be written out as a stand-alone file you can reference in all sorts of ways. The export goes like this: 1 Open the Edit Index and, where needed, pick one of the Edit Index filters out of the Edit Index option menu. You might, say, narrow the edit index to Offline Clips Only when you want a list of every offline clip in the present timeline written out. 2 Right-click that timeline within the Media Pool, choose Timelines > Export > Edit Index, then settle on a location and export format in the Export Edit Index dialog, and click Save.

### Exporting to ALE

DaVinci Resolve can write out ALE (Avid Log Exchange) files too. ALE is a tab-delimited, ASCII text-based clip logging list format whose purpose is to shuttle clip metadata that won’t fit inside MXF files. The point of an ALE file is to let you put out a log of every clip a given timeline uses, carrying all the metadata DaVinci Resolve has tied to those clips, so that metadata can be pulled into and matched up with clips over in Media Composer or Symphony. An ALE file breaks into three parts, named Heading, Column, and Data:

- The Heading lays out details about the clips under log, the picture and audio format among them, along with the frame rate.
- The Column line sets out each metadata column the list will export. A baseline set of metadata columns rides along automatically, filled in or not. On top of those, DaVinci Resolve tacks extra metadata columns onto the list whenever the matching metadata field in the Metadata Editor holds something. Type entries into the Camera, Keyword, and Shot fields of the Metadata Editor, for instance, and those columns join the exported ALE. No user setting governs any of this.
- The Data section runs several lines, one per event the list references, each holding all of the data that belongs to that clip.

When you export stereoscopic clips out of stereoscopic timelines, these extra metadata columns ride along automatically inside the pair of ALE files that get produced:

- Pan (measured against timeline resolution)
- Tilt (measured against timeline resolution)
- Zoom
- Rotate
- Convergence (measured against timeline resolution)
- HFlip (0 or 1)
- VFlip (0 or 1)

When the ALE files come out of projects built on ARRIRAW clips, these further metadata columns may be folded in:

- Temperature
- Tint

To export an ALE file: 1 Open the Edit page, right-click in the Media Pool the Timeline you mean to export, and choose Timelines > Export > ALE out of the contextual menu. 2 Give the ALE file a name, pick where to save it, and click OK. The ALE file gets written, and a dialog pops up reminding you of the file path it landed at (click OK to clear it).

A short ALE export, by way of example:

### Heading

### FIELD_DELIM

### TABS

### VIDEO_FORMAT

AUDIO_FORMAT

### 48khz

FPS

### 23.976

### Colu m n

Name, Tracks, Start, End, Take, Tape, UNC, FPS, Reel, Scene, Shoot, date, Manufacturer, Source Resolution, Source, Bit Depth, DESCRIPT, Comments, Audio SR, Audio Bit Depth, Auxiliary TC1, KN Start, Source File Path, Display Name

### Data

A001_C002_V01.CBF6A4FD139AD.mxf, V, 10:28:27:03, 10:28:28:00, A001_C002_V01.CBF6A4FD139AD /Volumes/Disk_1/Avid MediaFiles/MXF/1/A001_C002_V01.CBF6A4FD139AD.mxf 23.98, DaVinci Resolve, 1920x1080, 10 /Volumes/Disk_1/Avid MediaFiles/MXF/1/A001_C002_V01.CBF6A4FD139AD.mxf A001_C002_V01.CBF6A4FD139AD A016_C008_V01.CBF6A4FD13ABD.mxf,V, 23:35:56:03, 23:36:00:11, A016_C008_V01.CBF6A4FD13ABD /Volumes/Disk_1/Avid MediaFiles/MXF/1/A016_C008_V01.CBF6A4FD13ABD.mxf 23.98, DaVinci Resolve, 1920x1080, 10 /Volumes/Disk_1/Avid MediaFiles/MXF/1/A016_C008_V01.CBF6A4FD13ABD.mxf A016_C008_V01.CBF6A4FD13ABD A004_C012_V01.CBF6A4FD1438E.mxf, V, 14:07:31:21, 14:07:35:15, A004_C012_V01.CBF6A4FD1438E /Volumes/Disk_1/Avid MediaFiles/MXF/1/A004_C012_V01.CBF6A4FD1438E.mxf 23.98, DaVinci Resolve, 1920x1080, 10 /Volumes/Disk_1/Avid MediaFiles/MXF/1/A004_C012_V01.CBF6A4FD1438E.mxf

NOTE: An actual ALE doesn’t carry the commas printed above; they appear here only to keep the fields clear.

### Exporting to ALE with CDL

Avid Media Composer and Symphony will likewise import ALE files that carry extra CDL metadata columns, the ones that bind SOP (Slope/Offset/Power) and SAT (Saturation) adjustment metadata to every clip logged in the ALE. Bring an ALE with CDL file into Media Composer and the SOP and SAT data fill metadata columns, ready to be held onto and exported across the various Avid workflows. Below is an example showing the Heading, Column, and Data sections of a sample ALE with CDL, carrying a single line of clip and CDL data.

Putting out an ALE with CDL file runs thus: 1 Open the Edit page, right-click in the Media Pool the Timeline you mean to export, and choose Timelines > Export > ALE and CDL out of the contextual menu. 2 Give the ALE file a name, pick where to save it, and click OK. The ALE file gets written, and a dialog pops up reminding you of the file path it landed at (click OK to clear it).

A short ALE with CDL export, by way of example:
