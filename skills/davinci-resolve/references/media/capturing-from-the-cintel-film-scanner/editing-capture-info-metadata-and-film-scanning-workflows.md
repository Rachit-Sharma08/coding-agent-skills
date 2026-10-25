# Editing capture info metadata and film scanning workflows

Version: DaVinci Resolve 20.3 Reference Manual. Context: Capturing from the cintel film scanner.
[Chapter index](INDEX.md) / [Previous section](scanner-light-status-and-stabilization.md) / [Next section](focus-the-scanner.md)
<a id="source-before-you-begin"></a> <a id="source-editing-capture-info-metadata"></a> <a id="source-film-scanning-workflows"></a> <a id="source-load-and-align-the-film"></a>

### Editing Capture Info Metadata

When DaVinci Resolve runs alongside Cintel Scanner, a set of capture metadata fields turns up along the lower edge of DaVinci Resolve’s film scanner panel. Within the ‘capture info’ panel sit editable metadata fields that spell out capture properties such as where files get saved, the codec type, frame rate, and the format of file names. Each clip carries this metadata, and you can read it back on the media page. Before you start scanning, you may want to tweak some of the project settings.

The ‘capture info’ panel lets you specify metadata for your scanned clips.

- Capture Location: Before any film scanning session gets going, scroll down within DaVinci Resolve’s film scanner panel to its ‘capture info’ section and confirm the scanned files are landing in the directory and volume you intend. Click the ‘browse’ button and pick a location from the file destination dialog. Handling this first is wise, since this step is easy to overlook.
- Capture: When a Cintel Audio and KeyKode Reader is fitted, this menu hands you options for ‘audio only’ so no images get captured, or ‘image and sound’. As an alternative, you can capture ‘image only’ when audio doesn’t matter.
- Resolution: The resolution of the capture files rides on the source film format, so this field can’t be edited.
- Codec: DaVinci Resolve picks the ‘Cintel Raw’ codec for lossless compression by default, or you can opt for ‘Cintel Raw 3:1’ to get even smaller file sizes.
- Film Frame Rate: State the frame rate the film was first shot at. DaVinci Resolve adjusts the timeline frame rate on its own from this value. This setting has nothing to do with capture or transport speeds. Should you scan audio with the optional Audio and KeyKode Reader accessory, that reader compensates for frame rate on its own to keep an overall sample rate of 48kHz. As for timecode output, it works at 16, 24, 25, and 30 fps; outside those rates, nothing is output.
- File Name Prefix: A prefix to help pin down the scan. You might use your project’s name here — the title of whatever film is going through the scanner, for instance.
- Timestamp Prefix: Tick this checkbox to put a timestamp in front of your scans alongside the ‘file name prefix’ you set. Your clips get saved into separate sub-folders inside the destination folder. This checkbox is ticked by default. Should you want all your clips kept together in one master destination folder with no timecode in the file name, just clear the checkbox.

NOTE: Skip the timestamp prefix and your capture names may not be unique; when such files share one location, existing files could end up overwritten.

- Roll/Card, Reel Number, Clip Number, and Program Name: Each of these is a metadata field for labeling the clip.
- Flags: You can use these color coded flags to tag clips.
- Good Take: Corresponds to ‘circled take’ metadata in the media pool.
- Log Clip: Adds a clip to the media pool. Once you’ve marked ‘in’ and ‘out’ points for a section you want

to scan, check the metadata is right, then click ‘log clip’. For more details, the DaVinci Resolve manual covers this across its ‘Logging and Capturing Individual Clips’ and ‘Logging and Capturing Multiple Clips’ sections.

- Batch Clip, Capture Clip, Capture Now, and Snapshot: These scanning buttons give you different ways to capture clips. To read more about them, this manual devotes its ‘Scanning One or More Sections of Film’ section to the topic.

### Film Scanning Workflows

The sections that follow lay out how to scan film with DaVinci Resolve and drive the Cintel scanner. All through them, the features covered in the previous section appear in the order you’ll carry out each step of the scanning process.

### Before You Begin

Before you switch your scanner on and load film, first dust the gate so your scans come out as clean as they can. Compressed air can handle this, though a badly dirty gate may need to come off for a more thorough cleaning. That done, power up the Cintel Scanner, launch DaVinci Resolve, set up the project that will hold your scanned film, and over on the media page hit the ‘Cintel scan’ button. From there, the ‘Film Scanner’ tab brings up DaVinci Resolve’s film scanner panel. Ahead of loading any film or doing anything else, hit the ‘calibrate’ button down in the panel’s lower-left corner. You ought to dust the scanner gate every time before a fresh reel goes in, yet it’s the calibrate button that wipes out, from the scans you’re about to make, any blemishes in the optics that simply won’t come off.

### Load and Align the Film

Load the film you want to scan. With an image present, the scanner will line up a frame on its own. Bear in mind the image may come out framed wrong if you first load blank film leader. Next, pick the film type. If you need to, use the ‘perf nudge’ and ‘frame’ buttons to hand-tune the framing bar’s alignment to the scanner’s sensor such that the previous frame’s bottom and the following frame’s top barely show at the viewer’s top and bottom, while the current frame sits centered vertically. Make a point of confirming the image in the viewer isn’t zoomed in while you do this.
