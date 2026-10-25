# Different ways of using clip metadata and renaming clips using clip names

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using clip metadata.
[Chapter index](INDEX.md) / [Previous section](media-pool-metadata-import-and-export.md)
<a id="source-different-ways-of-using-clip-metadata"></a> <a id="source-renaming-clips-using-clip-names"></a> <a id="source-switching-between-file-names-and-clip-names"></a> <a id="source-using-metadata-to-define-clip-names"></a>

### Different Ways of Using Clip Metadata

So you'll make the most of the clip metadata tools built into DaVinci Resolve, here's a brief rundown of the numerous ways clip metadata can speed up your work.

- Searching for clips in the Media Pool
- Searching for clips in the Timeline
- Sorting the Media Pool by metadata columns in list view
- Creating Smart Bins in the Edit page
- Creating Timeline Filters in the Color page
- Using Metadata to create clip Clip Names
- Displaying Metadata in frame using the Color page Burn In palette

### Renaming Clips Using Clip Names

The most basic bit of clip metadata is a clip's name, which serves to identify clips almost everywhere they turn up within DaVinci Resolve. Out of the box, clips display the file name of their matching media file on disk. Ever since tapeless recording arrived, though, editors have been saddled with camera original media whose names aren't precisely "human readable." Happily, you can type in a friendlier clip name to use in its place while still holding on to the original file name, which is essential both for keeping the connection between a clip and its media and for tracking how an offline clip links back to the online media it came from. A clip's clip name can be edited in several ways. NOTE: The clip names of timelines, compound clips, and multicam clips can be edited too, letting you keep two naming conventions for those items, one set for creative editing and a separate set for finishing tasks. Use any of these approaches to change a clip's clip name:

- Within the Icon view of the Media Pool, give a clip's name a single click, pause briefly, then click once more to highlight the name, enter a new name, and hit return to confirm it.
- Within the List view of the Media Pool, the Clip Name echoes the file name of the source clip (which stays hidden by default), yet clicking any clip's Clip Name column lets you type a brand-new name from nothing.
- When the List view of the Media Pool has the Clip Name column visible, Option-click that column on a given clip to revise the file name rather than supply a wholly new name.
- To rename multiple clips at once, highlight all the clips whose clip name should change, then right-click any one of them and pick Clip Attributes. In the Clip Attributes window, switch to its Name panel, revise the Clip Name field there, and confirm with OK.

Once you've altered a clip's clip name, that clip shows up in these locations under the clip name rather than the original file name:

- The Media Pool's Thumbnail view
- The name bar of each clip in the Timeline
- The Source Viewer title bar
- The Clip Name field of the Clip Attributes dialog's Name panel

### Switching Between File Names and Clip Names

Because different tasks call for different information, you can flip between showing clip file names and clip names. Finishing editors, for instance, will more often need the file name of each clip, since that makes it simpler to chase down reconforming and relinking issues. Creative editors, by contrast, prefer the more legible clip names so they can locate what they need faster. To switch between file names and clip names:

- Choose View > Show File Names to flip between the two naming conventions.

### Using Metadata to Define Clip Names

If you're a keen user of clip metadata (and you really ought to be), you can drop "metadata variables" into a field that pull in other metadata belonging to that clip. As an example, you might enter the mix of variables and text shown in the following screenshot to build a clip name on its own. Once entered, variables appear as graphical tags with a background behind them, whereas the ordinary text characters you type sit before and after those tags.

A mix of variables and typed text characters used to build a clip name driven by that clip's metadata Consequently, that clip would show "12_A_3" as its name when scene "12," shot "A," and take "3" made up its metadata. Doing this, you're free to blend metadata variables with other characters (such as the underscore in the example above) to shape the metadata so it reads more clearly. Any single item of metadata present in the Metadata Editor can serve as a variable, and a handful of other clip and timeline properties can likewise be referenced through variables, among them the version name attached to a clip's grade, the EDL event number for a clip, and the timeline index number of that clip. Because metadata variables are such a handy way to generate names automatically across many clips, you may prefer to apply metadata variable-driven clip names by selecting every clip you'd like to edit and opening the Clip Attributes window. Editing the Clip Name field within the Name panel lets you assign one clip name to every selected clip in a single step.

When a text field accepts variables, here's how to insert one: 1 Enter the percentage sign (%), and a scrolling list pops up listing every variable on offer. 2 To zero in on a particular variable fast, begin typing the letters of its name, and the list filters itself automatically to display only variables holding the characters you just entered. 3 Pick the variable you want with the Up and Down Arrow keys, then press Return to insert that variable. The variable list that appears when you type the % character The moment you drop one or more metadata variables into a clip's Clip Name column and press Return, the string swaps over to its matching text. To edit the metadata string again, just click inside that column and the metadata variables come back. Note that, on clips where a referenced metadata field is empty, nothing shows up for that metadata variable in the Clip Name column. To remove a metadata variable:

- Click inside a field that uses variables to start editing it, click a variable to select it, then press Delete.

For more on working with variables, plus a full list of every variable on offer in DaVinci Resolve, see Chapter 16, "Using Variables and Keywords."
