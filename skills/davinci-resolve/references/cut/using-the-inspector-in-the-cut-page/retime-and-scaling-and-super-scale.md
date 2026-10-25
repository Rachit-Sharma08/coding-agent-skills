# Retime and scaling and super scale

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the inspector in the cut page.
[Chapter index](INDEX.md) / [Previous section](dynamic-zoom-and-composite.md) / [Next section](equalizer-and-clip-eq-in-the-audio-inspector.md)
<a id="source-audio"></a> <a id="source-cut-617"></a> <a id="source-retime-and-scaling"></a> <a id="source-super-scale"></a> <a id="source-the-audio-inspector-clip-and-track-parameters"></a> <a id="source-the-super-scale-parameters"></a> <a id="source-using-the-inspector-in-the-cut-page-part-2"></a>

### Retime and Scaling

Within the Video Inspector panel, the Retime and Scaling area carries four parameters governing retime quality and clip scale:

- Retime Process: On a clip-by-clip basis, lets you set a default way to process clips in mixed frame rate timelines and those carrying speed effects (fast forward or slow motion). The default is “Project Settings,” so every speed-effected clip gets handled identically.

You get three choices here, Nearest, Frame Blend, and Optical Flow, each covered at greater length in the Speed Effect Processing section see Chapter 51, “Speed Effects.”

- Motion estimation mode: When Optical Flow handles speed change effects or clips whose frame rate differs from the Timeline’s, the Motion Estimation pop-up lets you pick the best-looking render choice for a specific clip. Each approach carries its own artifacts, and the top-quality choice isn’t always right for a particular clip. The default is “Project Settings,” so every speed-effected clip is treated the same. Several options exist. The “Standard Faster” and “Standard Better” settings match the ones offered in earlier DaVinci Resolve releases. They use less processor power and produce good quality that suits most cases. That said, “Enhanced Faster” and “Enhanced Better” should deliver better results in almost every instance where the standard choices show artifacts, at the cost of heavier computation and therefore slower speeds on most systems.
- The “Standard Faster” and “Standard Better” settings match the ones offered in earlier

DaVinci Resolve releases. They use less processor power and produce

good quality that suits most cases. That said, “Enhanced Faster” and “Enhanced

Better” should deliver better results in almost every instance where the standard choices show

artifacts, at the cost of heavier computation and therefore slower speeds on

most systems.

- “Speed Warp Faster and “Speed Warp Better” come into play for even finer slow motion effects driven by the DaVinci Neural Engine. How well they work depends on what’s in the clip, but under the best conditions they deliver finer visual quality with fewer artifacts than even the Enhanced Better setting does.
- Scaling: On a clip-by-clip basis, lets you decide how clips that don’t fit the current project resolution are dealt with. The default is “Project Settings,” so every mismatched clip is automatically resized the same way. You can, however, also assign an individual automatic scaling method to any clip.

Your choices here are Crop, Fit, Fill, and Stretch; to read more, refer to Chapter 152, “Sizing and Image Stabilization.”

- Resize Filter: For any clip being resized in whatever way, this setting lets you pick the filter method used to interpolate image pixels during resizing. Different settings suit different kinds of resizing. There are four options:

Sharper: Generally gives the finest quality on projects whose clips have to be scaled up into a bigger frame size, or scaled down into HD resolutions. Smoother: Can deliver finer quality on projects whose clips have to be scaled down into an SD resolution frame size. Bicubic: Although the Sharper and Smoother choices edge it out slightly on quality, Bicubic remains a remarkably good resizing filter and demands less processor power than either of them. Bilinear: A lesser-quality choice that taxes the processor less. Handy for previewing your work on an underpowered computer ahead of rendering, after which you can swap in one of the higher-quality choices. Other Resize Methods: When you need to align with other VFX workflows, a range of particular resize algorithms is on hand.

