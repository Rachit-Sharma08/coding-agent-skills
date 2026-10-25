# Bus assignment buttons and legacy mixer bus assignment

Version: DaVinci Resolve 20.3 Reference Manual. Context: Mixing in the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](cartesian-view-and-cartesian-view-dolby-atmos.md) / [Next section](fader-controls-and-a-fader-in-the-fairlight-mixer.md)
<a id="source-arm-solo-and-mute-buttons"></a> <a id="source-bus-assignment-buttons"></a> <a id="source-decompose-in-place-contextual-menu"></a> <a id="source-legacy-mixer-bus-assignment"></a> <a id="source-making-fader-vca-assignments"></a> <a id="source-nested-audio-timelines"></a> <a id="source-nesting-vcas"></a> <a id="source-options-for-signal-routing-when-decomposing-a-clip"></a> <a id="source-recording-fader-automation-for-vcas"></a> <a id="source-the-channel-strips-bus-assignment-buttons"></a> <a id="source-using-vca-faders"></a> <a id="source-vca-faders"></a>

### Bus Assignment Buttons

To send a bus made in the Bus Assignment dialog straight onto the Mixer, click the + sign to bring up a dropdown menu of busses on offer. To send several busses at once, Command-Click (Ctrl+Click) each of your picks within the dropdown menu.

The Bus Outputs panel is where the routing of bus signals happens.

### Legacy Mixer Bus Assignment

Within the Legacy Mixer the bus assignments carry two sets of buttons that let you send audio from one channel strip’s output to Sub and Main busses you’ve built for your mix.

### The channel strip’s Bus Assignment buttons

- Main: These buttons route a track or sub’s channels into one or several of the main busses.
- Submix: With these buttons you assign that track’s channels to one or more submix busses.

### Nested Audio Timelines

Edited timelines may be folded together with other timelines by dragging the chosen nested timeline onto a vacant track in the destination timeline. It’s a remarkably powerful, handy feature. For broader background on nested timelines, refer to Chapter 43, “Take Selectors, Compound Clips, and Nested Timelines.” Say, for instance, you’ve built a master timeline meant to hold your master mix, and you want to fold in the work done on a separate timeline devoted to dialogue editing. That dialogue timeline can now show up as one nested timeline, depicted as a single track within the master mixing timeline.

Track A1, Dialogue, is a stereo stand-in for an edited timeline. Should you wish to handle the individual tracks and clips once more, a procedure called decompose turns that single nested timeline track back into the edited sequence. A range of options exist for decomposing back to the original set of tracks, with several bussing choices on offer. This image depicts what used to be a separate, edited timeline of dialogue tracks and is now one track, A1 Dialogue, pulled into the destination master mix timeline. Right-clicking the clip opens a contextual menu where you can decompose the track on the spot, returning it to its original tracks together with its clip edits. Two decompose options serve this. On the Fairlight page you can Preserve Audio Data, while on the Edit page you can Preserve Audio Data and also decompose by Using Clips Only.

### Decompose in Place contextual menu

After you’ve opted to decompose the track into its earlier Timeline elements, the Decompose Preserving Audio Data dialog box opens, putting several more options within reach.

### Options for signal routing when decomposing a clip

Decomposing a nested timeline in the Fairlight page presents three options. Every one of the three keeps mix and plugin automation intact on the source tracks; they part ways only over routing. The picks are: New Matching Busses: Every bus from the nested source timeline is carried into the current timeline as fresh, separate busses. These busses retain all the processing, routings, settings, and automation handed over from the nested source timeline. Whatever bus routing already exists in the destination timeline stays untouched. This option shines when you want to merge different mix layouts and keep all existing bus routing in the destination timeline, while folding the bus topology from the nested source timeline into the destination to forge one larger entity. Preserve Existing Paths: This option keeps all the master bus information in the current timeline and sends matching busses from the decomposed nested timeline over to preexisting, identical busses in the destination timeline. It’s the best fit when the nested source timeline and the destination timeline use the same bus routing structure, as you might find with a shared layout template. In that situation, you simply want to drop the tracks into the destination timeline and send them to the same master designations. All your mix automation and plugins still come across too. Leave Unassigned: This option drops the new tracks in unassigned when created, ready for you to route however you require.

Decomposed view of the nested dialogue timeline, with the original dialogue tracks and edits on display Nested audio timelines really earn their keep when you’re juggling large projects loaded with tracks and elaborate routing. Several editors can tackle different facets all at once. As an example, a dialogue editor might handle dialogue and ADR in one timeline while an effects editor designs and spots effects in another and a music editor cuts and spots music in a third, each on their own. Those interim timelines can then be brought in later to a master timeline for a final main mix. It also helps picture editors who’d rather not wrangle many tracks of audio while cutting picture. Over on the Edit page, once a track sequence is decomposed, it too can revert to the original track layout with every audio clip ready for further editing.

