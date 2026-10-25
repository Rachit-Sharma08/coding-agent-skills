# Create smart bin dialog and smart bins work better with metadata

Version: DaVinci Resolve 20.3 Reference Manual. Context: Adding and organizing media with the media pool.
[Chapter index](INDEX.md) / [Previous section](automatic-smart-bin-creation-and-manual-smart-bin-creation.md) / [Next section](media-pool-thumbnail-sorting-and-list-columns.md)
<a id="source-choosing-how-to-display-bins"></a> <a id="source-duplicating-clips-in-the-media-pool"></a> <a id="source-duplicating-timelines"></a> <a id="source-multiple-media-pool-bins-opened-as-new-windows"></a> <a id="source-organizing-smart-bins"></a> <a id="source-showing-bins-in-separate-windows"></a> <a id="source-smart-bins-organized-into-folders"></a> <a id="source-smart-bins-work-better-with-metadata"></a> <a id="source-the-create-smart-bin-dialog"></a> <a id="source-using-the-media-pool-in-thumbnail-view"></a>

### The Create Smart Bin dialog

- Show in all projects checkbox: Produces a persistent Smart Bin that shows up across every project in your project library. Smart Bins made in this fashion land in the User Smart Bins folder within each project’s Smart Bin region of the Media Pool.
- Match options: When filtering on several criteria, picking All requires that each individual criteria you list is satisfied before a clip passes the filter. Picking Any means a clip passes once a single one of the several criteria is satisfied.
- Filter criteria enable checkbox: Turns any criteria on or off so you don’t have to remove it entirely.
- Metadata category drop-down: Determines which category of metadata you’ll pull a criteria from. Every metadata category exposed in the Metadata Editor is reachable from this drop-down menu. On top of that, Color Timeline Properties (which holds many properties exclusive to the Color page timeline) and Media Pool Properties (which holds every column in the Media Pool) open up extra metadata available for filtering.
- Metadata type drop-down: Picks the precise type of metadata to apply, from those offered in the chosen metadata category.
- Metadata criteria drop-down: Sets the criteria used for filtering, based on the metadata you’ve picked. Possible choices cover such things as “true/false,” ranges of integers, ranges of dates, searches over strings, colors of flags and markers, and the like.
- Add filter criteria button: Appends extra criteria so you can assemble multi-criteria filters. Several criteria together might, for instance, surface all exterior clips that additionally carry the keyword “Sunset” and that aren’t closeups, letting you gather every exterior long and medium shot lit by sunset. Furthermore, Option-clicking this button inserts a nested match option, enabling still more advanced filters — for example, one where the filter has to satisfy all of one group of criteria along with any of a second group.

An intricate Smart Bin carrying several criteria plus a secondary match option setting While you tweak the filter criteria, the thumbnail timeline refreshes on its own to show how the Smart Bin you’re assembling behaves. 3 After you finish editing the filter criteria, click Create Smart Bin. The newly made Smart Bin shows up in the Smart Bin region of the Bin list, on the left side of the Media Pool’s browser area. After a Smart Bin exists, it sits in the lower portion of the Media Pool’s Bin list, together with every other Smart Bin belonging to that project. That arrangement keeps them tidy, set apart from the manually made bin shown above.

Every Smart Bin is grouped at the foot of the Bin list belonging to the Media Pool After you’ve built a Smart Bin, you’re free to revise it any time the need arises.

Ways to change Smart Bins that already exist:

- To rename a Smart Bin: Right-click whichever Smart Bin you’d like renamed, pick Rename from the contextual menu, type a new name, and press Return.
- To edit a Smart Bin: Double-click the Smart Bin, then alter the filter criteria, and click OK.
- To duplicate a Smart Bin: Right-click any Smart Bin and pick Duplicate from the contextual menu. This is handy for spinning off several variants of a Smart Bin you built with intricate rules, when you need variants by tweaking those rules rather than starting over from scratch every time.
- To delete a Smart Bin: Right-click whichever Smart Bin you’d like removed, then off the contextual menu pick Delete Smart Bin, and in the warning dialog that appears click Delete. Removing a Smart Bin leaves any gathered media tied to that bin untouched.

### Smart Bins Work Better With Metadata

Bear in mind that the more metadata you attach to each clip, the more ways you have to build custom Smart Bins (for editing) and Smart Filters (for grading) to home in on exactly the clips a given situation calls for. Not only does this make locating what you need simpler, it also speeds up your work. As a baseline, it’s worth using the Metadata Editor to tag each clip with details such as a Description, Shot and Scene designations, take information, and perhaps a few handy keywords like character names, shot framing, interior or exterior keywords, and so forth. As an example, once you’ve filled in enough metadata, you can construct multi-criteria Smart Bins or Smart Filters that turn up something along the lines of “each close-up of Sally inside the diner” or “each long shot of Antonio out in the parking lot.” On a documentary, pulling out “each interview shot of Louis from camera 1” or “each B-roll clip featuring Robyn” becomes effortless. Everything here speeds up locating media for editing, or rapidly pulls together comparable clips you need matched up for grading. For further detail on the Metadata Editor, refer to Chapter 19, “Using Clip Metadata.”

