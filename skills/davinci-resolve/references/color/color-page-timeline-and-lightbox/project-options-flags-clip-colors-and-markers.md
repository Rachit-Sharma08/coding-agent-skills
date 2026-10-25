# General options panel of the project settings and flags clip colors and markers

Version: DaVinci Resolve 20.3 Reference Manual. Context: Color page timeline and lightbox.
[Chapter index](INDEX.md) / [Previous section](thumbnail-information-and-representative-image.md) / [Next section](preset-timeline-filters-overview.md)
<a id="source-flags-clip-colors-and-markers"></a> <a id="source-general-options-panel-of-the-project-settings"></a> <a id="source-timeline-filtering"></a> <a id="source-timeline-filtering-options"></a>

### General Options panel of the Project Settings

Found in the Conform Options group within the Project Settings' General Options panel, a checkbox lets you adjust how C mode sorting behaves. Open the Settings window and click the Project Settings' General Options panel to expose the Sort Timeline Using Reel Name and Timecode checkbox. When that box is on (its default), every Timeline clip sorts by reel name first and then by source timecode. That way, clips carrying similar timecode off the same reel land beside each other under C mode. Turn the box off and reel name is disregarded, with all Timeline clips sorted solely by source timecode. The result may blend clips from several sources together, yet it proves handy in certain cases.

For instance, when grading dailies off a three camera shoot, you might prefer to view back-to-back clips from each of the three cameras lined up in turn on the Timeline, so that Cam1*Shot1, Cam2_Shot1, and Cam3_Shot1 come first, trailed by Cam1_Shot2, Cam2* Shot2, and Cam3_Shot2, and onward. Here you don't want the clips from cameras 2 and 3 shoved to the Timeline's tail end merely on account of their reel name.

### Flags, Clip Colors, and Markers

Just as in the Edit page, the Color page lets you flag or mark clips to keep track of specific media or frames you might need to attend to down the line. As an example, you could tag every closeup of one actor showing a blemish you intend to spend time repairing with a green flag. Ways to flag, recolor, and mark clips on the Color page:

- To add a flag to a clip: Park the playhead on a Mini-Timeline clip, then pick a color out of the Mark > Add Flag submenu, or Right-click whichever clip's thumbnail you like and grab a flag color from the Flags submenu. Since flags aren't frame-bound, flagging a single clip drops flags onto each other clip relying on that same source media in the Media Pool as well.
- To remove all of a clip's flags: Park the playhead on a Mini-Timeline clip, then go to Mark > Clear Flags, or right-click that clip's thumbnail and pick Flags > Clear All.
- To change the clip color: Park the playhead on a Mini-Timeline clip, then pick a color from the Mark > Set Clip Color submenu, or Right-click whatever clip's thumbnail and grab a color out of the Clip Color submenu. Clip Colors are clip-specific.
- To remove a clip's color: Park the playhead on a Mini-Timeline clip, then go to Mark > Set Clip Color > Clear Color, or right-click that clip's thumbnail and pick Clip Color > Clear Color.
- To mark a frame of a clip: Right-click that clip's thumbnail and grab a marker color from the Marker submenu.
- To remove a single marker: Right-click the clip's thumbnail and pick Delete Marker out of the Marker's submenu. As another route, highlight the marker within the Mini-Timeline and tap the Delete key.
- To remove all of a clip's markers: Right-click the clip in question and pick Clear All from the Markers submenu.

### Timeline Filtering

Sitting to the right of the Clips button up at the Color page Interface Toolbar's top right, a drop-down button offers preset ways to filter on the fly which clips the Timeline shows. With it you can mask every other Timeline clip aside from the subset you wish to concentrate on.

### Timeline filtering options

Take an example: after you've attached flags or markers to clips, masking every remaining Timeline clip that fails the test — say, hiding any clip lacking a green flag — becomes easy. None of this touches the underlying edit, and you can restore the Timeline to its starting state whenever you wish.

To filter the Timeline:

- Click the Timeline Filtering drop-down button, which sits just right of the Clips button over at the DaVinci Resolve UI's top left, then pick whichever option is offered. While filtering remains in effect, an orange line shows beneath the Clips button in the page's top UI toolbar.

To return the Timeline to normal:

- Click the Timeline Filtering drop-down button, and choose All Clips. Timeline filtering pairs with either A or C mode sorting so you can lay clips out in whatever fashion suits the job at hand. Clip filtering works in the Lightbox as well, and whichever clip filtering method is active will isolate clips across both the Timeline and Lightbox in step as you move between them.
