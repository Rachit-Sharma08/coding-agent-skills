# Audio assistant voice convert

Version: DaVinci Resolve 20.3 Reference Manual. Context: Audio assistant studio version only.
[Chapter index](INDEX.md) / [Previous section](dialogue-separator-track-fx-and-ducker-track-fx.md) / [Audio Assistant (Studio Version Only)](dialogue-separator-track-fx-and-ducker-track-fx.md)
<a id="source-creating-the-voice-model"></a> <a id="source-creating-your-own-voice-models"></a> <a id="source-preparing-the-voice-model-assets"></a> <a id="source-the-voice-convert-tool"></a> <a id="source-using-voice-convert"></a> <a id="source-voice-convert-analyzing-a-clip"></a> <a id="source-voice-convert-settings"></a> <a id="source-voice-convert-studio-version-only"></a> <a id="source-voice-model-generation"></a> <a id="source-voice-model-progress"></a>

### Voice Convert (Studio Version Only)

Within DaVinci Resolve sits a remarkably advanced AI-powered voice conversion feature that lets you, in effect, trade one person's spoken voice for a different one. What you can do with it spans a broad range and stirs up a fair bit of debate, yet the Voice Convert toolset proves enormously handy during post production. The way it works is that you feed it a generated voice model that DaVinci Resolve has captured, then “drive” that model with a separate voice recording acting as the source. For straightforward jobs, you might swap your existing voiceover tracks for one carrying more weight and gravitas, or even flip the gender of your own narration where that fits the material better. Maybe your recording happened somewhere noisy and you'd rather have a clean take, so you model your own voice to stand in for those flawed tracks. For trickier situations, you can build a voice convert model trained on your actor's vocal characteristics, then apply it to revise and substitute their earlier voiceover, sparing everyone a return trip to the booth. And at the far end, you can fully replace one performer's voice with another while keeping everything locked in step with the footage. All of the original's inflection, shifts in pitch, and emotional tone carry through; the only thing that differs is whose voice it sounds like. Plainly, wielding so capable a tool calls for a measure of responsibility from whoever uses it. Right now the rules covering privacy, copyright, and union agreements remain unsettled where AI-generated material is concerned, so you'll need to tread thoughtfully through the ethical questions of using it professionally.

### The Voice Convert tool

CUT NOTE: Running Voice Convert places a heavy load on the processor and won't switch on unless your machine carries at least 8 GB of video RAM, a safeguard against crashes and instability. Even on a capable rig, building a Voice Model draws sustained, heavy CPU and GPU resources, which can make running other tasks alongside it difficult.

### Using Voice Convert

As with the bulk of DaVinci Resolve's AI features, operating Voice Convert is quite straightforward, since the voice model shoulders all the intricate computation. Here's how to apply Voice Convert and turn one voice into another: 1 Drop the clip or clips whose voice you intend to alter onto the timeline, then highlight them. 2 Right-click the clip and pick Voice Convert from the context menu, or go to Clip > AI Tools > Voice Convert in the main menu. 3 Choose the track where the fresh audio should land (this can mean replacing the original). 4 Choose the file name that the fresh audio will carry. 5 Choose the Voice Model to apply to the fresh audio (custom voice models of your own can be built as described further down) along with its parameters. 6 Press Render to launch the Voice Convert process.

### Voice Convert analyzing a clip

Now the Voice Convert dialog pops up to report how the conversion is coming along. How long this lasts hinges on the duration and count of the clips you picked. After it finishes, the fresh audio lands on the timeline at precisely the position the original audio occupied (or that same spot on a different track, should you have chosen that route). Those new audio clips show up in the Media Pool too. Just run the timeline to preview the converted voice. Reverting to the original is as easy as right-clicking a clip and picking Revert to Original Voice from the context menu. TIP: Although you may drive voices carrying assorted accents, Voice Convert as a rule won't reproduce a different accent. Say your voice model belongs to a British-accented speaker and you drive it using an American accent; what comes out leans toward an American take on that British-accented speaker. Yet if you adopt a British accent while driving the British voice model, the results turn out well.

### Voice Convert Settings

Every voice conversion involves picking the setup parameters that steer the model.

Track: Pick the track on which the fresh audio should sit. Its default setting is Render in Place, which replaces the original audio. File Name: Establish the file name for the fresh audio clip. You may type a particular name or lean on the metadata variables to build a naming template. The name defaults to ClipName(Voice Model Name). Voice Model: Pick whichever voice model you'd like applied to the fresh audio. DaVinci Resolve ships with a handful of built-in choices, and whatever custom ones you build appear here as well. Tight Matching to Source: Tick this box to closely trail the pitch, intonation, and volume swings of the source voice. Untick it for a looser reading driven by the Pitch Variance tool. Pitch Variance: This tool switches on once the Tight Matching to Source box is unticked. Smaller values yield a flatter, more monotone reading, whereas larger ones add greater pitch variation. Pitch Change: Drag this slider to make the model-based voice deeper (negative values) or higher (positive values). Measured in semitones, the values move in 100 cents (.1 semitone) steps.

### Creating Your Own Voice Models

You're able to build voice models of your own to feed into Voice Convert. They might capture your own voice, or anyone else's provided you hold the rights. What follows covers a few best practices for arriving at a clean, workable voice model.

### Preparing the Voice Model Assets

Your strongest outcomes come from roughly ten minutes of clean, high-quality recordings of whichever voice you're modeling. Keep that audio clear of heavy room tone and noise, applying minimal or no dynamics processing. Aim for steady material that comes across as natural. Capturing a spread of emotional deliveries also helps, assuming you want to hear how those translate to the driven voice. Approach it the way you'd approach a voiceover audition and demonstrate your full range. The recordings needn't sit inside one continuous clip, although when you're juggling many separate files, gathering them into a single bin keeps things tidy. Across those several clips the quality ought to stay uniform, with no audio fluctuations between the recorded sources.

### Creating the Voice Model

Building a voice model of your own starts with picking one or more clips for analysis in the Media Pool, then right-clicking and choosing AI Tools > DaVinci AI Tools Voice Training from the context menu. On your very first run of this tool, DaVinci Resolve launches the Resolve Extras Download Manager so it can install the support files it needs.

### Voice Model Generation

First off, a warning splash screen shows up, confirming that you take full responsibility for how the tool gets used. After you click accept, the DaVinci AI Voice Training dialog opens with two settings to configure. Voice Model Name: Type a descriptive name for the model you're creating. Quality: Pick either Faster or Better mode for the analysis. Better runs roughly 3x longer than faster, and around 10 minutes of source material may need several hours to wrap up, depending on how powerful your computer is.

At the outset, model creation runs as a foreground process; once that first analysis pass finishes, it hands off to a background process, freeing you to keep working in DaVinci Resolve or other apps while it completes.

### Voice Model progress

Track how far the model has come via the Voice Model Generation Progress indicator located in

the lower-right corner, or by choosing Workspace > Voice Model Progress.

As the voice model nears completion, the Voice Model Generation Progress indicator gradually fills with blue. Hover near the top and a tooltip surfaces an ETA along with how much has finished. You're also free instead to pause the in-progress model or throw it away. Shutting DaVinci Resolve down likewise suspends the background process, which picks back up on its own the next time you launch DaVinci Resolve. After the model wraps up, its new voice preset becomes available inside the Voice Convert Dialog.
