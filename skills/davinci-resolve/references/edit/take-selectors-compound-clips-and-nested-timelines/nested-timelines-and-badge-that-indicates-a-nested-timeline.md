# Nested timelines and badge that indicates a nested timeline

Version: DaVinci Resolve 20.3 Reference Manual. Context: Take selectors compound clips and nested timelines.
[Chapter index](INDEX.md) / [Previous section](take-selectors-and-compositing-and-grading-take-selectors.md)
<a id="source-a-nested-timeline"></a> <a id="source-audio-buses-in-nested-timelines"></a> <a id="source-compositing-and-grading-nested-timelines"></a> <a id="source-converting-compound-clips-or-timelines-to-multicam-clips"></a> <a id="source-decomposing-in-place"></a> <a id="source-decomposing-nested-timelines"></a> <a id="source-editing-source-media-from-a-timeline-or-compound-clip"></a> <a id="source-match-frame-for-nested-timelines-and-compound-clips"></a> <a id="source-nested-timelines"></a> <a id="source-re-editing-a-nested-timeline"></a> <a id="source-swapping-the-contents-of-the-source-viewer-and-timeline"></a> <a id="source-the-badge-that-indicates-a-nested-timeline"></a> <a id="source-the-result-of-using-decompose-in-place"></a>

### Nested Timelines

Whole timelines, and parts of them, can be edited inside other timelines, either in part or entirely. As an example, when you've cut a program into scenes or reels so that each reel lives in its own separate timeline, you can edit every one of those timelines together, back-to-back, into a single timeline so as to put together a finished program.

Multiple timelines edited together into a single sequence

Clips that are nested timelines turn up with a distinctive badge sitting left of the timeline name.

### The badge that indicates a nested timeline

Timelines edit much like any other clip; you can pick one or more timelines and drag-and-drop them onto another timeline, drop them onto the Timeline Viewer editing overlay, or wield the toolbar editing buttons or keyboard shortcuts to edit them, exactly as you would any other clip. Beyond that, selecting several timelines within the Media Pool, then right-clicking and choosing Create Timeline Using Selected Clips, quickly gathers a batch of timelines into one nested sequence. The lone exception: you have to drag-and-drop a timeline into the Viewer if you mean to use it for setting In and Out points, given that double-clicking a timeline, or selecting a timeline and pressing Return, merely opens it into the Timeline Editor. You can, however, set In and Out points for timelines within the Filmstrip of the Media Pool, or you can edit one timeline into another in full, then trim its head and tail down to only what you need. A double-click on a nested timeline opens it into the Source Viewer for trimming, precisely like any other clip.

### Re-Editing a Nested Timeline

When you'd like to edit a nested timeline's contents, right-click it and pick Open in Timeline. In contrast to compound clips, no path control turns up here, since all you've done is open the original timeline. To get back to the timeline you came from, find and double-click it in the Media Pool, or select it via the Timeline drop-down sitting atop the Timeline Viewer. Editing an original timeline leaves untouched the running length of nested instances of that timeline living inside other timelines. Should you trim or delete clips in the original timeline that also show up in nested instances of it, then those stretches of the nested timeline simply go black.

### Swapping the Contents of the Source Viewer and Timeline

While you edit part of one timeline into another, it can help to view the contents of a timeline that's open in the Source Viewer inside the Timeline Editor. To pull that off, pick Timeline > Swap Timeline and Source Viewer (Command-Page Up). Whatever timeline sat open in the Source Viewer moves into the Timeline Editor, while the one that had occupied the Timeline Editor moves into the Source Viewer. That makes marking In and Out points easier as you watch the precise clip boundaries, ahead of hitting Command-Page Up once more, which trades the two panels' contents back and readies you for the next edit.

### Editing Source Media From a Timeline or Compound Clip

