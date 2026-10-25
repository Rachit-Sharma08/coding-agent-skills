# Modifiers and animating parameters in the inspector

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing parameters in the inspector.
[Chapter index](INDEX.md) / [Previous section](eyedropper-with-color-swatch-and-gradients.md) / [Next section](directional-blurs-with-usercontrols-applied.md)
<a id="source-an-example-of-customizing-directional-blur"></a> <a id="source-animating-parameters-in-the-inspector"></a> <a id="source-attaching-a-parameter-to-an-existing-animation-curve"></a> <a id="source-connecting-parameters"></a> <a id="source-connecting-parameters-by-pick-whipping"></a> <a id="source-connecting-parameters-by-publishing"></a> <a id="source-contextual-menus"></a> <a id="source-customizing-node-parameters-with-user-controls"></a> <a id="source-default-directional-blur-controls-in-the-inspector"></a> <a id="source-directional-blur-controlled-by-the-centers-position"></a> <a id="source-modifiers"></a> <a id="source-node-contextual-menus"></a> <a id="source-parameter-contextual-menus"></a> <a id="source-pick-whipping-one-parameter-to-another"></a> <a id="source-removing-animation-from-a-parameter"></a> <a id="source-the-edit-control-window"></a> <a id="source-the-publish-contextual-menu"></a>

### Modifiers

Modifiers are things like expressions, calculations, trackers, paths, and other mathematical building blocks that you connect to a parameter to broaden what it can do. Once a modifier is attached to a parameter, its own controls show up separately in the Inspector Modifiers tab. The steps to attach one: 1 Right-click on the parameter you'd like to give a modifier to. 2 Pick an entry from the Modifier submenu inside the contextual menu.

### Animating Parameters in the Inspector

In Fusion you can keyframe nearly every parameter on nearly every node, opening the door to animated results like moving transforms, spline-based rotoscoping, warps that shift over time, and on and on without limit. To make this easy, keyframing controls sit right inside the Inspector beside each keyframable parameter. They are:

- A gray Keyframe button sitting to the right of each keyframable parameter. Pressing this gray button drops a keyframe wherever the playhead currently rests and flips the button to orange.
- Once a parameter has a keyframe, jumping to a different frame and altering that parameter drops a new keyframe automatically at the spot you're on.
- Any time the playhead lands exactly on a keyframe, the button shows orange. Pressing an orange Keyframe button removes the keyframe at that frame and reverts the button to gray.
- If keyframes exist further along in either direction, little navigation arrows show up on the left and right. Pressing those left and right navigation arrows next to the keyframes sends the playhead straight to them.

Orange Keyframe buttons in the Inspector mark frames that hold a keyframe. After you've set keyframes on a parameter or two, and provided Show Modes/Options is turned on, the node holding those keyframed parameters wears a Keyframe badge that signals the node now carries animation.

A node that's been keyframed wears a Keyframe badge over in the Node Editor. Once node parameters are being keyframed, you're free to retime them within the Keyframes Editor and/or Spline Editor. To dig deeper into Fusion keyframing, turn to Chapter 71, “Animating in Fusion’s Keyframes Editor,” found in the DaVinci Resolve Reference Manual, or to Chapter 9 of the Fusion Reference Manual.

### Removing Animation From a Parameter

To clear all the keyframes from a parameter: 1 In the Inspector, right-click the keyframed parameter's name. 2 From the contextual menu, pick Remove “node name:parameter name”. TIP: Should you switch away from the default Bézier spline type, the contextual menu instead shows whatever spline type is currently in use.

### Attaching a Parameter to an Existing Animation Curve

You can hook several parameters up to one shared animation curve. That's a real timesaver whenever you're driving different parameters on a node with the very same animation. To wire a second parameter onto that same animation curve: 1 Right-click whichever second parameter you'd like to attach. 2 Within the contextual menu, hover your pointer over the Connect To submenu. 3 From the Connect To submenu, select the animated parameter's name.

### Connecting Parameters

There's frequently good reason to link two parameters even when no animation curve is involved. You have two ways to do it.

### Connecting Parameters by Publishing

To bind two parameters so that moving one moves the other, you join them by issuing the Publish menu command on the first and the Connect menu command on the second.

