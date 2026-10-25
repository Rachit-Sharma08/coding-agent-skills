# Audio channels when copying and pasting audio clips and auto align clips

Version: DaVinci Resolve 20.3 Reference Manual. Context: Modifying clips in the timeline.
[Chapter index](INDEX.md) / [Previous section](disabling-copying-and-pasting-timeline-clips.md) / [Next section](checking-and-fixing-your-results-and-clean-up-video-tracks.md)
<a id="source-apple-cinematic-mode-mac-os-only"></a> <a id="source-audio-channels-when-copying-and-pasting-audio-clips"></a> <a id="source-auto-align-clips"></a> <a id="source-duplicating-clips-and-transitions-in-the-timeline"></a> <a id="source-scene-cut-detection-on-the-timeline"></a> <a id="source-smart-reframe-studio-version-only"></a> <a id="source-split-photoshop-psd-layers-into-individual-timeline-tracks"></a> <a id="source-using-apple-cinematic-mode-in-davinci-resolve"></a>

### Audio Channels When Copying and Pasting Audio Clips

There’s one more thing to weigh when copying and pasting audio. While force pasting a clip onto a different track, the track whose Auto Select control you solo might carry an audio channel mapping that doesn’t line up with the clips you’re putting there. This crops up, for instance, when you copy stereo audio clips off a stereo track and paste them onto a mono audio track. DaVinci Resolve permits it, leaving you free to paste audio clips onto whichever track you please. That said, any extra audio channels in clips beyond what the audio track they sit on can support get muted. Happily, the fix is simple. Just right-click the track header of the troublesome audio track and reach for the Change Track Type To submenu to reset its channel mapping to something better suited to the clips you pasted in.

### Auto Align Clips

Auto Align Clips nudges one or more chosen clips so they line up with the timecode or audio waveforms of another clip carrying matching timecode or audio. It serves video clips, which can be lined up by timecode, as well as audio clips, which can be lined up by either timecode or waveform matching. Waveform matching is on the table too when you’re dealing with audio/video clips. Only a single clip per video or audio track may be selected for alignment, and every one of them lines up to whichever clip sits on the lowest-numbered video or audio track. Any selected clips lacking overlapping timecode or audio waveform stay where they are, left in their original spot on the Timeline. For instance, clip AA on track V1 overlaps clip BB on track V2 but not clip JJ on track V3 or clip KK on track V4. Select every clip and run Auto Align Edits, and clip BB slides to line up with clip AA, while clips JJ and KK stay put since they don’t overlap clip AA.

The starting Timeline, where clip AA and clip BB share a bit of overlapping audio yet sit out of sync

That Timeline once the Auto Align command has run; via audio waveform, clip BB got slipped into sync with clip AA. Clips JJ and KK were part of the selection too, but with no overlapping timecode or audio of their own they stayed where they were.

In a different case, clip AA on track V1 overlaps clips BB, CC, and DD over on tracks V2, V3, and V4 in turn. Select every clip and run Auto Align Edits, and clips BB, CC, and DD slide into alignment with clip AA.

The starting Timeline, where clip AA together with clip BB, CC, and DD all share overlapping audio yet sit out of sync.

That timeline once the Auto Align command has run. Every clip now sits in sync and the audio waveforms all line up. The rest of the clips shifted over to clip AA’s spot because it held the lowest place on the Timeline.

To use Auto Align clips: 1 Lay out the clips you’d like aligned together on the Timeline at one clip per track. Every clip syncs to the one on the lowest track number. They all need overlapping timecode or audio waveforms. 2 Pick every clip you want aligned (one per track only). 3 Right-click any one of the chosen clips; from the Auto Align Clips submenu, take your pick of “Based on Timecode,” or “Based on Waveform.” 4 Choose the track whose audio waveform you’d like to sync against. Pick Timecode and the operation happens instantly. Pick Waveform and a progress bar shows how long DaVinci Resolve needs to study the chosen audio waveforms before the clips line up. Should you have chosen clips that can’t be aligned, a warning box pops up naming which clips had errors. On the video side, this helps in multi-camera editing where you want an insert lined up with the action of an alternate angle. On the audio side, it helps where you hold several recordings of the same audio that you want aligned for more editing.

NOTE: Waveform matching falls short for re-recorded audio, like dialog redone with the ADR tools of the Fairlight page, because the match between two waveforms has to be exact before one can be found.

### Duplicating Clips and Transitions in the Timeline

You can duplicate one or more clips by selecting them, then Option-dragging the chosen clips to a different spot and/or track on the Timeline. Duplicating clips this way means holding the Option key down right up until you let go of the mouse button. Individual selected transitions duplicate the same way, by Option-dragging them onto another edit point.

### Smart Reframe (Studio Version Only)

DaVinci Resolve’s Smart Reframe feature smooths the job of quickly reframing material across drastic aspect ratio shifts. It comes in handy when you’ve shot a 16:9 horizontal video and now need a vertically-oriented 9:16 cut for mobile phones and social media deliverables, or when you’re dropping 4:3 archival footage into a 2.39:1 widescreen movie. Smart Reframe can run by hand or be carried out automatically through the DaVinci Resolve Neural Engine.

Smart Reframe at work, the Reference Point bounding box switched on (right) The Smart Reframe tool sits under the Sizing tab of the Inspector, and it’s on hand in the Cut page as well as the Edit page. Here is how to put the Smart Reframe tool to work: 1 Make a duplicate of your Timeline, right-click that Timeline and choose Timelines > Timeline Settings, then click Use Custom Settings to set the Timeline Resolution to whatever aspect ratio your delivery calls for. Confirm that “Mismatched resolution files” reads “Scale full frame with crop,” and click OK. 2 Pick one or more clips to reframe, then bring up the Inspector on its Video tab. 3 Bring up the Smart Reframe controls, keep the Object of Interest drop-down menu set to Auto (when more than one clip is chosen, Auto is the lone option), and click “Reframe.” DaVinci Resolve studies your footage and should shift each clip’s position on its own toward a more pleasing framing.

