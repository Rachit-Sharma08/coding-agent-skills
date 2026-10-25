# Creating a Fusion effect template changing durations of a template

Version: DaVinci Resolve 20.3 Reference Manual. Context: Creating a Fusion effect template.
[Chapter index](INDEX.md) / [Previous section](creating-a-fusion-effect-template.md) / [Creating a Fusion Effect Template](creating-a-fusion-effect-template.md)
<a id="source-changing-durations-of-a-template"></a> <a id="source-creating-a-custom-template-icon"></a> <a id="source-creating-media-drop-zones-in-templates"></a> <a id="source-using-fusion-template-bundles"></a>

### Changing Durations of a Template

Having built a template in Fusion, there will be times you want to alter its duration on the Edit or Cut page Timeline. Adjusting duration once animation enters the picture can get tricky, which is why Fusion offers two Modifiers to help govern keyframe behavior whenever those page Timelines have their duration changed. Anim Curves Modifier The Animation Curves Modifier (Anim Curves) serves to dynamically tune an animation's timing, values, and acceleration, even when you opt to revise a Comp's duration. With this Modifier in play, stretching or compressing animations, producing smooth motion, layering in bounce, or mirroring animation curves grows vastly simpler, sparing you the chore of hand-editing splines. As you author Fusion templates for the Edit or Cut page inside DaVinci Resolve, the Anim Curves Modifier lets the keyframed animation you built in Fusion stretch and compress as needed whenever a transition, a title, or an effect has its running time adjusted on those same Timelines. Keyframe Stretcher Modifier The Keyframe Stretcher modifier mainly comes into play when you author title templates in Fusion bound for DaVinci Resolve's Edit or Cut page. You attach the Keyframe Stretcher modifier to any animated parameter so that the Hold keyframes sitting between the opening on-screen animation and the closing off-screen animation stretch once the template is trimmed in the Timeline. By that means the animation holds onto its timing while the title's static stretch grows to satisfy the fresh duration.

### Creating Media Drop Zones in Templates

To make life easier on the Edit page, Fusion effects, plugins, and transitions can carry media drop zones, which let a user just drag clips straight from the Media Pool onto the template. As an example, you can swap a Fusion effect's background for a star-field in an instant, merely by dragging that clip out of the Media Pool and onto the media drop zone in the Inspector. Setting up a media drop zone inside a Fusion template goes like this: 1 Build a Macro from your current Fusion template. 2 On each MediaIn node you'd like to turn into a media drop zone, confirm the ClipName parameter is ticked. 3 Drop your template into the right Fusion Edit template folder (Transition, Effect, etc.) and relaunch DaVinci Resolve. From then on, using this template on the Edit page, you can drag clips out of the Edit page Media Pool and drop them into the Transition Inspector's Clip Name field. Doing so refreshes the template right away with whichever media you picked.

With the Clip Name parameters ticked on the MediaIn2 and MediaIn1 nodes inside the Macro Editor, media drop zones become available on both the incoming and outgoing ends of this Fusion transition.

A Media Pool clip being dropped onto a Clip Name field within the Transition Inspector that results, over on the Edit page

### Creating a Custom Template Icon

You're able to embed a custom icon into your template thumbnail within the Effects Library, taking the place of the template name's first three letters that appear by default. Making a basic Custom Template Icon works like this: 1 Produce a .png file of whichever icon you intend for the template. A size of 104 x 58 pixels is suggested, though any image gets resized to fit. 2 Give the file precisely the same name as your template, swapping a .png extension in for the .setting extension. 3 Put that .png image into the same directory where your template lives. After you restart DaVinci Resolve, the icon you made gets embedded into the template thumbnail throughout every Effects Library in the program.

A fisheye template shown with a Custom Icon applied, the left being before and the right after

### Using Fusion Template Bundles

So that templates pass easily to fellow Fusion users, several of them can these days be gathered into one .drfx file. That file then imports without fuss onto another Fusion workstation, keeping every custom template identical from one computer to the next. Building a Fusion Template Bundle means following a particular directory structure and leaning on your operating system's file browser plus its .zip compression utility. That directory structure appears below, and you can always track down a given folder from inside Fusion by right-clicking any bin in the Effect Library and choosing Show Folder. Folder structure for Templates used in the Edit page: Edit

- Effects
- Generators
- Titles
- Transitions The folder layout for Templates that the Fusion page uses: Fusion

Building a Fusion Template Bundle: 1 Within your OS, lay out the folder structure shown above so it holds the particular folder matching the template type you want bundled. Say you have one transition plus two effects templates; you'd make an Edit folder with two subfolders inside it called Transitions and Effects. 2 Copy your template (.setting) files into the right directories. Icon files and any related assets may go in as well. 3 Reach for your OS zip compression utility to turn that directory structure into a .zip file. 4 In your OS, rename the .zip file so it carries the “.drfx” extension in place of .zip. Its file icon ought to switch to mirror the new extension. Importing a Fusion Template Bundle: 1 Double-click a .drfx file within your OS. DaVinci Resolve starts up and a dialogue box appears asking whether you'd like to install the template bundle. 2 Drag the .drfx file from your OS straight onto the Fusion page in DaVinci Resolve. A dialogue box appears asking whether you'd like to install the template bundle. Removing a Fusion Template Bundle: 1 In your file browser, head to the relevant template directory. 2 Delete the .drfx file.

IMPORTANT: A Fusion Template Bundle keeps every template within a single file; it never unpacks them back into individual template files. As a result, deleting the .drfx file wipes out all the templates held inside that bundle along with it.
