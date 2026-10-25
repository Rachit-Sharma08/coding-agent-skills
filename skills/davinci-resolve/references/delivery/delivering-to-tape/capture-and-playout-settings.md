# Capture and playout settings

Version: DaVinci Resolve 20.3 Reference Manual. Context: Delivering to tape.
[Chapter index](INDEX.md) / [Previous section](tape-output-interface-and-edit-to-tape-controls.md) / [Next section](batch-outputting-multiple-clips-overview.md)
<a id="source-capture"></a> <a id="source-edit-to-tape-queue-option-menu-settings"></a> <a id="source-outputting-a-program-from-the-timeline"></a> <a id="source-playout-settings"></a> <a id="source-power-mastering"></a> <a id="source-tape-output-procedures"></a>

### Capture

You'll reach for these options when capturing clips off tape into the Media Pool through the Media page's Capture mode. The media comes in as DPX image sequences.

- Capture: Lets you decide between pulling in both Video and Audio or Video Only.
- Video Format: The format your scanned film frames get stored in. Off tape, your choices are DPX and QuickTime. Off the Cintel film scanner, you're limited to Cintel Raw Image (CRI), a raw data format that DaVinci Resolve debayers on its own into a Cineon log-encoded image for grading.
- Codec: The codec that writes the captured media. Off tape, the lineup spans the various Apple ProRes flavors, 8- and 10-bit YUV 422, 10-bit RGB, and the assorted DNxHD types. Cintel Raw Image files fall back to RGB.
- Save clips to: A field showing the directory path where media files captured off tape land. Aim for a volume quick enough to keep up with the data rate of whatever media format you're bringing in.
- Browse: Click here to pick a directory for the captured media to write into. Your chosen directory then shows in the field above.
- Save in this folder path: A row of checkboxes lets you spell out what extra information shapes the directory hierarchy holding the captured media. Each checkbox you enable tacks on another directory named after that checkbox's metadata. Pick any or all of: Program name, Clip number, Reel number, and Roll/Card.
- Apply reel number to: Lets you decide how the reel name gets written. A pair of checkboxes write the reel number into the file's name and/or into the Header data.
- Use prefix: A field where you type a prefix to fold into the media file's name, adding text identification that makes the media easier to spot and search for.
- Apply prefix to: Two checkboxes let you apply the prefix you typed to the file name and/or to the folder name.
- Use frame number with: When you're capturing to image sequences, this picks how many digits go into the frame number written into each frame file's name.
- Set batch ingest handles to: When capturing image sequences from a batch list, this sets how many frames of extra handles come in alongside every logged clip.
- Enable audio input: Tick this checkbox to bring in audio together with the video. For QuickTime or MXF files, the audio lands as extra tracks inside each file. For a DPX image sequence, a separate broadcast .wav file gets recorded.
- Input: Lets you pick how many audio tracks to capture, anywhere from 2 to 16.

### Playout Settings

These options touch nothing but the video signal sent out while you're in the Deliver page's Edit to Tape mode.

- Output: Lets you pick whether to send out both Video and Audio, Video Only, or Audio Only for an audio layback.
- Output Source Timecode: Tick this checkbox to send out each clip's own source timecode. It only comes into play when you're assemble editing to tape.
- Output LTC: On a Blackmagic Design DeckLink or UltraStudio device running HD-SDI, longitudinal timecode (LTC) rides on track 16 of the HD-SDI video signal, so a Mini Converter de-embedder can readily pull off this analog timecode audio signal and route it straight into a recording device. That's especially handy when outboard video processing gear such as a noise reducer or format converter fails to pass the VITC timecode through.
- Delay LTC by x frames: When you send LTC out to route around outboard processing gear like a noise reducer or format converter, you can offset for the processing lag by holding the timecode back a handful of frames so the processed image and the timecode hit the deck together. A DVS card provides its own separate timecode output.
- Enable audio output: Tick this checkbox and DaVinci Resolve plays every available timeline audio track alongside the outgoing video, letting both be laid to tape.
- Offset audio by x frames: Lets you dial in an offset between the audio track and the video to land proper A/V sync whenever outboard processing hardware is delaying the picture.
- Output x channels of audio: Pick how many audio tracks get sent out to tape.
- Set batch playout head handle to x seconds: When you batch-output several clips, you can

