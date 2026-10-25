# Adding titles and safe area overlays

Version: DaVinci Resolve 20.3 Reference Manual. Context: Titles generators and stills.
[Chapter index](INDEX.md) / [Next section](title-generator-shared-settings.md)
<a id="source-adding-titles"></a> <a id="source-custom-action-and-title-safe-areas"></a> <a id="source-davinci-resolve-title-generators"></a> <a id="source-editing-text"></a> <a id="source-editing-titles-within-the-timeline-viewer"></a> <a id="source-positioning-and-transforming-text"></a> <a id="source-title-generator-panels"></a> <a id="source-titles-generators-and-stills"></a> <a id="source-titles-generators-and-stills-part-1"></a> <a id="source-toggle-extents-for-selected-safe-area-overlays"></a> <a id="source-types-of-title-generators"></a> <a id="source-using-safe-area-overlays"></a>

### Titles, Generators, and Stills

From the Edit page you can drop titles, effects generators, and stills onto your timelines. Customized titles, generators, and stills can also be stored back into the Media Pool so you can reuse them down the line.

### Adding Titles

The Toolbox holds an assortment of titles and generators handy for building leader when you output to tape, dropping in slates, building subtitles, and otherwise meeting whatever text needs your program throws up. To pick and preview titles before dropping them into the Timeline, confirm that "Hover Scrub Preview" is ticked in the Titles option menu, then just glide your pointer across any thumbnail in the Titles tab. Where a title is animated (Fusion titles, that is), sweeping the pointer over the thumbnail previews the animation. After you've settled on your title, you can drag it out of the Titles tab onto your Timeline in the Edit page, or in the Cut page onto either the upper or lower Timelines, or lean on the editing selection modes along the bottom of the tab.

Scrubbing over a Title Thumbnail previews the title in the Viewer. You can edit titles and generators much as you would any other clip. On top of that, when selected, both titles and generators surface the same Composite, Transform, and Cropping parameter groups that any other clip does; with those parameters you can composite titles and sweep them around to build assorted text effects. Ways to add and edit generators and titles:

- To drag and drop a generator directly into the Timeline: Drag and drop titles or generators straight into the Timeline and the resulting clip lands with a default duration of 5 seconds. That duration is adjustable in the Edit panel of the User Preferences.
- To edit a generator using the edit overlays of the Timeline Viewer: On the clip you mean to edit a generator into, click its destination control, then lay down Timeline In and Out points to fix how long the resulting edit runs, and drag the generator you mean to edit onto whichever edit overlay of the Timeline Viewer matches the kind of edit you're after.
- To reposition the text of a title in the Timeline Viewer: In the Timeline, pick the title generator you'd like to edit, then click its visible text within the Timeline Viewer so its bounding box gets selected; in that state you're free to reposition, scale, and rotate the text item. As you move text, it snaps to key spots in the frame such as the Viewer's vertical and horizontal center; hold the Option key to switch off snapping when you'd rather place the text freely.
- To edit the text of a title in the Timeline Viewer: In the Timeline, pick the title generator you'd like to edit, then double-click its visible text within the Timeline Viewer to drop in a text editing cursor. From there you can select, delete, or add any text you like by typing right in the Timeline Viewer.
- To edit the parameters of a generator or title: With the Inspector open, pick whichever generator or title you'd like to edit so it loads into the Inspector.

### Using Safe Area Overlays

This drop-down menu lays plenty of handy framing guides over the Viewer so you can see which part of the image stays in and which part gets cropped away should you alter the Timeline's aspect ratio. You switch the framing guides on and off via the Safe Area Framing Guide icon in the Viewer, and you pick the precise guides from the drop-down menu. Social Media: 1:1, 4:5, 9:16, 1.91:1, 16:9. Broadcast and Film: Default (your current timeline aspect ratio), 1.33, 1.66, 1.77, 1.85, 2.35. Safe Area Guides: These choices lay extra guide lines over the Viewer to keep your composition from getting clipped at the far edges of a physical cathode ray tube. Although it feels a bit dated now that flat screen digital televisions rule, plenty of legacy programs still honor these guidelines. Safe Areas can still earn their keep as guides for making sure the spread of mobile devices and social media sites around today don't accidentally crop your image.

