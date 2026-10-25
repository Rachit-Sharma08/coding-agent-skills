# Editing effects and transitions and the effects library

Version: DaVinci Resolve 20.3 Reference Manual. Context: Effects overview.
[Chapter index](INDEX.md) / [Next section](effects-inspector-controls-and-adding-filters-to-video-clips.md)
<a id="source-audio-fx"></a> <a id="source-converting-fusion-compositions-to-edit-effects"></a> <a id="source-editing-adding-and-copying-effects-and-filters"></a> <a id="source-editing-adding-and-copying-effects-and-filters-1"></a> <a id="source-editing-adding-and-copying-effects-and-filters-2"></a> <a id="source-editing-effects-and-transitions"></a> <a id="source-editing-effects-and-transitions-1"></a> <a id="source-effects-library-favorites"></a> <a id="source-inspector-effects-controls"></a> <a id="source-open-fx"></a> <a id="source-open-fx-1"></a> <a id="source-overview"></a> <a id="source-seeing-effects-in-the-timeline"></a> <a id="source-shift-space-to-display-the-effects-search-dialog"></a> <a id="source-the-toolbox"></a> <a id="source-using-the-effects-library"></a> <a id="source-using-the-inspector"></a>

## Overview

Covers: Editing Effects and Transitions; Editing, Adding, and Copying Effects and Filters.

## Editing Effects and Transitions

### Editing Effects and Transitions

## Editing, Adding, and Copying Effects and Filters

### Editing, Adding, and Copying Effects and Filters

Here you will learn the ways to locate and apply effects to Timeline clips,

duplicate them between clips, take them off again, and tweak their settings

through the Inspector after they have been placed.

To read up on which specific Resolve FX you have on hand, refer to “Resolve FX.”

### Using the Effects Library

Every effect available for your edit — filters, transitions, titles, and generators alike — lives within the Effects panel. That panel presents a tiered listing of each transition, title effect, generator, and filter on offer, grouped by category. If you want a preview of a video effect prior to dropping it onto a clip, first confirm that “Hover Scrub Preview” is enabled in the Effects option menu, and then glide your pointer over any thumbnail in the Effects tab, sliding it back and forth. That effect previews in the Viewer at its default parameters and scrubs through whichever clip is highlighted in the Timeline. Should nothing be selected, it falls back to the clip sitting beneath the playhead. Triggering a given video effect on a clip is as easy as dragging that effect’s thumbnail onto a Timeline clip. Alternatively, double click the thumbnail, or pull an effect straight into the Inspector, to apply it to the chosen clip. When you wish to fine-tune the effect’s parameters, bring up the Effects tab inside the Inspector.

Hovering across an Effect Thumbnail gives you a preview of that effect right in the Viewer. To hunt for a specific effect, click the magnifying glass icon sitting at the top of the Effects Library. The drop-down menu positioned just beside it lets you decide between searching the whole FX library (All Folders) or limiting the search to the current folder only. Category Names work as search terms when you are looking for effects and transitions. As an illustration, a search for “Stylize” surfaces every Resolve FX filed under the Stylize section. Searches can also be run using whatever language is set under DaVinci Resolve > Preferences > User > UI Settings, alongside English.

### Shift-Space to Display the Effects Search Dialog

Hitting Shift-Space now summons the Effects Search dialog across the Cut, Edit, Color and Fairlight pages, mirroring the behavior that the Fusion page always had. With a clip already selected, clicking an effect within the search list will apply it to that selected clip.

A press of Shift-Space brings up the Effects Search Dialog. Here, entering “film” surfaces every effect that has Film in its name.

### The Toolbox

This is where you find every video and audio transition, title, and generator bundled with DaVinci Resolve: Toolbox Surfaces all transitions, titles, generators, and effects together. Video Transitions: Holds each of the built-in transitions supplied by DaVinci, grouped by category. Near the foot of the list a User category surfaces whatever presets you have saved. Any video transition can be dragged onto any Timeline edit point with overlapping clip handles to fold it into your edit; you may drag the transition so it finishes on, sits centered on, or begins on the edit point. See Chapter 48, “Using Transitions,” for further detail. Audio Transitions: Holds audio transitions used to build crossfades. Titles: Titles edit into the Timeline the same way any other clip does. After a title is placed in the Timeline, its text and position can be changed straight in the Timeline Viewer, or you can reach its controls inside the Inspector for additional tailoring. Generators: Generators likewise edit into the Timeline just like any clip. Pick a generator and open the Inspector to reach its controls for additional tailoring. A default duration for generators can also be chosen within the Editing panel of the User Preferences. Effects: Effects act as placeholders in the Timeline that enable more specialized Fusion compositing, or that let you alter the tracks below by way of an adjustment clip.

### Open FX

Third-party Open FX filters, transitions, and generators are supported by DaVinci Resolve on the Edit page. After you install such effects on your workstation, they show up in this part of the Effects Library, grouped by type and group according to the metadata carried inside each effect.

### Open FX

