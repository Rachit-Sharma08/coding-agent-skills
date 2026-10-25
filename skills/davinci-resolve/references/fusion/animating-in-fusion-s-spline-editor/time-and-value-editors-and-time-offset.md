# Time and value editors and time offset

Version: DaVinci Resolve 20.3 Reference Manual. Context: Animating in Fusion s spline editor.
[Chapter index](INDEX.md) / [Previous section](copying-and-pasting-keyframes.md) / [Next section](selection-states-and-reshaping-splines-using-the-toolbar.md)
<a id="source-bézier-splines-can-mix-linear-and-smooth-curves"></a> <a id="source-changing-a-splines-status"></a> <a id="source-filtering-the-spline-editor"></a> <a id="source-modifying-spline-handles"></a> <a id="source-reducing-points"></a> <a id="source-time-and-value-editors"></a> <a id="source-time-offset"></a> <a id="source-time-scale"></a> <a id="source-value-editor"></a> <a id="source-working-with-filters"></a>

### Time and Value Editors

Sitting in the lower-right corner of the Spline Editor, the Time and Value Editors let you reset a keyframe’s position and parameter value by typing a number into the number field for each button. Every field toggles among three modes that adjust a keyframe’s time and value in three exact yet separate ways. By default, each field reads the literal frame number or parameter value where you want the keyframe placed. The remaining modes offset and scale the keyframe’s position or value instead.

Type a value or a particular time into the number fields to alter the selected keyframe. Time Editor: The Time Editor exists to change the current time of the selected keyframe. Switching the Time mode lets you type a particular frame number, an offset off the current frame, or spread the keyframes according to their distance (scale) from the playhead. Pick whichever of the three modes you want from the Time mode drop-down menu.

Three time editing modes can be chosen from the Time mode drop-down menu. Time: The number field displays the current frame number of the selected control point. Typing a new frame number into the field relocates the selected control point to that frame. When nothing is selected, or when several keyframes are selected, the field stays empty and no time can be entered.

### Time Offset

Choosing T Offset from the drop-down menu switches the number field’s mode over to Time Offset. Under this mode, the number field shifts the selected keyframes forward or backward in time. You can type in either a positive or a negative offset. As an example, an offset of 2 carries a selected keyframe from frame 10 to 12. Had several keyframes been selected in that same example, each one would advance two frames ahead of where it sat.

### Time Scale

Choosing T Scale from the drop-down menu switches the number field’s mode over to Time Scale. Under this mode, the selected keyframes’ positions scale relative to where the playhead sits. As an example, with a keyframe on frame 10 and the playhead on frame 5, typing a scale of 2 drives the keyframe 10 frames ahead of the playhead’s spot, landing on frame 15. Keyframes lying to the left of the playhead get scaled using negative values.

### Value Editor

The Value Editor exists to change the selected keyframe’s parameter value through one of three Value modes. Switching the Value mode lets you type a particular value for a parameter, an offset off that value, or spread the values out. You set the mode from the Value mode drop-down menu.

Three value editing modes can be chosen from the Value mode drop-down menu. Value: The number field displays the value of whichever keyframes are currently selected. Typing a new number into the field alters the selected keyframe’s value. With more than one keyframe selected, the value shown is an average across the keyframes, yet typing a new value makes every keyframe take on that value. Value Offset: Picking Offset from the drop-down menu puts the Value Editor into the Offset mode. Under this mode, the value for the selected keyframes shifts up or down. You can type in either a positive or a negative offset. As an example, typing a value of -2 turns a value of 10 into 8. With several keyframes selected, all of them have their values changed by -2. Value Scale: Picking Offset from the drop-down menu puts the Value Editor into the Scale mode. Typing a new value scales or multiplies the selected keyframes’ values by the amount you give. As an example, typing a value of 0.5 turns a keyframe’s value of 10 into 5.

### Modifying Spline Handles

Every Bézier spline keyframe carries two control handles that mold the spline as it runs through the key point. Those handles show up only while the keyframe is selected. To begin with, the handles sit at linear, which yields straight-line transitions between keyframes. Still, you can smooth out any control point by right-clicking over it and picking Smooth, or by pressing Shift-S.

### Bézier splines can mix linear and smooth curves

Dragging a keyframe’s handles changes the slope of the segments running through the spline. By default, a control point’s two handles are tied together, so moving one moves the one on the opposite side along with it. This keeps the tension through the keyframe steady. Even so, there are times when you’ll want to adjust these handles on their own for a sharper curve or effect. To break a Bézier spline’s control handles temporarily, so one moves apart from the other: 1 Select the control point you want to change. 2 Hold the Command key down and drag one of the control handles. They’ll now move apart from each other for as long as you keep the Command key held. To have every Bézier handle behave independently throughout the Spline Editor: Right-click in the graph and pick Independent Handles from the Options contextual menu. Turning this option on makes all the Bézier handles independent. It amounts to the same thing as using the Command key while moving a handle, except it covers every control point until you switch it off.

