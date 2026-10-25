# How collaboration works and automatic bin and timeline locking

Version: DaVinci Resolve 20.3 Reference Manual. Context: Collaborative workflow.
[Chapter index](INDEX.md) / [Previous section](collaborative-workflows-and-render-cache.md) / [Next section](editor-and-assistant-editor-collaboration.md)
<a id="source-automatic-bin-and-timeline-locking"></a> <a id="source-automatic-clip-locking"></a> <a id="source-compositing-artists-and-colorists-can-work-together"></a> <a id="source-examples-of-collaborators-working-together"></a> <a id="source-how-collaboration-works"></a> <a id="source-keeping-bins-locked"></a> <a id="source-managing-bin-locks-manually"></a> <a id="source-manually-locking-and-unlocking-timelines"></a> <a id="source-receiving-changes-made-by-collaborators"></a> <a id="source-receiving-changes-on-the-edit-page"></a> <a id="source-receiving-changes-on-the-fusion-and-color-pages"></a>

### How Collaboration Works

In its most basic form, collaborative workflow leans on a “first come, first served” scheme to decide who is allowed to alter what. In practice, whoever is first to pick a bin in the Media Pool, open a timeline, or pick a clip on the Fusion page or Color page earns a “lock” over that item. After an item gets locked (shown by a tinted collaborator badge), the rest of the collaborators may view it but can’t alter it. Doing this keeps versioning conflicts from cropping up. A bin or clip lock lifts the moment a collaborator picks a different bin or timeline on the Media or Edit pages, or a different clip on the Fusion page or Color page. From there, whatever edits were applied to the formerly locked item get “checked in” and offered to every collaborator the next time they refresh their project (done by clicking a circular refresh icon that, within the Media Pool, sits to a bin’s right — or, on the Edit page Viewer, sits in its corner). Because every change a collaborator makes is committed to the project automatically as it happens, nothing you do will ever be lost while you collaborate with your team. Even so, each collaborator individually picks the moment to refresh whichever bin, timeline, or clip they’re currently on so they can take in everyone else’s changes — this keeps a never-ending swirl of shifting grades and compositions from pulling your attention away while you work. The sections coming up go deeper into Bin and Timeline locking and Clip locking.

### Automatic Bin and Timeline Locking

Each time a collaborator opens a given bin, that bin together with everything in it becomes locked, which blocks any other collaborators in the project from changing whatever lives inside it. That keeps versioning conflicts at bay while the work is underway. A locked bin still lets you look at its contents — handy when you simply need to learn where a certain clip ended up — but it won’t let you change anything. Although collaborators may open locked bins and view what’s inside for reference, they’re unable to make any editorial or organizational edits. Once a bin and its contents are locked, the only changes still permitted are building or revising clip compositions on the Fusion page and revising clip grades on the Color page. You can always spot that a collaborator holds a lock on a bin and its contents, because a badge surfaces beside the bin (on its right) within the Bin list, plus in the corner of whatever timeline thumbnails happen to be shown across the Media Pool browser area. Resting the pointer over that badge in the Bin list pops up a tooltip carrying that collaborator’s name.

When a fellow collaborator holds a lock on the Projects bin, an icon signals it. As soon as a collaborator (anybody but you) alters a bin’s contents or a timeline, a circular “refresh” badge turns up beside every affected bin in the Bin list of the Media Pool, next to that person’s collaborator icon. Click those badges any time you’d like to bring your copy of the shared project up to date with all of the editorial and organizational changes others made in that bin. Releasing a bin or timeline is as easy as picking a different bin or timeline. That’s all it takes.

When another collaborator has altered something, an icon flags it; a click refreshes your project so those alterations appear

### Managing Bin Locks Manually

The locked state of bins is also yours to steer by hand, for those occasions when you’d rather hold bins locked for later use, or stop them from locking at all when all you mean to do is glance through their contents.

### Keeping Bins Locked

When you’ve got one or more bins that you’ll be flipping back and forth between, and you want to stop other collaborators from changing them — or simply make sure no one else accidentally locks you out of them — you can right-click your selected bins and pick Lock Bins to lock them.

Bins locked this way stay locked even after you click away from them, right up until you right-click them once more and pick Unlock Bins. Because your collaboration icon is visible to other users too, they’ll be able to tell who currently holds the lock on the bin.

A bin you’ve locked by hand keeps its lock even after it’s deselected Keeping Bins Unlocked On top of that, you’re able to keep bins from locking when they’re selected. You might, for instance, only want to look over what’s in a bin without blocking anyone else from editing it. To do that, just Option-click any bin and it opens in read-only mode, flagged by an eyeball badge sitting at the left side of the bin within the Bin list. While you’re in this mode, any other collaborator remains free to lock that bin even as you look through its contents. Picking any other bin wipes out this read-only state.

