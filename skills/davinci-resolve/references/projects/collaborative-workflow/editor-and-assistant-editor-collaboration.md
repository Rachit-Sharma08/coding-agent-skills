# Multiple editors working together and editors and assistant editors working together

Version: DaVinci Resolve 20.3 Reference Manual. Context: Collaborative workflow.
[Chapter index](INDEX.md) / [Previous section](collaboration-bin-and-timeline-locking.md) / [Next section](compositor-editor-and-colorist-collaboration.md)
<a id="source-collaborative-workflow-part-2"></a> <a id="source-editors-and-assistant-editors-working-together"></a> <a id="source-editors-and-compositing-artists-working-together"></a> <a id="source-multiple-editors-working-together"></a>

### Multiple Editors Working Together

Whoever opens a timeline first is the sole person allowed to make editorial changes to it on the Edit or Fairlight pages. Anyone else who opens that project is “locked out” of editing on the Edit or Fairlight pages, yet they can still view the Timeline and apply grading changes on the Fusion or Color pages. So whenever you’d like several editors going at one project, a good approach is to split your program into separate “reels,” with each reel sitting as its own timeline in its own bin. If, however, a couple or more editors truly have to work the same timeline, you can pull it off by duplicating the timeline and stitching the changes back together afterward. As an illustration, collaborating editor Anne might take these steps to revise a timeline that editor Erin already has open:

- To start, Anne can copy the locked timeline into a bin separate from the one Erin holds a lock on. Or Erin might get ahead of it and duplicate the timeline into a separate bin beforehand.
- Next, Anne re-edits her duplicate timeline, making whatever adjustments are needed to a scene other than the one Erin is busy with at the moment. Tackling different scenes is the tidiest and simplest way to run this workflow.
- Then, Anne uses Collaborative Chat to let Erin know the changes are done.
- Finally, Erin refreshes the project so Anne’s updated duplicate timeline shows up in the Media Pool,

then right-clicks it and picks Compare With Current Timeline from the contextual menu to bring up the Timeline Comparison window, which lets her fold the altered portion of the duplicate timeline into the original timeline Erin still has open. In the screenshot below, the changes Erin highlighted (made while Anne was busy) appear on the left, and Anne’s highlighted changes appear on the right. A right-click inside the right-hand highlighted region surfaces an Accept Change command, letting that scene’s edits move from the duplicate timeline over to Erin’s original timeline.

With the Compare With Current Timeline command you can spot how two separately edited takes on one timeline diverge, then fold a single scene’s worth of a collaborator’s edits (shown at right) into the original timeline

To read more about putting timelines side by side, refer to Chapter 34, “Creating and Working with Timelines.”

### Editors and Assistant Editors Working Together

Editing metadata, building new bins, and rearranging clips is something collaborators can only do inside unlocked bins. That means your project ought to be laid out so that an editor is able to lock the contents of whichever bins they need at a particular moment, while the assistants press on with extra timelines and media inside that project’s other bins. Beyond copying timelines out of a locked bin into a bin under your control, though, you can also copy clips from one timeline into another. So if you genuinely must alter source clips while the original source clips sit locked, you can apply your edits to copies of them instead.

### Editors and Compositing Artists Working Together

There’s plenty of room for editors and compositing artists to collaborate tightly, because a compositing artist can build compositions for one or more clips on a timeline even as it’s being edited — and even though that timeline, along with the bin holding it, is locked away from other editors. What follows is an example of an editor cutting a commercial spot loaded with greenscreen footage while teaming up with one or more compositing artists.

- To begin, the editor assembles a rough cut for each foreground clip showing the actors' performances; with that rough cut in place, they then drop in the background clips that pair with each greenscreen clip, producing a sequence built from stacks of clips.
- Next, working through one stack at a time, the editor highlights each stack and applies the New Fusion Clip command so the compositing artists have something to build on. Turning every stack into a Fusion clip means the compositing artists can reach all the clips that each composition requires straight from the Fusion page, working side by side.
- The editor then sends word through collaborative chat that finished composites are waiting, and is free to go back to polishing the cut.
- After that signal arrives, one or several compositing artists begin tackling the Fusion clip compositions in parallel with the editor, assembling whatever layered composite each shot calls for. Whenever a compositing artist wraps up a clip and moves on to the next one, a notification badge shows up for the editor at the top-right corner of every composited clip in the Timeline, and matching badges appear in the Bin List of the Media Pool and at the top-right corner of the Timeline viewer. A click on any badge reloads the affected clips so the editor can review what changed.
