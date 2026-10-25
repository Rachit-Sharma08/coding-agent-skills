# More about timelines and grading and timelines grades and versions

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the edit page.
[Chapter index](INDEX.md) / [Previous section](edit-page-user-interface-and-edit-page-in-its-entirety.md) / [Next section](edit-index-columns-overview.md)
<a id="source-audio-fx"></a> <a id="source-creating-a-master-timeline"></a> <a id="source-edit-index"></a> <a id="source-edit-index-list-shown-open"></a> <a id="source-effects-library-favorites"></a> <a id="source-enabling-the-use-of-a-master-timeline"></a> <a id="source-index"></a> <a id="source-more-about-timelines-and-grading"></a> <a id="source-navigating-the-timeline-using-the-edit-index"></a> <a id="source-openfx"></a> <a id="source-the-effects-library"></a> <a id="source-the-toolbox"></a> <a id="source-timelines-grades-and-versions"></a> <a id="source-using-the-effects-library"></a>

### More About Timelines and Grading

A DaVinci Resolve project holds one or more edited timelines (other applications sometimes call these a sequence), which are organized in the Media Pool as well and presented in the Timeline Editor (known as “the Timeline”). Timelines are made of clips whose source media lives in the Media Pool, and those clips also turn up as edit events in the Edit Index that you can surface at the right of the Timeline.

### Timelines, Grades, and Versions

Inside any given timeline, grades are tied to the timecode of the source clip they sit on. So as you reshape the timeline, each clip’s grade travels with it, which makes shuttling between editing and grading as your needs dictate remarkably easy. By default, every timeline in a project keeps its own independent grades through local versions; that holds even when your timelines are duplicates. In other words, each clip in every timeline carries a wholly independent grade. Switch the clips in one or more timelines over to Remote versions, though, and a clip’s grades become shared by every instance of that clip across all timelines whose clips likewise use Remote versions. Import a new timeline that reshuffles clips into a different order and set it to Remote versions, and grades follow the clips automatically, so the clips in each new timeline inherit the grades applied to those same clips in other timelines. You can flip a timeline between Local and Remote grades whenever you wish. To learn more about Local versus Remote versions, turn to Chapter 142, “Grade Management.” You can also carry grades from one timeline to another with the ColorTrace feature. For more on ColorTrace, turn to Chapter 149, “Copying and Importing Grades Using ColorTrace.”

### Enabling the Use of a Master Timeline

Earlier releases of DaVinci Resolve carried a Master Timeline — one long timeline holding every clip in the Media Pool, arranged by default in ascending timecode order. The Master Timeline served a range of tasks, but architectural improvements have made it unnecessary, so by default it doesn’t show up in new projects created under DaVinci Resolve version 10 or later. Even so, if you want a Master Timeline to keep a single timeline that always contains every clip currently in the Media Pool, there’s a way to create one. You have to do it the instant you create a new project, before any media goes into the Media Pool. Once one or more clips land in the Media Pool, the option you need turns disabled. To build a fresh Master Timeline: 1 Start a new project; open the General Options panel within the Project Settings; then switch on the “Automatically match master timeline with media pool” checkbox. If you’d also like all clips to default to Remote versions as you grade, the way earlier DaVinci Resolve releases did, switch off the “Use local version for new clips in timeline.”

The option to use a Master Timeline lives in the Color section, itself part of the General Options panel within the Project Settings. 2 Click Save to dismiss the Project Settings window. 3 Head to the Edit page and choose File > New Timeline (Command-N). 4 As the New Timeline Properties window comes up, switch the Empty Timeline checkbox off, then click Create New Timeline. Now, alongside the new timeline, a Master Timeline shows up in the Timeline list. TIP: To guarantee you always get a Master Timeline whenever you create new projects, you can edit the Project Setting preset for your user account to carry these settings, or build a fresh Project Setting preset with these settings that you can switch to with ease.

The Master Timeline is one long sequence gathering every clip in the Media Pool, laid out in ascending timecode order. Each clip in the Master Timeline shows at its full duration, no matter the duration of the matching clips in an EDL-, AAF-, or XML-imported timeline. Any time you add more clips to the Media Pool, they join the Master Timeline automatically.

### Creating a Master Timeline

The Master Timeline comes in handy for organizing media that hasn’t been edited yet, as when you’re grading digital dailies. It’s also handy for picking out a band of similar clips by their similar timecode ranges. You might, for instance, find all the talking head shots from one section of tape gathered together within the Master Timeline.

### Using the Effects Library

