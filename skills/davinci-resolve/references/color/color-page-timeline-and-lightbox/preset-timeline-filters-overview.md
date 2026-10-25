# Preset timeline filters overview

Version: DaVinci Resolve 20.3 Reference Manual. Context: Color page timeline and lightbox.
[Chapter index](INDEX.md) / [Previous section](project-options-flags-clip-colors-and-markers.md) / [Next section](creating-and-using-smart-filters.md)
<a id="source-preset-timeline-filters"></a>

### Preset Timeline Filters

DaVinci Resolve ships with a handful of preset rules for filtering the Timeline, spanning many of the usual organizational workflows:

- All Clips: Nothing gets filtered out, so each clip of the present edit appears.
- Selected Clips: Filters all currently selected clips.
- Graded Clips: Filters all clips that have been graded.
- Clips with Fusion Composition: Clips with Fusion page effects applied to them.
- Ungraded clips: Filters all clips that have not yet been graded.
- Modified clips: Submenu, filters every clip altered inside a given time window.
- Unrendered clips: Filters all clips that have not yet been rendered.
- Clip Color: Filters every clip carrying any color, none at all, or one specific color assigned within the Timeline;

a submenu presents each color.

- Flagged Clips: Filters every clip bearing any flag, none, or one specific flag; a submenu

presents each color.

- Marked Clips: Filters every clip holding any marker, none, or one specific marker; a submenu

presents each color.

- Keywords: Filters every clip to which a given keyword is assigned. A submenu lays out a list holding

each keyword in use across the present project's Media Pool.

- People: Filters every clip tagged with a given person via the People Management

Window. A submenu automatically lays out a roster of each person who's been identified.

- Stereoscopic: Filters stereo 3D clips; via a submenu you can narrow to All Stereo Clips, or

restrict to Stereo clips that were Autoaligned, ones carrying Convergence adjustments, ones with Floating Windows adjustments, or stereoscopic clips whose left- and right-eye media has been swapped.

- Grouped: Filters every clip that sits inside a given group; a submenu lists each group on offer.
- Tracked: Filters all clips with motion tracking.
- Noise Reduction: Filters all clips using noise reduction.
- OpenFX: Filters all clips using OpenFX.
- Different Frame Rate: Filters every clip whose frame rate differs from the project's own.
- Edit Sizing: Filters every clip on which some Edit Sizing parameter was changed.
- Input Sizing: Filters every clip on which some Input Sizing parameter was changed.
- Common Media Pool Source: Filters every clip that draws on the same Media Pool source as the present clip does.
- Matte Nodes: Filters every clip that carries an exposed Matte node inside the Node Editor.
- Mattes Available: Filters every clip with a matte attached, regardless of whether it's actually in use.
- Collaborative Update Available: (Only available in Collaborative Mode) Filters every clip marked as having received an update over the course of a collaborative workflow.
