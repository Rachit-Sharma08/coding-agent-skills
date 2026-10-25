# Text character level styling

Version: DaVinci Resolve 20.3 Reference Manual. Context: Text.
[Chapter index](INDEX.md) / [Previous section](text-layout-tab.md) / [Next section](text-follower-timing-tab.md) / [Text+ TXT+](multitext-and-plasma-and-text.md)
<a id="source-character-level-styling"></a> <a id="source-character-level-styling-modifiers-tab"></a> <a id="source-common-controls"></a> <a id="source-common-controls-1"></a> <a id="source-comp-name"></a> <a id="source-controls"></a> <a id="source-follower"></a> <a id="source-inspector"></a> <a id="source-text-modifiers"></a> <a id="source-text-modifiers-1"></a> <a id="source-text-tab"></a> <a id="source-text-toolbar"></a> <a id="source-text-toolbar-1"></a>

### Common Controls

Image and Settings Tabs The Inspector's Image and Settings tabs recur across many Generator nodes. These shared controls get a thorough write-up at this chapter's close, in the "The Common Controls" section.

### Text+ Toolbar

Pick the Text node and a toolbar shows up in the viewer. Below, each button is covered from left to right.

### Text+ toolbar

Allow Typing in Viewer Switch this on and you can type and edit text right in the viewer. A click on the text in the viewer drops the insert cursor inside the text. The Left and Right Arrow keys shift the insert cursor across characters. The Up and Down Arrows hop between text lines. Allow Manual Kerning The Manual Kerning button takes over from the automatic kerning text usually gets. A click on the small red handle under any character picks that character for kerning. You can also drag a selection rectangle around whichever characters you'd like to kern. With any characters picked, hold the Option (macOS) or Alt key (Windows) while tapping the Left or Right Arrow key to make tiny tweaks to the chosen characters' kerning. Hold the Alt + Shift (Windows) or Option + Shift (macOS) keys while tapping arrow keys to shift the character in bigger steps. To animate where each character sits, head into the Inspector's Advanced Controls, right-click the Manual Font Kerning control label, and pick Animate off the contextual menu. Each time a character moves, a fresh key lands on the animation spline. Every character is animated off the one spline, just as with polyline mask animation. No Text Outline Switch this button on and it stops any outline being drawn around the text's edges. That outline isn't part of the text; it's an onscreen control there to help mark where the text sits. Treat it as one part of a three-way toggle, its companions being Text Outline Outside Frame Only and Show Always Text Outline. Text Outline Outside Frame Only What this button does is trace a text-edge outline lying past the visible frame. It helps you find text that has drifted offscreen and no longer renders anything visible. Treat it as one part of a three-way toggle, its companions being No Text Outline and Show Always Text Outline. Show Always Text Outline What this button does is trace a text-edge outline regardless of whether the text shows within the frame. Treat it as one part of a three-way toggle, its companions being No Text Outline and Text Outline Outside Frame Only.

### Common Controls

Image and Settings Tabs The Inspector's Image and Settings tabs recur across many Generator nodes. These shared controls get a thorough write-up at this chapter's close, in the "The Common Controls" section.

### Text+ Modifiers

You assign text modifiers by right-clicking inside the Styled Text box and picking a modifier off the contextual menu. With a modifier chosen, its controls turn up in the Modifiers tab at the Inspector's top.

### Text+ modifiers

### Character Level Styling

The Character Level Styling modifier acts on Text+ nodes alone. Once it's applied, you can pick out single characters straight in the viewer and lay different text attributes on them via the Modifiers tab controls. NOTE: Character Level Styling can be applied directly only to Text+ nodes, never to Text 3D nodes. That said, styled text from a Text+ node can land on a Text 3D node by copying the Text+, right-clicking the Text 3D, and choosing Paste Settings.

### Inspector

### Character Level Styling Modifiers tab

### Text Tab

The Modifiers tab's Styled Text box shows the very text held in the Tools tab of the Text+ Inspector. You can't, however, pick the individual characters you want to change inside the Styled Text box; they have to be picked in the viewer. With text picked in the viewer, the Text tab offers the usual text formatting options, which act only on the chosen characters. Clear Character Styling on Selection Every change made to the chosen characters gets reset. Clear All Character Styling Every character attribute returns to its original value. Transform Tab and Shading Tab For the lowdown on these Text+ tabs, see the "Text+" section above.

### Comp Name

Comp Name makes the styled text turn into the current Composition Name. That comes in quite handy for automating burn-ins on daily renderings. See the TimeCode modifier as well. You apply it by right-clicking in a Text+ node's Styled Text field and picking Comp Name.

### Controls

This modifier has no controls.

### Follower

The Follower modifier lets you sequence text animations. You apply the modifier by right-clicking in a Text+ node's Styled Text field and picking Follower. Over in the Modifiers tab, you begin by animating the text's parameters (mind that altering any parameter in the Modifiers tab stays invisible unless a keyframe is added.) Then, in the Timing tab, you set how long the animation waits between characters.
