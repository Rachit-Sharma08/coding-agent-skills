# Removing media from the media pool and removing unused media from a project

Version: DaVinci Resolve 20.3 Reference Manual. Context: Adding and organizing media with the media pool.
[Chapter index](INDEX.md) / [Previous section](adding-media-to-the-cut-edit-fusion-and-fairlight-pages.md) / [Next section](media-pool-selection-and-bin-organization.md)
<a id="source-a-clip-matte-seen-in-icon-view"></a> <a id="source-a-clip-matte-seen-in-list-view"></a> <a id="source-a-timeline-matte-seen-in-thumbnail-view"></a> <a id="source-adding-and-removing-external-mattes"></a> <a id="source-adding-mattes"></a> <a id="source-adding-offline-reference-movies"></a> <a id="source-extracting-audio-in-media-storage"></a> <a id="source-manually-organizing-the-media-pool"></a> <a id="source-matching-rgb-and-matte-images"></a> <a id="source-removing-media-from-the-media-pool"></a> <a id="source-removing-unused-media-from-a-project"></a> <a id="source-using-embedded-mattes-in-openexr-files"></a> <a id="source-what-are-mattes-for"></a>

### Removing Media From the Media Pool

When the Media Pool holds clips you want gone, clearing them out is simple, whether one at a time or as a whole group. To remove clips from the Media Pool, do one of the following:

- Pick one or more clips inside the Media Pool, then hit the Delete or Backspace key.
- Pick one or more clips inside the Media Pool, right-click one of the chosen clips, and then pick Remove Selected Clips.
- Anywhere within the Media Pool, right-click and pick Remove All Clips in Bin.

NOTE: When “Automatically match master timeline with media pool” has been switched on in the General Options panel of the Project Settings, the Media Pool won’t let you clear every clip while other timelines still draw on those same media files. Clearing clips off the Master Timeline (should it be exposed):

- Go to the Edit page, then pick one or more clips inside the Media Pool, right-click one of the chosen clips, and pick “Remove Selected Clips from Master Timeline.”

To read more about working with the Master Timeline, refer to Chapter 33, “Using the Edit Page.”

### Removing Unused Media from a Project

DaVinci Resolve can clear out unused media clips from the Media Pool on its own, getting things ready for archiving or for handing a tidy project off to another workstation. The pass loads every timeline, compound clip, and Fusion composition, then checks them all for media usage. Whatever clips that check fails to encounter are dropped from the Media Pool. The option erases nothing from your disk; it simply takes the clips out of the Media Pool and the Project. The action cannot be undone. Based on how large the Project is, the pass may run for several minutes. To remove unused media from a Project: 1 Click the Media Pool Option (3-dot) menu. 2 Pick Remove Unused Clips from the drop-down menu. 3 Click the Load All Timelines button to begin, or Cancel to call it off.

Pick Remove Unused Clips from the Media Pool Option menu, then click the Load All Timelines button to kick off the analysis

### Adding and Removing External Mattes

When you receive matte files meant to go with one or more media files in a program you are grading, you can bind them straight onto particular clips in the Media Pool so they serve as key sources for a Clip Grade inside the Node Editor of the Color page. You may even rely on matte files that bundle several mattes inside one piece of media. That is achieved either by writing distinct mattes to a clip’s red, green, and blue channels, or by packing several matte passes inside one OpenEXR file.

### Matching RGB and Matte images

With the Media Pool set to Icon view, any clips carrying clip mattes display a badge.

### A clip matte, seen in Icon view

When the Media Pool sits in List view, clip mattes show up nested below the clip they belong to.

### A clip matte, seen in List view

As another option, you can place a timeline matte into the Media Pool that is bound to no particular clip and can serve as a key source on the Color page inside any clip’s Clip grade, or inside a Timeline Grade. In the Media Pool, timeline mattes show up as clips that stand on their own.

### A timeline matte, seen in Thumbnail view

### What Are Mattes For?

