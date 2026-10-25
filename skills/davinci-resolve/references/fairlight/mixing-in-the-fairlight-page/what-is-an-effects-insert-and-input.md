# What is an effects insert and input

Version: DaVinci Resolve 20.3 Reference Manual. Context: Mixing in the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](selecting-channel-strips-and-tracks-and-track-organization.md) / [Next section](copying-and-pasting-effects.md)
<a id="source-changing-the-order-of-effects-on-a-channel"></a> <a id="source-direct-output"></a> <a id="source-effects"></a> <a id="source-effects-order-dropdown-menu"></a> <a id="source-input"></a> <a id="source-insert"></a> <a id="source-micinst"></a> <a id="source-moving-inserts-by-dragging"></a> <a id="source-path-settings"></a> <a id="source-path-settings-window"></a> <a id="source-record-level"></a> <a id="source-trim"></a> <a id="source-what-is-an-effects-insert"></a>

### What Is An Effects Insert?

Every effect you place on a channel switches on a signal processing “insert” — an insertion point. From there the source signal runs through the effect’s input to its output, then carries on to any further insert(s) and on to the next stage in the Mixer’s signal flow. Beyond the built in Dynamics and EQ processing, DaVinci Resolve allows six inserts per channel in all. Clicking the Input area opens the Input dropdown menu, where you can patch inputs, patch busses, and set up the input parameters for audio signals coming through Blackmagic or other hardware audio interfaces.

“Pre” vs. “Post” When a signal is described as pre, it’s tapped for use ahead of some other connection point. You might, for instance, favor pre-fader metering since the meter then always reflects the original signal level arriving from disk. A post signal, by contrast, is taken after a connection point. Typically you’d want effect sends headed to a reverb to track a track’s main fader so the reverb level rises and falls with the overall level. For that reason, Bus Sends default to post fader routing.

### Input

To learn more about working with the Input menu’s options, consult Chapter 171, “Setting Up Tracks, Busses, and Patching.”

Through the Input dropdown menu you can begin patching any source that’s available by way of the Patch Input/Output window.

### Path Settings

Selecting Input at the top of the Mixer channel strip brings up the Path Settings control window. The controls there let you alter several aspects of the Mixer channel strip that might need attention before or after recording — managing the mic/line inputs on Fairlight audio interface hardware, among other things.

### Path Settings window

### Mic/Inst

This panel shows controls only when channels 1 or 2 of a Fairlight SX36 audio interface are hooked up to your system. With that connection in place, you can remotely drive every option — level included — for the SX36’s mic/instrument inputs whenever they’re assigned to the channel. Lacking an SX36 connection, the area stays empty.

### Record Level

- Record: Tied to and the same as the channel strip’s Record Enable button, placed here for convenience; pressing either one activates the other.
- Thru: Lets the input signal reach the Mixer without turning on a record path. It’s perfect when you want a source always on hand purely for monitoring.
- Record Level: Lets you put a digital gain change on the record path to disk, downstream of your audio interface’s analog-to-digital converter. Ordinarily leave this at 0.0 (no change, unity gain), since it governs the level being recorded to disk. For the best audio fidelity, the recommended approach is to manage the input level into DaVinci Resolve with your audio interface’s own level controls. Even so, you may occasionally want a touch more level, or lack access to the interface’s controls, and in those cases this input adjustment is available.

### Trim

- Polarity: Flips the polarity of the signal entering the channel strip — often called “flipping the phase.” Picture an input like an explosion whose transient attack yields a strongly positive-going waveform sitting mostly above the zero line. Inverting the polarity makes that signal chiefly negative-going, so its waveform now bunches below the zero line. Polarity inversion is sometimes employed to bring signals from several microphones into tighter alignment, and it can serve creatively to shape such a signal’s frequency response.
- Trim Level: Lets you adjust the level of the signal arriving from disk, after the Track FX (which work straight off disk) and before every other effect. Sitting downstream of the recorded-to-disk signal, Trim Level leaves the recording level untouched. As a playback adjustment, Trim lets you set how loud the signal entering your mix is so as to optimize what feeds the effects and busses, or to nudge an otherwise flawless mix element slightly up or down.

### Direct Output

Every audio channel strip can switch on a direct output capable of feeding any other input destination. To patch that source, use the Track Direct option in the Patch Input/Output dialog through the Source dropdown.

- On/Off: Turns the direct output on or off.
- Pre: Places the direct output’s tap-off point pre (ahead of) the channel fader. On by default.
- Level Control: Adjusts the level across the range from full off (minus infinity) up to +10 dB. Default is 0.0 (unity gain).

Further detail appears in Chapter 171, “Setting Up Tracks, Busses, and Patching.”

### Insert

Bound to and the same as the channel strip’s Effects In button, provided here for convenience; pressing either activates the other. With one toggle it moves every Fairlight FX, AU, or VST effect on a channel into or out of the signal path.

### Effects

Fairlight FX, VST, and Audio Unit effects can all be placed on the Mixer’s channel strips. Such an effect acts on the whole track rather than on just one or more of that track’s clips in the Timeline. Clicking the plus (“+”) button reveals a dropdown menu from which any Fairlight FX, VST, or AU effect installed on your machine can be added to the track. Entries in that menu are grouped by processing type, and within each type a nested set offers Fairlight FX, AU, and VST (on a Mac) or Fairlight FX and VST (on Windows). NOTE: What you’ve installed determines the lineup, but the audio effects offered for Mixer channel strip inserts is frequently near to — or the very same as — those reachable for clip-based audio processing in the Effects panel along the left of the Cut, Edit, and Fairlight pages. TIP: Keep favorite effects handy at the top of the list by flagging them as favorites in the Effects panel. To mark one, click the star beside its name.

Clicking the plus sign brings up the Effects dropdown list for assignment

Hover over any effect in the list to surface controls for turning it on or off, swapping or removing it, or opening that effect’s custom controls (its own user interface).

Holding the pointer over an effect insert brings up that effect’s controls.

### Changing the Order of Effects on a Channel

To rearrange the effect order on any Mixer channel strip, click the Effects Order button. The dropdown that opens lets you reshuffle the routing among every insert effect (Fairlight FX, or AU, or VST plugins) together with the built-in Dynamics and EQ modules. By default that routing is Effects (“FX”), Dynamics, EQ.

### Effects Order dropdown menu

Reordering effects can lead to markedly different creative outcomes. As a rule, for instance, it’s wise to put noise reduction at the head of a signal chain so you don’t alter the volume or character of the noise floor you mean to strip out, letting the plugin work at its best. You might likewise place dynamics processing ahead of EQ, since reshaping your source’s spectral content can change how the compressor reacts.

### Moving Inserts by Dragging

Relocating inserts is as easy as clicking and dragging one to a fresh spot. With this method you can carry an effect from one channel over to another, or shift or trade an effect’s place on a channel to a different insert slot on that same channel (bumping aside whatever plugin was already there). Keep in mind that, for now, the technique won’t copy tracks to busses or the other way around.
