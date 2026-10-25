# Directional blurs with usercontrols applied

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing parameters in the inspector.
[Chapter index](INDEX.md) / [Previous section](modifiers-and-animating-parameters-in-the-inspector.md)
<a id="source-adding-another-control"></a> <a id="source-directional-blurs-with-usercontrols-applied"></a>

### Adding Another Control

To begin, let's rename the Center. In the Add Control window, pick Center from the ID list. A dialog pops up offering Replace, Hide, or Change ID. We'll go with Replace. We're now editing the Center input. We'll set the Name to Blur Vector, the Type to Point, and the Page to Controls — the first tab, where the controls usually live. Hit OK, and our new input shows up on our node in the Node Editor. Because the control's ID stays Center, our SimpleExpressions are untouched. To tuck away the Length and Angle, we'll launch the UserControls script once more. This time, with the Length and Angle IDs selected, we'll pick Hide in the dialog. Hit OK for each. Lastly, to adjust which choices the Type offers, two paths are open to us. We can hide the buttons and swap in a checkbox, or we can trim the MultiButton down from four entries to two. Let's do both.

- For the checkbox, fire up UserControls once more, only this time, in place of choosing an existing ID, we'll enter Centered into the Name. That action makes both our input's name and its ID become Centered. We leave the Type at Number and the Page at Controls. Over in the Type Attributes, make the Input Ctrl a CheckboxControl. Hit OK, and there's our checkbox. So that the new control drives the Type, attach a SimpleExpression onto the Type:

iif(Centered==1, 2, 0). With that in place, UserControls can be used to tuck the Type control out of sight.

- For a new MultiButton, launch the UserControl script and create a fresh control ID called TypeNew. Feel free to set its Name to Type, since Names needn't be unique — only the IDs do. Make the Type Number, the Page Controls, and the Input Ctrl a MultiButtonControl. Within the Input Ctrl attributes, we get to type in our button names. We'll use Linear and Centered — enter each and click Add. Press OK, and our new buttons appear with the surplus options gone. So that this new control drives the original Type, attach a SimpleExpression onto the Type:

iif(TypeNew==0, 0, 2).

With that in place, UserControls can be used to tuck the original Type control out of sight.

### Directional Blurs with UserControls applied
