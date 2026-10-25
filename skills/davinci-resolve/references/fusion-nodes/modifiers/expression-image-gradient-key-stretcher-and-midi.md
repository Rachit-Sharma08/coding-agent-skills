# Expression and from image and gradient color and key stretcher modifier and midi extractor

Version: DaVinci Resolve 20.3 Reference Manual. Context: Expression, From image, Gradient color, Key stretcher modifier, Midi extractor.
[Chapter index](INDEX.md) / [Previous section](expression-modifier-formula-names-and-descriptions.md) / [Next section](midi-spline-and-position-modifiers.md) / [Expression](custom-poly-and-expression.md)
<a id="source-controls-tab"></a> <a id="source-controls-tab-1"></a> <a id="source-controls-tab-2"></a> <a id="source-example"></a> <a id="source-expression-syntax-operators"></a> <a id="source-from-image"></a> <a id="source-from-image-modifier"></a> <a id="source-gradient-color"></a> <a id="source-inspector"></a> <a id="source-inspector-1"></a> <a id="source-inspector-2"></a> <a id="source-key-stretcher-modifier"></a> <a id="source-midi-extractor"></a> <a id="source-the-gradient-modifier-controls-tab"></a> <a id="source-the-midi-extractor-modifier-controls-tab"></a>

### Expression Syntax Operators

You lean on operators to work out statements. Pair them with functions, and you can carry out logical and mathematical work inside the Number Out and Point Out tabs.

x+y x-y x>=y x>y !x -x +x x^y xy xy x%y x>=y x>=y x=y x == y x<>y x != y x&y x && y x|y x || y

x and y summed. x with y subtracted. Yields 1.0 when x falls below y, else 0.0. Yields 1.0 when x exceeds y, else 0.0. Yields 1.0 when x = 0, else 0.0. (0.0 - x). (0.0 + x) (which changes nothing in practice). x taken to the power y. x times y. x over y. x mod y, that is the remainder left after (x divided by y). Yields 1.0 when x is at most y, else 0.0. Yields 1.0 when x is at least y, else 0.0. Yields 1.0 when x equals y precisely, else 0.0. Yields 1.0 when x equals y precisely, else 0.0 (same as the previous one). Yields 1.0 when x differs from y, else 0.0. Yields 1.0 when x differs from y, else 0.0 (same as the previous one). Yields 1.0 when neither x nor y is 0.0, else 0.0. Yields 1.0 when neither x nor y is 0.0, else 0.0 (same as the previous one). Yields 1.0 when at least one of x or y isn't 0.0, else 0.0. Yields 1.0 when at least one of x or y isn't 0.0, else 0.0 (same as the previous one).

Example 1 To tie a numeric control to a motion path's Y value, attach an expression to whichever control you're targeting and wire the Path into Point In 1. Type the formula p1y into the Number Out field. Example 2 So that the Expression's Number Out gives back the greater of Number In 1 and Number In 2, scaled by the cosine of Number In 3, plus Point In 1's X coordinate, drop the formula max(n1, n2) * cos(n3) + p1x straight into Number Out. Example 3 Add a Background node that's solid black alongside a Hotspot node. Set its Hotspot size at 0.08 and crank the Strength to the top. Drive the Hotspot center with an expression. Move the current frame to 0. Park n1 at 0.0 and add a Bézier Spline. At frame 29, raise the value of n1 up to 1.0. Select both points, then loop that spline via the Spline Editor. Now feed these equations into the expression's Point Out tab. For the X-Axis Expression put `n1`, and for the Y-Axis Expression put `0.5 + sin(time*50)`. 4 Render a quick preview and have a look at how it came out. (Worth trying this one with motion blur switched on.)

### From Image

The From Image modifier acts only on gradients — the sort of gradient sitting on a Background node, say. It reads samples off an image along a line you lay out yourself and builds a gradient out of those samples. From Image differs from the other modifiers in that you won't find it in the Modify With menu. You apply this modifier by right-clicking a Gradient bar in the Inspector and picking From Image.

