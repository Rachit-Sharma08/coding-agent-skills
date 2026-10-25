# Whats available in the stills navigator and browse and import timeline grades from other projects

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the gallery.
[Chapter index](INDEX.md) / [Previous section](gallery-options-and-organizing-stills-using-albums.md)
<a id="source-browse-and-import-timeline-grades-from-other-projects"></a> <a id="source-importing-and-exporting-stills"></a> <a id="source-using-and-organizing-memories"></a> <a id="source-whats-available-in-the-stills-navigator"></a>

### What’s Available in the Stills Navigator

A range of content is reachable through the Stills Navigator's hierarchical list. The disclosure triangles sitting to the left of each item in the Stills browser open up that item's contents, and plenty of items hold several nested tiers of content inside, every tier reached by its own disclosure triangle.

Across the Gallery Stills project library every connected project is shown, letting you import those stills DaVinci Resolve looks: A set of predefined grades, sorted by type, that supplies fine examples of the various looks DaVinci Resolve offers. Shipping with DaVinci Resolve, these grades can't be changed. Project Libraries: Every project library on hand turns up in this list. Each one nests its own run of users, projects, and timelines, plus a single nested PowerGrade item per user that reaches the stills saved within. Orphans: A separate directory, set in the Master Settings panel of the Project Settings, stores stills. Delete a project library and the stills that belonged to it are orphaned. Every orphaned still no longer tied to any present project library shows up under the Orphan item in the Stills Navigator.

### Browse and Import Timeline Grades From Other Projects

Through the Gallery window you can view and bring in grades from the timelines of other projects even when those grades were never saved as stills to begin with. Open the Gallery Window, then drive the hierarchical disclosure controls of the Stills panel to expand and choose a particular Project Library > User > Project > Timeline; on the right you'll then find at least three browsable albums: the Stills galleries that got created, the Memories, and, at the very bottom, an album named Timeline Media. Browsing through the Timeline Media album, you can inspect the grades presently applied to every clip in that timeline, which makes copying the ones you want into the current project's Stills album or Memories straightforward. It really pays off when you're on a series and decide you'd like to reuse various grades, looks, adjustments, or fixes drawn from earlier episodes in the one you're on now. Before, you had to recall to save every clip as a still just to browse the grades like this. These days you can browse the Timeline's clips directly instead.

Browsing the timeline grades for another project in the project library

### Importing and Exporting Stills

You can bring still images of assorted graphics formats into the Gallery, which is especially handy when a client hands over reference images they'd like you to work from. Stills can likewise be exported out of the Gallery, ideal for shipping a batch of reference stills to a remote client for sign-off. Either way, you get to decide whether images are imported or exported alongside a LUT. Across both import and export, DaVinci Resolve handles these file formats: DPX, CIN, TIFF, JPEG, PNG, PPM, BMP, and XPM. Bringing in a single still or several at once works this way: 1 On the Gallery's gray backdrop, right-click any open spot. 2 Pick one of these commands:

- Import: Brings in image files together with a corresponding DRX file whenever one sits in the chosen directory.
- Import With Output LUT: Brings in an image plus DRX file and, should a matching LUT file occupy the chosen directory, that as well.

3 Once the Import Stills dialog opens, pick the file type to import from the “Files of type” drop-down menu, navigate to whichever files you need, highlight them, then press Import. Exporting one or more still images runs as follows: 1 Should you want exported Gallery stills to carry any labels you've attached, right-click somewhere in the Gallery background and tick “Use labels on still export” in the contextual menu. 2 Highlight one or several stills in the Gallery.

3 Right-click any one of the highlighted stills and pick from these commands:

- Export: Each chosen still yields a pair of files, namely an image file in whatever format you pick plus a DRX (DaVinci Resolve eXchange) file carrying the grading metadata stored with that Gallery still.
- Export With Display LUT: Provided a Video Monitor Lookup Table is set for the current project within the Color Management panel of the Project Settings, this command writes out the image after it passes through the specified LUT. Alongside it goes a DRX file holding the grading metadata stored with that Gallery still.

4 With the Export Stills dialog open, pick an export file format from the “Files of type” drop-down menu, settle on a location, enter a name in the Save As field, and click Save. Every selected still goes out together with all of its companion files. Every file is prefixed with the name you keyed into the Export Stills dialog, trailed by an underscore, that still's still ID number, plus the file's three-letter extension. To export the grade only (.DRX file) and no image: Normally a still exported from the Gallery yields both an image file and a .drx file carrying that image's grade. To send out only the (.drx) grades from the Color Gallery while skipping the images, you can now right-click a Gallery still or stills and pick Export from the drop-down menu. Then, in the file browser that opens, choose .drx from the file format selector and press export.

### Using and Organizing Memories

Memories and stills carry the same information and can each be split screened, copied, appended, exported, and shown as a node graph exactly like any other still. That said, stills designated as a memory become quicker to reach through keyboard shortcuts. By default Memories stay hidden, yet you can surface them by clicking the Memories button positioned to the right of the Gallery list button at the Gallery's top-left.

Keep frequently used grades in Memories so you can recall them faster The Memories thumbnail display makes it simple to track which stills sit in which memories when you're leaning on several memories to copy grades across a program.

To shuttle stills and memories between each other, take one of these steps:

- Drag a still onto a memory bank.
- Drag a memory into the Gallery.

TIP: Used this way, memories let you ferry stills from one album over to another. To stash the present clip's grade into a memory so it's there later, take one of these steps:

- Choose Color > Memories > Save Memory A–H (Option-1 through 8).
- With the DaVinci Resolve Advanced control panel, hit CRNT on the Search Dial panel, then strike the letter of whichever memory bank you're saving to. The SHIFT UP and SHIFT DOWN buttons let you save to another memory that shares the same button.
- Saving a grade onto a memory that already holds something replaces the earlier memory.

To apply a memory to the current clip in a timeline:

- Right-click a memory and choose Apply Grade.

To clear a memory:

- Right-click a memory, then choose Clear.
