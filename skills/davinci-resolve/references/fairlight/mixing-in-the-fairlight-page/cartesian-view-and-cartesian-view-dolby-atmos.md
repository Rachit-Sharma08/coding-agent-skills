# Cartesian view and cartesian view dolby atmos

Version: DaVinci Resolve 20.3 Reference Manual. Context: Mixing in the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](boom-parameter-and-spherical-view.md) / [Next section](bus-assignment-buttons-and-legacy-mixer-bus-assignment.md)
<a id="source-cartesian-view"></a> <a id="source-cartesian-view--dolby-atmos"></a> <a id="source-spherical-view-1"></a> <a id="source-the-3d-spherical-panner-control-window"></a>

### Cartesian View

The 3D Panner control window - Default Cartesian view A click on the 3D button moves the Panner interface into the default Cartesian view, which carries a handful more controls than the 2D Pan window:

- Pan enable: Toggles the Panner on and off.
- Snap: This button flips Speaker Snap mode on and off for a given object. As playback runs,

Speaker Snap mode shifts an audio object to whichever active speaker sits nearest its set location, heading off problems like phantom panning.

- Panner viewer: A sizable 3D depiction of the virtual room, in which a blue sphere marks where the track’s audio sits.

Perspective Buttons: With these buttons you view the room from a range of preset angles. To spin it freely, hold Command-Option-Shift (Ctrl + Alt + Shift in Windows) as you drag. Clicking any one of the perspective buttons brings you back to a default view.

- Front panner: A 2D panning control letting you adjust along both the horizontal Left/Right axis and the vertical Down/Up axis.
- Side panner: A 2D panning control letting you adjust along both the horizontal Front/Back axis and the vertical Down/Up axis.
- Top panner: A 2D panning control standing in for the horizontal left/right axis and the vertical front/ back axis, with which you make these particular spatial adjustments.
- Left/Right: Shifts the signal’s balance between the left and right speakers, according to whichever speaker configuration you’re mixing for.
- Front/Back: Lets you tune the signal’s balance between the front and rear speakers given the surround format you are mixing in.
- Down/Up: With this you reposition a sound source along the vertical axis.
- Height Mode Presets: Sitting to the right of the Down/Up control, these three height presets

bind the Front/Back and Down/Up parameters to act together, supplying fixed panning paths that lift a sound source’s height to its peak (100U) while carrying it from one edge of the sound field to the other. Freeform: The default for this section, it lets you set the Down/Up and Front/ Back controls on their own.

Flyover: Sends the sound source up in a steep arc to 100U, then across from one edge of the sound field to the other while holding peak height. Triangular: This preset takes the source diagonally up to 100U and straight back down again as it crosses from one edge of the sound field to the other. Arc: Lifts the sound source up in an arc to 100U and brings it straight back down the same way as it crosses from one edge of the sound field to the other.

- Rotate: This controller spins the sound source or mix around the listening position at the heart of the sound field.
- Tilt: This knob tips a sound source or mix as much as ninety degrees to either side so it vertically rotates or “swings” around the listening position at the heart of the sound field.
- Spread: With multichannel audio, this sets the spread or distance separating the sound sources. It’s gauged on a numeric scale of 1-99, on which 1 carries the label PNT (“Point”) and 99 carries the label FULL.
- Divergence: Sets how much signal bleed or spillover passes from one speaker into the loudspeakers beside it, letting the sound fill more of the sound field with less concentration on a single speaker position. That signal bleed appears as green horizontal lines running out from both sides of each speaker position, growing longer as you push the parameter value up.

2D: A click on this button turns the divergence indicators into circles.

- Boom: This sets the send level into the LFE portion of the mix (the Low-Frequency Extension subwoofer system).

On: Switches the Boom output on. Pre: Sends the LFE signal pre-fader. Only: Permits the panner to emit nothing but an LFE signal off the channel. While this button stays active, the Boom level line within the channel strip Pan Indicator turns gray.

### Cartesian View — Dolby Atmos

The 3D Panner control window - Cartesian view – Dolby Atmos While you work within a Dolby Atmos workflow, the 3D Cartesian view of the Panner carries every feature listed above for the default Cartesian view, plus these additional controls placed along the top of the interface:

NOTE: These controls are not available on Dolby Atmos busses.

- Elevation Button: This button conceals and reveals the four top speakers within the Viewer.
- Zone: On top of the option to view all speakers, this dropdown menu presents five more that let

you bring certain speakers into this object’s mix or leave them out: No Back: Conceals the rear surround speakers. No Sides: Conceals the side surround speakers. Center Back: Displays only the Center and Rear speakers. Screen Only: Displays only the Center and Left and Right Front speakers. Surr (Surround) Only: Displays only the Surround speakers.

### Spherical View

### The 3D Spherical Panner control window

With the 3D Spherical Panner you place your source anywhere across the sound field, the listener’s top and bottom included. Spherical panning rests on Azimuth, Elevation, and Distance. This view of the 3D panner supplies these controls:

- Azimuth: This control spins the sound source around the sphere’s circumference.
- Elevation: This lifts and lowers the sound source toward the sphere’s top and bottom,

so you can set it above or below the listener if you like.

- Distance: This control sets how far the signal source sits from the listening position at

the sphere’s center.

- Rotate: Spins the sound source (or sources) around the listening position at the heart of the

sound field.

- Spread: This control sets the spread or distance separating the sound sources. It’s gauged

on a numeric scale of 1-99, on which 1 carries the label PNT (“Point”) and 99 carries the label FULL.

- Size: As of this writing, this parameter isn’t active.
- Room: As of this writing, this parameter isn’t active.
- Pitch: This knob tips the sound source or mix forward or backward while spinning or “swinging” it as much as ninety degrees around the central listening position.
- Roll: This knob tips a sound source or mix as much as ninety degrees to either side so it vertically rotates or “swings” around the central listening position.
- Panner viewer: A sizable 3D depiction of the spherical sound field, in which a blue sphere marks where the track’s audio sits.
- Perspective Buttons: With these buttons you view the Sphere from a range of preset angles. To spin it freely, hold Command-Option-Shift (Ctrl + Alt + Shift in Windows) as you drag. Clicking any one of the perspective buttons brings you back to a default view.
