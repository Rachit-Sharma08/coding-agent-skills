# H 264 master and h 265 master

Version: DaVinci Resolve 20.3 Reference Manual. Context: Rendering media.
[Chapter index](INDEX.md) / [Previous section](tiktok-deliver-page-preset-and-presentations-preset.md) / [Next section](custom-preset-editing-import-and-export.md)
<a id="source-audio-only"></a> <a id="source-avid-aaf"></a> <a id="source-choosing-the-frameio-preset"></a> <a id="source-creating-and-using-your-own-presets"></a> <a id="source-final-cut-pro-7-or-x-xml"></a> <a id="source-frameio"></a> <a id="source-h264-master"></a> <a id="source-h265-master"></a> <a id="source-imf-studio-version-only"></a> <a id="source-premiere-xml"></a> <a id="source-pro-tools"></a>

### H.264 Master

Use this to output H.264 files covering an entire program. Once chosen, it defaults to single clip mode rendering, the Format becomes QuickTime, and the Codec becomes H.264. Quality, Encoding Profile, and Entropy Mode all become Auto; for Passes the default is Single; Key Frames arrive set to Automatic, and Frame Reordering comes switched on. For audio the Codec defaults to AAC with the Data Rate at 320 Kb/s and the Bit Depth at 16.

### H.265 Master

Use this to output H.265 files covering an entire program. Once chosen, it defaults to single clip mode rendering, the Format becomes QuickTime, and the Codec becomes H.265. Quality becomes Automatic, Encoding Profile becomes Main; for Passes the default is Single; Key Frames arrive set to Automatic, and Frame Reordering comes switched on. For audio the Codec defaults to AAC with the Data Rate at 320 Kb/s and the Bit Depth at 16.

### IMF (Studio Version Only)

To the right of this preset a dropdown supplies options for Generic, 20th Century Fox, and Netflix-qualified presets. The preset serves facilities that turn in IMF files as digital-only deliverables. A Preset Type dropdown lets you pick the right settings to fill the assorted locked IMFspecific parameters that show up.

### Frame.io

Sitting at the top of the Deliver page’s Render Settings panel, a Frame.io preset lets you render and upload a program for review. Every option in the Render Settings panel refreshes to show controls fitting this process. Down at the foot of the Render Settings list, an “Upload directly to Frame.io” checkbox decides whether the rendered output gets uploaded. A Description field gives you room to add a description that travels up with the rendered media.

### Choosing the Frame.io preset

Picking the Frame.io preset converts the Location field into a Frame.io field, and the Browse button lets you select a project and folder path that will receive the exported result.

Exporting to Frame.io narrows the choices available in the Resolution, Format, Video Codec, and Type dropdown menus down to whichever ones best suit Frame.io file sharing. Pick the export options you want, then press the Add to Render Queue button so this job joins the Render Queue just like any other export. As soon as that job finishes rendering, it moves on by itself to upload to Frame.io, and an upload percentage indicator shows up in the job listing reporting the progress of this upload. Because this upload runs in the background, you're free to keep doing other tasks in DaVinci Resolve as the file uploads. To check how much longer the upload needs from any other page, pick Workspace > Background Activity and open the Background Activity window.

Choosing a Frame.io account to deliver a program to To read further on Frame.io integration, turn to Chapter 13, “Frame.io and Dropbox Replay Integration.”

### Final Cut Pro 7 or X XML

A dropdown tied to this preset offers a choice between two distinct XML formats exported together with the media you're rendering:

- Picks the right settings for projects originally handed off from Final Cut Pro 7 to DaVinci Resolve through XML. It targets the scenario where you're rendering media bound for a return trip to Final Cut Pro (done by exporting an XML file from the Edit page). It Renders Individual Clips; on macOS the “Codec” setting falls back to Apple ProRes 422 (HQ); Output Size adopts the current Timeline Resolution as it stands; that value comes from the Master Settings panel inside the Project Settings; and Use Unique Filenames sits switched on. Picking this preset causes an XML of the timeline to be exported automatically beside the media, carrying path names that mirror the rendered clips.
- Picks the right settings for projects originally handed off from Final Cut Pro X to DaVinci Resolve through XML. It targets the scenario where you're rendering media bound for a return trip to Final Cut Pro X (done by exporting an FCPXML file from the Edit page). It Renders Individual Clips; under macOS the “Codec” setting reverts to Apple ProRes 422 (HQ); Output Size takes on whatever the current Timeline Resolution happens to be; you set that over in the Master Settings panel under the Project Settings; and Use Unique Filenames stays switched on.

Picking this preset causes an XML of the timeline to be exported automatically beside the media, carrying path names that mirror the rendered clips.

### Premiere XML

Picks the right settings for projects originally handed off from Premiere Pro to DaVinci Resolve through XML. It targets the scenario where you're rendering media bound for a return trip to Premiere Pro. It Renders Individual Clips; on macOS the “Codec” setting drops back to Apple ProRes 422 (HQ); Output Size matches the current Timeline Resolution as configured; that figure is read from the Master Settings panel within the Project Settings; and Use Unique Filenames remains switched on. Picking this preset causes an XML of the rendered timeline to be exported automatically beside the media, carrying path names that mirror the rendered clips.

### Avid AAF

