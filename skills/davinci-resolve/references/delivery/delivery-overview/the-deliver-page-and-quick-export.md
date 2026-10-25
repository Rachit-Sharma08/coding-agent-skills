# The deliver page and quick export

Version: DaVinci Resolve 20.3 Reference Manual. Context: Delivery overview.
[Chapter index](INDEX.md) / [Previous section](deliver-and-delivery-effects-processing.md) / [Next section](deliver-page-viewer-and-skimming-in-the-viewer.md)
<a id="source-assign-icons-to-user-presets"></a> <a id="source-deliver-page"></a> <a id="source-filtering-the-thumbnail-timeline"></a> <a id="source-render-or-edit-to-tape-modes"></a> <a id="source-render-settings"></a> <a id="source-rendering-files-vs-outputting-to-tape"></a> <a id="source-the-deliver-page"></a> <a id="source-the-deliver-page-timeline"></a> <a id="source-the-deliver-pages-timeline-and-thumbnail-timeline"></a> <a id="source-the-interface-toolbar"></a> <a id="source-the-interface-toolbar-1"></a> <a id="source-the-render-settings"></a> <a id="source-the-viewer"></a> <a id="source-using-quick-export"></a> <a id="source-using-the-deliver-page"></a> <a id="source-using-the-deliver-page-1"></a>

## Using the Deliver Page

### Using the Deliver Page

After grading is complete, the project still has to be rendered or sent to tape so it can reach your client. That is precisely the role of the Quick Export window and the Deliver page. The pages ahead cover working with Quick Export, navigating the Deliver page interface as a whole, and offer some background on how DaVinci Resolve outputs effects across various scenarios.

### Using Quick Export

Plenty of jobs do not call for an elaborate delivery configuration. For those moments when a fast export is all you want and the Deliver page’s full capability is overkill, File > Quick Export lets you pick from an assortment of export presets to send your program out from any DaVinci Resolve page. Quick Export can even push your program straight to one of the supported video sharing services — among them YouTube, Vimeo, and Frame.io. Your own presets can be added to the Quick Export window too. To use Quick Export: 1 (Optional) On the Cut, Edit, Fusion, or Color page, mark In and Out points along the Timeline to isolate the portion of the current program you want exported. With no timeline In or Out points placed, the whole timeline goes out. 2 Choose File > Quick Export. 3 From the top row of icons in the Quick Export dialog, pick a preset and hit Export. 4 In the export dialog, point to a directory and type a file name, then click Save. A progress bar dialog comes up to indicate the export’s remaining duration.

A custom preset as it appears in the Quick Export Dialog. Here is how you build a fresh Custom Preset and place it into Quick Export: 1 Over on the Deliver page, choose Custom Export within the Render Settings, then tune the Video, Audio, and File settings for the preset you are building. Custom Presets can only be built from Single Clip settings, never Individual Clips. 2 From the Render Settings 3-dot option Menu, choose Save as New Preset. 3 Enter a name for the new Preset and pick a preset icon to stand for it. 4 Tick the Add to quick export box. 5 Click Save. From now on your preset and its icon appear in the Quick Export Dialog on every DaVinci Resolve page, and they also join the Render Settings on the Deliver Page.

The Quick Export Dialog with its List View icon circled. To switch the Quick Export choices over to List View: 1 Bring up the Quick Export Dialog. 2 Within the Render Settings, click the List View icon.

### Assign Icons to User Presets

As you build a new Custom Preset on the Deliver page, beyond supplying a name you may now select an icon from the list so it can stand for the preset in both the Render Settings and the Quick Export dialog.

Creating a new Custom Preset in the Deliver page

### The Deliver Page

Five functional zones make up the Deliver page, and each one lets you configure a separate aspect of a render or a tape output.

### Deliver page

### The Interface Toolbar

Running along the top edge of the Deliver page sits a toolbar whose buttons toggle the visibility of various interface sections. Reading left to right, those buttons are:

