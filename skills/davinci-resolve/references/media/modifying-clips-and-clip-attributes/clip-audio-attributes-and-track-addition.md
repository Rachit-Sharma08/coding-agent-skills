# Audio panel of the clip attributes window and add track controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Modifying clips and clip attributes.
[Chapter index](INDEX.md) / [Previous section](media-pool-inspector-and-clip-attributes.md) / [Next section](new-subclip-dialog-and-removing-or-changing-subclip-limits.md)
<a id="source-add-track-controls"></a> <a id="source-changing-clip-thumbnails-in-the-media-pool"></a> <a id="source-creating-subclips"></a> <a id="source-reel-name-attributes"></a> <a id="source-the-audio-panel-of-the-clip-attributes-window"></a> <a id="source-the-timecode-panel-of-the-clip-attributes-window"></a> <a id="source-timecode-attributes"></a> <a id="source-update-timecode-from-audio--ltc"></a>

### The Audio panel of the Clip Attributes window

### Add Track Controls

Sitting atop the Track/Channel list, a cluster of controls lets you append extra tracks onto a clip. Tacking on those extra tracks gives you a way to remap the clip’s available channels so they surface in the Timeline as you edit.

- Format: A drop-down through which you pick a format for whatever new tracks you add. Your pick here drives how many channels show up in the Channel Assignments list beneath it, and likewise what sort of Timeline audio track it takes to surface every channel of the clip. Should you pick

a Channel Format carrying fewer channels than the clip actually holds, every surplus channel gets switched off. The choices on hand are: Mono: Suited to single-channel clips Stereo: Suited to clips bearing two-channel left/right audio 5.1: Suited to 5.1 surround mixes 7.1: Suited to 7.1 surround mixes Adaptive: Suited to multiple-mono production audio — multi-channel recordings, for instance, where a boom microphone, a pair of separate lavaliere microphones, and a mixdown track are all captured at once.

- Tracks: Sets how many tracks you wish to tack onto the current clip or clips. Every track you tack on means one more linked audio item gets dropped into one more audio track once the clip is edited into the Timeline. Say you hold a multi-channel production recording made with four separate microphones; you could tack on 3 mono audio tracks and then route each channel to its own track, surfacing every channel as a standalone audio clip in the Timeline so each microphone can be edited on its own.
- Add button: Tacks the tracks you have specified onto the current clip or clips.

On the left, a clip holding one track of two-channel stereo audio, set beside a clip on the right holding two tracks of single-channel mono audio Audio Track and Channel List Beneath the Add Track controls, the list carries one entry per track defined inside whichever clip or clips you have selected. Pop-ups inside that list let you respecify and route how the clip’s channels get distributed across the variously mapped tracks you built.

- Format: Whichever format a given audio track takes — the options being Mono, Stereo, 5.1, 7.1, or Adaptive.
- Source Channel: Per track, you see as many channels as the chosen format demands.

Where a Stereo track carries two source channels, a 7.1 track carries eight. Each channel is shown nested below whichever track it belongs to. To drop a particular channel out of the clip, pick &lt;none&gt; from the list.

- Track: The name of each track in a clip.
- Channel in Track: The name of each channel in that track.
- Delete Track button: Float the pointer over a track and a trashcan icon surfaces; click it to remove that track.

The trashcan button for deleting an audio track from inside Clip Attributes, which shows up only while the mouse hovers over a track

Support for Mixed Audio Track Formats from Source Clips DaVinci Resolve will also handle media whose several audio tracks hold channels embedded in differing formats. A clip bearing one stereo track, one 5.1 surround track, and six mono tracks, for example, can each be configured correctly in the Audio panel of Clip Attributes once that clip has been imported. The Audio panel of Clip Attributes now gives you a say over which format (Mono, Stereo, 5.1, 7.1, Adaptive) the channels embedded in a given clip ought to take. As a result, you can build clips with several tracks, each potentially drawing on a different audio format and a different mix of clips — a real convenience for mastering.

Clip Attributes now allows channels to be parceled out across separate tracks each holding its own channel assignments

### Timecode Attributes

Should you be wrestling with clips whose timecode is wrong, or whose timecode bears a faulty relationship to the EDL, XML, or AAF project you were handed, these attributes let you revise the timecode and reel name of clips in the Media Pool. Not one of these tools touches the source media sitting on disk; they merely rewrite the timecode metadata inside your DaVinci Resolve project, which in turn shapes the timecode of whatever media you render.

- Current Frame Timecode: Hands a fresh time to the timecode sitting at whatever frame of the clip you are presently viewing.
- Slate Timecode: When your source media stems from a shoot on which a timecode slate was used, you can register that slate timecode as a secondary timecode track usable for assorted operations — all without disturbing the clip’s primary timecode, which may already be carrying program sync.

