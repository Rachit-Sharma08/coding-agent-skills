# Editing and removing transitions and setting the default transition

Version: DaVinci Resolve 20.3 Reference Manual. Context: Video and audio effects in the cut page.
[Chapter index](INDEX.md) / [Previous section](adding-transitions-and-cut-dissolve-and-smooth-cut-buttons.md) / [Next section](audio-effects-and-generators.md)
<a id="source-adding-resolve-fx-and-other-plugins"></a> <a id="source-adding-titles"></a> <a id="source-changing-the-default-transition"></a> <a id="source-editing-and-removing-transitions"></a> <a id="source-editing-text"></a> <a id="source-editing-titles"></a> <a id="source-positioning-and-transforming-text"></a> <a id="source-setting-the-default-transition"></a> <a id="source-the-title-settinµgs-of-video-inspector"></a> <a id="source-titles"></a> <a id="source-titles-thumbnails"></a> <a id="source-transforming-a-titles-text-box-in-the-viewer"></a> <a id="source-video-effects"></a>

### Editing and Removing Transitions

After a transition is in place, you can edit it in a range of ways to suit your program best, whether from the Timeline itself or by way of the Transition Inspector. Methods of editing transitions in the Timeline:

To change a transition's duration: Drag the start or end of a transition in the Timeline so it grows or shrinks symmetrically around the current edit.

To move a transition from one edit to another: A transition can be dragged from where it currently sits onto another edit point.

To copy a transition from one edit to another: Pick a transition, then option-drag it onto another edit point to drop in a duplicate transition.

To change a transition's type: Drag a different transition out of the Transition Browser onto the current one in the Timeline.

To remove a transition: Pick a transition in the Timeline and press the Delete key.

To remove all transitions in a timeline: Click the Timeline Actions menu and pick Clear Transition from All Edits.

Editing transitions in the Transition Contextual menu: A transition's parameters can be edited right in the Timeline, by right-clicking the transition and picking one of the options off the contextual menu.

A right-click on a transition over in the Timeline surfaces the editing options above. Change Transition Type: Switch to any other installed transition by picking one out of the drop-down menu. Change Duration: Set the transition's duration, shown in both seconds and frames. Set as Default Transition: Makes the currently selected transition the Default Transition.

Alignment Options: Lets you set where the transition falls relative to the edit point it's on. The three on offer read "Start on Edit," "Center on Edit," along with "End on Edit." Cut/Copy/Paste: The standard cut, copy, and paste controls used when editing transitions in the timeline. Editing transitions in the Transition Inspector: For finer control over your transition, right down to every transition-specific parameter, lean on the Transition Inspector. To read more on each specific transition that ships with DaVinci Resolve, see Chapter 30, "Using the Inspector in the Cut Page."

### Setting the Default Transition

Out of the box, the default transition is a plain cross dissolve. Should you want to make some other transition the default, just right-click a transition thumbnail and pick Set as Standard Transition off the contextual menu.

Beyond the Default Transition type, you can also set its duration and alignment, either from the Timeline Options menu or by right-clicking the transition in the Timeline and picking "Set Default Transition."

### Changing the Default Transition

### Titles

The Titles Browser holds a collection of title clips you can draw on to add superimposed titles, slates, interstitial titles, lower thirds, or otherwise meet whatever textual needs your program carries.

### Titles Thumbnails

To audition titles ahead of dropping them into the Timeline, make sure "Hover Scrub Preview" is ticked in the Titles option menu, then just rest your pointer on any thumbnail in the Titles tab. Where the title is animated (i.e., Fusion titles), sliding the pointer across the thumbnail previews the animation. Once you've settled on your title, you can drag it from the Titles tab onto your Timeline on the Edit page or on the Cut page—either the upper or the lower Timelines—or instead rely on the editing selection modes along the bottom of the tab.

A scrub over a Title Thumbnail previews that title in the Viewer. The two categories hold two different kinds of titles. The "Titles" category holds simple, bare-bones titles you can customize in all sorts of ways. Among the choices, the Text title is the most flexible. The "Fusion Titles" category holds more elaborate titles that are visually richer and carry more preset animation.

### Adding Titles

A title goes onto the Timeline when you open the Titles Browser and drag and drop titles into the Timeline wherever you'd like them, just as you would any other clip. A title clip lasts 5 seconds by default. This standard "generator" duration is adjustable over in the User Preferences' Editing panel. After being edited onto the Timeline, titles move, resize, and superimpose much as any other clip would. Beyond that, once selected, titles and generators alike surface the very same Transform, Cropping, Speed, and Composite controls any other clip carries; those controls let you composite titles in various ways to build different text effects.

### Editing Titles

After a title is on the Timeline, the original title generators that came with DaVinci Resolve carry onscreen controls letting you edit text and transform and position blocks of text right inside the Timeline Viewer.

### Positioning and Transforming Text

As long as the Timeline playhead sits over a text generator that's atop one or more background clips, clicking the text in the Timeline Viewer surfaces onscreen transform controls matching the Position, Zoom, and Rotation parameters in the Inspector.

### Transforming a title's text box in the Viewer

As you drag text to reposition it, snapping kicks in at the X and Y center of the frame, as well as

around the frame's outer third. As you drag a text object, holding the Shift key down restricts

its travel to the X or Y axes alone. Holding the Option key down switches snapping off.

### Editing Text

A double-click on text within the Timeline Viewer makes that text editable, so you can drop in a text cursor or select characters and edit just as you would inside any text editor.

Editing a title's text in the Viewer Editing Titles Using the Video Inspector For tighter control over your titles, double-clicking any title surfaces its parameters in the Video Inspector. There you can switch fonts, colors, drop shadows, backgrounds, and so on. Basic transform parameters and cropping are adjustable there too. To read more about Editing Titles, see Chapter 49, "Titles, Generators, and Stills."

### The Title settinµgs of Video Inspector

### Adding Resolve FX and Other Plugins

The Effects Browser surfaces video and audio plugins you can drag and drop onto your clips. On the video side, several categories of Resolve FX plugins ship with DaVinci Resolve, but should you have installed Resolve-compatible OFX plugins, those turn up here too, sorted into their own categories. On the audio side, a set of Fairlight FX plugins comes with DaVinci Resolve, but should you have installed VST plugins on macOS or Windows, or have Audio Units installed on macOS, those appear in the Audio category as well. When your video or audio plugins pile up, a search field makes the one you're after easy to track down.

### Video Effects

Each available category of video plugins builds a different sort of image effect—blurs, lighting effects, or stylization of various kinds. To preview a video effect ahead of placing it on a clip, make sure "Hover Scrub Preview" is ticked in the Effects option menu, then just rest your pointer on any thumbnail in the Effects tab and slide it across the thumbnail. The effect previews in the Viewer with its default parameters, scrubbing through whichever clip is selected in the Timeline. Where no clip is selected, it falls back on the clip currently under the playhead. To turn on a particular video effect for a clip, just drag the chosen effect's thumbnail onto a clip in the Timeline. On the Cut page, double-clicking the thumbnail will likewise put the effect onto the selected clip. To tune the effect's parameters, open the Effects tab in the Inspector.

Scrubbing over an Effect Thumbnail previews that effect in the Viewer.
