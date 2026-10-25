# General audio sample rate

Version: DaVinci Resolve 20.3 Reference Manual. Context: Project settings.
[Chapter index](INDEX.md) / [Previous section](capture-and-playout.md) / [Next section](use-fixed-bus-mapping-and-use-32-bit-float-recording.md)
<a id="source-audio-sample-rate"></a> <a id="source-general"></a> <a id="source-project-settings-part-4"></a>

### General

### Audio Sample Rate


You may only adjust this setting before your first timeline gets created. As soon as a project holds one timeline or more, the Audio Sample Rate stays fixed at whichever value you picked. Expressed in kilohertz, the Audio Sample Rate counts how many samples per second DaVinci Resolve uses while handling audio. Its default sits at 48000 (or 48 kHz), the usual choice across broadcast and cinema work. You do have the option of switching it to 96000 or 192000 should you wish to mix and treat audio with greater precision. Keep in mind that picking a steeper sample rate, like 96 kHz rather than 48 kHz, consumes double the processing power and yields media taking up double the space. NOTE: No matter which Timeline Sample Rate you choose, audio files brought in at other sample rates get re-sampled automatically to the Timeline Sample Rate so playback stays accurate.
