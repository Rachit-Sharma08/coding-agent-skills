# To select clips in the media pool and organizing media into bins

Version: DaVinci Resolve 20.3 Reference Manual. Context: Adding and organizing media with the media pool.
[Chapter index](INDEX.md) / [Previous section](media-pool-and-unused-media-removal.md) / [Next section](automatic-smart-bin-creation-and-manual-smart-bin-creation.md)
<a id="source-automated-organization-using-smart-bins"></a> <a id="source-import-and-export-davinci-resolve-project-bins-drb"></a> <a id="source-import-and-export-davinci-resolve-timelines-drt"></a> <a id="source-import-and-export-power-bins"></a> <a id="source-organizing-media-into-bins"></a> <a id="source-sharing-media-among-projects-using-power-bins"></a> <a id="source-smart-bins-are-only-as-good-as-your-metadata"></a> <a id="source-smart-bins-update-their-contents-dynamically"></a> <a id="source-the-power-bins-area-of-the-bin-list"></a> <a id="source-to-select-clips-in-the-media-pool"></a>

### To Select Clips in the Media Pool

You have several ways to pick clips in the Media Pool ahead of relinking, unlinking, moving, duplicating, deleting, or carrying out any other operation on them.

- Click any clip to select it.
- Drag a bounding box around several clips to select them all.
- With either the Command or the Shift key held, draw a bounding box across a separate

discontiguous group of clips so as to either add them to the current selection or take them out of it.

- Click one clip, then Shift-click another so both clips plus everything between them form one continuous selection. A further Shift-click can grow or shrink the selection.
- Command-click clips one by one to build a discontiguous selection. A Command-click on a clip that is already selected drops just that clip while the rest of the selection stays put.
- With a single clip selected, hold the Shift or Command keys and use the Arrow keys to extend the selection onto neighboring clips.

### Organizing Media into Bins

Sorting clips into separate bins in the Media Pool is straightforward. Certain workflows demand it, while in others it is entirely up to you. Methods of working with bins in the Media Pool:

- To add a bin to the Media Pool: Within the Bin list, right-click and pick Add Bin. For a bin nested inside another, right-click whichever bin and pick Add Bin.
- To move selected clips into a new bin: Pick every clip you intend for the new bin, then right-click one of those chosen clips and pick Create Bin With Selected Clips.
- To rename a bin: Pick the bin you want renamed, then click its name once more to make it editable. With the name highlighted, type a fresh name and press Return. As an alternative, right-click a bin, pick Rename Bin, then type a fresh name and press Return.
- To route incoming clips toward one particular bin: Click a bin in the Media Pool so it is selected, then lean on any of the methods covered above to pull media out of the Media Storage panel straight into that bin.
- To move media from one bin to another: Drag one or more chosen clips out of their present spot in the Media Pool and into that bin. Several clips can be picked in the Media Pool through Shift‑clicking or Command-clicking, or by drawing a bounding box across a group. One bin may also be dragged into another.
- To delete a bin: Pick the bin you want removed, then tap the Backspace or Delete key. As an alternative, give a bin a right-click and pick Delete Bin. Wiping a bin that holds nested bins takes that whole set of bins with it.
- To sort bins: Right-click any bin and pick an option from the Sort By submenu. The choices are Name, Date Created, Date Modified, and User Sort.
- To reorganize bins manually: Right-click somewhere in the Bin list and pick Sort By > User Sort. Then drag bins up or down within the Bin list into whatever order you prefer. An orange dividing line marks where the dragged bins will land when dropped and helps reveal whether a bin you are dragging is about to nest inside another or not. Your User Sort order persists even after you switch to a different sort order, and choosing User Sort once more brings your custom order back.

### Import and Export DaVinci Resolve Project Bins (.drb)

Particular bins can be imported and exported from one DaVinci Resolve project to another, letting you move bins quickly between projects and workstations that share the same media. Every bit of Metadata, In/Out points, Timelines, and so on travels along with the clips in the bin, though none of the actual media files come with it. Sending bins out of the Media Pool goes like this: 1 In the Media Pool, pick one or more bins. 2 Give that selection a right-click and pick “Export Bin,” or instead pick File > Export > Export Bin. 3 In the file system dialog, decide where the DaVinci Resolve Bin file (.drb) goes and click Save. Bringing bins back into the Media Pool goes like this: 1 Within the Media Pool, right-click and pick “Import Bin,” or instead pick File > Import > Import Bin. 2 Do one of the following:

- Choose a DaVinci Resolve Bin file (.drb) from the file system dialog.
- Double click the .drb file in your file system.

The bin or bins then turn up in the Media Pool. Whichever bins you import this way get the word “import” tacked onto their name to head off duplicate names. Should an imported bin hold clips that already lived in the Media Pool, those possible duplicates are skipped during import and instead relinked to the media your project references. That keeps the Media Pool clean. Even so, if the bin or bins were moved onto a different computer, you may need to relink offline media.

### Import and Export Power Bins

Power Bins (bins that carry over from one project to the next) can be imported and exported as .drb files exactly like ordinary bins. Power Bins stay hidden by default and are turned on by clicking the Media Pool Option (3-dot) menu and picking Show Power Bins.

### Import and Export DaVinci Resolve Timelines (.drt)

