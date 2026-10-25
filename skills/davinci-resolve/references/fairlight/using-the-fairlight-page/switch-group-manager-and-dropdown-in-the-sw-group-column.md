# Switch group manager and dropdown in the sw group column

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](mpeg-h-options-in-the-tracks-panel-overview.md) / [Next section](timecode-and-fairlight-synchronization-settings.md)
<a id="source-clip-mode-vs-track-mode"></a> <a id="source-fairlight-page---inspector---audio-tab"></a> <a id="source-inspector"></a> <a id="source-markers"></a> <a id="source-test-tone-settings-for-generating-tone-noise-and-beeps"></a> <a id="source-the-audio-tab"></a> <a id="source-the-dropdown-in-the-presets-column"></a> <a id="source-the-dropdown-in-the-sw-group-column"></a> <a id="source-the-effects-tab"></a> <a id="source-the-file-tab"></a> <a id="source-the-preset-group-manager"></a> <a id="source-the-switch-group-manager"></a>

### The Switch Group Manager

After at least one group exists, it becomes selectable from the dropdown of any cell within the SW Groups column. From here you can rapidly set up an assortment of bespoke assignments.

### The dropdown in the SW Group column

- Presets: Lets a track be placed into a preset that you define. As an example, one preset might be built from a Bed Mix and Language switch group, while another might pair those same tracks with a spoken subtitle. To establish a Preset, click the relevant cell in that track's Presets column and pick “Presets…” to bring up the Preset Manager window, where new Presets get created.

### The Preset Group Manager

After at least one preset exists, it can be switched on from the dropdown of any cell within the SW Groups column. Since a single track may belong to several presets, the Presets dropdown holds one checkbox for each preset, letting you assign more than one at a time.

### The dropdown in the Presets column

After everything's set, the metadata carried by these presets shapes how the content gets exported into the finished deliverable, leaving you with a collection of presets that hold every configured component and switch group.

### Markers

You can show the markers panel as thumbnails or as a list. In thumbnail mode, every marker on your timeline maps to a thumbnail that shows the timecode of where it sits beneath it, with the marker's color placed just left of that timecode spot. In list view, each marker occupies a row that carries these details: marker number, then frame (rendered as a thumbnail), followed by marker name, plus start timecode, end timecode, duration, marker color, along with notes. For each marker present in the Timeline, the Markers panel lays out a single row of such information.

### Inspector

On the Fairlight page, the Inspector's Audio, Effects, and File panels give you tools for handling selected tracks, buses, and clips on the Audio Timeline. TIP: For finer, “granular” control over virtual sliders, keep the Option or Shift key pressed as you click into the numerical value field and drag it to the left or the right.

### Fairlight page - Inspector - Audio tab

### The Audio Tab

Use the Audio tab to set a chosen track's volume level and to apply and tweak Track FX. With audio clips on the Audio Timeline or in the Media Pool, you can set a chosen clip's volume level and pan, apply and tweak a range of Fairlight FX and EQ, and shift the clip's pitch up or down.

### The Effects Tab

This panel surfaces any Audio Effects you've placed on a track or bus by way of the Effects section on its Mixer channel strip, as well as those dropped onto a Timeline clip from the Effects Library.

### The File Tab

Use this panel to inspect and change the metadata and configuration of chosen Timeline or Media Pool clips. To go deeper on the Fairlight page's Inspector, refer to Chapter 176, “The Fairlight Inspector.”

### Clip Mode vs. Track Mode

A Clip Mode and a Track Mode button live in the Inspector so there's no doubt over whether your parameter-property edits in the Audio tab land on an audio clip or on a track.

The Clip Mode button (circled)

The Track Mode button (circled)

- When you select an audio clip in the Media Pool or on the Timeline, the Clip Mode button lights up and the clip's name shows at the top of the Inspector, just right of the Track Mode button.
- Pressing the Track Mode button while a Timeline clip is selected makes any further Audio tab edits apply to the matching Mixer channel. At that point the name shown at the top of the Inspector changes from the clip name to the track name.

To dig further into the Fairlight Page Inspector, turn to Chapter 176, “The Fairlight Inspector.”

### Test Tone Settings for Generating Tone, Noise, and Beeps

An all-purpose oscillator lives on the Fairlight page, and you tailor its settings by selecting Fairlight > Test Tones Settings. Doing so brings up the Test Tones Settings window, which you set up to produce tones, noise, or beeps by means of five sets of controls:

- Enable/Disable Test Tones toggle: Switches the Oscillator on or off across the whole system.
- Frequency control: Dials in a custom oscillating-tone frequency anywhere from 20 Hz to 15kHz.

Defaults to 1kHz.

- Frequency buttons: Let you jump straight to 100, 440, 1K, or 2K preset tones, or to a steadily climbing

sweep running from 20 Hz to 15kHz.

- Noise type buttons: A pair of buttons lets you pick between White noise and Pink noise.
- Level dial: Sets how loud the tone or noise comes out, spanning –50dB to +10dB. Defaults to –15 dB.

The Oscillator can be configured to put out whatever tone or noise you need, after which you patch it onto tracks to record tones, or onto audio outputs to calibrate speakers. The beep options of the ADR panel, if you use them, run through the Oscillator as well. To route the Test Tone out to your speakers: 1 Pick Fairlight > Patch Input/Output, which brings up the Patch Input/Output window. 2 Under the Source dropdown menu pick System Generator, and under the Destination dropdown menu pick Audio Outputs. 3 Over on the left side, press the button for what you intend to send out — Osc (Oscillator) or Noise. 4 Over on the right side, press the wired audio outputs you'd like to route into, and press Patch. Almost at once the tone or noise should start coming from your configured speakers. Depending on the I/O settings of the particular track, when the Osc is patched through a track you may need to Arm the track via the R (record) button, or hit the Thru button under the channel's Path Settings, letting the signal pass through for output monitoring. 5 To stop, select any one of the patched buttons and press Un-Patch. To lay down a tone or noise from the Oscillator onto an audio track: 1 Pick Fairlight > Patch Input/Output, which brings up the Patch Input/Output window. 2 Under the Source dropdown menu pick System Generator, and under the Destination dropdown menu pick Track Input. 3 Over on the left side, press the button for what you intend to send out — Osc (Oscillator) or Noise. 4 Over on the right side, press the wired audio outputs you'd like to route into, and press Patch. Shut the Patch Input/Output window. 5 Press the Arm Record (R) button on the track header belonging to whichever track the Oscillator was patched onto. Assuming your Main has been patched correctly through to your outputs, the tone or noise will be audible, and that track's audio meter ought to show the level the Oscillator is putting out. 6 On the transport controls, press the Record button to begin laying that tone down onto the patched track. Once you're done, press the Stop button or hit the Spacebar to finish recording.
