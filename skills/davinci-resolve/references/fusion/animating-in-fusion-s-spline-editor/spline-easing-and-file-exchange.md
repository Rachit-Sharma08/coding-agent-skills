# Spline easing and file exchange

Version: DaVinci Resolve 20.3 Reference Manual. Context: Animating in Fusion s spline editor.
[Chapter index](INDEX.md) / [Previous section](ease-in-out.md)
<a id="source-importing-and-exporting-splines"></a> <a id="source-the-ease-inout-controls-above-the-graph-area"></a>

### The Ease In/Out controls above the graph area

Hit the Lock In/Out button and the pair of sliders merges into a single one, which makes every tweak land on both direction handles at once.

### Importing and Exporting Splines

Moving spline shapes into or out of an ASCII text file is fully supported. That convenience lets you bank elaborate spline curves to reuse down the road, or hand tracking, path, and animation data off between applications. Any spline you export picks up the .spl file extension so it’s simple to spot. Exporting works as follows: 1 In the Spline Editor, highlight whichever spline is active. 2 Right-click the spline within the graph area to bring up the contextual menu, then pick Export. 3 Pick one of the three format choices the submenu offers. 4 Type a name and folder into the file browser dialog before clicking Save. Three choices are on the table when you export: Samples, Key Points, or All Points. Samples drops a control point onto every frame so the spline is reproduced faithfully. Key Points mirrors the spline’s control-point placements and values while relying on linear interpolation. All Points writes the spline out exactly as it appears in the Spline Editor, carrying over the identical position, value, and interpolation. Bringing one in goes like this: 1 For the parameter, attach an animation spline. 2 Inside the Spline Editor, right-click the animation spline and pick Import Spline off the contextual menu. 3 Within the File Browser dialog, choose the spline curve .spl file, then click Open. Pulling in a new curve overwrites whatever animation already sat on the chosen spline.
