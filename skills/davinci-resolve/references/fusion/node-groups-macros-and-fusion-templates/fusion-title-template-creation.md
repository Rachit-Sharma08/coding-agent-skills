# Creating Fusion templates and getting started with a Fusion title template

Version: DaVinci Resolve 20.3 Reference Manual. Context: Node groups macros and Fusion templates.
[Chapter index](INDEX.md) / [Previous section](groups-and-creating-groups.md) / [Next section](fusion-generator-template-creation.md)
<a id="source-and-thats-it"></a> <a id="source-creating-a-fusion-transition-template"></a> <a id="source-creating-fusion-templates"></a> <a id="source-getting-started-with-a-fusion-title-template"></a> <a id="source-getting-started-with-a-fusion-transition-template"></a> <a id="source-saving-a-new-fusion-transition"></a> <a id="source-saving-a-title-macro"></a> <a id="source-updating-a-fusion-transition"></a> <a id="source-using-your-new-title-template"></a> <a id="source-using-your-new-transition-template"></a>

### Creating Fusion Templates

Folding Fusion into DaVinci Resolve opened the door to making Fusion Titles, Transitions, Effects, and Generators templates meant for the Edit page. These templates can be authored on the Fusion page or within Fusion Studio, then copied across into DaVinci Resolve. At heart, Fusion Titles, Generators, and Transition templates are comps authored in Fusion yet editable, with custom controls, on the Edit page Timeline. This section walks you through the process.

### Getting Started with a Fusion Title Template

Step one in making a Fusion title template is assembling a Fusion composition out of Fusiongenerated objects put together to form just about any title or generator you can dream up. If you’re feeling really ambitious, animation can go in too. Here, 3D titles and 2D titles have been merged into a show opener.

Building a composition to turn into a title template.

### Saving a Title Macro

At bottom, macros are Fusion compositions converted into self-contained nodes. As a rule, such nodes act as building blocks within Fusion, letting you fold the compositing tricks you reach for constantly into nodes of your own. Even so, you can put this macro capability toward making title templates for the Edit page. With your composition assembled, pick every last node you want folded into that template apart from the MediaIn and MediaOut nodes in DaVinci Resolve, or, over in Fusion Studio, the Loader and Saver nodes. Picking out the nodes destined to become a title template. TIP: Should you wish to govern the sequence in which node controls show up afterward, Command-click each node you mean to fold into the macro, one after another, following the order you want controls from those nodes to appear. It’s one more step, yet it keeps matters tidier later on. With that selection made, give one of the chosen nodes a right-click and pick Macro > Create Macro off the contextual menu.

Up comes the Macro Editor window, packed to the gills with a tiered listing of every single parameter belonging to the composition you’ve just picked.

The Macro Editor filled out with the parameters drawn from all the nodes you picked. Daunting as this list may seem, collapsing the disclosure control of the topmost Text1 node lays bare what’s actually happening.

A simple list of all the nodes we’ve selected. Collapsing the top node’s parameters lays bare a plain list of all the nodes we’ve picked. The point of the Macro Editor is to let you decide which parameters get exposed as custom editable controls for that macro. Whatever controls you settle on turn up in the Inspector each time you pick that macro, or the node or clip the macro becomes.

So the only thing left now is to switch on the checkboxes of every parameter we’d care to customize. Here, our ticks will land on the Styled Text checkbox belonging to the Text3D node, then the Diffuse Color, Green, and Blue checkboxes on the Cloth node, plus the Z Rotation checkbox over on the SpotLight node — leaving just the template’s middle word open to edits, though we get to recolor it and tip its lighting too (which makes a “swing-on” effect attainable).

Ticking the checkboxes for whichever parameters we mean to adjust once this serves as a template. After switching on all the parameters we want in the eventual template, we hit the Close button, and a Save Macro As dialog comes up. To make the Title template show up in the Effects Library > Titles category of DaVinci Resolve, store the macro in these locations: On macOS: `Macintosh HD/Users/username/Library/Application Support/Blackmagic Design/ DaVinci Resolve/Fusion/Templates/Edit/Titles` On Windows: `C:\Users\username\AppData\Roaming\Blackmagic Design\DaVinci Resolve\ Support\Fusion\Templates\Edit\Titles` On Linux: `home/username/.local/share/DaVinciResolve/Fusion/Templates/Edit/Titles`

Picking the spot to store an Edit page title template within DaVinci Resolve.

### Using Your New Title Template

With your macro saved, you’ll have to quit DaVinci Resolve and launch it again. Opening the Edit page Effects Library, you should spot your new template within the Titles category, set to go in the Fusion Titles list.

