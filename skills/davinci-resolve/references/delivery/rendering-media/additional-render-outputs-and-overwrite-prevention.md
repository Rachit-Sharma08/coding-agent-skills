# Additional outputs and how to avoid overwriting clips when rendering output media

Version: DaVinci Resolve 20.3 Reference Manual. Context: Rendering media.
[Chapter index](INDEX.md) / [Previous section](audio-panel-and-file.md) / [Next section](render-queue-jobs-across-projects.md)
<a id="source-additional-outputs"></a> <a id="source-choosing-which-versions-to-render-for-each-clip"></a> <a id="source-defining-a-range-of-clips-and-versions-to-render"></a> <a id="source-how-to-avoid-overwriting-clips-when-rendering-output-media"></a> <a id="source-using-the-render-queue"></a>

### Additional Outputs

Every job you set up in the Render Settings starts out with one output. Even so, you can build several outputs whenever you have to deliver more than one version of media — each with its own video formats and codecs and distinct data burn-in settings — to render into separately named subfolders (optional).

The menu command that creates an extra output, displayed beside an output already present in panel 2 This comes in handy for arranging several rendered passes when a client wants two sets of media — say, QuickTime ProRes 422 (HQ) media together with MXF DNxHD media. It also helps when you have to put out two media sets, one carrying window burns and the other clean.

To add additional outputs in the Render Settings:

- Pick Create Additional Output off the Render Settings Option menu. Beneath the Filename and Location controls sits a row of numbers that opens each output you build so you can tune its settings. There's no cap on how many outputs you make.

To remove an additional output:

- Open the additional output panel you'd like gone, then click the Delete button along the bottom.

### How to Avoid Overwriting Clips When Rendering Output Media

The three options covered above — "Use unique filenames," "Place clips in separate folders," and "Use commercial workflow" — each give you a way to organize rendered media so rendered clips that share a file name don't overwrite each other. They're needed because every clip carries a single logical span of timecode, and because many clips frequently point back to one source media file bearing one name. As it renders a clip, DaVinci Resolve will overwrite any other media files carrying the same name automatically. So when you're aiming to hold onto the source media file's earlier filename, or putting out several versions of one clip, the clips you mean to output stand a real chance of clobbering one another, leaving only the last clip rendered. Those three options each head this off in their own way.

### Defining a Range of Clips and Versions to Render

With the Render Settings set, your next call is how much of the Timeline to render. A Mini-Timeline plus a Thumbnail timeline are on hand to help you move through your project's clips and settle on which to render. Track controls let you switch whole tracks in or out of the output; for instance, to render a textless version of a timeline where every title clip lives on track V4, just disable track V4. On top of that, these same controls let you decide which clip versions get rendered. To render the entire Timeline:

- Pick Entire Timeline off the Render dropdown in the Deliver page timeline. This choice surfaces only when clips aren't filtered.

To switch off a video or audio track so its clips stay out of the render:

- Click the Video or Audio Disable Track button on whichever tracks you mean to leave out.

To render only a filtered portion of the Timeline's clips: 1 Bring up the Color timeline if it isn't showing, then pick an option off the Timeline Filter dropdown sitting to the right of the Clips button in the Interface toolbar. The Thumbnail timeline then narrows to display only clips that fit the chosen criteria. Say you already rendered a session but have made changes since — you can reach for one of the "Show Modified Clips" options to surface just the clips altered within a certain stretch of time. Or pick the "Show Unrendered Clips" option to reveal every clip not yet rendered. 2 Pick "All Filtered Clips" off the Render dropdown in the Timeline toolbar.

To clear clip filtering:

- Pick All Clips off the Timeline Filter dropdown sitting to the right of the Clips button in the Interface toolbar.

To define a continuous range of clips to render: 1 To mark the first clip of the range you mean to render, take one of these steps:

- On a clip thumbnail within the Thumbnail timeline, right-click and choose Mark In.
- Park the playhead in the Timeline or the Viewer and tap the I key, or right-click the

Timeline ruler and choose Mark In. 2 To mark the last clip of the range you mean to render, take one of these steps:

- On a clip thumbnail (within the Color timeline) or a clip (within the Edit timeline) in the Thumbnail timeline, right-click and choose Mark Out.
- Park the playhead in the Timeline or the Viewer and tap the O key; alternatively right-click the Timeline ruler and choose Mark Out.

In and Out points show up within the Timeline ruler, and an orange bar marks out the range you've picked to render. The In and Out fields refresh with the first and last frame numbers, in timecode and frame count, while the Duration field refreshes with the total frame count you're about to render. IMPORTANT: When you're in Individual Clips mode, In and Out points snap by themselves to the nearest clip In or Out point on the Timeline. Partial clips can't be rendered in Individual Clips mode, though you can render them in Single Clip mode.

To render a single clip:

- Open the Thumbnail timeline if it's not up yet, right-click any clip thumbnail, and choose Render This Clip.
- An orange bar on the Timeline ruler signals that clip is queued for rendering. To render several clips one by one, pick each clip individually to add it as its own job to the Render Queue.

### Choosing Which Versions to Render for Each Clip

By default, whatever version is currently selected back on the Color page gets rendered per clip. To render a different one, the simplest move is making sure they're selected on the Color page Timeline before the Deliver page is opened. Still, a Versions submenu — sitting in the Thumbnail timeline's contextual menu for each thumbnail — also gives you options for managing grade versions. Those commands mirror what the Color page's Thumbnail timeline already offers. To pick the version that gets rendered:

- Right-click any clip thumbnail in the Thumbnail timeline, then pick a version off the Versions submenu.

TIP: From the Thumbnail timeline of the Color or Render screen you can right-click a clip and rename any version of a grade. That can smooth a facility's workflow when material moves between suites and applications.

### Using the Render Queue

After you've nailed down the settings needed to render the media you want, plus the slice of the current session to render, you add it all as a job to the Render Queue. Pile on as many jobs as you like, depending on which files you need to output. Each job can carry its own clip ranges and its own clip settings, covering different render directories, formats, resolutions, data levels, burn-in settings, and more. That means the Render Queue can line up renders of several sections of the current session, or several versions of the same media. You can even line up several sessions, if you've got a few differently graded ones. To add a job to the Render Queue: 1 Pick a timeline. 2 Dial in the settings you want over in the Render Settings, either through one of the Presets or by setting your own custom values. 3 Pick a range of clips to render via the Deliver page Timeline, following the steps laid out in the section above. 4 Click the Add to Render Queue button along the bottom of the Render Settings. 5 If no render location has been chosen yet, a File Destination dialog now prompts you for one, so pick a spot and click Ok. Should media already sit in the render location you named, a dialog may also warn you "This render may overwrite existing clips in this folder." To press on, click Yes; otherwise click No. That render setup now joins the Render Queue as a job, displaying the project and timeline name plus the location path the render will be written to.