### Organizing Smart Bins

Smart Bins you’ve made by hand can be grouped into Folders and Sub-Folders for tidier sidebar handling, exactly the way ordinary bins are.

### Smart Bins organized into folders

To add a Smart Bin folder: Right-click within the Smart Bins region and pick Add Folder from the contextual menu to make folders that you can drag Smart Bins into. Every folder carries a disclosure triangle, letting you reveal or conceal what it holds.

A further upside of Folders is that selecting a Folder shows the complete contents of every Smart Bin within it in the Media Pool browsing area. Picking any single Smart Bin then limits the Media Pool to only the media referenced by that Smart Bin. Right-clicking a Folder and choosing commands from the contextual menu lets you rename it, remove it, open it as a new window, or sort it together with all the other Smart Bins.

### Duplicating Clips in the Media Pool

You can duplicate clips so as to spawn an instance of that media that behaves as a wholly new source clip, fully independent of the original instance of that clip imported into DaVinci Resolve. The duplicate can hold its own metadata and markers that stay fully separate from the original clip imported into your project. To make duplicates of one or several clips: 1 Pick the clip or clips you wish to duplicate. 2 Carry out one of these:

- Choose Edit > Duplicate Clip
- Keep the Option key pressed as you drag one or several selected clips over to a different bin
- In the Media Pool, right-click a clip, then off the Contextual Menu pick Duplicate Clip

Adding Clips From the Timeline to the Media Pool Equally, you may drag one or several clips out of the Timeline and back into the Media Pool to spawn a duplicate. Just as with duplicating clips inside the Media Pool, each duplicate comes into being as a new source clip that stays wholly apart from the original instance of that clip imported into DaVinci Resolve and can hold its own metadata and markers that remain fully separate from the original clip imported into your project. For instance, the original clip in the Timeline stays conformed to the original clip first imported into the Media Pool; removing the original clip from the Media Pool renders that clip “non-conformed” in the Timeline, whereas the duplicate you just made stays linked and on hand. Should you land in this situation, you can at any point turn Conform Lock Enabled off on that clip within the Timeline and then reconform that Timeline Clip onto the duplicate you’ve made, though that adds a step because DaVinci Resolve regards the duplicate clip as an entirely fresh piece of media that merely happens to share identical clip details. It may feel odd, yet a range of finishing workflows lean on this ability, so it’s worth knowing.

### Duplicating Timelines

Timelines may be duplicated for any number of reasons: to keep a backup of a timeline at a given date, to spin off a variation of an edit, or to produce separately graded versions. To duplicate a Timeline:

- Select a Timeline in the Media Pool, and choose Edit > Duplicate Timeline.
- Hit Command-4 so the Timeline takes focus, then choose Edit > Duplicate Timeline.

### Choosing How to Display Bins

After you’ve set up a bin structure for your project, you can tailor the way your bins display, according to how you prefer to work.

### Showing Bins in Separate Windows

When you right-click a bin in the Bin list, you can pick “Open As New Window” to launch that bin into a window of its own. That window amounts to a self-contained Media Pool, carrying a Bin list of its own, its own Power Bins and Smart Bins lists, plus display controls.

### Multiple Media Pool bins opened as new windows

When more than one Media Pool window is open, you can use the Workspace > Media Pool Windows submenu to surface a floating Media Pool window that sits open yet hidden. This pays off most when two displays are attached to your workstation, since you can drag these separate bins onto the second display while DaVinci Resolve runs in single screen mode. Hiding the Bin list not only frees up more space for clips, it also keeps you from accidentally jumping bins when you really mean to view just one bin’s contents in that window.

### Using the Media Pool in Thumbnail View

When you work in Thumbnail view via the controls at the top right of the Media Pool, you’re able to resize the thumbnails for easier viewing, and you can pass the mouse pointer over each clip to hover scrub through what it holds. Clicking any clip to select it shows it in the Media page Viewer. Whatever clip is selected at the moment is also sent to video for monitoring. While in Thumbnail view, you control how clips get sorted through the Sort Order drop-down, which sits at the Media Pool’s upper right, positioned between the Icon Size slider and the Icon/List view buttons. Fourteen choices are on offer here. The naming-oriented ones are File Name, Reel Name, and Clip Name; timing-oriented are Start TC plus Duration; technical ones cover Type, FPS, and Audio Ch; then come Flags, followed by Date Modified together with Date Created, and finally the production fields Shot, Scene, and Take.
