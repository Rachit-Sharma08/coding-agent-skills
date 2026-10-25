# Color and multimaster trim manager

Version: DaVinci Resolve 21 New Features Guide. Context: Color and keyframing.
[Chapter index](INDEX.md) / [Previous section](media-and-media-pool-tabbed-layouts.md) / [Next section](aces-amf-and-dolby-hdr-analysis-reset.md)
<a id="source-clip-groups-support-grade-versioning"></a> <a id="source-color"></a> <a id="source-color-1"></a> <a id="source-customizable-hdr-and-nit-scopes-ranges"></a> <a id="source-film-look-creator-adds-aurora-preset-and-fade-rolloff-controls"></a> <a id="source-hdr-vivid-improvements"></a> <a id="source-multimaster-trim-manager"></a> <a id="source-node-graphs-can-be-viewed-as-a-layer-list"></a> <a id="source-node-stacks-support-up-to-eight-layers"></a> <a id="source-render-ai-magic-mask-2-as-an-external-matte"></a> <a id="source-shared-node-support-for-stereoscopic-3d-clips"></a> <a id="source-the-enable-trim-on-selector"></a> <a id="source-the-multimaster-trim-manager"></a> <a id="source-the-new-aurora-core-look-applied"></a> <a id="source-the-node-graph-in-node-view"></a> <a id="source-the-original-footage"></a>

## Color

### Color

### MultiMaster Trim Manager

In DaVinci Resolve 21, the new MultiMaster Trim Manager streamlines how you handle HDR grade trims. The tool lets you steer several grade trims from one timeline. Your timeline's hero grade is the main node graph — Pre and Post Group plus node stack layers included — while each extra trim layer is a grade laid over that hero grade for a specific deliverable. So you might grade your master 4000 nit HDR timeline and, at the same time, set up and oversee trims for HDR 1000 and SDR Rec.709 output. Turn the MultiMaster Trim Manager on through Color > MultiMaster Trim Manager, which opens the window pictured below; to begin, flip the trim passes switch at the window's top left.

### The MultiMaster Trim Manager

From this window you can build and oversee as many trims as your timeline calls for. Use the relevant button to add or drop a trim. Rename one by clicking its name in the list and typing a replacement. You can also give each trim its own monitoring, output, and color management output color space settings.

Out of the box every trim switches on these node graphs: After Clip, then Before Group, plus After Group, alongside Before Timeline, and finally an After Timeline node graph. Any of those node graph elements can be toggled on or off through the 3-dot option menu of the Trim Manager window.

### The Enable Trim On Selector

Switch which trim is active through the 3-dot option menu in the Color page node graph. The chosen trim's name shows at the top of the node graph so you can see at a glance which trim is live.

Select Trim Pass in the Node Graph option menu You can also dial blanking per trim — at either a clip or timeline level — within the Output Sizing palette. For that, tick the Use Trim blanking checkbox so the blanking is set at the trim level. Bear in mind this works separately from the node stack layers you turn on for the main clip grade. Lastly, when output time arrives in the Deliver page, you can pick the exact Trim Pass grade to render for each output under video settings.

Within the Deliver page Video Render settings, choose the Trim Pass you want to output.

### Render AI Magic Mask 2 as an External Matte

A Magic Mask can now be rendered out as its own matte node. The rendered magic mask frames are then available externally to serve as an alpha source across all sorts of effects and uses. The external matte node produced by rendering the Magic Mask — to make it, pick Render in Place Magic Mask out of the 3-dot option menu and then choose where the cached frames should be rendered.

To build the external matte, choose Render in Place Magic Mask from the option menu

### Clip Groups Support Grade Versioning

Grade versioning now extends to clip groups, not just single clips. Versioning a clip group lets you build and juggle several looks shared across every common clip in that group. With node stack layers you can now keep multiple versions of your Pre-Clip and Post-Clip node graphs too. Members of a group can't hold differing group versions — choosing a version for the group sweeps across all of its clips. Create or change versions by right-clicking a grouped clip in the timeline and working through Groups and its submenus.

Making a fresh Clip Group version via the context menu of a clip on the Color page timeline

### Node Graphs can be Viewed as a Layer List

A fresh Layer List view now lives in the node graph, reached by clicking its icon at the node graph's upper left. The mode lays every one of your nodes out as a stacked list of layers, ordered from bottom to top according to your node order. The bottom-most layer is Node 1, and each further node piles on top as you create or rearrange it within the node tree. Using their respective icons, layers let you enable or disable, lock, and add or remove nodes. Further capability is slated for upcoming releases. Each layer also carries a preview thumbnail plus an icon list of the tools added to that node.

### The node graph in node view

The same graph in Layer View (top left arrow)

### Node Stacks Support up to Eight Layers

DaVinci Resolve 21 raises the ceiling on node stack layers, doubling it from four up to eight.

### Film Look Creator adds Aurora Preset and Fade Rolloff Controls

DaVinci Resolve 21 gives the Film Look Creator a new Aurora preset built to mimic a high-contrast, vivid film look that echoes today's common film stocks. The headline Aurora preset demonstrates how the core look is meant to be applied, although you may want to pile on extra contrast for the best outcome.

### The original footage

### The new Aurora core look applied

The effect also gained two new controls. Color Settings Fade Rolloff: This slider sets how softly the black level is halted at the fade threshold. Film Gate Softness: Controls how blurry the film gate's edges are.

### Shared Node Support for Stereoscopic 3D Clips

Just as ordinary 2D clips do, Stereoscopic 3D clips can now make use of Shared Nodes — a node whose changes propagate at once to every other instance of it within the grades of other clips.

### Customizable HDR and Nit Scopes Ranges

Within HDR projects, the HDR Parade scopes can now take custom ranges. Reshaping those ranges stretches the waveforms in the scope so you can zero in on one particular slice of the waveform.

Ticking the Scale Display Range box narrows the parade scope onto one particular stretch of the waveform.

### HDR Vivid Improvements

DaVinci Resolve 21 brings several enhancements to HDR Vivid support, among them:

- HDR Vivid tooling can now be driven from the DaVinci Resolve Mini Panel.
- A Color timeline filter that surfaces clips by their HDR Vivid analysis and trim status.
- A fallback to the last working trim whenever a manual trim runs past the HDR threshold.
- An HDR badge added to each timeline thumbnail once analysis is done.
- A Mastering display dropdown choice within the HDR Vivid project settings.
- A new Tone mapping mode option for low-light grading inside the Color page HDR Vivid controls.