call for a certain number of frames ahead of each clip's In point to be sent out too.

- Set batch playout tail handle to x seconds: When you batch-output several clips, you can call for a certain number of frames after each clip's Out point to be sent out too.
- Apply gaps between clips: This checkbox drops a black gap of the stated frame duration between each pair of clips being sent out while you're outputting in batch mode.

### Edit to Tape Queue Option Menu Settings

The options below live in the Option menu over at the upper-right corner of the Edit to Tape Queue.

- Show Job Details: Reveals more about each job sitting in the Render Queue.
- Clear Recorded: Wipes out every queue item that's already gone to tape.
- Clear All: Wipes out every queue item.
- Sort by Reel & Timecode: Runs a two-key sort on reel and timecode, putting reel first

and timecode second.

- Sort by Timecode: Orders strictly by timecode.
- Output Source Timecode: Tells tape output to lay source timecode to tape (each clip's

own timecode) in place of record timecode (drawn from the Timeline).

- Use Preview for Tape Output: Switches on Preview mode for tape output. Preview

mode lets you rehearse how an edit-to-tape pass will behave before you commit it to recording.

### Tape Output Procedures

Several distinct paths exist for getting media onto tape, and which one fits depends both on your goal and on how heavy your grades are next to what your workstation can crunch.

### Power Mastering

Power Mastering lets you pick either a span of clips or a whole timeline and lay it to tape in real time, no rendering involved. That spares you a lengthy render and conserves disk space besides. Power Mastering gives up nothing, because your program still goes out at full quality. Should a few clips carry grades you already know are too processor-heavy to Power Master, the Render Cache controls can cache those troublesome clips before they go out. For a fuller treatment, turn to Chapter 8, “Improving Performance, Proxies, and the Render Cache.”

### Outputting a Program From the Timeline

The most straightforward way to go to tape is to send out a single Timeline, whether the whole thing or just a portion when you're insert editing a small revised stretch. To Power Master to tape: 1 If you must, lean on the Render Cache to cache any clips too processor-heavy to output live. 2 Click the Edit to Tape mode button left of the transport controls to flip into tape output.

3 Stake out how much of the current Timeline to send by running the playhead through the program, then right-clicking the clips that mark the range's beginning and end and invoking the Mark In and Mark Out commands. 4 With the transport controls, locate the In point on tape where recording should begin, and click the In button. 5 Pick Insert from the dropdown at the Viewer's upper right when you're either going to a striped and blacked tape or inserting over a program already on tape. 6 Click the Power Mastering (lightning bolt) button down at the bottom of the tape settings to drop the job you just built into the Edit to Tape Queue. 7 Click Start Record to set the output to tape in motion. Device control handles recording onto the chosen stretch of tape, while a progress bar at the foot of the Render Queue indicates how long it'll run.

Prefer not to Power Master? Then render the stretch of the Timeline you need to send as one clip up front, a self-contained media file, and feed that clip straight into the Edit to Tape Queue. That can be the smoother route when the timeline you're outputting is exceptionally processor-heavy.

To send a pre-rendered media file to tape: 1 Down at the foot of the tape settings, click the Add Clips button; in the VTR Record dialog, choose the media file you rendered back in step 1, then hit Add Clip(s) to Queue. The file you chose joins the Edit to Tape Queue as a Power Mastering job and goes out whole. 2 With the transport controls, locate the In point on the tape where recording should begin, and click the In button. 3 Pick Insert from the dropdown at the Viewer's upper right when you're either going to a striped and blacked tape or inserting over a program already on tape. 4 To rehearse the edit before it's actually committed to tape, turn on “Use Preview for Tape Output” via the Edit to Tape queue option-menu, then click Start Record and watch DaVinci Resolve walk through the edit on the deck. Once you've previewed it, switch that setting back off. 5 Click Start Record to set the output to tape in motion. Device control handles recording onto the chosen stretch of tape, while a progress bar at the foot of the Render Queue indicates how long it'll run.