### The Interface toolbar

Delivery full/half height button: Expands the Render Settings panel so it occupies your display’s entire height when you want more room to scroll through the various render settings, trading away some Timeline width in return. Render Settings: This panel enumerates every render setting on offer for configuring rendering jobs in DaVinci Resolve. Out of the box you get a brief list, with further options revealed once you click “Advanced Settings.” Tape: Switches the Deliver page over to Tape Output mode.

Clips: Toggles the Thumbnail timeline shown above the Deliver page timeline Render Queue: A roster of every job you have queued for rendering in the current project. Jobs that were rendered earlier stay put in the queue — handy for reference or for re-rendering them later — until you remove them by hand. Render Queue full/half height button: Stretches the Render Queue across your display’s full height when you need extra space to list render jobs, again at the cost of a slimmer Timeline.

### The Render Settings

Within the Render Settings live the adjustable controls that dictate how DaVinci Resolve renders media out. Selecting the Tape option greys these controls out. The Render Settings break down into four broad sections:

- Render Presets: Up top sits a scrollable strip of icons from which you can grab one of several presets to rapidly configure the kind of render you are after. Picking the Custom option reveals every render setting so you can build a render by hand.
- Render Location: Clicking the Browse button brings up a dialog for selecting the volume and directory you will render into.
- Render: A pair of options lets you render the Timeline’s whole selected region as one clip fit for review or mastering, or as a run of individual clips better aligned with round-trip workflows. Whichever you select shifts which render settings show up underneath.
- Video, Audio, and File Render Settings Panels: Every remaining render setting is spread across three panels. At the top of the Video and Audio panels, checkboxes let you turn off video export on its own (when only the audio should go out) or turn off audio export on its own (when only the video should go out).

For a fuller account of all these settings, refer to Chapter 187, “Rendering Media.”

### Render Settings

### Rendering Files vs. Outputting to Tape

Since the Deliver page serves two purposes, the Tape button in the Interface toolbar is what you use to switch between rendering files and sending output to tape. Pressing it swaps the Viewer’s usual controls for tape controls.

### Render or Edit to Tape modes

### The Deliver Page Timeline

The Timeline on the Deliver page is where you mark out which clips to render or send to tape and which version of each clip should be output. This Timeline is built from a Thumbnail timeline up top — toggled by the Clips button — that makes picking single clips or clip ranges for rendering straightforward, plus a more conventional timeline beneath it on which you place In and Out points to render any arbitrary stretch of your program. A Timeline toolbar handles setting the render range, tweaking how the Timeline looks, and zooming in or out.

### The Deliver page’s Timeline and Thumbnail timeline

TIP: Hitting Shift-Z scales the whole program to fill the Timeline’s available width.

### Filtering the Thumbnail Timeline

On the Deliver page, the Thumbnail timeline also carries a Timeline Filter dropdown, sitting just to the right of the Clips button within the Interface toolbar.

The Deliver page’s Thumbnail timeline matches the Color page

Filtering the Timeline’s contents through this dropdown lets you narrow, in several ways, the span of media you intend to output. As an example, when a timeline has already been rendered but you have made edits since, one of the “Modified Clips” options can be set to surface only the clips altered inside a given timeframe. A second popular choice, “Unrendered Clips,” singles out every clip not yet rendered — useful in workflows where you render only a portion of the Timeline at a time. With the Thumbnail timeline filtered, jobs can be queued solely in Individual Clips mode. Whether Thumbnail filtering is active is indicated by an orange underline beneath the Clips button in the UI toolbar. That orange line below the Clips button signals filtering is on

### The Viewer

As file-based media is rendered, the Viewer presents an exact preview of how the output media will appear under the present settings, while the transport controls drive the playhead across the current Timeline. Clicking the speaker icon toggles audio playback on or off, and right-clicking that same speaker icon and dragging the slider sets the level.
