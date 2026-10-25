# Audio filters in the effects library and custom audio filter interface for izotope rx4

Version: DaVinci Resolve 20.3 Reference Manual. Context: Working with audio in the edit page.
[Chapter index](INDEX.md) / [Previous section](audio-assistant-delivery-and-silence-removal.md) / [Next section](creating-your-own-voice-models.md)
<a id="source-audio-filters-in-the-effects-library"></a> <a id="source-installing-audio-filters"></a> <a id="source-the-button-for-opening-a-filters-custom-control"></a> <a id="source-the-custom-audio-filter-interface-for-izotope-rx4"></a> <a id="source-the-voice-convert-tool"></a> <a id="source-using-voice-convert"></a> <a id="source-voice-convert-analyzing-a-clip"></a> <a id="source-voice-convert-settings"></a> <a id="source-voice-convert-studio-version-only"></a>

### Audio filters in the Effects Library

To edit a clip’s audio filters:

- Pick that clip and open the Inspector. Every audio filter on the clip is listed under the Effects panel, within the Audio tab, and that filter's controls show up right inside the Inspector.

Plenty of VST and Audio Unit audio filters come with a bespoke user interface that makes wrangling the filter's controls far easier. You can open these from inside DaVinci Resolve.

### The custom audio filter interface for iZotope RX4

To expose a filter’s custom controls:

- Click the Custom Control button (the one next to the trash can). The custom controls open in a floating window. Close that window when you're done tweaking them.

### The button for opening a filter’s custom control

Ways to work with audio filters inside the Inspector:

- To disable or re-enable a filter: Click the toggle button sitting at the far left of each filter's title bar.
- To remove a filter: Click the Trash Can button.

Once they're on a clip or track, audio filters can be keyframed or automated as well — just like volume and pan settings — letting you build audio effects that evolve over time.

### Installing Audio Filters

Since VST effects don't go to one standard location, you may now and then have to point the application at a directory of VST plugins you've just installed on your machine. For that, the Audio Plugins panel of the Preferences window holds a list where you can manually add or drop VST plugin directories whenever needed.

After you've put one or more VST directories on the list, a second list beneath it shows every audio plugin found inside those directories. Each entry carries a checkbox indicating whether it's enabled at the moment. Any VST plugin that crashes DaVinci Resolve while loading at startup gets disabled automatically. This list lets you see which plugins were disabled — useful for troubleshooting — and re-enable any “blacklisted” ones by switching their checkboxes back on.

### Voice Convert (Studio Version Only)

DaVinci Resolve carries a remarkably advanced AI-driven voice conversion tool that essentially lets you trade one speaking voice for another. Its applications run broad and even somewhat controversial, yet this Voice Convert toolset can prove a hugely valuable asset in a post production. It lets you take a generated voice model that DaVinci Resolve has captured and “drive” that model off another voice recording used as its base. Simple uses include swapping your own voiceover tracks for a voice with greater depth and gravitas, or even flipping the gender of your own voice if that suits the material better. Maybe you recorded in a noisy room and want a clean version instead, using your own voice as the model to stand in for your noisy originals. In tougher cases you might train your own voice convert model on your actor's vocal patterns and use it to alter and replace their earlier voiceover without dragging them back into the booth. It's even possible, finally, to swap an actor's voice out wholesale for another while staying dead-on in sync with the picture. The original's inflection, pitch movement, and emotion all carry over — it merely sounds like a different person. Obviously a tool this powerful demands a degree of responsibility from whoever uses it. Privacy, copyright, and union laws and rules are all unsettled right now where AI generated content is concerned, and the ethics of using it professionally have to be navigated with care.

### The Voice Convert tool

NOTE: Voice Convert is highly processor intensive and needs your system to carry at least 8GB of video ram before it'll switch on, which guards against crashes and instability. Even on a powerful rig, building a Voice Model demands sustained, heavy CPU and GPU effort, so juggling other tasks while it runs can be tough.

### Using Voice Convert

As with most of DaVinci Resolve's AI tools, Voice Convert is quite straightforward to use, since the voice model shoulders all the heavy processing. To use Voice Convert to change one voice to another: 1 Drop the clip or clips whose voice you want to change onto the timeline and select them. 2 Right-click the clip and pick Voice Convert from the context menu, or pick Clip > AI Tools > Voice Convert from the main menu. 3 Pick the track where the new audio should land (this can mean overwriting the original). 4 Pick the file name you'd like the new audio to carry. 5 Pick the Voice Model for the new audio (custom voice models of your own can be built as described below), along with its parameters. 6 Click Render to launch the Voice Convert process.

### Voice Convert analyzing a clip

The Voice Convert dialog now opens and reports the conversion's progress. How long this runs depends on how many clips you chose and their length. Once finished, the new audio lands on the timeline in precisely the same spot as the original (or at the same spot on a different track, if you chose that option). Those new audio clips show up in the Media Pool as well. Just play the timeline back to audition the new voice. To return to the original, right-click a clip and pick Revert to Original Voice from the context menu. TIP: You can drive voices that carry different accents, but Voice Convert usually can't manufacture another accent. As an example, take a voice model of a speaker with a British accent and drive it with an American accent, and you'll get something closer to an American rendering of that British-accented speaker. Speak with a British accent while driving the British voice model, however, and it works nicely.

### Voice Convert Settings

Every voice conversion calls for set up parameters that drive the model.

- Track: Pick which track the new audio belongs on. It defaults to Render in Place, which writes over the original audio.
- File Name: Define the file name of the new audio clip. Type a specific name, or build a naming template out of the metadata variables. The name defaults to ClipName-(Voice Model Name).
- Voice Model: Pick the voice model you want applied to the new audio. A handful of built-in choices ship with DaVinci Resolve, and any you build yourself will appear here too.
- Tight Matching to Source: Tick this box to closely track the source voice's pitch, intonation, and volume variance. Clear it for a looser reading driven by the Pitch Variance tool.
- Pitch Variance: This tool comes alive once the Tight Matching to Source box is cleared. Smaller values yield a flatter, more monotone reading, while larger ones add more pitch movement.
- Pitch Change: This slider builds a deeper voice (negative values) or a higher one (positive values) off the model. Values are given in semitones and adjust in 100 cents (.1 semitone) steps.
