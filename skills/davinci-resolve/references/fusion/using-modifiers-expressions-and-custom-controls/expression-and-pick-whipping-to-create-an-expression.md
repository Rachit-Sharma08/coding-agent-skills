# Expression and pick whipping to create an expression

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using modifiers expressions and custom controls.
[Chapter index](INDEX.md) / [Previous section](multiple-modifiers-and-parameter-calculations.md) / [Next section](inspector-for-a-default-direction-blur-and-fusionscript.md)
<a id="source-choose-edit-controls-to-create-and-customize-parameters"></a> <a id="source-customizing-user-controls"></a> <a id="source-edit-control-dialog"></a> <a id="source-expression"></a> <a id="source-pick-whipping-to-create-an-expression"></a> <a id="source-removing-simpleexpressions"></a>

### Expression

Description

sin(time/20)/2+.5

This yields a sine wave ranging from 0 to 1.

iif(Merge1.Blend == 0, 0, 1)

When the Blend value equals 0 this gives back 0; otherwise it gives back 1. The iff() function serves as shorthand for a conditional, the if-then-else construct.

iif(Input.Metadata.ColorSpaceID == "sRGB", 0, 1)

Should the image feeding the current node’s Input carry the sRGB colorspace tag, this gives back 0. With no other node name spelled out, the expression takes the Input to be arriving from the current node — making it the same as self.Input. Across most Fusion nodes, though not every one, the Input is the principal image input that the Node Editor draws as an orange triangle. Images carry members you are able to read off, among them Depth, Width, Metadata, and the like.

Point(Text1.Center.X, Text1. Center.Y-.1)

In contrast to the earlier cases, what comes back here is a Point rather than a Number. A Point input draws on two members, X and Y. For this case, the Point handed back sits 1/10 of the image height beneath the Text1’s Center. That can prove handy when forging one-way parameter links, such as nudging one Text away from another.

Text1.Center - Point(0,.1)

This one closely resembles the expression just above. Here the SimpleExpression hands back Text in place of a Number or Point.

Text("Colorspace: "..(Merge1. Background.Metadata.ColorSpaceID)

Whatever text sits within the quotes gets joined onto the metadata string, which might yield: Colorspace: sRGB

`Text("Rendered "..os.date("%b %d, %Y").. " at "..os.date("%H:%M").."\n on the computer "..os. getenv("COMPUTERNAME").. " running "..os. getenv("OS").."\n from the comp "..ToUNC(comp.Filename))`

This produces a far longer Text, along the lines of: Rendered Nov 12, 2019 at 15:43 on the computer Rn309 running Windows*NT from the comp \\ SRVR\Proj\ Am109\SlateGenerator* A01.comp

os.date("%H:%M")

A range of details about the machine can be drawn from the OS library. Up above, os.date fetches the date along with the time in hours:minutes.

"..os.getenv("COMPUTERNAME").. " running "..os.

os.getenv will read back any environment variable you ask for — here, the machine’s name together with its operating system.

"\n from the comp "..ToUNC(comp.Filename)

A \n is what inserts a fresh line into the Text. By way of the comp variable you can reach assorted attributes of the comp — the filename among them, given here as a UNC path.

TIP: With lengthy SimpleExpressions, you may find it useful to pull the Inspector panel out so it grows wider, or to copy/paste by way of a text editor or the Console. Once you have set an expression that drives animation, the Spline Editor can be opened to watch the values charted across time. It is a sound way to gauge how your SimpleExpression resolves from frame to frame.

A sine wave shown in the Spline Editor, produced by the expression driving Text1: Size To learn more about composing Simple Expressions, consult the Fusion Studio Scripting Guide along with the official Lua documentation.

### Pick Whipping to Create an Expression

While a SimpleExpression field stands open, a + button shows along its left edge. Drag that + button over onto another control — an act known as "pick whipping" — and the two parameters become tied together, much as the Connect To menu would do. The difference is that, where a Connect To link is fixed, the pick whip lets you reshape the connection by editing the expression further.

Pick whipping as a fast way to wire one parameter to another You can also build and edit SimpleExpressions from inside the Spline Editor. In the Spline Editor, right-click the parameter and pick Set SimpleExpression off the contextual menu. The SimpleExpression then gets charted within the Spline Editor, letting you watch the outcome across time.

### Removing SimpleExpressions

Getting rid of a SimpleExpression is a matter of right-clicking the parameter’s name and picking Remove Expression off the contextual menu.

### Customizing User Controls

Within the Inspector, every tool lays its parameters out in a sensible sequence. Controls you reach for most sit nearer the top, while the finer tuning controls fall further down the list. Now and then, though, you will want to add, conceal, or alter those controls. SimpleExpressions and macros frequently call for it, but you might also do it on favorites and presets purely for usability or appearance. You add or revise custom controls through the Edit Control dialog, reached by right-clicking the node’s name in the Inspector and selecting Edit Controls from the menu.

### Choose Edit Controls to create and customize parameters

Inside the Edit Control dialog, the ID menu is where you either pick an existing parameter or spin up a fresh one. From the Type attributes list you give the control a name and settle whether it behaves as a text field, a number field, or a point.

### Edit Control dialog

The page list is how you drop the new control onto one of the Inspector’s tabs. Further settings fix its defaults and ranges, plus whether it gets an onscreen preview control. Settings tied to the chosen Type live in the Input Ctrl box, while the View Ctrl attributes box holds whatever onscreen preview controls are meant to show, if any. Everything you change in the Edit Controls dialog is held within the current tool instance, which means it can be copied/ pasted onto other nodes throughout the comp. Carrying those changes into other comps, though, means saving the node settings and filing them into the Bins in Fusion Studio or among your favorites. By way of illustration, we will tailor the controls of a DirectionalBlur:
