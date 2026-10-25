# Introduction to mixing and mixer

Version: DaVinci Resolve 20.3 Reference Manual. Context: Mixing in the Fairlight page.
[Chapter index](INDEX.md) / [Next section](selecting-channel-strips-and-tracks-and-track-organization.md)
<a id="source-bus-to-bus-routing"></a> <a id="source-converting-older-fixed-bus-projects-to-flexbus"></a> <a id="source-customizing-the-onscreen-mixer-controls"></a> <a id="source-flexbus-bus-routing-buttons"></a> <a id="source-flexbus-routing-and-mixing"></a> <a id="source-introduction-to-mixing"></a> <a id="source-legacy-fixed-bussing"></a> <a id="source-main-and-submix-bus-buttons"></a> <a id="source-mixing-in-the-fairlight-page"></a> <a id="source-mixing-in-the-fairlight-page-part-1"></a> <a id="source-the-mixer"></a> <a id="source-the-small-track-mixer-view"></a> <a id="source-tracks-and-busses"></a> <a id="source-using-legacy-fixed-busing"></a> <a id="source-what-is-a-bus"></a>

### Mixing in the Fairlight Page

Think of the Mixer as the command center of the Fairlight page: it gives you everything required to blend a program’s separate audio tracks into a unified, balanced result. Drawing on EQ, dynamics, panning, and level control — plus every kind of Fairlight FX, VST, and Audio Units plugin effect, all fully automatable — you can shape your sound and bring each track’s parts into balance with the rest. The purpose of this chapter is to walk through the Mixer’s many functions so its capabilities are yours to command.

### Introduction to Mixing

Here you’ll learn to lean on the Mixer for setting levels and refining the sound of every track in the timeline. The emphasis falls on what the channel strip controls do, apart from a few topics covered elsewhere: bussing is detailed in Chapter 171, “Setting Up Tracks, Busses, and Patching.” Recording audio is covered in Chapter 173, “Recording.” Mix automation is handled in Chapter 178, “Mix Automation.”

### The Mixer

Through a panel of onscreen controls, the Audio Mixer lets you route track channels to output channels, tune EQ and dynamics, set levels and capture automation, pan both stereo and surround material, toggle mute and solo per track, and insert Fairlight FX, or VST, or AU effects plugins. In the simplest case, every audio track in the timeline maps to one channel strip within the Mixer, and a lone main stereo mix bus named “Bus 1” gathers all those tracks into a single overall mix by default.

The Audio Mixer, its channel strips matched up with the Timeline’s tracks

### Tracks and Busses

As soon as you begin adding busses, the Audio Mixer reveals two groups of channel strips. The strips on the left side stand for the audio tracks in the Timeline, whereas the strips farther to the right surface a control set for each bus you’ve built.

Out of the box, the Audio Mixer splits into two zones — tracks live at left and busses at right. Should your tracks and busses together exceed what fits across your display, each Mixer half carries its own scroll bar, letting you pick which tracks and which busses sit side by side. You can equally drop the divider between the two zones for one continuous scrolling view of every track, or rearrange the channels and where they split.

### FlexBus Routing and Mixing

FlexBus is the name given to the Fairlight audio engine’s bussing system. True to that name, FlexBus delivers a high degree of freedom over bus types and how signals are routed. The earlier Fixed Bus arrangement in DaVinci Resolve Fairlight (used prior to DaVinci Resolve v17) provided a more constrained, fixed bus topology that remains available, yet FlexBus lets you patch outputs and sends however a given project demands. Under FlexBus, any track may feed up to ten busses, plus sends — each with their own level and pan controls — to ten more busses. A bus can route into other busses as many as six layers deep, which supports intricate stem building and processing and yields separate deliverables. See Chapter 171, “Setting Up Tracks, Busses, and Patching,” for more.

### What is a Bus?

In an audio mixer, a bus is nothing more than a shared point where signals join. A bus may be mono, stereo, or some wider format such as 5.1 or Dolby Atmos 9.1.6 (which carries 16 audio signals). These bussed junctions serve as the audio’s mixing points: every audio track sending its signal into the bus is added together to form a master output for that bus.

### Bus-to-Bus Routing

