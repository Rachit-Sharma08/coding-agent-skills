# Link grouping and working separately with multichannel audio file elements

Version: DaVinci Resolve 20.3 Reference Manual. Context: Setting up tracks busses and patching.
[Chapter index](INDEX.md) / [Previous section](defining-audio-track-types-and-rearranging-tracks.md) / [Next section](bus-assign-window-and-setting-signal-paths.md)
<a id="source-assigning-busses"></a> <a id="source-bus-assignment-using-the-mixer"></a> <a id="source-bus-formatting-with-fixed-bus"></a> <a id="source-bus-routing-dropdown-menu-on-a-channel-strip"></a> <a id="source-creating-busses"></a> <a id="source-legacy-fixed-bussing"></a> <a id="source-link-grouping"></a> <a id="source-making-bus-assignments"></a> <a id="source-setting-up-tracks-busses-and-patching-part-2"></a> <a id="source-the-bus-assign-window"></a> <a id="source-the-depth-of-options-in-the-flexbus-system"></a> <a id="source-working-separately-with-multichannel-audio-file-elements"></a>

### Link Grouping

The Link Group function lets you tie together related mono tracks of material and handle them as one entity driven by a single fader on a single channel strip. A link group can only be built from mono tracks; the other types — stereo, 5.1, 7.1, Atmos, or Adaptive — are ineligible. Where a multi-channel track uses lanes, a link group of mono tracks instead acts as separate, editable tracks in the Timeline. Even so, each track gets mapped when you pick a track type, following one of the usual multi-channel mappings (stereo, 5.1, 7.1, Adaptive). Link groups come in extremely handy — say, when you’ve received separate “.L/.R” halves of a stereo mix, or a batch of six related audio files that must be assembled into one 5.1 surround mix, or when surround channels must be re-edited one channel at a time. To create a Link Group from individual mono tracks: 1 Make two or more Mono audio tracks you’d like grouped together. If you want a link group with a specific channel mapping such as 5.1, be sure to create enough tracks (here, 6). 2 Choose Fairlight > Link Group. 3 Once the Link Group dialog opens, mono audio tracks show up as active buttons (every other track type is grayed out, since those can’t be linked). Click to enable the button for each track you want in the link group you’re building. Which track-type mappings are available for your group depends on how many tracks you selected.

Selecting six tracks to use for creating a link group 4 After all the required tracks are picked, press one of the “Link as” buttons shown below. In this case six tracks are chosen, so 5.1 Film or 5.1 would be valid clicks.

Selecting enough tracks lets you build groups linked as particular surround mappings.

After that, the tracks you chose should merge into a single block, signaling they’ve been linked.

The Link Group window displays the link indicator line beside the track names. Depending on how many mono channels you selected, Fairlight presents the possible linking options. For example, with ten channels selected, both Atmos 7.1.2 and 5.1.4 appear as choices.

The Link As option hinges on how many channels are being linked. 5 Close the Link Group window once you’re done. Once a link group is in place, one bar stretches down the headers’ left edge, covering the whole group. Provided the tracks are tall enough, every one carries a label showing its assigned channel per the track mapping you chose in step 4 — for a 5.1 surround mapping, say, L, R, C, LFE, Ls, Rs, and so on. You’re also free to edit extra or alternative contributing elements of a surround mix into whichever track stands for that channel.

Within a Link Group, each track is labeled so you can tell which one stands for which surround channel.

### Working Separately with Multichannel Audio File Elements

If you’ve edited a multichannel audio clip onto a multichannel track, that track and its contents can be converted into a Link Group of mono tracks, each holding a single clip for one of the track’s channels. This helps when you need to repair a multi-channel surround clip whose track mapping is wrong. Convert it into a Link Group, and you can then rearrange the channels with ease. Turning one multichannel timeline into a Link Group works like this: right-click the header of a multichannel audio track and select Convert to Linked Group from the contextual menu. Doing so immediately produces one fresh audio track for each channel, all bound together. Converting a 5.1 track, for example, gives six new tracks each carrying a separate audio clip (one per channel), all linked. Where required, a linked group can also be broken apart to bring back separate mono tracks. To unlink one: 1 Choose Fairlight > Link Group. 2 In the Link Group dialog that opens, pick the link group you wish to unlink. 3 Click Unlink. 4 Close the Link Group window when finished. SMPTE and Film order Standards The differences in how the multichannel files get routed stem from the path order of the SMPTE or Film standards. They are:

