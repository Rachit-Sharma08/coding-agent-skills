# Tape ingest and tape capture interface

Version: DaVinci Resolve 20.3 Reference Manual. Context: Ingesting from tape.
[Chapter index](INDEX.md) / [Next section](individual-and-batch-clip-logging-capture.md)
<a id="source-capture"></a> <a id="source-deck-settings"></a> <a id="source-editable-capture-metadata"></a> <a id="source-ingesting-from-tape"></a> <a id="source-ingesting-from-tape-1"></a> <a id="source-setting-up-to-capture-from-tape"></a> <a id="source-tape-capture-viewer-in-the-media-page"></a> <a id="source-tape-ingest"></a> <a id="source-the-tape-capture-interface"></a> <a id="source-the-three-methods-of-capture"></a> <a id="source-using-capture-now"></a>

### Ingesting From Tape

Through a compatible video input device, like a Blackmagic Design UltraStudio or a DeckLink card, DaVinci Resolve can pull media in off tape. Device control is among the supported features.

### Tape Ingest

Here we walk through bringing media off tape straight into the Media Pool inside DaVinci Resolve. Whether you've got just a few clips to grab for an existing project or you have to recapture every clip tied to the events of an EDL, the Media page in Capture mode lets you pull from any device-controllable deck over a compatible video interface. To move into tape capture on the Media page: Click the Capture button, which sits to the left of the Interface toolbar along the top of the Media page. The Media page then shifts to show the controls relevant to editing to tape, and a purpose-built set of capture metadata and controls takes the place of the Audio panel to help you keep tabs on the clips you produce.

### The Tape Capture Interface

Once you're in Capture mode, the Media page drives the VTR so you can set In and Out points for logging or grabbing a chosen stretch of the tape.

### Tape Capture viewer in the Media page

- Transport controls: Though the transport controls look much like the ones you'd use just to play through selected clips on the Media page, here they instead drive the VTR.
- Shuttle control: Where the scrubber bar once sat, a shuttle control now appears, letting you shuttle across the span of reverse and forward speeds the connected deck supports.
- In and Out controls: Under Capture mode, the In and Out buttons sitting to the right of the transport controls mark out a stretch of the tape to capture.
- Capture panel: The panel flips over to the Capture panel on its own, bringing tape-specific metadata and capture controls. Filling in File Name Prefix refreshes the file name preview displayed up in the Header, which also reports the Capture directory, Resolution, and Frame Rate set in the Capture and Playback panel of the Project Settings.

### Editable capture metadata

### Setting Up to Capture From Tape

Ahead of any tape capture, you'll have to set a range of options within the Capture and Playback panel of the Project Settings. There are two clusters of settings, especially, that must be filled in.

### Deck Settings

These options bear on both capture and playback whenever you turn to the Tape Ingest options on the Media page or the Tape Output options on the Deliver page.

- Video capture and playback: From this drop-down menu you pick the video format (frame size and frame rate) to output to tape with. Your DeckLink card's format conversion can downconvert HD timelines to SD and upconvert SD timelines to HD.
- Use left and right eye SDI: A checkbox letting the Blackmagic Design DeckLink HD Extreme 3D+ take in and send out muxed stereoscopic video alongside supported VTRs, like HDCAM SR decks running 4:2:2 x 2 mode. (As muxed stereoscopic signals come in, each eye is split off into its own left-eye and right-eye image files.)
- Video connection operates as: Chooses among the offered signal options: Use 4:4:4 SDI and Enable Single Link. Exactly which options show up rides on the video capture card you've got.
- Data Levels: Lets you state the data range (typically scaled or full range) applied while ingesting from or outputting to tape. The option flips the data range of the signal your video capture card puts out, but solely during capture from tape on the Media page or output to tape on the Deliver page. While no capture or output is underway, your video capture card reverts to the data range setting of the same name over in the Master Settings panel of the Project Settings pane, which dictates how you monitor the signal sent out to an external broadcast display or projector.
- Video bit depth: 10-bit stands as the sole option.
- Use deck autoedit: Where your video deck supports it, this is the best route for laying video

