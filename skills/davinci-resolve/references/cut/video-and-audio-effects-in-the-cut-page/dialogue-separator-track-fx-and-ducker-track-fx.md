# Dialogue separator track FX and ducker track FX

Version: DaVinci Resolve 20.3 Reference Manual. Context: Dialogue separator track FX studio version only, Ducker track FX.
[Chapter index](INDEX.md) / [Previous section](voice-dialogue-and-music-processing.md) / [Dialogue Separator Track FX (Studio Version Only)](voice-dialogue-and-music-processing.md) / [Next section](audio-assistant-voice-convert.md)
<a id="source-adding-ducker-input-sources-in-the-inspector"></a> <a id="source-audio-assistant-studio-version-only"></a> <a id="source-beat-detector-studio-version-only"></a> <a id="source-dialogue-matcher-studio-version-only"></a> <a id="source-ducker-controls"></a> <a id="source-ducker-graph-display"></a> <a id="source-ducker-track-fx"></a> <a id="source-the-dialogue-separator-plugin"></a> <a id="source-the-ducker-plugin"></a> <a id="source-using-the-ducker"></a> <a id="source-video-and-audio-effects-in-the-cut-page-part-3"></a>

### The Dialogue Separator plugin

### Ducker Track FX

This plugin lets you take the audible signal from one track or several and use it to pull down the level of another.

While it can be put to plenty of creative uses, a common application of “ducking” is automatically lowering a music or sound effects bed so dialogue or a VO track stands out more clearly in a mix.

That's accomplished without compressing the signals coming in. Set up properly in the Ducker interface or by way of the Inspector's Audio tab, your audio tracks can practically “mix themselves.”

In a simple scenario, the Ducker uses the level changes of a single incoming dialogue or VO track to lower the volume of the sound effects bed of a noisy freeway.

In a trickier situation—say a scene where three characters are talking beside that same noisy freeway—a lone Ducker plugin can draw on the level changes of each dialogue track to attenuate the traffic noise.

With just one input source (Dialogue 1), the Ducker would kick in only while the first character

speaks. This new capability, though, lets you bring the other two dialogue tracks (Dialogue 2 and

Dialogue 3) in as input sources for knocking down the traffic noise.

### The Ducker plugin

### Using the Ducker

Carrying on from the use cases above: 1 Pick the target track you'd like to attenuate (the Freeway Traffic track), and open up the Ducker. 2 Open the Source dropdown and pick Dialogue 1 to serve as the input source.

- For extra input sources, Command-click the remaining track names; here that means Dialogue2 and Dialogue3.
- Run a stretch of your sequence and dial in the duck level along with the other controls until it sounds right.

Adding Input Sources via the Inspector If working inside the Inspector suits you better: 1 Pick the Freeway Traffic track, confirm the Ducker is on, and bring up the Inspector’s Audio tab. 2 Hit the plus sign at the right of the Source 1 dropdown that holds Dialogue1; that spawns a dropdown menu for Source 2, and you then pick Dialogue2 off the list.

3 Hit the plus sign at the right of the Source 2 dropdown; that spawns a dropdown menu for Source 3, and you then pick Dialogue3 off the list.

### Adding Ducker input sources in the Inspector

### Ducker Controls

- Duck Amount: Sets, in dB, how much the target track gets attenuated; its default sits at 2.7 dB. For most jobs, somewhere between 2.0 dB and 5.0 dB suits best.
- Lookahead: Tunes the lookahead time, measured in milliseconds, defaulting to 15ms. With lookahead, the Ducker can begin attenuating the destination track ahead of the source track becoming audible.

A larger value has the Ducker “pre-anticipate” the source track that much sooner. Where you want the Ducker to start dropping the sound before a dialogue or VO line begins, experiment with higher values—though the default usually serves you well.

- Rise Time: Sets, in milliseconds, how long the Ducker takes to arrive at the reduction the Duck Amount calls for. It defaults to 10 milliseconds, which suits most cases. Longer Rise Times can help alongside higher Duck Amount values and wider gaps in the source track.
- Hold: This parameter fixes how long the target signal stays attenuated. Its default is 150ms.
- Recovery Time: This figure governs how fast the target signal climbs back to its prior level once attenuation ends. The default sits at 750ms, but dialing in the right Recovery time is key to ducking that sounds natural, so test a range of values to land on the best one.

### Ducker Graph Display

This area presents a gray line standing for the incoming signal set against the Ducker's action, drawn in yellow. Dips in the yellow line mark attenuation of the target track, driven by the Duck Amount together with the other parameters.

### Beat Detector (Studio Version Only)

For a piece of music on the timeline, DaVinci Resolve can detect the beats on its own, and it lets you snap to those beat marker spots. That comes in handy when you're aiming to cut on the beat. NOTE: For now, the Beat Detector performs reliably only with beat-driven music carrying 4/4 or 3/4 time signatures. To pick up the beats, right-click the timeline audio clip and choose Detect Music Beats off the context menu. After the analysis, the timeline clip presents beat indicator overlays, and other timeline elements can snap onto them. A music track carrying the Beat Detector. Those lined overlays line up with the music's beat.

### Dialogue Matcher (Studio Version Only)

Dialogue Matcher lets you match one piece of dialogue to another, lining up level, EQ, and reverb. It can rescue situations where new recordings don't sit in the same environment as existing ones. The Dialogue Matcher is a fully automated tool that only asks the user to grab a tone profile from one clip and then apply it to another.

Capturing a Dialogue Profile from a clip using the main menu

To Use Dialogue Matcher: 1 Pick a reference clip whose dialogue you'd like to match, right-click it, and go to Clip > AI Tools > Dialogue Matcher > Capture Dialogue Profile. 2 Pick the clip whose dialogue you mean to alter, right-click, and go to Clip > AI Tools > Dialogue Matcher > Apply Dialogue Profile. 3 Switching the Dialogue Matcher on or off for a clip is a matter of right-clicking and going to Clip > AI Tools > Dialogue Matcher > Enable. 4 To strip the Dialogue Matcher off a clip, right-click and go to Clip > AI Tools > Dialogue Matcher > Remove Applied Profile.

### Audio Assistant (Studio Version Only)

Through the Audio Assistant, DaVinci Resolve is able to sort and color-code your tracks for you, smooth

over your dialogue levels, and move the mixer faders so as to build a professional-quality blend of your music,

sound effects, and dialogue.

As this runs, your dialogue gets cleaned up as well, and where the situation calls for it, Voice Isolation and

De‑Essing are brought in. Music tracks receive Ducking, whatever automation is required gets

written, and the right mastering and finalizing plugins are added and tuned to help

reach the correct loudness level for whichever delivery standard you've selected.

Working with AI Audio Assistant goes like this: 1 Open up a timeline that still holds unmixed audio. Where you've set the starting fader positions is irrelevant, since Audio Assistant takes over every fader move while it mixes. 2 Kick off the automatic mix by picking Timeline > AI Tools > Audio Assistant from the Timeline menu, choosing the Delivery Standard that suits your mix in the dropdown menu, then pressing the Auto Mix button.

Audio Assistant dialog - Delivery Standard 3 At this stage the Audio Assistant dialog switches over to show how far along the mix has gotten, with a button available should you wish to stop it.

Audio Assistant dialog - Mix Progress 4 Once mixing wraps up, you're free to listen back to the result and either tweak it further or scrap it entirely if that's what you prefer. CUT NOTE: Should a track land in the wrong category, right-click that track's header, pick the proper category under the Track Category portion of the contextual menu, and run the Audio Assistant a second time.
