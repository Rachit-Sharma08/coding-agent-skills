# Band 1 controls active and band 6 controls active

Version: DaVinci Resolve 20.3 Reference Manual. Context: Mixing in the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](compressor-and-hard-and-soft-knee-graphs.md) / [Next section](uses-for-pre-fader-routing-and-legacy-bus-sends-auxiliaries.md)
<a id="source-accessing-the-bus-sends-window"></a> <a id="source-band-1-controls-active"></a> <a id="source-band-6-controls-active"></a> <a id="source-bands-2--5"></a> <a id="source-bus-send-window-controls"></a> <a id="source-bus-sends"></a> <a id="source-creating-sends"></a> <a id="source-the-band-3-controls"></a>

### Band 1 controls active

### Band 6 controls active

- Band filter type: A click on the Band 1 or Band 6 button turns its corresponding controls on or off.
- Band filter type: Off by default, Bands 1 and 6, once active, each open up the filtering options shown below:

On Band 1 the choices are Low Shelf, Bell, High Shelf, and High Pass. For Band 6 you instead get Low Pass, Low Shelf, Bell, and High Shelf.

- Frequency: Adjusts the center frequency of the EQ band.
- Filter Slope: For the high and low pass filters, selectable slopes begin at 6dB/octave

and reach 24dB/octave.

- Gain: With bands 1 and 6 set to a bell or shelving response curve, this parameter trims or

lifts the chosen frequency over a ±20 dB range.

### Bands 2 – 5

On by default, these band controls let you make a range of EQ adjustments..

### The Band 3 controls

- Band enable button: A click on these Band buttons turns their corresponding controls on or off.
- Band filter type: The filtering options on Bands 2 to 5 are Low Shelf, Peaking, Notch, and High Shelf.
- Frequency: Adjusts the center frequency of the EQ adjustment.
- L, ML, MH, H Buttons: A band's center frequency can be confined by these buttons to one of these

frequency ranges: Low, Medium Low, Medium High, or High.

- Gain: Active once a band uses a bell or shelving response curve, this control sets

the center frequency's level over a ±20 dB range.

- Q Factor: Available when a band uses a bell response, or when the Equalizer

type is Fire, this parameter sets an EQ band's bandwidth across a range of .3 to 10.3. Lower Q factors broaden the bandwidth and higher ones tighten it, deciding the degree to which adjacent frequencies are affected as the center frequency moves.

### Bus Sends

A channel strip's source signals can be routed to a bus destination through Bus Sends, with control over level, pan, mute, and pre/post fader routing. Bus sends can be set up on channels feeding any bus destination you have made. A few common mixing jobs that sends are handy for:

- Submixing: For instance, rendering distinct mixed outputs in different formats at once, such as stereo, 5.1 surround, or Dolby Atmos.
- Feeding signals to a shared effect: For instance, routing to a reverb plugin, where post fader sends from several mixer channels supply, in differing amounts, a reverb sitting on a bus channel strip.
- Headphone cue mixes: Build separate pre-fader mixes for the talent without altering what you hear on your own main monitor speakers.

### Creating Sends

To make a Bus Send and reach its controls:

- In the Mixer's Bus Sends area, click the assign button marked with the plus sign (+).
- A dropdown listing the available busses appears; pick one to assign.
- Your send is now created.

Hovering over the rectangular name button gives you a disable/bypass button, an access icon that opens the Bus Send window for the channel, and an "x" for deleting the send. A tooltip appears displaying the send bus name.

Hovering over the rectangular name button will show send controls.

### Accessing the Bus Sends Window

To manage a channel's sends, open the Bus Sends window by clicking the center of the name button.

### Bus Send window controls

In the Bus Send window, each Bus Send you make presents these controls:

- On: Turns the send on or off.
- Pre: Toggles the send between pre- and post-fader routing. Turning this button on lets

that track feed levels to the destination bus ahead of any level adjustments made on the track itself.

- Send Level: Sets how much signal travels from the chosen feed into the send bus, over a span of OFF to +10dB.
- Pan: Provides panning across Bus Send destinations.
