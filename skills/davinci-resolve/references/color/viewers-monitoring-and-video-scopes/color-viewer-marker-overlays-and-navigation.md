# Marker overlays and navigation and timeline marker list available in color page viewer option menu

Version: DaVinci Resolve 20.3 Reference Manual. Context: Viewers monitoring and video scopes.
[Chapter index](INDEX.md) / [Previous section](viewer-reference-wipes-and-timeline-clips.md) / [Next section](video-scope-types-and-qualifier-focus.md)
<a id="source-changing-vectorscope-scales"></a> <a id="source-changing-waveform-scales"></a> <a id="source-displaying-scopes-with-data-or-video-levels"></a> <a id="source-marker-overlays-and-navigation"></a> <a id="source-the-parade-scope-showing-the-data-range-scale"></a> <a id="source-the-parade-scope-showing-the-hdr-nit-scale"></a> <a id="source-timeline-marker-list-available-in-color-page-viewer-option-menu"></a> <a id="source-using-video-scopes"></a> <a id="source-vectorscope-scale-options"></a> <a id="source-video-scope-location"></a> <a id="source-video-scope-measurement-using-scales"></a> <a id="source-video-scope-performance-and-detail"></a> <a id="source-waveform-scale-options"></a>

### Marker Overlays and Navigation

Should you rest the playhead directly over a marker within the Timeline of the Color page, that marker's details surface in a Viewer overlay, exactly as they do on the Edit page, which makes reading notes and spotting the available information simpler. Hiding these overlays is straightforward: click the Viewer option menu and switch "Show marker overlays" off.

### Timeline Marker List Available in Color Page Viewer Option Menu

A submenu within the option menu of the Color page Viewer enumerates every Timeline Marker present in the timeline you've got open. This makes working through client notes a breeze.

A quick-access list of Timeline markers reachable from the option menu of the Viewer

### Using Video Scopes

Though they aren't bound directly to how the Viewers are used, video scopes still operate side by side with them to assist you in assessing the pictures you're handling. A collection of five real-time video scopes ships with DaVinci Resolve, which you can lean on to keep an eye on the internal data levels of the clips throughout your project as you work. Every scope delivers a clear graphical breakdown of distinct traits of the video signal, presenting the relative strength and span of separate color components — luma, chroma, saturation, hue, gamut, white point, plus the red, green, and blue channels that jointly make up the color and contrast of the pictures in your program.

### Video Scope Location

Out of the box, you can display any single one of these scopes at a moment in the lower right corner of the Color page, by clicking the Video Scope button found in the palette button bar.

The video scope, parked alongside the remaining palettes down at the foot of the Color page

If you prefer, clicking the Expand button at the upper right of the video scope opens the video scopes into a floating window, where you're able to show all four video scopes together, or one at a time, on whichever monitor is hooked up to your workstation.

Video scopes in a floating window in HDR (ST.2084/HLG) mode On top of that, the video scopes can sit docked on a secondary display within many of the dual-screen layouts DaVinci Resolve offers. That said, with three computer displays and dual screen layouts active, you've still got the choice of opening the floating Scopes window and dropping it onto your third display, sized however big you want. The video scopes don't live solely in the Color page. You'll find them in the Media and Deliver pages too, for any moment you have to assess the video signal more impartially, like while preparing to capture from tape or scan from film, or while readying things for output. To bring up video scopes from the Media, Color, or Deliver pages, do one of these: Choose Workspace > Video Scopes > On/Off (Command-Shift-W), which floats them out; or floatingwrkspace > Dual Screen > On, which folds them into a dual screen layout instead.

### Video Scope Measurement Using Scales

Since what you're assessing is the internal condition of the image data, the numeric scales of the WFM and Parade scopes by default always show 10-bit full range data spanning 0–1023, no matter which Video/ Data Level setting you've picked within the Master Settings panel of the Project Settings. That hands you a view into the way the image gets processed by DaVinci Resolve ahead of being sent out through your computer's video I/O interface. While you're grading in HDR (High Dynamic Range), you can pick HDR (ST.2084/HLG) out of the Video Scopes option menu (this capability exists in the Studio version alone). Doing so swaps the 10-bit scale of the Waveform, Parade, and Histogram video scopes for a scale built on nit values (or cd/m2) in its place.

### The Parade scope showing the data range scale

