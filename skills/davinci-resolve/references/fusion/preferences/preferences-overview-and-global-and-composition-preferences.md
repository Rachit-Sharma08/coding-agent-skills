# Preferences overview and global and composition preferences

Version: DaVinci Resolve 20.3 Reference Manual. Context: Preferences.
[Chapter index](INDEX.md) / [Next section](user-interface-and-view.md)
<a id="source-3d-view"></a> <a id="source-categories-of-preferences"></a> <a id="source-defaults"></a> <a id="source-flow"></a> <a id="source-frame-format"></a> <a id="source-general"></a> <a id="source-global-and-composition-preferences"></a> <a id="source-path-map"></a> <a id="source-preferences"></a> <a id="source-preferences-overview"></a> <a id="source-preferences-part-1"></a> <a id="source-script"></a> <a id="source-spline-editor"></a> <a id="source-splines"></a> <a id="source-timeline"></a> <a id="source-tweaks"></a>

### Preferences

This chapter walks through the assorted options on offer in the Fusion Preferences Window.

### Preferences Overview

A broad range of optional settings lives in the Preferences window, letting you shape Fusion’s behavior to fit your working environment more closely. You reach these settings through the Preferences window, opened by way of a menu sitting up near the interface’s top edge. Within DaVinci Resolve, opening the Fusion Preferences window is done in one of these ways:

- On macOS, switch to the Fusion page and choose Fusion > Fusion Settings.
- On Windows, switch to the Fusion page and choose Fusion > Fusion Settings.
- On Linux, switch to the Fusion page and choose Fusion > Fusion Settings. Within Fusion Studio, opening the Fusion Preferences window is done in one of these ways:
- On macOS, choose Fusion Studio > Preferences.
- On Windows, choose File > Preferences.
- On Linux, choose File > Preferences.

The Preferences window includes composition settings.

### Global and Composition Preferences

A category sidebar runs down the left of the Preferences window, with the settings panel filling the right. Fusion Studio carries two tiers of preferences: Global and Composition. On the Fusion page in DaVinci Resolve there is only one Global preference, and it governs every project, whether new or already made. The Global preferences hold options tied to Fusion’s overall behavior together with the defaults for each new composition. In Fusion Studio, the Composition preferences can further tweak whichever composition is currently open without disturbing the Global preferences or any other composition that happens to be open yet not on display.

### Categories of Preferences

The Global preferences claim the very first entry in the Preferences sidebar. Clicking the Global and Default Settings disclosure arrow opens up the sections that follow.

Fusion Studio Global and Default settings

### 3D View

The 3D View preferences hand you control over a range of 3D Viewer parameters, among them grids, the starting ambient lighting arrangement, plus Stereoscopic views. AVI (Windows Fusion Studio Only) The AVI preferences establish the default compression options applied as a Saver node writes out AVI files. You can override these on a case-by-case basis through the Format tab in the Saver’s Inspector.

### Defaults

The Defaults preferences let you settle the default behavior for a spread of choices, among them animation, the global range, how timecode is shown, and the automatic merging of tools.

### Flow

A good number of the options living in the Node Editor’s contextual menu are also adjustable through the Flow preferences, including the settings for Tile picture, the Navigator, and pipe style.

### Frame Format

The Frame Format preferences let you build new frame formats and also pick the default image height and width when you add new creator tools like Background and Text+. You set the playback frame rate here too.

### General

The General preferences gather options for everyday operation, such as auto save and the gamma settings for color controls. GPU (Fusion Studio Only) The GPU preferences carry options for picking specific GPU acceleration methods according to your computer platform and hardware. They are also used for switching on caching and for debugging GPU devices and tools. Layout (Fusion Studio Only) The Layout preferences let you save the precise arrangement of Fusion’s windows. Loader (Fusion Studio Only) The Loader preferences are where the default Loader’s depth plus its aspect ratio get their options, and where you spell out the local and network LoaderCache settings. Memory (Fusion Studio Only) The Memory preferences configure memory management for multi-frame and simultaneous branch rendering. Network (Fusion Studio Only) The Network rendering preferences set up options like picking a render master, email notification, and whether the machine may act as a render slave.

### Path Map

The Path Map preferences establish the virtual file path names that Loaders and Savers draw on, plus the folders Fusion consults to find comps, macros, scripts, tool settings, disk caches, and the rest. Preview (Fusion Studio Only) The Preview preferences are the place to establish the options for Preview creation along with playback. QuickTime (macOS Fusion Studio Only) Here is where the QuickTime codec used for rendering gets preset.

### Script

The Script preferences include a field for the passwords that run scripts externally, the programs used to edit scripts, and the default Python version to apply.

### Spline Editor

The Spline Editor preferences let you set a range of spline options covering Autosnap behavior, handles, markers, and more.

### Splines

The Splines preference holds options for handling and smoothing animation splines, Tracker path defaults, onion-skinning, roto assist, and more.

### Timeline

The Timeline preferences are where you build and edit Timeline/Spline filters and set the default options for the Keyframes Editor.

### Tweaks

The Tweaks preferences handle assorted settings that change behavior when frames load over the network and during queue/network rendering.
