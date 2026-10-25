# Dialogue separator track FX and ducker track FX

Version: DaVinci Resolve 20.3 Reference Manual. Context: Dialogue separator track FX studio version only, Ducker track FX.
[Chapter index](INDEX.md) / [Previous section](dialogue-leveler-and-music-remixer-and-music-editor.md) / [Next section](audio-assistant-delivery-and-silence-removal.md)
<a id="source-adding-ducker-input-sources-in-the-inspector"></a> <a id="source-audio-assistant-studio-version-only"></a> <a id="source-beat-detector-studio-version-only"></a> <a id="source-dialogue-matcher-studio-version-only"></a> <a id="source-dialogue-separator-track-fx-studio-version-only"></a> <a id="source-ducker-controls"></a> <a id="source-ducker-track-fx"></a> <a id="source-the-dialogue-separator-plugin"></a> <a id="source-the-ducker-plugin"></a> <a id="source-the-initial-music-is-too-long"></a> <a id="source-using-the-ducker"></a>

### The initial music is too long

Here the Music Editor has shortened the audio clip so its length lines up with the video. Observe the jagged lines across the audio clip, which flag where the original got cut. Within the waveform, notice that the tail of the music carries over into the retimed clip. TIP: Although the timing is often very close, it isn't always precise. When you require an exact result after using AI Music Editor, consider the Elastic Wave tool over on the Fairlight page, picking the general purpose (music) algorithm. What you end up with is really a dedicated Music Editor clip, so you can keep refining the edit. To reach the edit beneath, right-click the clip and decompose, which reveals the edit points along with whatever crossfades were generated. Bear in mind, though, that after decomposing you can no longer trim the clip's overall length as a unit, since every editing fragment has become its own clip.

### Dialogue Separator Track FX (Studio Version Only)

Powered by DaVinci Neural Engine AI, Dialogue Separator hands you separate control over the levels of dialogue, of background sounds, and of the reverberant field or ambient room tone (“ambience”).

### The Dialogue Separator plugin

Take a case where a source file has wonderful roomy character but carries music or crowd noise underneath — that's where the Dialogue Separator earns its keep. Here you can rebalance the mix to pull down the background sounds, or tweak the room sound so the dialogue reads more clearly.

A second scenario: somebody walking toward the camera in a roomy space as they talk. Automation could rebalance things so the ambient room tone steadily grows “drier” as the person nears, leaving the background untouched. At present, Dialogue Separator works in mono only. Stereo sources have to be broken into dual-mono, with each mono track handled on its own.

### Ducker Track FX

With this plugin you tap the audible signal from one or several tracks to pull down the level of another. There are plenty of creative applications, but the usual point of “ducking” is to automatically dip a music or sound effects bed so dialogue or a VO track sits more clearly out front in the mix — and it does so without compressing the signals coming in. Configure it properly inside the Ducker interface, or through the Audio tab in the Inspector, and your tracks will all but “mix themselves.” As a basic example, the Ducker reads the level changes of one incoming dialogue or VO track and reduces the volume on the sound effects bed of a noisy freeway. Take a trickier setup — three people talking beside that same noisy freeway — and a lone Ducker plugin can read each dialogue track's level changes to hold down the traffic noise. Given a single input source (Dialogue 1), the Ducker only kicks in while the first person talks. This newer capability, though, lets you bring in the remaining two dialogue tracks (Dialogue 2 and Dialogue 3) as further input sources for taming the traffic noise.

### The Ducker plugin

### Using the Ducker

Picking up from the use cases above: 1 Pick the target track you mean to attenuate (the Freeway Traffic track) and launch the Ducker. 2 Open the Source dropdown and pick Dialogue 1 to serve as the input source.

- For extra input sources, Command-click the remaining track names — here, Dialogue2 and Dialogue3.
- Run a portion of your sequence and tune the duck level along with the rest of the controls until it sounds right.

Adding Input Sources via the Inspector If the Inspector is where you'd rather work:

- Pick the Freeway Traffic track, confirm the Ducker is turned on, and bring up the

Inspector’s Audio tab.

- Hit the plus sign beside the Source 1 dropdown that holds Dialogue1, which spins up a

