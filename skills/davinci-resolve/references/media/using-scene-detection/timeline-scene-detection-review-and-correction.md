# Scene cut detection on the timeline and checking and fixing your results

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using scene detection.
[Chapter index](INDEX.md) / [Next section](scene-detection-cut-list-and-options.md)
<a id="source-checking-and-fixing-your-results"></a> <a id="source-cut-list"></a> <a id="source-detection-graph-displays-potential-scene-cuts"></a> <a id="source-scene-cut-detection-on-the-timeline-studio-version-only"></a> <a id="source-scene-detect-window"></a> <a id="source-scene-detection-in-the-media-page"></a> <a id="source-the-scene-detect-graph"></a> <a id="source-the-scene-detect-viewer-transport-controls"></a> <a id="source-the-scene-detect-viewers"></a> <a id="source-the-scene-detect-window-interface"></a> <a id="source-using-scene-detection"></a> <a id="source-using-scene-detection-1"></a>

### Using Scene Detection

When a program arrives as one continuous media file and no EDL came with it to break the file apart, DaVinci Resolve’s Scene Detect window can locate the cut points for you and carve the file into separate clips that are ready to grade.

### Scene Cut Detection on the Timeline (Studio Version Only)

To take an already-cut video apart into its constituent clips for re-editing or color work, you can now handle the whole thing inside an Edit or Cut page Timeline. The DaVinci Neural Engine lets DaVinci Resolve examine an edited sequence on its own and divide it into separate clips. Should you rather, the original Scene Cut Detection tool in the Media Pool, covered later in this chapter, remains available. To use Scene Cut Detection on the Timeline: 1 Place one or several clips you intend to break apart on the Timeline. When your clips sit across more than a single video track, you can lock or unlock tracks individually so the detection only touches the video tracks you choose. You can also confine Scene Cut Detection to part of a clip alone by marking In and Out points on the Timeline that bracket the stretch you want examined. 2 Choose Timeline > Detect Scene Cuts. Up comes a dialogue box reading “Detecting scene cuts in clips x of x.” The wait varies with the duration, count, and intricacy of whatever clips you picked. After the Scene Cut Detection wraps up, your chosen clip ends up split into a run of through edits that can then act as standalone clips.

### Checking and Fixing Your Results

Should the Neural Engine get something wrong, you’re able to correct it by hand: move to the cut with the Up and Down Arrow keys to step through the Timeline, then do one of these:

- To remove a Cut: Select the through edit by clicking it, then hit the “Delete” key.
- To make a New Cut: Set the timeline indicator on the cut point, then choose Timeline >

Split Clips (Command-\).

One clip of a completed edit, made up of several cuts, shown prior to the Detect Scene Cuts command

Several separate clips pulled out of the edited clip with Detect Scene Cut; the In and Out points kept the operation bounded, and one of the through edits that resulted shows up highlighted in green.

### Scene Detection in the Media Page

Automatic scene detections can still be run with the original tools over in the Media page. One thing worth remembering about the original Media page Scene Detection is that the chosen clip gets analyzed and split inside the Media Storage panel, before that clip ever joins the Media Pool. Here’s how to load a clip into the Scene Detect window: 1 Head to the Media page, then find and select, via the Media Storage browser, whichever clip you want carved apart. A clip you mean to scene-detect shouldn’t be brought into the Media Pool first. The clip needs Scene Detection run on it before any import happens. 2 On that file, right-click and pick Scene Cut Detection. 3 Holding the clip you picked, the Scene Detect window now appears. 4 Hit the Auto Scene Detect button at the lower left of the interface. DaVinci Resolve runs through the chosen scene and studies the footage for likely cut points.

### The Scene Detect Window Interface

There are three principal regions in the Scene Detect window: the viewers, the Graph, and the Cut List. Working together, these controls let you study the movie, inspect the cuts that were found automatically, and ready the Cut List for return to your project.

### Scene Detect window

### The Scene Detect Viewers

Three viewers sit along the top of the Scene Detect window, a single main viewer plus a pair of smaller picture-in-picture (PiP) viewers. The trio exists so you can readily tell whether the playhead in the Scene Detect Graph happens to land on a cut point. The PiP viewer on the left holds the final outgoing frame at a detected cut point. The frame shown in the main viewer is the first incoming frame at that cut point, while the PiP viewer on the right gives the second incoming frame there. When the playhead in the Scene Detect Graph sits squarely over an edit point, the leftmost viewer ought to display an entirely different frame from the center and rightmost viewers, and those two should closely resemble each other. When that holds, you’ve located a correct cut point. The example below shows this. In the Scene Detect viewers you see the final frame of the outgoing clip alongside the opening two frames of the incoming clip. A left viewer that differs markedly from the main and right viewers points to a correct cut point. Should all three viewers seem to show one unbroken run of frames, then what you’re seeing isn’t a cut point.

No scene cut here as all images are almost the same. A row of controls sits below the viewers.

### The Scene Detect viewer transport controls

- Transport controls: Seven of them are provided — namely first frame and step back, then play reverse, stop, and play forward, followed by step forward plus last frame.

The In, Out, Prune, and Show Cut List controls

- In: Places an In point that marks one end of a range of the Scene Detection Graph you want to prune.
- Out: Places an Out point that marks one end of a range of the Scene Detection

Graph you want to prune.

- Prune: Should you spot plenty of false-positive scene cuts (say, a cluster of

cuts that line up with a dissolve between two shots), bracket the undesirable stretch of scene cuts in the Scene Detect Graph with the In and Out buttons, then click Prune; this clears every scene cut between those points that sits within a frame of another scene cut. From each identified group, the cut with the highest probability stays and the rest get deleted.

(Left) Bracketing scene cuts for pruning with In and Out points, (Right) What you get after clicking the Prune button to clear every unwanted scene cut except one

- Show Cut List: Toggles the Cut List on and off; that list holds the scene cuts found so far.

### The Scene Detect Graph

Most of the lower half of the Scene Detect window, over toward the left, is taken up by the Scene Detect Graph, which presents the scene detect analysis once you’ve hit the Start button. Whatever frames DaVinci Resolve judges to be cut points show up as green vertical “scene cuts” at differing heights. A given scene cut’s height reflects how probable it is that the frame truly marks an edit point rather than a swish pan, an abrupt jump in frame motion, or a sharp shift in color or lighting — any of which can trick the scene detection algorithm. A horizontal magenta confidence bar lets you set how much confidence a scene cut needs before it joins the Cut List. Dragging that bar upward past any low-confidence shorter scene cuts turns those lines gray and drops them from the Cut List.

### Detection graph displays potential scene cuts

NOTE: Dissolves and the rest of the transitions don’t get detected on their own, though a dissolve will usually show up as a triangular cluster of lines that peaks at its center. Below the graph sit four controls. Auto Scene Detect: This kicks off the scene cut detection process. Add: Drops a scene cut by hand at wherever the playhead currently sits. Now and then a pair of neighboring clips with close color and lighting will read as one clip to the scene detection algorithm. This option lets you insert scene cuts at frames where none were found at first. Delete: Removes by hand a scene cut sitting at the spot of the current frame indicator inside the graph. Zoom slider: Zooms the Scene Detect Graph in or out so you can study the results with more or less detail.

### Cut List

Down at the lower right of the Scene Detect window, the Cut List shows a single row for every scene cut that crosses the confidence bar. Three columns give each cut’s order number, frame number, and timecode value. Items in the Cut List can be selected so you can judge each cut with the three viewers up top. Each time you pick a fresh item in the Cut List, the playhead leaps to that frame within the Scene Detect Graph.
