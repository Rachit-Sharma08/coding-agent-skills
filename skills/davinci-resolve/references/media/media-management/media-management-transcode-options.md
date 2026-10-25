# Options in the media management window and options for transcode only

Version: DaVinci Resolve 20.3 Reference Manual. Context: Media management.
[Chapter index](INDEX.md) / [Previous section](media-management-and-drt-timelines.md)
<a id="source-file-naming-when-you-consolidate-media"></a> <a id="source-options-for-transcode-only"></a> <a id="source-options-in-the-media-management-window"></a>

### Options in the Media Management Window

Each Media Management operation puts different options on the table.

- Entire Project Copy/Transcode all media: (Not available for Timelines) Picking this option copies the complete source media for every last clip in the project. Should you add more media down the line and then run the Copy function again, DaVinci Resolve copies only the extra files needed to mirror the current Media Pool.
- Destination: Click the Browse button to pick a destination for the managed media to be copied to. Need a fresh directory? Right-click a Volume icon over in the File Browser list, pick New Folder, key a name into the resulting dialog, and click OK.
- Timeline selections: With the Timelines mode of media management chosen, you can open the Timeline Selection controls and switch on the checkbox beside each timeline holding media you want included.
- Copy/Transcode All media: Copies all media available to that operation.
- Copy/Transcode Used media: Restricts copying to the media files behind clips a timeline actually uses, and

brings them across whole.

- Copy/Transcode Used media and trim keeping x frame handles: Restricts copying to the media files a timeline uses, yet strips away unused heads and tails save for the handles you specify.
- Use project name subfolder: Automatically builds a subfolder named after the project beneath the destination directory holding all the copied or transcoded media.
- Consolidate multiple edit segments into one media file: This option only opens up if you've picked "Copy and trim used media" When several clips in a timeline trace back to the same media file, a single consolidated media file gets built holding every frame from all those clips, plus whatever extra frames sit between them. Even though this option ends up copying or moving more media, it's tremendously handy when you're consolidating media you intend to grade with the automatic grade linking of remote versions, since it preserves the original tie between each Timeline clip and the source media file it came from.
- Preserve folder hierarchy after x folder levels: Keeps a depth you specify of the original directory structure a clip's source media file uses, rebuilding it as new files are rendered for output. The number you pick sets how many subdirectory levels DaVinci Resolve will automatically build inside the currently named "Render job to" directory to mirror the path the source files use. Defaults to 0, which builds no matching subdirectories. The count of path levels is measured starting from the head of each media file path.
- Relink to new files: (Appears for the Copy operation only) Relinks the chosen clips and/or timelines to the new media you've produced by copying, wherever you copied it.

### Options for Transcode Only

The options below show up only when Transcode is the Media Management operation in play. Settings: Surfaces the default controls for the Media Management operation. Video: Surfaces the video codec controls for rendering to every available video format. Audio: Surfaces the audio codec controls for rendering to every available audio format.

### File Naming When You Consolidate Media

When you're media managing clip-based formats such as QuickTime or MXF, and the "Trim Used Media" option is on while the "Consolidate Multiple Edit Segments Into One Media File" checkbox is off, timelines drawing on several clips from the same media file will spawn several trimmed media files. So these files don't overwrite each other, extra characters get tacked onto each trimmed media file sharing a source; which characters are used hinges on the video format. For DPX files: \_0, \_1 For R3D files: \_S000.RDC, \_S001.RDC For QuickTime files: \_S000.mov, \_S001.mov
