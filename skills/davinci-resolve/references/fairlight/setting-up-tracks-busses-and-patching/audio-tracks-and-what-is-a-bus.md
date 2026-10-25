# Audio tracks and what is a bus

Version: DaVinci Resolve 20.3 Reference Manual. Context: Setting up tracks busses and patching.
[Chapter index](INDEX.md) / [Next section](defining-audio-track-types-and-rearranging-tracks.md)
<a id="source-audio-tracks"></a> <a id="source-bus-to-bus-routing-and-mixing"></a> <a id="source-busses-in-nested-timelines"></a> <a id="source-controlling-signal-flow"></a> <a id="source-converting-older-fixed-bus-projects-to-flexbus"></a> <a id="source-exposing-bus-tracks-in-the-timeline"></a> <a id="source-setting-up-tracks-busses-and-patching"></a> <a id="source-setting-up-tracks-busses-and-patching-part-1"></a> <a id="source-surround-panning-and-bussing"></a> <a id="source-using-legacy-fixed-bussing"></a> <a id="source-what-is-a-bus"></a>

### Setting Up Tracks, Busses, and Patching

Among the earliest tasks when preparing a fresh project for mixing on the Fairlight page is establishing the audio tracks and busses required to route and merge the parts of your mix. This chapter walks through creating audio tracks and using busses to manage a mix as efficiently as possible. That said, the Fairlight page lets you add to or revise your setup whenever you like, so you can stay focused on the creative side and handle any necessary housekeeping as the mix develops. The FlexBus structure in Fairlight permits bus-to-bus, track-to-bus, or bus-to-track signal routing and adds broader Dolby Atmos support, covering import, export, and manipulation of Atmos ADM files.

### Audio Tracks

On a DaVinci Resolve timeline, every audio track maps to one channel strip along the left edge of the Mixer. Based on the way the track was configured, it adopts a specific audio format — among them mono, stereo, 5.1 or 7.1 surround, and Dolby Atmos. Through the lanes shown inside each track on the Fairlight timeline, track routing ensures the assorted audio channels within a track’s clips land at the right audio output for both monitoring and rendering. Although audio tracks in DaVinci Resolve frequently hold several channels from one clip, how those individual channels appear varies by page:

- On the Cut and Edit pages, each audio track shows a single clip “lane” in the Timeline no matter how many channels its clips carry. The waveform you see is a composite that blends the clip’s assorted channels together.
- The upside is that multichannel tracks become easier to handle without the clutter of multiple channel lanes that would make things look much “busier.” The downside is that you lose sight of detailed activity occurring on any individual channel of that track.
- The Fairlight page shows the same track count as the Edit page, except that each Fairlight track is split into lanes exposing every separate channel of a clip’s audio. That extra visual detail can aid both editing and mixing.

(Top) On the Cut and Edit pages, the 6 channel and stereo audio appears as single composite tracks. (Bottom) On the Fairlight page, that same audio shows the six channel and stereo tracks split into multiple lanes, one matching each of the file types.

Having grasped how tracks behave on the Fairlight page, the next key idea to master before you can fully tap the page’s power is FlexBus, which gives you several ways to combine audio tracks.

### What Is a Bus?

In plain terms, a bus is a shared signal connection point within an audio mixer. A bus can be mono, stereo, or any wider format such as 5.1 or Dolby Atmos 9.1.6 (which carries 16 audio signals). The bussed connections are summed into one signal that you steer from a single bus channel strip. By default, for instance, one bus named “Bus 1” sums the levels of every clip on every track of a timeline into the combined signal routed to your speakers or headphones. Busses let you organize how a timeline’s tracks are mixed in inventive ways. Suppose five audio tracks hold all the edited dialogue clips for a given program — you can send the outputs of all five to a dedicated submix bus. That lets the pooled levels of every contributing dialogue track be processed, tweaked, and mixed together through one channel strip’s controls. You can also stack busses to structure a mix, routing submix busses into further “main busses.” Individual tracks feed submix busses, and several submixes can then feed one or more “main output” busses. For example, picture four submix busses — German dialogue, English dialogue, Music, and Effects. You might route the German, Music, and Effects submixes into a Main 1 bus to deliver the German edition, and the English, Music, and Effects submixes into a Main 2 bus to deliver the English-language edition.

