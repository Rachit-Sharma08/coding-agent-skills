# Identifying the input color space of different clips

Version: DaVinci Resolve 20.3 Reference Manual. Context: Data levels color management and ACES.
[Chapter index](INDEX.md) / [Previous section](rcm-image-processing-pipeline-extracted-diagram-labels.md) / [Next section](camera-raw-formats-and-source-media-color-space-metadata.md)
<a id="source-identifying-the-input-color-space-of-different-clips"></a>

### Identifying the Input Color Space of Different Clips

At the heart of automated color management lies knowing the color space and transfer function carried by every clip of source media in your project. DaVinci Resolve has several ways to work this out, following a cascading decision-tree you can override by hand where needed. Working out the Input Color Space ran through these stages of automated decision making: 1 When the source media is a camera raw format such as .braw, .R3D, .ari, etc., DaVinci Resolve leans on manufacturer-supplied colorimetry to debayer the clip automatically and pin down its Input Color Space. 2 Failing that, when the source media carries embedded color space metadata (something QuickTime or .MXF allow), that metadata is used to pin down the Input Color Space. 3 Failing that, when no embedded color space metadata exists, the default Input Color Space setting in the Project Settings is applied to give an Input Color Space to every clip not otherwise identified. 4 Where needed, you may set the Input Color Space of clips in the Media Pool by hand, which overrides either embedded color space metadata (should it be wrong) or the default Input Color Space setting (when you are juggling multiple color spaces). The Input Color Space of camera raw media cannot be overridden.

Each of these steps is taken up in finer detail across the sections that follow.
