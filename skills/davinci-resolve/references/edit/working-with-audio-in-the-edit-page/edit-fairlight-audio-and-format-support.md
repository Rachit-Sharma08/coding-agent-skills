# Audio in the edit vs Fairlight pages and compatible audio formats

Version: DaVinci Resolve 20.3 Reference Manual. Context: Working with audio in the edit page.
[Chapter index](INDEX.md) / [Next section](audio-track-layouts-and-clip-attributes.md)
<a id="source-a-single-audio-channel-exposed-in-the-timeline"></a> <a id="source-an-audio-clip-opened-into-the-source-viewer"></a> <a id="source-assigning-audio-channels-in-the-media-pool"></a> <a id="source-audio-in-the-edit-vs-fairlight-pages"></a> <a id="source-compatible-audio-formats"></a> <a id="source-editing-audio-into-the-timeline"></a> <a id="source-editing-audio-using-the-source-viewer"></a> <a id="source-how-to-assign-audio-channels"></a> <a id="source-mono-multichannel-audio-files-with-suffixes-import-as-a-multichannel-clip"></a> <a id="source-simultaneous-audio-waveform-display-in-the-source-viewer"></a> <a id="source-support-for-mixed-audio-track-formats-from-source-clips"></a> <a id="source-using-multi-channel-timeline-tracks"></a> <a id="source-working-with-audio-in-the-edit-page"></a> <a id="source-working-with-audio-in-the-edit-page-part-1"></a>

### Working with Audio in the Edit Page

Right inside the Edit page, DaVinci Resolve packs a robust toolkit for editing, mixing, and mastering the audio in your programs. No matter whether you are tweaking synced audio for dailies, polishing the levels of a cut you are putting together, mixing a program for output, or importing the sound designer’s audio mix files and laying them in so you can output them for mastering, DaVinci Resolve supplies Level, Pan, and Channel Assignment controls to govern your audio output across both monitoring and delivery, automated fader recording at the track level and the clip level for mixing, plus VST and Audio Unit audio filter support so you can master audio tracks and channels with industry-standard noise reduction, compression, EQ, and further filters. And should that still fall short, the Delivery page lets you export to Pro Tools, handing off your program along with its audio ready for more work. After you wrap the editorial audio work in your program and you want to really dig into its audio for fine-grained editing and mixing, the audio-focused tools on the Fairlight page are there. To read more, turn to Chapter 170, “Using the Fairlight Page.”

### Audio in the Edit vs. Fairlight Pages

Although the Fairlight page delivers purpose-built audio editing and mixing fit for sweetening your program’s audio once the edit is done, the Edit page brings broad audio powers of its own. Those let editors cut and refine audio clips, dial in levels, and run simple mixes while they first build the program. Once the pieces are cut together, though, the intent is for you to move freely between the Edit and Fairlight page as you polish, leaning on whichever environment best fits the job in front of you.

### Compatible Audio Formats

Among the formats DaVinci Resolve works with you will find WAVE and Broadcast WAVE, AIFF, MP3, AAC (M4A), CAF, plus iOS Voice Memo (macOS only), the AC3 audio format housed in either MTS or QuickTime containers, and Enhanced AC-3 (macOS and Windows only). When it comes to sample rates, the audio DaVinci Resolve handles runs to 32, 44.1, 48, 88.2, 96, and 192 kHz, among others.

### Assigning Audio Channels in the Media Pool

As soon as you bring audio into the Media Pool, it pays to confirm that whatever channels those files hold are mapped properly before you begin cutting clips into the Timeline. Put differently, you want stereo files set as stereo clips, 5.1 and 7.1 files set as surround clips, and multi-channel files set to surface as many tracks as you mean to edit on their own in your program. You make a clip’s channel assignments from the Audio panel of the Clip Attributes window. This matters especially once a clip carries more than two audio channels. Production sound recordists, for instance, may lay down three, six, or even more audio channels, one for each of the several microphones used on set to capture different actors at once, along with a mixdown track. In that situation you have to spell out how many of these channels should play (or stay muted), along with how many audio items belong on the Timelines of the Edit and Fairlight pages. Clips that are mono, stereo, 5.1, or 7.1 sort themselves out automatically, yet multi-channel clips that need custom assignments in the Media Pool ought to be remapped through Clip Attributes where needed, so DaVinci Resolve can more readily drop incoming audio clips onto the right Timeline track. You may change the clip attributes one clip at a time or for a batch of selected clips together. To read more about these settings, turn to Chapter 22, “Modifying Clips and Clip Attributes.”

### How to Assign Audio Channels

Within the Audio panel of the Clip Attributes window, every audio-bearing clip offers the options below:

The controls available for adding tracks with which to remap channels At the top of the Track/Channel list sits a group of controls for adding extra tracks to a clip. Those extra tracks let you remap the clip’s available channels so they show up as more items in the timeline once you edit it, with one item for each track that has an unmuted channel. The way you deal with audio in your timeline is your call. Take production audio made of five channels, four for separate microphones plus one mixdown channel: you might lean on Clip Attributes to fold every channel onto a single track.

A single-track clip carrying four channels, shown in the Clip Attributes window’s Audio panel

Under this mapping, the audio clip shows up as a lone item on a single Edit page Timeline track, or as five lanes within one track on the Fairlight page Timeline. Either way, you get one editable unit out of it.

### A single audio channel exposed in the Timeline

