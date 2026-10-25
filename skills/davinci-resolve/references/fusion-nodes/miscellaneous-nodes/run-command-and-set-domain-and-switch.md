# Run command and set domain and switch

Version: DaVinci Resolve 20.3 Reference Manual. Context: Run command, Set domain, Switch.
[Chapter index](INDEX.md) / [Previous section](frame-average-and-keyframe-stretcher-and-run-command.md) / [Next section](switch-and-time-speed-and-time-stretcher.md) / [Run Command Run](frame-average-and-keyframe-stretcher-and-run-command.md)
<a id="source-basic-node-setup-4"></a> <a id="source-common-controls-1"></a> <a id="source-common-controls-2"></a> <a id="source-controls-tab-2"></a> <a id="source-example"></a> <a id="source-frame-tab"></a> <a id="source-fusion-2554"></a> <a id="source-inputs-4"></a> <a id="source-inputs-5"></a> <a id="source-inspector-2"></a> <a id="source-inspector-3"></a> <a id="source-set-domain-dod"></a> <a id="source-set-domain-node-introduction"></a> <a id="source-start-and-end-tabs"></a> <a id="source-switch-node-introduction"></a> <a id="source-switch-swi"></a> <a id="source-the-run-command-end-tab"></a> <a id="source-the-run-command-frame-tab"></a> <a id="source-the-run-command-start-tab"></a> <a id="source-the-set-domain-controls-tab-in-adjust-mode"></a> <a id="source-the-set-domain-controls-tab-in-set-mode"></a> <a id="source-the-set-domain-node"></a> <a id="source-the-switch-node"></a>

### Inspector

### The Run Command Frame tab

### Frame Tab

Within the Frame tab you choose and tweak the command that will execute. Hide Tick the Hide checkbox so the application or script throws up no window as it runs. Wait Tick this checkbox to make the node pause until a remote application or tool exits before it carries on. With this checkbox cleared, the Fusion keeps rendering and doesn’t wait on the external application. Frame Command Here you enter the path for the command meant to run once each frame finishes rendering. You can rely on the Browse button to locate the path. Interactive This checkbox sets whether the launched application runs interactively, accepting user input. Number A (%a) and Number B (%b) A variety of wildcards work with the frame commands; at render time these wildcards get swapped out for the appropriate values.

- %a: Emits the value held in the Number A thumbwheel control.
- %b: Emits the value held in the Number B thumbwheel control.
- %t: Emits the current frame number (with no zero padding).
- %s: Drops in the text taken from the large text entry field.

Should you wish to prepend zero padding to the numbers that %t produces, write the wildcard as %0x, with x standing for how many characters to pad the value to. The same trick applies to %a and %b. As an illustration, test%04t.tga would yield these values come render time: test0000.tga test0001.tga test0009.tga test0010.tga A value can also be padded with spaces by invoking the wildcard as %x, where x is the count of spaces you’d like to pad the value with.

### The Run Command Start tab

### The Run Command End tab

### Start and End Tabs

Each of the Start and End tabs holds a file browser for a command that runs as the composition begins rendering and as the composition wraps up rendering.

### Example

Suppose you want each rendered frame copied off to a different directory as it’s produced; into the root folder, namely C\, place a file named copyfile.bat carrying the text below. @echo off set parm=%1 %2 copy %1 %2 set parm= Build or open any node tree holding a Saver. This example presumes the Saver outputs D\ test0000.exr, test0001.exr, etc. You might need to adjust the example so it lines up. Tack a Run Command node onto the Saver so the Saver wraps up saving first. Now, in the Frame Command text box belonging to the Run Command node, key in: C\copytest.bat D\test%04f.exr C\ Tick the Hide Frame command checkbox so the Command Prompt window doesn’t flash up momentarily after each frame. As this node tree renders, every file gets copied to the C\ directory the instant it’s rendered. You could put the Run Command node to work shipping files over FTP to a remote network drive, printing each frame as it renders, or kicking off a custom imageprocessing tool. Plain batch files aren’t the limit of what the Run Command node can run, either. FusionScript, VBScript, Jscript, CGI, and Perl files are all fair game, to name a handful.

