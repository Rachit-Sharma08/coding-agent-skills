# Audio assistant dialog delivery standard and ripple delete silence for selected clip

Version: DaVinci Resolve 20.3 Reference Manual. Context: Working with audio in the edit page.
[Chapter index](INDEX.md) / [Previous section](dialogue-separator-track-fx-and-ducker-track-fx.md) / [Next section](audio-filters-and-izotope-rx4-interface.md)
<a id="source-audio-assistant-dialog---delivery-standard"></a> <a id="source-audio-compound-clips"></a> <a id="source-audio-mixer-controls"></a> <a id="source-audio-playback-for-variable-speed-clips"></a> <a id="source-displaying-audio-meters"></a> <a id="source-mute-and-solo-tracks-for-output"></a> <a id="source-opening-an-audio-compound-clip"></a> <a id="source-ripple-delete-silence-for-selected-clip"></a> <a id="source-the-audio-mixer"></a> <a id="source-the-ripple-delete-silence-dialog"></a> <a id="source-using-audio-filters"></a>

### Audio Assistant dialog - Delivery Standard

Audio Assistant dialog - Mix Progress

4 Once mixing wraps, you're free to audition the mix and, if you like, refine it further or throw it out entirely.

NOTE: Should a track land in the wrong category, right-click its track header, pick the proper category from the Track Category portion of the contextual menu, then run the Audio Assistant once more.

### Ripple Delete Silence for Selected Clip

On the Edit or Cut page timeline you can analyze a chosen clip and strip out its silences, drawing on the comparable tool over in Fairlight. Pick a clip, choose Clip > Audio Operations > Ripple Delete Silence, and the Ripple Delete Silence dialog opens.

- Threshold: Sets the highest audio signal level (in dB) that counts as silence. Anything sitting below the threshold is regarded as silence and stripped out. Raise the threshold and more audio gets removed.
- Pre Head: Defines how much silence, or pre-roll, sits ahead of each audible passage.
- Post Tail: Defines how much silence, or post-roll, sits after each audible passage.
- Minimum to Trip: Sets the least amount of silence (in frames) that gets

stripped from the chosen timeline clips. Larger numbers preserve more silent stretches in the audio. Smaller numbers yield more strips, though some leftover audio may sound “chopped up” where it cuts off sharply.

- Cross fade audio: Lays a basic crossfade across the surviving audio clips to ease the transition, provided your head and tail settings leave enough room.

### The Ripple Delete Silence dialog

To remove silences from a timeline clip: 1 Pick any clip on a track. 2 Go to Clip > Audio Operations > Ripple Delete Silence. 3 The chosen audio redraws with vertical red stripes that mark where the resulting silences fall and how long they run, based on the values you set in the Remove Silence dialog. 4 Hit Remove. Everything under the red stripes is cut away, and the surviving sections of the clip are ripple deleted together along the timeline.

### The Audio Mixer

On the Edit page the Audio Mixer is a pared-down take on the Fairlight page Mixer, built to hand you a tidy set of graphical controls for dialing in basic track levels (the Edit page has no track-level fader automation), panning stereo audio per track, and muting and soloing tracks as you go. Open it like so: Click the Mixer button over on the Interface toolbar. The Audio Mixer lays out a row of channel strips whose controls map to the Timeline's tracks, and each strip shows as many audio meters as that track has channels. By default a Main 1 channel strip sits at the far right, letting you ride the overall mix level. That said, any subs and mains you create on the Fairlight page show up at the mixer's right edge too.

The Audio Mixer, showing four channel strips that map to the Timeline's four tracks NOTE: Automation can't be recorded on the Edit page. For full mixing controls with complete automation recording, turn to the Fairlight page.

### Audio Mixer Controls

These controls live on every track's channel strip:

- Track Color: Tracks can each carry a distinct color code to keep you organized. The same colors show up in the timeline track header and on the Fairlight page.
- Track Number: This shows the number of the timeline audio track that the channel strip belongs to.
- Track Effects: To open one, double-click a track effect at the top of the fader controls. FX: Brings up the Track Effects controls in the Inspector. EQ: Brings up the Track Equalizer. DY: Brings up the Track Dynamics.
- Pan control: Lets you swing a Mono track's audio between left and right, flip a Stereo track's left and right channels, or work in surround.
- Name: The name of the audio track the strip represents. Should you have renamed the audio tracks in the Timeline, those names show here.
- Solo: Silences every track apart from the ones soloed.
- Mute: Switches that audio track off.
- dB: Reports the current level of that track in decibels.
- Fader: Drag each track's vertical fader with your mouse or other pointing device to

set that track's volume and record automation. Drag upward to raise volume, downward to lower it.

- Audio meters: Sitting to the right of each fader, the audio meters show the playback volume of every channel on that track. Each strip carries its own meters, one per channel that track has been configured for.

### Mute and Solo Tracks For Output

Engaging the Audio Mixer's Mute or Solo controls turns track audio off for playback as well as for output delivery. Be certain you've switched any needed tracks back on before you move to the Deliver page. Mute and solo on tracks can only be changed on the Edit, Cut, and Fairlight pages.

### Displaying Audio Meters

When all you need is a look at your program's levels, you can flip the display over to the “Control Room” audio meters in place of the Mixer. How many audio meters appear depends on the speaker configuration currently active under System Preferences in its Video and Audio I/O panel. To show the Audio Meters: Hit the Mixer button over on the Interface toolbar so the audio panel appears, then pick Meters out of the option menu in the upper-right corner.

### Audio Compound Clips

Audio compound clips are supported in DaVinci Resolve, and you build them the same way as any compound clip: select several audio clips, right-click one, and pick New Compound Clip. Compound clips that include video can now hold several audio items as well. Right-click an audio compound clip, pick Open in Timeline, and when it opens on the Edit or Fairlight page, breadcrumb controls show up under the Timeline so you can step out of the compound clip and return to the master Timeline.

### Opening an audio compound clip

### Audio Playback for Variable Speed Clips

Clips with variable speed effects on them — video or audio — can now be played back with the variable speed audio either pitch-corrected or not. A choice in the Speed menu of the Retime controls decides whether the audio gets pitch-corrected.

### Using Audio Filters

DaVinci Resolve ships with Fairlight FX, a collection of audio plugins specific to DaVinci Resolve that run natively across macOS, Windows, and Linux, delivering high-quality, professional-grade audio effects to every DaVinci Resolve user on every platform. Beyond those, DaVinci Resolve will work with third-party VST audio plugins on Mac OS X and Windows. Under Mac OS X, DaVinci Resolve also handles Audio Unit (AU) audio plugins. Install these effects on your machine and they turn up in the Audio FX panel of the Effects Library. With audio plugins you can treat single audio clips or whole tracks of audio — adding creative touches such as echo or reverb, or addressing mastering needs through noise reduction, compression, or EQ. Ways to apply audio filters to clips on the Edit page:

- To apply an audio filter to a clip: Drag whatever filter you want from the Audio FX panel of the Effects Library onto the Timeline clip you're targeting.
- To apply an audio filter to multiple clips: Pick every clip you intend to treat, then drag whichever filter you want out of the Effects Library's Audio FX panel onto any one of those selected clips.