As another option, you could silence the four separate microphone channels and listen to only the top mixdown channel. To do that, set channels 2-5 to mute. Muted channels never go away, they simply are not heard, and you can switch them back on any time by right-clicking a clip in the Timeline and choosing Clip Attributes to return to these controls for the particular timeline clip you have cut.

A clip with four muted channels, shown in the Clip Attributes window’s Audio panel NOTE: When you export audio clips that have muted tracks to Pro Tools from the Deliver page, those muted channels go along in the export too.

A further alternative is to build these clips with five separate audio tracks, each carrying a single audio channel, so every channel surfaces on its own in the Timeline for independent editing. Begin by making the top track Mono using Embedded Channel 1. Next, through the Add channel controls at the top of the channels list, set Tracks to 4, the format to Mono, and click Add to spawn four more tracks beyond the one that clip started with. Pointing channels 2-5 at these fresh tracks gives the track mapping shown in the next screenshot. The Clip Attributes window’s Audio panel once four channels have been added Cut a clip like that into the Timeline and you wind up with five linked audio items spread across five separate audio tracks, every one of them editable on its own in the Timeline.

Each channel exposed as a separately editable clip in the Timeline

### Support for Mixed Audio Track Formats from Source Clips

DaVinci Resolve likewise handles media whose several audio tracks hold channels in differing formats. A clip bearing one stereo track, one 5.1 surround track, and six mono tracks, say, can all be configured properly from the Audio panel of Clip Attributes once that clip is imported. That Audio panel of Clip Attributes now lets you decide which format (Mono, Stereo, 5.1, 7.1, Adaptive) the channels inside a given clip take. So you can build clips of several tracks, each potentially drawing on a different audio format with a different mix of clips, which proves useful for mastering.

Through Clip Attributes you can now spread channels across separate tracks, each holding its own channel assignments.

### Mono-Multichannel Audio Files with Suffixes Import as a Multichannel Clip

DaVinci Resolve can read mono audio files carrying channel-name suffixes and bring them in as one formatted multichannel audio clip. Which format results turns on how many files it finds and what their channel suffixes are. To illustrate, Audio001.L.wav and Audio001.R.wav on their own come in as a stereo ‘Audio001.wav’ clip. Add a third file bearing a ‘C’ or ‘LFE’ suffix and you get LCR or 2.1 formatted media.

Importing multi-mono audio files to a single multichannel track

### Editing Audio Into the Timeline

In the Edit page Timeline, a distinct group of audio tracks holds every bit of audio you cut into the Timeline, plus any standalone audio files that may have arrived together with an AAF or XML file.

### Editing Audio Using the Source Viewer

Load an audio-only clip into the Source Viewer, or load a clip holding both video and audio and switch the Viewer to Audio Waveform, and you get a split view: the full waveform of the whole source clip fills the top half, while the bottom half carries a magnified slice of the waveform that you can zoom from 1x to 50x via the Zoom menu in the Source Viewer’s upper-left corner. From here it is easy to drag the box up top to locate the audio section you need against the entire clip, all while still dropping In and Out points precisely with the scrubber bar underneath. This view lays out every channel inside each track of the current clip. Just as with any other clip, you can add markers and lay down In and Out points for audio clips to get ready for editing.

### An audio clip opened into the Source Viewer

### Simultaneous Audio Waveform Display in the Source Viewer

You can also edit off audio waveforms even with the Source Viewer set to Source. A pair of options in the Option Menu put a superimposed audio waveform along the foot of the Viewer, laid over the video of whichever clip is selected.

- Show Current Frame Audio Waveform: Displays a magnified stretch of audio that scrolls along as the clip plays. Handy for catching dialog and music cues while you run through a clip.
- Show Full Clip Audio Waveform: Displays the audio waveform spanning that clip’s whole source media, with the stretch between the In and Out points you set in the Source Viewer highlighted. Handy for steering through the clip by treating the audio waveform as a reference.

With “Show Current Frame Audio Waveform” switched on, the Source Viewer puts the audio waveform along the foot of the picture

### Using Multi-Channel Timeline Tracks

Multi-channel audio tracks on the Edit page Timeline come in handy when your clips are stereo, 5.1, 7.1, or carry some arbitrary count of channels captured in the field, because you can pack all those channels as one clip onto one track, correctly routed to your project’s outputs and easily handled as a single item in the Timeline. Open the Fairlight page, though, and you will find that while the total tally of audio tracks matches the Edit page, the Fairlight page presents the channels the Edit page keeps hidden as lanes inside each track, surfacing every channel as a visible audio item in the Timeline. That way editors can deal with multi-channel audio free of visual clutter, while audio editors and mixers get to see every channel on every track to finish their work. Returning to audio tracks on the Edit page, several kinds exist, paralleling the several kinds of audio clip: Mono, Stereo, 5.1, 7.1, and Adaptive. Although you can cut any sort of audio clip into any sort of audio track, any clip audio channels beyond the channel count a given timeline track type holds get muted. Nothing stops you, for instance, from cutting a six-channel Adaptive audio clip onto a Mono audio track, yet you will hear only its first channel, since a Mono track puts out a single channel. For that reason, it pays to lay out your timeline so each clip rides on a track able to hold the channel count it carries. TIP: Cut an audio clip into the undefined gray region below the existing audio tracks in the Timeline and new audio tracks spring up automatically, matching in count the number of tracks the clip you drag holds, with every new track given audio mappings that fit the incoming audio items.