Surfaces every Resolve FX and third-party Open FX present on your workstation together. Filters: Holds the Resolve FX filters bundled with DaVinci Resolve, plus whatever thirdparty OFX plugins you have installed on your workstation. Filters drag onto video clips to apply an effect to that clip. After application, filters can be tweaked and tailored by opening the Open FX panel of the Inspector. Generators: Holds whatever third-party OFX generators you have installed on your workstation. These edit into the Timeline exactly like the native generators shipped with DaVinci Resolve, yet they additionally surface an Open FX panel beside the Transition panel in the Inspector, letting you tailor settings that belong only to that transition. Transitions: Holds whatever third-party OFX transitions you have installed on your workstation. OFX transitions behave much like any other transition, yet they also surface an Open FX panel beside the Transition panel in the Inspector, where settings unique to that transition can be tailored.

### Audio FX

Across every platform, DaVinci Resolve ships a collection of built-in Fairlight FX, a native audio plugin format that puts assorted audio tools and effects within reach on macOS, Windows, and Linux. Under macOS and Windows, DaVinci Resolve handles third-party VST audio plugins, covering most of the professional third-party tools and effects relied upon throughout the audio postproduction field. Under macOS, DaVinci Resolve handles Audio Unit (AU) audio plugins. After you install these effects on your workstation, they show up in this panel of the Effects Library. Audio plugins let you put effects onto audio clips or whole tracks of audio, whether to add creative texture such as echo or reverb, or to fix mastering problems through noise reduction, compression, or EQ.

### Effects Library Favorites

Clicking the far right of any transition, title, or generator lets you flag that effect with a star as a favorite effect. Once you do, the favorited effects collect in their own Favorites zone at the foot of the Effects Library Bin list. Favorited effects are sorted into categories automatically within the list.

Stars mark a flagged favorite effect; every favorite is filtered and sorted into categories automatically.

### Converting Fusion Compositions to Edit Effects

Should you have built a Fusion Composition you would like to reuse across several projects, it can now be saved to the Effects toolbox on the Edit page. That way the effect stays within easy reach on the Edit page, and drops readily onto Timeline video clips. Turning a Fusion composition into an Edit effect goes like so: 1 In Fusion, output the composition as a macro by right clicking a node and picking Create Macro out of the contextual menu. 2 Store the macro file (.setting) under the directory matching your platform — MacOS: `/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/ Templates/Edit/Effects` Windows: `C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Templates\Edit\Effects` Linux: `/opt/resolve/Fusion/Templates/Edit/Effects` From then on the effect appears, ready to drag and drop, within the toolbox’s “Fusion Effects” section inside the Effects Library on the Edit page.

### Seeing Effects in the Timeline

Whenever you put any sort of effect on a Timeline clip — be it an Inspector adjustment, a speed effect, a plugin you have applied, and so on — clips carrying that effect take on a darker shade of whatever color they already are, signaling that an effect is present. Stripping all effects off a clip (for instance, with the Remove Attributes command) restores that clip to its original color. This lets you tell at a glance which clips carry effects and which do not.

An effect-bearing clip, darkened in shade, sitting between a pair of normally-shaded clips that carry no effects

### Using the Inspector

After effects are placed on a timeline, the Effects Inspector is the spot for editing their parameters. The Inspector serves as the hub for adjusting every setting tied to filters, compositing, sizing, titling, transitions, generators, and effects of all sorts.

Which parameters the Inspector shows hinges on your Timeline selection; (left) a clip’s parameters, (right) a title’s parameters.

A great many of the procedures in this section depend on the Inspector, which opens or closes when you click the Inspector button sitting at the far right end of the Edit and Cut page toolbars, or when you doubleclick a transition or generator within the Timeline. There are three ways the parameters of Timeline clips end up shown in the Inspector:

- When no clips are selected in the Timeline, the clip sitting in the topmost auto-select-enabled track that crosses the playhead has its parameters presented in the Inspector.
- The Inspector always presents the parameters of one or more items selected in the Timeline, which takes precedence over the clip in the highest track that crosses the playhead, when needed. Altering the selection alters which parameters appear, and any parameters you edit in the Inspector affect only the currently selected clip. With several clips selected, the Inspector shows “Multiple Clips” and lets you tune the parameters of every selected clip together.
- Picking Timeline > Selection Follows Playhead tells DaVinci Resolve to keep selecting whichever clip crosses the playhead in the Timeline. Consequently the Inspector keeps showing the parameters of whichever clip sits at the playhead, and as an added benefit that same clip becomes selected for your other editing operations too. When several stacked clips cross the playhead simultaneously, the uppermost video clip whose Auto Select control is enabled gets selected, surfacing its parameters in the Inspector, while every other clip is disregarded.

### Inspector Effects Controls

Different Effects clips in the Timeline expose different controls. Whatever panels are surfaced, the parameters inside each panel are sorted into groups, each carrying a title bar that names the group, alongside additional controls letting you govern every parameter inside that group together.
