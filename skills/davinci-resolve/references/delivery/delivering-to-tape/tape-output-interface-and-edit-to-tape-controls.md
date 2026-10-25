# Tape output interface and edit to tape controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Delivering to tape.
[Chapter index](INDEX.md) / [Next section](capture-and-playout-settings.md)
<a id="source-capture-and-playout-settings"></a> <a id="source-delivering-to-tape"></a> <a id="source-delivering-to-tape-1"></a> <a id="source-edit-to-tape-controls"></a> <a id="source-gang-timecode-to-tape"></a> <a id="source-general-options"></a> <a id="source-insertassemble-dropdown-menu"></a> <a id="source-setting-up-for-tape-output"></a> <a id="source-start-record-button"></a> <a id="source-the-gang-timecode-to-tape-option"></a> <a id="source-the-tape-output-interface"></a>

### Delivering to Tape

This section explains how the Deliver page lets you send a timeline, whole or in pieces, out to a device-controllable VTR hooked up to a compatible Blackmagic Design video interface. No matter which output interface you settle on, confirm that the RS-422 interface ties into the VTR's own and that device control is up and running.

### The Tape Output Interface

You carry out tape output from the Deliver page, but only after switching it into Tape mode. To flip the Deliver page over to tape output:

- Click the Tape button, the third one in from the left along the Interface toolbar at the top of DaVinci Resolve. The Deliver page then refreshes to surface the controls that pertain to editing to tape.

Once Edit to Tape mode is active, you drive the VTR from the Deliver page, marking In and Out points for an insert or assemble edit of the chosen stretch of the current Timeline out to tape.

- Capture and Playout: The Render Settings panel becomes the Capture and Playout panel, holding the controls and settings that dictate how DaVinci Resolve sends your program to tape.
- Edit to Tape Queue: The Render Queue becomes the Edit to Tape Queue, where you can assemble a batch made up of already-rendered media files or In- and Out-point-bounded slices of the current Timeline, all for output to tape together.
- Transport controls: Though they look much like the ones in Render mode, the transport controls here drive the VTR instead.
- Shuttle control: A shuttle control takes the place of what used to be the jog or scrubber bar, letting you sweep across whatever reverse and forward speeds the deck supports.
- In and Out controls: Under Edit to Tape mode, the In and Out buttons sitting right of the transport controls stake out a span of tape to Insert or Assemble edit onto from within the current Timeline. Still in Edit to Tape mode, marking In and Out points for a particular stretch of the Timeline is also possible: right-click a clip over in the Thumbnail or Mini‑Timeline and pick Mark In or Mark Out. In and Out points can only land at the start and finish of clips.
- Cue In and Cue Out controls: The buttons beside the timecode In and Out fields cue the tape to those particular frames on tape.

### Edit to Tape controls

### Gang Timecode to Tape

With the Deliver page sitting in Tape mode, right-clicking the ruler that runs across the top of the Timeline and picking “Gang Timecode to Tape” throws DaVinci Resolve into a state where setting an In point on the Deliver page Timeline automatically drops a matching In point on the tape deck. Lay down both In and Out points on the Deliver page Timeline and the deck's In and Out points get placed at the identical timecode, which makes layering insert edits onto an already-output program straightforward.

### The Gang Timecode to Tape option

### Insert/Assemble Dropdown Menu

Beneath the In and Out buttons, a dropdown menu sets how the chosen portion of the Timeline gets edited to tape. It carries two choices:

- Insert: Carries out an insert edit to tape, where the selected tape tracks get overwritten cleanly and frame-accurately while the timecode and control track keep running. An insert edit demands that you output to either a blacked tape or a prerecorded one.
- Assemble: Carries out an assemble edit, where every tape track gets overwritten, the video, audio, timecode, and control tracks included.
- Crash: (Shows up only when “Output Source Timecode” is switched on within the Playout area inside the Project Settings' Capture and Playback panel) Much like an assemble edit, save for the absence of a pre-roll period to bring the VTR up to speed. A crash edit likewise overwrites every track of the tape, video, audio, timecode, and control tracks alike, and can leave a more noticeable jump right at the edit point. Even so, there are situations where a crash edit is the sole option available for a given task.

NOTE: While DaVinci Resolve runs a Batch Output operation, the only ways to output clips are assemble editing or crash recording.

### Start Record Button

After you've placed In and Out points to bound how much tape gets recorded onto, the Start Record button kicks off device-controlled output to tape.

### Setting Up for Tape Output

Ahead of any edit to tape, the Capture and Playback panel of the Project Settings holds several options you'll want to dial in so they line up with the format and style of tape output you're undertaking.

### General Options

Switch on the Output LTC checkbox and DaVinci Resolve is told to send out LTC timecode.

### Capture and Playout Settings

These options govern capture as well as playback whenever you're using the Media page's Tape Ingest options or the Deliver page's Tape Output options.

- Video capture and playback: This dropdown is where you pick the video format (frame size and frame rate) used to output to tape. Your DeckLink card's format conversion can downconvert HD timelines to SD and upconvert SD timelines to HD.
- Use left and right eye SDI: A checkbox letting supported video interfaces take in and put out muxed stereoscopic video alongside supported VTRs, HDCAM SR decks running 4:2:2 x 2 mode among them. (As muxed stereoscopic signals come in, each eye is split off into its own left-eye and right-eye image files.) This parameter surfaces only when your hardware is configured for it.
- Video connection operates as: Chooses among the signal options on offer: Use 4:4:4 SDI, and enable Single Link. Which of them you'll see hinges on the video capture card in use.
- Data Levels: Lets you set the data range (typically scaled or full range) applied as you ingest from or output to tape. The toggle swaps the data range of the signal your video capture card emits, but solely during capture from tape on the Media page or output to tape on the Deliver page. Outside of active capture or output, your video capture card reverts to the like-named data range control found under the Project Settings' Master Settings panel, the one steering how you monitor the signal sent to an external broadcast display or projector.
- Video bit depth: Pick the bit depth that fits what your deck can handle. The options are 8-bit and 10-bit. A 10-bit output taxes the processor more but delivers higher quality on compatible gear, and it's the default.
- Use deck autoedit: Where your video deck supports it, this is the surest way to lay video onto the deck, since it has the deck roll the edit on the stated preroll and govern the edits through serial device control. Leave this checkbox off and the deck falls back to a plain edit On/Off mode, which risks frame inaccuracies unless the “Non auto edit timing” setting is dialed in correctly.
- Non auto edit timing: Tunes the edit synchronization of the attached deck while auto edit is switched off.
- Deck preroll: Sets how many seconds of preroll to use. The right amount turns on how your deck performs.
- Video output sync source: With a DeckLink card this stays at Auto. Other capture cards may need the sync source set to “Reference” for playout and “Input” for ingest. The setting appears only if a DVS card is installed in your system.
- Add 3:2 pulldown: Adds or strips the 3:2 pulldown needed to record or play 23.98 fps media onto or off a 29.97 tape format.
