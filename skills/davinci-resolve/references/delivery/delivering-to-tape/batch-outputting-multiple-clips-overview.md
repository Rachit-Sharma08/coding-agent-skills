# Batch outputting multiple clips overview

Version: DaVinci Resolve 20.3 Reference Manual. Context: Delivering to tape.
[Chapter index](INDEX.md) / [Previous section](capture-and-playout-settings.md)
<a id="source-batch-outputting-multiple-clips"></a>

### Batch Outputting Multiple Clips

There's also the choice of laying a set of clips to tape as a batch job rather than going out from the Timeline. Once you've lined up a batch of several clips in the Edit to Tape Queue, DaVinci Resolve records them onto tape one after another on its own. The way timecode gets generated during batch output rides on the “Output Source Timecode” option, found under the Project Settings' Capture and Playback panel. Leave it off and a single continuous timecode track is written across everything sent to tape. Switch it on and each clip's source timecode is written to tape with breaks between. While batch-outputting to tape, you can space the clips apart with black handles to ease later ingest, drawing on the “Set batch playout head/tail handle” options housed in that same Capture and Playback panel of the Project Settings.

To Batch Record several clips to tape: 1 With the transport controls, locate the In point on tape where recording should begin, and click the In button. 2 Take one of these routes to add items for output to the Edit to Tape Queue:

- Click the Add Clips button at the foot of the tape settings, select one or several media files in the VTR Record browser, then hit Add Clip(s) to Queue.
- Right-click any clip in the Timeline, pick Render This Clip, then click the Power Mastering button at the foot of the tape settings to drop that clip into the Queue.

3 Pick either Assemble or Crash from the dropdown at the Viewer's upper right. Since the clips you're sending carry discontinuous timecode, insert editing isn't available during batch output. 4 With every clip you mean to send now in the queue, click Start Record to start the output to tape. Device control handles recording onto the chosen stretch of tape, while a progress bar at the foot of the Render Queue indicates how long it'll run.
