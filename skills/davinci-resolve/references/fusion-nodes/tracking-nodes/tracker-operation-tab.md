# Tracker operation tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Tracker.
[Chapter index](INDEX.md) / [Previous section](tracker-pattern-list-and-trackers-tab.md) / [Next section](tracker-layering-merge-and-position-controls.md) / [Tracker Tra](tracker-a-tracker-node-branched-from-the-node-tree.md)
<a id="source-operation-menu"></a> <a id="source-operation-tab"></a> <a id="source-the-tracker-operation-tab"></a>

### Operation Tab

Whereas the Trackers tab controls let you shape how the Tracker node studies motion to build motion paths, the Operation tab takes that studied motion data and puts it to work, carrying out image transforms of assorted kinds. A wide range of jobs falls within the Tracker node's reach, anything from match moving an object into a moving scene, to steadying a shaky camera move, to swapping out the content of a sign. Turn to the options and buttons on the Operation tab to choose what job the Tracker node performs.

### The Tracker Operation tab

### Operation Menu

Four jobs that the Tracker performs are held within the Operation menu. The rest of the controls on this tab fine-tune whatever that selection produces.

- None: Beyond simply locating and tracking the pattern you chose, the Tracker carries out no further operation on the image. This is the default mode, relied on to build a path that will subsequently drive some other parameter on another node.
- Match Move: With only the orange background input hooked up, this mode steadies the image. Once a foreground image is wired into the green foreground input, that foreground image follows along in position, rotation, and scaling according to the tracking patterns. Both stabilizing and match move call for at least one tracking pattern to fix position, and two or more to fix scaling and rotation.
- Corner Positioning: The Corner Positioner mode tracks a rectangular object's four corners and swaps its contents out for a fresh image. At minimum, four tracking patterns are required for this function. Where there aren't enough tracking patterns, fresh tracking patterns get added until the tally hits four.
- Perspective Positioning: This mode runs the reverse of the Corner Positioning mode. Instead of swapping out the rectangle's contents, the four trackers are mapped onto the image's four corners. Its typical use is stripping perspective out of an image. As with the Corner Positioning mode, this one needs four tracking patterns, which get tacked on automatically should fewer patterns exist.
