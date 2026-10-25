# Data burn in and data burn in window

Version: DaVinci Resolve 20.3 Reference Manual. Context: Metadata burn in.
[Chapter index](INDEX.md) / [Next section](data-burn-in-metadata-and-custom-output-options.md)
<a id="source-data-burn-in"></a> <a id="source-data-burn-in-1"></a> <a id="source-data-burn-in-frame-io-and-dropbox-replay-integration"></a> <a id="source-data-burn-in-window"></a> <a id="source-overview"></a> <a id="source-project-vs-clip-mode"></a> <a id="source-saving-and-loading-burn-in-presets"></a> <a id="source-setting-up-burned-in-metadata"></a>

## Overview

Covers: Data Burn-In; Frame.io and Dropbox Replay Integration.

## Data Burn-In

### Data Burn-In

Working with the Data Burn-In window, which every page in DaVinci Resolve makes available, is the subject of this chapter.

Through the Data Burn-In window you can show chosen metadata as a timeline-wide “window burn” laid over the picture in the Viewer. That window burn becomes part of the files rendered out on the Deliver page, and it also goes out to video — whether for viewing on an external display or for sending to tape. To open the Burn-In window, choose Workspace > Data Burn-In.

### Data Burn-In window

Window burns have long served as a handy reference when building offline media you’ll need to keep tabs on down the line. Yet the Data Burn window goes far beyond that. To name a few uses, it can watermark review files you’d rather not see distributed by mistake — whether through custom text or alpha-channel graphics — it can paste graphical logos or “bugs” onto programs headed for broadcast (once more, alpha-channel graphics are an option), it can overlay your own reference guidelines of one kind or another atop the images under watch, or it can simply put timecode or clip names on screen for a while so you have something to reference on your monitor as you edit, mix, or screen graded dailies alongside a client.

Viewer displaying record timecode, source timecode, and source clip name

### Project vs. Clip Mode

A pair of buttons up top in the Data Burn window decides whether you’re editing a single batch of burned-in metadata shown across the whole Timeline, or editing burned-in metadata one clip at a time. The two can run together: you might hold timeline-wide window burn settings while keeping separate clip-specific window burn settings for a few clips inside that same timeline. During rendering on the Delivery page, window burns get applied whether you render timelines as separate source clips or render everything as a single clip.

A pair of distinct panels handle adjustments for project-wide window burns alongside clip-specific window burns

### Setting Up Burned-In Metadata

Arranging different clip and project metadata for output as a window burn is straightforward. Here’s how to set one up: 1 Choose Workspace > Data Burn-In. 2 Up at the top of the Data Burn-In window, click either Project or Clip. 3 Tick the checkboxes beside whatever metadata items you wish to show inside the “Add to Video Output” column. Fuller detail on the items offered comes later in this chapter. That first metadata item sits centered close to the frame’s bottom, just over Action Safe. Every further metadata item you switch on appears stacked above the ones already shown, no matter where it falls within the “Add to Video Output” list. 4 Click whichever enabled metadata item in the list you want highlighted black, then tweak that item’s Custom Output parameters off to the right. Fuller detail on the parameters offered comes later in this chapter.

To reset the current window burn setup: Press the Reset button sitting beside the Option drop-down menu, which clears the Data Burn window’s current mode.

### Saving and Loading Burn-In Presets

When certain metadata combinations come up often and you flip between them, each combination can be stored as a preset to reuse later. Saving one as a burn-in preset goes: 1 Open the Option menu and pick Save As New Preset. 2 In the Burn In Preset dialog that pops up, key a name, then click OK. Your new preset now sits among the saved presets listed under the Option menu. Removing a burn-in preset goes: 1 From the Option menu, pick a preset. 2 Open the Option menu once more and pick Delete. 3 You’ll get a dialogue box prompting you to confirm the deletion. Changing a burn-in preset goes: 1 From the Option menu, pick a preset. 2 Adjust it as you see fit. 3 Open the Option menu and pick Update.