- 5.1 film order: L, C, R, Ls, Rs, LFE
- 5.1 SMPTE order: L, R, C, LFE, Ls, Rs
- 7.1 film order: L, C, R, Lss, Rss, Lsr, Rsr, LFE
- 7.1 SMPTE order: L, R, C, LFE, Lss, Rss, Lsr, Rsr

### Creating Busses

Picking Fairlight > Bus Format opens the Bus Format window, where you create the busses you need (within your system’s limits) to organize your program’s tracks and channels. The Bus list lets you rename a bus, set the format of each one (a dropdown shows up in the Format column of every list entry), reports how many channels a bus has, and lets you color-code each bus (a Color dropdown picks that bus’s color). Just click any item on the Bus list to select it and pick different choices from the Format and Color dropdowns, or click a bus’s Name to select it and type a custom name. Three buttons sit at the bottom of the list, letting you Add Bus, Duplicate, or Remove selected busses. When you’ve finished adjusting the available busses, click OK to keep the changes and close the Bus Format window, or Cancel to close it without applying anything (though all pre-existing busses stay put). The bottom button row additionally shows a Used tally of what’s in use and what remains available on your workstation.

### The depth of options in the FlexBus system

Immersive Formats (Studio Version Only) To enable the immersive formats, head to Preferences > Video and Audio I/O > System Panel > Immersive Audio and select from the appropriate options. Once turned on, the various immersive bus formats become available in the Bus Format panel’s Bus list.

From the Video and Audio I/O panel you can switch the Immersive Audio options on or off.

### Legacy Fixed Bussing

Working with the FlexBus topology is strongly advised for its flexibility, and some newer features only function under FlexBus. At some point, though, you might have to use legacy Fixed Bussing in a new project. To enable Fixed Bussing in a freshly created project, before adding any timeline, open Project Settings > Fairlight, and under the Bussing heading tick “Use fixed bus mapping.” From then on, all bussing runs through the legacy Fixed Bus topology.

### Bus formatting with Fixed Bus

The legacy Bus Format window carries four buttons for creating the various Fixed Bus types. Whenever you create a new bus — whether a Main, Sub, Aux, or Multi Track — it gets added to the list that shows beneath. The legacy Bus list behaves just like the FlexBus list, offering rename, format, color code, and so on, plus buttons to Duplicate or Remove selected busses. When you’ve finished adjusting the available busses, click OK to keep the changes and close the Bus Format window, or Cancel to close it (though any busses you made stay put). The bottom button row additionally shows a Used tally of what’s in use and what remains available on your workstation.

### Assigning Busses

After you’ve made one or more busses, you can route various tracks to specific busses, and likewise busses to busses, busses to tracks, and the final Main bus destinations.

### Bus Assignment Using the Mixer

Assigning your track(s) to any available bus is easy using the plus (“+”) icon on a Mixer channel strip:

- Pick a mixer channel, then click the plus (“+”) icon within either the Bus Output or Bus Sends section.
- From the dropdown menu, pick whichever destination you want.
- A rectangle bearing the bus’s name shows up, confirming the bus has been assigned.

### Bus routing dropdown menu on a channel strip

TIP: To rapidly route a bus to a chosen group of tracks — or to every track — hold a modifier before you carry out the action: the Option key (Mac) or the Alt key (Windows) covers all selected tracks, while Command‑Option (Mac) or Control-Alt (Windows) covers all mixer channel strips. Such shortcuts can shave plenty of time off your workflow.

### The Bus Assign Window

When there are plenty of busses or tracks to deal with, the Bus Assign window makes it simple to connect to all of them in one place. Choose Fairlight > Bus Assign to open the window. You can build several bus assignments inside the dialog, and those new assignments turn up in the Bus Outputs section on the Mixer’s channel strips. The top displays the Send and the Out of each available bus, while the bottom lists every available track and bus you can connect to. By default the Bus Assign window opens in List view, where each bus and track appears as a list, but the icon in the window’s upper right switches it to Icon view, where Available Tracks show up as buttons.

### Making Bus Assignments

Assigning Using List View Click a button in the Busses section to pick the Send or Out of that bus, then click any destination in the tracks/busses list below, or drag across a group of tracks or busses to assign them all. Once assigned, the bus number shows up in the Bus Sends or Bus Outputs column.

- To assign every track, Sub, and Aux to a bus: Pick a button within the Busses section to highlight that bus, then click Assign All.
- To clear all track assignments from a particular bus: Pick a button within the Busses section to highlight that bus, then click Unassign All. Once your bus assignments are complete, click the Close button to dismiss the dialog.