- Deinterlace Quality (Interlaced Clips Only): Permits per clip deinterlace quality tuning of how DaVinci Resolve merges an interlaced clip’s two fields into progressive frames. Normal: A high-quality deinterlacing method suited to most clips. On many clips, Normal can’t be told apart from High. Normal is always applied automatically while playing back in DaVinci Resolve. High: A more processor-intensive approach that can occasionally give better results, depending on the footage, at the cost of slower render times. DaVinci Neural Engine: This choice uses the advanced machine learning algorithms of the DaVinci Neural Engine to study motion between the fields of interlaced material and rebuilds them into one frame. It is extremely computationally intensive but, in the best case, should produce an even more pleasing result than the “high” setting.

### Super Scale

### The Super Scale parameters

For those moments when you require finer upscaling than the regular Resize Filters offer, you can now switch on one of the “Super Scale” options in the Inspector. Unlike the many scaling options across the Edit, Fusion, or Color pages, Super Scale actually raises the source resolution of the clip being processed, meaning that clip ends up with more pixels than before and is heavier to work with than before, unless you optimize it (which bakes the Super Scale effect into the optimized media) or cache it somehow. To dig into Super Scale further, refer to Chapter 11, “Image Sizing and Resolution Independence.” Turning to Super Scale within the Inspector accomplishes the same thing as configuring the matching controls for the media clip over in the Clip Attributes. That means altering this setting affects every additional edit that references the selected media too. The Super Scale group carries the following parameters that govern quality and clip scale:

- Super Scale: Lets you pick how much scaling you need. Your choices are 2-3-4x and 2-3-4x Enhanced.
- Sharpness: Lets you set how much detail the scaling carries. The choice here is held to Low, Medium, or High, unless Super Scale mode runs in Enhanced, which opens up variable sharpness. You’ll want to weigh this setting against Noise Reduction.
- Noise Reduction: Lets you set how much noise reduction the scaling applies. The choice here is held to Low, Medium, or High, unless Super Scale mode runs in Enhanced, which opens up variable noise reduction. You’ll want to weigh this setting against Sharpness.

### Audio

### The Audio Inspector Clip and Track parameters

Depending on which icon you’ve picked at the upper left of the Inspector, the Audio Inspector can act on individual clips or on whole tracks. Usually this choice flips automatically for you based on what is selected in the timeline. As an example, clicking an audio clip in the timeline opens the Inspector in Clip mode, while clicking an audio track header switches the Inspector to Track mode by itself. You can always override these manually just by clicking the right icon. Clip and Track modes hold different options for audio editing.

The Audio Inspector in Clip mode (circled)

The Audio Inspector in Track mode (circled)

For the audio side of video editing, the Audio tab gathers the controls you reach for most, such as Volume, Pan, Pitch, and Equalizer. On top of that, it bundles several truly useful tools powered by the DaVinci Neural Engine, among them Voice Isolation, Dialog Leveler, and Music Remixer.

- Volume: Every clip carries one volume control, tied to the volume overlay drawn across each audio clip.
- Pan: A straightforward Pan slider that drives stereo panning. Although most professional mixes keep their panning to the sturdier panner over in the Fairlight page Mixer, this basic Pan control comes in handy for picture editors over on the Edit page who want to whip up simple panning moves to support a craft edit.
- Voice Isolation (Studio Version Only): Voice Isolation is a plugin built to strip loud, unwanted noises out of existing voice recordings. The effect leans on AI to supply models that let you fully erase undesired sounds. Trained on every kind of human voice, male or female, young or old, the AI model can deliver remarkable results isolating dialog from background noise in a recording, covering everything from air conditioning or fans to extremely loud sources like a jackhammer, restaurant chatter, or music playing while the subject talks, and beyond.

To read more about Voice Isolation, refer to Chapter 31, “Video and Audio Effects in the Cut Page.” Amount: This control sets how much voice isolation processing gets applied. To read more about Voice Isolation, refer to Chapter 181, “Fairlight FX.”

