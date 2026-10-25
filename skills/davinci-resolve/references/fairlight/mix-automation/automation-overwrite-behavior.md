# Overwriting automation and new automation overwrites the previous levels

Version: DaVinci Resolve 20.3 Reference Manual. Context: Mix automation.
[Chapter index](INDEX.md) / [Previous section](individual-track-automation-and-preview.md) / [Next section](automation-copy-paste-erase-and-automation-mix-list.md)
<a id="source-adding-and-editing-new-keyframes"></a> <a id="source-adjusting-and-deleting-automation-keyframes"></a> <a id="source-adjusting-individual-keyframes"></a> <a id="source-automation-curve-after-deleting-the-selected-keyframes"></a> <a id="source-automation-follows-edit"></a> <a id="source-clear-all-track-automation"></a> <a id="source-editing-automation"></a> <a id="source-fairlight--automation-controls"></a> <a id="source-new-automation-overwrites-the-previous-levels"></a> <a id="source-overwriting-automation"></a>

### Overwriting Automation

After automation has been recorded for a given clip, you can overwrite it on later passes. With either of the recording approaches described earlier, adjusting the level of a track control that already holds recorded automation shows a red line indicating the new level against the level recorded previously.

Setting new levels to overwrite previously recorded automation displays a red line Hitting play to actually capture this new automation overwrites the earlier levels at this new value.

### New automation overwrites the previous levels

Copying, pasting, and erasing of automation data is handled under the Fairlight Menu > Automation > Copy/ Paste/Erase.

### Automation Follows Edit

As you edit your timeline, you get to decide whether automation travels along with clips as they move or stays pinned to its place. It's on by default, but you can change that by unchecking Fairlight > Automation > Follows Edit. While it's enabled, any time a clip gets moved or edited on the Timeline, whatever automation you'd written across its range comes along too, so that as edits change, the automation tied to a given clip range stays intact. It also proves immensely handy during an initial edit of audio clips that carry automation data. Say you have a recurring sound effect panning left to right; automate that pan onto the audio clip first. As that clip is copied throughout the Timeline, it keeps the same panning automation for every fresh instance. That can be very handy for all sorts of edits needing identical automation data across audio clips in a timeline.

Bear in mind, though, that Automation Follows Edit should be switched off when copying and pasting clips or sequences whose applied automation has no bearing on the new edits. While Automation Follows Edit is on, automation data “lives with” the time range it originated in. Anything of that sort, like volume or panning, rides along with clips. So if an entire section is deleted, all the automation inside the clips in that section is deleted as well. If a section of clips is relocated within the Timeline, all the automation embedded in those clips moves with them to the new spot on the Timeline. With automation switched on in the Fairlight toolbar, the Automation Follows Edit button shows up.

The Automation Follows Edit button, positioned just left of the toolbar's Flag button

### Editing Automation

While automation is switched on (the Toggle Automation button is active), the Pencil tool appears. Paired with the Focus mode, these tools let you edit automation in a variety of ways.

The principal tools for editing automation come from Focus mode. Enabling automation (with Toggle Automation on) brings up the Pencil.

### Adjusting and Deleting Automation Keyframes

The Focus tools give you two distinct ways to adjust automation.

### Adjusting Individual Keyframes

With the Focus tools, you can grab any automation keyframe and drag it up or down and left or right (limited by its neighboring keyframes) to adjust it directly. While zoomed in, this can be a handy way to make exact adjustments. The portion of automation altered by the keyframe you're dragging stays green to show the new curve forming, and a tooltip displaying the value currently being adjusted appears, while the data made earlier shows in gray. Once you let go of the mouse button, the curve is adjusted

A lone keyframe under adjustment, with its earlier level rendered in gray Adjusting and Deleting Multiple Keyframes There's also the Focus mode I-beam selector tool, which lets you build a selection covering several keyframes, then move or delete them.

Pick a span of keyframes with the Focus mode I-beam selector Should you delete the keyframes inside the range, the surviving stretch of the curve levels off so it spans the selection's first keyframe through its last.

### Automation curve after deleting the selected keyframes

### Adding and Editing New Keyframes

For additional detail on drawing and editing keyframes, see “Working with Audio Keyframes on the Timeline” earlier in this chapter.

### Clear All Track Automation

If your goal is to wipe out every bit of automation tied to a track or bus, send and plugin automation included, right-click the track header and pick Clear Track Automation from the menu. A fresh window then opens, presenting the following choices in case you reconsider or wish to erase the automation:

- Cancel: To keep your automation data.
- Reset: Wipes every bit of automation and sends all the controls and parameters it touched back to their default

settings and values.

- Hold: Wipes every bit of automation while preserving the settings and values on all the controls it touched

and parameters.

### Fairlight > Automation Controls

The Fairlight > Automation submenu holds a set of commands that kick off various automation tasks. The commands are:

- All Read: Returns to Read mode every parameter that currently sits in Trim or in Write mode.
- Punch In: With Preview mode on, moves whatever parameters are presently in Preview (blue) over to

Write or Trim. With Preview mode off, it moves every Automation-enabled parameter across all selected channels into Write or Trim.

- Punch Out: With Preview mode on, moves any parameter sitting in Write, Trim or Preview over to Read. With Preview mode off, it moves every Automation-enabled parameter across all selected channels into Read.
- Fill Range: Whenever an active In and Out range exists in the Timeline, the present value of each parameter in Preview gets written across that range.
- Glide Range: While in Preview mode, it “glides” each parameter away from the value it holds at the Timeline's In point toward the preview value waiting at the Out point.
- Join Mix: Allows you to pick automation writing back up by hand in Latch mode, starting at the present level and traveling to whatever level you choose.