4 (Optional) Should the “Auto” setting fail to give you what you want on a given clip, you can pick the main subject by hand with these steps: a) To set the subject area yourself, pick “Reference Point” off the Object of Interest drop-down menu, then click the Target icon right beside the menu. That flips the Viewer mode to Smart Reframe on its own, revealing the onscreen controls for picking a reference. b) Drag the Reference Point bounding box over the chief subject of interest in the frame. The Transform controls just above in the Inspector can shift the source clip around when your subject falls outside the current framing. 5 (Optional) To hold the AI to reframing along one axis only, pick either Pan Only, or Tilt Only off the Mode selector. 6 Click Reframe.

The Smart Reframe controls in the Inspector, with the manual Reference Point picked DaVinci Resolve fixes onto, and tracks as needed, your subject by way of the reference you chose, panning and scanning the original clip automatically to hold that reference inside the new aspect ratio. Even though some manual tweaking is involved, this function still slashes the time that pan and scanning footage takes when you adjust and keyframe the sizing controls by hand.

### Split Photoshop PSD Layers into Individual Timeline Tracks

Right-click an Adobe Photoshop Document (.psd) sitting in a timeline and pick Split PSD Layers in Place to spread each of the file’s layers out onto its own track. How many new tracks get made will match how many layers the file holds.

Splitting Photoshop PSD layers onto individual tracks is done by rightclicking them and choosing Split PSD Layers in Place.

The results of splitting a PSD file. Since DaVinci Resolve reads and splits rasterized flattened layers, a few preparation steps fall on the underlying PSD asset ahead of import. Flattening layers by merging them in Photoshop is usually a hands-on task. The goal is to pare down the image structure, bake in Photoshop-specific effects, and rasterize fonts so everything stays compatible with DaVinci Resolve. Here’s the process step by step: Rasterize transparency and effects Where your layers/fonts hold effects such as shadows or gradients, merging can occasionally shift how they look. Think about rasterizing first. For that, select one or more layers, right-click, and choose Rasterize Layer Style. Doing the same for text layers is advised too. Merge and flatten similar layers Group similar layers together and select the ones you mean to merge. Right-click the selected layers and choose Merge Layers (Cmd/Control+E) to fold them into a single ‘flat’ layer. Depending on how involved the Photoshop document is, you might reach for the option: File > Scripts > Flatten All Layer Effects. Name layers Give the layers names that describe the image, effect, or element underneath. Naming the flattened layers now lets DaVinci Resolve carry those names through to the split clips.

### Apple Cinematic Mode (Mac OS Only)

Newer Apple iPhone models carry a Cinematic mode that leans on lidar to mimic the depth of field a lens iris produces. The mode lets you fabricate shallow depth of field looks or shift focus from one focal point to the next. You reach this capability right inside the Edit Timeline of DaVinci Resolve. Apple Cinematic mode at an F-Stop of 16; observe how the background stays in focus. That Yellow square marks the focus point.

Apple Cinematic mode at an F-Stop of 2; observe how the background goes blurred. That Yellow square marks the focus point.

### Using Apple Cinematic Mode in DaVinci Resolve

Bringing Cinematic footage shot on an iPhone into DaVinci Resolve takes a few extra steps, and the MacOS version is the only one where it works. Here is how to import iPhone Cinematic footage into DaVinci Resolve: 1 On the iPhone, switch the camera mode over to Cinematic before the video is shot. 2 Once the video is done, track it down in the Photos app and tap the Share icon. IMPORTANT: In the Share interface, select “Export Unmodified Original.” Send it by any other route (AirDrop, say) and the cinematic information gets stripped out of your video. 3 Pick a spot on your phone to save to within the Files interface. 4 Back in the Files interface, find the cinematic video, tap it, then hit the Share button once more. 5 Now send the cinematic video over to your computer by AirDrop or some other route. 6 Open DaVinci Resolve and bring the cinematic video into the Media Pool the usual way.

Set the Viewer Overlay to Cinematic mode (circled) via the drop-down menu. Here is how to put the Cinematic tools to work in DaVinci Resolve: 1 Drop a Cinematic Video clip onto the timeline and select it. 2 In the Viewer Overlay, pick Cinematic off the drop-down menu. 3 Over in the Video Inspector, the Cinematic toolset ought to show up at the bottom of the list. 4 Pick a recorded focus point in the Viewer, marked out by a yellow rectangle. 5 Work the F-Stop controls to dial in the depth of field.

### Scene Cut Detection on the Timeline

When you need an already-edited video broken into its component clips for re-editing or color correction, that can happen right in the Timeline. By way of the DaVinci Neural Engine, DaVinci Resolve can examine an edited video on its own and divide it into separate clips. Timeline Scene Cut Detection lives in the Cut page as well. Should you rather, the original Scene Cut Detection tool over in the Media Pool stays usable. To use Scene Cut Detection on the Timeline: 1 Pick one or more clips you’d like to split on the Timeline. As an alternative, you can confine Scene Cut Detection to just part of a clip by marking In and Out points on the Timeline around the stretch you want examined. 2 Choose Timeline > Detect Scene Cuts. Up comes a dialogue box reading “Detecting scene cuts in clips x of x.” The wait can stretch out depending on the length, count, and intricacy of whatever clips you picked. After the Scene Cut Detection wraps up, your chosen clip is split into a run of through edits that can now serve as standalone clips.
