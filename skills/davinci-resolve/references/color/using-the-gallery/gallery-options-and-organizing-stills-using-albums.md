# Gallery options and organizing stills using albums

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the gallery.
[Chapter index](INDEX.md) / [Previous section](playing-stills-and-setting-up-image-wipes-and-timeline-wipes.md) / [Next section](stills-navigator-and-other-project-grades.md)
<a id="source-browse-all-grades-from-the-current-timeline"></a> <a id="source-gallery-options"></a> <a id="source-gallery-window"></a> <a id="source-organizing-stills-using-albums"></a> <a id="source-powergrade-albums"></a> <a id="source-powergrades-are-associated-with-your-user-login"></a> <a id="source-the-gallery-management-window"></a> <a id="source-use-albums-to-organize-your-stills"></a> <a id="source-using-the-gallery-part-2"></a>

### Gallery Options

Up in the upper right corner of the Gallery palette sit several options letting you adjust how your stills are viewed and organized.

- Still Size Slider: Drag this slider left and the still thumbnails shrink; drag it right and they grow.
- Sort Stills: Pick an option from this submenu to reorder every clip in the Gallery. Your choices: Still ID: Orders the stills by the ID number assigned to each (track, clip number, grade version). Label: Orders the stills by each one's text label. Record Timecode: Orders the stills by where each lands in the program. Source Timecode: Orders the stills by the timecode of whichever source clip they came from. Grab Date: Orders the stills by the date each was first grabbed. Create Time: Orders stills according to the moment you stored each one.
- Thumbnail View: Press this icon to put the gallery into Thumbnail view; each still shows up as an image.
- List View: Press this icon to put the gallery into List view; each still shows up as columns of text attributes.
- Search: Brings up a search dialog box for finding stills by their text label.
- Gallery View: Brings up the full Gallery Management window.

The Gallery options, reading left to right: Still Size Slider, then Sort Stills, Thumbnail, List, Search, Expand, and Options

Right-click the gray area of the Gallery, behind the Still icons, and you open a contextual menu offering a range of extra options for steering how many stills get stored, how they're shown, and how they're arranged in the Gallery. The options are as follows:

- Switch Wipe Mode: Flips the Reference mode among showing a "Gallery" still, a "Timeline" clip, or an "Offline" reference movie.
- Trace Timeline: When switched on, selecting a clip in the Timeline also auto-selects the first still that was stored from that clip to the Gallery.
- One Still Per Scene: When switched on, holds the Gallery to storing just one still per clip in the Timeline. Should several stills already have been stored before you flip this option on, those stills linger in the Gallery until you store another still from the same clip, at which point every other still from that clip vanishes.
- Apply Display LUT: When a Display LUT sits selected within the Project Settings, over in the Color Management panel's Lookup Tables panel, it reaches the video output through a connected video interface, and reaches the Viewer too. As a rule you wouldn't want that Display LUT reaching stills you're storing as well, given it's meant to stay temporary. So stills get stored with a LUT-free image. Still, for cases where you might also want to keep a reference to the Display LUT currently in use, switching on "Apply Display LUT" stores the Display LUT alongside the still and applies that LUT whenever the still serves for split-screen reference. Bear in mind that the internally stored Display LUT only kicks in while playing that still in the Viewer; the DPX image that's stored stays untouched.
- Apply Grades Using: This submenu holds three options governing how the keyframes automatically stored within each saved grade get applied.

No Keyframes: No keyframes get copied. Whatever state the grade held at the frame used to store the still is what lands on the target clip or clips. Keyframes Aligning Source Timecode: Keyframes get copied with the source timecode of the saved grade lined up against the source timecode of the target clip. This is the ideal pick while copying a grade back onto the clip it originally came from, or onto a duplicate of that clip elsewhere in the Timeline, where you want the keyframes lining up with the same frames as before. Where no source timecode overlap exists, keyframes get pasted lined up with the edit's start frame, matching the third option (below). Keyframes Aligning Start Frames: Keyframes get copied with the start frame of the clip the still was stored from lined up against the start frame of the target clip. This is the ideal pick while copying a grade carrying keyframes from one clip onto an entirely different clip with different timecode.

- Use labels on still export: Lets you fold labels you've attached to stills into the file name of exported stills.
- Show All Stills: This command surfaces every available still in the current album should any have been hidden, by searching or by the Show Current Timeline Only command, for instance.
- Show Current Timeline Only: Pick this option to hold the Gallery to showing only the stills stored from the currently selected Timeline. Every other still from other Timelines stays hidden until you switch over to that Timeline.

