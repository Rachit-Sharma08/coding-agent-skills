# Defining audio track types and rearranging tracks

Version: DaVinci Resolve 20.3 Reference Manual. Context: Setting up tracks busses and patching.
[Chapter index](INDEX.md) / [Previous section](audio-tracks-and-what-is-a-bus.md) / [Next section](multichannel-link-groups-and-element-editing.md)
<a id="source-changing-track-type"></a> <a id="source-defining-audio-track-types"></a> <a id="source-deleting-tracks"></a> <a id="source-disabled-tracks"></a> <a id="source-disabling-tracks"></a> <a id="source-duplicated-tracks-with-appended-names"></a> <a id="source-duplicating-tracks"></a> <a id="source-rearranging-tracks"></a> <a id="source-timeline-contextual-menu---delete-tracks"></a> <a id="source-timeline-contextual-menu---disable-tracks"></a> <a id="source-timeline-contextual-menu---duplicate-tracks"></a>

### Defining Audio Track Types

When you create a new audio track, you must decide what kind it will be. Right-clicking in the lower audio portion of the Timeline track header brings up a contextual sub-menu offering the various audio track types you can create.

- Mono: Holds a single channel with only one lane.
- Stereo: Holds stereo left and right channels, with two lanes.
- 3.0: Carries three channels across three lanes, in either LRC (Left, Right, Center) or LCR

(Left, Center, Right) format.

- 4.0: Carries four channels across four lanes, in either LRCS (Left, Right, Center, Surround), LCRS (Left,

Center, Right, Surround), or Quad format.

- 5.x: A 5.0 track carries five channels for a 5.0 surround mix, spread over five lanes in total. Under the broadcast SMPTE layout the order is Left, Right, Center, Surround Left, and Surround Right; under the cinema layout (5.0 Film) the tracks run Left, Center, Right, Left Surround, and Right Surround.

A 5.1 track carries six channels for a 5.1 surround mix, spread over six lanes in total. Under the broadcast SMPTE layout the order is Left, Right, Center, LFE, Surround Left, and Surround Right; under the cinema layout (5.1 Film) the tracks run Left, Center, Right, Left Surround, Right Surround, and LFE.

- 7.x: A 7.0 track carries seven channels for a 7.0 surround mix, spread over seven lanes in total. The broadcast SMPTE layout orders them Left, then Right, then Center, then Left Surround, then Right Surround, then Back Left Surround, and finally Back Right Surround; the cinema layout (7.0 Film) instead orders them Left, then Center, then Right, then Left Surround, then Right Surround, then Back Surround Left, and finally Back Surround Right.

A 7.1 track carries eight channels for a 7.1 surround mix, spread over eight lanes in total. The broadcast SMPTE layout orders them Left, then Right, then Center, then LFE, then Left Surround, then Right Surround, then Back Left Surround, and finally Back Right Surround; the cinema layout (7.1 Film) instead orders them Left, then Center, then Right, then Left Surround, then Right Surround, then Back Surround Left, then Back Surround Right, and finally LFE.

- Adaptive: Holds up to 24 audio channels, each with its own lane inside the track. A single Adaptive track can carry clips with differing channel counts, up to the ceiling set for that track. You set that ceiling (1–24) yourself when the Adaptive track is created. If you edit a clip carrying more channels than the Adaptive track was made to hold, the surplus clip channels are muted.
- Dolby Atmos: Several Dolby Atmos formats are on offer: 5.1.2, 5.1.4, 7.1.2, 7.1.4, and 9.1.6. The naming of these channel configurations folds the height channels into the nomenclature. A configuration is written as three digits separated by periods, like 7.1.4. The first digit gives the count of main, or ear-height monitoring, channels encircling the listener. The second digit gives the count of subwoofer channels. The third digit gives the count of height channels — speakers placed on the ceiling, or, with a soundbar, aimed at it.

NOTE: The 9.1.4, 9.16, and 22.2 Dolby Atmos bus formats exist solely in DaVinci Resolve Studio, and on top of that they demand that Dolby Atmos first be switched on under Preferences > Video and Audio I/O > Immersive Audio.

Adding Tracks (Contextual Menu) The right-click contextual menu on any audio track’s header controls carries two track-adding commands:

- Add Track: Inserts one audio track of whatever type you pick from a submenu.
- Add Tracks: Lets you add as many tracks as you wish, specifying their type and where they sit

among the other tracks in the Timeline.

### Rearranging Tracks

You can reorder tracks by right-clicking inside a track’s header area and selecting either Move Track Up or Move Track Down from the contextual menu that opens. Tracks can also be moved within the Index by grabbing them and dragging them to where you want them. That second approach works for relocating several tracks at once.

### Duplicating Tracks

To duplicate a track, right-click its header and pick “Duplicate Track” from the contextual menu. You can duplicate several tracks at once by selecting them, right-clicking any of the group’s headers, and choosing “Duplicate Tracks” from the contextual menu. Duplicate tracks have the word “copy” appended to their names.

### Timeline contextual menu - Duplicate Tracks

### Duplicated tracks with appended names

### Deleting Tracks

Right-click within a track’s Timeline header and pick Delete Track. Any clips on a track you remove are deleted from the Timeline along with it, but they stay safe in the Media Pool. To remove a batch of tracks from the Fairlight timeline, right-click any of the selected headers and pick Delete Tracks from the contextual menu. To purge every empty audio track from that timeline, right-click any header and pick Delete Empty Tracks from the contextual menu.

### Timeline contextual menu - Delete Tracks

### Disabling Tracks

To disable an audio track, right-click its track header and select Disable Track from the contextual menu. To turn off several tracks at once, select them, right-click any header in the group, and choose Disable Tracks from the contextual menu.

### Timeline contextual menu - Disable Tracks

### Disabled tracks

To switch your tracks back on, run through one of the selection methods according to how many tracks are involved, then pick Disable Track or Disable Tracks from the contextual menu.

### Changing Track Type

If you set your timeline up with one type of audio track but later realize a different type is what you need, you can change it whenever you like. Just right-click anywhere within that track’s Timeline header and select a choice from the contextual menu’s Change Track Type To submenu.