To Publish and Connect parameters: 1 Right-click the name of whichever parameter you'd like to publish and pick Publish from its contextual menu. 2 Right-click the second parameter you mean to attach, then from the Connect To submenu select the name of the parameter you just published.

### The Publish contextual menu

### Connecting Parameters by Pick Whipping

Another route is to tie two parameters together with simple expressions. Pick whipping with simple expressions lets you wire values up and combine them visually, with no need to publish a value beforehand. The pick whip itself is a momentary line you drag from one parameter to another to forge a link between them. To join two parameters with a pick whip: 1 Double-click into the field of the parameter you'd like to pick whip onto another, enter =, and then hit the Return key. 2 Once the Pick Whip controls show up beneath the parameter, drag a “whip” out of the Add button over to the target parameter. From then on, changing the target parameter changes the original one too.

### Pick whipping one parameter to another

TIP: Turn off the Auto Control Close node’s General preference, then select a pair of nodes in the Node Editor, and you'll be able to pick whip two parameters that live on different nodes. Beyond that, the Expression field lets you layer mathematical formulas onto the incoming value from the target parameter. To read up further on Pick Whipping and Expressions, consult Chapter 74, “Using Modifiers, Expressions, and Custom Controls,” within the DaVinci Resolve Reference Manual, or Chapter 12 of the Fusion Reference Manual.

### Contextual Menus

Inside the Inspector you can call up two kinds of contextual menu.

### Node Contextual Menus

To bring up the Node Context menu from inside the Inspector, right-click on the Inspector header. That node's contextual menu offers the very same entries you'd reach by right-clicking the node within the Node Editor itself. To learn more about these choices, refer to Chapter 67, “Working in the Node Editor.” inside the DaVinci Resolve Reference Manual, or to Chapter 5 of the Fusion Reference Manual.

### Parameter Contextual Menus

You reach an individual parameter's contextual menu by right-clicking over that parameter's name, slider, thumbwheel, range control, button array, or any other control type. Right-clicking a slider, for instance, brings up the slider's contextual menu, complete with options to animate the control or stack on extra modifiers. A good many of these options got covered earlier in this chapter.

### Customizing Node Parameters with User Controls

Every Fusion node has an interface laid out to expose its parameters in a sensible way. Even so, there are times you'll want to add, conceal, or rework the controls. That's most often done for simple expressions and macros, though you might also do it for the sake of usability or appearance with favorites and presets. You add or edit user custom controls through the Edit Control dialog. Right-click a node's name in the Inspector (up in the header bar) and pick Edit Control from the contextual menu. A fresh window opens, labeled Edit Control.

### The Edit Control window

Under the Input attributes you can choose an existing control or build a brand-new one, give it a name, set its type, and place it on a tab. Under the Type attributes you spell out the input controls, the defaults and ranges, and whether an onscreen preview control exists. The Input Ctrl attributes box holds settings tied to the particular node control selected, while the View Ctrl attributes box holds settings for the preview control, should there be one. Every change you make with UserControls lives inside the node instance itself, which means they can be copy/pasted, saved into a setting, added to the Bins, or added to your favorites.

### An Example of Customizing Directional Blur

For this walkthrough, imagine we'd like a more intuitive means of steering a linear blur than working the Length and Angle sliders separately.

### Default Directional Blur controls in the Inspector

By leaning on the Center input control alongside its preview control, we can set both an angle and a distance directly inside the viewer through expressions. 1 Right-click the Length parameter's label, pick Expression off the contextual menu, then drop this expression into the Expression field that opens up: `-sqrt(((Center.X-.5)*(Input.XScale))^2+((Center.Y-.5)*(Input.YScale)*(Input. Height/Input. Width))^2)` 2 After that, right-click the Angle parameter's label, again pick Expression off the contextual menu, and drop this expression into the Expression field that opens up: `atan2(Center.Y-.5)/(Input.OriginalWidth/Input.X , .5-Center.X) * 180 / pi`

### Directional Blur controlled by the Center’s position

That works, but the controls are bewildering. The Center control no longer acts as the center, and it really ought to carry the name “Blur Vector” instead. Since the Length and Angle controls aren't meant to be touched, they ought to be tucked out of sight, and because we're only after a linear blur, the Radial and Zoom buttons are surplus. All we actually need is a choice between Linear and Centered.
