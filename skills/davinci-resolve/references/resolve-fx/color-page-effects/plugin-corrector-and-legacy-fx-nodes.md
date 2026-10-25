# Adding a plugin as a new corrector node and adding a plugin as a stand alone FX node legacy

Version: DaVinci Resolve 20.3 Reference Manual. Context: Color page effects.
[Chapter index](INDEX.md) / [Previous section](resolve-fx-and-open-fx.md)
<a id="source-adding-a-plugin-as-a-new-corrector-node"></a> <a id="source-adding-a-plugin-as-a-stand-alone-fx-node-legacy"></a> <a id="source-editing-effects-using-the-full-screen-viewer"></a> <a id="source-intellitrack-ai-point-tracker-studio-version-only"></a> <a id="source-keyframing-resolve-fx-and-ofx-in-the-inspector"></a> <a id="source-motion-tracking-resolve-fx-and-compatible-ofx-plugins"></a> <a id="source-resolve-fx-and-open-fx-onscreen-controls"></a> <a id="source-resolve-fx-and-open-fx-settings"></a> <a id="source-the-parameters-of-the-glow-resolve-fx"></a>

### Adding a Plugin as a New Corrector Node

To bring an Open FX plugin into your grade as a self-contained effect, drag any plugin out of the Open FX Library and drop it into the Node Editor, or onto one of your grade's connection lines, and Resolve spins up a new Corrector Node already carrying that Open FX plugin. From that point the node exposes all the extra inputs and Alpha connectors the effect requires. Since color correction nodes now cover every case, there's no longer any reason to build separate FX nodes. The upshot is tidier node trees and far less hand-wiring of links between nodes.

### Adding a Plugin as a Stand-Alone FX Node (Legacy)

Because the Resolve FX system was reworked to feel more natural and approachable, pulling an effect from the Effects Library into the Node Editor now spawns it on a standard corrector node rather than an FX Node. FX nodes have been deprecated as of DaVinci Resolve 18.5. Building an FX node serves no purpose any longer, since everything FX nodes once did has been folded into the standard corrector node. Even so, for older projects, or simply if the former workflow suits you better, you can still compel an FX node to appear by option-dragging the effect out of the Effects Library into the Node Editor in place of an ordinary drag.

### Resolve FX and Open FX Settings

Selecting a node that has a Resolve FX or Open FX plugin on it flips the Open FX panel over to its Settings, where every parameter tied to that plugin is laid out and ready to tune. Move any of the usual controls to shape how the plugin acts on the image.

### The parameters of the Glow Resolve FX

### Editing Effects Using the Full Screen Viewer

Since the Open FX panel is frequently too cramped to fit the complete control set of the more elaborate filters, it stays on screen even after you flip the Color page into Full Screen Viewer mode. Enter that mode by choosing Workspace > Viewer Mode > Full Screen Viewer (Shift-F). With this layout, precise work gets a lot easier because you're looking at a bigger image while every one of your effects sits in a taller panel along the side. TIP: While Full Screen Viewer mode is active you can still open and close the Node Editor whenever you need to jump between nodes during effects work.

In the Color page's Full Screen Viewer mode, the Settings panel stays available while you keep working

### Resolve FX and Open FX Onscreen Controls

On all three of the Edit page, Fusion page, and Color page, both Resolve FX and Open FX surface on-screen controls that let you adjust an effect visually. Within the Edit and Color pages, picking an Open FX plugin node, or a plugin in the Inspector that carries onscreen controls, automatically flips the Viewer over to Open FX Overlay mode with those controls ready at hand. Each plugin surfaces its own set of custom controls, so what you can steer, the effect itself or the image, varies with the plugin's purpose.

Adjusting the onscreen controls exposed by the GenArts Sapphire Glint Rainbow plugin Should the Viewer end up on some other onscreen control mode for any reason (say, displaying the Window or Image Wipe controls), getting back to the Open FX controls is always a matter of picking Open FX Overlay mode from the onscreen control drop-down menu beneath the Viewer.

