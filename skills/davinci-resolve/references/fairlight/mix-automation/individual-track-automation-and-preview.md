# Recording automation for specific individual tracks and automation preview mode

Version: DaVinci Resolve 20.3 Reference Manual. Context: Mix automation.
[Chapter index](INDEX.md) / [Previous section](recording-automation-for-multiple-tracks.md) / [Next section](automation-overwrite-behavior.md)
<a id="source-automation-active-range"></a> <a id="source-automation-preview-mode"></a> <a id="source-recording-automation-for-specific-individual-tracks"></a> <a id="source-right-click-to-view-automation"></a> <a id="source-the-automation-dropdown-menu"></a> <a id="source-viewing-automation-in-the-timeline"></a>

### Recording Automation for Specific Individual Tracks

Follow these steps to capture automated moves on controls within control strips you've specifically armed: 1 Bring up the Automation toolbar and carry out the following three preparatory steps: a) Decide whether you intend to write fresh automation or to trim automation that's already on record. Write mode suits the first time you record automation, or any time you're replacing earlier automation with entirely new values. Trim mode suits situations where you're making incremental adjustments to automation recorded earlier. b) After that, set Touch to Off, which turns off blanket automation recording and obliges you to arm the particular tracks you wish to automate. 2 Click the automation arm button situated above the fader of whichever Mixer track or track header you want to record automation onto. Even with the Touch control set to off, moving a control on an armed channel strip records automation in Latch mode.

The automation arming button above a fader in the Mixer

The automation arming button in the track header

3 Position the playhead at the start of the timeline section you want to record automation across. 4 Then start playback by any means (Spacebar, L, Play button, Fairlight or third-party audio control panel), and apply whatever changes you like to the controls you armed for automation recording. As you adjust them, the affected fader control glows red to signal that automation is being recorded. Should the Timeline be showing the very automation data you're recording, you can watch the new automation drawn live, in red.

New automation line in red while being recorded

5 Once you're done, halt playback by any means (Spacebar, K, Stop button, Fairlight or thirdparty audio control panel). Automation recording halts at the same time. Displayed automation shifts to green after recording ends. If the result isn't to your liking, you can undo and begin again, or edit the automation through the methods covered later in this chapter. Alternatively, you can move the playhead back and overwrite automation with new automation whenever you wish.

### Automation Preview Mode

Preview is one more mix automation workflow, made specifically for working across scene-based material. With it on, mix items that are in preview aren't governed by previously recorded automation, so they react to their controls manually. Afterward, those items can be switched into write (or trim) to lay down actual automation. As a rule, Preview mode serves to try out new mix settings on one specific stretch of a timeline while other stretches already hold recorded automation data. Preview mode stops previously recorded automation from moving the controls you're trying to adjust within a targeted section. Once you're satisfied with the new adjustments, they can be committed to the targeted section. Preview mode releases the faders (along with other controls) from automation control and lets you move them freely as you experiment with various levels and settings. Normally, moving one or more controls means writing automation data for them, but switching into Preview mode lets you play with the controls as much as you wish without committing anything, writing automation data only when you're ready. To bring enabled mix items into the Preview state, first enter Preview mode by doing one of the following:

- Toggle Preview in the Automation toolbar.
- Press the Preview key on the Mix page of the Fairlight controller.

Once Preview is engaged:

- Individual parameters can be switched into Preview Touch Latch.
- The AUTO key beside a fader can be used to preview every enabled parameter on that channel.
- The Auto button on the screen mixer strips is available for this too.
- While Preview mode is active, every parameter sitting in Preview is marked with a BLUE automation indicator.

After you're in Preview mode, you can move mix items into write (or trim) through:

- Dropping in manually via the Fairlight > Automation > Punch In menu choice.
- Dropping in manually with the In key on the Fairlight controller.
- An automatic drop-in based on the Active In and Out points on the Fairlight controller. Once a parameter is enabled for Preview, it holds that state no matter how the transport starts and stops. That differs from placing mix items into WRITE, which has to be redone after every transport stop.

Other Preview-related operations include:

- Populating a range marked by In and Out points using every parameter that's presently in Preview.
- Sliding each parameter from the value it holds at the Range In point over to its Preview value at the Range Out point.

### Automation Active Range

Using the Automation Active Range, you can designate just one specific range on the timeline for automation recording, so that anything beyond that range stays “write protected” and remains undisturbed.

- To switch on the Active Range, pick Fairlight > Automation > Active Range, where you're able to mark the Active Range In/Out points, or to enable or disable the Active Range.
- After a range is set, automation writing happens only within that range.
- You can pick whichever automation mode you'd like to work in (e.g., Snap).
- After playback gets underway, every bit of automation data generated ahead of the range is handled automatically in

Preview mode (without your having to flip the Preview switch on) right up until you hit the Active Range in point. Once you're inside the Active range, automation recording begins.

- When the range ends, automation recording is punched out for you automatically.
- Switching the Active Range off is done by clearing the checkmark on Fairlight > Automation > Active Range > Enable.

NOTE: Whatever controls sit in Read mode keep playing back their automation no matter what state the Active Range is in. A red bar marks the Active Range along the ruler; automation data gets written inside that range

### Viewing Automation in the Timeline

Once automation has been recorded against a supported plugin parameter or a Mixer channel control, picking it out and displaying it on the matching timeline track is possible through one of the approaches outlined below.

### Right-Click to View Automation

Fairlight lets you pick out and display track automation by right-clicking parameters on Fairlight FX, on supported Audio Unit or VST plugins, or on Mixer channel controls. The name of that parameter or control shows up in the track header, while its matching automation curve appears in the Timeline. This is a real time-saver, particularly when automating supported plugins that carry a long parameter list, such as a parametric EQ or a mixer channel strip emulation.

### The Automation Dropdown Menu

With automation switched on through the Toggle Automation button, the Automaton dropdown menu on the track header lets you pick which automation curve to display; the available choices cover Fader, Mute, Pan, EQ, Compressor, Limiter, Aux, Plugins, and Misc controls.

Mixing automation for the Fader shown in the Timeline NOTE: While you're looking at Fader Level automation on a track routed to a VCA, the curve for that VCA's automation shows up as well.
