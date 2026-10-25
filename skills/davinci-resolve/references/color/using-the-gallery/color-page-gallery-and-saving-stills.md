# Color page gallery and saving stills

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the gallery.
[Chapter index](INDEX.md) / [Next section](playing-stills-and-setting-up-image-wipes-and-timeline-wipes.md)
<a id="source-changing-the-powergrade-still-directory"></a> <a id="source-color-page-gallery"></a> <a id="source-deleting-stills"></a> <a id="source-hover-scrub-in-the-gallery"></a> <a id="source-live-previews-of-gallery-stills"></a> <a id="source-right-click-on-a-still-to-choose-still-properties"></a> <a id="source-saving-stills"></a> <a id="source-selecting-stills"></a> <a id="source-using-the-gallery"></a> <a id="source-using-the-gallery-part-1"></a> <a id="source-where-are-stills-saved"></a>

### Using the Gallery

The Gallery gives you a way to store, browse, and draw on saved still frames pulled from a program's various clips. Every project keeps its own separate set of stills, and each still you store is made up of a DPX image of the saved frame plus the grade metadata. Saved stills come in handy as reference while matching one clip against another, or you can lean on them to copy grades onto other clips or other timelines. Two avenues exist for working with what's in the Gallery. The Color page carries a small Gallery, sitting left of the Viewer, that puts saved stills and grades within easy reach as you work. The Gallery window, which opens from a button at the Gallery's top right, hands you a dedicated interface for organizing your grades, ferrying grades and memories between projects, and reaching a dedicated collection of DaVinci Resolve looks.

The Color page's Gallery and the larger Gallery window environment share a good many of the same commands for organizing stills. That said, the commands for saving stills and for tailoring split-screen views stay confined to the Color page.

### Color page Gallery

### Saving Stills

Among the most frequent operations is storing a clip as a still (carrying that clip's embedded grade) for later reference and reuse. To store a single still on the Color page, take one of these actions:

- Choose Color > Stills > Grab Still (Option-Command-G).
- Right-click the Viewer and choose Grab Still.
- Press GRAB STILL on the Transport panel of any DaVinci Resolve control panel.

Stills can also be stored automatically for every clip across the whole Timeline. That comes in handy when you're set to export a batch of grades to pass off to another colorist, or when you have to apply a run of grades by hand from one project into another while ColorTrace™ won't cooperate. To store a still covering each clip across the current timeline, right-click the Viewer and pick from these:

- Grab All Stills > From First Frame: The first frame of every clip gets stored to the Gallery.
- Grab All Stills > From Middle Frame: The middle frame of every clip gets stored to the Gallery.
- Grab Missing Stills > From First Frame: Only the first frame of clips that have no stills in the Gallery gets

stored to the Gallery.

- Grab Missing Stills > From Middle Frame: Only the middle frame of clips that have no stills in the

Gallery gets stored to the Gallery.

You can halt the Grab All Stills operation whenever you like by clicking the Cancel button in the "grabbing stills" dialog box. That's useful when you spot a clip needing a change after the tool has started and you'd rather not sit through the whole timeline being grabbed before you fix it. With your correction made, simply fire off Grab All Stills again. By default, any stills you store are named "TrackNumber.ShotNumber. VersionNumber" with dots between each number. If you prefer, the General Options panel of the Project Settings offers an option to "Automatically label Gallery stills" along assorted lines. That's spelled out more fully later in this chapter.

### Selecting Stills

To select a range of stills, take one of these actions:

- Click one still, then Shift-click another to grab a contiguous range of stills.
- Command-click whichever stills you like to build a noncontiguous selection.
- Right-click any still and pick one of these commands; Select All: Grabs every clip in the Gallery. Select Current to Last: Grabs every still running from the one you clicked through to the last still in the Gallery. Select First to Current: Grabs every still running from the one you clicked through to the first still in the Gallery.

### Deleting Stills

When you need to clear one or more stills, that's only doable through the Gallery's contextual menu. To delete one or more stills, take one of these actions: 1 In the Gallery, select one still or several. 2 Right-click any one of those selected stills and pick Delete Selected. Each still further carries an assortment of metadata that DaVinci Resolve relies on to manage what's in the Gallery in various ways. That metadata can serve for searching and sorting too, and you view it by opening the Still Properties window. To show a still's properties: Right-click a still in the Gallery and pick Properties. A floating translucent window pops up showing the date the still came into being, which clip supplied it, the moment it was grabbed, plus the source and record timecode readings of the frame it originated from.

### Right-click on a still to choose Still Properties

### Where are Stills Saved?

By default, every grade/still you store lands in the DPX format and goes into the directory path set in the "Gallery stills location" field, which sits inside the Master Settings panel's Working Folders section over in the Project Settings. That path defaults to a hidden ".gallery" directory built at the spot of the first Media Storage Volume you name in the Media Storage panel of the System Preferences window.

### Changing the PowerGrade Still Directory

Optionally, you can shift where PowerGrade stills get stored by opening the Gallery Option menu and choosing Change PowerGrades Path. A "Select PowerGrades Folder" dialog then prompts you to pick a directory where all PowerGrades get stored.

### Live Previews of Gallery Stills

The Live Preview option, found within the Gallery option menu, gives you a preview of how the current clip would appear once a given Gallery Still grade is applied to the currently selected clip, all by gliding the pointer across the still you'd like to preview. Enabling and Disabling the Gallery Live Preview: 1 Open up the Gallery option menu and pick Live Preview.

With the Live Preview option for the Gallery browser, hovering over a saved grade previews it on the current clip inside the Viewer 2 Within the Node Editor, click whichever node you'd like to preview applying the still's grade onto. The live preview reveals how the current clip will look once the grade of the still you pick reaches the currently selected node of the current grade, which shapes the result. 3 Glide the pointer across the still you'd like to preview. The Viewer image refreshes, revealing how that clip would appear with that still's grade reaching the currently selected node.

### Hover Scrub in the Gallery

With Live Preview switched on in the Gallery option menu, the Hover Scrub Preview submenu lets you decide how Live Preview gets shown by a thumbnail in the Gallery, and in the Viewer, as the pointer passes over a still or LUT inside the LUT Browser:

- You can opt to scrub both the thumbnail under your pointer along with the Viewer, which previews the current still's grade or a LUT across the span of the current clip in the thumbnail as well as in the Viewer.
- You can opt to scrub the thumbnail by itself, so the Viewer keeps showing only the grade or LUT across whatever frame the playhead currently sits on.
- You can switch scrubbing off entirely, whereupon the thumbnail and the Viewer both show only the grade or LUT across whatever frame the playhead currently sits on.

The Hover Scrub Preview options when Live Preview is enabled