When you've got a timeline holding clips you'd like edited into another timeline, but as source clips rather than nested timeline segments, you can switch on Edit > Decompose Compound Clips on Edit. This mode decides whether a timeline gets edited into another as a nested timeline, or instead immediately broken down into its constituent source clips. Switching the mode on lets you edit source clips out of a timeline by drag-and-drop, 3-point edits, or whatever other method suits you. To return to editing nested timelines, switch Edit > Decompose Compound Clips on Edit off. The mode is particularly handy for workflows where you're piecing together “selects” timelines holding the best bits of various interviews or performances, which you intend later on to edit as sources into the actual program you're cutting. Marking Clips in Timelines Loaded into the Source Viewer As you edit Source Media out of a timeline that's loaded into the Source Viewer, you can rely on Mark Clip (the X key) to drop Viewer In and Out points lining up with the start and end of whichever clip crosses the playhead inside that timeline. This makes it simple to edit a single clip out of a Timeline in the Viewer into your program, entirely on its own.

(Left) a timeline sitting in the Source Viewer; (Right) a press of X drops In and Out points onto the clip under the playhead, set to edit

### Decomposing Nested Timelines

There are two principal ways to turn a nested timeline back into its constituent clips.

### Decomposing in Place

To break a nested timeline apart once it's already sitting edited inside another timeline, right-click it and choose Decompose in Place. The same works across several selected nested timelines all at once.

### A nested timeline

### The result of using Decompose In Place

Should the decomposed clip end up with extra audio, video, or subtitle tracks, then more tracks get added to the Timeline to fit them. If that poses a problem, you can rearrange the clips Decomposing Nested Timelines While Editing When you'd like to edit a whole timeline into another timeline purely as the source clips, switch on Edit > Decompose Compound Clips on Edit, then edit that timeline into your program by whatever method suits you, as laid out earlier in this chapter.

### Compositing and Grading Nested Timelines

Much like compound clips, nested timelines behave as a single clip within the Timeline; they turn up as a single MediaIn node on the Fusion page for compositing, and you can grade them as one clip on the Color page. That said, when you'd like to add effects to or grade the original clips inside a nested timeline one by one, you can either open that timeline out of the Media Pool, or right-click that clip and pick Open in Timeline so as to reach its constituent clips for compositing or grading.

### Audio Buses in Nested Timelines

Nest a timeline inside another timeline that's got buses configured for mixing on the Fairlight page, and every Sub and Aux routing behaves as intended within the nested timeline, which surfaces all channels of Main 1 in the enclosing timeline. Seen in this light, the nested timeline's audio works out to a submix that routes its resulting audio onto whatever audio track it lands on when edited. To read more about Buses and audio mixing broadly, consult Part 13, “Fairlight.”

### Match Frame for Nested Timelines and Compound Clips

The Match Frame to Source Clip feature works for compound clips along with nested timelines. Depending on the context, the relevant underlying source clip gets loaded into the Source Viewer. With a compound clip or timeline loaded into the Source Viewer, running a match frame (from the Source Viewer) has DaVinci Resolve give priority to locating a nested copy of the clip in the timeline so as to carry out the match frame. Where no nested copy turns up, the match frame runs automatically to line the underlying source clip up against a timeline instance. In the same way, running the match frame from the timeline (or timeline viewer) has DaVinci Resolve first try to locate the same underlying clip and frame inside the compound clip or nested timeline loaded into the Source Viewer. Should the frame prove impossible to locate, then match frame to source runs automatically as usual. This proves especially handy while you compare two different versions of a timeline and bounce between them.

### Converting Compound Clips or Timelines to Multicam Clips

Compound clips and timelines can be converted into multicam clips for smoother editing by way of the Edit page's Multicam Editing interface. The conversion only runs one way. There's no converting a multicam clip back into a timeline or compound clip. Should you want the original timeline or compound clip kept, be sure to duplicate it first and convert the duplicate. To dig deeper, consult Chapter 42, “Multicam Editing.” Turning a compound clip or timeline into a Multicam clip: Right-click the clip or timeline in the Media Pool and pick “Convert Compound Clips (Timelines) to Multicam Clips” off the drop down menu.
