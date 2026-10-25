# Perturb and probe and publish and resolve parameter and shake

Version: DaVinci Resolve 20.3 Reference Manual. Context: Perturb, Probe, Publish, Resolve parameter, Shake.
[Chapter index](INDEX.md) / [Previous section](perturb.md) / [Next section](shake-and-track-and-vector-result.md) / [Perturb](perturb.md)
<a id="source-controls-tab"></a> <a id="source-controls-tab-1"></a> <a id="source-controls-tab-2"></a> <a id="source-inspector"></a> <a id="source-inspector-1"></a> <a id="source-probe"></a> <a id="source-publish"></a> <a id="source-resolve-parameter"></a> <a id="source-shake"></a> <a id="source-the-perturb-modifier-controls-tab"></a> <a id="source-the-perturb-modifier-gradient-controls"></a> <a id="source-the-probe-modifier-controls-tab"></a> <a id="source-the-probe-modifier-value-tab"></a> <a id="source-the-publish-modifier-controls-tab"></a> <a id="source-value-tab"></a>

### Inspector

### The Perturb modifier Controls tab

### Controls Tab

For Perturb, the Controls tab mostly handles the Strength, Wobble, and Speed parameters of the random jitter. Value Whatever this control holds hinges on the type of control the modifier was placed on. Should the Perturb modifier have gone onto a basic Slider control, the Value appears as a slider. Should it have gone onto a Gradient control, a Gradient control shows here instead. Use it to fix the default, or center, value the Perturb modifier acts on.

### The Perturb modifier Gradient controls

Jaggedness (Polylines and meshes only) This lets you raise how much variation runs along the length of the polyline or mesh, as opposed to over time. A higher Jaggedness yields a squigglier polyline or a more tangled mesh, separate from its movement. Phase (Polylines and meshes only) Animating this can shift the ripple of a polyline or mesh along its own length, from one end to the other. The effect reads most plainly when Speed sits at 0.0. Random Seed Randomize The Random Seed serves to “seed” how much jitter the modifier applies. Two Perturb modifiers sharing identical settings but holding different random seeds turn out two utterly different results. Click the Randomize button to drop in a random seed value. Strength This control tunes the strength of the Perturb modifier's output, that is, its largest deviation from the primary value set above. Wobble The Wobble control dictates how smooth the resulting values come out. Less wobble means a smoother handoff between values, whereas more wobble yields less predictable results. Speed Raising the Speed slider value quickens the rate at which the value shifts. It can heighten the apparent wobbliness more predictably than the Wobble control does, lending the jitter a more frantic or languorous character.

### Probe

The Probe modifier ranks among the most versatile modifiers in Fusion. It lets you steer any numeric parameter by the color or luminosity of a particular pixel or rectangular patch of an image. Picture driving the Brightness node off the pixel values of flickering lights in a shot, or gauging graded LUTs to compare values. You apply it by right-clicking a parameter and picking Modify With > Probe.

### Inspector

### The Probe modifier Controls tab

### Controls Tab

For the Probe modifier, the Controls tab lets you choose the node to probe, set the channel that drives the parameter, and govern how big the probed patch is. Image to Probe Drag a node out of the Node Editor into this field to name the image to probe. Channel Pick the channel you'd like to probe. The usual choices run:

- Red
- Green
- Blue
- Alpha

Luma With a Probe modifier sitting somewhere in your comp, you can wire other nodes' values to its outputs too. The Probe lets you tap into its values one by one:

- Result
- Red
- Green
- Blue
- Alpha

Position X Y Where in the image the probe draws its samples from. Probe Rectangle Out of the box, the Probe reads only the value of a single pixel at its position. Switch on the Probe Rectangle mode and you can sample across a wider patch of pixels based on the Evaluation method. Width Height Controls These set how large the patch to be probed is. Evaluation Decides how the pixels inside the rectangle get crunched into the output value. The choices cover:

- Average: All pixel values inside the rectangle are averaged.
- Minimum: The smallest value of all pixels inside the rectangle is used.
- Maximum: The highest value of all pixels inside the rectangle is used.

### The Probe modifier Value tab

### Value Tab

The Value tab governs the modifier adjustment's range or scale, thereby setting how sensitive the Probe is. Scale Input By default the Probe puts out the Black Value when the probed patch comes to a value of 0 (that is, black), and it puts out its White Value when the probed patch comes to a value of 1 (that is, white). This range control lets you reshape the Probe's sensitivity. Black Value The value the Probe puts out should the probed patch return the result set in Scale Input Black. White Value Whatever the Probe emits once the probed patch yields the result fixed under Scale Input White. Out of Image Value Whatever the Probe emits once the probed patch sits beyond the frame boundaries of the probed image. When probing a rectangle, this value won't be produced until the whole rectangle lies beyond the frame boundaries of the image being probed.

### Publish

Only parameters that carry animation are reachable from the Connect To menu. To wire up non-animated parameters, you first have to Publish them. Animated controls get published on their own, while static controls call for manual publishing. To publish a static control, right-click it and pick Publish out of the contextual menu.

### The Publish modifier Controls tab

### Controls Tab

The Controls tab presents the published control on offer for linking to other controls. Published Value How the published control displays naturally depends on which control was published from which node.

### Resolve Parameter

The Resolve Parameter Modifier comes into play when you build a transition template in Fusion meant for DaVinci Resolve's Edit page or Cut page. As you construct a transition in Fusion, the Resolve Parameter modifier gets attached to whichever control you wish to animate. The Resolve Parameter modifier animates that parameter automatically across the transition's length, letting you trim the transition over on the Edit page or Cut page. As an instance, building a cross dissolve goes like this: 1 Out of the Effects Library, drop a Fusion Composition onto the Edit page Timeline. 2 Within Fusion, drop a Dissolve node into the Node Editor. 3 Over in the Inspector, right-click the Background/Foreground parameter, then pick Resolve Parameter out of the Modifier contextual menu. With the modifier on the Background/Foreground parameter, the slider updates by itself any time the transition is altered back on the Edit/Cut page. 4 Within the Node Editor, right-click the Dissolve node and pick Macro > Create Macro. 5 Whenever the macro you're building will act as a Fusion transition, the Macro Editor needs two inputs plus one output selected. Beneath the Dissolve heading here, tick the boxes for Output, Background and Foreground. 6 Name the transition, after which you store the macro via the top File menu.

7 Drop the macro into the folder below so the Edit page or Cut page Effects Library lists it. On MacOS the destination is `$TEMPLATE_MAC_OS_PATH/Transitions`, or alternatively `$TEMPLATE_MAC_ USER_PATH/Transitions`. Should you be running Windows instead, place it under `$TEMPLATE_WIN_OS_PATH\Transitions`, or else `$TEMPLATE_WIN_ USER_PATH\Transitions`. 8 Close and relaunch DaVinci Resolve so the transition list in the Effects Library updates. 9 On the Edit page, open the Effects Library. Browse to Video Transitions Fusion Transitions, and your custom Fusion transition shows up there.

### Shake

The Shake modifier serves to randomize a Position or Value control so semi-random numeric inputs come out. The shake that results can be wholly random. The motion may also be smoothed for a gentler, more organic feel. To put the Shake modifier on a parameter, pick Modify With > Shake from that parameter's contextual menu. The Shake modifier draws on the following controls to pull off its effect. You apply it by right-clicking a parameter and picking Modify With > Shake.
