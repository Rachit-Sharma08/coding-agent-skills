# Logging and capturing individual clips and logging and capturing multiple clips

Version: DaVinci Resolve 20.3 Reference Manual. Context: Ingesting from tape.
[Chapter index](INDEX.md) / [Previous section](tape-ingest-and-tape-capture-interface.md)
<a id="source-batch-capture-via-edl"></a> <a id="source-logging-and-capturing-individual-clips"></a> <a id="source-logging-and-capturing-multiple-clips"></a>

### Logging and Capturing Individual Clips

When you're after a precise range of tape, or several sections in one pass, another route is to log each section of tape you want ahead of time, then call on the Capture Clip or Batch Clips commands as a follow-up step. To grab a single clip through device control: 1 With the transport controls, locate the start of the tape section you intend to record and click the In button. Next, locate its end and press the Out button. 2 Key all the pertinent details into the various fields of the Metadata Editor. The Header refreshes with a preview of the file name about to be saved. 3 Once you're done, click Capture Clip. Deck control kicks in automatically to run through the stated range of tape and grab that clip. As soon as capture wraps, the new clip shows up in the Media Pool.

### Logging and Capturing Multiple Clips

To save time, you might instead log a batch of clips in one go, drawn from several tapes where needed, and then batch capture the whole lot together. To log one or more clips: 1 Using the transport controls, track down the start of the tape section you mean to record and click the In button. After that, track down its end and press the Out button. 2 Type all the pertinent details into the various fields of the Metadata Editor. The Header refreshes to preview the file name that will be written. 3 When that's done, click Log Clip. The clip joins the Media Pool as an offline tape clip, flagged by a black icon bearing a tape badge.

A logged clip sitting in the Media Pool ahead of capture To batch capture one or more logged clips: 1 (Optional) Flip the Media Pool over to List view, then use the Reel No column header to order the clips there by reel number. Doing so makes it simpler to pick out a run of clips to grab off one reel. 2 Choose one or more offline tape clips in the Media Pool that originate from a single reel. 3 Click Batch Clips, found at the foot of the Metadata Editor. Should you want to break off capture at any point, click Batch Clips again. Deck control takes over automatically to run through the tape currently in the VTR and grab every logged clip you've chosen that turns up on it, beginning with the one carrying the lowest timecode value and finishing with the one holding the highest timecode value. A progress bar, paired with text, reports how much remains before capture wraps. With each clip captured, its matching logged clip in the Media Pool gains a thumbnail mirroring the captured media. Once DaVinci Resolve has captured all the clips off a given reel, Batch Capture comes to a halt.

### Batch Capture Via EDL

An EDL can likewise serve to build offline tape clips, one per event in the EDL, which you then batch capture to pull in all the media a project needs to conform from tape. To bring an EDL in as a batch capture list: 1 Open the Project Settings, then in the sidebar click Master Panel and verify each of these:

- Set “Timeline frame rate” to the frame rate of your EDL.
- Turn on “Use drop frame timecode” if your EDL requires it.
- Make sure “Use Timecode” is set to “Embedded in the source clip.”
- Turn on “Assist using reel names from the.”

2 Choose File > Import Batch List From EDL. 3 Should a Conform Settings dialog pop up asking you to sign off on the current Project Settings, click OK if everything checks out. 4 Through the controls of the Select EDL files dialog, pick one or more EDLs, then click Open. Picking several EDLs pulls in every event from each EDL together. 5 In the dialog that follows, settle on a frame rate to conform the EDL at, then click OK. Every event in the EDL now shows up as offline tape clips in the Media Pool, set for capturing. If you load an EDL while the Media Pool already holds clips sharing a reel name and start timecode with events in the EDL, DaVinci Resolve skips making new offline tape clips for those.

A batch of logged clips brought in from an EDL 6 (Optional) Switch the Media Pool to List view, then click the Reel No column header to order the Media Pool clips by reel number. That eases picking a run of clips to grab off one reel. 7 (Optional) Any offline clips you don't intend to capture can be cleared out: right-click them within the Media Pool and choose Remove Selected Clips.

8 Mark which of the offline tape clips you'd like captured. Ideally, choose stretches of clips drawn from one and the same reel. 9 Click the Capture mode button sitting to the left of the transport controls, after which clicking Batch Clips kicks off capture. To stop capture partway through at any moment, click Batch Clips a second time. On its own, Deck control plays through whatever tape is loaded in the VTR and grabs each logged clip you've marked that it locates there, opening with the clip whose timecode value is lowest and closing with the clip whose timecode value is highest. Alongside text, a progress bar indicates how far there is left to go until capture finishes. As every clip comes in, the logged clip it answers to in the Media Pool picks up a thumbnail echoing the captured media. The instant DaVinci Resolve wraps up every clip from a given reel, Batch Capture stops.