Single timelines can be exported and imported from one DaVinci Resolve project into another already-existing DaVinci Resolve project, letting you move timelines quickly between projects and workstations without generating extra imported project files. Only the timeline together with its related clip information is exported; none of the actual media files travel with it. Sending one timeline out of the Media Pool goes like this: 1 In the Media Pool, pick a timeline. 2 Choose File > Export > Export AAF, XML, DRT (Shift-Command-O). 3 In the file system dialog’s format options popup, pick “DaVinci Resolve Timeline Files (\*.drt).” 4 In that same dialog, decide where the DaVinci Resolve Timeline file (.drt) goes and click Save. Sending several timelines out at once goes like this: 1 In the Media Pool, pick multiple timelines. 2 Give a timeline a right-click and pick Timelines > Export > DaVinci Resolve Timeline Files. 3 From your file browser, pick the folder they should be saved to. Compared with the single-timeline route, a multi-timeline export gives you no chance to rename the .drt files as they go out. Every one keeps the timeline name it carries in the Media Pool. Bringing a timeline back into the Media Pool goes like this: 1 In the Media Pool, pick a bin where the imported timeline should land. 2 Do one of the following:

- Choose File > Import Timeline > Import AAF, XML, DRT (Shift-Command-I); next, out of the file system dialog, pick a DaVinci Resolve Timeline file (.drt) and click Open.
- Double click the .drt file in your file system.

The timeline then turns up in the Media Pool together with every clip tied to it, including any media sync information. Whichever timelines you import this way get the word “import” tacked onto their name to head off duplicate names. The imported timeline is conformed automatically to matching media already present in the Media Pool. Even so, if the timeline was moved onto a different computer, you may need to reimport or relink missing or offline media to bring the imported timeline fully online. NOTE: This method handles only one timeline per import or export. To bring in or send out several timelines, use the Import/Export Bin function covered above.

### Sharing Media Among Projects Using Power Bins

Power Bins offer a means of importing and arranging media that you want on hand for every project in DaVinci Resolve. They occupy a distinct region of the Media Pool, set off by resizable dividers from both the ordinary bins and the Smart Bins regions. Power Bins follow a hierarchy, just as regular bins do, and you may nest as many as you like, one within another. As with regular bins, you create Power Bins by hand, right-clicking inside the Power Bins region and picking Add Bin. The distinction is that any clips you import into Power Bins are shared across every project in a single-user installation, or across all projects owned by a given user in a multiuser installation. That makes them akin to Power Grades in the gallery of the Color page. It also makes Power Bins perfect for holding shared media reused all the time, such as stock video, sound effects, stills, and items like company slates plus the network graphics and animations that open every episode of a series.

### The Power Bins area of the Bin list

You build and work with Power Bins the same way as any other bin, following the steps covered already. To show or hide the Power Bin area of the Bin list: Pick Show Power Bins from the Media Pool option menu to flip the visibility of all power bins on or off.

### Automated Organization Using Smart Bins

A fully automatic route to organizing media in the Media Pool is to lean on Smart Bins, created either automatically or by hand, which round up every clip and timeline in the Media Pool sharing traits drawn from any of the intrinsic or user-editable metadata exposed in the Metadata Editor and Media Pool. If you know the Color page, you will find Smart Bins behave much like Smart Filters, and they are built and edited through nearly the same steps. To read more about Smart Filters, refer to Chapter 126, “Using the Color Page.” Smart Bins bend to almost any need. Built on one or more metadata-based rules, they can be as plain or as elaborate as you wish. They can even apply several groups of several rules for cases where you must round up clips meeting every condition in one set yet only a single condition from a second set. In this way, Smart Bins let you handle a broad range of organizational needs while you cut your program.

### Smart Bins Are Only As Good As Your Metadata

Worth stressing, though, is that while plenty of intrinsic metadata attaches to every clip in DaVinci Resolve on its own (clip properties like frame rate, frame size, codec, file name, and the rest), the more effort you put into entering extra metadata in the Metadata Editor as you prepare a project for editing and grading, the more potent Smart Bins become at helping you sift and sort through the contents of the program you are grading. Metadata entries that pay off immediately with Smart Bins include scene, shot, and take information, plus keywords that flag central descriptors — among them day versus night, interior versus exterior, framing, and the like — alongside Face Detection put to work attaching character names. Such categories of metadata can drive the automatic creation of Smart Bins, but they can equally be mixed together when you hand-build Smart Bins that are even more pointed. Picture being able to round up every clip in one scene, locate all the interview clips for one subject, or surface all the edited timelines matching one name, simply by clicking a Smart Bin that scans the current Media Pool on its own. When you or an assistant invest the time to enter metadata for a project’s source material that captures these traits, you will find the clips you need for any situation far faster.

### Smart Bins Update Their Contents Dynamically

Smart Bins stay current at all times and pull in whatever fresh media lands in the Media Pool. That keeps organization effortless even on projects where new media arrives in the Media Pool daily, as happens while editing during a shoot. Drawing on metadata entered in-camera, by the DIT or media wrangler handling ingest, or by an Assistant Editor working with you, Smart Bins automatically take in every Media Pool clip whose criteria match, no matter whether the clip arrived a month back or a minute back.
