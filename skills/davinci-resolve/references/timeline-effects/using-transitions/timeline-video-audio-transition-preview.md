# Video and audio transitions in the timeline and previewing transitions

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using transitions.
[Chapter index](INDEX.md) / [Next section](transition-inspector-properties-and-favorites.md)
<a id="source-adding-and-editing-transitions"></a> <a id="source-adding-transitions-by"></a> <a id="source-adding-transitions-when-theres-not-enough-handles"></a> <a id="source-dragging-to-create-overlap"></a> <a id="source-previewing-transitions"></a> <a id="source-the-transition-contextual-menu-in-the-effects-library"></a> <a id="source-using-transitions"></a> <a id="source-using-transitions-part-1"></a> <a id="source-video-and-audio-transitions-in-the-timeline"></a> <a id="source-working-with-transitions"></a>

### Using Transitions

When moving from one image to the next calls for something weightier than a plain cut, transitions act as the connective tissue that ties those moments together. The pages here lay out the various ways to add and edit transitions throughout your program.

### Working With Transitions

As another route for spanning the shift from one clip to the next, transitions frequently signal a jump in time or place as scenes change. The transitions DaVinci Resolve offers run from assorted takes on the classic cross dissolve through various kinds of wipes, giving you plenty of room to maneuver when polishing creative edits. On top of those, DaVinci Resolve also handles third‑party OpenFX transitions you install onto your system. You apply transitions at edit points, where they show up as editable objects within the Timeline.

### Video and audio transitions in the Timeline

### Previewing Transitions

If you want to see a transition before dropping it into the Timeline, first confirm that “Hover Scrub Preview” is ticked in the Transitions option menu, then rest your pointer on any transition — found in the Transitions tab (Cut page) or in the Effects Library Toolbox (Edit page) — and slide it across the thumbnail. The preview plays in the Viewer drawing on the two clips closest to the smart indicator on the Cut page, or the two clips closest to the playhead on the Edit page.

Scrubbing over a Transition Thumbnail previews the transition in the Viewer. Hit Shift-Space to summon the Effects Search dialog, which covers transitions too. Begin typing in the search field to surface the transitions you’re after. Clicking a transition in the search list applies it to whichever edit point lies nearest the playhead.

### Adding and Editing Transitions

The procedures that follow explain how to add and edit transitions in the Timeline through the mouse as well as keyboard shortcuts. Mouse-based ways to add transitions:

- To add a transition by dragging it from the Effects Library: Pull a video transition out of the Effects Library and onto an edit point in the Timeline so it sits centered at, ending at, or starting at that edit point. Without any overlap between the two clips’ heads and tails, placing a transition exactly where you want may not be possible.
- To add a transition by double-clicking its Effects Library icon: A double-click on that icon within the library drops the transition onto the edit point marked by the smart indicator (Cut page), or at the tail of whatever clip currently sits under the playhead (Edit page).
- To add a transition by clicking the Transition Alignment icons: On the Cut page, three Transition Alignment icons run along the bottom of the Transitions Library. Clicking any one of them lays the selected transition on the edit point flagged by the smart indicator, using the alignment you chose.
- To add a transition using the Effects Library contextual menu: Choose your edit points (capped at one per track), after which a right-click on a video transition inside the Effects Library lets you select Add to Selected Edit Points. With that, the transition lands on every chosen edit point simultaneously.

### The Transition contextual menu in the Effects Library

- To add a transition using the Edit Point contextual menu: On the Edit page, right-click any edit point between clips that have overlapping handles, then pick one of the four standard-transition durations on offer; those options — quarter-second, half-second, one second, and two seconds — are expressed in frames according to whatever the Timeline’s current frame rate happens to be.

The Transition contextual menu for an edit in the Timeline Keyboard-shortcut ways to add transitions:

