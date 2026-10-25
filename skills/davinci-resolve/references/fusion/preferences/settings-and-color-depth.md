# Settings and color depth

Version: DaVinci Resolve 20.3 Reference Manual. Context: Preferences.
[Chapter index](INDEX.md) / [Previous section](auto-tools-and-global-range.md) / [Next section](gpu-and-options.md)
<a id="source-auto-save"></a> <a id="source-color-depth"></a> <a id="source-general-1"></a> <a id="source-preferences-part-2"></a> <a id="source-proxy"></a> <a id="source-settings"></a> <a id="source-the-general-preferences"></a> <a id="source-usability"></a>

### Settings

The Settings section spells out the format chosen in the Default Format menu. You can change an existing format or build a new one.

- Width/Height: When building a new format for the menu or changing an existing menu item, you give the format’s Width or Height in pixels through these fields.
- Frame Rate: Enter or view the frames per second the format plays. From the Saver tool, this becomes the default Frame Rate for previews as well as final renders. The comp’s own playback is fixed by it too, along with the frame-to-time-code conversion for tools that take temporal inputs.
- Has Fields: With this checkbox on, any Creator or Loader tool added to the Node Editor will run in Fields process mode.
- Film Size: This field defines how many frames sit in one foot of film. The value drives the display of time code in Feet + Frames mode.
- Aspect Ratio: The chosen frame format’s pixel aspect ratio is established through these two fields.
- Guide 1: The four fields for Guide 1 set the left, top, right, and bottom guide positions for

the custom guides in the viewer. Repositioning a guide means typing a value somewhere in the 0 to 1 range. At the bottom-left corner the value is forever 0/0, and at the top-right corner it is forever 1/1. Should the entered value’s aspect fail to agree with the frame format defined by the Width and Height parameters, a further guide turns up onscreen. The dotted line marks the image aspect centered about Guide 1’s Center values.

- Guide 2: This setting fixes the image aspect ratio against the whole frame format width and height. Values above 1 shrink the height relative to the width. Values below 1 grow the height relative to the width.
- New: The New button is how a fresh default setting joins the drop-down menu. After the button is clicked, the dialog box that pops up is where you name that setting.
- Copy: Pressing the Copy button duplicates whatever setting is current, giving you a fresh one to customize.
- Delete: Pressing the Delete button takes whatever setting is current off the default drop-down list.

### Color Depth

Within the Color Depth section, its three menus let you select the color mode that handles preview renders, interactive renders, and full (final) renders. Working an image at 8-bit gives you the lowest color depth, seldom adequate for final work these days, yet perfectly fine for quick previews. 16-bit color brings far greater color fidelity at the cost of more system resources. Both 16-bit and 32-bit float per channel consume still more system resources and are the best fit for digital film and HDR rendered images. By default, the composition pays these options no mind until a Loader or Creator tool has its Color Depth control set to Default.

### General

The sections gathered under the General preferences bear on how the Inspector behaves and on a few additional user interface elements besides.

### Usability

Under Usability sit a range of project, Node Editor, and user interface settings that, according to how you work, can smooth out using the application.

- Auto Clip Browse: With this checkbox on, the File Browser appears automatically when a new Loader or Saver is added to the Node Editor.
- New Comp on Startup: When ticked, a new, empty project is created each time Fusion Studio launches. This has no bearing on DaVinci Resolve’s Fusion page.

### The General preferences

- Summarize Load Errors: While loading node trees, or “comps,” that hold unknown tools (for example, comps built on other computers with plugins absent from the current machine), the missing tools are summarized in the console instead of a dialog appearing for every missing tool.
- Save Compressed Comps: This option lets node trees be saved compressed rather than as ASCII-based text files. Compressed node trees occupy less disk space, though they may take a moment longer to load. Node trees holding complex spline animation and many paint strokes can swell into tens of megabytes with this option off. Compressed comps, however, cannot be edited in a text editor unless saved again uncompressed.
- Show Video I/O Splash: This toggles whether the Splash image appears over the video display hardware. It applies only to Fusion Studio.
- Use Simplified Copy Names: This option cuts down on the underscores that appear in tool names when copying.
- Show Render Settings: With this checkbox ticked, the Fusion Render Settings dialog appears each time a render begins in Fusion Studio. Holding Shift as you start a render stops the dialog from appearing for that session, applying whatever settings were used on the last render. Switching this option off reverses that behavior.
- Mouse Wheel Affects the Window Under the Pointer: As a rule, a turn of the mouse wheel or a trackpad swipe affects whichever window is active. With this option on, the affected window is the one lying under the cursor, so there is no need to click into a window beforehand to activate it.
- Frames Start From: This fixes which frame number begins the clip times in the Loader and its Clip list.
- Show Color As: This setting pins down the numeric scale that stands in for colors. Your options are Normalized (0 to 1), 8-bit (0 to 255), and 16-bit (0 to 65,535). The image’s real processing and quality stay untouched, yet it can ease the mental arithmetic you sometimes do when working out adjustments.

### Auto Save

The Auto Save settings take effect in Fusion Studio alone. For auto backups on the Fusion page within DaVinci Resolve, turn instead to the DaVinci Resolve Project Load and Save Preferences. With Auto Save switched on in Fusion Studio, comps write themselves to a backup file at steady intervals that the Delay setting fixes. Should a backup file turn up as you go to open the comp, you are offered the choice between loading the backup and loading the original. When the backup comp is opened from the location named in the Path Map preference, saving that backup writes over the original file. When the backup file is shut without saving, it gets deleted while the original stays intact.

- Save Before Render: When on, the comp is saved automatically before a preview or final render begins.
- Delay: This preference sets the interval between Auto Saves. The interval uses mm:ss notation, so entering 10 makes an Auto Save happen every 10 seconds, whereas entering 10:00 makes an Auto Save every 10 minutes.

### Proxy

- Update All, Selective, No Update: The Update mode button sits above the toolbar. This preference lets you pick which mode fresh comps adopt by default. Ordinarily that default is Selective, which renders just the tools required to put the images up in the Display view. All renders every tool in the composition, whereas None blocks all rendering.
- Standard and Auto: These sliders set the default ratio used to create proxies once the Proxy and Auto Proxy modes are switched on. These settings leave the final render quality alone.

Although the images get processed at a reduced size compared with their originals, the viewing scales shown in the viewers continue to reference the original resolutions. On top of that, image processing carried out in Proxy Scale mode can vary a little from rendering at full resolution. You can adjust the Proxy and Auto Proxy size ratios straight from the interface by right-clicking the Prx and APrx buttons above the toolbar and picking the value you want from the contextual menu.
