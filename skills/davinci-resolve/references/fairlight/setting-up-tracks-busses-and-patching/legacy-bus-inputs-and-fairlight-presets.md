# Input menu with legacy fixed bussing and Fairlight presets library

Version: DaVinci Resolve 20.3 Reference Manual. Context: Setting up tracks busses and patching.
[Chapter index](INDEX.md) / [Previous section](legacy-fixed-bus-patching-and-a-channel-strips-input-menu.md)
<a id="source-filter-by-menu-of-preset-types"></a> <a id="source-input-menu-with-legacy-fixed-bussing"></a> <a id="source-the-fairlight-presets-library"></a> <a id="source-update-or-create-new-preset-dialog"></a> <a id="source-using-the-presets-library"></a>

### Input Menu with Legacy Fixed Bussing

Under the legacy Fixed Busing, the options there differ a little. Here's how they look once it's enabled. Input The Patch Input/Output window opens configured to let you patch assorted inputs (the system audio input, for example) onto the tracks of the Timeline. That speeds up readying audio inputs ahead of recording. Aux Bus A shortcut opening the Patch Input/Output window (covered earlier in this chapter), which opens configured to let you patch assorted Aux busses onto specific submix and Timeline track channels. Sub Bus A shortcut opening the Patch Input/Output window (covered earlier in this chapter), which opens configured to let you patch assorted Sub (submix) bus channels onto specific Timeline track channels. Main Bus A shortcut opening the Patch Input/Output window (covered earlier in this chapter), configured so you can route assorted Main bus channels toward particular Timeline track channels. Path Settings Picking this brings up the Path Settings window, whose controls tune the input level of audio signals arriving from an input/output device.

### The Fairlight Presets Library

The Fairlight page provides a strong, adaptable preset system letting you store and recall presets for everything from the entire configuration of the audio page down to individual presets for plugins. Reaching the presets library is done through Fairlight > Presets Library.

The Fairlight Presets Library, its saved presets along the left panel and the target tracks down the right

Up at the upper left, a Filter By dropdown menu lets you pick which preset type you want to work with.

### Filter By menu of preset types

The choices are:

- Equalizer Presets: Presets for the built-in channel EQ.
- Dynamics Presets: Presets for the built-in Dynamics Processor.
- Plugins Presets: Fairlight FX, AU, or VST.
- Global Track Presets: All settings for a Mixer channel strip.
- Global Bus Presets: All settings for a Mixer bus.
- Fairlight Configuration Presets: Numerous parameters of the Fairlight page get stored as a preset, including:
- Track height.
- Which tracks stay visible versus hidden within the Index's Tracks pane.
- Split point in the Mixer.
- Full Track vs. Small Track views in the Mixer.
- Track Groups enable status.

NOTE: A handful of items aren't presently kept in Fairlight Configurations, such as which panels show (Media Pool or Index, for example), Meter Panel show/hide, Fairlight video window docking, plus the size when the video window is set to float.

### Using the Presets Library

From the Filter By dropdown menu over on the left, choose whichever preset type you intend to work with. Over on the right, the tracks list (present for most preset types) serves a dual role: it's both a roster of sources holding information you'd like stored and a roster of destinations you'd like assigned once presets exist. To store and recall and assign presets:

- The first time you store a preset, choose, over in the window's right-hand tracks list, the source track you'll be pulling the preset type from (a Fairlight Configuration preset being the exception, since it's global and presents no tracks to pick).
- Click the Save New button to store your preset.
- To load your preset onto a different track, clear any tracks currently selected in the track list on the right, then pick the track(s) you'd like to assign to. Click Apply and the preset loads.
- To store a fresh version of an existing preset or refresh your current one, begin by choosing a track in the track list that already has your preset assigned. Next click the Save New button; a dialog then appears offering the choice to refresh the preset's existing version or to store a brand-new preset built from the current settings.
- To Delete a preset, pick it in the list, then click the Delete button.

### Update or Create New preset dialog
