# Automation copy paste erase and automation mix list

Version: DaVinci Resolve 20.3 Reference Manual. Context: Mix automation.
[Chapter index](INDEX.md) / [Previous section](automation-overwrite-behavior.md)
<a id="source-automation--copypasteerase"></a> <a id="source-automation--mix-list"></a> <a id="source-new-mix-dialog"></a> <a id="source-playing-automation"></a> <a id="source-the-mix-list-window"></a>

### Automation – Copy/Paste/Erase

The Fairlight > Automation submenu additionally provides dedicated local choices for Copy, Paste, and Erase of automation data. Copy/Paste lets you carry out powerful range-based manipulation of automation, or build a “snapshot” change in which all automation data is pasted at a single moment in time, letting every enabled parameter jump at once to new levels. Working with these commands means you have to spell out which automation parameters are affected by using the Automation Enables controls (the same ones that govern what automation data gets recorded). For instance, to affect fader, mute, and pan automation, you first have to turn on the enables for those parameters. Only the enabled parameters are affected.

NOTE: These commands work whether you're in Clip view or Automation view (for any parameter); what ends up affected is decided by the Automaton Enables rather than by which view you're in.

Enables configured so that copy, paste, or erase touches only Fader, Mute, and Pan data

- Copy: When an active In and Out range exists in the Timeline, Fairlight > Automation > Copy places onto the clipboard the automation data belonging to every selected channel and enabled parameter inside that range. Lacking an active In and Out range, the command instead grabs the data of all automated parameters across every selected and enabled item at the playhead (Snapshot mode).
- Paste: Drops in, at the active range or in point, all the automation data sitting on the clipboard for Automation-enabled parameters. Where an active In to Out range has been set, that range gets populated with whatever automation data was placed on the automation clipboard through Automation > Copy. Where no active In to Out range has been set, the entire automation clipboard is simply dropped in.

TIP: You can move Track Automation among Faders, Sends, and Direct-Out levels. To illustrate, the Fader Level automation from one track can be copied onto a different track's Send Level, and the other way around too. The clipboard's contents may well be directed at a separate channel set and/or a separate target time, just by picking a fresh in point or track selection. Where an active In to Out range has been set in the Timeline, and the clipboard carried Snapshot mode data at the moment of copying, this range gets populated with the static values from that snapshot data.

- Erase: When an active In and Out range exists in the Timeline, Erase removes the automation data of every selected channel inside the range, honoring all the Automation Enable buttons. With no range selected, nothing changes.

TIP: To strip all automation from a Timeline or set of tracks, select the whole timeline range, switch on the Automation Enable buttons for the automation types you mean to clear, and pick Fairlight > Automation > Erase. As an alternative, Fairlight > Automation > Mix List can serve to clear all automation off the Timeline.

### Automation – Mix List

With the Mix List, you can build and manage several mix “passes” plus complete routing and effects setups for one Timeline. Every stored mix can hold wholly different mix automation data changing over time, along with its own routing, plugin setup, track grouping, and so on. This ability is tremendously powerful and grants plenty of creative latitude for producing different versions of mixes (for instance shifting among stereo, 5.1, and Dolby Atmos as formats), or for working with entirely different plugin effects or different creative takes on the mix itself across all the automated parameters.

### The Mix List Window

So the Mix List proves useful for more than holding mix automation data; it can store a dynamic preset of practically anything about how the Mixer is set up. Bear in mind that the Mix List is tied to one specific Timeline and likewise can't be shared across projects. Even so, leaning on the Mix List can be handier than saving many separate versions of timelines or projects. The Mix List can sit as a floating window where the various mixes are visible, or it can stay tucked away until the moment you have to load or save another version. Using the Mix List Window:

- Set up your mix, including all routing and automation as you like.
- Once you've got a mix version worth saving, head to Fairlight > Automation > Mix List, pick “Save Mix,” and supply a name plus whatever notes you'd care to attach.
- From there you're free to alter your mix automation, any routing, and so forth, then store a new version, bring up a different one, or remove an existing mix.
- That “System” preset is a built-in system preset you can't change; feel free to disregard it.

The “New Mix” Dialog: Choosing “New Mix” within the Mix List window brings up a dialog carrying these options:

- Cancel: Lets you cancel the operation.
- Write All: Records the present levels of every control onto their automation curves, laying down a baseline

“snapshot” of all parameters.

- Empty Mix: Strips every bit of automation data out of the mix, keeping only the assignments, routing,

track group enables, etc. This choice gives you a straightforward way to begin “fresh” with a mixer setup on a new mix.

### New Mix dialog

### Playing Automation

Once you've automated a mix, playing it back just means moving the playhead to a spot on the timeline ahead of the recorded automation and starting playback. As the timeline runs, the onscreen controls for each automated parameter appear in green. They glide and refresh so the levels they captured are reflected. During playback, any control holding recorded automation is displayed in green.