Opening a bin in read only mode leaves your collaborators free to lock it as you look through what’s inside TIP: As long as a bin is open but you’ve manually left it unlocked, you can still load clips into the Source Viewer and tag them with markers — provided no other user picks that same bin and locks you out.

### Manually Locking and Unlocking Timelines

The locking of timelines is something you can also manage by hand. Opening a timeline locks every other collaborator out of changing that timeline, yet it still permits other users to alter the bin in which that timeline lives. That gives you more freedom in arranging your Media Pool and keeps you from locking media or other timelines sitting in the same folder. Individual Media Pool bins can still be locked by hand if you want to protect their contents on their own. To free a timeline so other collaborators can take it on:

- Right-click that timeline within the Media Pool and pick Timelines > Unlock Timeline from the contextual menu.

To lock a timeline and stop other collaborators from touching it: 1 Right-click that timeline within the Media Pool and pick Timelines > Lock Timeline from the contextual menu. 2 While you hold the lock, no other collaborator can alter the timeline, though they’ll still be able to alter any of the bin’s other clips and timelines.

### Automatic Clip Locking

On the Fusion and Color pages, clip locking behaves in much the same fashion. With many compositing artists at work on the Fusion page and many colorists at work on the Color page, whichever compositing artist or colorist is first to pick a particular clip automatically holds the lock over it. Every other compositing artist or colorist then sees a badge on that clip in the Thumbnail timeline indicating that it’s locked, along with who holds the lock. In the screenshot below, the SO badge in the corner of clip 7 on the Color page Thumbnail timeline signals that the clip is locked.

Within the Thumbnail timeline, badges show you which clips a collaborator has locked for grading Automatically Checking In Work When You Change Clips Once you’ve wrapped up the clip in front of you, you simply pick a different clip, and the edits you applied to the previous clip are saved automatically and pushed out to every other colorist working that timeline on the Color page. There’s no refresh to perform. That’s the key way clip locking on the Color page departs from bin locking.

### Compositing Artists and Colorists Can Work Together

Separate clip locks are kept by the Fusion page and the Color page apiece. So, across any group of compositing artists, just one of them can be on a given clip at any moment, and on the Color page only one colorist can be on a clip at any moment. Yet since Fusion and Color page clip locking is tracked independently, a single compositing artist and a single colorist are able to share one clip in the timeline at the same time — even with an editor also working that timeline.

### Receiving Changes Made by Collaborators

While you collaborate, it’ll often be the case that several compositing artists are running multiple compositions at once, the colorist and their assistants are busy with the grade, and the editor and their assistants are polishing the edit, with everyone pulling together inside the same project.

### Receiving Changes On the Edit Page

While compositors composite and colorists grade clips inside the same timeline of the same project, every clip touched on the Fusion or Color page fires off a Refresh badge in three spots on the Edit page, letting the collaborating editor(s) choose for themselves when to refresh their timeline and view what’s changed. In the top-right corner of the Timeline Viewer. A click on this badge refreshes the grades and composites for every clip in the open Timeline.

For any timeline whose edits, grades, and composites have changed, a clickable “update” badge shows in the Timeline Viewer’s corner To the right of the bin that holds the modified timeline within the Media Pool’s bin list. A click on this badge refreshes every clip in the Timeline inside that bin.

For Media Pool bins holding timelines whose edits, grades, and composites have changed, a clickable “update” badge shows over them In the top-right corner of every modified clip within the Timeline. Over any clip in the Timeline whose edits, grades, and composites have changed, a clickable “update” badge shows

### Receiving Changes On the Fusion and Color Pages

For anyone working the Fusion or Color pages, additional badges flag when editors have altered the Timeline, or when fellow compositing artists or colorists have altered other clips in that timeline. A timeline you’re shut out of because another collaborator holds its lock is flagged by a badge in the top-right corner of the Viewer, while alterations editors made to the Timeline on the Edit page are flagged by a refresh badge in that very spot. A click on this badge refreshes every clip in the Timeline.

Within the Viewer, a badge signals that someone else holds a lock on this timeline Open up the Media Pool and a badge turns up to the right of any bin in the Bin List that’s been rearranged or that holds a modified timeline. A click on this badge refreshes every clip in the Timeline inside that bin.

For Media Pool bins whose timelines have changed, a badge shows up on their right A badge surfaces in the top-right corner of each clip in the Thumbnail timeline that a fellow compositing artist or colorist has altered. Clicking a single clip’s badge refreshes that clip on its own.

Over any clip in the Timeline whose grade has changed, a badge shows. Clicking it refreshes that one clip alone.

### Examples of Collaborators Working Together

Whoever opens a timeline first is the sole person allowed to make editorial changes to it on the Edit or Fairlight pages. Anyone else who opens that project is “locked out” of editing on the Edit or Fairlight pages, yet they can still view the Timeline and apply grading changes on the Fusion or Color pages. So whenever you’d like several editors going at one project, a good approach is to split your program into separate “reels,” with each reel sitting as its own timeline in its own bin.