There are two purposes matte files serve. By tradition, a matte is a grayscale media file marking out regions of differing opacity, where white stands for solid areas and black stands for transparency. As an example, clips exported from a compositing application sometimes arrive alongside one or more matte files matching keys or rotoscoped mattes from that composite. Bringing these matte files in with the “Add as Matte” command binds them to the clips they accompany in the Media Pool, so each is available only to the clips it has been synced with. That said, mattes also work as creative devices for laying grain and texture down for effect. Just what a matte accomplishes hinges on the way you wire it in the Node Editor of the Color page. Because these are media files you might wish to apply as mattes to virtually any clip, they can likewise enter the Media Pool as a so-called timeline matte, which you can drop onto whatever clip you like. TIP: Where it helps, LUTs may also be laid onto clip mattes as well as timeline mattes within the Media Pool — simply right-click a matte and pick a LUT out of the 1D LUT or 3D LUT submenus. That proves useful for fixing up mattes that came in formatted incorrectly.

### Adding Mattes

Mattes have to be added by very particular steps before you can use them. To assign a matte to a clip in the Media Pool: 1 Pick the clip in the Media Pool you intend to attach an external matte to. 2 Within the Media Storage panel, locate the matching external matte file, give it a right-click, and pick Add to Media Pool as a Matte. That binds the matte to the clip as a clip matte. A badge marks the clip as having a matte while the Media Pool is in Icon view, and the matte itself becomes visible — appearing as a nested item below the clip it is bound to — after the Media Pool is switched over to List view. Stripping mattes back off clips within the Media Pool: 1 Set the Media Pool over into List view. 2 Give a right-click to whichever external matte file should go and pick Remove Selected Clips. Taking out an external matte clip also strips that matte’s key from any clip grades relying on it, so that any clip using it as a key input shifts from a secondary operation back to a primary operation, where the color change touches the whole image. To add a timeline matte to the Media Pool: 1 Confirm that no clip is selected in the Media Pool. 2 Within the Media Storage panel, locate an external matte file, give it a right-click, and pick Add to Media Pool as a Matte. The external matte then shows up in the Media Pool as a timeline matte. Mattes can also be assigned to clips right on the Color page, which is sometimes quicker.

To assign a matte to a clip in the Color page:

- Drag any clip from the Media Pool to the Node Editor.

In the Node Editor the dragged clip then acts as an External matte feeding the grade of whichever clip is current, and that same clip is assigned for you automatically to the current clip back in the Media Pool. To read more about putting external matte clips to work as keys while grading, refer to Chapter 146, “Combining Keys and Using Mattes.”

### Using Embedded Mattes in OpenEXR Files

When you bring in OpenEXR files that carry embedded matte passes, no extra step is required, since those mattes already live inside the clip you just imported into the Media Pool. To read more about working with mattes inside OpenEXR files, refer to Chapter 146, “Combining Keys and Using Mattes.”

### Adding Offline Reference Movies

While shifting a project out of another application and into DaVinci Resolve, it helps to render the whole program as one media file to serve as an Offline Reference Movie. You can then bring that file in by a special route for dual Viewer comparison on the Edit page, or for a split-screen fade wipe comparison on the Color page. As of DaVinci Resolve 16 importing reference movies this way is no longer required for an offline comparison, yet it can still prove handy when you are juggling many timelines and versions that demand pinpoint precision. Adding a clip as an offline reference clip works like this: right-click the clip within the Media Storage panel and pick “Add As Offline Clip.” The clip then shows a small checkerboard badge on its Media Pool icon, or it appears as the icon over to the left of the Media Pool.

Checkerboard icon indicating an Offline comparison video To read more about putting an offline video to use against an imported Timeline on the Edit page, refer to Chapter 55, “Preparing Timelines for Import and Comparison.” To read more about split-screen reference of Offline video on the Color page, refer to Chapter 126, “Using the Color Page.”

### Extracting Audio in Media Storage

When a video clip in the Media Storage panel carries audio you want but the picture is of no interest, the Extract Audio command builds a standalone audio clip you can then bring into the Media Pool on its own. Pulling the audio out of a media file goes like this: 1 Within the Media Storage panel, right-click a clip and pick Extract Audio. 2 Inside the Extract Audio dialog, hit the Browse button to settle on a different disk spot for the extracted clip. 3 Click Extract. The audio channels are pulled out and saved as a .WAV file at the chosen destination. 4 Once that standalone .WAV file exists, you will have to import it into the Media Pool before you can use it in your project.

### Manually Organizing the Media Pool

No matter whether you are doing onset work, building digital dailies, sorting media to edit, or ingesting media to conform to an imported project, keeping things in order is absolutely critical. The Media Pool hands you a great many tools for that. This section looks at how bins let you organize collections of clips by hand.
