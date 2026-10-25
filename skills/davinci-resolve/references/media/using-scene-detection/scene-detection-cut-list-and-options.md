# Cut list shows all currently detected cuts and scene detect options drop down menu

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using scene detection.
[Chapter index](INDEX.md) / [Previous section](timeline-scene-detection-review-and-correction.md)
<a id="source-an-example-scene-detect-workflow"></a> <a id="source-the-cut-list-shows-all-currently-detected-cuts"></a> <a id="source-the-scene-detect-options-drop-down-menu"></a>

### The Cut List shows all currently detected cuts

To select items in the Cut List:

- Click any item in the Cut List.
- Hit N (next) or the Down Arrow to move the selection to the next item down.
- Hit P (previous) or the Up Arrow to move the selection to the item above.

While you travel through the list, you can drop any items the viewers confirm aren’t genuine cuts. When the list runs long and there’s no time to go through it in one sitting, you can store it for later with commands in the Scene Detect Options drop-down menu. After you’ve gone over the list and trust that every cut is right, it can split the media file into separate clips in the Media Pool when you click “Add Cuts to Media Pool,” which sits just beneath it.

### The Scene Detect Options Drop-down Menu

A range of commands lives in the Options drop-down menu at the top-right corner of the Scene Detect window.

- Reset Zoom: Adjusts the Scene Cut Graph’s zoom level so the whole clip fits across the present width.
- Reset Marks: Wipes out whatever In and Out points you currently have set.
- Prune Scene Cuts: Should you spot plenty of false-positive scene cuts (say, a

cluster of cuts that line up with a dissolve between two shots), bracket the undesirable stretch of scene cuts in the Scene Detect Graph with the In and Out buttons, then click Prune Scene Cuts; this clears every scene cut between those points that sits within a frame of another scene cut. From each identified group, the cut with the highest probability stays and the rest get deleted.

- Save Scene Cut: Writes the current scene cut detection data, the probability metadata included, out to disk. Scene Cut files carry the file extension .sc and can be brought back in afterward to pick up a long scene detection job where you left off.
- Load Scene Cut: Brings an existing .sc file into the Scene Detect window. The media file you’re on has to be opened into the Scene Detect window first before a Scene Cut file can be loaded.
- Save EDL: Exports the Cut List as a CMX-style EDL.
- Load EDL: Brings a CMX-style EDL into the Cut List so the cut data from that EDL can feed the Scene Cut Detection process.
- Auto Cue: While turned on, the playhead hops to every new scene cut the moment it’s detected once you start scene detection. That lets you assess each scene cut as it turns up through the three viewers up top.

### An Example Scene Detect Workflow

What follows lays out an ideal way to work through scene detection when no EDL is present. To scene detect a media file: 1 Use the Media Storage browser of the Media page to find a media file you want to scene detect. 2 Confirm its frame rate and whether it relies on drop-frame timecode, and be sure the “Timeline frame rate” lines up with the “Use drop frame timecode” parameter over in the Master Settings panel of the Project Settings. Those parameters don’t set themselves when the project already holds media in the Media Pool, and mismatches with your media can cause trouble. 3 Right-click the media file, and choose Scene Cut Detection. 4 Once the Scene Detect window comes up, open the Options drop-down menu and pick Auto Cue (it’s usually on already, but a quick check never hurts), then click Auto Scene Detect. Scene detection begins, and you can assess each scene cut the moment it appears. If a scene cut seems off (three frames in a row in sequence), jot down where it falls in the list so you can revisit it. 5 After DaVinci Resolve completes scene detection, take the playhead to a few of the shorter scene cuts and confirm whether they’re real cuts with the three viewers up top. When the frames shown read “different-same-same,” it’s a true cut. When they read “same-same-same” (really three sequential frames), those aren’t cuts.

TIP: Rapid camera movement like whip pans, abrupt brightness shifts like camera flashes, or even film reaching speed and making the shutter “flash” can throw off the analysis, since it watches for big changes across the image. 6 When there are plenty of low-confidence scene cuts you’ve confirmed aren’t cuts, drag the magenta confidence bar down so those low-confidence scene cuts drop beneath it and clear them all from the list at once. 7 After that, you might want to work down the Cut List, checking each scene cut to confirm it’s right. Click the first scene cut on the list, check it, then hit the keyboard Down Arrow key to move to the following list item down, check that one, and keep going until every item on the list is checked. To head back up the list, the Up Arrow key selects the previous list item. Whenever an item isn’t a cut point, click the “Delete” button in the bottom-left corner of the Scene Detect window to clear that scene cut. 8 Where parts of the Scene Detect Graph hold thick clusters of spikes, those are likely frames whose kinds of motion fooled the Scene Cut Detector. To clear this unwanted “noise” out of the data, isolate it with the In and Out buttons, then click “Prune” to drop these unwanted scene cuts. 9 Whenever there’s a gap between two scene cuts where you’re sure another scene cut belongs, scrub the playhead or rely on the transport controls to find the absent cut, then click the “Add” button in the bottom-left corner of the Scene Detect window to put in another scene cut. TIP: Neighboring shots whose color and contrast ranges sit very close together can occasionally slip past the scene detection algorithm. When you’re aware of scenes like that in the footage you’re analyzing, it’s worth scrubbing through them a little more carefully so nothing gets overlooked. Even so, if a missed cut turns up afterward, the Split Clip control in the Edit page timeline can always add a fresh edit point. 10 Once you trust that the Cut List is right, click “Add Cuts to Media Pool” to break the media file into separate clips inside the Media Pool. 11 Should the Conform Settings dialog come up, click OK provided you already confirmed your settings back in step 2. 12 Close the Scene Detect window. Those separately carved clips from the media file you analyzed now appear in the Media Pool, ready for you to lay the entire run of clips, in order, into a fresh Timeline for grading.