- Dialogue Leveler: The Dialogue Leveler studies source material to spot dialog and then “ride down” the louder stretches, “lift up” the softer ones, and pull down background noise that isn’t dialog. It does this without the usual dynamics processor “pumping” (compression/limiting) or other tell-tale side effects, giving results on par with meticulous hand-done clip gain moves or with laboriously “riding” the track using fader automation. Preset Menu: From the preset menu you get these choices:
- Optimized for most sources: Chosen by default, this one performs nicely across most sources.
- More lift for low levels: Pick this one when the source holds more low level dialog you’d like lifted.
- Lift soft whispery sources: Pick this one when the source carries whispered dialog alongside background noise. Reduce Loud Dialogue: With this on, louder dialogue is ridden down on its peaks and behaves much like a “perfect limiter” where you needn’t set a threshold or time constants. Owing to the “near real time” nature, analysis runs ahead of audible playback for the best results. Lift Soft Dialogue: With this on, it locates low level dialogue and lifts and evens out material that swings more in level and runs softer, yet since the process keeps its attention on dialogue, it generally avoids lifting background sounds (except when they land at the exact instant the dialogue does). In most cases, of the three choices the Lift Soft Dialogue one proves handiest, as it brings faint lines of dialogue forward and smooths them naturally without pushing up background noise. Background Reduction: With this on, it trims background sounds by locking onto dialogue and easing them out per the built-in presets (Preset menu). Output Gain: Set the Output Gain either by click-dragging on the Output Gain control or by typing a figure into the numeric field (the Output Gain control runs in dB across a 0 to +6 dB range at .1dB resolution).

### CUT 617

- Dialogue Separator (Track Mode Only): Leaning on the DaVinci Neural Engine AI, the Dialogue Separator hands you separate command over the dialogue level, the background sounds and "ambience," the reverberant field, and the ambient room sound. Say a source file carries a wonderfully roomy sound but music or crowd noise sits behind it; you can rebalance so those background sounds ease back a touch, or pull the room sound down somewhat for clearer intelligibility.

To read up further on the Dialogue Separator, turn to Chapter 31, "Video and Audio Effects in the Cut Page."

- Music Remixer: As an effect, the Music Remixer runs on DaVinci Neural Engine AI. Through AI, this Track FX plugin splits music into separate basic stems: Vocals, Drums, Bass, Guitar and "Other," meaning "everything else." The level controls let you rebalance or remix the sources, while the mute buttons trigger instant changes that pull parts into and out of your mix. Music Remixer hands you a creative way to bend a music track to your needs. As an example, a track might need its vocal removed, or rearranging to open up quieter moments or a build. CUT

For a fuller account of the Music Remixer, head to Chapter 31, "Video and Audio Effects in the Cut Page."

- Music Editor: Lets you smoothly stretch or trim music to match the length of your edit. Punch in a target duration and hit the Adjust button so the clip is shortened or lengthened to that figure. Rather than time compression/expansion or any pitch change to the music, Music Editor borrows a music editor's own editing tricks to fit the material to the length picture demands. It hunts for sensible spots to build transitions — depending on whether you are stretching length (by repeating sections) or cutting material — and tries to draw on the original composition's ending or fade where the timing works out. Where the ending is abrupt, crafting a fade out by hand falls to you.

Want more on the Music Editor? Look to Chapter 31, "Video and Audio Effects in the Cut Page." NOTE: As an "intelligent edit," Music Editor performs well on beat driven music (pop, dance, etc.). Free form, ambient, or non-beat driven material is not what it is built for.

- Ducker (Track Mode Only): With the Ducker Track FX plugin, a track's level can drop automatically off an external source signal — a behavior known as "ducking." Most often, ducking has dialogue or VO automatically pull down a music or sound effects bed, yet plenty of creative uses exist. Dialed in properly, your sources can frequently "mix themselves," yielding very useful results.

Only level changes drive the Ducker's work; the audio is neither compressed nor limited. For deeper coverage of the Ducker, refer to Chapter 31, "Video and Audio Effects in the Cut Page."

Settle on the target track you mean to affect (the "destination" track), then open the Ducker. Source: This is the source track whose signal ducks the target track's level. Press the +/- buttons on the right to add further source tracks or strip extra ones away. Duck Level: Tune how much "ducking" gets applied.

- Pitch: Lets you shift a clip's pitch while leaving its speed alone. Two sliders are on hand: one tunes clip pitch by semi tones (coarse moves, each a twelfth of an octave), the other by cents (fine moves, each 100th of a semi tone).
