# Legacy fixed bus patching and a channel strips input menu

Version: DaVinci Resolve 20.3 Reference Manual. Context: Setting up tracks busses and patching.
[Chapter index](INDEX.md) / [Previous section](bus-assign-window-and-setting-signal-paths.md) / [Next section](legacy-bus-inputs-and-fairlight-presets.md)
<a id="source-bus"></a> <a id="source-direct-output"></a> <a id="source-input"></a> <a id="source-insert"></a> <a id="source-legacy-fixed-bus-patching"></a> <a id="source-path-settings"></a> <a id="source-record-level"></a> <a id="source-trim"></a> <a id="source-using-a-channel-strips-input-menu"></a>

### Legacy Fixed Bus Patching

Should you opt for the legacy Fixed Bussing under the Project Settings, the options show up somewhat differently. These Audio Source options exist:

- Audio Inputs: The physical audio inputs available on your workstation, for instance SX-36, MADI, or system audio. Handy while patching to record audio.
- Monitor Direct: Monitor system Direct Out. Sits after the fold up/down matrix yet ahead of the Monitor VolumeLevel/Dim/Mute.
- Monitor Out: Monitor system output. Sits after both the fold up/down matrix and the Monitor VolumeLevel/Dim/Mute.
- Main Direct: Main Bus Direct Out; available pre or post the Main bus master fader, carrying an offset.
- Main Out: Main Bus Out; always taken post the Main bus master fader.
- Main Send: Main bus master insert send.
- System Generator: Supplies assorted utility sources, with beeps and timecode generation included:

OSC: Supplies a test oscillator. The oscillator's controls appear in a floating window opened through Fairlight > Test Tone Settings. Noise: Draws on the Noise generator, where white or pink noise can be picked through Fairlight > Test Tone Settings. Beeps: Refers to those beeps that operations on the ADR panel generate, the controls for which are on the ADR setup page. Timecode generator: Creates timecode once enabled with the transport running, its controls offered in a floating window opened through Fairlight > Remote Control Settings.

- Track Direct: Track Direct Out; available pre or post the track fader, carrying an offset.
- Track Reproduction: This is the signal coming from track playback, ahead of any processing.
- Track Send: Track Insert send.

These Audio Destination options exist:

- Audio Outputs: The physical audio outputs available on your workstation. For instance, the Fairlight SX-36 audio interface, MADI, third party interfaces (USB or Thunderbolt, for example), or system audio. Handy while patching to play audio back to speakers or headphone systems.
- Main Return: Main Bus master insert return.
- Talk Back: The setup for patching the General Purpose Input and General Purpose Output for talkback.
- Track Input: The inputs of the available audio tracks within the current timeline, which feed the Record and Thru path.
- Track Return: Track insert return.
- Dolby Atmos Send: For original content you author, patch this one manually. If a Dolby Atmos master file is what you import instead, the Send patching covering the bed and object tracks is established for you. Once an external Dolby RMU renderer is active, whatever sources are patched onto these sends appear mirrored on the physical outputs running to the external renderer, in line with the base audio outputs defined in system preferences.

### Using a Channel Strip’s Input Menu

Atop each track's channel strip in the mixer, the Input dropdown menu offers a few shortcuts for patching assorted inputs and busses onto the tracks of your mix. Picking any option in this menu makes the Patch Input/Output window open with various Source and Destination selections already configured.

### Input

The Patch Input/Output window opens configured to let you patch assorted inputs (the system audio input, for example) onto the tracks of the timeline. That speeds up readying audio inputs ahead of recording.

### Bus

A shortcut that opens the Patch Input/Output window (covered earlier in this chapter) and lets you patch Bus Out or Bus Sends onto Timeline track channels.

### Path Settings

This brings up the Path Settings window for the track, holding controls that adjust the input level of audio signals arriving from an input/output device.

The Path Settings window presenting audio inputs together with track inputs Here are those parameters: Mic/Inst Controls surface on this panel solely once channels 1 or 2 of a Fairlight SX36 audio interface are hooked up to your system. When they're hooked up, every option (level included) for the SX36 mic/instrument inputs can be run remotely after they've been assigned to the channel. Lacking any connection to an SX36, this region stays empty.

### Record Level

- Record: A convenience duplicate of the channel strip's Record Enable button, tied to it directly. Pressing either one enables the other.
- Thru: Lets the input signal flow into the mixer without arming a record path. It's perfect when you'd like a source signal always on hand purely to monitor it.

TIP: That mixer channel can likewise be flipped into Thru mode by Command-clicking the Track Arm button, whether in the Mixer or the Track Header. The button turns green and shows a ’T’ inside it.

- Record Level: Lets you put a digital gain adjustment on the record path to disk, downstream of your audio interface's analog-to-digital converter. As a rule this control belongs at 0.0 (no change, unity gain), since it governs the level you're recording to disk. Best practice is steering the input level into DaVinci Resolve from your audio interface's level controls to keep audio fidelity high. Even so, a moment may come when you want a touch more level, or lack access to an audio interface's controls, and for those you can tweak the input.

### Trim

- Polarity: This button reverses the polarity of whatever signal arrives at the channel strip (a move sometimes dubbed “flipping the phase”). Picture an incoming signal such as an explosion, where the transient attack produces a strongly positive-going waveform (one that mostly rides above the zero line).

Flip the polarity and the signal turns mostly negative-going, the waveform gathering below the zero line. Polarity inversion is sometimes used to better line up signals from several microphones and can serve creatively to shape such a signal's frequency response.

- Trim Level: The Trim knob lets you tune the level of the signal arriving “off of disk” during playback so the feed into effects and the busses is optimized. It's useful for nudging an otherwise perfect element slightly up or down within your mix. Trim adjustments land post the recorded signal and Track FX (which work straight “off of disk”), and pre every other effect, leaving the recording level untouched.

### Direct Output

Every audio channel strip can switch on a direct output usable to feed any other input destination. To patch this source, reach for the Source dropdown of the Patch Input/Output dialog and select Track Direct there.

- On/Off: Turns the direct output on and off.
- Pre: Places the direct output tap-off point pre (before) the channel fader. On by default.
- Level Control: Sets the direct output level anywhere from minus infinity (fully off) up to +10 dB.

Default is 0.0 (unity gain).

For more information see Chapter 171, “Setting Up Tracks, Busses, and Patching.”

### Insert

A convenience duplicate of the channel strip's Effects In button, tied to it directly. Clicking either location enables its counterpart and flips every Fairlight FX, AU, or VST channel effect into or out of the signal path.