Some mixes need only one bus — the default stereo Main 1 bus might suffice for straightforward stereo work. Alternatively, you can build “submixes” in which several busses pour into still other busses to form a master mix. You might, say, keep a dialogue bus, an effects bus, and a music bus so each group can be controlled on its own through its bus “master,” then send those 3 masters into a main output bus for the final rendered mix. The output of a bus can also be routed to an audio track to record what comes out of it, or sent to monitor speakers so you can hear the real time result. And ultimately, the Deliver page is able to render whatever your chosen master bus outputs into a final bounced file.

The FlexBus architecture lets a wide range of bus track types be created or altered. Because busses are user-definable, they support bus-to-bus, bus-to-track, or track-to-bus routing, and each bus can sum signals running from mono all the way to fully immersive formats (Dolby Atmos and Ambisonics, for example) however you choose. Just like every other audio track type in Fairlight, bus types remain changeable whenever the need arises. What makes FlexBus so capable is that it can steer signals toward many destinations simultaneously, enabling elaborate mixing setups. Suppose you must produce two mixes whose content is the same but whose output levels differ. You could set up two mix busses — one aimed at a target output level of -14 LUFS and the other at -24 LUFS. The completed mix signal goes to a single bus, which then splits into two further busses: one carrying a limiter tuned for the -14 LUFS mix and the other set correctly for the -24 LUFS mix, so both versions emerge at once. With Ambisonic work, one Ambisonic bus can be routed into another even when their orders don’t match, and the Fairlight engine and FlexBus take care of any necessary up- or down-mixing on their own.

Broadened Dolby Atmos features and Ambisonics are both supported by FlexBus; turn to Chapter 184, “Immersive Audio Workflows,” for details.

### FlexBus bus routing buttons

### Legacy Fixed Bussing

Before DaVinci Resolve 17, the Mixer used a fixed layout with set, unchanging counts of sends, submix busses, and main outputs. To stay compatible with older projects, DaVinci Resolve continues to support that earlier “legacy” bussing layout. Under today’s FlexBus bussing, the Mixer’s appearance differs a bit: the legacy Mixer’s Aux panel is now called Bus Send, and its Main/Submix panel is now Bus Outputs. Within the legacy Fixed Bus view:

- The channel strip for each audio track carries Main and Submix bus buttons, which route that strip’s audio output either to a Sub (commonly used to group subsets of tracks into submixes) or to a Main (commonly used for outputting or rendering complete mixes).
- Every Sub and Aux channel strip carries a set of Main buttons, allowing varied groupings of Subs to be routed to each Main. Because Main channel strips are the end of the bussing chain, they bear no buttons.
- Tracks are routed to busses, and busses to other busses, by way of the Main and Submix buttons.

### Main and Submix bus buttons

### Using Legacy Fixed Busing

Should you prefer the former Fixed Bus mapping approach, you can enable it on new projects by opening the Project Settings > Fairlight panel and ticking the “Use fixed bus mapping” checkbox. That said, since the older legacy fixed bus system offers no real benefit and a number of capabilities exist only in FlexBus, FlexBus is the recommended choice.

### Converting Older Fixed Bus Projects to FlexBus

To migrate an older Fixed Bus project over to FlexBus, follow these steps:

- Open Project Settings > Fairlight.
- Beneath the Bussing heading, clear the “Use fixed bus mapping” checkbox.
- A dialog then appears that lets you convert the project to FlexBus.

### Customizing the Onscreen Mixer Controls

Found in the Mixer’s upper right-hand corner, the 3 dot Option menu offers a range of choices for tailoring how the Mixer looks and for deciding which controls stay visible or hidden:

### The Small Track Mixer view

- Full Track Mixer or Small Track Mixer option: The Full Track Mixer devotes extra space to buttons and controls big enough to read without straining, whereas the Small Track Mixer fits a far greater number of channel strips on screen simultaneously.
- Show Labels option: These are the category names for the Mixer’s functional regions, shown along the far left edge of the channel strip area. They help newcomers find their way, but after you grow comfortable with the layout, switching them off frees up a little extra space for an additional channel strip or two.
- Channel Strip Control Visibility options: Lets you reveal or conceal controls within the Mixer. Anything you won’t be using, no longer need to tweak, or want left undisturbed can be hidden.
