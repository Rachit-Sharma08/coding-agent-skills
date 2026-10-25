# Midi extractor and natural cubic spline and offset angle distance position

Version: DaVinci Resolve 20.3 Reference Manual. Context: Midi extractor, Natural cubic spline, Offset angle distance position.
[Chapter index](INDEX.md) / [Previous section](expression-image-gradient-key-stretcher-and-midi.md) / [Next section](offset-angle-distance-position-and-path.md) / [MIDI Extractor](expression-image-gradient-key-stretcher-and-midi.md)
<a id="source-about-midi"></a> <a id="source-channels-tab"></a> <a id="source-inspector-3"></a> <a id="source-midi-events"></a> <a id="source-midi-messages"></a> <a id="source-natural-cubic-spline"></a> <a id="source-natural-cubic-spline-editor"></a> <a id="source-offset-angle-distance-position"></a> <a id="source-offset-tab"></a> <a id="source-pitch-bend"></a> <a id="source-the-midi-extractor-modifier-channels-tab"></a> <a id="source-the-offset-position-modifier-controls"></a> <a id="source-the-offset-time-tab"></a> <a id="source-time-tab"></a> <a id="source-usage"></a>

### The MIDI Extractor modifier Channels tab

### Channels Tab

The Channels tab is where you pick which Channels the modifier draws on. Channels The Channels checkboxes pick which of the MIDI file's 16 channels actually count toward events. This is a handy way to pull one specific instrument out of an arrangement.

### About MIDI

One MIDI interface carries 16 channels. As a rule, these go to separate instruments inside one device or to separate devices. MIDI data is normally 7 bits, spanning 0–127. Fusion shows this as a value from 0–1, to stay in step with how Fusion handles data elsewhere. Plenty of distinct MIDI messages and events exist, but the ones that matter most with this modifier are spelled out below.

### MIDI Messages

Note On: This marks a note (on a given channel) coming on; it carries a pitch (0–127, where middle C is 60) and a Velocity (0–127, capturing how hard the key or strings or whatever got struck). Note Off: This marks a note (on a given channel) going off; it carries a pitch (0–127, where middle C is 60) and a Velocity (0–127, capturing how hard the key or strings or whatever got let go). Control Change: This message signals that some controller has moved. There are 128 controllers (0–127), each holding data from 0–127. Controllers set parameters like Volume, Pan, the amount of Reverb or Chorus, and general things such as foot controllers or breath controllers.

### MIDI Events

Channel Aftertouch: This event marks pressure landing on the keys (or strings or whatever) over the course of a note. It stands for the general, all-over pressure on this channel, so it just carries a pressure value (0–127). Poly Aftertouch: This event marks pressure landing on the keys (or strings or whatever) over the course of a note. It applies to each individual note, so along with a pressure value (0–127) it also carries a note number.

### Pitch Bend

What the Pitch Bend controller usually states is how much pitch bend or variation gets laid on the note. Since pitch bend values travel as 14-bit values, this control spans -1 to 1 and carries a correspondingly finer resolution.

### Natural Cubic Spline

The Natural Cubic Spline counts among Fusion's animation modifiers and is normally laid on numerical values rather than point values. You apply it by right-clicking a numerical control and picking Modify With > Natural Cubic Spline. NOTE: Cubic splines, unlike the other spline types, carry no control handles. They try on their own to draw a smooth curve passing through the control points.

### Usage

Because it's an animation spline, this modifier carries no real Controls tab. You can still see and shape its effect, though, within the Spline Editor.

### Natural Cubic Spline Editor

### Offset (Angle, Distance, Position)

There are three Offset modifiers for building differences between values. Which values those are — controls, paths, or points — depends on the modifier. Fusion's three kinds of Offset modifier are:

- Offset Angle
- Offset Distance
- Offset Position

Offset Angle The Offset Angle modifier puts out a value from 0 to 360 keyed to the angle separating two positional controls. The Position and Offset parameters can hold still, link to other positional parameters, or link to paths of their own. Every offset shares one set of controls, which act differently according to the offset type in use. Those controls get covered below. Offset Distance The Offset Distance modifier puts out a value keyed to the gap between two positional controls. This modifier can put out a value derived from a mathematical expression laid on a position. Offset Position The Offset Position modifier makes a position (X and Y coordinates) keyed to how positional controls relate. This modifier works like a calculation control, except it puts out X and Y coordinates in place of a value. You apply it by right-clicking a control and picking Modify With > Offset.

### Inspector

### The Offset Position modifier controls

### Offset Tab

All three Offset modifiers share the very same Inspector. The Offset tab carries Position and Offset values along with a Mode menu for choosing which mathematical operation the offset control runs. Position X and Y The X and Y values that Position feeds into the calculation. Offset X and Y The X and Y values that Offset feeds into the calculation. Flip Position Horizontal and Vertical Switch these on and the Position gets mirrored across the image's vertical or horizontal axis. Flip Offset Horizontal and Vertical Switch these on and the Offset position gets mirrored across the image's vertical or horizontal axis. Mode The Mode menu holds the mathematical operations the Offset control runs. The choices on offer are:

- Offset
- Difference (Position - Offset)
- Difference (Offset - Position)
- Average Use Position Only
- Use Offset Only
- Maximum
- Minimum Invert Position
- Invert Offset
- Invert Sugar
- Random Offset

Image Aspect Tunes the modifier's output to make up for the project's image aspect (not pixel aspect). A square 500 x 500 image takes an Image Aspect value of 1, while a rectangular 500 x 1000 image takes an Aspect Value of 2. The default always follows whatever frame format is currently picked in the preferences. Work out image aspect by dividing the width by the height. You can also bend this control to fake the look of aspect.

### Time Tab

### The Offset Time tab

Position Time Scale This hands back the Position's value at whatever Time Scale you name (0.5, say, gives its value at the halfway point of the present frame time). Position Time Offset This hands back the Position's value at whatever Time Offset you name (10, say, reaches 10 frames earlier). Offset Time Scale This hands back the Offset's value at the Time Scale you name. Offset Time Offset This hands back the Offset's value at the Time Offset you name.
