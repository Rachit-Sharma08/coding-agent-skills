# Importing media and import media and import folder buttons

Version: DaVinci Resolve 20.3 Reference Manual. Context: Importing and organizing media in the cut page.
[Chapter index](INDEX.md) / [Next section](bin-timeline-import-and-folder-sync.md)
<a id="source-bins-seen-in-the-media-pool"></a> <a id="source-create-bin-with-selected-clips"></a> <a id="source-creating-and-using-bins"></a> <a id="source-importing-and-organizing-media-in-the-cut-page"></a> <a id="source-importing-and-organizing-media-in-the-cut-page-part-1"></a> <a id="source-importing-media"></a> <a id="source-master-bin"></a> <a id="source-opening-bins"></a> <a id="source-organizing-media-into-bins"></a> <a id="source-removing-media"></a> <a id="source-renaming-bins"></a> <a id="source-the-hierarchical-bin-drop-down-menu"></a> <a id="source-the-import-media-and-import-folder-buttons"></a>

### Importing and Organizing Media in the Cut Page

Editing can't begin until you've brought the clips you intend to use for your program into the Media Pool, which acts as your project's central repository of clips. That can take in video, audio, and graphics files of any format DaVinci Resolve supports. After import, the Cut page's Media Pool gives you a host of organizational tools that speed up reaching and sifting your project's media as you track down the clips you need to build your program.

### Importing Media

Sitting atop the Media Pool, two Import buttons open import dialogs you use to pick the media you want to pull into the Media Pool for your project.

### The Import Media and Import Folder buttons

To import individual clips:

1 Do one of the following:

a) Click the Import Media button.

b) Press Command-I.

c) Right-click the Media Pool and choose Import Media.

2 Within the Import dialog, pick one or several clips to import, then click Open. 3 Should a prompt offer to switch the frame rate of an empty project so it matches the incoming media, click Change.

Whatever media you import—be it video, audio, or graphics—shows up as a single clip in the Media Pool. A whole folder of media can also come in as a bin within the Media Pool.

Here's how to bring a whole folder of media in as a bin: 1 Click the Import Media Folder button. 2 Within the Import dialog, pick a folder holding the media you'd like to import, then click Open. 3 Should a prompt offer to switch the frame rate of an empty project so it matches the incoming media, click Change.

Every folder you bring in shows up as a bin inside the Media Pool. Double-click a bin and its contents open into the Media Pool, where you can look over each clip one by one.

TIP: When you want richer media-import options, turn to the Media page, which brings its Media Storage browser along with a fuller-featured take on the Media Pool.

### Removing Media

When a project holds clips you've no further use for, just select them and tap the Delete or Backspace keys. A Dialog checks whether you mean to remove the chosen clip or clips; click Remove and they leave the Media Pool while staying untouched on your media storage device. To clear out every clip in the bin that's currently open (the Master bin included), you can instead right-click anywhere inside the Media Pool and pick Remove All Clips in Bin off the contextual menu.

### Organizing Media into Bins

On short projects, keeping every clip together in one bin (the Master bin being the Media Pool's top level) can be quick. On longer ones, though, splitting your media into clip subsets across separate bins makes browsing each bin's contents through the Viewer's Source Tape easier to handle. TIP: Clips you're sure you won't use—say where the camera rolled on unusable scenery or moments, or takes that are wholly unusable—can be shifted into another bin so they stay out of the Source Tape for the bins that hold the clips you do want.

### Master Bin

The Master bin sits at the top level of your project hierarchy. Every piece of media

content (clips, timelines, graphics, other bins, and so on) for your project lives in the Master bin. On the Cut page, the Master bin

additionally surfaces all of your project's timelines for quick reach, no matter where in

your project they were created.

### Creating and Using Bins

To organize your media you can spin up bins by choosing File > New Bin (Shift-Command-N), or by right-clicking inside the Media Pool and picking New Bin off the contextual menu. Bins can be nested inside other bins, and that lets you arrange the clips you need hierarchically in all sorts of ways.

### Bins seen in the Media Pool

After a bin exists, you can drag and drop one or more selected clips into it, much the way you would on the desktop of your operating system's file manager.

### Opening Bins

Open any bin you can see in the Media Pool by double-clicking it, or by clicking the Bin dropdown at the Media Pool's upper-left corner and picking a bin to open from the menu (those appear as a hierarchical list). Once open, a bin's contents fill the Media Pool, and a path indicator atop the Media Pool reveals how many levels down you've gone wherever you've nested bins within bins. Click any level of that path to climb back up the hierarchy, or grab a different bin from the Bin drop-down.

### The hierarchical Bin drop-down menu

### Create Bin With Selected Clips

Creating a bin and loading clips into it can also happen in a single move. Pick one or several clips in the Media Pool, right-click one of those selected clips, and pick Create Bin With Selected Clips off the contextual menu. A fresh bin titled “Bin X” shows up (with X being the next free number), now holding the clips you'd selected.

### Renaming Bins

Renaming a bin starts with clicking its name once, then clicking a second time slowly (click too quickly and it counts as a “double-click,” which opens the bin); the name then lights up, ready for editing. You can also right-click a bin and pick Rename Bin off the contextual menu, which likewise lights up the bin's name for editing. After you've typed the new name, hit Return (or Enter).