Every effect you can drop into your edit — filters, transitions, titles, and generators included — lives in the Effects Library, which breaks into two parts. On the left sits a bin list presenting a hierarchical list of all the available Transitions, Title Effects, Generators, and Filters, grouped by category. On the right is a browsing area where you see the contents of whichever bins are selected. As with the Media Pool, a button at the top left opens or closes the Effects Library’s bin list, while a menu just right of that button sorts the list into different categories.

### The Effects Library

### The Toolbox

All the video and audio transitions, titles, and generators bundled with DaVinci Resolve show up in the Effects Library’s Toolbox category. Toolbox: Surfaces all Transitions, Titles, Generators, and Effects at once. Video Transitions: Holds every built-in transition DaVinci Resolve offers. You can drag any video transition onto any Timeline edit point that has overlapping clip handles to add it to your edit; you’re free to drop the transition so it ends on, centers on, or starts on the edit point. For more, turn to Chapter 48, “Using Transitions.” Audio Transitions: Holds audio transitions for building crossfades. Titles: Titles edit into the Timeline like any other clip. With one in the Timeline, you can edit its title text and position straight in the Timeline Viewer, or reach its controls in the Inspector for further customization. Generators: A generator, too, edits into the Timeline just as any other clip would. Select a generator, then open the Inspector, and its controls become available for further customization. You can also set a standard duration that generators appear with in the Editing panel of the User Preferences. Effects: Holds distinctive placeholder effects such as Adjustment Clip and Fusion Composition, which can be customized to apply sophisticated effects to your programs.

### OpenFX

On the Edit page, DaVinci Resolve supports third-party OpenFX filters, transitions, and generators. Once you install these effects on your workstation, they show up in this section of the Effects Library, sorted by type and group according to the metadata inside each effect. OpenFX: Brings up, all at once, every Resolve FX along with the third-party OpenFX sitting on your workstation. Filters: Holds the Resolve FX filters bundled with DaVinci Resolve, plus any third-party OFX plugins you’ve installed on your workstation. Drag a filter onto a video clip to apply its effect to that clip. With one applied, you can edit and customize the filter by opening the OpenFX panel of the Inspector. Transitions: Holds any third-party OFX transitions installed on your workstation. OFX transitions work much like any other transition, but they additionally surface an OpenFX panel beside the Transition panel in the Inspector, where you tailor settings unique to that transition. Generators: Holds any third-party OFX generators installed on your workstation. These edit into the Timeline just like the native generators bundled with DaVinci Resolve, but they additionally surface an OpenFX panel beside the Transition panel in the Inspector, where you tailor settings unique to that transition.

### Audio FX

Across every platform, DaVinci Resolve supports Fairlight FX, the built-in audio plugins that ship with DaVinci Resolve. Beyond those, DaVinci Resolve supports third-party VST audio plugins under macOS as well as Windows, and Audio Unit (AU) audio plugins under macOS. Install these effects on your workstation and they show up in this panel within the Effects Library. With audio plugins you can apply effects to single audio clips, or to a whole track’s worth of audio, lending creative qualities like echo or reverb, or sorting out mastering issues through noise reduction, compression, or EQ.

### Effects Library Favorites

Clicking the far right of any transition, title, or generator marks that effect with a star as a favorite. Once you do, the favorited effects collect in a separate Favorites area down at the bottom of the Effects Library Bin list.

Stars mark a flagged favorite effect; here all favorites are filtered.

### Index

The index lays out information about your timeline in a stripped-down spreadsheet format, serving both as a reference and as a means of timeline navigation. It splits across the Edit Index, Tracks, and Markers tabs.

### Edit Index

Clicking the Edit Index button brings up the Edit Index. By default it presents an EDL-style list view of every edit event in the current timeline. Whichever timeline is selected in the Timeline list shows its events here. That said, you can filter the Edit Index’s contents through commands in the Option drop-down, covered later in this section. Each clip and transition appears as its own event, every one carrying several columns of information. Re-edit a timeline and your changes turn up in this list too. The Edit Index helps creative editors hunting for particular effects used in the current timeline, as well as finishing editors who need more information about a specific clip, or who may have to filter the whole edit by particular criteria to troubleshoot assorted issues.

### Edit Index List shown open

### Navigating the Timeline Using the Edit Index

Any time you move the Timeline playhead across a clip, the Edit Index refreshes to show only the clips on the video track that clip sits on, and that clip’s event gets highlighted in the Edit Index. This makes the link between a Timeline clip and its event easy to read, which helps when you’re troubleshooting problems. The Option menu additionally holds commands that narrow the view down to clips on enabled tracks alone, to video clips alone, or to audio clips alone.