Picks the right settings for projects originally handed off from Avid Media Composer or Symphony to DaVinci Resolve through AAF. This setting is NOT for exporting to Pro Tools. It targets the scenario where you're rendering media bound for a return trip to Media Composer, which you set up by exporting an AAF file out of the Edit page. Here the “Codec” setting falls back to DNxHR 444 12 bit; Output Size lines up with the current Timeline Resolution as it stands; that comes from the Master Settings panel under the Project Settings; and Render Clip with Unique Filename sits switched on. Picking this preset causes an AAF of the timeline to be exported automatically beside the media, carrying path names that mirror the rendered clips.

### Pro Tools

Beginning with DaVinci Resolve version 16, Pro Tools export has seen a major overhaul. The preset surfaces the right options so you can export, bound for Pro Tools, a specially formatted AAF project file together with linked audio files plus a linked reference video file, or send the same to any application able to import a Pro Tools formatted AAF file. While exporting through the Pro Tools preset, you have to use the AAF file generated and saved automatically at the target location, since it carries special formatting for Pro Tools and holds path names mirroring the rendered clips. Avoid exporting an AAF via the File > Export AAF/XML command, because that won't yield the right exchange file for Pro Tools and it won't behave correctly. Using the Pro Tools preset makes DaVinci Resolve produce the following: 1 Your selection in the Codec dropdown menu of the Audio panel governs whether the audio from the Timeline is exported as a set of files linked to a separate AAF, or as an AAF with the audio file embedded inside as one deliverable.

- Pick Linear PCM and the individual files come out linked to a standalone AAF interchange file
- Pick Embedded in AAF and you get one AAF that wraps embedded Broadcast WAV audio files inside it, all as a single deliverable

No matter whether you export separate files or one embedded AAF deliverable, every audio clip in the current Timeline can come out as individual mono or multichannel audio files. The usual mono round trip export running from DaVinci Resolve over to Pro Tools is the default arrangement, with the “Render one track per channel” box ticked inside the Audio tab of the Pro Tools Render Setting. Under this option, a 5.1 polyphonic .wav file gets exported as six individual mono .wav files. Should the “Render one track per channel” box be cleared, DaVinci Resolve will instead output multichannel polyphonic .wav files. When you go that route, it pays to confirm beforehand that Pro Tools handles the specific multi-channel formats you intend to export before you commit to this workflow. Every exported file holds each audio channel from the source media, even those channels muted in the audio panel of Clip Attributes. So however the video editor arranged the audio channels within the Timeline, you'll always hand over every channel of each audio clip to whoever handles your audio postproduction. 2 You may also bring in handles through the “Add X frame handles” option, found under Advanced Settings within the Video panel, which appends extra frames at the start and finish of each exported audio clip. That supplies the editing flexibility needed by whoever refines your audio. 3 The kind of audio file produced hinges on which video format you pick in the Video panel:

- Picking the MXF OP-Atom video format yields MXF audio files on export.
- Picking the QuickTime format yields Broadcast Wave files on export.

4 Every bit of video in your timeline will be rendered and output as one reference movie, using the format chosen in the Video panel, with all effects and titles baked in. Subtitles too can be burned into the reference movie or saved out as a file. Should you wish to supply a window burn, you can switch on visible metadata through the Workspace > Data Burn-In window. If exporting a reference movie isn't wanted, you can clear the Export Video box in the Video panel. Outputting through the Pro Tools preset exports an AAF of the audio tracks of the current Timeline, shaped so it imports cleanly into Pro Tools, or into any other digital audio workstation (DAW) software that gets along with the Pro Tools flavor of AAF import.

- Exported audio files carry the file name and timecode of the source media they came from, so relinking to the source media in Pro Tools stays possible if needed. For Video+Audio files synced inside DaVinci Resolve, the exported audio files take the timecode and name of the synced audio source file rather than that of the video clip.
- Whatever custom name you assigned a track travels out with it, ready for Pro Tools to use.
- All track and clip volume automation is exported, with all keyframes.
- iXML metadata is also exported, including channel names when available.

IMPORTANT: While exporting to Pro Tools on the Deliver page, audio effects are not exported nor baked in, so FairlightFX, EQ, Compression, Pitch, and Elastic Wave effects end up ignored. Should imported AAF files give you trouble, look for audio effects or audio compound clips inside the Timeline, and swap any you locate for duplicates of those same audio clips stripped of effects.

### Audio Only

This preset is built purely to produce an audio-only media file out of the Timeline. With video rendering switched off, its default is to render the Main 1 bus as one clip, putting out one track per channel through the MXF OP-Atom format, the Linear PCM codec selected, and a depth of 16-bits. That said, the QuickTime, MP4, and WAV formats can also be used, and 24- or 32-bit output is available too. On top of that, you may render other Mains or Submixes, or single out a specific Timeline Track to render. Lastly, the current program can be rendered as Individual Clips.

### Creating and Using Your Own Presets

When a certain group of settings keeps coming up in your work, you can convert it into a custom Easy Setup for quick recall. To create a new Easy Setup: 1 For a clean start, make sure Custom is picked from the preset panel, which unlocks every setting across the Render Settings pane. 2 Dial in the specific settings your new preset calls for across the Video, Audio, and File panels. 3 From the Render Settings Options menu, pick Save as New Preset. 4 Enter a name in the “Render Preset” dialog, then press Save. The new preset now appears within the Preset panel. To load a preset:

- Click whichever preset you want. Across the Render Settings pane, every setting shifts to match your chosen preset.