### Reducing Points

When a spline has too many control points crowded together, picking Reduce Points trims their number and makes the remaining points easier to work with. The spline keeps its overall shape as faithfully as it can while dropping redundant points from the path. To cut down a spline’s point count: 1 Select the span of keyframes you’d like to thin. 2 Right-click in the graph area and pick Reduce Points from the contextual menu. 3 Once the Reduce Points dialog comes up, drag the slider down to a lower value. You can push the slider value as low as it goes, provided the spline still closely echoes the shape of your original spline.

TIP: At a value of 100, none of the spline’s points get removed. Dial in smaller values to drop more points.

### Filtering the Spline Editor

The Spline Editor can show the animation splines for many parameters at the same time, and Fusion gives you several ways to decide which spline you view and which you edit. An intricate composition can readily hold dozens, even hundreds, of animation curves. The bigger a composition gets, the harder pinning down one specific spline becomes. You have two routes for filtering the splines on display in the Spline Editor: show only selected tools, or build a filter that surfaces just certain tools. The Spline Editor provides various means of governing which splines appear. Most of these options live in the Options menu, tucked into the upper-right corner of the Spline Editor panel.

The Options menu governs which splines turn up in the Spline Editor. Show Only Selected Tool: You can narrow the splines on display in the Spline Editor down to just those belonging to selected tools. Picking this option at the top of the Options menu surfaces only the splines for tools currently selected over in the Node Editor. Show All/None: By default the Spline Editor presents all the splines for every node carrying animated parameters. Enabling Show Only Selected Tools in the Options menu overrides that. You can also turn off the Show All setting by picking Show None, at which point the Spline Editor sits empty. Expose All Controls: The Expose All Controls option amounts to applying no filtering at all to the parameters. Picking it shows, in the Spline Editor header, every parameter belonging to all the nodes over in the Node Editor. It serves as a quick route to activating one parameter and having an animation spline added for it automatically when none exists yet.

When a lot of nodes are on display, each possibly bearing a lot of parameters, this can clutter the interface and bog it down. The option works best paired with the Show Only Selected Tool option, which caps how many nodes and parameters show up and delivers the best performance. Follow Active: You reach the Follow Active option by right-clicking in the graph and picking Options > Follow Active. This option lets you filter the splines in the graph without filtering the header list of tools. Whereas the Show Only Selected Tool option conceals other tools in the header, the Follow Active option keeps the header showing all the tools yet automatically enables only the splines belonging to the Active tool.

### Working with Filters

Filters let you pick the particular types and classes of tools that appear in the Spline Editor and Keyframes Editor. As an example, you might build a filter that surfaces only particle nodes, or one that surfaces only color correction and brightness/contrast tools. To build a filter: 1 From the Options menu, pick Create/Edit Filters. 2 Click the New button to start a new filter and give it a name in the dialog box. 3 Tick a checkbox beside a whole category, or beside individual tools within each category, to set which tools the filter takes in.

Tick each tool you’d like to keep in the Spline Editor whenever the filter is active. The Invert All and Set/Reset All buttons make sweeping changes to all the checkboxes, flipping the selected states as just described. To flip the selection state of the categories while building a filter list: 1 Click the Invert All button. 2 With the custom filter set up, click the Save button to dismiss the Settings dialog and store the filter. To tick or untick every checkbox: 1 Click the Set/Reset All button repeatedly until all categories end up either checked or unchecked. 2 With the custom filter set up, click the Save button to dismiss the Settings dialog and store the filter.

To apply a filter to the Spline Editor:

- Pick the filter you want by name from the Options menu. That filter takes effect across both the Spline Editor and the Timeline.

Every filter you build appears in the Options menu. To switch a filter off and bring all tools back into the Spline Editor:

- Pick Show All from the Options menu.

### Changing a Spline’s Status

The Spline header presents a hierarchical list of animated parameters together with their parent nodes. Clicking the disclosure arrow beside a tool’s name unfolds the names of every animated parameter on that tool. Clicking straight on a parameter name in the Spline header switches that spline on for display and editing.

The Spline header showing the Brightness Contrast tool alongside its animated Gain and Gamma parameters. Tool Status Checkbox: Beside each spline’s name sits a checkbox that signals the spline’s status. Selecting a parameter name makes the checkbox active, which lets you view and edit the spline in the graph. Each checkbox carries three selection modes: active, viewed, and disabled. Clicking straight on the checkbox cycles it through these three states. Altering the parent node checkbox’s state applies that state to every spline under that node.

Active: With the checkbox showing a check mark, the spline appears in the graph and is editable. Viewed: With the checkbox showing a solid gray box, the spline is visible in the graph but locked against editing. It’s read-only. Disabled: With the checkbox empty, the spline neither appears in the graph nor can be edited. Checkboxes dictate which splines you can see and edit.