### Inspector

### From Image modifier

### Controls Tab

You use the From Image controls tab in the Inspector to choose which node holds the image you mean to sample. There you set where the line begins and ends in the image, plus how many color samples build the gradient. Image to Scan Drag the node you want color-sampled out of the Node Editor and into this box. Start X/Y, End X/Y This pair of point controls fixes the Start and End of the line that the samples are drawn along, from whatever image you named in the Image to Scan box. You can also shift the points right in the viewer. Number of Sample Steps This sets how many separate color samples get taken across the line. The effect of this setting is also visible if you check the node's own Gradient control. Define more sample steps here, and more individual color stops show up on the Gradient control. You can even build a gradient with the From Image modifier first and then strip that modifier back off the Gradient control. The gradient you built survives intact and is then open to manual fine-tuning. Edges Edges governs what happens at the image's edges once the sample line runs past the actual frame of the image being sampled. Black This sends out black at every spot on the sample line that sits beyond the image bounds. Wrap This loops the line's edges around the image's borders. Duplicate This makes the image's edges repeat as faithfully as it can, extending the image past its native size. Color This puts out a color of your choosing rather than black at every spot on the sample line lying beyond the image bounds.

### Example

On the left, the source image displays the color selection line in red. On the right, the image shows the gradient that selection produced.

### Gradient Color

With the Gradient Color modifier you build a gradient of your own and map it across a chosen time range so it drives a value. Set the animation's frames with the Start and End time controls. When both the Start and End time values sit at 0, the modifier hands back the value at the gradient's starting point. The Offset control lets you animate the gradient by hand. You apply it by right-clicking a parameter and picking Modify With > Gradient Color.

### Inspector

### The Gradient modifier Controls tab

### Controls Tab

A Gradient bar makes up the Controls tab, and that's where you add and tune the gradient's points. The Start Time and End Time thumbwheels down at the foot of the Inspector set which time range the gradient maps into. Gradient The Gradient control is a bar on which you can add, change, and delete the gradient's points. Every point carries its own color. Both that color and the point's position can be animated. On top of that, a From Image modifier can be hung on the gradient so it's read out of an image. Gradient Interpolation Method By default the gradient runs a straight linear interpolation from one point to the next within RGB color space. Now and then that throws up colors you didn't want. Picking a different color space may give a nicer outcome. Repeat Sets how the gradient's left and right borders behave.

From top down, gradients on Once, Repeat, and Ping Pong respectively, with the gradient pushed leftward.

- Once: As you shift the gradient with the Gradient Offset control, the border colors hold their values. Pushing the default gradient left gives a white border on the left; pushing it right gives a black border on the right.
- Repeat: As you shift the gradient with the Gradient Offset control, the border colors loop around. Pushing the default gradient left makes a hard jump from white to black; pushing it right makes a hard jump from black to white.
- Ping Pong: As you shift the gradient with the Gradient Offset control, the border colors bounce to and fro. Pushing the default gradient left has the edge fade from white back into black; pushing it right has the edge fade from black back into white.

Gradient Offset Lets you scroll across the gradient. Time Controls The Start Time and End Time thumbwheels set which time range the gradient maps into. You give this in frames. You can reach the same result by putting the Gradient on Once and animating the offset thumbwheel.

### Key Stretcher Modifier

The Keyframe Stretcher modifier mainly comes into play while you're building title templates in Fusion meant for DaVinci Resolve's Edit page or Cut page. You attach the Keyframe Stretcher modifier to an animated parameter, so that parameter's keyframes stretch whenever the template gets trimmed on the Timeline. You apply it by right-clicking a parameter and picking Modify with > KeyStretcher. For fuller detail on the Keyframe Stretcher Modifier controls, turn to "Keyframe Stretcher" — that's "Miscellaneous Nodes," Chapter 111 of the DaVinci Resolve Reference Manual, or Chapter 51 over in the Fusion Reference Manual.

### MIDI Extractor

