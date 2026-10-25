# Custom sort of clip thumbnails in the media pool and columns in list view

Version: DaVinci Resolve 20.3 Reference Manual. Context: Adding and organizing media with the media pool.
[Chapter index](INDEX.md) / [Previous section](smart-bins-and-metadata.md) / [Next section](media-pool-clip-timeline-and-synced-audio-search.md)
<a id="source-custom-sort-of-clip-thumbnails-in-the-media-pool"></a> <a id="source-editable-name-description-keyword-and-comments-columns"></a> <a id="source-finding-clips-timelines-and-media"></a> <a id="source-the-media-sort-options"></a> <a id="source-the-metadata-view-with-clips-sorted-by-scene-shot-take"></a> <a id="source-using-metadata-view-in-the-media-pool"></a> <a id="source-working-with-columns-in-list-view"></a>

### Custom Sort of Clip Thumbnails in the Media Pool

You’re now able to reposition Media Pool clips by hand in Thumbnail view, so you can cluster clips together however makes visual sense to you.

You enable Custom Sort by picking Custom in the Sort menu of the Media Pool. Choose Thumbnail View in the Media Pool, and from the sort menu pick Custom. From there you can drag your thumbnails into any arrangement or grouping you like. With Snap to Grid picked in the Sort menu, the icons snap into orderly rows and columns. Switch off Snap To Grid to allow freeform placement. When two thumbnails overlap, whichever was moved last sits on top.

With Snap to Grid turned off you may rearrange thumbnails however you wish (overlapping included), and that layout is preserved throughout the Medial Pool across all pages. The placement of your icon thumbnails persists in the Media Pools across every page in DaVinci Resolve. The layout is also kept if you briefly switch to a different sort order and afterward come back to the Custom sort.

### Working With Columns in List View

When you work in List view via the controls at the top right of the Media Pool, you pick up extra organizational control by surfacing columns that display the metadata each clip carries, before media is added to your timeline. These columns are useful for organizing your media.

The Customize Columns window, reached by right‑clicking a column header while in List View Ways to customize metadata columns in List view:

- To show or hide columns: At the top of any Media Pool column, right-click to bring up the Customize Columns window. Within the Column Fields, tick the checkboxes for any columns you want shown or hidden. Unticked columns stay invisible. Once you’re done, click save.
- To rearrange column order: Drag any column header left or right to reorder the columns, or drag the column names into your preferred sequence in the Selected Fields section of the Customize Columns window.
- To resize any column: Drag the boundary between any two columns right or left to shrink or grow that column.
- To sort by any column: Click whichever column header you want to sort by. Each further click on the same header flips that column between ascending and descending sort order.

After you’ve dialed in a column layout suited to your specific purpose, you can store it to recall later.

Ways to save and apply custom column layouts:

- To create a column layout: Show, hide, resize, and reorder the columns you need for a given task, then right-click any column header in the Media Pool, and:
- Choose Customize Columns.
- Click on the option menu, and select Save as New Preset.
- Enter a new name for your column layout and press OK.
- To recall a column layout: In the Media Pool, right-click on any column header, then pick Load Custom Layout and, off the contextual menu, pick whichever column layout name you’d like to apply. Alternatively, pick Load Preset under the preset name within the Customize Columns option menu.
- To edit a column layout: Bring up the column layout you mean to edit, apply whatever changes are needed, then in the Media Pool right-click on any column header and pick Customize Columns. Inside the Customize Columns window, click the Save button. Another route is to pick Update under the preset name within the Customize Columns option menu.
- To delete a column layout: In the Media Pool, right-click on any column header, and pick Customize Columns . Next pick Delete Preset under the preset name within the Customize Columns option menu. To confirm, click delete a second time. Although the metadata columns offered match the fields shown in the Metadata Editor, the columns you get in the Media Pool on the Media and Edit pages amount to just a slice of all the metadata that’s present. You may put any metadata field — custom metadata fields among them — into your Column layouts.

### Editable Name, Description, Keyword, and Comments Columns

Beyond the Clip Name, when the Keyword, Description and Comments columns are shown by the Media Pool in List view, you can change what they contain by clicking once inside a clip’s Description or Comments field, pausing a beat, and then clicking a second time to select that field.

### Using Metadata View in the Media Pool

Within the Metadata View mode, each clip shows up as its own card displaying a thumbnail and basic clip metadata information. This view aims to carry more metadata information than a thumbnail yet more focused information than the List view. The feature, paired with its sort modes, gives you a powerful means of arranging and rearranging clips within the Media Pool. Reading the metadata fields of the Metadata view from top to bottom:

- Thumbnail: A scrubbable thumbnail image of your clip.
- Row 1: A primary description field whose contents shift depending on which sort order you’ve chosen.
- Row 2: Start Timecode, Date Created, Camera #.
- Row 3: Scene, Shot, Take.
- Row 4: Clip Name, Comment.

What makes the Metadata view powerful is the way it automatically clusters your clips by the sort order you pick in the Media Pool Sort By menu, in the very top-right corner of the Media Pool. Every distinct sort mode swaps out the main description field on the card and also reshuffles the Media Pool to mirror the chosen organization method.

The Metadata View icon view (its icon highlighted up in the top bar), with the thumbnail shown mid-scrub beside that clip’s metadata

### The Media Sort options

The sort modes offered within the Metadata view are:

- Bin: Clusters by bin, switches the primary description field over to clip name, and sequences everything by timecode.
- TImecode: Clusters by creation date, drives the primary description field to creation date plus start timecode, and sequences by timecode.
- Camera: Clusters by camera #, drives the primary description field to camera # alongside start timecode, with the sequence again by timecode.
- Date Time: Clusters by day, fills the primary description field with creation date and file name, and runs the sequence off timecode.
- Clip Name: Clusters by whatever first letter the clip name begins with, alphabetically, points the primary description field at clip name, and sequences by timecode.
- Scene, Shot: Clusters by scene, feeds the primary description field with scene-shot-take, and sequences by scene-shot-take.
- Clip Color: Clusters by clip color name, sets the primary description field to creation date and start timecode, and orders everything by timecode.
- Date Modified: Clusters by day, supplies the primary description field with creation date and file name, and sequences by whenever the OS filesystem last changed the clip.
- Date Imported: Clusters by day, fills the primary description field with creation date and file name, and sequences by the date the clip joined the Media Pool.
- Ascending: Arranges the Media Pool running from the smallest numerical value up to the largest, and alphabetically A through Z.
- Descending: Arranges the Media Pool running from the largest numerical value down to the smallest, and alphabetically Z back to A.

### The Metadata view with clips sorted by Scene-Shot-Take

The Metadata view with the same clips sorted by Camera

### Finding Clips, Timelines, and Media

A number of approaches exist for tracking down various items in the Media Pool and Media Storage, whether they’re clips, timelines, or media sitting on disk.
