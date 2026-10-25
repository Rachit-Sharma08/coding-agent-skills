# Music editor preparing the voice model assets

Version: DaVinci Resolve 20.3 Reference Manual. Context: Music editor studio version only.
[Chapter index](INDEX.md) / [Previous section](creating-your-own-voice-models.md) / [Music Editor (Studio Version Only)](dialogue-leveler-and-music-remixer-and-music-editor.md)
<a id="source-creating-the-voice-model"></a> <a id="source-for-more-information-see-part-13-fairlight"></a> <a id="source-preparing-the-voice-model-assets"></a> <a id="source-the-fairlight-page"></a> <a id="source-voice-model-generation"></a> <a id="source-voice-model-progress"></a>

### Preparing the Voice Model Assets

Aim for roughly ten minutes of pristine, high-fidelity recordings of whatever voice you intend to model. Keep that audio largely clear of background ambiance and noise, and apply minimal or no dynamics processing. Consistency matters: the source should sound organic and even throughout. Capturing a range of emotional deliveries can also help, in case you later want to hear how those carry through to the driven voice. Approach the take the way you would a voice over audition, and demonstrate your full range. The recordings need not arrive as a single long take, but when many separate files exist, gathering them into one bin keeps things organized. Across those several clips, hold the quality steady so there are no shifts in the captured sources.

### Creating the Voice Model

To build a voice model of your own, pick one or more clips for analysis inside the Media Pool, then right-click and select AI Tools> DaVinci AI Tools Voice Training from the context menu. The very first time you launch this tool, DaVinci Resolve brings up the Resolve Extras Download Manager so the necessary support files can be installed.

### Voice Model Generation

A warning splash screen comes up first, confirming that you take complete responsibility for how the tool is applied. After you click accept, the DaVinci AI Voice Training dialog opens, presenting two settings to configure.

- Voice Model Name: Type a meaningful name for the model you are creating.
- Quality: Pick either Faster or Better mode for the analysis. Better runs roughly 3x longer than faster,

and around 10 minutes of source can take several hours to finish, depending on how powerful your machine is. When a voice model first starts, it runs as a foreground process; after the opening analysis wraps up, it hands off to a background process, so you remain free to keep working in DaVinci Resolve or switch to other apps while it completes.

### Voice Model progress

Track how the model is coming along through the Voice Model Generation Progress indicator at the lower-right of the screen, or open it via Workspace > Voice Model Progress.

The Voice Model Generation Progress indicator gradually fills with blue as the voice model wraps up. Hovering over the top reveals an ETA and a progress-completed tooltip. From there you may instead pause the in-progress model or throw it away. Closing DaVinci Resolve likewise halts the background process, which picks back up by itself when DaVinci Resolve is next opened. After the model finishes, its new voice preset becomes available within the Voice Convert Dialog.

### The Fairlight Page

On the Edit page, the audio controls lean toward straightforward mixing, enough to keep levels reasonable while you assemble a program. When you need full-scale audio sweetening, mixing, automation, and mastering, the Fairlight page sits just a single click away.

### For more information, see Part 13, “Fairlight.”
