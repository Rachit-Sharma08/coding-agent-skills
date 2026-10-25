# Introduction to multicam editing and creating and modifying multicam clips

Version: DaVinci Resolve 20.3 Reference Manual. Context: Multicam editing.
[Chapter index](INDEX.md) / [Next section](multicam-clip-adjustment-and-editing.md)
<a id="source-changing-the-start-timecode-for-multicam-clips"></a> <a id="source-converting-compound-clips-or-timelines-to-multicam-clips"></a> <a id="source-creating-and-modifying-multicam-clips"></a> <a id="source-introduction-to-multicam-editing"></a> <a id="source-logging-and-editing-multicam-clips"></a> <a id="source-multicam-clip-badge-in-the-timeline"></a> <a id="source-multicam-editing"></a> <a id="source-multicam-editing-part-1"></a> <a id="source-new-multicam-clip-properties-dialog"></a> <a id="source-selecting-a-single-reference-audio-track-for-multicam-clips"></a> <a id="source-setting-up-a-timeline-for-multicam-editing"></a> <a id="source-using-native-audio-channels-from-source-when-editing-multicam-angles"></a>

### Multicam Editing

When your footage was captured at the same moment by several cameras, the Multicam Editing features in DaVinci Resolve let you build multicam clips that you cut together through a visual switcher. There are also separate controls for swapping the angles of multicam clips that you have already placed into the Timeline.

### Introduction to Multicam Editing

For programs where a performance, an interview, or some event was captured by several cameras rolling at once, DaVinci Resolve supplies dedicated multi-camera editing features — multicam editing for short. Cutting with these features happens across three stages:

- To begin with, you assemble multicam clips out of each separate camera angle (these are known as “ISOs,” or isolated cameras).
- Next, you place the multicam clips you just built onto a timeline.
- Finally, you switch on the Multicam Viewer, at which point you can begin cutting and switching between

angles, much like a director working a live multi-camera show. The steps below walk through each of those stages, plus the choices you have at every step.

### Creating and Modifying Multicam Clips

The very first thing required is to build at least one multicam clip. To make a multicam clip: 1 Bring every ISO (isolated camera) clip belonging to the multi-camera performance or event you intend to edit into the Media Pool. 2 Highlight all of the clips that should be synced as a group, right-click that selection, and pick “Create Multicam Clip Using Selected Clips.” 3 Once the New Multicam Clip Properties dialog appears, set the options described below:

### New Multicam Clip Properties dialog

Start Timecode: Displays the starting timecode for the multicam clip you are creating, derived either from the timecode of the sync point when Angle Sync uses timecode, or from the sync-point timecode of whichever clip carries the earliest timecode when Angle Sync uses waveform. Multicam Clip Name: Lets you supply a label more meaningful than “Multicam 1” for the clip you are about to make.

Frame Rate: Reports automatically the frame rate tied to the clips you picked. There is a Drop Frame checkbox available when your clips run drop frame timecode. Angle Sync: The technique that lines up every separate angle. When you sync angles by hand, you can rely on In or Out points placed inside each clip. When matching timecode was jam synced onto each camera shooting an angle, pick Timecode for a quick sync that is only as precise as the timecode itself. When every camera carried a microphone capturing the location audio at the same time, pick Sound so the form of each audio waveform aligns the angles. When you have placed your own sync point markers onto the clips by hand, pick Marker. Channel: When Sound is chosen as the Angle Sync type, you can pick which audio channel from the clip serves as the sync source. Angle Name: The technique that labels each angle inside the multicam clip you are building. Angles can carry Sequential numbering, draw on Angle or Camera metadata, or take the Clip or File name. Split Multicam at gaps: When Sound is your Angle Sync type, you can have the Multicam files split wherever there is a break in the audio. Detect clips from same camera: Switching on this checkbox causes several clips recognized as coming from one camera to be gathered onto a single angle track within the resulting multicam clip. It also turns on the “Detect using” drop-down menu. Detect Using: Which metadata decides which clips originate from the same camera. The options are Camera #, Angle, Reel Number, Reel Name, and Roll/Card #, all of which you can edit in the Metadata Editor of the Media page, or you can pick Reel Name, which is set up — by hand or on its own — through the Conform Options found in the General Options panel under Project Settings, or alternatively through the Name panel of the Clip Attributes window. The Conform Options are covered more fully in Chapter 4, titled “System and User Preferences.” Move Source Clips to “Original Clips” Bin: Ticking this box sends each source ISO clip off to an Original Clips bin, tucking them aside once your multicam clip has been built. Use source audio channels: When ticked, this opens up the separate tracks and channels in the source clip’s audio (described further below). 4 After your options are set, click Create. Based on the Angle Sync method picked, a waveform analysis may show a progress bar, after which the new multicam clip appears in whatever bin is currently active in the Media Pool. Multicam clips carry a multicam badge in the lower left corner of the clip thumbnail.

