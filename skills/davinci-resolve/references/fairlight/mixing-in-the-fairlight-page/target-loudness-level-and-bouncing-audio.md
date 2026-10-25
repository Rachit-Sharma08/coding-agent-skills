# Target loudness level and bouncing audio

Version: DaVinci Resolve 20.3 Reference Manual. Context: Mixing in the Fairlight page.
[Chapter index](INDEX.md) / [Next section](third-party-control-panel-support-for-mixing-overview.md)
<a id="source-ai-audio-assistant-studio-version-only"></a> <a id="source-bouncing-audio"></a> <a id="source-mixing-in-the-fairlight-page-part-4"></a> <a id="source-target-loudness-level"></a>

### Target Loudness Level

Lets you dial in, expressed in LUFS, the loudness target that the master Loudness meters aim toward for your intended deliverable. As an illustration, the default loudness standard in DaVinci Resolve sits at -23 LUFS, while YouTube's published target is -14 LUFS. Choosing -14 LUFS shifts the "0" indicator on the loudness scale to that point, so you can drive your master mix toward the corresponding loudness standard.

### Bouncing Audio

The term bouncing audio describes taking one or more Timeline tracks, mixing and rendering them down onto a different track of the Timeline, and thereby "baking in" CPU-heavy effects together with detailed or layered edits so that a fresh, unbroken stretch of audio media results. Wherever the bounced file lands is governed by the Project Settings > Capture and Playback panel > "Save clips to" field. The Fairlight page offers two commands for performing a bounce:

- Timeline > Audio > Bounce Selected Tracks in Place
- Timeline > Audio > Bounce Mix to Track

To use Bounce Selected Tracks to New Layer: 1 Mark In and Out points so the portion of the Timeline you intend to bounce is defined. Skipping this step means no action occurs. 2 Hold Command and click the track headers or the mixer channel strips for every track you wish to include, which selects them. 3 Choose Timeline > Audio > Bounce Selected Tracks to New Layer. Each chosen track is rendered and processed, then surfaces as the uppermost audio layer on that track. As long as View > Show Audio Track Layers stays disabled, the freshly bounced audio looks like the sole clip occupying the track. The source audio nonetheless remains (carrying any clip-based effects that were never rendered) at the bottom of that track's layer stack; switch on View > Show Audio Track Layers to expose it. That bounced audio is a brand-new media file deposited at the directory location named in the Project Settings > Capture and Playback panel > "Save clips to" field.

To use Bounce Mix to Track: 1 From the menu, pick Timeline > Bounce Mix to Track. A Bounce Mix to Track window opens and lists every bus that is presently available. 2 Within the Destination Track column, decide which mixes get bounced by picking New Track or by selecting an already-existing track from the dropdown menus. 3 Click OK. Resolve processes, mixes, and bounces the chosen mix onto the designated track as a fresh chunk of audio. The result is new media written out to the directory location named in the Project Settings > Capture and Playback panel > "Save clips to" field. TIP: A Bounce Audio Effects command likewise lives in the contextual menu for Timeline audio clips that carry clip-based audio effects. For more information, see Chapter 180, "Audio Effects."

To learn more about how clips, ranges, and files are exported, consult Chapter 175, "Editing Basics in the Fairlight Page."

### AI Audio Assistant (Studio Version Only)

Using the AI Audio Assistant, DaVinci Resolve is able to sort and color-code your tracks on its own, balance your dialogue levels, and move the Fairlight mixer faders to assemble a polished, professional-grade blend of dialogue, music, and sound effects. As part of that pass, your dialogue gets cleaned up, with Voice Isolation and De‑Essing applied where warranted. Music tracks receive Ducking, whatever automation is called for gets written, and the right mastering and finalizing plugins are inserted and tuned so the loudness suits the delivery standard you picked. To use AI Audio Assistant: 1 Open a timeline that holds unmixed audio. Where the faders start out is irrelevant, since Audio Assistant takes over every fader move while it mixes. 2 Kick off the automatic mix by choosing Timeline > AI Tools > Audio Assistant from the Timeline menu, picking the Delivery Standard for your mix in the drop-down menu, and clicking the Auto Mix button.

3 The Audio Assistant dialog switches over to show how far the mixing has progressed, along with a way to abort it.

Audio Assistant dialog - Mix Progress 4 Once mixing finishes, you're free to audition the mix and, should you want to, tweak it further or throw the whole thing out.

NOTE: Should a track end up filed under the wrong category, right-click that track's header, pick the right category from the Track Category portion of the contextual menu, and run the Audio Assistant again.