To dial in the right Slate timecode, choose a Media Pool clip that shows a timecode slate, and park the playhead on a frame where the slate’s timecode reads clearly. Next, open the Timecode panel of the Clip Attributes window and key the timecode value you can read in the picture into the Slate Timecode field.

- Offset Source Timecode: When a whole batch of clips carries timecode that is simply shifted, you can fix that offset across however many selected clips you wish.

### The Timecode panel of the Clip Attributes window

### Reel Name Attributes

Within the General Options panel of the Project Settings, the “Assist using Reel Names” checkbox ranks among the most consequential settings for steering how conform behaves. It sits off out of the box, leaving Reel Names empty. That is perfectly fine for conform workflows where the file path or file name plus source timecode is all you need to pin each media file to its clip. Yet should reconforming your project’s clips demand more than that, ticking the “Assist using Reel Names” checkbox lets DaVinci Resolve lean on one of four methods to set reel names automatically for every Media Pool clip. The Clip Attributes dialog also opens the door to defining by hand how the Reel Names of one or more chosen Media Pool clips get assigned. That helps whenever certain clips in a project call for a different reel name extraction method, or for reel names entered by hand. After you have leaned on Clip Attributes to rewrite a clip’s reel names, those clips stop refreshing on their own when you adjust the “Assist using Reel Names” options in the Project Settings.

Before the reel name attributes in the Clip Attributes window can be edited, you have to switch on “Assist using Reel Names” under the General Options of the Project Settings and settle on a Reel Assist setting.

- Source clip file pathname: Derives the reel name by pulling it out of each media file’s path. This lets you draw a reel name from the whole file name or part of it, or from the whole — or part — of any folder name along the path enclosing that file. You spell out the extraction through the Pattern field.
- Pattern: A code laying out how a reel name ought to be pulled from the source clip pathname. Further notes on building patters come later in this chapter.

The Reel Name panel of the Clip Attributes Window

- Media Pool bin name: Here the reel name comes from whatever bin in the Media Pool holds that clip. In a stereoscopic workflow, for one, you might export offline stereo media using the “Left” and “Right” bin names — the bins they sit in — as reel names. Another case would be VFX undergoing incremental processing, filed into individually named bins like “VFX_Tuesday_10-12.”
- Embedding in Source clip file: Handy with file formats that tuck the reel name inside the media file itself. CinemaDNG and other digital cinema cameras, QuickTime files born of Final Cut Pro, and DPX frame files all number among the formats that can hold reel name header data.
- Source clip filename: Where no reel number has been defined, it is frequently simplest to fall back on the Source clip filename.
- User Defined: This choice surfaces only when you hand-edit the reel name for one or more chosen Media Pool clips by way of the Clip Attributes dialog. Picking User Defined lets you type whatever text string you please as the reel name.

### Update Timecode from Audio – LTC

Certain cameras provide no way to lock onto an outside timecode source. The timecode they record might be time of day or free run, yet it will not be frame-accurately matched to other cameras, to the dual system audio recorder, or to the digital slate. That turns multi-cam or dual sound system syncing into a slow, hands-on chore. DaVinci Resolve answers this so long as the footage the camera shot carries a timecode reference on its audio track from the shoot — achieved by feeding an externally generated timecode into the camera’s audio input. Pick that clip, or clips, in the media pool, then right-click one of the highlighted clips and choose “Update timecode from audio - LTC.” On its own and at once, DaVinci Resolve rewrites the clip timecode from the LTC it detects on the audio tracks. The clips are now yours to use as though they had been synced right on set.

### Changing Clip Thumbnails in the Media Pool

With the Media Pool set to Thumbnail mode, a small image stands in for each clip, defaulting to that clip’s first frame. Hover the pointer over any clip for a moment and you can scrub its thumbnail to preview the contents. Once you stop scrubbing, though, sliding the pointer off the clip snaps the thumbnail back to the first frame of media, which may or may not capture what the clip actually holds. If you prefer, this can be changed. To set a custom thumbnail for any clip: 1 Bring the pointer over the clip whose thumbnail you mean to customize. 2 Hover briefly, then scrub along to a frame that represents it well. 3 Right-click the clip and pick Set Poster Frame, or hit Command-P. To wipe out a clip’s custom poster frame:

- Give the clip a right-click and pick Clear Poster Frame, or else tap Option-P.

### Creating Subclips

Subclips hand you yet another route to organizing media within the Media Pool, since they let you split overlong clips into shorter pieces. Say a project’s director favors “rolling takes,” with several takes all captured inside one clip; you can pull those takes apart by turning each into a subclip. To make a subclip: 1 Pick any Media Pool clip to load it into the Viewer. 2 Lay down In and Out points marking the stretch you want carved into a subclip. 3 Then do one of these:

- Give the jog bar a right-click and pick Make Subclip.
- Pull a clip out of the Viewer, or the Source Viewer, and drop it onto the Media Pool.

4 Up comes a new subclip dialog, where you can title the subclip and, by ticking the checkbox, opt to use its full extents.