dropdown menu for Source 2; from there choose Dialogue2 in the list.

- Hit the plus sign beside the Source 2 dropdown to spin up a dropdown menu for

Source 3, then pick Dialogue3 in the list.

### Adding Ducker input sources in the Inspector

### Ducker Controls

- Duck Amount: Governs how much the target track is attenuated, measured in dB, defaulting to 2.7 dB. In most cases a setting from 2.0 dB to 5.0 dB performs best.
- Lookahead: Tunes how much lookahead time, in milliseconds, is used; the default is 15ms. Lookahead lets the Ducker begin attenuating the destination track before the source track becomes audible.
- A bigger value makes the Ducker “pre-anticipate” the source track to a greater degree. Should you want the Ducker dipping the sound ahead of a line of dialogue or VO, try pushing the value higher, though the default tends to give solid results.
- Rise Time: Sets the number of milliseconds the Ducker takes to arrive at the reduction defined by the Duck Amount. Its default is 10 milliseconds, fine for the majority of cases. Longer Rise Times can help when you're running higher Duck Amount values and there are longer gaps in the source track.
- Hold: Controls the duration over which the target signal stays attenuated. Default is 150ms.
- Recovery Time: Specifies how fast the target signal climbs back to where it was once attenuation lets up. The default sits at 750ms, but dialing in the right Recovery time matters a lot for natural-sounding ducking, so experiment with several values to land on the best one.

Ducker Graph Display Within this region a grey line plots the incoming signal alongside the Ducker's behavior, drawn in yellow. Where the yellow line dips, the target track is being attenuated according to the Duck Amount working together with the remaining parameters.

### Beat Detector (Studio Version Only)

For a piece of music sitting on the timeline, DaVinci Resolve is able to find the beats on its own, and it lets you snap to those beat marker positions. That comes in handy whenever you're cutting to the beat. NOTE: For now the Beat Detector functions reliably only with beat-driven music and only at 4/4 or 3/4 time signatures. Right-click the timeline audio clip and pick Detect Music Beats from the context menu to run the detection. After analysis, beat indicator overlays appear on the timeline clip, and you can snap other timeline elements to them.

A music track carrying the Beat Detector. Its lined overlays line up against the music's beat.

### Dialogue Matcher (Studio Version Only)

Using Dialogue Matcher, you can align one piece of dialogue to another so the level, EQ, and reverb agree. It's handy when fresh recordings don't sit in the same environment as existing material. Fully automated, the Dialogue Matcher only asks the user to grab a tone profile off one clip and then apply it onto another.

Capturing a Dialogue Profile off a clip by way of the main menu To Use Dialogue Matcher: 1 Pick a reference clip carrying the dialogue you want to match, right-click, and pick Clip > AI Tools > Dialogue Matcher > Capture Dialogue Profile. 2 Pick the clip whose dialogue should change, right-click, and pick Clip > AI Tools > Dialogue Matcher > Apply Dialogue Profile. 3 Turn the Dialogue Matcher on or off for a clip by right-clicking and picking Clip > AI Tools > Dialogue Matcher > Enable. 4 Strip the Dialogue Matcher off a clip by right-clicking and picking Clip > AI Tools > Dialogue Matcher > Remove Applied Profile.

### Audio Assistant (Studio Version Only)

Through the Audio Assistant, DaVinci Resolve can sort and color-code your tracks on its own, balance out your dialogue levels, and set the mixer faders to deliver a professional-grade blend of your music, sound effects, and dialogue. Along the way your dialogue gets cleaned up too, with Voice Isolation and DeEssing applied where called for. Music tracks receive ducking, whatever automation is needed gets written, and the right mastering and finalizing plugins are inserted and tuned to reach the proper loudness target for the delivery standard you picked.

To use AI Audio Assistant: 1 Open up a timeline holding unmixed audio. Where the faders start really doesn‘t matter, because Audio Assistant takes care of every fader move while it mixes. 2 To kick off automatic mixing, pick Timeline > AI Tools > Audio Assistant from the Timeline menu, choose the Delivery Standard for your mix in the dropdown menu, and hit the Auto Mix button. 3 The Audio Assistant dialog switches over to show how the mixing is progressing, with a button to cancel.
