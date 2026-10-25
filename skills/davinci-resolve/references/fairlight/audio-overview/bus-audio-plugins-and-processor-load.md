# Applying audio plugins to busses and dealing with processor intensive plugins

Version: DaVinci Resolve 20.3 Reference Manual. Context: Audio overview.
[Chapter index](INDEX.md) / [Previous section](applying-plugins-and-editing-plugin-parameters.md)
<a id="source-applying-audio-plugins-to-busses"></a> <a id="source-caching-audio-clips-with-plugins"></a> <a id="source-dealing-with-processor-intensive-plugins"></a> <a id="source-exporting-audio-clips-with-plugins"></a>

### Applying Audio Plugins to Busses

Audio plugins go onto Main and Sub buses the same as any other track, so you can apply whatever audio mastering effects individual submixes call for, or even a whole main. TIP: Plugins can be assigned in a hurry across a chosen set of channel strips, or to all of them, by holding the Option key (Mac) or the Alt key (Windows) for every selected track, or Command-Option (Mac) or Control-Alt (Windows) for every mixer channel strip, prior to performing the operation. Such shortcuts can cut plenty of time from your workflow.

### Dealing With Processor Intensive Plugins

As you stack more and more plugins straight onto clips in complicated mixes, you may find you don't have the processing power to play every audio track and effect in real time. When that happens, there are two routes to lighten the load that audio clip effects place on your workstation.

### Caching Audio Clips With Plugins

One fast fix is to manually switch on caching for one or more selected audio clips carrying audio effects, which lifts your project's performance. Once an audio clip is cached, all the plugin effects are “baked in,” and that clip's audio waveform refreshes to reflect the changed audio. Cached clips show a small badge to the right of the FX badge in the clip's name bar.

A cache badge signals that this audio clip carries cached effects The action is non-destructive and leaves the source media of cached clips permanently untouched. A cached clip's plugin parameters remain yours to tweak at any time. Bringing up a cached clip's graphical controls briefly pauses audio caching, and when you're done, the clip re-caches by itself and refreshes its waveform to mirror the change, provided Cache Audio Effects remains enabled.

To cache audio effects for one or more selected clips:

- Right-click an audio clip that has a plugin on it and pick Cache Audio Effects to turn on audio effect caching for that clip. Right-click one clip among several selected ones and you turn on Cache Audio Effects across every selected clip at once. From then on, that clip stays cached (and re‑cached each time you alter the plugin's parameters) until you manually turn audio caching off.

To disable audio caching for one or more selected clips:

- Right-click a clip that has already been cached and pick Cache Audio Effects to switch off audio effect caching for it.

### Exporting Audio Clips With Plugins

A second way to lighten the toll audio clip effects take on your system is exporting the effected clip onto a separate layer. Doing so creates a brand-new piece of audio media carrying the effect “baked in,” saved to the directory spelled out in the “Save clips to” field, which lives under the Capture and Playback panel inside the Project Settings. To bounce one or more selected audio clips that carry effects onto a separate layer:

- Right-click an audio clip that has a plugin on it and pick Export Audio Files. Right-click one clip among several selected ones and you're offered choices for what to export from each selected clip all at once. Once exported, clips hold no editable effects, yet you can always choose View > Show Audio Track Layers to reveal the original underlying clip, which still keeps the original plugin effect; from there you can unmute it, move it back up top, edit the effect, and export a fresh version of the clip that arrives as the topmost layer.

To learn more about exporting clips to files, turn to Chapter 175, “Editing Basics in the Fairlight Page.”