### VCA Faders

A VCA fader serves to govern the level of several tracks from a single control. You can tie several faders to one dedicated VCA, whereupon a VCA channel strip turns up at the right of the Mixer. VCAs let you adjust the underlying level of several faders at once via a single VCA master fader, which can be a boon when wrangling the levels of complicated sets of audio tracks.

Group Labels in each control strip, above the control strip label You’ll find the controls for this within the VCA and Group label region of every mixer channel strip, which shows the VCA or Track Group to which each fader has been tied.

### Making Fader VCA Assignments

Any channel strip can be tied to one of 64 VCAs by right-clicking the VCA label region and picking a VCA from the dropdown that opens. Where a fader already belongs to a VCA, picking “No VCA” detaches it. NOTE: So as to keep clutter down, the VCA Assignment dropdown menu shows just 10 VCAs to begin with; more come in as required. Once those first 10 are all assigned, the menu pulls in further VCAs from the available pool, one a a time.

Right-clicking a VCA Label opens a dropdown menu through which you tie faders to that VCA or pull them off it. TIP: VCAs can be assigned fast across a chosen set of channel strips, or across every one, if you hold — prior to running the operation — the Option key (Mac) or the Alt key (Windows) to cover all selected tracks, or instead Command-Option (Mac) or Control-Alt (Windows) to cover all mixer channel strips. Such shortcuts spare you a good deal of workflow time.

### Using VCA Faders

After you’ve tied several faders to a VCA, a dedicated channel strip for that VCA shows up on the right side of the Mixer. Adjusting the VCA channel strip drives, all at once, every fader, solo button, and mute button of all channel strips belonging to that group, as shown below.

Moving the VCA 1 fader likewise moves the SYNC, VO, and Drum Hit faders tied to that VCA. Even while governing faders that belong to a VCA, you can still nudge each individual channel strip fader on its own to make relative adjustments.

- Channel strip faders shift together only when you move the VCA fader.
- As the VCA fader moves, each individual fader keeps its relative offset from the other faders

the VCA governs. For instance, as the screenshot above shows, the VCA 1 fader is driving the faders in tracks SYNC, VO, and Drum Hit, while every individual channel strip fader in that group holds its offset from the rest.

### Recording Fader Automation for VCAs

You can lay down automation data onto a VCA fader, and every fader in that VCA group will follow even though none of them is actually automated itself. That makes it painless to record intricate automation spanning several faders while keeping the freedom to fine-tune each individual fader down the line.

### Nesting VCAs

VCAs may also be “nested,” such that one or more VCAs fall under the control of yet another VCA. To nest a VCA, just assign the VCAs you want governed to another “master” VCA.

### Arm, Solo, and Mute Buttons

These controls match the ones found on the track header of every timeline audio track.

- Record Arm: Readies a track for recording once the Record button on the transport is engaged (lights up red when enabled).
- Solo: Lets you silence every other track so you can hear one track you need to focus on by itself (lights up green when enabled). With Solo enabled across several tracks, all soloed tracks play and all non-soloed tracks fall silent. Solo status carries into rendering, so when one or more tracks are soloed, the muted tracks aren’t output or rendered.
- Solo Safe: Command-Shift-click a Solo button to drop it into Solo Safe mode (lights up blue when enabled). Channel strips set to Solo Safe keep playing even when Solo is on for other tracks. Solo Safe can help with effect returns busses carrying effects like reverb, where you might want to hear the reverb while the tracks feeding it are soloed.
- Exclusive Solo: With this on, clicking a track’s Solo button pulls other soloed tracks out of Solo mode. That means just one track can be soloed and heard at a time, handy when you want to compare audio sources, to catch sonic differences while comparing levels or processing.

NOTE: A track sitting in Solo Safe mode stays unaffected when you solo a track under Exclusive Solo mode. To bring that track in, you must switch the Safe Solo button off by hand first. Off by default, Exclusive Solo can be switched on by choosing it from the Fairlight menu. You can also bind a key command to this function within the Keyboard Customization dialog. For more on Keyboard Customization, refer to Chapter 4, “System and User Preferences.”

- Mute: Switching Mute on stops audio playback from that track (lights up orange when enabled). This carries into rendering, so when one or more tracks are muted, they aren’t output or rendered.

The channel strip’s Record Arm, Solo, and Mute buttons TIP: Click a button and drag the cursor over several channel strips to toggle that button on or off across several tracks effortlessly.