TIP: During a session you'll often want to briefly hide or reveal the onscreen controls in the Viewer to get a clean, unobstructed view of the image you're working on. Rather than picking Off from the menu, you can flip any set of onscreen controls off and back on in an instant by pressing Shift-` (tilde).

### Keyframing Resolve FX and OFX in the Inspector

You can keyframe Resolve FX and Open FX across the Edit, Fusion, and Color pages. On the Edit and Color pages, though, the only way to keyframe them (as of this writing) is through the keyframing controls living in the Inspector. The good news is that the bulk of straightforward keyframing chores can be handled with the three buttons sitting to the right of any keyframeable parameter. You'll need a minimum of two keyframes for an effect to animate.

The Inspector's trio of keyframe controls, reading left to right: Previous keyframe, Create/Delete keyframe, Next keyframe

Methods of keyframing parameters in the Inspector:

- To add a keyframe: Pick a clip, open the Inspector, park the Timeline playhead on the frame that should hold a keyframe, then click the Keyframe button beside the Inspector parameter you intend to animate. After a parameter has at least one keyframe on it, any further changes you make to Inspector parameters, or with the onscreen Transform/Crop controls in the Timeline Viewer, will lay down new keyframes on their own whenever the playhead sits on a different frame.
- To move the playhead to the next or previous keyframe: Click the little left- or right-pointing arrow flanking a parameter's keyframe control, or hit Right-Bracket ( [ ) or Left-Bracket ( ] ), to send the playhead to the adjacent keyframe.
- To edit an existing keyframe of a parameter: Park the playhead directly over the keyframe you mean to change, then alter that parameter either from the Inspector or by way of the Timeline Viewer's onscreen controls.

Methods of changing keyframe interpolation in the Inspector:

- To change a keyframe to Static: (Color page only) A Static keyframe produces an abrupt, single-frame jump right at the keyframe it sits on, which works well for snappy, sudden effects. Use the next/previous keyframe controls to land the playhead on a frame that has a keyframe, then right-click the orange keyframe button and pick “Change to Static Keyframe.” The keyframe control turns into a round button, signaling the keyframe is now Static.
- To change a keyframe to Dynamic: Use the next/previous keyframe controls to bring the playhead to a frame holding a keyframe, then right-click the orange keyframe button and pick “Change to Dynamic Keyframe.” The keyframe control becomes a diamond button, signaling the keyframe is now Dynamic.

Methods of deleting keyframes and disabling keyframed effects:

- To delete a single keyframe: Open the Inspector, bring the Timeline playhead to a frame carrying a keyframe, and click the orange Keyframe button in the Inspector to remove it.
- To delete all keyframes for one parameter: Click the reset button just to the right of that parameter's keyframe control in the Inspector.
- To delete every keyframe across a whole parameter group in the Inspector: Click the reset button sitting beside the title bar of that group within the Inspector.
- To disable or enable a single parameter’s keyframed effect: Within the Timeline, click the toggle control at the left edge of a parameter's keyframe track. A white dot signals it's on, whereas the absence of a dot means it's dimmed and switched off.
- To switch a whole parameter group's keyframing off or on from the Inspector: Click the toggle control sitting at the left end of that group's title bar within the Inspector. Orange indicates the group is on; gray means it's off.

### Motion Tracking Resolve FX and Compatible OFX Plugins

Working with Resolve FX in the Color page, any Resolve FX carrying position parameters, such as Dent, Lens Flare, Light Rays (with “From a Location” chosen), Mirrors, Radial Blur, Ripples, Vortex, and Zoom Blur, can be motion tracked so it rides along with a moving subject in the frame, either through the simpler and more dependable IntelliTrack mode (covered just below) or the older point-based approach found in the Tracker palette's FX mode. To match-move a Resolve FX onto a feature by way of the FX tracker: 1 Build a fresh node and drag the Resolve FX filter you intend to use onto it so the effect is applied. For this walkthrough we're laying down a Lens Flare effect, which supplies the position parameters required to be match moved against the shot's motion, and we're picking the MIR-I 2.8/37 preset, which resembles a sun.

Applying a Lens Flare to the shot 2 Should it prove necessary, use the Viewer's onscreen controls or the X Position and Y Position sliders to nudge the Resolve FX effect to wherever you want it.

Moving the Lens Flare using the onscreen controls

3 Next, bring up the Tracker Palette and click the fx icon at top right. Opening the Tracker palette's FX tracker mode 4 Click the Add Tracker Point button over at the lower-left of the Tracker palette to drop tracker crosshairs onto the middle of the Viewer.

Adding a point tracker 5 Pull the crosshairs over to a high-contrast detail (a small object or a corner, for instance), then click the Track Forward button. Here, a rock sitting out at sea serves as a solid plane of motion for following a distant sun. No inner or outer box needs positioning or resizing as you go; all you do is drag the crosshairs so they're centered on the feature you mean to track.

Centering the point tracker over the feature you intend to follow 6 Now click the Track Forward button, and DaVinci Resolve traces the feature. The Resolve FX on that node travels right along with the track, and once tracking wraps up you're done.

A successful track 7 With tracking complete, you're free to nudge the Resolve FX anywhere you like to offset it from the track.

To read more on single-point tracking, consult the “Point Tracker Workflows” section over in Chapter 140, “Motion Tracking Windows.”

### IntelliTrack AI Point Tracker (Studio Version Only)

Driven by the DaVinci Neural Engine, the IntelliTrack point tracker lives in the FX tracker of DaVinci Resolve Studio. You can lean on the IntelliTrack setting to track your Resolve FX. Much like other AI-based tools, IntelliTrack leans on neither fixed rule sets nor heuristics; rather, it learns from real-world footage. That training makes it far less prone to stumbling in tricky situations, for example following a subject that briefly disappears behind an obstruction. In the majority of shots it proves both sharper and sturdier than the ordinary Point Tracker. Using IntelliTrack: Every bit of IntelliTrack's analysis runs out of sight, and the only thing you have to supply is to select the IntelliTrack setting, lay the tracking crosshairs over high-contrast regions on the one moving subject, and then tap any of the tracker's direction buttons. Choosing IntelliTrack mode for the window tracker on the Color page
