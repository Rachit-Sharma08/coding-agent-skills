# Clip attributes and dialogue matching

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing basics in the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](conventional-cut-copy-and-paste-overview.md) / [Next section](audio-clip-layering-and-audio-compound-clips.md)
<a id="source-ai-dialogue-matcher"></a> <a id="source-clip-attributes-naming"></a> <a id="source-copying-and-pasting-clip-attributes"></a> <a id="source-copying-and-pasting-track-attributes"></a> <a id="source-eq-level-and-ai-dialogue-matching"></a> <a id="source-eq-matcher"></a> <a id="source-level-matcher"></a> <a id="source-paste-and-remove-attributes"></a> <a id="source-removing-attributes"></a> <a id="source-the-paste-attributes-dialog-in-the-fairlight-page"></a> <a id="source-the-pasted-clip"></a> <a id="source-timeline-clip-ai-dialog-matcher-contextual-menu"></a> <a id="source-using-the-cutcopy-head-and-tail-commands"></a>

### The pasted clip

Going about cut and paste this way makes it fast to cut or copy clips with keyboard commands alone, and the clip’s ghost overlay makes it easy to land the clip you’re pasting precisely where you need it, perfectly in sync.

### Using the Cut/Copy Head and Tail Commands

Four more commands make it easy to cut or copy stretches of one or more clips that cross the playhead — either from the In point up to the playhead’s current spot (the Head), or from the playhead’s current spot through to the Out point (the Tail). Here is how to cut or copy a clip’s head or tail and paste the result: 1 With these commands there’s no partial selection to make, so either the Selection (press A) or Range Selection (press T) mode will serve. 2 Select the track holding the clip you mean to copy or cut. When one or more tracks are already selected, the Control-Option-Up or Down Arrow key shortcuts let you shift the track selection state up or down so it lands on whichever tracks hold the clip you mean to cut or copy. 3 Run the playhead so it crosses the clip you mean to cut or copy at the frame you want to mark — either the head’s end or the tail’s start. Where the playhead crosses a clip on a selected track, that clip should select itself automatically. Bear in mind that even when you select a clip with the mouse without selecting a track first, the playhead should still be moved to cross the clip you’re copying or pasting, since doing so lays down a key reference point for the work ahead. 4 Pick Edit > Cut/Copy Head/Tail to lift the stretch of the selected clip you mean to paste. That stretch of the clip lights up right away. 5 From here, you have two routes for getting the cut or copied head or tail of the clip to the spot in the Timeline where you mean to paste it:

a) Moving the playhead now drags the clip you cut or copied along with it, drawn as a ghost clip with waveform “attached” to the playhead at the frame you picked. Whether you drag the playhead with your mouse or work JKL to run the playhead through the Timeline, the cut or copied clip travels in step so that shifting the playhead repositions the cut or copied clip on that track. b) Should you want the cut or copied clip on a different track, lean on the Control-Option-Up or Down Arrow key shortcuts to switch the selected track; the ghost clip follows the change in track selection. In this way, the playhead lets you line the ghost waveform up against the other audio clips around it ahead of pasting. 6 With the clip sitting where you want it, press Command-V to paste it at the spot you’ve picked (right-clicking a track and choosing Paste from the contextual menu works too). The clip turns solid, and that’s it.

### Paste and Remove Attributes

The Fairlight page carries Paste Attributes and Remove Attributes commands for copying and resetting audio parameters and effects, much like the matching commands on the Edit page.

### Clip Attributes Naming

Double-click any clip in the Timeline to reach the Clip Attributes window and rename the clip. A right-click still gets you to this window, opening the dropdown menu of options.

### Copying and Pasting Clip Attributes

With clips, it’s as straightforward as copying a clip, then selecting one or more audio clips, right-clicking another clip, and choosing Paste Attributes from the contextual menu. A dialog comes up so you can pick which audio attributes to paste before you click Apply.

### The Paste Attributes dialog in the Fairlight page

### Copying and Pasting Track Attributes

