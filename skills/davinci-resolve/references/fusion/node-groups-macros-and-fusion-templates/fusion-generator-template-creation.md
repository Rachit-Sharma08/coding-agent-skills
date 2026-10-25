# Getting started with a Fusion generator template and creating a Fusion generator template

Version: DaVinci Resolve 20.3 Reference Manual. Context: Node groups macros and Fusion templates.
[Chapter index](INDEX.md) / [Previous section](fusion-title-template-creation.md) / [Next section](creating-a-fusion-effect-template.md)
<a id="source-creating-a-fusion-generator-template"></a> <a id="source-getting-started-with-a-fusion-generator-template"></a> <a id="source-saving-a-new-fusion-generator"></a> <a id="source-using-your-new-generator-template"></a>

### Getting Started with a Fusion Generator Template

The Effects Library holds a single, simple Noise Gradient Fusion Generator you can take as a launching point for building generators of your own.

The Fusion Generator templates sitting inside the DaVinci Resolve Effects Library. To bring the Fusion Noise Gradient Generator up on the Fusion page, do this: 1 Over on the Edit page, pull the Fusion Noise Gradient Generator from the Effects Library onto the Timeline. 2 Right-click over the Noise Gradient Generator and pick Open in Fusion Page off the pop-up menu.

Up comes the Fusion page, laying out the node tree behind the Fusion Generator.

### Creating a Fusion Generator Template

Simple as it is to start from the Noise Gradient Generator template, you can just as readily begin by dropping a Fusion Composition Effect onto a Timeline on the Edit page. To set out making a Fusion Generator Template from an empty Fusion composition, go like this: 1 Over on the Edit page, pull the Fusion Composition Effect from the Effects Library onto the Timeline. 2 Right-click over the Composition Effect and pick Open in Fusion Page off the pop-up menu.

An empty Fusion page carrying one solitary MediaOut node opens, set for you to build a Fusion Generator. The Fusion Generator is a solid image produced from however many tools you combine to form a static or animated background. You may opt to blend gradient colors, masks, paint strokes, or particles in 2D or 3D to form the background generator you’re after.

The Fusion Generator node tree creating concentric circles.

### Saving a New Fusion Generator

Having built the generator you want in Fusion, you’ll need to store it to the Effects Library for reuse across other projects from the Edit page. Doing so means building a Macro and storing it in the Generator folder. As a rule, macros act as building blocks within Fusion, letting you fold the compositing tricks you reach for constantly into nodes of your own. Even so, you likewise put this macro capability toward making Generator templates for the DaVinci Resolve Edit page. Begin by picking every node in the Node Editor you want folded into the Generator template, the MediaOut node included. With that selection made, give one of the chosen nodes a right-click and pick Macro > Create Macro off the contextual menu.

The Macro Editor displaying the parameters of all the nodes you selected. Up comes the Macro Editor window, laying out a hierarchical list of every parameter in the composition you’ve just picked. The node order follows the sequence in which they were picked in the Node Editor before the macro was made. The point of the Macro Editor is to let you decide which parameters get shown as custom controls in the Edit page Inspector once the Generator is applied. You can settle on a pared-down set of parameters for customization by ticking the checkboxes beside any parameter name. After switching on every parameter you want in the eventual template, hit the Close button, and a Save Macro As dialog comes up. Here you can type the Transition’s name, as it ought to read in the Edit page Effects Library.

To make the Generator template show up in the Effects Library > Fusion Generators category of DaVinci Resolve, store the macro in these locations: On macOS: `Macintosh HD/Users/username/Library/Application Support/Blackmagic Design/ DaVinci Resolve/Fusion/Templates/Edit/Generators` On Windows: `C:\Users\username\AppData\Roaming\Blackmagic Design\DaVinci Resolve\ Support\Fusion\Templates\Edit\Generators` On Linux: `home/username/.local/share/DaVinciResolve/Fusion/Templates/Edit/Generators`

### Using Your New Generator Template

With your macro saved, you’ll have to quit DaVinci Resolve and launch it again. Opening the Effects Library on the Edit page, the new Generator template shows under the Generators category, in the Fusion Generators list.

A custom Fusion Generator stored within the Edit page Effects Library. Drop this Generator onto the Timeline, open the Inspector, and whatever parameters you left editable show up, should there be any.
