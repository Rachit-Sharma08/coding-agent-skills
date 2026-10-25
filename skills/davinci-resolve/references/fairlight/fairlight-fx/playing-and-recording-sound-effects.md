# Playing and recording sound effects

Version: DaVinci Resolve 20.3 Reference Manual. Context: Foley sampler.
[Chapter index](INDEX.md) / [Previous section](flanger-and-foley-sampler.md) / [Next section](frequency-gain-lfe-limiter-and-meter-effects.md) / [Foley Sampler](flanger-and-foley-sampler.md)
<a id="source-fairlight-fx-part-3"></a> <a id="source-playing-and-recording-sound-effects"></a>

### Playing and Recording Sound Effects


After the Foley Sampler is configured with effects you can trigger from a MIDI controller, capturing those effects takes only a few steps. 1 Confirm that the “Save clips to” field, found in the Capture and Playback panel of the Project Settings, points at the storage volume you intend to record onto — use the Browse button to redirect it if needed. 2 In the track header of the audio track that hosts the Foley Sampler, press the R button so the track enters Record Enable mode. 3 In the Fairlight toolbar, press the Record button. 4 As recording proceeds, trigger your sounds in time with the on-screen image by pressing the keys or pads of the MIDI controller, then press Stop once you have finished. The result is a captured clip holding the effects you performed, aligned to the picture. Should the timing drift slightly, the Elastic Wave audio retiming tools let you nudge things back into alignment rather than recording the whole pass again.

A freshly captured audio clip, produced by recording the sounds you triggered through the Foley Sampler
