# Parallel loudness measurement and selecting a downmix option

Version: DaVinci Resolve 20.3 Reference Manual. Context: Immersive audio workflows.
[Chapter index](INDEX.md) / [Previous section](enabling-the-ambisonics-meter-overlay-and-ambisonic-effects.md) / [Next section](export-and-selecting-tracks-and-busses-to-export.md)
<a id="source-atmos-re-renders"></a> <a id="source-auro-3d-support-studio-version-only"></a> <a id="source-bounce-mix-to-track-dolby-atmos-re-render-options"></a> <a id="source-dolby-atmos-configuration-controls"></a> <a id="source-dolby-atmos-render-preset-options"></a> <a id="source-low-latency-rendering"></a> <a id="source-mpeg-h-authoring"></a> <a id="source-object-based-format-support-studio-version-only"></a> <a id="source-parallel-loudness-measurement"></a> <a id="source-selecting-a-downmix-option"></a> <a id="source-surround-buses-in-fairlight-studio-version-only"></a> <a id="source-track-configuration"></a>

### Parallel Loudness Measurement

While the render runs, a parallel 5.1 down-mix can serve as the source for a 5.1 loudness measurement. Some delivery specifications (those for Netflix, for instance) demand that the loudness measurement of Atmos Masters happen at 5.1. You're able to switch on this parallel 5.1 (or stereo) render for the loudness measurement while still monitoring in the room's native format.

### Selecting a Downmix option

### Low-latency Rendering

Earlier builds of the Dolby Atmos Renderer ran at a fixed latency of 10.67 ms. With that limit gone, you can now pick lower latency engine processing block sizes, which brings monitoring latency through the Dolby Atmos renderer down. The renderer does, however, force the larger block size during certain operations — the Binaural renderer, say, or whenever a parallel loudness down-mix is switched on.

### Surround Buses in Fairlight (Studio Version Only)

Fairlight's FlexBus structure opens up user-definable buses. Atmos mixes need several bus formats, which DaVinci Resolve 17 and later make available.

- 9.1.6
- 22.2

### Object-Based Format Support (Studio Version Only)

- Dolby Atmos with support for 7.1.2 and 7.1.4
- MPEG-H with support for 5.1.4, 7.1.4, and 7.2.3
- SMPTE ST.2098 with support for 9.1 OH, 9.1 HT, 11.1 HT, 13.1 HT, and 15.1 HT

### Auro-3D Support (Studio Version Only)

- Auro-3D with support for 9.1, 10.1, 11.1 (7+4), 13.1

### Dolby Atmos Configuration Controls

By way of the Video and Audio I/O panel of the Resolve System Preferences, you can switch on and configure the use of a Dolby RMU for Dolby Atmos mixing. Type in the RMU's IP address and pick the base audio output.

Configuring Dolby Atmos in the Resolve System Preferences

### Atmos Re-Renders

To keep things on par with the external renderer, you can build presets that spell out a PCM output format together with a set of sources drawn from the bed, object, and group definitions (5.1, for example). Bounce Mix to Track makes room for these re-render presets inside Dolby Atmos timelines, so a single pass can turn out several deliverables. The render presets get stored and recalled along with the timeline.

### Bounce Mix to Track Dolby Atmos re-render options

Beyond the render format, the source can be picked from some combination of beds, objects, or defined VCA groups.

### Dolby Atmos Render Preset options

### MPEG-H Authoring

DaVinci Resolve supports MPEG-H authoring. That covers Native MPEG-H track and bus formats plus monitoring, including the option to set basic track-level meta-data for export into an MPEG- H scene, along with export of a MPEG-H Master file. Switch it on and the formats turn up as choices for a bus, track, or monitoring format inside the Bus Format window.

The MPEG-H format options in the Bus Format window

The same formats also turn up for multi-channel track assignment.

The MPEG-H format options in the Track Format submenu Much as with most immersive content, tracks are mixed natively, building a bed mix out of a set of immersive object tracks driven by dynamic panning. Those get folded onto the main bus to make up the immersive mix.

### Track Configuration

On top of that process, switching the format on enables a set of MPEG-H meta-data columns in the DaVinci Resolve Track index — namely Track Type, Kind, Language, SW Group, and Preset.

These columns, and the steps to configure them, get a fuller treatment in Chapter 170, “Using the Fairlight Page.”

With MPEG-H switched on in the Project Settings, the Tracks panel surfaces extra columns of information for defining every track within the Timeline