- To add a video+audio transition using the Effects Search: Tap Shift-Space to open the Effects Search dialog, transitions included. Type into the search field to bring up the matching transitions, then click one in the result list to apply it to whichever edit point is closest to the playhead.
- To add a video+audio transition using the keyboard: Pick one or more edit points with the Selection tool — or park the playhead beside an edit you want and tap V to grab it — then press Command-T (Timeline > Add Transition) for the standard transition. The transition takes its length from the “Standard transition duration” set in the Editing panel of the User Preferences, which is one second out of the box, unless the selected edit point’s overlapping handles allow only less.
- To add a video or audio-only transition using the keyboard: Pick one or more edit points, then press Option-T (Timeline > Add Video Only Transition) for a video-only transition, or Shift-T (Timeline > Add Audio Only Transition) for an audio-only one. Again, the length follows the “Standard transition duration” set in the Editing panel of the User Preferences — one second by default, or whatever the selected edit point’s overlapping handles permit.
- To add a transition with specific alignment using the keyboard: Pick an edit, tap the U key to land on its start, center, or end, then press Command-T. The standard transition arrives aligned according to that edit selection: choosing the start of the edit drops a transition ending on the edit, choosing the end drops one starting on the edit, and choosing the center drops one centered the same way.

Methods of moving and duplicating transitions:

- To move a transition from one edit to another: Pick a transition, then drag it over to a different edit point.
- To copy a transition from one edit to another: Pick a transition, then option-drag it across to another edit point.

To duplicate a single transition across several edit points at once: 1 Right-click the transition you wish to duplicate and choose copy (or press Command-C). 2 With the Command-Key held down, click every edit point in the Timeline you’d like the transition copied to until they glow green, then let go of the Command-Key. 3 Right-click any of those green-highlighted edit points and choose Paste (or press Command-V), which copies the chosen transition onto all of the selected edit points. Timeline-based ways to alter transitions:

- To change a transition’s type: Drop a different transition from the Effects Library on top of the existing one in the Timeline.
- To change a transition’s duration: In the Timeline, drag the transition’s start or end to lengthen or shorten it evenly around the current edit. Or instead, take one of these actions:
- Right-click any transition and pick Change Transition Duration, or select it and press Command-D, then set a new duration in the dialog that opens and click Change.
- Double-click any transition to bring it up in the Inspector, where you can enter a fresh duration in seconds or frames.
- Drag a transition’s edge along the Timeline to resize its duration. Keeping the Command key pressed as you drag lets you reshape just one side of the transition’s duration.
- To change a transition’s alignment: In the Timeline, right-click the transition and select a different alignment method from its contextual menu. Alternatively, double-click any transition to open it in the Inspector and pick a fresh option from the Alignment drop-down.
- To remove a transition: Pick a transition in the Timeline and tap the Delete key. Failing that, give it a right-click within the Timeline and pick Delete off the contextual menu.

### Adding Transitions When There’s Not Enough Handles

When the overlapping outgoing and incoming handles at an edit point lack the frames to hold the standard transition duration, and you go to add a transition — whether by picking one or more edit points then hitting Command-T, or by right-clicking an edit point to reach its contextual-menu transition options — a dialog pops up with three choices:

- Trim Clips: This automatically trims the incoming and outgoing sides of each chosen edit point to build the overlap the standard transition requires.
- Skip Clips: Leaves the chosen edit points that lack enough overlap without any transition.
- Cancel: Calls off the operation altogether.

### Adding Transitions By

### Dragging to Create Overlap

Another approach makes building transitions easy during drag-and-drop editing: simply overlap the start and end of two clips at the spot where you want a transition to land. While you drag a clip or edit to overlap another clip, hold the Option and Shift keyboard modifiers down together. Three variations are open to you:

Grab a clip’s In or Out point, then with Option-Shift held down drag that edit point so it overlaps a neighboring clip where the transition should form.

Making a transition by Option-Shift dragging an edit point so two clips overlap Grab a clip, then with Option-Shift held down drag the whole clip so it overlaps a neighboring clip where the transition should form. Making a transition by Option-Shift dragging a full clip so it overlaps another one

With the Option-Shift keys held down, drag a clip out of the Media Pool so it overlaps a clip already sitting in the Timeline.

Making a transition by Option-Shift dragging a Media Pool clip onto a clip that already lives in the Timeline
