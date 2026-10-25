# Audio

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the inspector in the edit page.
[Chapter index](INDEX.md) / [Previous section](video-inspector-stabilization.md) / [Next section](equalizer-and-clip-eq-in-the-audio-inspector.md)
<a id="source-audio"></a> <a id="source-the-audio-inspector-clip-and-track-parameters"></a> <a id="source-using-the-inspector-in-the-edit-page-part-2"></a>

### Audio

### The Audio Inspector Clip and Track parameters

The Audio Inspector operates on either individual clips or whole tracks, depending on which icon is chosen at the Inspector’s upper left. As a rule this option sets itself for you

according to what you’ve selected in the timeline. Click an audio clip in the timeline, for instance, and the Inspector opens in Clip mode; click an audio track header, and it flips to Track mode on its own. You can always override these manually just by clicking the right icon. Clip and Track modes carry different options for audio editing.

The Audio Inspector in Clip mode (circled)

The Audio Inspector in Track mode (circled)

The Audio tab gathers the audio controls used most often in video editing, among them Volume, Pan, Pitch, and Equalizer. It also holds several remarkably handy DaVinci Neural Engine powered tools such as Voice Isolation, Dialog Leveler, and Music Remixer.

- Volume: Every clip carries one volume control tied to the volume overlay drawn across each audio clip.
- Pan: A basic Pan slider governing stereo panning. Although most professional mixes confine panning to the more capable panner in the Fairlight page Mixer, this simple Pan control helps picture editors on the Edit page quickly whip up basic panning effects to support a craft edit.
- Voice Isolation (Studio Version Only): Voice Isolation is a plugin built to strip loud, unwanted sounds out of existing voice recordings. The effect draws on AI models that let you fully eliminate the sounds you don’t want. Its AI model is trained on every sort of human voice — male or female, young or old — so you can achieve striking results that pull dialog clear of background noise in a recording, covering everything from air conditioning or fans to extremely loud sources like a jackhammer, restaurant chatter, or music playing while the subject speaks, and beyond.

For a fuller treatment of Voice Isolation, turn to Chapter 45, “Working with Audio in the Edit Page.” Amount: Lets you dial how much voice isolation processing is applied.

- Dialogue Leveler: The Dialogue Leveler studies source material to find dialog, then “rides down” the louder stretches, “lifts up” the softer ones, and turns down background sounds that aren’t dialog. It does so without the usual dynamics-processor “pumping” (compression/limiting) or other obvious artifacts, giving results akin to meticulous manual clip gain work or to carefully “riding” the track with fader automation.

Preset Menu: The preset menu offers these choices:

- Optimized for most sources: Chosen by default, this works well across most sources.
- More lift for low levels: Pick this when the source carries more low-level dialog that

you’d like to boost.

- Lift soft whispery sources: Pick this when the source holds whispered dialog and background noise.

Reduce Loud Dialogue: Once on, louder dialogue gets ridden down on its peaks, behaving rather like a “perfect limiter” for which you needn’t set threshold or time constants. Thanks to the “near real time” design, analysis runs ahead of audible playback for the best outcome. Lift Soft Dialogue: Once on, it locates low-level dialogue and lifts and evens out material that runs softer and more uneven in level, yet because the process zeroes in on dialogue it generally won’t raise background sounds (unless they coincide with the dialogue itself). More often than not, Lift Soft Dialogue proves the most useful of the three, since it brings barely-audible lines of dialogue up to an audible, naturally smooth level without amplifying background noise.

Background Reduction: Once turned on, it tones down background sounds by zeroing in on dialogue and easing them out per the internal presets (Preset menu). Output Gain: Dial in the Output Gain by clicking and dragging the Output Gain control, or else type a value straight into the field for numbers (the Output Gain control runs in dB across a 0 to +6 dB range at .1dB resolution).

- Dialogue Separator (Track Mode Only): Leaning on DaVinci Neural Engine AI, the Dialogue Separator hands you separate command over the dialogue level, the background sounds and "ambience," the reverberant field, and the ambient room sound. Say a source file carries a wonderfully roomy sound but music or crowd noise sits behind it; you can rebalance so those background sounds ease back a touch, or pull the room sound down somewhat for clearer intelligibility. To read up further on the Dialogue Separator, turn to Chapter 45, "Working with Audio in the Edit Page."
- Music Remixer: As an effect, the Music Remixer runs on DaVinci Neural Engine AI. Through AI, this Track FX plugin splits music into separate basic stems: Vocals, Drums, Bass, Guitar and "Other," meaning "everything else." The level controls let you rebalance or remix the sources, while the mute buttons trigger instant changes that pull parts into and out of your mix. Music Remixer hands you a creative way to bend a music track to your needs. As an example, a track might need its vocal removed, or rearranging to open up quieter moments or a build. For a fuller account of the Music Remixer, head to Chapter 45, "Working with Audio in the Edit Page."
- Music Editor: Lets you smoothly stretch or trim music to match the length of your edit. Punch in a target duration and hit the Adjust button so the clip is shortened or lengthened to that figure. Rather than time compression/expansion or any pitch change to the music, Music Editor borrows a music editor's own editing tricks to fit the material to the length picture demands. It hunts for sensible spots to build transitions — depending on whether you are stretching length (by repeating sections) or cutting material — and tries to draw on the original composition's ending or fade where the timing works out. Where the ending is abrupt, crafting a fade out by hand falls to you. Want more on the Music Editor? Look to Chapter 45, "Working with Audio in the Edit Page."

NOTE: As an "intelligent edit," Music Editor performs well on beat-driven music (pop, dance, etc.). Free form, ambient or non-beat driven material is not what it is built for.

- Ducker (Track Mode Only): With the Ducker Track FX plugin, a track's level can drop automatically off an external source signal – a behavior known as "ducking." Most often, ducking has dialogue or VO automatically pull down a music or sound effects bed, yet plenty of creative uses exist. Dialed in properly, your sources can frequently "mix themselves" and yield very useful results. Only level changes drive the Ducker's work; the audio is neither compressed nor limited.

For deeper coverage of the Ducker, refer to Chapter 45, "Working with Audio in the Edit Page." Settle on the target track you mean to affect (the "destination" track), then open the Ducker. Source: This is the source track whose signal ducks the target track's level. Press the +/- buttons on the right to add further source tracks or strip extra ones away. Duck Level: Tune how much "ducking" gets applied.

- Pitch: Lets you shift a clip's pitch while leaving its speed alone. Two sliders are on hand: one tunes clip pitch by semi tones (coarse moves, each a twelfth of an octave), the other by cents (fine moves, each 100th of a semi tone).
