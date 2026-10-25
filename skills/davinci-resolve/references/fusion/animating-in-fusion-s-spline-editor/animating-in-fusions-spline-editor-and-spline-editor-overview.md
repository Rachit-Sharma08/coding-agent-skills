# Animating in fusions spline editor and spline editor overview

Version: DaVinci Resolve 20.3 Reference Manual. Context: Animating in Fusion s spline editor.
[Chapter index](INDEX.md) / [Next section](navigating-around-the-spline-editor-and-markers.md)
<a id="source-animating-in-fusion-s-spline-editor-part-1"></a> <a id="source-animating-in-fusions-spline-editor"></a> <a id="source-changing-spline-colors"></a> <a id="source-contextual-menus"></a> <a id="source-graph"></a> <a id="source-playhead"></a> <a id="source-renaming-splines"></a> <a id="source-spline-editor-interface"></a> <a id="source-spline-editor-overview"></a> <a id="source-spline-editor-toolbar"></a> <a id="source-spline-toolbar-buttons"></a> <a id="source-status-bar"></a> <a id="source-the-graph-header-and-toolbar"></a> <a id="source-the-spline-editor-with-three-animated-parameters"></a> <a id="source-the-spline-header"></a> <a id="source-what-are-splines"></a>

### Animating in Fusion’s Spline Editor

These pages walk through keyframing effects and steering animations inside Fusion’s Spline Editor.

### Spline Editor Overview

The Spline Editor stands as the chief workspace for reshaping and polishing animation. Your main use for it is to render how parameters’ values shift over time, drawn as splines. Where Keyframes plainly pin a parameter’s value to a particular frame, Splines are the lines or curves that interpolate values across keyframes. Set a keyframe on a parameter and a spline springs into being, ready to appear in the Spline Editor where you can fine-tune the animation further. The Spline Editor, though, outdoes an ordinary curve editor, since it can also lay out functions that may be no splines at all, such as characters shifting inside a text string or the mathematical expressions steering your animations.

### The Spline Editor with three animated parameters

### What Are Splines?

Every animation rests on splines that trace a parameter’s value at any moment in time. Across the Spline Editor graph, the comp’s time runs along the horizontal axis while the parameter’s value runs along the vertical one. Picturing animation as splines, rather than as keyframes the way the Keyframes Editor does, pays off because splines let you work the interpolation that sits between keyframes. Suppose a parameter holds a keyframe valued at 1.0 on frame 1, then a keyframe valued at 10.0 on frame 10, after which the values in between get smoothly interpolated, computed from the spline’s shape. The functions and controls within the Spline Editor hand you remarkable command over that interpolation.

### Spline Editor Interface

Out of the box the Spline Editor stays hidden, yet a click of the Spline button on the user interface toolbar reveals it whenever you like. Another route: in the Node Editor right-click a node, or in the Keyframes Editor right-click a segment, then pick Edit Splines from the drop‑down menu. You can keep the Spline Editor open beside the Node Editor or Keyframes Editor, or set it apart so it fills the whole work area.

### The Graph, Header, and Toolbar

Three principal working areas make up the Spline Editor: the graph, header, and toolbar. Along the Spline Editor’s left edge sits the header, presenting a list of animated parameters. Most of the panel goes to the splines shown in the graph area, with a toolbar stretched across the bottom that offers assorted ways to work the splines.

### Graph

The graph claims the most space in the interface. Here is where you view and edit the animation splines. Two axes span the graph: the horizontal one stands for time, the vertical one for the spline’s value. A slim bar known as the playhead travels down through the graph to mark the current time, much as it does in the Timeline Editor. Drag the playhead and the current time shifts, refreshing whatever frame the viewers show. Stripping a spline off a parameter takes the animation away with it Spline Editor Header The header gives you a way to decide which splines show up in the graph. It lists each spline in the project under the tool that holds that parameter. Next to every name a checkbox signals whether that spline is on display in the graph and whether it can be edited.

### The Spline header

### Spline Editor Toolbar

Running along the foot of the Spline Editor, the toolbar gathers the operations most often performed on an animation spline. Every operation it carries is reachable from the graph’s context menu too, but these buttons offer a quicker shortcut.

### Spline toolbar buttons

### Playhead

The playhead is that slim red vertical bar passing down through the Spline Editor graph to stand for the comp’s current time. Drag it and the current time changes.

### Status Bar

Down in the Fusion window’s lower-right corner, the status bar steadily reports where the pointer sits, together with the time and value axes.

### Contextual Menus

Two contextual menus can be reached from the Spline Editor. A right-click over the graph brings up the Spline contextual menu, whereas a right-click on the Time Ruler above the graph brings up the Guide contextual menu.

Right-click on the horizontal axis Time Ruler for the Guide menu

### Renaming Splines

Whatever a spline is called in the header takes after the parameter it drives. To rename a spline, right-click it within the header and pick Rename Spline from the contextual menu.

### Changing Spline Colors

Every spline in the graph gets its own distinct color, which makes telling them apart simpler whenever several are on screen together. While a spline is active, a round color swatch shows up beside that spline’s name in the header. To recolor a spline: 1 Click the color circle sitting next to the spline name in the header. 2 Or right-click that spline’s name in the header and pick Change Color from the contextual menu. 3 Pick the new color out of the dialog box that opens and click OK.
