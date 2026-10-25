# Uses for pre fader routing and legacy bus sends auxiliaries

Version: DaVinci Resolve 20.3 Reference Manual. Context: Mixing in the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](band-1-controls-active-and-band-6-controls-active.md) / [Next section](boom-parameter-and-spherical-view.md)
<a id="source-2d-panner-controls"></a> <a id="source-channel-strip-pan-controls"></a> <a id="source-default-view"></a> <a id="source-legacy-bus-sends--auxiliaries"></a> <a id="source-mixing-in-the-fairlight-page-part-3"></a> <a id="source-pan"></a> <a id="source-the-panner-control-window--default-2d-view"></a> <a id="source-uses-for-pre-fader-routing"></a>

### Uses for Pre-fader Routing

A frequent application of pre-fader sends is cue mixes for ADR or voice over talent, when the performer wants to monitor a mix completely different from the control room mix. With pre-fader sends and a full mix built to a bus that feeds the headphone system, you get a mix that stands entirely on its own. Pre-fader sends also suit special creative effects, such as routing a dialogue channel to a reverb plugin through a send. If that send is pre-fader, then when the main channel fader is pulled down near zero, the dialogue keeps feeding the reverb, so it sounds extremely reverberant (nearly all of the signal is "wet"). Slowly bringing the channel fader up makes the voice seem to approach the listener, shifting the reverb balance toward a more present sound. Bus send levels show in the rectangles for each send and carry the color codes assigned to the destination busses.

Bus Send levels shown on the Mixer channel strip

### Legacy Bus Sends – "Auxiliaries"

Before DaVinci Resolve 17, the Bus Send panel went by the name Auxiliaries. Any project made before DaVinci Resolve 17 will use the legacy Fixed Busing. The sole distinction between the two is that "Aux" stands in for sends throughout the windows and titles.

### Pan

The Fairlight Mixer supplies 2D and 3D pan controls covering a range of audio formats, from mono and stereo through standard 5.1 and 7.1 surround, and on to sophisticated immersive formats like Dolby Atmos, Ambisonics, Auro 3D, and NHK 22.2.

### Channel Strip Pan Controls

Within each Channel Strip, the Pan section holds a Panning Indicator that gives you visualization and panning control over left, right, front, and back. While double-clicking the Panning indicator opens the Panner for extra parameters, you can also do the following directly in the channel strip Pan section with the Panner closed:

Drag inside the Pan Indicator to set the basic panning position.

- Single click to bypass panning.
- Command-drag to adjust the width on multichannel tracks.
- Check the Boom level on surround channels, shown as a horizontal blue line near

the foot of the Panning Indicator.

Channel strip Pan Indicator for a stereo track

### 2D Panner Controls

### Default View

How the source audio is mapped determines which controls appear in the Pan window. You can pan either by dragging the icons in the Panner Viewer or by using the controls down the left side of the window.

### The Panner control window – Default 2D view

In its default 2D form, the Audio Pan window presents these controls:

- Pan Enable: Turns the Panner on and off.
- Spherical: This button shifts the Panner interface away from the default 2D view and into the 2D Spherical top-down view.
- 3D: A click on this button moves the interface into the 3D Cartesian view, which supplies controls for handling immersive audio formats like Dolby Atmos, Ambisonics, Auro 3D, and NHK 22.2, covered in the 3D Pan Controls section below.

When you click both the Spherical and 3D buttons, the interface moves into the 3D Spherical view.

- Left/Right: Shifts the signal’s balance between the left and right speakers, according to whichever speaker configuration you’re mixing for.
- Front/Back: Lets you tune the signal’s balance between the front and rear speakers given the surround format you’re mixing in.
- Rotate: This controller spins the sound source (or sources) around the listening position at the heart of the sound field.
- Spread: With multichannel audio, this sets the spread or distance separating the sound sources. It’s gauged on a numeric scale of 1-99, on which 1 carries the label PNT (“Point”) and 99 carries the label FULL.
- Divergence: Sets how much signal bleed or spillover passes from one speaker into the loudspeakers beside it, letting the sound fill more of the sound field with less concentration on a single speaker position. That signal bleed appears as green horizontal lines running out from both sides of each speaker position, growing longer as you push the parameter value up.

2D: A click on this button turns the divergence indicators into circles.

- Boom: This sets the send level into the LFE portion of the mix (the Low-Frequency Extension subwoofer system).

On: Switches the Boom output on. Pre: Sends the LFE signal pre-fader.