A multicam clip showing its badge in the Media Pool

### Using Native Audio Channels from Source when Editing Multicam Angles

The multicam creation dialog offers an option called Use source audio channels, which is switched on by default. While it is on, the multicam clip is built in a mode that opens up the separate tracks and channels of the source angle. If that layout doesn’t work for you, untick the option and every audio track and channel for an angle is consolidated onto one adaptive track sized to hold all of the source’s audio channels. The multicam clip audio then sits on a timeline on an adaptive track. Native audio channels give you access to the individual tracks within the source angle. After a multicam clip is built with the option on, you can audition the audio tracks in the Audio Configuration section of the inspector File tab. With the option off, the multicam clip audio drops onto an adaptive track. With it on, the audio follows the track format of the source. Multicam audio clips can additionally pick alternative mono audio channels from the timeline clip context menu (Command right-click works for quicker access) and from the timeline clip audio configuration section in the Inspector.

### Selecting a Single Reference Audio Track for Multicam Clips

In DaVinci Resolve, multicam clips can adopt reference audio files (for example, those captured by a separate sound mixer) as the audio track shared by every angle, provided you attach an audio file to your multicam clip. While building the multicam clip, choose Reference Audio/Angle 1 in the Multicam Audio selector. That choice locates the first audio-only angle automatically and assigns it as the reference audio for all remaining angles. When a multicam setup contains no audio-only angle, the first angle is used automatically as the reference audio for the clip. While cutting multicam, you can reach the channels underlying the reference audio angle by Command-rightclicking the clip, just as you would with source audio multicam clips.

Setting up the Reference Audio track in a multicam clip

### Changing the Start Timecode for Multicam Clips

The starting timecode can be altered for both multicam and compound clips. To do this, right-click the multicam or compound clip in the Media Pool and pick Starting Timecode from the context menu. A Set New Start Timecode box appears; enter the fresh starting timecode you want and click OK.

### Converting Compound Clips or Timelines to Multicam Clips

Compound clips and timelines can be turned into multicam clips for simpler editing by way of the Edit page’s Multicam Editing interface. The conversion only runs one direction. There is no way to turn a multicam clip back into a timeline or compound clip. To hold on to the original timeline or compound clip, be sure to duplicate it first and convert the copy. To turn a compound clip or timeline into a multicam clip:

- Right-click the clip or timeline in the Media Pool and pick “Convert Compound Clips (Timelines) to Multicam Clips” from the drop-down menu.

### Logging and Editing Multicam Clips

After one or more multicam clips exist, you can review them either in the Media page or within the Edit page’s Source Viewer, then drop markers onto them (the markers are shared across every angle) to set up for the multicam edit you have planned. While reviewing multicam clips on the Media page, the Viewer Option menu lets you decide how many angles appear in the viewer.

Markers placed on a multicam clip within the Media page in readiness for cutting

### Setting up a Timeline for Multicam Editing

With one or more multicam clips built, getting them ready to edit is just a matter of cutting them into the Timeline, either by dragging the multicam clip from the Media Pool onto the Timeline, or by loading the multicam clip into the Source Viewer and then applying any of the editing methods on hand to drop it into the Timeline. After they are edited in, they sit in the Timeline like any clip, only with a multicam badge to the left of the clip name.

### Multicam clip badge in the Timeline

While you carry out a multicam edit, DaVinci Resolve runs the whole audio mix as you cut, so if you would like to take that chance to edit a master audio mix file or an extra piece of music to accompany the multicam clip, you are free to do so.