NOTE: A range of other commands live in this contextual menu and get covered elsewhere in this chapter.

### Organizing Stills Using Albums

Every still you store always drops into the Gallery's currently open album, which for new projects defaults to "Stills 1." That said, you can spin up extra albums for sorting your stills by whatever categories suit you. Showing, creating, and removing albums all happen through the Gallery in either the Color page or the Gallery windows.

### Use albums to organize your stills

To show or hide the Albums list: Over at the Gallery's top left, click the Album button. With the Albums list hidden, clicking the Album button surfaces the Albums list, left of the Gallery, holding every album currently available in the open project, plus the PowerGrade album down at the bottom. With the Albums list already showing, it goes hidden instead, freeing up more room for still thumbnails in the Gallery. Once the Albums list is up, several quick and easy ways exist to work with albums. Ways to work with albums:

- To add a new album: Right-click the Albums list and pick Add Still Album from the contextual menu. A new album springs up, numbered in sequence.
- To add a new PowerGrade album: Right-click the Albums list and pick Add PowerGrade Album from the contextual menu. A new album springs up, numbered in sequence.
- To rename an album: Double-click any album in the list, and once it's selected, type a new name and press Return.
- To navigate albums: Click any album to make it the current one. On the DaVinci Resolve Advanced control panel, the PREV PAGE/NEXT PAGE buttons let you move up and down the Album list.
- To move clips from one album to another: Take a still from the Gallery and drag-and-drop it onto an album.
- To remove an album: Right-click any album, pick Remove Current Album, and click Delete at the prompt. Every clip inside that album gets deleted right along with the album, so tread carefully here.

### PowerGrade Albums

PowerGrade albums are built to hold grades you mean to reuse often, or stills you have to reference across multiple projects—say while grading a series that carries common looks from one episode to the next.

### PowerGrades are associated with your user login

Unlike stills stored in the list's other albums, which are usually on hand only to the project where they were stored, stills stored to a PowerGrade album are shared across every project kept within a given project library. Each project library carries its own unique PowerGrade album. Building a new project library builds a new PowerGrade album, which begins as a blank slate. Even so, the Gallery window is always there to copy PowerGrade stills out of other projects and project libraries into the current one, and you can spin up however many PowerGrade albums you need to organize your grades. For fuller detail covering project management plus project libraries, see Chapter 3, "Managing Projects and Project Libraries." In function, PowerGrade albums are no different from any other album, and you can store, organize, and use stills in PowerGrade albums just as you would with other albums. Because PowerGrade albums are special in that DaVinci Resolve maintains them, the last PowerGrade album can't be deleted.

### Browse all Grades from the Current Timeline

The Gallery carries a Timelines album, found at the bottom of the Album list, that lets you browse every grade in the current timeline, or in other timelines of the current project (by way of a drop-down menu that appears atop the Gallery browser area), making it simple to lift grades from points earlier or later along your timeline, or out of other timelines drawing on the same media. This proves especially handy on reality shows or documentaries where the same clips can crop up several times across different parts of a program. Being able to just surface every existing grade in the Gallery spares you from storing a still for every grade you suspect you might reuse down the road.

The Gallery's Timelines grade browser surfaces, on its own, every grade across the current timeline

### The Gallery Management Window

Although a fair bit of stills management is possible through the Gallery as it appears on the Color page, the Gallery window brings extra capability: copying stills across separate projects and project libraries, organizing your stills along with your memories, plus reaching the DaVinci Resolve looks bundled with the application. To open the Gallery window: At the upper right-hand corner of the Gallery, click the Gallery View button, or else select Workspace > Gallery.

### Gallery window

The Gallery opens into a floating window, split into four areas:

- Stills navigator: Lets you move through the contents of whatever other projects and project libraries are on hand. This hierarchical list surfaces standalone projects as well as project library > user > project relationships. Clicking the disclosure triangle beside any entry expands its contents, and clicking any project in the list opens its albums and stills inside the Group Stills browser.
- Group Stills browser: Shows whatever item is currently picked in the Stills navigator. To copy one or several chosen stills into the current project, select an album in the Project Stills browser and drag the stills over into the Project Stills browsing area.
- Project Stills browser: Holds the very same Album list and Project Stills browser shown in the Color page Gallery.
- Project Memories: Offers a roomier look at the project memories shown in the Color page Gallery.

To resize different areas of the Gallery window:

- Bring the pointer to the dividing border between any of the Gallery's areas. Once the pointer turns into the resize cursor, drag that border to set the neighboring interface areas to whatever dimensions suit you. Drag right out to the screen edge and that interface area disappears entirely.
