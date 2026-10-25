# Contextual menu for parameters in the inspector and modifiers

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using modifiers expressions and custom controls.
[Chapter index](INDEX.md) / [Next section](multiple-modifiers-and-parameter-calculations.md)
<a id="source-adding-modifiers-to-individual-parameters"></a> <a id="source-adding-the-right-modifier-for-the-job"></a> <a id="source-combining-modifiers-and-keyframes"></a> <a id="source-connecting-multiple-parameters-to-one-modifier"></a> <a id="source-publishing-a-parameter"></a> <a id="source-the-contextual-menu-for-parameters-in-the-inspector"></a> <a id="source-the-modifiers-tab-with-two-modifiers-applied"></a> <a id="source-using-modifiers"></a> <a id="source-using-modifiers-expressions-and-custom-controls"></a> <a id="source-using-modifiers-expressions-and-custom-controls-1"></a>

### Using Modifiers, Expressions, and Custom Controls

Among Fusion’s greatest strengths are the several routes it opens for reaching past the ordinary toolset that ships with the program. Here you will find a primer on a range of advanced capabilities — Modifiers, Expressions, and Scripting among them — each of which lets you broaden what the software does and fold Fusion more tightly into your studio.

### The Contextual Menu for Parameters in the Inspector

You reach nearly all of the capabilities described here through a contextual menu, which pops up whenever you rightclick most parameters in the Inspector. The exact menu you get changes according to which spot in the Inspector your right-click lands on. In particular, right-clicking a parameter name or a slider opens a richly stocked contextual menu — one that can attach animation, expression fields, and modifiers that broaden behavior, plus publishing and linking tools that let you drive several controls at once.

### Using Modifiers

Modifiers — which act as add-ons to a node’s toolset — give you a way to drive parameters. A good many of them will generate, on their own, animation that would be a chore to build by hand. At one end a modifier might be nothing more than keyframe animation or a link tying parameters to other nodes; at the other it might involve elaborate expressions, procedural functions, outside data, third-party plugins, or fuses.

### Adding the Right Modifier for the Job

The set of modifiers on offer hinges on the kind of parameter sitting under your right-click. Each parameter type — numeric values, text, polylines, gradients, and points — comes with its own compatible modifiers, which is why the Modify With menu narrows its choices to suit whichever parameter you picked.

### Adding Modifiers to Individual Parameters

To attach modifiers to a parameter, use the Inspector’s contextual menu, or right-click that parameter’s onscreen control out in the viewer. Whichever path you take, you are shown a live list of the modifiers suited to the parameters you have selected. As an example, dropping a Perturb modifier onto any slider auto-animates the parameter by jiggling its value at random. With the modifier in place, the Modifiers tab fills with controls for tuning how fast and how far the random animation swings.

Adding a Perturb modifier to the Center X and Y parameters by way of the Inspector contextual menu

You will find a modifier’s controls under the Modifiers tab in the Inspector. Should the node you have selected carry a modifier, that Modifiers tab lights up to signal as much. Where no modifier has been applied, the tab simply stays grayed out.

### The Modifiers tab with two modifiers applied

Just as node tools do, modifiers show up with their own header bars and header controls. You can likewise drag a modifier’s title bar into a viewer when you want to inspect what it puts out.

### Combining Modifiers and Keyframes

Auto-animating modifiers such as Perturb and Shake pair nicely with keyframes, together yielding animation that feels more lifelike and organic. You might, say, lay down the broad motion path of an object by keyframing its Center X and Y parameters, then layer a modifier over those same parameters to add a secondary jitter. To pair a keyframed motion path with a Perturb modifier: 1 Apply a Transform to some image, perhaps a butterfly or spaceship. 2 In the Node Editor, click the Transform node to select it. 3 Over in the Inspector, press the Keyframe button sitting to the right of the Center X and Y parameters. 4 Place the butterfly or spaceship picture at whatever spot you intend the animation to open on. 5 Keep advancing the playhead through the render range, nudging the image each time, until a figure-8 motion path takes shape. 6 In the Inspector, right-click the Center X label and pick Modify With > Perturb. 7 Open the Modifiers tab atop the Inspector, then dial in jittery random movement by tuning the Strength, Wobble, and Speed parameters as playback runs.

### Publishing a Parameter

What the Publish modifier does is expose a parameter’s value so that other parameters are free to connect to it. The upshot is that a single slider can drive several parameters at once, whether they sit on the same node or on different ones. Publishing a motion path, for one, lets you hook a number of objects up to that one path.

Publish a parameter so that other parameters may be tied to it After a parameter has been published, a right-click on some other parameter lets you pick Connect To > [published parameter name] out of the contextual menu. From then on the two values move together, and editing one of them in the Modifiers tab shifts the other. The pick whip drawn between two parameters delivers comparable linking while granting you more latitude. Pick whipping across parameters gets its own treatment further along in this chapter.

### Connecting Multiple Parameters to One Modifier

One modifier — or one published parameter — can govern several parameters together so that they behave in unison. The Connect To submenu is where this gets set up. Much as with assigning a modifier, the menu trims itself down to just those choices that fit whichever parameter you right-clicked. The resulting link runs both ways: edit either side and the opposite parameter follows.

Linking modifiers across several parameters by way of the Connect To menu