down to the deck, since it lets the deck roll the edit off the specified preroll and steer the edits over serial device control. With this checkbox off, the deck falls back on a plain edit On/Off mode, which risks frame inaccuracies should the “Non auto edit timing” setting be set up wrong.

- Non auto edit timing: Fine-tunes the edit synchronization of the connected deck whenever auto edit is switched off.
- Deck preroll: Sets how many seconds of preroll to use. The right amount hinges on how your deck performs.
- Video output sync source: With a DeckLink card this sits at Auto. Other capture cards may ask you to point the sync source at “Reference” for playout and “Input” for ingest. You'll only see this setting if the DVS card is installed on your system.
- Add 3:2 pulldown: Adds or strips out the 3:2 pulldown that lets 23.98 fps media be laid onto, or played back off, a 29.97 tape format.

### Capture

You'll lean on these options when you turn to Capture mode on the Media page to bring tape clips into the Media Pool, or when you're driving the Cintel Film Scanner to scan film across various formats.

- Capture: Lets you decide between capturing both Video and Audio together, or Video on its own.
- Video Format: The format your captured media gets saved as. When you're capturing from tape, the

choices on offer are DPX and QuickTime.

- Codec: The codec that writes your captured media. For tape capture, the lineup takes in Apple ProRes in its assorted flavors, YUV 422 at 8- and 10-bit, 10-bit RGB, plus the DNxHD family in its various forms.
- Save clips to: A field showing the directory path where media files grabbed from tape land. Aim for a volume quick enough to keep up with the data rate of the media format you're capturing.

Browse: Hit this button to pick a directory for writing captured media into. Whatever directory you settle on turns up in the field above.

- Save in this folder path: A run of checkboxes lets you dictate what extra information shapes the directory hierarchy holding the captured media. Each checkbox you tick adds one more directory whose name comes from that checkbox's metadata. Pick any or all of these: Program name, Clip number, Reel number, Roll/Card.
- Apply reel number to: Lets you decide how the reel name gets written. A pair of checkboxes let you stamp the reel name into the file's name and/or into the Header data.
- Use prefix: A field where you can enter a prefix to attach to the media file's name. This lets you fold in text identification so the media is easier to spot and search for.
- Apply prefix to: Two checkboxes let you opt to apply the prefix you entered to the file name and/or to the folder name.
- Use frame number with: For captures going to image sequences, you choose how many digits go into the frame number written into each frame file's name.
- Set batch ingest handles to: Lets you tack extra frames of handles onto the start and finish of every scanned clip during batch capture with the scanner.
- Input: A drop-down for picking how many audio tracks to capture, anywhere from 2 to 16.

### The Three Methods of Capture

After you've dialed in every relevant option in the Project Settings window, at the very least the settings labeled “Video Capture and Playback,” “Capture Clips Saved to,” along with Apply Reel Name to,” you're set to begin capturing. Which of the three tape-capture methods you reach for comes down to your workflow. Across all of them, media can be brought in as QuickTime Movies or DPX image sequences.

### Using Capture Now

When all you need is to grab a stretch of tape in a hurry, the Capture Now command does the job. To Capture Now: 1 Lean on the transport controls and the In button to pin down what you'd like to capture. 2 Fill in all the pertinent details across the various fields of the Metadata Editor. The Header refreshes to preview the file name that's going to be saved. 3 Use the transport controls to roll playback, then click the Capture Now button down at the foot of the Metadata Editor. 4 Once the stretch of tape you meant to record has run out, click Capture Now once more to halt capture. A fresh clip turns up in the Media Pool, dropped on its own into a new folder in the Media Pool under a name built from the timecode value turned into a frame count according to the ingest frame rate. To illustrate, a clip grabbed at timecode 01:00:00:00 winds up with the file name 00086400.dpx.
