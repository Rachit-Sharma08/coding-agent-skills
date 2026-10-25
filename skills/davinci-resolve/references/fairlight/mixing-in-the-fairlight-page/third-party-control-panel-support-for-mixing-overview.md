# Third party control panel support for mixing overview

Version: DaVinci Resolve 20.3 Reference Manual. Context: Mixing in the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](target-loudness-level-and-bouncing-audio.md)
<a id="source-third-party-control-panel-support-for-mixing"></a>

### Third-Party Control Panel Support for Mixing

Third-party mixing control panels that speak HUI and MCU and carry as many as eight faders — the Mackie MCU Pro Control Surface among them — work with DaVinci Resolve over USB MIDI and are chosen in the Control Panels panel of the Resolve System Preferences. As of this writing, the core panel controls that map to Fairlight functions cover the following. Transport controls including:

- Rewind (REW)
- Fast Forward (FF)
- Stop (double-press the Stop button for Home in the Timeline)
- Play (double-press the Play button to “play again”)
- Record (hitting Record+Play starts a take whenever at least one track has been armed for recording)
- Jog control (Press SCRUB and rotate the jog wheel)

Channel Strip controls including:

- Rotary controls for panning, with Rotary Value display and Rotary touch
- Alphanumeric Track Name display
- Record button to arm tracks for recording (functions solely once a source is patched into a track input)
- Solo, with a double-press selecting or de-selecting that track
- Mute
- Select to select the track corresponding to that channel strip
- Fader control and optional Level display
- Channel and Fader Bank buttons that step leftward and rightward through the available banks of channel strips
- Double-press the Fader Bank Left button, which sends the playhead to Home within the mixer (track 1)
- Double-press the Fader Bank Right, which jumps you over to the Master channel strips

Marker buttons:

- Marker to add a marker
- Pressing the Marker+Stop buttons sets Home
- Pressing the Marker+FF/REW buttons jumps the playhead forward or backward

Additional supported controls for control panels that have them include:

- Master Solo clear/restore
- Undo (pressing the Undo+Option buttons does Redo)
- Arrows to move the selection
- Zoom horizontal and vertical controls
- Audio Tracks, to turn Automation On/Off
- Write/Trim/Touch/Latch switches
- Nudge controls
- Cut, Copy, and Paste

Monitoring controls include:

- Level control
- Dim
- Mute
- Alt Speaker

To dig deeper into how third-party mixing control panels are supported, visit the Blackmagic Support site located at www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion.
