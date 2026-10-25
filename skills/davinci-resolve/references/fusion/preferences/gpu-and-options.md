# Gpu and options

Version: DaVinci Resolve 20.3 Reference Manual. Context: Preferences.
[Chapter index](INDEX.md) / [Previous section](settings-and-color-depth.md) / [Next section](loader-preferences-and-defaults.md)
<a id="source-debugging"></a> <a id="source-document-layout"></a> <a id="source-gpu"></a> <a id="source-layout"></a> <a id="source-loader"></a> <a id="source-options"></a> <a id="source-program-layout"></a> <a id="source-the-gpu-preferences"></a> <a id="source-the-layout-preferences"></a> <a id="source-window-settings"></a>

### GPU

Only Fusion Studio offers the GPU preference. Within DaVinci Resolve, GPU processing is set up through Resolve's Memory and GPU preferences. Inside Fusion Studio, the GPU preference defines which GPU acceleration method handles processing, according to your computer platform and what your hardware can do. It additionally governs enabling caching plus debugging of GPU devices and tools.

### Options

Among the GPU options are radio buttons that decide whether the GPU is engaged during processing and, when it is, which computer framework handles communication with the GPU.

- GPU Tools: Three settings exist for this preference: Auto, Disable, and Enable. With Disable chosen, tools and third-party plugins get no GPU acceleration, though Fuses might still call for it. Pick Enable and GPU acceleration becomes available to tools and plugins, provided the right drivers are present.

### The GPU preferences

- API: Which GPU processing method is applied is chosen by the API setting.
- Device: When several GPUs are present, the Device setting picks which GPU hardware gets used.

With the Auto setting, GPU processing takes precedence; should it be unavailable, however, Fusion falls back on the platform default. As things stand, both the AMD and CPU options need one of two installs present. The first is the driver named AMD Catalyst 10.10 Accelerated Parallel Processing (APP) technology Edition; the alternative is ATI Stream SDK 2.1 or a later version. The Select setting hands you explicit choice of the device.

### Debugging

The higher-level preferences housed in this section exist for diagnostics and for examining how the GPU is operating.

- Verbose Console Messages: Switching this on prints information to the Console — Startup Logs, Compiler Warnings, and Messages, for instance.
- OpenGL Sharing: Turning this on pools system RAM together with onboard GPU RAM, yielding a bigger yet slower OpenGL memory pool.
- Clear Cache Files: Choosing this wipes the GPU code that's already compiled, after which the kernels get recompiled.

### Layout

You'll find the Layout preferences only in Fusion Studio. To store a Layout from DaVinci Resolve's Fusion page, go through the Workspace > Layout Presets menu. The Layout options govern the arrangement, size, and placement of the assorted windows in Fusion's interface at startup or when a comp gets created.

The options are numerous, yet in practice you just arrange the interface however you like it at startup and as each new composition opens, then bring up this Preferences panel and press the three buttons to capture the Program Layout, the Document Layout, and the Window Settings.

### The Layout preferences

### Program Layout

The Program Layout serves to store the overall Fusion interface window together with any floating windows that are open. Every fresh composition you open inside the larger overall Fusion interface window will conform to these preferences.

- Grab Program Layout: Hitting this button records the application's current overall position and size.
- Run Mode: From this menu you set the application's default startup mode, choosing among a Maximized application window, a Minimized application, or a Normal application display.
- Use the Following Position and Size: When ticked, Fusion Studio launches using the values captured at the time Grab Program Layout was pressed.
- Create Floating Views: When ticked, the floating viewers' position and size get recorded whenever the Grab Program Layout button is used.

### Document Layout

What the Document Layout stores is the arrangement of panels and windows for the Fusion comp you're currently in.

- Recall Layout Saved In Composition: When ticked, loading a saved composition brings back every Document Layout setting from the controls beneath.
- Grab Document Layout: Hitting this button records the whole interface setup, taking in all the inner positions and sizes of panels and work areas.
- Window: When a single composition uses several windows, this menu picks which window the Window Settings will affect.

### Window Settings

Instead of storing whole comp layouts, the Window Settings let you store the position and size of individual floating windows and panels within a comp.

- Automatically Open This Window: When ticked, the chosen window opens on its own for new flows.
- Grab Window Layout: Hitting this button records the chosen window's size and position.
- Run Mode: Pick the default run mode for the chosen window. Your choices are a

Maximized window, a Minimized window, or a Normal window display.

- Use Grabbed Position and Size: When ticked, the chosen window is created from the

stored position and size.

### Loader

You'll find the Loader preferences only in Fusion Studio. The Loader preferences let you configure the default Loader's color depth and aspect ratio and also set up the local and network cache settings.