### Surround Panning and Bussing

For surround or immersive work, audio tracks from the Timeline reach busses through each channel strip’s multi-format surround panner, so a bus can be set up to suit a specific audio format such as mono, stereo, LCRS, 5.1 surround, or 7.1 surround, as well as immersive formats like Atmos. Routing across multiple busses even lets you output several formats at the same time.

### Bus to Bus Routing and Mixing

The FlexBus structure in Fairlight grants full user freedom over bus types and signal routing, making bussing entirely user-definable and letting you patch outputs and/or sends in whatever manner your project demands. Each track can feed up to ten busses, plus sends with their own level and pan controls to ten more. Busses can cascade into other busses as many as six layers deep, which supports intricate stem building and processing and yields discrete deliverables. User-definable busses enable bus-to-bus, bus-to-track, or track-to-bus routing, with every bus capable of passing signals from mono all the way up to fully immersive formats such as Dolby Atmos. As with every track type in Fairlight, these bus types can be reassigned at any time when needed. The strength of the FlexBus system lies in letting you send signals to many destinations simultaneously, achieving elaborate mixing setups. Perhaps you need two mixes identical in content but differing in output level. You can set up two mix busses — one at an output level of -2dB true peak and one at -10dB true peak. The finished mix signal goes to one bus, which then splits into two more, one fitted with a limiter set to -2dB and the other to -10 dB, producing both versions at once.

Within the FlexBus structure, a wide assortment of bus track types can be created or reassigned.

### Using Legacy Fixed Bussing

If the older Fixed Bus mapping approach suits you better, you can turn it on for fresh projects: open the Fairlight panel within Project Settings and check the “Use fixed bus mapping” box. If a project already has Fixed Bussing turned on and you wish to switch to FlexBus, clear the “Use fixed bus mapping” checkbox. Be aware that after the switch, you won’t be allowed to revert to legacy bussing.

For more information see Chapter 177, “Mixing in the Fairlight Page.”

### Converting Older Fixed Bus Projects to FlexBus

To convert older Fixed Bus projects to FlexBus, follow these steps:

- Open Project Settings > Fairlight.
- Under the Bussing heading, uncheck “Use fixed bus mapping.”
- A dialog will appear allowing you to convert the project to FlexBus.

### Busses in Nested Timelines

When you place a timeline inside another timeline that already has busses configured for Fairlight mixing, every bus routing keeps functioning as intended inside the nested timeline, which surfaces all channels through the default main bus (Bus 1) within the enclosing timeline. From that angle, the nested timeline’s audio amounts to a submix whose resulting audio outputs to the audio track it was edited onto. You can alternatively decompose the nested timeline into its own bus structure inside the main timeline you imported it into, exposing all of the original tracks just as they were. That makes this a very powerful feature for combining work that was done at separate times or came from separate contributors — for more, consult Chapter 177, “Mixing in the Fairlight Page.” in section Nested Audio Timelines.

### Exposing Bus Tracks in the Timeline

Any bus can be surfaced as a track in the Timeline, which lets you see and edit the automation applied to that bus’s parameters. To show a bus in the Timeline: 1 Turn on the Toggle Automation button in the Fairlight toolbar. Every bus is shown by default. 2 To hide one, open the Index and click the eye button beside the bus you want hidden in the Timeline. 3 To work with automation on a bus, pick the automation curve you want to view from the dropdown in the track header controls.

### Controlling Signal Flow

A sound workflow for getting editing and mixing set up on the Fairlight page goes like this:

- Arrange and configure your timeline’s tracks as needed — for instance, tidy clips on tracks, set track types, color, grouping, and so on.
- Build the busses required to shape the mix’s desired signal flow.
- Send the audio tracks, or any submix busses, to the bus destinations the mix layout calls for.