With tracks, things go a bit differently. Right-click a track header and choose Copy Attributes to grab every track setting and effect. Next, with one or more other track headers selected, right-click that selection and choose Paste Attributes. A dialog comes up so you can pick which track attributes to paste before you click Apply.

The Fairlight page Paste Attributes dialog, here carrying attributes across from one track onto another

### Removing Attributes

For clips or tracks alike, you can right-click and choose Remove Attributes to open a dialog where you pick which attributes to reset to their defaults. NOTE: Ticking the Volume check box in Remove Attributes wipes out every Clip Gain keyframe that’s been added to a clip.

### EQ, Level, and AI Dialogue Matching

To help lay a solid groundwork for a great mix, Fairlight puts forward three features that match unlike timeline clips by their tonal characteristics (EQ profile), their volume level, or their sonic characteristics, as laid out below.

### EQ Matcher

EQ Matcher comes in handy where, for instance, you need to swiftly carry the tonal characteristic (EQ Profile) of on-location dialogue recorded with one kind of microphone over to newly recorded dialogue captured in post on an entirely different microphone. Here is how to capture and apply an EQ Profile: 1 On the timeline clip you’re matching to, right-click and pick Clip Operations > EQ Matching > Capture EQ Profile from the contextual menu.

Timeline clip EQ Matcher contextual menu 2 The captured EQ Profile then goes onto another audio clip by either of these routes: Apply to Clip EQ: For every selected clip on the destination track, this drops the same EQ setting onto its Clip EQ plugin. Apply to Track EQ: Lays the EQ profile over the entire track. Up in the EQ section of the matching Mixer channel strip, the applied EQ curve appears.

A fresh EQ curve shown within a Mixer channel strip Apply to Automated Track EQ: Where a track holds several clips, each one needing its own EQ setting to hold the right tonal match through playback, this option earns its keep. The selection lets you swiftly write automation data, which reshapes the Track EQ curve for each clip as needed. Here is how to put the EQ profile onto an automated track EQ: 1 On the timeline clip you’re matching to, right-click and pick Clip Operations > EQ Matching > Capture EQ Profile from the contextual menu. 2 With the Toggle Automation button — found just right of the transport control — confirmed active (red), pick an EQ parameter out of the Automation drop-down within the destination Track Header, such as EQ > Band 3 > Gain. 3 On the first clip you’re targeting, right-click and pick Clip Operations > EQ Matching > Apply to Automated Track EQ. Do the same for each clip that follows on the track.

- As you repeat the this step, you’ll watch the automation curve shift with every application of the EQ Profile.
- Through playback, the EQ Curve display in the matching mixer channel strip shifts according to the automation data and Playhead position.

### Level Matcher

Level Matcher lets you swiftly and precisely line up the volume of unlike timeline clips with one another. Here is how to match your clip levels with the Level Matcher: 1 On the timeline clip you’re matching to, right-click and pick Clip Operations > Level Matching > Capture Level Profile.

Timeline clip Level Matcher contextual menu 2 On a timeline clip you mean to adjust, right-click and pick Clip Operations > Level Matching > Apply Level Profile. Do the same for whatever other timeline clips you’d like to change.

### AI Dialogue Matcher

AI Dialogue Matcher proves useful when you need to align the ambient quality of one timeline clip with another. In a dialogue replacement scenario, for instance, you may need newly recorded dialogue to sound as though it was captured in the same room as the rest of the on-location dialog.

### Timeline clip AI Dialog Matcher contextual menu

Here is how to put AI Dialogue Matcher to work: 1 On the timeline clip you’re matching to, right-click and pick AI Tools > Dialogue Matcher > Capture Dialogue Profile from the contextual menu. 2 After the audio is analyzed, right-click across the timeline regions you’re targeting and pick AI Tools > Dialogue Matcher > Apply Dialogue Profile from the contextual menu. With the dialogue profile applied, a checkmark turns up beside the Enabled option in the Dialogue Matcher contextual menu.

- Clicking that checkmark flips the dialogue profile on and off.
- Choosing Remove Profile strips the profile off the clip entirely.