### Common Controls

Settings Tab This same Settings tab within the Inspector recurs on the rest of the miscellaneous nodes too. Detailed coverage of these common controls waits at the chapter’s end, under the “The Common Controls” section.

### Set Domain [DOD]

### The Set Domain node

### Set Domain Node Introduction

Set Domain serves to tweak or define an image’s active region — the part of the image regarded as holding valid data. The image‘s physical dimensions stay untouched. Anything beyond the Domain of Definition (DoD) goes unprocessed by downstream nodes, which speeds up rendering for computation-intensive nodes. The node offers an absolute mode for defining the domain of definition by hand, plus a relative mode for nudging the existing domain of definition.

### Inputs

The pair of inputs on the Set Domain node are where you attach 2D images. Input: The orange background input has to be wired up. It takes a 2D image whose DoD you intend to replace or adjust. Foreground: The green image input is optional yet likewise takes a 2D image. With the foreground input connected, the Set Domain node swaps the Background input’s domain of definition out for the foreground’s DoD.

### Basic Node Setup

The example below presumes an image is wired into a Set Domain node so the DoD can be configured by hand.

A Set Domain node defines, by hand, the region that bounds image processing.

### Inspector

### The Set Domain Controls tab in Set mode

### The Set Domain Controls tab in Adjust mode

### Controls Tab

Mode The Mode menu presents two options, the choice resting on whether you mean to nudge or offset the current domain or instead lock in exact values for it. Either Set or Adjust mode can carry out the same operations. Under Adjust mode, each slider sits at a default of 0, which marks its own full extent of the image. Positive values pull the DoD inward while negative values push the DoD outward to take in more data. Set mode starts out at the full extent of the visible image. By default the sliders run on a 0-1 scale, left to right and bottom to top. Left Sets the DoD’s left edge. Raising this slider drives the left edge rightward, leaving out more data along the left margin. Here 1 stands for the image’s right edge and 0 for its left edge. The slider’s default is 0 (left border). Bottom Sets the DoD’s bottom edge. Raising this slider drives the bottom edge upward, leaving out more data along the bottom margin. Here 1 stands for the image’s top edge and 0 for its bottom edge. The slider’s default is 0 (bottom border). Right Sets the DoD’s right edge. Raising this slider drives the right edge leftward, leaving out more data along the right margin. Here 1 stands for the image’s right edge and 0 for its left edge. Within Set mode, the slider defaults to 1 (right border). Top Sets the DoD’s top edge. Raising this slider drives the top edge downward, leaving out more data along the top margin. Here 1 stands for the image’s top edge and 0 for its bottom edge. Within Set mode, the slider defaults to 1 (top border).

### FUSION 2554

### Common Controls

Settings Tab Here again, the Settings tab in the Inspector shows up on the other miscellaneous nodes as well. These common controls get spelled out fully toward the chapter’s close, in the “The Common Controls” section.

### Switch [Swi]

### The Switch node

### Switch Node Introduction

Switch is a tool that lets artists flip among several input sources, picking a single output from whichever inputs they’ve chosen. That ability is particularly handy for flipping between different visual elements inside a composition. How many input connections there are can vary, since the node accommodates a dynamic count of inputs that you can rename whenever you like. Through controls on the Config tab, users add or drop inputs and edit their names. Most kinds of tools, Shapes and 3D included, work with Switch. On top of that, you’ll spot the Switch modifier under a control’s context menu — in both its Modify With submenu and its Insert submenu — so it can be attached to any supported control.

### Inputs

By means of the slider in the Config tools, you can attach as many as nine inputs to a Switch Node. Need more than nine sources? Just key the figure into the Number of Inputs field by hand.