Within the Effects Library, the Fusion Titles section is where custom titles turn up. Once this template is edited onto the Timeline and the Inspector is opened, the parameters we made editable become visible, and they let us tailor the template to suit our own ends.

Customizing the template we made.

### And that’s it!

### Getting Started with a Fusion Transition Template

In building a Fusion transition template, the smoothest route is to begin from an existing transition template and extend it. The Fusion Transitions category of the DaVinci Resolve Effects Library holds three transitions. Of these, the Cross Dissolve is the plainest, whereas the Slice Push stands as the most involved example.

The Fusion transition templates located in DaVinci Resolve’s Effects Library.

### Creating a Fusion Transition Template

At their core, the three Fusion Transitions sitting in the DaVinci Resolve Effects Library are Fusion compositions that were turned into macros. As a rule, macros act as building blocks within Fusion, letting you fold the compositing tricks you reach for constantly into nodes of your own. Even so, you can put this macro capability toward making transition templates for the DaVinci Resolve Edit page. With a Fusion Transition applied on the Edit page, a right-click on it lets you pick Open in Fusion Page.

Right-clicking over a Fusion Transition in the DaVinci Resolve Edit page.

Up comes the Fusion page, showing off the node tree behind the Fusion transition.

The Cross Dissolve node tree in Fusion. On the Edit page Timeline, the outgoing clip is stood in for by the MediaIn 1 node. The incoming clip is what the MediaIn 2 clip stands for. The Cross Dissolve effect can be tweaked or swapped out wholesale to craft a transition of your own using any of Fusion’s nodes.

The Fusion Cross Dissolve node tree swapped out for Transforms plus a Merge node. TIP: To change how long the Fusion transition runs from the Edit page Timeline, the Resolve Parameter Modifier has to be applied to whatever parameter is animated. Rather than keyframing the transition, you construct it through the Scale and Offset parameters of the Resolve parameter modifier.

### Updating a Fusion Transition

Having altered the transition in Fusion, you can opt to refresh the transition in the Timeline, or else make a fresh transition that you store into the Edit page Effects Library. To refresh the transition, simply head back to the Edit page. Whatever changes you apply on the Fusion page show through in the Edit page Timeline transition.

### Saving a New Fusion Transition

When, after altering the transition in Fusion, you need to store it to the Effects Library for reuse on other transitions or other projects, you must build a macro and store it in the Transitions folder. Begin by picking every node in the Node Editor you want folded into the transition template, the two MediaIn nodes and the MediaOut node included. TIP: Because the transition template has to carry the MediaIn and MediaOut nodes, the closing steps of saving a transition template must happen on DaVinci Resolve’s Fusion page and can’t happen in Fusion Studio.

With that selection made, give one of the chosen nodes a right-click and pick Macro > Create Macro off the contextual menu.

The Macro Editor displaying the parameters of all the nodes you selected. Up comes the Macro Editor window, laying out a hierarchical list of every parameter in the composition you’ve just picked. The node order follows the sequence in which they were picked in the Node Editor before the macro was made. The point of the Macro Editor is to let you decide which parameters get shown as custom controls in the Edit page Inspector once the transition is applied. With transitions, you may opt to show no controls at all in the Inspector, leaving only duration tweaks in the Timeline. Alternatively, you can settle on a pared-down set of parameters for customization by ticking the checkboxes beside any parameter name. After switching on every parameter you want in the eventual template, hit the Close button, and a Save Macro As dialog comes up. Here you can type the transition’s name, as it ought to read in the Edit page Effects Library. To make the transition template show up in the Effects Library > Fusion Transitions category of DaVinci Resolve, store the macro in these locations: On macOS: `Macintosh HD/Users/username/Library/Application Support/Blackmagic Design/ DaVinci Resolve/Fusion/Templates/Edit/Transitions` On Windows: `C:\Users\username\AppData\Roaming\Blackmagic Design\DaVinci Resolve\ Support\Fusion\Templates\Edit\Transitions` On Linux: `home/username/.local/share/DaVinciResolve/Fusion/Templates/Edit/Transitions`

### Using Your New Transition Template

With your macro saved, you’ll have to quit DaVinci Resolve and launch it again. Opening the Effects Library on the Edit page, the new transition template shows under the Video Transitions category, in the Fusion Transitions list.

A custom Fusion Transition stored within the Edit page Effects Library. Drop this transition onto a cut in the Timeline, open the Inspector, and whatever parameters you left editable show up, should there be any.
