# Inspector for a default direction blur and fusionscript

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using modifiers expressions and custom controls.
[Chapter index](INDEX.md) / [Previous section](expression-and-pick-whipping-to-create-an-expression.md)
<a id="source-fusionscript"></a> <a id="source-the-inspector-for-a-default-direction-blur"></a>

### The Inspector for a default direction blur

Suppose we wanted a more hands-on means of steering a linear blur out in the viewer, in place of reaching for the Length and Angle sliders back in the Inspector. By way of a SimpleExpression, we will steer the length and angle parameters using the Center parameter’s onscreen control in the viewer. Such a SimpleExpression would read roughly thus: For Length: `sqrt(((Center.X-.5)*(self.Input.XScale))^2+ ((Center.Y-.5)*(self.Input.YScale)*(self.Input.Height/self.Input.Width))^2)` For Angle: `atan2(.5-Center.Y , .5-Center.X) * 180 / pi`

DirectionalBlur driven by where the Center sits.

Granted, this is a fairly advanced function, but it performs well enough. Dragging the onscreen control sets both the angle and the length of the directional blur. The trouble now is that the parameter names mislead. The Center parameter no longer behaves as a center at all; it stands for the blur’s direction and length, so "Blur Vector" would suit it better. Since the Length and Angle controls no longer need editing, they ought to be tucked out of sight, and because this is strictly a linear blur, the Type menu has no need of Radial or Zoom — Linear and Centered are the only choices we require. The Edit Controls dialog makes such changes simple. To rework the example’s Inspector parameters along these lines: 1 Within the Edit Control dialog, choose Center out of the ID list. 2 A dialog appears asking whether you mean to Replace, Hide, or Change ID; we will go with Replace. 3 Rename it to Blur Vector. 4 Set its Type to Point. 5 Under the Page list, pick Controls. (Normally Controls is the Inspector’s first tab.) 6 Click OK.

The DirectionalBlur Center parameter has had its name swapped to Blur Vector. That new Blur Vector parameter now shows up in the Inspector. Because the control’s internal ID stays Center, our SimpleExpressions went untouched. To conceal the Length and Angle parameters within the Inspector: 1 Within the Edit Control dialog, pick Length out of the ID list. 2 Choose Controls under the Page list. 3 From the input Ctrl list, choose Node. 4 Click OK. 5 Back in the Edit Control dialog, this time pick Angle from the ID list. 6 Again from the input Ctrl list, choose Node. 7 Click OK.

Lastly, to strip the Radial and Zoom options out of the Type menu: 1 In the Edit Control dialog, pick Type from the ID list. 2 Choose Controls under the Page list. 3 In the Items list, highlight Radial and press Del to drop it. 4 In the Items list, highlight Zoom and press Del to drop it. 5 Click OK. Only two options remain in the Type menu now. Should you prefer to swap the Type menu out for a fresh checkbox control, you can manage that with one new control plus a tiny expression. To build a new control: 1 Within the Edit Control dialog, enter Center Blur in the Name field. 2 From the ID list, choose New Control. 3 With Type set to Number, point the Page at Controls. 4 For its Input Ctrl, choose CheckboxControl. 5 Click OK. So that this fresh checkbox drives the original Type menu, you must hang a SimpleExpression off the Type: iif(TypeNew==0, 0, 2) In Lua script, the "iif" operator goes by the name conditional expression. It weighs something according to whether a condition holds true or false.

### FusionScript

As a route to higher productivity, scripting is indispensable. Scripts can unlock new abilities or take over repetitive chores, above all the ones peculiar to your own projects and workflows. Within Fusion, a script might reshuffle the nodes in a comp, look after caches, and turn out several output files ready for delivery. They can also bridge Fusion to other applications — logging an artist’s hours, firing off emails, or refreshing web pages and databases. The umbrella name for Fusion’s scripting environment is FusionScript. It supports Lua, and in certain contexts Python 2 and 3 as well. FusionScript furthermore bundles libraries that smooth over many routine jobs you would otherwise do by hand in Lua and Python inside Fusion. Interactive scripts can be run under a variety of circumstances. Among the common ones:

- Utility Scripts, which run in the Fusion application context, sit under the File > Scripts menu.
- Comp Scripts, which run in the composition context, sit under the Script menu, or you type them

into the Console.

- Tool Scripts, which run in the tool context, sit within the Tool’s context menu > Scripts.

Still other script kinds exist too — these include SimpleExpressions, Intool Scripts, and Hotkey Scripts, as well as Event Suites, Bin Scripts, Scriptlibs, and Startup Scripts. Beyond that, Fusion Studio permits external and commandline scripting, plus Job and Render node scripting for network rendering. FusionScript likewise underpins Fuses and ViewShaders, the specialized scripting-driven plugins for tools and viewers usable across both Fusion and Fusion Studio. For deeper detail on scripting, turn to the Fusion Scripting Documentation, reachable from the Documentation submenu within the Help menu.