### The Parade scope showing the HDR "nit" scale

### Changing Waveform Scales

A Waveform Scale Style submenu inside the Video Scopes option menu (the three dots menu) lets you decide how the numeric scale sitting at the left of Waveform and Parade scopes gets represented. The choices on offer begin with 10-bit display (the default), then 12-bit display, followed by Percentage (0 to 100), then millivolt (mV), and lastly HDR (ST.2084/HLG). Beyond the extra flexibility this affords you, it also means there's no longer any need to head into the Preferences to make the scope show an HDR scale in nits (cd/m2).

### Waveform scale options

IMPORTANT: When you're working in a workflow that isn't DaVinci Resolve Color managed and you switch on the HDR (ST.2084/HLG) scopes, the waveform will reflect HDR levels at all times, even where you've hand-picked the output color space as Rec.709, so it won't be 100% accurate.

### Changing Vectorscope Scales

A Vectorscope Scale Style submenu inside the Video Scopes option menu (the three dots menu) lets you decide how the hue reference indicators get shown.

### Vectorscope scale options

Four graticule options exist: Off: Switches off every graticule overlay within the Vectorscope, handing you a clean look at the Vectorscope graph set against black. Standard: The default arrangement. Cross hairs mark the scope's center, while boxes pinpoint, for every primary and secondary hue, its center target (red, magenta, blue, cyan, green, yellow). A surrounding circle supplies a broad reference for the angle along which any portion of the graph might land. Simplified: Presents a crosshairs marking the scope's center plus smaller crosshairs marking each primary and secondary hue. Handy whenever you want references stripped of extra clutter. Hue Vectors: A graticule crafted to give colorists a more practical reference for creative calls and image comparison. There's nothing merely ornamental about it. For every primary and secondary hue, graticule lines trace its reference angle, running from the hue targets inward to the center, furnishing a more instantly practical reference while you weigh one vector scope graph against another. Within the zone of average saturation in most pictures, these reference lines fade away, so they don't obstruct your read of faint detail. The center crosshairs sit along the red‑cyan and yellow-blue axes, marking the natural warm-to-cool axis running between them. Tic marks flag both the 75% and 100% levels of image saturation per hue. You're also free to decide whether the primary and secondary hue targets appear for 75% image saturation, 100% image saturation, or both, and whether the text labels for each hue get shown.

### Displaying Scopes With Data or Video Levels

When a project is being graded at video levels, a setting within the Video Scope option menu's Waveform Scale Style submenu lets you flip the video scope scaling between Data Levels (the default) on one hand and Video Levels on the other (which you reach by switching on Video Level Scopes). This governs nothing but how your scopes appear; monitored or rendered output stays untouched.

The Waveform scope shown at default Data Levels,

The same waveform shown with Video Level Scopes turned on

### Video Scope Performance and Detail

Within DaVinci Resolve 16 every video scope was overhauled to render more detail at faster speeds than earlier releases managed. Although they're GPU-accelerated, the video scopes still draw on a measure of video processing muscle to run. Based on whichever mix of video scopes and scope options you've turned on, your real time processing headroom may dip ever so slightly. Shutting the video scopes returns all that processing to color correction and effects. On heavy-duty workstations you'll likely spot no change, yet on weaker machines, closing the scopes could yield a modest gain. A pair of global settings within the Video Scope option menu shape the performance and detail of every video scope alike.

- On slower workstations, a quality submenu lets you pick High, Medium, or Low quality scope drawing, trading legibility against performance. High quality reveals the fullest detail about the video signal, whereas an Auto option chooses on the basis of what your workstation can handle.

The Quality setting in the Video Scope option menu

- Every video scope carries a Low Pass Filter setting within the Video Scope option menu that strips a signal's noise so the scope graphs read more cleanly. Though this can serve as an "x-ray" for spotting detail inside the scope graph interiors, it can leave the highlight and shadow excursions on the graph looking slightly shy of their real positions, so enabling the "Extents" option of whatever scope you're on is advised, giving you a clear read of the peak excursions across your scopes. Extents draws an outline marking every graph excursion to reveal the genuine level of all overshoots and undershoots within the video signal, even with the Low Pass Filter switched on.

The Waveform scope with Low Pass Filter turned off

The Waveform scope with Low Pass Filter turned on