The MIDI Extractor modifier lets you drive a control's value off the data held inside a MIDI file. Using it assumes a bit of MIDI know-how, which this manual won't cover. The value the modifier puts out is pulled from whatever MIDI event you pick in the Mode menu. You can trim each mode so it only processes certain messages for that event — say, processing some notes while skipping others. Extra factors such as Scale, Velocity, Attack, and Decay can scale or reshape that value further. You apply it by right-clicking a parameter and picking Modify With > MIDI Extractor.

### Inspector

### The MIDI Extractor modifier Controls tab

### Controls Tab

You use the Controls tab to load the MIDI file, reshape its timing, and decide which MIDI messages and events drive changes in the Fusion parameter. MIDI File This browser control points to the MIDI file fed into the modifier as its input. Time Scale Time Scale sets the ratio between time the way the MIDI file states it and time the way Fusion states it. At 1.0 the MIDI events run at ordinary speed, at 2.0 they run twice as fast, and so on. Time Offset Time Offset tunes the sync between the MIDI file's timing and Fusion's timing. Should there be an unexpected lag, or should the MIDI file need to begin partway into or ahead of some animation in Fusion, this control can shift the MIDI data however you need.

Result Offset, Result Scale These sliders set the span of values the modifier puts out. By default it generates values from 0 to 1 (or -1 to 1 when in PitchBend mode). That won't always fit the node/parameter, and scale can widen the span (for instance \* 0.0 - 2.0). Offset supplies a fixed value to sit on as a base. Result Curve The Result Curve is another way to shape the output. What it changes, though, is the curve of the result. By default, whatever MIDI data comes in, the results land linearly from 0.1 to 1.0 (so a velocity 127 note gives 1.0, while 63 gives roughly 0.5). The Result Curve lays a gamma-like curve over things so the middle values can yield higher or lower results without losing the full scale. Mode This menu offers Beat, Note, Control Change, Poly AfterTouch, Channel AfterTouch, or Pitch Bend, marking which MIDI event the values get read from. Beat mode stands a little apart in that it puts out steady pulses keyed to the MIDI file's tempo (any tempo maps included). The Beat mode draws on no particular messages; it times its events off the tempo map held in the MIDI file. Combine Events This menu decides what to do when several events land at once. That comes up readily in Notes mode. With other events, it comes up if Multiple Channels are picked. Use it to take the result from the latest event to fire, the oldest one still going, the highest- or lowest-valued event, or the average, sum, or median of every event happening just then. Beat (Quarters) (Beat Mode Only) This sets how frequently a beat lands while in Beat mode. It's stated in quarter notes, so 1.0 gives one beat per quarter. Note Range (Note and Poly Aftertouch Modes Only) This sets which span of notes will produce a value. For instance, isolate the kick drum out of a GM drum track by putting the note range at 35–36. Pitch Scale (Note Mode Only) Pitch Scale sets how strongly the result shifts with pitch. At 1.0 the result ranges across 0.0 to 1.0 over the whole span. Velocity Scale (Note Mode Only) This sets how strongly the result shifts with velocity. At 1.0 the result ranges across 0.0 to 1.0 over the whole span. It gets added onto the Pitch Scale result to form the final result. Control Number (Control Change Mode Only) This names the MIDI controller number that events are pulled from. Envelope Controls (Note and Beat Modes Only) These map out an Envelope that values follow leading up to, throughout, and trailing each note or beat. Pre-Attack Time sets how far ahead of the event it begins ramping up toward the pre-attack level. Attack is the Time/ Level it ramps to once the event has fired, then comes the Decay ramp and Sustain, lasting until the event ends. That stage applies to Notes alone. Beats last no time at all, so it jumps straight to

Release. Release is how long it takes to ramp down after the event wraps up. For a Beat, give Release some value or there probably won't be much beat to hear. You can use these values to trail the real sounds in the MIDI sequence, or simply to spin up interesting effects. Every time value in the MIDI Extractor is given in seconds.