- Action: Hold all movement and important action inside this box.
- Title: Hold all on screen text inside this box.
- Center: Marks the precise middle of the image.

The Safe Area Framing Guide icon (circled), plus the safe area overlays and the framing options you can pick from

### Custom Action and Title Safe Areas

The Editing panel of the User Preferences now carries a "Use custom safe area overlays" checkbox; switch it on and Action Area and Title Area fields appear, letting you dial a custom percentage into each. By default these sit at 93% for Action Area and 90% for Title Area.

### Toggle Extents for Selected Safe Area Overlays

Beyond the Action, Title, and Center overlays, you can also flip the Extents Safe Area overlay on or off. That feature lives at View > Safe Area > Extents.

### Types of Title Generators

Once opened into the Inspector, a title exposes a batch of text parameters letting you style what sits in that clip's Text field right inside the Inspector. Every one of the titles handles rich text, so you can style words, lines, or paragraphs of text on their own using the parameters on hand, Color, Font, and Size among them. Other attributes—Alignment, Anchor, Position, and Shadow—act on the whole title. These titles are on offer: L Lower 3rd: (supports rich text) Drops two lines of text automatically into the bottom left corner of title safe, each carrying its own rich text plus Position/Zoom/Rotation controls for sizing and animating on their own. M Lower 3rd: (supports rich text) Drops two lines of text automatically into the bottom middle of title safe, each carrying its own rich text plus Position/Zoom/Rotation controls for sizing and animating on their own. R Lower 3rd: (supports rich text) Drops two lines of text automatically into the bottom right corner of title safe, each carrying its own rich text plus Position/Zoom/Rotation controls for sizing and animating on their own. Scroll: (supports rich text) Automates a scrolling title run climbing from the bottom of the screen to the top. How long the generator clip lasts in the Timeline sets how fast the scroll moves. Shares the Simple title's parameters. Text: (supports rich text) Good for building titles made of a word, a line, or a paragraph of text. One body of text draws on a single set of rich text controls that let you style chosen portions of the title text differently. Text+: (does not support rich text) A sophisticated title generator drawing on the Fusion page's title generation tools. Compared with the simple title generator above, this one packs far broader control over styling, rendering, and animating, though all title text rides on a single style. Fusion Titles: A range of ready-made title templates put together in Fusion. DaVinci Resolve ships with a library of pre-built Fusion titles, yet you can roll your own to show up in this category of the Effects browser too.

### DaVinci Resolve Title Generators

The original title generators bundled with DaVinci Resolve all carry similar controls, and every one of them can handle rich text styling.

### Editing Titles Within the Timeline Viewer

After you drop a title generator onto the Timeline, the original title generators bundled with DaVinci Resolve give you onscreen controls for editing text and for transforming and placing blocks of text right inside the Timeline Viewer.

### Positioning and Transforming Text

As long as the Timeline playhead sits over a text generator stacked atop one or more background clips, clicking the text in the Timeline Viewer brings up onscreen transform controls matching the Position, Zoom, and Rotation parameters in the Inspector.

Drag the text to position it in the Viewer As you drag text to a new spot, snapping kicks in at the frame's X and Y center, as well as around the frame's outer third. Holding the Shift key while you drag a text object pins movement to just the X or Y axes.

### Editing Text

Double-clicking text in the Timeline Viewer flips that text into an editable state, where you can drop in a text cursor or select characters to edit the text the way you would in any text editor.

Double-click on the text to edit it in the Viewer

### Title Generator Panels

Within the Video Inspector, a text generator's parameters fall across a pair of panels: the Title panel alongside the Settings panel.

- The Title panel holds every text editing, styling, and sizing control used to shape the contents and look of a title in your project, the Rich Text, Drop Shadow, Stroke, and Background parameters included.
- The Settings panel holds the same Composite, Transform, and Cropping parameters that every other clip in DaVinci Resolve carries. Those parameters exist for compositing and animating a title.
